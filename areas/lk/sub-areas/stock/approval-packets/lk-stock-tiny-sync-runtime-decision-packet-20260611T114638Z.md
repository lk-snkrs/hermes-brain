# Decision packet — LK Stock OS Tiny Sync Runtime

- Run/packet ID: `20260611T114638Z`
- Profile/dono: `[LK] Estoque Loja Física` / `lk-stock`
- Status: **PREPARADO — runtime não ativado**
- Pedido Lucas: seguir após pesquisa de webhook/sync Tiny
- Classificação: production-adjacent runtime decision packet
- Writes externos executados: `0`
- Tiny write: `0`
- Shopify write: `0`
- Webhook/cron novo ativado: `0`
- Secrets impressos: `0`

## 1. Objetivo

Manter a database local Stock OS atualizada com alterações de estoque do Tiny/Olist, preservando Tiny `LK | CONTROLE ESTOQUE` como fonte primária e mantendo a DB local como cache/read model operacional.

## 2. Estado local atual verificado

- DB atual apontada: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260611T023437Z.db`
- Pointer: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- DB local SQLite salva na VPS em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/`
- Linhas atuais em `current_local_stock`: `5191`
- Guardrails atuais: `public_availability_safe=0`, `availability_claim_allowed=0`, `tiny_write=0`, `shopify_write=0`
- Verificação local antes deste packet: `python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'` → `20 tests OK`

## 3. Fontes oficiais Tiny/Olist consultadas

1. **Webhook atualização de estoque**
   - URL doc: `https://www.tiny.com.br/api-docs/api2-webhooks-atualizacao-estoque`
   - Uso: Tiny/Olist envia notificação quando há modificação de estoque para produtos mapeados com a plataforma configurada.
   - Configuração Tiny: Menu → Configurações → Aba E-commerce → Integrações → integração → Aba Webhook → `URL de notificações do estoque`.
   - Confirmação: endpoint precisa retornar HTTP `200`.
   - Retry: até `15` tentativas, delay progressivo aumentando `5 minutos` por tentativa.

2. **Fila de atualizações de estoque**
   - URL doc: `https://www.tiny.com.br/api-docs/api2-produtos-atualizacoes-estoque`
   - Endpoint: `https://api.tiny.com.br/api2/lista.atualizacoes.estoque`
   - Parâmetros: `token`, `dataAlteracao`, `formato=json`, `pagina` opcional.
   - Requer extensão: `API para estoque em tempo real`.
   - Atenção crítica: registros obtidos são removidos da fila/marcados como processados. Precisa checkpoint e ledger antes/depois.

3. **Consulta de estoque por produto**
   - URL doc: `https://www.tiny.com.br/api-docs/api2-produtos-estoque`
   - Endpoint: `https://api.tiny.com.br/api2/produto.obter.estoque.php`
   - Parâmetros: `token`, `id`, `formato=json`.
   - Uso Stock OS: confirmar saldo por depósito, especialmente `LK | CONTROLE ESTOQUE`.

## 4. Runtime proposto — arquitetura segura

### 4.1 Ingress público

- Serviço: `hermes-webhooks` no Vercel.
- Rota proposta: `POST https://hermes-webhooks.lucascimino.com/webhooks/lk-stock/tiny/stock`
- Alias técnico possível: `https://hermes-webhooks.vercel.app/webhooks/lk-stock/tiny/stock`
- Upstream interno: Hermes Gateway/runner do profile `lk-stock` ou runner local equivalente já aprovado.

### 4.2 Payload Tiny esperado — webhook estoque

Campos esperados conforme documentação:

```json
{
  "cnpj": "<cnpj_ou_cpf_conta_olist>",
  "idEcommerce": 123,
  "tipo": "estoque",
  "versao": "1.0.0",
  "dados": {
    "tipoEstoque": "F",
    "saldo": "5.25",
    "idProduto": 123456,
    "sku": "CODIGO-TINY",
    "skuMapeamento": "SKU-ECOMMERCE",
    "skuMapeamentoPai": "SKU-PAI-ECOMMERCE"
  }
}
```

Interpretação Stock OS:

- `dados.idProduto` → chave forte para posterior `produto.obter.estoque.php`.
- `dados.sku` → código/SKU do produto no Tiny/Olist.
- `dados.skuMapeamento` e `dados.skuMapeamentoPai` → ponte com Shopify/e-commerce quando houver mapeamento.
- `dados.tipoEstoque`:
  - `F`: físico;
  - `D`: disponível.
- `dados.saldo` → novo saldo informado pelo webhook, mas para pronta entrega pública a DB deve manter guardrail e/ou reconfirmar fonte viva conforme freshness.

## 5. Schema local proposto

Adicionar/usar tabelas locais append-only na DB Stock OS atual ou em DB runtime profile-scoped:

### `tiny_stock_event_ledger`

- `id` INTEGER PRIMARY KEY
- `received_at_utc` TEXT
- `source` TEXT default `tiny_webhook_stock`
- `event_hash` TEXT UNIQUE
- `cnpj_hash` TEXT — hash, não valor bruto se não necessário
- `id_ecommerce` TEXT
- `tipo` TEXT
- `versao` TEXT
- `tipo_estoque` TEXT
- `tiny_id_produto` TEXT
- `tiny_sku` TEXT
- `sku_mapeamento` TEXT
- `sku_mapeamento_pai` TEXT
- `saldo_payload` REAL
- `payload_json` TEXT
- `processing_status` TEXT — `received`, `applied_local`, `ignored_duplicate`, `blocked_invalid`, `failed_retryable`, `failed_terminal`
- `processing_error` TEXT
- `applied_db_path` TEXT

### `tiny_stock_snapshots`

- `id` INTEGER PRIMARY KEY
- `observed_at_utc` TEXT
- `source` TEXT — `tiny_webhook_stock`, `tiny_lista_atualizacoes_estoque`, `tiny_produto_obter_estoque_full_refresh`
- `tiny_id_produto` TEXT
- `tiny_sku` TEXT
- `sku_mapeamento` TEXT
- `sku_mapeamento_pai` TEXT
- `deposito` TEXT
- `saldo` REAL
- `tipo_estoque` TEXT
- `freshness` TEXT — `webhook_live`, `queue_reconcile`, `full_refresh`, `stale`
- `needs_live_tiny_confirmation` INTEGER default `1`
- `public_availability_safe` INTEGER default `0`
- `availability_claim_allowed` INTEGER default `0`

### `tiny_stock_sync_checkpoint`

- `sync_name` TEXT PRIMARY KEY
- `last_success_at_utc` TEXT
- `last_data_alteracao_requested` TEXT
- `last_page_completed` INTEGER
- `last_status` TEXT
- `last_error` TEXT
- `updated_at_utc` TEXT

## 6. Idempotência e segurança

- Webhook idempotente por hash canônico de payload: `sha256(source + idProduto + sku + skuMapeamento + tipoEstoque + saldo + payload bruto normalizado)`.
- Fila Tiny idempotente por `idProduto + codigo + data_alteracao + saldo + deposito` quando disponível.
- Nunca responder `200` antes de persistir pelo menos o evento bruto no ledger local/upstream.
- Se o processamento local falhar após persistir o ledger, responder erro para retry quando seguro ou marcar `failed_retryable` e acionar reconciliação.
- Não imprimir token Tiny, segredo de webhook, CNPJ completo se não necessário, headers sensíveis ou payload com segredo.
- Se o Tiny não oferecer assinatura/HMAC própria no webhook de estoque, usar URL secreta + validação de allowlist/campo esperado + secret compartilhado no path/header via Vercel quando configurável. Registrar risco residual.

## 7. Sync composto recomendado

### Camada A — Webhook Tiny estoque

- Objetivo: atualização quase real-time.
- Entrada: payload Tiny `tipo=estoque`.
- Ação: gravar ledger + snapshot local + marcar SKU/handle afetado com freshness `webhook_live`.
- Telegram: silent-OK. Alertar só falha repetida, payload inválido recorrente, ou divergência crítica.

### Camada B — Fila `lista.atualizacoes.estoque`

- Objetivo: recuperar eventos perdidos e reconcile leve.
- Cadência proposta: a cada 15–60 minutos ou diário, a definir depois de validar extensão/volume.
- Cuidado: a doc informa que registros obtidos são removidos/marcados como processados.
- Obrigatório: checkpoint transacional antes/depois e arquivo/ledger de payload bruto.

### Camada C — Full Tiny stock refresh

- Objetivo: baseline/reconciliação completa da DB local.
- Cadência inicial proposta: manual ou diário fora de pico; depois semanal se webhook+fila forem estáveis.
- Estimativa atual:
  - resolvidos/consultáveis: `1h30–3h`;
  - todos incluindo bloqueados/identidade: `3h–5h`.
- Guardrail: não libera pronta entrega pública sem freshness suficiente/reconfirmação.

## 8. Secrets/variáveis necessárias — nomes apenas

- `TINY_API_TOKEN_LK` ou nome já usado no Doppler para Tiny LK.
- `LK_STOCK_TINY_WEBHOOK_SECRET` — se usarmos secret compartilhado para rota/proxy.
- `HERMES_WEBHOOKS_UPSTREAM_SECRET` — para Vercel re-assinar chamada ao Hermes runner/gateway.
- `HERMES_GATEWAY_LK_STOCK_ENDPOINT` — se houver upstream gateway.

Nenhum valor deve ser escrito no Brain, logs ou Telegram.

## 9. Testes antes de ativar

Antes de dizer `ativado`, executar e registrar:

1. Unit tests locais Stock OS: `python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'`.
2. Teste de normalização de payload Tiny válido.
3. Teste de idempotência: mesmo payload 2x → 1 evento aplicado, 1 duplicado ignorado.
4. Teste de payload inválido/sem secret → rejeição.
5. Teste de persistência ledger antes de `200`.
6. Teste de atualização local de snapshot sem `public_availability_safe`.
7. Probe HTTP negativo na rota pública sem assinatura/secret → `401` ou `403`.
8. Probe HTTP válido assinado → `200` + evento no ledger.
9. `cronjob list` mostrando apenas jobs aprovados.
10. Readback SQLite com contagem de eventos e guardrails zerados.

## 10. Kill criteria

Pausar/desativar runtime se ocorrer qualquer um:

- >3 falhas consecutivas de processamento Tiny.
- Evento Tiny sem campos essenciais em lote/repetição.
- Divergência entre saldo webhook e `produto.obter.estoque` acima de limiar definido.
- DB local marcada stale por falha de reconcile.
- Rota pública recebendo payloads não autorizados/replay.
- Qualquer risco de write Tiny/Shopify não aprovado.

## 11. Rollback

- Desativar/limpar URL de webhook no Tiny ou apontar para rota disabled.
- Pausar/remover cron específico via `cronjob list` → `cronjob pause/remove`.
- Reverter pointer local para DB anterior: `lk_stock_os_current_variant_promotion_20260611T023437Z.db`.
- Manter ledger para auditoria; não apagar sem backup.
- Zerar/ignorar snapshots com `source` do runtime problemático.

## 12. Fora de escopo mesmo após aprovar este runtime

- Tiny write.
- Shopify inventory/product write.
- Promessa automática de pronta entrega para cliente.
- Compra/transferência/fornecedor.
- Notion/Júlio write.
- Campanha/CRM/WhatsApp/Klaviyo.
- Deduplicação ou saneamento produtivo em Tiny/Shopify.

## 13. Aprovação necessária para ativar

Para ativar runtime real, precisa aprovação explícita e escopada. Frase sugerida:

> Aprovo ativar o Tiny Stock Sync runtime do `lk-stock`, usando `hermes-webhooks` no Vercel na rota `/webhooks/lk-stock/tiny/stock`, com ledger local SQLite, idempotência, secret/HMAC quando disponível, retry/rollback/kill criteria deste packet, Telegram silent-OK e zero writes Tiny/Shopify/fornecedor/cliente/campanha.

Sem essa aprovação, o estado permanece: **packet preparado, runtime não ativado**.
