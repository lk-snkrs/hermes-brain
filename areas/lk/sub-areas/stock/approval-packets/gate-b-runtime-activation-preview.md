# Gate B — Runtime Activation Preview

> **Status:** preview only. Sem aprovação explícita atual, nada abaixo deve ser ativado.

## Escopo proposto

Ativar, em etapa futura separada, a base local do `lk-stock` com:

- webhook público para eventos autorizados;
- cron diário real de reconciliação;
- receipts de falha/divergência/P0;
- Telegram silent-OK: só P0, falha de fonte ou aprovação necessária.

## Rotas/eventos propostos

- `POST /webhooks/lk-stock/shopify/order-paid` — venda paga Shopify, read-only.
- `POST /webhooks/lk-stock/shopify/product-update` — produto/variante Shopify, read-only.
- `POST /webhooks/lk-stock/tiny/stock-snapshot` — snapshot de estoque Tiny autorizado, read-only.

Ingress público preferencial: `hermes-webhooks` no Vercel.

## Fontes e escopos

- Tiny / `LK | CONTROLE ESTOQUE`: fonte final para disponibilidade.
- Shopify: contexto de produto/venda, não estoque final.
- Base local: cache/índice operacional, não fonte final.

## Secrets necessários — nomes, sem valores

- `SHOPIFY_WEBHOOK_SECRET_LK`
- `TINY_API_TOKEN_LK_READONLY` ou equivalente autorizado
- `HERMES_WEBHOOK_RESIGN_SECRET_LK_STOCK`
- `LK_STOCK_LOCAL_DB_PATH`

## Cadência proposta do cron diário

- 1 vez por dia em janela de baixo ruído operacional.
- Telegram: silencioso quando OK.
- Falha de fonte: marcar `stale`, gerar receipt e alertar somente se bloqueia decisão/ação.

## Kill criteria

Desativar/parar imediatamente se:

- validação HMAC falhar de forma repetida;
- evento duplicado furar idempotência;
- base local tentar escrever em Tiny/Shopify;
- freshness ficar `stale` e ainda assim algum output afirmar disponibilidade;
- Telegram gerar ruído de OK/fallback benigno.

## Rollback

1. Pausar webhook/cron.
2. Manter base local como evidência read-only.
3. Marcar todos os snapshots como `stale`.
4. Voltar para Gate A/manual read-only com Tiny/fonte viva consultada sob demanda.

## Verificação antes de ativar

- Testes offline passam.
- Fixture webhook duplicada resulta em `ignored` por idempotência.
- Cron dry-run sucesso marca `cron_diario`.
- Cron dry-run falha marca `stale` e gera receipt local.
- Query A1 com `stale` declara “não confirmado”.
- Writes externos executados: `0`.

## Frase exata de aprovação futura

> Aprovo ativar o runtime real do Gate B do `lk-stock`, usando `hermes-webhooks` no Vercel para os eventos listados e cron diário read-only, com HMAC, idempotência, kill criteria, rollback acima, Telegram silent-OK e zero writes Tiny/Shopify/fornecedor/cliente/campanha.

## Runtime ativado agora

Nenhum.

## Writes externos agora

0.
