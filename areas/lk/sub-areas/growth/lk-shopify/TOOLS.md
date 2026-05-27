# TOOLS — LK Shopify Hermes

## Ferramentas/skills obrigatórias

- `hermes-agent`
- `multiempresa-routing-lucas`
- `lk-seo-weekly-improvement`
- `lk-shopify-readonly`
- `seo-page`, `seo-content`, `seo-ecommerce`, `seo-schema`, `seo-geo` quando aplicável
- `verification-before-completion` antes de qualquer conclusão

## Permitido sem aprovação

- Leitura pública do site.
- Leitura autenticada read-only quando credenciais já existirem.
- Shopify Admin GET/query-only.
- GSC/GA4/GMC read-only quando autorizado/conectado.
- Scorecards, relatórios, approval packets, rollback plans.
- Docs no Brain sem segredos.

## Bloqueado sem aprovação atual

- Shopify mutation.
- Theme/dev-theme upload.
- Production publish/merge/deploy.
- GMC/feed/ProductInput/DataSource write.
- Klaviyo/ads/WhatsApp/email/campanha.
- Preço, estoque, desconto, checkout, fulfillment ou cliente.

## Regra de segredo

Token Telegram e credenciais ficam apenas em `.env`/Doppler/profile seguro. Nunca em Brain, PRD, relatório ou resposta Telegram.