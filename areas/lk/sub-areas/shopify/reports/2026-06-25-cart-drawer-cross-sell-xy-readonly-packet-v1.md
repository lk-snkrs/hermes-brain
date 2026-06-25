# Read-only packet v1 — Cart drawer cross-sell X→Y

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** cart drawer `cart-drawer__upsell-inner`
- **Status:** análise read-only v1 concluída, mas **superseded pela v2** porque Lucas corrigiu que compra sequencial deve usar janelas 30/90/180 dias. **Não usar v1 para implementação.** Nenhum write Shopify/GitHub/theme executado.
- **PII:** nenhum dado de cliente/pedido individual salvo ou impresso. Uso de customer/order IDs ficou somente em memória durante agregação; output persistido é agregado por handle/modelo.
- **Correção de Lucas:** ranking deve ser possibilidade de cross-sell: cliente comprou/colocou X → tem % de chance de comprar Y.

## Método v1

Combina duas evidências agregadas:

1. **Mesmo pedido:** produtos X e Y comprados juntos.
2. **Sequencial 30 dias:** mesmo cliente comprou X e depois Y em até 30 dias, agregado sem PII.

Métricas:

- `support_total`: evidências agregadas X→Y.
- `same_order_support`: compras juntas no mesmo pedido.
- `sequential_30d_support`: compra posterior em até 30 dias.
- `confidence`: chance agregada X→Y dentro das exposições observadas.
- `lift`: quanto Y aparece com X acima do acaso.
- `score`: score operacional v1 para ordenar candidates.

## Resumo de dados

| Métrica | Resultado |
|---|---:|
| Pedidos escaneados | 2000 |
| Pedidos válidos agregados | 1691 |
| Clientes com 2+ pedidos | 149 |
| Cestas com 2+ produtos | 448 |
| Produtos únicos | 698 |
| Regras X→Y com support ≥ 2 | 230 |
| Handles com regra candidata support ≥ 3 e score ≥ 78 | 27 |
| Regras candidatas no mapa v1 | 46 |

## Top regras X→Y v1

| X | Y | Support | Mesmo pedido | Seq. 30d | Confidence | Lift | Score |
|---|---|---:|---:|---:|---:|---:|---:|
| `jason-markk-essential-kit` | `jason-markk-repel-spray` | 12 | 12 | 0 | 0.4615 | 6.462 | 100.0 |
| `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | `calca-alo-yoga-suit-up-trouser-regular-preto` | 6 | 6 | 0 | 0.7500 | 30.545 | 92.5 |
| `slide-nike-mind-001-light-smoke-grey-cinza` | `slide-nike-mind-001-black-chrome-preto` | 9 | 7 | 2 | 0.3750 | 9.333 | 92.5 |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | 6 | 3 | 3 | 1.0000 | 64.000 | 90.8 |
| `jason-markk-repel-spray` | `jason-markk-essential-kit` | 12 | 12 | 0 | 0.3529 | 6.875 | 90.3 |
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `air-jordan-1-low-gs-se-concord` | 6 | 0 | 6 | 0.6667 | 298.667 | 89.1 |
| `slide-nike-mind-001-black-chrome-preto` | `slide-nike-mind-001-light-smoke-grey-cinza` | 8 | 7 | 1 | 0.3333 | 8.296 | 87.8 |
| `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | `camiseta-saint-studio-boxy-supima-breuer-preto` | 5 | 3 | 2 | 0.4545 | 67.879 | 87.6 |
| `calca-alo-yoga-suit-up-trouser-regular-preto` | `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | 6 | 6 | 0 | 0.4000 | 25.600 | 87.5 |
| `jason-markk-premium-suede-cleaning-kit-kit-de-suede` | `jason-markk-repel-spray` | 4 | 4 | 0 | 0.8000 | 11.200 | 85.0 |
| `jason-markk-ready-to-use-foam-cleaner` | `jason-markk-repel-spray` | 4 | 4 | 0 | 0.8000 | 11.200 | 85.0 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-angora-sea-salt-bege` | 4 | 3 | 1 | 0.5714 | 36.571 | 84.4 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-rich-oak-marrom` | 4 | 3 | 1 | 0.5000 | 20.364 | 84.4 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 4 | 3 | 1 | 0.5000 | 16.000 | 84.4 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-quartz-grey-cinza` | 4 | 3 | 1 | 0.5000 | 37.333 | 84.4 |

## Regras por modelo/silhueta

| Modelo X | Modelo Y | Support | Confidence |
|---|---|---:|---:|
| `adidas-spezial` | `adidas-samba` | 2 | 1.0000 |
| `adidas-samba` | `onitsuka-tiger-mexico-66` | 12 | 0.4138 |
| `air-jordan-1` | `new-balance-9060` | 5 | 0.3125 |
| `new-balance-530` | `onitsuka-tiger-mexico-66` | 3 | 0.2500 |
| `new-balance-530` | `new-balance-9060` | 2 | 0.1667 |
| `adidas-samba` | `new-balance-9060` | 4 | 0.1379 |
| `new-balance-9060` | `onitsuka-tiger-mexico-66` | 9 | 0.1364 |
| `air-jordan-1` | `onitsuka-tiger-mexico-66` | 2 | 0.1250 |
| `nike-slide-mind` | `onitsuka-tiger-mexico-66` | 4 | 0.1212 |
| `onitsuka-tiger-mexico-66` | `adidas-samba` | 12 | 0.0916 |
| `new-balance-9060` | `air-jordan-1` | 5 | 0.0758 |
| `adidas-samba` | `adidas-spezial` | 2 | 0.0690 |

## Candidate map local

Arquivo gerado:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v1.json`

Critérios do candidate map:

- `support_total >= 3`;
- `score >= 78`;
- até 4 recomendações por handle;
- sem PII;
- exclui item atual no runtime do drawer.

## Interpretação

A v1 já mostra padrões reais e melhores que `best-selling` genérico:

- kits/produtos complementares: `jason-markk-essential-kit` ↔ `jason-markk-repel-spray`;
- variações compradas juntas: `Nike Mind 001`, `Alo Suit Up`, `New Balance 9060`;
- pares de modelo/silhueta úteis para fallback: `adidas-samba → onitsuka-tiger-mexico-66`, `new-balance-530 → onitsuka-tiger-mexico-66`, `air-jordan-1 → new-balance-9060`.

Mas há ressalva importante: várias regras ainda são pares de variações/cor do mesmo produto/modelo. Isso pode ser bom para alguns casos, mas o cart drawer precisa decidir se queremos:

1. **mesma família/modelo**: outra cor/modelo parecido; ou
2. **complementar real**: cleaner, spray, meia, outro item complementar; ou
3. **híbrido**: primeiro cross-sell real; se não houver, mesma silhueta/modelo.

## Recomendação para implementação DEV

Implementar uma versão segura híbrida:

```text
cart item X
→ by_handle[X] com support>=3/score>=78
→ excluir X e itens já no carrinho
→ validar produto publicável/comprável via products.json
→ renderizar até 4
→ fallback by_model[model(X)] se não houver by_handle
→ se ainda não houver, esconder bloco
```

Título recomendado:

- `Também compram com este produto`

Não usar:

- `/collections/all`;
- margem/valor;
- prioridade de estoque como score;
- lista fixa manual sem evidência.

## Próxima decisão

Se Lucas aprovar, próximo passo é preparar DEV com:

1. novo asset/JSON ou objeto JS agregado com `cart_drawer_cross_sell_candidate_map_v1`;
2. alteração em `snippets/lk-cart-drawer.liquid` para consumir X→Y;
3. readback DEV;
4. QA com produtos que têm regra e produtos sem regra;
5. approval/merge Production só depois de DEV aprovado.

## Rollback

- Remover o mapa X→Y do snippet/asset;
- manter estado atual do PR #99: sem fallback `/collections/all`, escondendo se não houver regra.

## Writes externos

0. Apenas leitura Shopify Admin agregada. `values_printed=false`.
