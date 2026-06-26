# LK POS pós-compra 30min — ativação canary #147746

Data: 2026-06-10T15:15:39.101276+00:00

## Escopo aprovado
Lucas aprovou no Telegram reativar o fluxo para a nova venda POS `#147746` (Sofia Sartori), após diagnóstico de que o pedido já estava na fila e o número passava validação Evolution (`exists=true`).

## Ações locais
- Reativado `/opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py`:
  - `LIVE_SEND_ENABLED=True`
  - `CANARY_LIMIT=12`
- Justificativa do limite: havia `prior_live_sends=11`; limite 12 abre apenas 1 slot de canary para o job atual.
- Verificação de sintaxe: `py_compile_ok`.
- Execução imediata antes do horário não enviou mensagem: `skipped_future=1`, `sent=0`, `errors=0`.
- Verificador pós-vencimento iniciado em background para rodar após `send_after` do pedido e registrar status sanitizado.

## Estado antes do vencimento
- Pedido: `#147746`
- Job: `248068561fe38d37`
- Status: `scheduled`
- `send_after`: `2026-06-10T15:35:59+00:00`
- `send_executed=false`
- `external_write_executed=false`
- `customer_daily_limit=false`
- `values_printed=false`

## Chatwoot
Observação operacional: o fluxo atual de pós-compra envia via Evolution API / LK Flagship direto; Chatwoot deve ser tratado como inbox/CRM/registro de conversa e futura superfície ideal para atendimento, mas não foi migrado para Chatwoot neste ato.

## Não feito
- Não houve Shopify/Tiny write.
- Não houve alteração de estoque/preço.
- Não houve ativação/migração de Chatwoot/Meta templates.
- Não foram registrados dados sensíveis ou secrets.
