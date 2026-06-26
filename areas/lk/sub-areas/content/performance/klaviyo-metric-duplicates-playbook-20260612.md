# Playbook LK Content — Klaviyo metric duplicates / ecommerce tracking

Data: `2026-06-12`
Origem: LK Growth read-only QA de Klaviyo.
Modo: documentação interna. Nenhum write externo. `values_printed=false`.

## Regra operacional

Ao ler métricas do Klaviyo para newsletter, campanha, flow ou post-mortem, **não deduplicar métricas apenas pelo nome**.

A conta LK tem métricas duplicadas com o mesmo `name`, mas de integrações/criações diferentes. Se o script escolher a “primeira” métrica por nome, pode cair em métricas API novas/zeradas e gerar falso diagnóstico de que ecommerce está sem evento.

## Mapeamento seguro para relatórios LK Content

Usar preferencialmente:

- `Received Email` → integração `Klaviyo`.
- `Opened Email` → integração `Klaviyo`.
- `Clicked Email` → integração `Klaviyo`.
- `Placed Order` → integração `Shopify`.
- `Added to Cart` → integração `Shopify`.
- `Active on Site` → métrica API legada com volume; validar por `metric_id`/`created`, não só por nome.
- `Viewed Product` → métrica API legada com volume; validar por `metric_id`/`created`, não só por nome.
- `Started Checkout` → validar contra Shopify/GA4 antes de usar como verdade de funil, porque apareceu como API com poucos únicos.

## Achado verificado em 2026-06-12

Janela consultada: 2026-06-05 a 2026-06-12 UTC.

- Email engagement tinha volume normal.
- Ecommerce **não estava zerado** na métrica correta:
  - `Placed Order` / Shopify: 100 eventos / 95 únicos.
  - `Added to Cart` / Shopify: 216 eventos / 123 únicos.
  - `Active on Site` / API legado: 723 eventos / 566 únicos.
- O zero anterior vinha de métricas duplicadas zeradas:
  - `Placed Order` / API criado em 2025.
  - `Added to Cart` / API criado em 2025.
  - `Active on Site` / API criado em 2026.

## Como escrever leitura executiva

Correto:

> Klaviyo mostra abertura/clique e também eventos ecommerce quando filtrado pela métrica/integração correta. Ainda assim, usar Shopify/GA4 como fonte de verdade para receita e conversão; Klaviyo é sinal auxiliar/CRM.

Evitar:

> Klaviyo está com compras/carrinhos zerados.

Só dizer isso se todas as métricas candidatas por nome + integração + created/metric_id estiverem zeradas e reconciliadas contra Shopify/GA4.

## Checklist antes de post-mortem ou decisão CRM

1. Listar todas as métricas candidatas por `name`.
2. Registrar `integration`, `created` e `metric_id` no output interno sanitizado.
3. Agregar por métrica correta, não por nome único.
4. Comparar sinais comerciais com Shopify/GA4 antes de causalidade.
5. Nunca alterar flow, campanha, snippet, integração ou Shopify sem aprovação explícita atual.

## Artefatos relacionados

- LK Growth QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/measurement/klaviyo-tracking-qa-20260612.md`
- Script LK Growth ajustado: `/opt/data/profiles/lk-growth/scripts/lk_klaviyo_readonly_analytics.py`

## Non-actions

- Não alterado: Klaviyo externo, campanhas, flows, segmentos, profiles, Shopify, GMC, Ads, WhatsApp/e-mail ou checkout.
- Não impresso: tokens, API keys, secrets ou payloads sensíveis.
