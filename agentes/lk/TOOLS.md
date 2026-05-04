# TOOLS — Agente LK

## Fontes principais

- Supabase LK: `SUPABASE_LK_URL`, `SUPABASE_LK_SERVICE_KEY`
- Shopify LK: `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_STORE`, `SHOPIFY_STORE_URL`
- Klaviyo: `KLAVIYO_API_KEY`
- Meta Ads: `META_ACCESS_TOKEN`, `META_ADS_ACCOUNT_ID`
- GA4/GSC quando aplicável
- Judge.me, Tiny, Frenet, Metricool quando necessário
- Evolution API/Clo para envios aprovados

## Regras

- Usar Doppler para buscar valores sob demanda.
- Nunca salvar secret value no Brain.
- Para estoque, preço, pedido e cliente: consultar fonte viva.
- Para campanha/envio: gerar preview e aguardar aprovação Lucas.
