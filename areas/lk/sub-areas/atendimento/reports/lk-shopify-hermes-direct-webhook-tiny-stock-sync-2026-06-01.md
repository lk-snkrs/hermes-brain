# Receipt — LK Shopify → Hermes direct webhook → Tiny local stock sync

Data: 2026-06-01
Área: LK / Atendimento / Operações
Escopo aprovado: Opção B — sem Vercel; usar webhook do Hermes; sem writes em Shopify/Tiny além da alteração aprovada de URL de webhook Shopify; processador local determinístico; SQLite local como mirror.

## Resultado

Ativado o fluxo direto:

```text
Shopify orders/paid|orders/cancelled
→ https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync
→ Hermes webhook adapter
→ processador local /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py
→ leitura Tiny read-only
→ SQLite/ledger local
```

## Mudanças feitas

1. Webhook Hermes ajustado para rota determinística de estoque:
   - Arquivo: `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/webhook.py`
   - Rota com `kind=lk_shopify_tiny_stock_sync_dryrun` não dispara LLM/agent-run.
   - A rota chama diretamente o processador local.
   - A validação usa Shopify HMAC (`X-Shopify-Hmac-Sha256`) no payload bruto.
   - O segredo da rota é passado explicitamente ao processador, sem depender de env global.

2. Registry local de webhooks ajustado:
   - Arquivo: `/opt/data/webhook_subscriptions.json`
   - Rota principal: `lk-shopify-tiny-stock-sync`
   - Eventos: `orders/paid`, `orders/cancelled`
   - Script: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
   - Deliver: `log`
   - Secret alinhado ao `SHOPIFY_WEBHOOK_SECRET` sem exposição de valor.

3. Webhooks reais Shopify atualizados para Hermes direto:
   - `orders/paid` ID `1646886125790`
   - `orders/cancelled` ID `1646886158558`
   - Novo endereço de ambos:
     - `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync`

## Verificações

### Endpoint público Hermes

Teste assinado com HMAC Shopify válido:

- `orders/paid`: HTTP `202`
- `orders/cancelled`: HTTP `202`
- Resposta contém `write_executed: false`
- Processador registrou ledger local.

Teste com assinatura inválida:

- HTTP `401`
- `status: auth_failed`
- `write_executed: false`

### Ledger local

Arquivo:

```text
/opt/data/hermes_bruno_ingest/local_sql/lk_shopify_tiny_stock_sync_dryrun/ledger.ndjson
```

Últimos testes registrados como bloqueados por segurança quando SKU não teve match confiável no Tiny:

- `tiny_no_match`
- `tiny_match_not_high_confidence`

Isso é esperado para dry-run/test payload: falha de lookup não vira estoque inventado e não gera write externo.

### Cron fullsync

Job ativo:

- ID: `c64a0c63b881`
- Nome: `LK Tiny stock local DB daily fullsync`
- Agenda: `20 10 * * *`
- Deliver: `local`
- Script: `lk_tiny_stock_fullsync_watchdog.py`
- Modo: `no-agent`

### Testes

Passaram:

- `/opt/data/scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py`
- `/opt/data/scripts/tests/test_lk_tiny_stock_fullsync_watchdog.py`
- `/opt/data/tests/test_lk_tiny_stock_local_db.py`
- `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`

Suite unittest reportou: `Ran 11 tests ... OK`.

## Garantias operacionais

- Shopify é usado apenas como origem de evento.
- Tiny permanece fonte de verdade de estoque.
- O processador consulta Tiny read-only.
- A atualização de estoque local é snapshot absoluto do Tiny, não delta do evento Shopify.
- Nenhum write em Shopify/Tiny é feito pelo processador.
- O retorno e ledger usam `write_executed: false`.
- Falha de lookup ou match de baixa confiança bloqueia a atualização local daquele item, não assume disponibilidade.

## Próximos pontos recomendados

1. Melhorar o matcher SKU ↔ Tiny para reduzir `tiny_match_not_high_confidence` em produtos reais.
2. Adicionar teste específico do adapter Hermes para rota `kind=lk_shopify_tiny_stock_sync_dryrun` se houver suite do gateway disponível no repo ativo.
3. Quando Lucas aprovar writes Shopify no futuro, criar fase separada com approval packet, snapshot/readback/rollback; não misturar com este dry-run/read-only.
