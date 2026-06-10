# Gate B — Tabela local Tiny↔Shopify / Crosswalk runtime preview

> Status: preview/decision packet. Nenhum runtime, webhook, cron ou write externo foi ativado por este documento.

## Pedido Lucas

Lucas lembrou que o agente precisa de uma tabela própria/local como backup operacional porque a API do Tiny demora para responder. A tabela deve facilitar controle, webhook, integração e sincronização total de madrugada.

## Decisão de arquitetura

A base local do `lk-stock` deve ser uma **tabela operacional/cache vivo**, não uma nova fonte final de disponibilidade.

- Fonte final de estoque/pronta entrega: Tiny, depósito `LK | CONTROLE ESTOQUE`.
- Base local: índice rápido de decisão, crosswalk SKU/tamanho, freshness, divergências e fila de saneamento.
- Shopify: superfície de produto/venda/webhook; não é fonte final de estoque.

## Entidades/tabelas necessárias

O schema Gate B atual já possui:

- `products`
- `variants`
- `stock_snapshots`
- `sales_velocity`
- `demand_signals`
- `scores`
- `event_ledger`
- `receipts`

Para o “cruzamento perfeito”, adicionar/fortalecer logicamente:

### 1. `variants` como crosswalk canônico

Campos existentes úteis:

- `provider_variant_id` = Shopify variant id.
- `sku` = Shopify SKU.
- `size` = tamanho Shopify.
- `tiny_codigo` = código Tiny correspondente.
- `mapping_confidence` = confiança do vínculo.
- `source_observed_at` = timestamp da observação.

Extensão recomendada futura:

- `mapping_status`: `matched_exact_sku_stock_resolved`, `tiny_duplicate_exact_code_blocked`, `shopify_variant_tiny_missing`, `tiny_only_shopify_missing`, `stock_missing_deposit`, `stale`.
- `tiny_id`: id Tiny resolvido quando único.
- `shopify_handle`: cópia rápida para auditoria.
- `last_crosswalk_at`: última reconciliação.

### 2. `stock_snapshots` como histórico rápido de saldo

Contrato:

- estoque por SKU/tamanho/fonte/depósito/timestamp;
- freshness: `live`, `cron_diario`, `stale`, `fonte_viva_consultada_agora`;
- nunca afirmar disponibilidade se freshness estiver `stale` ou se crosswalk estiver bloqueado.

### 3. `event_ledger` como trilha de webhook/sync

Contrato:

- todo webhook/cron/backfill gera evento idempotente;
- duplicado vira `ignored`, não recalcula duas vezes;
- falha de fonte vira `failed` e marca freshness `stale` quando aplicável.

### 4. `sku_mapping_issues` ou view derivada

Fila local para saneamento:

- `tiny_duplicate_exact_code_blocked`;
- `shopify_variant_tiny_missing`;
- `tiny_only_shopify_missing`;
- `size_mismatch`;
- `missing_official_deposit`;
- `stale`.

## Fluxo live com webhook

1. Shopify order/product webhook chega no ingresso autorizado.
2. Validar HMAC no Vercel `hermes-webhooks`.
3. Reassinar para Hermes/runner `lk-stock` se aplicável.
4. Normalizar evento.
5. Gravar `event_ledger` com idempotência.
6. Atualizar vendas/produto/variant local.
7. Recalcular score afetado.
8. Não consultar Tiny em massa no webhook se isso gerar lentidão; usar cache local + marcar necessidade de reconciliação quando necessário.
9. Telegram só se houver P0 real, falha de fonte ou aprovação necessária.

## Fluxo madrugada / sincronização total

1. Rodar cron diário em janela aprovada.
2. Fazer backfill/reconcile completo:
   - Shopify variants/produtos ativos;
   - Tiny códigos/estoque por SKU/tamanho no depósito `LK | CONTROLE ESTOQUE`;
   - vendas Shopify 7/30/90;
   - divergências SKU/tamanho/código duplicado.
3. Atualizar crosswalk e stock snapshots.
4. Marcar itens OK como `cron_diario`.
5. Marcar falhas/divergências como bloqueadas/stale.
6. Gerar receipt local.
7. Telegram silent-OK; alertar apenas exceções acionáveis.

## Estado piloto U204LMMC

Artefatos já gerados:

- `areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py`
- `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-20260609T104627Z.json`
- `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-20260609T104627Z.csv`
- `areas/lk/sub-areas/stock/receipts/lk-stock-tiny-shopify-crosswalk-u204lmmc-20260609T104709Z.md`

Achado: tamanho 34 / `U204LMMC-1` bloqueado por duplicidade de código exato no Tiny.

## Próximo passo recomendado

Antes de ativar runtime, implementar localmente o **Gate B.1 — crosswalk table upgrade**:

1. Migrar schema local para registrar `mapping_status`, `tiny_id`, `last_crosswalk_at` e issues.
2. Adaptar `lk_stock_tiny_shopify_crosswalk.py` para gravar na SQLite local, não só CSV/JSON.
3. Rodar em dry-run para `U204LMMC`.
4. Criar teste cobrindo duplicidade Tiny e bloqueio de disponibilidade.
5. Só depois preparar aprovação para cron madrugada / webhook real.

## Frase de aprovação para o próximo passo local/offline

> Aprovo implementar o Gate B.1 local/offline da tabela de crosswalk Tiny↔Shopify, com migração SQLite local, gravação do crosswalk do `U204LMMC`, testes e receipt, sem webhook/cron/runtime real e sem writes Tiny/Shopify.

## Bloqueios mantidos

- Webhook público: não ativado.
- Cron real/madrugada: não ativado.
- Gateway/bot Telegram: não ativado.
- Tiny write: 0.
- Shopify write: 0.
- Compra/transferência/reserva/cliente/fornecedor: 0.
