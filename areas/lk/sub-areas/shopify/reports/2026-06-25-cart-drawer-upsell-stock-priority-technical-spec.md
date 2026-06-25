# Technical spec — Cart drawer upsell priority via LK Stock

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Status:** especificação técnica preparada; implementação bloqueada até evidência/regra do `lk-stock`.
- **Motivo:** Lucas pediu seguir após corrigirmos o bug dos “mesmos 4”; próximo passo é conectar a ordem do `cart-drawer__upsell-inner` com prioridades operacionais do LK Stock.

## Estado atual pós-PR #99

Arquivo:

- `snippets/lk-cart-drawer.liquid`

Já resolvido:

- fallback genérico `/collections/all/products.json` removido;
- produtos sem modelo detectado não mostram mais os mesmos 4 genéricos;
- Salomon XT-6 e Autry Medalist adicionados ao detector de modelo;
- GitHub/Shopify Production readback OK no PR #99.

## Objetivo da fase 2

Substituir a lógica puramente `best-selling` por uma ordenação que combine:

1. contexto do carrinho/modelo;
2. disponibilidade/pronta entrega confirmada pelo `lk-stock`;
3. prioridade operacional de estoque/grade/giro;
4. segurança de não prometer disponibilidade sem evidência.

## Fonte canônica Stock

Referência encontrada no Brain:

- `areas/lk/sub-areas/stock/rotinas/best-seller-ready-stock-score-v0.md`

Score v0 documentado:

| Critério | Peso |
|---|---:|
| Vendas recentes | 30 |
| Margem/valor | 20 |
| Demanda externa | 15 |
| Risco de ruptura | 15 |
| Histórico/família | 10 |
| Confiança de dados | 10 |

Bloqueio do score:

- se SKU/Tiny mapping não tiver confiança alta, item vira `needs_sku_resolution` antes de decisão operacional;
- fixtures/probes/testes não podem alimentar score.

## Proposta técnica Shopify

### 1) Input Stock → Shopify

A forma mais segura é LK Stock devolver um artefato sanitizado, sem quantidades sensíveis se não necessário:

```json
{
  "generated_at": "...",
  "source": "lk-stock",
  "confidence": "high|medium|low",
  "priority_handles": [
    {"handle":"tenis-x", "score":86, "reason":"same_model + pronta_entrega + grade_saudavel"},
    {"handle":"tenis-y", "score":78, "reason":"fallback_sneaker + demanda"}
  ],
  "blocked_handles": [
    {"handle":"tenis-z", "reason":"needs_sku_resolution|sem_evidencia|baixo_estoque_critico"}
  ]
}
```

### 2) Lógica no cart drawer

Pseudo-fluxo:

```text
cart item(s)
→ detectar modelo/silhueta
→ buscar candidatos do modelo/coleção curada
→ excluir produto atual
→ excluir blocked_handles
→ ordenar por stock_priority_score desc
→ fallback para best-selling do modelo somente se stock confidence >= medium
→ renderizar até 4
→ se não houver candidatos confiáveis, esconder bloco
```

### 3) Onde plugar no código

Funções atuais relevantes:

- `detectModelCollection(cart)`
- `loadModelBestSellers(container, model, cartHandles)`
- `loadCuratedBestSellersFallback(container, cartHandles)` — após PR #99, esconde fallback genérico.
- `renderUpsell(container, recs, title)`

Nova função sugerida:

```js
function applyStockPriority(products, stockPriority, cartHandles) {
  // remove current cart handles
  // remove blocked handles
  // annotate score/reason
  // sort score desc, then keep source order
}
```

## Pendência obrigatória

`lk-shopify` não deve consultar Tiny/DB/estoque diretamente. A implementação só pode avançar quando `lk-stock` devolver uma das opções:

1. lista de handles priorizados; ou
2. regra/score com evidência sanitizada suficiente.

Handoff ativo:

- `areas/lk/sub-areas/stock/handoffs/cart-drawer-upsell-priority-logic-request-20260625.md`

Reminder ativo:

- `rem-lk-stock-cart-drawer-upsell-priority-20260625`

## Próxima decisão para Lucas

Sem resposta do `lk-stock`, o estado seguro é manter PR #99: não repetir os mesmos 4 genéricos e esconder upsell quando não há modelo.

Quando `lk-stock` responder, LK Shopify prepara:

1. patch DEV;
2. QA com produtos mapeados e não mapeados;
3. PR/merge Production após aprovação;
4. receipt/readback.

## Writes externos

Nenhum nesta especificação. `values_printed=false`.
