# Read-only packet — PDP Product Suggestions v3 candidates / Motor LK

- Data/hora: 2026-06-27T10:28:45Z
- Perfil: lk-shopify
- Escopo: análise read-only de candidatos/reason codes para PDP Product Suggestions v3
- Writes externos: 0
- Consulta direta de estoque: não
- Elegibilidade LK Stock: pendente do handoff já registrado
- values_printed=false

## Resumo

- PDPs amostrados: `6`
- PDPs com 2+ candidatos v3 agora: `4`
- PDPs que precisam de mais dado/família/Stock antes de DEV: `2`

## Resultado por PDP

### `bone-aime-leon-dore-saint-george-logo-hat-bege-marrom`

- Produto: Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom — vendor `Aimé Leon Dore`, type `Boné`, product.js HTTP `200`
- Recommendations API HTTP `200`, candidatos brutos `10`
- Curadoria excluída/dedupe: `5` handles
- Cross-sell/co-compra existente: `0` regras
- Decisão: `needs_family_or_stock_handoff_before_theme_write`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| — | — | — | — | sem candidatos suficientes |

Bloqueios relevantes:
- `bone-aime-leon-dore-saint-george-logo-hat-bege-verde` — current_or_curadoria_duplicate
- `camiseta-aime-leon-dore-saint-george-coconut-milk-bege` — cross_type:Boné→Apparel
- `camiseta-aime-leon-dore-saint-george-asphalt-preto` — cross_type:Boné→Apparel
- `camiseta-aime-leon-dore-ald-golf-swing-coconut-milk-off-white` — cross_type:Boné→Camiseta
- `camiseta-aime-leon-dore-postcard-cream-bege` — cross_type:Boné→Apparel

### `air-jordan-1-low-panda-2023`

- Produto: Tênis Nike Air Jordan 1 Low Panda (2023) Preto — vendor `Jordan`, type `Tênis`, product.js HTTP `200`
- Recommendations API HTTP `200`, candidatos brutos `10`
- Curadoria excluída/dedupe: `5` handles
- Cross-sell/co-compra existente: `0` regras
- Decisão: `ready_for_DEV_packet`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| 1 | `air-jordan-1-low-aluminium` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:air-jordan-1-low` |
| 2 | `air-jordan-1-low-unc-2021` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:air-jordan-1-low` |
| 3 | `air-jordan-1-low-black-grey-pink` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:air-jordan-1-low` |
| 4 | `air-jordan-1-low-medium-olive-verde` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:air-jordan-1-low` |

### `tenis-onitsuka-tiger-mexico-66-triple-black-preto`

- Produto: Tênis Onitsuka Tiger Mexico 66 Triple Black Preto — vendor `Onitsuka Tiger`, type `Tênis`, product.js HTTP `200`
- Recommendations API HTTP `200`, candidatos brutos `10`
- Curadoria excluída/dedupe: `4` handles
- Cross-sell/co-compra existente: `0` regras
- Decisão: `ready_for_DEV_packet`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| 1 | `tenis-onitsuka-tiger-mexico-66-slip-on-black-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:mexico-66` |
| 2 | `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:mexico-66` |
| 3 | `tenis-onitsuka-tiger-mexico-66-pure-gold-black-dourado` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:mexico-66` |
| 4 | `tenis-onitsuka-tiger-mexico-66-black-dragon-fruit-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:mexico-66` |

Bloqueios relevantes:
- `medicom-toy-bearbrick-series-48-100-toy-art-blind-box-lacrado` — cross_type:Tênis→Colecionável

### `tenis-new-balance-9060-quartz-grey-cinza`

- Produto: Tênis New Balance 9060 Quartz Grey Cinza — vendor `New Balance`, type `Tênis`, product.js HTTP `200`
- Recommendations API HTTP `200`, candidatos brutos `10`
- Curadoria excluída/dedupe: `0` handles
- Cross-sell/co-compra existente: `4` regras
- Decisão: `ready_for_DEV_packet`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| 1 | `tenis-new-balance-9060-angora-sea-salt-bege` | `cross_sell_aggregate_existing_cart_packet` | `84.4` | `historical_xy, copurchase_or_sequential_aggregate` |
| 2 | `tenis-new-balance-9060-garter-snake-pearl-grey-verde` | `cross_sell_aggregate_existing_cart_packet` | `78.5` | `historical_xy, copurchase_or_sequential_aggregate` |
| 3 | `new-balance-9060-triple-white` | `cross_sell_aggregate_existing_cart_packet` | `78.5` | `historical_xy, copurchase_or_sequential_aggregate` |
| 4 | `tenis-new-balance-9060-rich-oak-marrom` | `cross_sell_aggregate_existing_cart_packet` | `78.5` | `historical_xy, copurchase_or_sequential_aggregate` |

Bloqueios relevantes:
- `jason-markk-essential-kit` — cross_type:Tênis→Manutenção

### `tenis-nike-vomero-premium-black-volt-preto`

- Produto: Tênis Nike Vomero Premium Black Volt Preto — vendor `Nike`, type `Tênis`, product.js HTTP `200`
- Recommendations API HTTP `200`, candidatos brutos `10`
- Curadoria excluída/dedupe: `0` handles
- Cross-sell/co-compra existente: `0` regras
- Decisão: `ready_for_DEV_packet`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| 1 | `tenis-nike-vomero-premium-barely-volt-cinza` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:vomero-premium` |
| 2 | `tenis-nike-vomero-premium-black-sapphire-rose-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:vomero-premium` |
| 3 | `tenis-nike-vomero-premium-realtree-camo-black-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:vomero-premium` |
| 4 | `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` | `recommendations_api_filtered` | `98` | `recommendations_api, same_category, same_vendor, same_family_token:vomero-premium` |

### `jason-markk-repel-spray`

- Produto: None — vendor `None`, type `None`, product.js HTTP `404`
- Recommendations API HTTP `None`, candidatos brutos `0`
- Curadoria excluída/dedupe: `0` handles
- Cross-sell/co-compra existente: `1` regras
- Decisão: `needs_family_or_stock_handoff_before_theme_write`

| rank | handle | source | score | reason_codes |
|---:|---|---|---:|---|
| 1 | `jason-markk-essential-kit` | `cross_sell_aggregate_existing_cart_packet` | `87.4` | `historical_xy, copurchase_or_sequential_aggregate` |

## Interpretação

- O v3 consegue reaproveitar sinais de co-compra/sequência já existentes para alguns anchors, mas essa base ainda é esparsa.
- Para PDPs com Curadoria forte, como ALD hats, o motor precisa deduplicar Curadoria e usar Recommendations API filtrada/família como complemento.
- No Saint George, após bloqueio estrito de cross-type e dedupe da Curadoria, sobraram menos de 2 candidatos fortes; portanto ainda não deve virar patch DEV sem uma fonte de família/curadoria/Stock melhor.
- LK Stock ainda é necessário apenas para contrato de elegibilidade operacional; enquanto não responder, eligibility fica `unknown/pending`, sem promessa de disponibilidade.
- Nenhum dado de estoque bruto, cliente, pedido individual ou secret foi consultado/imprimido.

## Próximo approval packet DEV

Só preparar patch DEV depois de:

1. retorno/handoff do LK Stock sobre elegibilidade;
2. reforço de fonte de família/Curadoria para acessórios, especialmente ALD hats;
3. decisão se v3 entra primeiro como JSON/asset estático ou lógica client-side incremental sobre v2;
4. QA de não duplicar Curadoria LK e não cruzar categoria ruim.