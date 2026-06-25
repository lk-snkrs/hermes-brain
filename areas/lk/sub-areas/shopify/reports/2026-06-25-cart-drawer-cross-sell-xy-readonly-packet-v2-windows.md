# Read-only packet v2 — Cart drawer cross-sell X→Y com janelas 30/90/180

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** cart drawer `cart-drawer__upsell-inner`
- **Status:** análise read-only corrigida conforme Lucas; **nenhum write Shopify/GitHub/theme executado**.
- **Correção de Lucas:** compra sequencial X→Y deve usar janelas **30/90/180 dias**, não apenas 30 dias.
- **PII:** nenhum dado de cliente/pedido individual salvo ou impresso. IDs foram usados apenas em memória para agregação; output persistido é agregado por handle/modelo.

## Método v2 corrigido

Evidências agregadas:

1. **Mesmo pedido:** X e Y no mesmo pedido.
2. **Sequencial 30 dias:** cliente comprou X e depois Y em até 30 dias.
3. **Sequencial 90 dias:** cliente comprou X e depois Y em até 90 dias.
4. **Sequencial 180 dias:** cliente comprou X e depois Y em até 180 dias.

Como 30 ⊂ 90 ⊂ 180, o score usa `weighted_support` para não inflar artificialmente a mesma evidência:

```text
weighted_support = same_order
                 + 0.70 * seq_30
                 + 0.45 * (seq_90 - seq_30)
                 + 0.25 * (seq_180 - seq_90)
```

## Resumo de dados

| Métrica | Resultado |
|---|---:|
| Pedidos escaneados | 2000 |
| Pedidos válidos agregados | 1691 |
| Clientes com 2+ pedidos | 149 |
| Cestas com 2+ produtos | 448 |
| Produtos únicos | 698 |
| Regras X→Y com support ≥ 2 | 270 |
| Handles com regra candidata support ≥ 3 e score ≥ 78 | 29 |
| Regras candidatas no mapa v2 | 52 |

## Top regras X→Y v2

| X | Y | Support 180d | Mesmo pedido | Seq 30 | Seq 90 | Seq 180 | Conf. 180d | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `jason-markk-essential-kit` | `jason-markk-repel-spray` | 12 | 12 | 0 | 0 | 0 | 0.4138 | 96.4 |
| `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | `calca-alo-yoga-suit-up-trouser-regular-preto` | 6 | 6 | 0 | 0 | 0 | 0.7500 | 92.5 |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | 6 | 3 | 3 | 3 | 3 | 1.0000 | 90.8 |
| `slide-nike-mind-001-light-smoke-grey-cinza` | `slide-nike-mind-001-black-chrome-preto` | 9 | 7 | 2 | 2 | 2 | 0.3462 | 89.6 |
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `air-jordan-1-low-gs-se-concord` | 6 | 0 | 6 | 6 | 6 | 0.6000 | 89.1 |
| `slide-nike-mind-001-black-chrome-preto` | `slide-nike-mind-001-light-smoke-grey-cinza` | 8 | 7 | 1 | 1 | 1 | 0.3333 | 87.8 |
| `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | `camiseta-saint-studio-boxy-supima-breuer-preto` | 5 | 3 | 2 | 2 | 2 | 0.4545 | 87.6 |
| `calca-alo-yoga-suit-up-trouser-regular-preto` | `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | 6 | 6 | 0 | 0 | 0 | 0.4000 | 87.5 |
| `jason-markk-repel-spray` | `jason-markk-essential-kit` | 12 | 12 | 0 | 0 | 0 | 0.3243 | 87.4 |
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `moletom-pace-uniforma-zip-stone-navy-azul` | 6 | 0 | 0 | 6 | 6 | 0.6000 | 86.3 |
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `camiseta-masp-x-leonilson-o-grande-rio-branco` | 6 | 0 | 0 | 6 | 6 | 0.6000 | 86.3 |
| `jason-markk-premium-suede-cleaning-kit-kit-de-suede` | `jason-markk-repel-spray` | 4 | 4 | 0 | 0 | 0 | 0.8000 | 85.0 |
| `jason-markk-ready-to-use-foam-cleaner` | `jason-markk-repel-spray` | 4 | 4 | 0 | 0 | 0 | 0.8000 | 85.0 |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-angora-sea-salt-bege` | 4 | 3 | 1 | 1 | 1 | 0.5714 | 84.4 |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-rich-oak-marrom` | 4 | 3 | 1 | 1 | 1 | 0.5000 | 84.4 |

## Candidate map corrigido

Arquivo local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v2_windows.json`

Critérios:

- `support_total_180d >= 3`;
- `score >= 78`;
- janelas sequenciais 30/90/180 incluídas;
- até 4 recomendações por handle;
- sem PII;
- excluir item atual no runtime do drawer.

## Comparação com v1

| Item | v1 | v2 corrigida |
|---|---:|---:|
| Janelas sequenciais | 30 dias | 30/90/180 dias |
| Regras support ≥ 2 | 230 | 270 |
| Handles candidatos fortes | 27 | 29 |
| Regras candidatas no mapa | 46 | 52 |

## Interpretação

A correção melhora cobertura e respeita o modelo pedido por Lucas: cross-sell X→Y com janela curta/média/longa.

A implementação DEV deve consumir o mapa v2, não o v1.

Fluxo proposto:

```text
cart item X
→ by_handle[X] do mapa v2
→ excluir X e itens já no carrinho
→ validar produto comprável/publicado
→ renderizar top 4 por score
→ fallback by_model[model(X)]
→ se vazio, esconder
```

## Fora do escopo

- margem/valor;
- prioridade de estoque como score;
- `/collections/all`;
- lista fixa manual;
- qualquer write Shopify sem aprovação.

## Próxima decisão

Approval packet corrigido deve apontar para v2 e para o mapa `cart_drawer_cross_sell_candidate_map_v2_windows.json`.

`values_printed=false`.
