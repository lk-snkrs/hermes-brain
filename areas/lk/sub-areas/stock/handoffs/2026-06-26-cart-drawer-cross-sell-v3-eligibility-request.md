# Handoff — LK-Stock eligibility for cart drawer cross-sell v3

- **Data:** 2026-06-26
- **Origem:** lk-shopify
- **Destino/owner:** `lk-stock` / `[LK] Estoque Loja Física`
- **Status:** aberto — aguardando validação de elegibilidade/estoque pelo LK-Stock
- **Pedido Lucas:** “Seguir” após pergunta se LK-Stock seria usado para entender/validar o cross-sell.
- **Escopo:** validar se os produtos recomendados do mapa cross-sell v3 podem continuar elegíveis para exibição no cart drawer.

## Importante — fronteira de responsabilidade

LK Shopify **não consultou estoque diretamente** em Tiny/Shopify/DB/planilha/cache.

O ranking X→Y continua sendo por probabilidade de cross-sell, não por estoque:

- co-compra no mesmo pedido;
- compra sequencial mesmo cliente em 30/90/180 dias;
- confidence/lift/support/recência;
- curadoria leve para remover pares estatísticos estranhos.

LK-Stock entra **somente como filtro final de elegibilidade**:

- disponível/ok → manter elegível;
- ruptura/não confirmado → bloquear/remover temporariamente;
- divergência Tiny/Shopify → não confirmado e pedir reconciliação.

## Evidência do mapa atual

Arquivo local completo para retomada:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_v3_stock_handoff_handles.json`

Fonte do mapa:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v3_curated_light.json`

Resumo:

| Item | Valor |
|---|---:|
| Source | `v2_public_available_curated_light_v3` |
| Método | `same_order_plus_same_customer_sequential_30_90_180d_aggregate + light quality curation` |
| Janelas sequenciais | `[30, 90, 180]` |
| Anchors X | 22 |
| Recommended Y | 21 |
| Handles únicos X/Y | 30 |
| Regras X→Y | 37 |

## Handles para validação LK-Stock

- `calca-alo-yoga-suit-up-trouser-regular-azul-marinho`
- `calca-alo-yoga-suit-up-trouser-regular-preto`
- `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza`
- `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom`
- `calca-saint-studio-alfaiataria-leve-prega-dupla-preta`
- `camiseta-saint-studio-boxy-supima-breuer-preto`
- `camiseta-saint-studio-classy-suedine-supima-chairs-branco`
- `jason-markk-essential-kit`
- `jason-markk-repel-spray`
- `new-balance-9060-triple-white`
- `slide-nike-mind-001-black-chrome-preto`
- `slide-nike-mind-001-light-bone-bege`
- `slide-nike-mind-001-light-smoke-grey-cinza`
- `slide-nike-mind-001-solar-red-vermelho`
- `tenis-new-balance-9060-angora-sea-salt-bege`
- `tenis-new-balance-9060-black-castlerock-grey-preto`
- `tenis-new-balance-9060-garter-snake-pearl-grey-verde`
- `tenis-new-balance-9060-mushroom-arid-stone-camurca`
- `tenis-new-balance-9060-quartz-grey-cinza`
- `tenis-new-balance-9060-rich-oak-marrom`
- `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza`
- `tenis-new-balance-9060-team-away-grey-cinza`
- `tenis-nike-moon-shoe-sp-jacquemus-medium-brown`
- `tenis-nike-moon-shoe-sp-jacquemus-off-white`
- `tenis-nike-vomero-premium-alabaster-amarelo`
- `tenis-nike-vomero-premium-black-volt-preto`
- `tenis-nike-vomero-premium-flat-stout-marrom`
- `tenis-nike-vomero-premium-white-bright-crimson-branco`
- `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege`

## Regras X→Y para contexto

| X anchor | Y recomendado | score | support 180d | confidence 180d | lift |
|---|---|---:|---:|---:|---:|
| `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | `calca-alo-yoga-suit-up-trouser-regular-preto` | 92.5 | 6 | 0.75 | 30.545 |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | 90.8 | 6 | 1.0 | 64.0 |
| `slide-nike-mind-001-light-smoke-grey-cinza` | `slide-nike-mind-001-black-chrome-preto` | 89.6 | 9 | 0.3462 | 8.615 |
| `slide-nike-mind-001-black-chrome-preto` | `slide-nike-mind-001-light-smoke-grey-cinza` | 87.8 | 8 | 0.3333 | 8.296 |
| `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | `camiseta-saint-studio-boxy-supima-breuer-preto` | 87.6 | 5 | 0.4545 | 67.879 |
| `calca-alo-yoga-suit-up-trouser-regular-preto` | `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | 87.5 | 6 | 0.4 | 25.6 |
| `jason-markk-repel-spray` | `jason-markk-essential-kit` | 87.4 | 12 | 0.3243 | 6.317 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-angora-sea-salt-bege` | 84.4 | 4 | 0.5714 | 36.571 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-garter-snake-pearl-grey-verde` | 78.5 | 3 | 0.4286 | 96.0 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `new-balance-9060-triple-white` | 78.5 | 3 | 0.4286 | 17.455 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-rich-oak-marrom` | 78.5 | 3 | 0.4286 | 17.455 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-rich-oak-marrom` | 84.4 | 4 | 0.5 | 20.364 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 84.4 | 4 | 0.5 | 16.0 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-quartz-grey-cinza` | 84.4 | 4 | 0.5 | 37.333 |
| `tenis-new-balance-9060-team-away-grey-cinza` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 81.2 | 3 | 0.75 | 24.0 |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza` | `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | 81.2 | 3 | 0.75 | 56.0 |
| `slide-nike-mind-001-solar-red-vermelho` | `slide-nike-mind-001-black-chrome-preto` | 81.2 | 3 | 0.6 | 14.933 |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-preta` | `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | 81.2 | 3 | 0.6 | 44.8 |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-preta` | `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza` | 80.7 | 3 | 0.6 | 67.2 |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | `calca-saint-studio-alfaiataria-leve-prega-dupla-preta` | 81.2 | 3 | 0.5 | 56.0 |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza` | 81.2 | 3 | 0.5 | 56.0 |
| `slide-nike-mind-001-light-bone-bege` | `slide-nike-mind-001-light-smoke-grey-cinza` | 81.2 | 3 | 0.5 | 12.444 |
| `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` | `tenis-new-balance-9060-rich-oak-marrom` | 80.7 | 3 | 1.0 | 40.727 |
| `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` | `new-balance-9060-triple-white` | 80.7 | 3 | 1.0 | 40.727 |
| `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` | `tenis-new-balance-9060-quartz-grey-cinza` | 80.7 | 3 | 1.0 | 74.667 |
| `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` | `tenis-new-balance-9060-angora-sea-salt-bege` | 80.7 | 3 | 1.0 | 64.0 |
| `tenis-new-balance-9060-garter-snake-pearl-grey-verde` | `tenis-new-balance-9060-black-castlerock-grey-preto` | 80.7 | 3 | 1.0 | 112.0 |
| `tenis-new-balance-9060-garter-snake-pearl-grey-verde` | `tenis-new-balance-9060-angora-sea-salt-bege` | 80.7 | 3 | 1.0 | 64.0 |
| `tenis-new-balance-9060-garter-snake-pearl-grey-verde` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 80.7 | 3 | 1.0 | 32.0 |
| `tenis-new-balance-9060-black-castlerock-grey-preto` | `tenis-new-balance-9060-angora-sea-salt-bege` | 80.7 | 3 | 0.5 | 32.0 |
| `tenis-new-balance-9060-black-castlerock-grey-preto` | `tenis-new-balance-9060-rich-oak-marrom` | 80.7 | 3 | 0.5 | 20.364 |
| `tenis-new-balance-9060-black-castlerock-grey-preto` | `tenis-new-balance-9060-quartz-grey-cinza` | 80.7 | 3 | 0.5 | 37.333 |
| `tenis-new-balance-9060-black-castlerock-grey-preto` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 80.7 | 3 | 0.5 | 16.0 |
| `tenis-nike-vomero-premium-alabaster-amarelo` | `tenis-nike-vomero-premium-black-volt-preto` | 80.7 | 3 | 0.5 | 22.4 |
| `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` | `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo` | 79.1 | 3 | 0.4286 | 8.0 |
| `tenis-nike-vomero-premium-white-bright-crimson-branco` | `tenis-nike-vomero-premium-flat-stout-marrom` | 78.1 | 3 | 0.4286 | 96.0 |
| `tenis-nike-moon-shoe-sp-jacquemus-off-white` | `tenis-nike-moon-shoe-sp-jacquemus-medium-brown` | 78.0 | 6 | 0.3158 | 7.074 |

## Output esperado do LK-Stock

Entregar tabela agregada, sem PII:

| recommended_handle | status_lk_stock | evidência | ação recomendada |
|---|---|---|---|
| handle | `ok` / `bloquear` / `não_confirmado` / `divergência` | fonte/horário/critério | manter/remover/reconciliar |

Critérios sugeridos:

1. Produto vendável/ativo para o canal online.
2. Sem ruptura operacional crítica.
3. Se houver divergência Tiny vs Shopify/Stock OS, marcar `não_confirmado` e pedir reconciliação.
4. Não ordenar por estoque; só validar elegibilidade.

## Reminder OS loop needed

yes

## Reminder OS owner

`lk-stock`

## Reminder OS next action

Validar os 30 handles únicos do cross-sell v3 e retornar lista de handles elegíveis/bloqueados/não confirmados para LK Shopify aplicar no próximo mapa v4 ou filtro futuro.

## Reminder OS review trigger

Quando LK-Stock retornar a validação, ou em próxima iteração do cart drawer cross-sell.

## Reminder OS evidence

Este handoff + arquivo local `cart_drawer_cross_sell_v3_stock_handoff_handles.json` + receipt do rollout v3/GA4:

- `areas/lk/sub-areas/shopify/receipts/2026-06-25-cart-drawer-cross-sell-v3-ga4-adapter-theme.md`

## Writes externos

Nenhum write externo neste handoff. Sem consulta de estoque direta por LK Shopify.

`values_printed=false`.
