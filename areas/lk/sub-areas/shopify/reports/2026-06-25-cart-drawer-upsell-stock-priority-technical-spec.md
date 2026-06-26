# Technical spec — Cart drawer cross-sell logic X → Y

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Status:** especificação corrigida após feedback de Lucas; implementação bloqueada até análise read-only de co-compra/cross-sell e approval packet.
- **Motivo:** Lucas corrigiu que o objetivo não é prioridade de margem/estoque. A lógica certa é **cross-sell probabilístico**: se o cliente colocou/comprou X, quais produtos Y têm maior chance de compra conjunta/seguinte.

## Estado atual pós-PR #99

Arquivo:

- `snippets/lk-cart-drawer.liquid`

Já resolvido:

- fallback genérico `/collections/all/products.json` removido;
- produtos sem modelo detectado não mostram mais os mesmos 4 genéricos;
- Salomon XT-6 e Autry Medalist adicionados ao detector de modelo;
- GitHub/Shopify Production readback OK no PR #99.

## Objetivo da fase 2

Substituir a lógica de `best-selling`/fallback por **cross-sell baseado em co-compra**:

> Se cliente colocou/comprou X, quais produtos Y historicamente têm maior chance de serem comprados junto ou na sequência?

A ordem dos 4 cards deve vir de uma matriz X→Y, não de margem, estoque, coleção genérica ou gosto manual.

## Modelo correto de ranking

### Fonte primária — co-compra / associação de cesta

Construir uma matriz com pedidos reais, em leitura segura e agregada:

- pares comprados no mesmo pedido: `X + Y`;
- pares comprados pelo mesmo cliente em janela curta, se permitido/seguro: `X → Y em N dias`;
- agregação por produto e por modelo/silhueta para evitar amostra pequena;
- excluir o produto atual do carrinho;
- excluir produtos indisponíveis/publicamente não compráveis apenas como filtro final, sem transformar estoque em critério de ranking.

### Métricas sugeridas

| Métrica | Uso |
|---|---|
| `support(X,Y)` | volume absoluto de pedidos com X e Y juntos |
| `confidence(X→Y)` | % dos pedidos com X que também compram Y |
| `lift(X,Y)` | quanto Y aparece com X acima do acaso |
| `recency_weight` | dá mais peso para comportamento recente |
| `model_family` | agrupa por modelo/silhueta quando SKU/variante tem pouca amostra |

### Score cross-sell sugerido

| Critério | Peso sugerido |
|---|---:|
| Confidence X→Y | 45 |
| Lift X,Y | 25 |
| Support mínimo / robustez | 15 |
| Recência | 10 |
| Mesmo universo/complementaridade visual | 5 |

Critérios explicitamente fora do ranking:

- margem/valor;
- prioridade de giro/estoque;
- coleção `/all`;
- escolha manual fixa sem evidência.

Estoque entra só como **filtro de elegibilidade** no final, preferencialmente via LK Stock quando necessário: não recomendar item sem evidência de disponibilidade/comprabilidade.

## Proposta técnica Shopify

### 1) Input cross-sell → Shopify

Gerar um artefato agregado, sem dados pessoais:

```json
{
  "generated_at": "...",
  "source": "shopify_orders_aggregated_readonly",
  "method": "basket_cooccurrence",
  "rules": {
    "min_support": 3,
    "lookback_days": 180,
    "exclude_current_cart_product": true
  },
  "by_handle": {
    "produto-x": [
      {"handle":"produto-y", "confidence":0.23, "lift":2.1, "support":11, "score":87},
      {"handle":"produto-z", "confidence":0.18, "lift":1.7, "support":8, "score":74}
    ]
  },
  "by_model": {
    "new-balance-530": [
      {"handle":"produto-y", "score":82, "reason":"co_compra_modelo"}
    ]
  }
}
```

### 2) Lógica no cart drawer

Pseudo-fluxo:

```text
cart item(s)
→ identificar handle/modelo do X
→ procurar recomendações X→Y no mapa agregado
→ excluir produto atual e itens já no carrinho
→ aplicar filtro de elegibilidade/comprável/disponível
→ ordenar por cross_sell_score desc
→ renderizar até 4
→ se não houver regra confiável, fallback por modelo/silhueta; se ainda não houver, esconder bloco
```

### 3) Onde plugar no código

Funções atuais relevantes:

- `detectModelCollection(cart)`
- `loadModelBestSellers(container, model, cartHandles)`
- `loadCuratedBestSellersFallback(container, cartHandles)` — após PR #99, esconde fallback genérico.
- `renderUpsell(container, recs, title)`

Nova função sugerida:

```js
function loadCrossSellRecommendations(container, cart, cartHandles) {
  // read static/generated cross-sell map
  // merge handle-level and model-level rules
  // filter current cart products
  // fetch product JSON only for selected Y candidates
  // render top 4 by cross_sell_score
}
```

## Pendência obrigatória

Antes de implementar no tema, LK Shopify precisa produzir um **packet de análise read-only** com dados agregados de pedidos/co-compra:

1. período analisado;
2. método de agregação;
3. top regras X→Y;
4. exclusões/filtros;
5. risco de amostra pequena;
6. proposta do artefato JSON/Liquid para o tema;
7. QA e rollback.

LK Stock deixa de ser dono do ranking. Ele pode ser consultado depois apenas como filtro de disponibilidade/elegibilidade, sem decidir o score principal.

## Próxima decisão para Lucas

Próximo passo correto: análise read-only de pedidos/co-compra para gerar a matriz X→Y. Depois disso, preparar patch DEV + approval packet para plugar no cart drawer.

## Writes externos

Nenhum nesta especificação. `values_printed=false`.
