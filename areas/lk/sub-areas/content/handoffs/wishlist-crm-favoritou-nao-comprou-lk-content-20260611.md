# Handoff para LK Content — Wishlist CRM “Favoritou e não comprou” — 2026-06-11

Origem: LK Shopify / Wishlist OS Fase 1.1.

## Pedido do Lucas

Lucas aprovou seguir com o pacote 2/CRM e pediu usar o agente `LK Content`.

## Objetivo

Criar conceito/copy premium para campanha ou flow draft “favoritou e não comprou”, usando sinais de wishlist como intenção, sem desconto inicial e sem urgência falsa.

## Escopo permitido agora

- Copy e variações de assunto/preheader/body/CTA.
- Brief criativo/editorial.
- Preview textual/visual interno.
- Recomendações de segmentação e frequency cap em nível de proposta.

## Bloqueios

- Não enviar campanha.
- Não ativar flow.
- Não criar/editar Klaviyo/SWYM sem aprovação explícita.
- Não usar estoque como promessa.
- Não usar back-in-stock/últimas unidades sem retorno de `lk-stock`/Tiny.

## Produtos semente

### 1. Tênis Nike Travis Scott x Air Jordan 1 Low OG SP 'Black Phantom' Preto
- Família: Air Jordan 1
- Favoritos: 6
- Potencial estimado: R$ 71.999,94
- Vendas 90d Shopify: 1 un.
- URL: https://lksneakers.com.br/products/travis-scott-x-air-jordan-1-low-og-sp-black-phantom

### 2. Tênis Alo Yoga ALO Runner Espresso Marrom
- Família: Alo Yoga
- Favoritos: 6
- Potencial estimado: R$ 14.399,94
- Vendas 90d Shopify: 2 un.
- URL: https://lksneakers.com.br/products/tenis-alo-yoga-alo-runner-espresso-marrom

### 3. Tênis On Running Cloudsolo Loewe White Light Grey Cinza
- Família: Loewe / On Running
- Favoritos: 5
- Potencial estimado: R$ 49.999,95
- Vendas 90d Shopify: 1 un.
- URL: https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-white-light-grey-cinza

## Direção de copy recomendada

- Tom: humano, premium, baixo atrito.
- Sem cupom na primeira versão.
- Sem “últimas unidades”/“acabando” até validação de estoque.
- Evitar linguagem operacional: wishlist social count, bucket, SKU, Tiny, estoque negativo.
- CTA sugerido: `Ver meu favorito` ou `Voltar ao produto`.

## Copy seed

Assunto: `Seu favorito ainda está por aqui`

Preheader: `Você salvou este produto na sua lista. Se ainda estiver pensando nele, ele continua por aqui na LK.`

Corpo:

`Você salvou este produto entre os seus favoritos. Se ele ainda está no seu radar, deixamos o caminho direto para você voltar a ver detalhes, tamanhos e fotos na LK.`

CTA: `Ver meu favorito`

## Fonte de evidência

- Ações Fase 1.1: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/wishlist/wishlist-phase-1-1-actions-2026-06-11.json`
- PDP/CRO audit read-only será salvo em relatório paralelo por LK Shopify.

## Não-ações executadas

- 0 Klaviyo writes.
- 0 SWYM writes.
- 0 sends.
- 0 Shopify writes.
- 0 estoque/preço/produto/tema/app.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: waiting_event; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/content/handoffs/wishlist-crm-favoritou-nao-comprou-lk-content-20260611.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Content / profile lk-content
- Reminder OS next action: Produzir somente copy/brief/preview interno para wishlist CRM; não enviar nem ativar Klaviyo/SWYM sem aprovação explícita.
- Reminder OS review trigger: Revisar quando Lucas pedir pacote CRM ou antes de qualquer Klaviyo/SWYM/customer-facing write.
- Evidence: areas/lk/sub-areas/content/handoffs/wishlist-crm-favoritou-nao-comprou-lk-content-20260611.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
