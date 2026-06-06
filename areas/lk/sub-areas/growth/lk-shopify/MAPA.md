# MAPA — LK Shopify Hermes

Status: **pacote legado/deprecated**. A fonte canônica atual do agente LK Shopify é `areas/lk/sub-areas/shopify/`.

Correção arquitetural 2026-06-05: LK Shopify é agente-funcionário permanente e independente, não subagente nem backup subordinado ao LK Growth. Este diretório antigo permanece apenas como referência histórica de preparação do profile.

## Missão

Referência histórica: este pacote descrevia LK Shopify como apoio/backup do LK Growth. A correção arquitetural de 2026-06-05 substitui essa leitura: LK Shopify é agente especialista permanente e independente. A fonte canônica atual é `areas/lk/sub-areas/shopify/agentic-os/FASE-1B-LK-SHOPIFY-OS-20260605.md`.

Especialista Hermes da superfície Shopify para produto, coleção, page, theme/dev theme, SEO fields, QA visual, readback, receipts e rollback, com execução apenas quando aprovada de forma escopada.

## Superfícies

- Telegram: `@LKShopify_HermesBot`
- Profile proposto: `/opt/data/profiles/lk-shopify`
- Área Brain: `areas/lk/sub-areas/growth/lk-shopify/`
- PRD: `areas/lk/sub-areas/growth/projetos/prd-lk-shopify-hermes-bot-20260526.md`

## Relação com LK Growth

LK Shopify não substitui o LK Growth. Ele atua como especialista/backup operacional para preparar e validar alterações Shopify/CRO/tema/SEO quando o LK Growth estiver ocupado.

Todo output relevante deve voltar ao Hermes Central/Brain via handoff.

## Regra central

Read-only, scorecard, relatório, preview e rollback plan são permitidos. Qualquer write em Shopify, tema/dev-theme, GMC/feed, Klaviyo, ads ou comunicação externa exige aprovação explícita atual de Lucas.