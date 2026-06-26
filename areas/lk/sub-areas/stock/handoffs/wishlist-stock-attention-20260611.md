# Handoff LK Stock — Wishlist stock attention — 2026-06-11

Origem: LK Shopify / Wishlist Pulse SWYM read-only.

Motivo: produtos com desejo em wishlist e sinal Shopify de baixa/zero disponibilidade. Shopify é apenas sinal; Tiny/LK Stock é a fonte de verdade para estoque/pronta entrega.

Ação pedida ao lk-stock: validar Tiny/loja física/grade antes de qualquer comunicação de back-in-stock, baixa disponibilidade ou pronta entrega.

Relatório origem: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/wishlist/wishlist-pulse-2026-06-11.json`

## Top itens para validação

### 1. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
- Favoritos SWYM/social count: 22
- Valor potencial estimado: R$ 52.799,78
- Sinal Shopify totalInventory: -14
- Sinal Shopify variantes disponíveis: 15
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo

### 2. Tênis Onitsuka Tiger Mexico 66 Birch Peacoat Bege
- Favoritos SWYM/social count: 17
- Valor potencial estimado: R$ 40.799,83
- Sinal Shopify totalInventory: -5
- Sinal Shopify variantes disponíveis: 14
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-brich-peacoat-bege

### 3. Tênis Nike Vomero Premium x Melitta Baumeister Total Orange Laranja
- Favoritos SWYM/social count: 12
- Valor potencial estimado: R$ 59.999,88
- Sinal Shopify totalInventory: -1
- Sinal Shopify variantes disponíveis: 12
- URL: https://lksneakers.com.br/products/tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja

### 4. Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza
- Favoritos SWYM/social count: 12
- Valor potencial estimado: R$ 38.399,88
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 16
- URL: https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza

### 5. Boné 5 Panel Aimé Leon Dore Unisphere Branco
- Favoritos SWYM/social count: 6
- Valor potencial estimado: R$ 5.999,94
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 1
- URL: https://lksneakers.com.br/products/bone-5-panel-aime-leon-dore-unisphere-branco

### 6. Tênis Nike Vomero Premium Flat Stout Marrom
- Favoritos SWYM/social count: 5
- Valor potencial estimado: R$ 29.999,95
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 13
- URL: https://lksneakers.com.br/products/tenis-nike-vomero-premium-flat-stout-marrom

### 7. Tênis Nike Vomero Premium White Bright Crimson Branco
- Favoritos SWYM/social count: 5
- Valor potencial estimado: R$ 19.999,95
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 10
- URL: https://lksneakers.com.br/products/tenis-nike-vomero-premium-white-bright-crimson-branco

### 8. Tênis New Balance 9060 Mushroom Arid Stone Bege
- Favoritos SWYM/social count: 5
- Valor potencial estimado: R$ 13.499,95
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 12
- URL: https://lksneakers.com.br/products/tenis-new-balance-9060-mushroom-arid-stone-camurca

### 9. Tênis Onitsuka Tiger Mexico 66 SD Birch Metropolis Bege
- Favoritos SWYM/social count: 5
- Valor potencial estimado: R$ 12.499,95
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 15
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-sd-birch-metropolis-bege

### 10. Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom
- Favoritos SWYM/social count: 5
- Valor potencial estimado: R$ 11.999,95
- Sinal Shopify totalInventory: -1
- Sinal Shopify variantes disponíveis: 11
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-beige-grass-green-marrom

### 11. Tênis Nike Air Jordan 1 Retro High Fragment Design x Travis Scott Couro Branco Azul
- Favoritos SWYM/social count: 4
- Valor potencial estimado: R$ 143.999,96
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 12
- URL: https://lksneakers.com.br/products/tenis-air-jordan-1-retro-high-fragment-design-x-travis-scott-couro-branco-e-azul

### 12. Tênis Nike Travis Scott Air Jordan 4 Retro Cactus Jack Azul
- Favoritos SWYM/social count: 4
- Valor potencial estimado: R$ 59.999,96
- Sinal Shopify totalInventory: 0
- Sinal Shopify variantes disponíveis: 7
- URL: https://lksneakers.com.br/products/tenis-travis-scott-air-jordan-4-retro-cactus-jack-nubuck-azul-6

## Guardrails

- Não foi enviada comunicação para cliente.
- Não foi prometida disponibilidade.
- Não foi alterado estoque/preço/produto/coleção.
- Qualquer campanha `voltou ao estoque` ou `últimas unidades` depende de retorno do lk-stock/Tiny.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/wishlist-stock-attention-20260611.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/lk/sub-areas/stock/handoffs/wishlist-stock-attention-20260611.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
