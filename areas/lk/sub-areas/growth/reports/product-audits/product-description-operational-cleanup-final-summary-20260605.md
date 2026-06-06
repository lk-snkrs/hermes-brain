# LK — resumo final da limpeza de descrições de produto

- Data: 2026-06-05
- Escopo: Shopify `product.descriptionHtml` / REST `body_html`.
- Objetivo: remover linguagem operacional indevida de descrições editoriais e manter comunicação premium/neutra.
- Aprovação: Lucas autorizou continuidade com “seguir” no turno atual.

## QA final GraphQL/Admin

- Total de produtos auditados: 2331
- Promessa `envio em 2 dias`: 0
- `Produtos em estoque`: 0
- `Estoque próprio: envio`: 0
- `Pronta entrega`: 0
- `Entrega SP / Envio SP`: 0
- `roda/rodar/rodam`: 0
- Frase neutra nova presente: 2233

## Preservado por guardrail

- `Sujeito a encomenda`: 8 ocorrências mantidas.
- `sob encomenda`: 2239 ocorrências mantidas.
- Motivo: não mexer na mensagem/campo operacional de encomenda nem nos sinais de disponibilidade/prazo quando fazem parte do atendimento.

## Não alterado

- Preço, estoque, variantes, SKUs, inventoryPolicy, tags, SEO, theme, checkout, GMC, campanhas, Klaviyo e mensagens externas.

## Receipts/rollback

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/product-description-cleanup-all-remaining-20260605T172042Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/product-description-cleanup-all-remaining-resume-20260605T173148Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/product-description-prazo-operational-variants-resume-20260605T175721Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/product-description-prazo-final-faq-cleanup-20260605T180753Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/product-description-prazo-final-one-residual-rest-20260605T181107Z`

## Evidência QA

- QA final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/product-audits/final-description-qa-graphql-20260605T181343Z`

## Revisão de impacto recomendada

- Janela: em aproximadamente 7 dias.
- Métricas: PDP sessions, add_to_cart rate, checkout_started, conversion rate, revenue por PDP/coleção, GSC impressions/clicks/CTR das páginas alteradas, e eventuais tickets/perguntas sobre prazo.
