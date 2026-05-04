# Rotina — LK Morning Briefing

## Objetivo
Enviar resumo diário de desempenho LK com dados reais.

## Área dona
LK / Operações comerciais

## Fontes
Supabase LK, Shopify, scripts atuais do Hermes Brain.

## Regra Hermes
Não afirmar faturamento, pedidos, ticket ou anomalias sem consultar fonte viva.

## Doppler keys
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`
- `SHOPIFY_ACCESS_TOKEN` se consultar Shopify

## Verificação
Checar se o comando exato do cron funciona e se os dados estão frescos.
