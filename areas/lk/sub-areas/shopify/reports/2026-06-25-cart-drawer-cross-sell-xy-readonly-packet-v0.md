# Read-only packet — Cart drawer cross-sell X→Y v0

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Escopo:** cart drawer `cart-drawer__upsell-inner`
- **Pedido/correção de Lucas:** lógica deve ser cross-sell: “cliente comprou X, tem % de chances de comprar produtos Y”.
- **Writes externos:** 0. Apenas leitura Shopify Admin agregada.
- **PII:** nenhum dado de cliente/pedido individual salvo ou impresso. Output agregado por produto/handle.

## Correção conceitual aplicada

A ordem dos 4 produtos não deve vir de:

- margem/valor;
- prioridade de estoque;
- `/collections/all`;
- best-seller genérico;
- lista manual fixa.

A lógica correta é:

```text
X no carrinho
→ buscar regras históricas X→Y
→ ordenar Y por chance de cross-sell
→ excluir X e itens já no carrinho
→ renderizar até 4
```

## Análise read-only v0 executada

Script local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/analyze_cross_sell_xy.py`

Output agregado:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cross_sell_xy_readonly_aggregate.json`

Parâmetros v0:

| Item | Valor |
|---|---:|
| Pedidos escaneados | 750 |
| Cestas com 2+ produtos | 142 |
| Produtos únicos | 400 |
| Regras com support mínimo 2 | 6 |
| PII impressa | não |

## Top regras encontradas — amostra v0

| X | Y | Support | Confidence | Lift | Score |
|---|---|---:|---:|---:|---:|
| `the-peptide-lip-tints-rhode-multicolor` | `rhode-pocket-blush` | 3 | 0.6000 | 14.200 | 89.5 |
| `rhode-pocket-blush` | `the-peptide-lip-tints-rhode-multicolor` | 3 | 0.5000 | 14.200 | 89.5 |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | 2 | 1.0000 | 35.500 | 88.0 |
| `slide-nike-mind-001-light-smoke-grey-cinza` | `slide-nike-mind-001-black-chrome-preto` | 2 | 0.5000 | 14.200 | 88.0 |
| `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | `camiseta-saint-studio-boxy-supima-breuer-preto` | 2 | 0.5000 | 35.500 | 88.0 |
| `slide-nike-mind-001-black-chrome-preto` | `slide-nike-mind-001-light-smoke-grey-cinza` | 2 | 0.4000 | 14.200 | 77.0 |

## Interpretação

A direção conceitual está correta, mas a v0 ainda **não é suficiente para virar regra de produção do cart drawer**:

1. Só 142/750 pedidos recentes tinham 2+ produtos na mesma cesta.
2. Com `support >= 2`, apareceram apenas 6 regras.
3. As regras têm baixa robustez para a maior parte do catálogo.
4. Resultado bruto traz pares de beleza/apparel/slides; pode ser verdadeiro cross-sell, mas precisa de decisão de curadoria se o drawer deve recomendar apenas sneakers ou qualquer produto LK.

## Próximo modelo recomendado

Para fazer isso direito, o packet v1 deve combinar:

### A) Co-compra real

- mesmo pedido X+Y;
- support/confidence/lift;
- janela maior que 750 pedidos, se API/escopo permitir.

### B) Compra sequencial

- mesmo cliente compra X e depois Y em janelas de **30/90/180 dias** — correção de Lucas em 2026-06-25;
- output agregado e sem PII.

### C) Agrupamento por modelo/silhueta

Quando o produto exato não tem amostra suficiente:

```text
New Balance 530 → outros 530 / meias / produtos com co-compra real do universo 530
Adidas Samba → outros Samba / Gazelle / Spezial se dados confirmarem
Rhode lip tint → pocket blush se dados confirmarem
```

### D) Filtro de elegibilidade

- produto publicado/comprável;
- excluir produto atual e itens já no carrinho;
- disponibilidade apenas como filtro final, não score principal.

## Proposta de implementação depois do packet v1

Artefato agregado no tema ou asset JSON:

```json
{
  "by_handle": {
    "produto-x": [
      {"handle":"produto-y", "score":87, "confidence":0.23, "lift":2.1, "support":11}
    ]
  },
  "by_model": {
    "new-balance-530": [
      {"handle":"produto-y", "score":72, "reason":"model_level_cross_sell"}
    ]
  }
}
```

Cart drawer:

```text
cart item X
→ by_handle[X]
→ fallback by_model[model(X)]
→ filtro comprável/disponível
→ top 4
→ se vazio, esconder
```

## Status

- PR #99 continua correto como stop-gap: remove os mesmos 4 genéricos.
- A fase cross-sell precisa de um packet v1 mais robusto antes de qualquer theme write.
- `values_printed=false`.
