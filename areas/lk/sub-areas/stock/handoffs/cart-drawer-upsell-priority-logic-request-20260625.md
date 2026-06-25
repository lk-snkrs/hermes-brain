# Handoff — LK Stock priority logic for cart drawer upsell

- **Data:** 2026-06-25
- **Origem:** lk-shopify
- **Destino/owner:** lk-stock / [LK] Estoque Loja Física
- **Contexto:** Lucas apontou que a ordem dos 4 produtos exibidos no `cart-drawer__upsell-inner` “não faz sentido” e pediu conectar a lógica às prioridades do LK Stock.
- **Status:** bloqueado aguardando regra/evidência do lk-stock. LK Shopify não consultou estoque diretamente.

## Pedido ao LK Stock

Definir uma regra operacional de prioridade para os 4 produtos recomendados no cart drawer, usando somente fonte/evidência do lk-stock.

## Contexto técnico atual

Arquivo atual:

- `snippets/lk-cart-drawer.liquid`

Lógica atual do cart drawer:

1. Detecta modelo/silhueta do item no carrinho.
2. Busca `/collections/<modelo>/products.json?limit=16&sort_by=best-selling`.
3. Filtra disponíveis pelo JSON público Shopify e remove produtos já no carrinho.
4. Renderiza os 4 primeiros em `cart-drawer__upsell-inner`.
5. Se não detectar modelo ou não houver produto, cai em fallback `/collections/all/products.json?limit=16&sort_by=best-selling`.

Problema apontado por Lucas:

- A ordem dos 4 cards não parece comercial/operacionalmente inteligente.
- Precisamos conectar com prioridade LK Stock, não apenas best-selling público.

## Informação mínima necessária do LK Stock

Favor retornar uma das opções abaixo, com evidência sanitizada:

### Opção A — lista de handles priorizados

Para uso imediato no cart drawer:

```json
{
  "priority_handles": [
    "handle-1",
    "handle-2",
    "handle-3",
    "handle-4"
  ],
  "fallback_handles": ["..."],
  "blocked_handles": ["..."]
}
```

### Opção B — regra de score por produto

Critérios sugeridos, se o lk-stock preferir regra dinâmica:

- pronta entrega confirmada;
- grade saudável / tamanho relevante disponível;
- prioridade de giro/ruptura/encalhe;
- margem/curadoria, se disponível e autorizado;
- excluir baixo estoque crítico ou item que não deve ser empurrado;
- excluir produto atual do carrinho;
- priorizar mesmo modelo/silhueta quando fizer sentido.

Formato sugerido:

```json
{
  "score_rules": [
    {"criterion":"pronta_entrega_confirmada", "weight": 40},
    {"criterion":"same_model_or_silhouette", "weight": 25},
    {"criterion":"grade_saudavel", "weight": 20},
    {"criterion":"stock_priority", "weight": 15}
  ],
  "blocked_conditions": ["sem_evidencia_stock", "baixo_estoque_critico", "produto_atual_no_carrinho"]
}
```

## Critério de aceite para LK Shopify depois do retorno

LK Shopify só deve implementar quando houver resposta/evidência do lk-stock. Implementação proposta:

- remover fallback `/collections/all`;
- manter modelo/silhueta como contexto;
- aplicar ranking LK Stock sobre candidatos;
- renderizar até 4 produtos;
- se não houver evidência suficiente, esconder bloco ou usar fallback curado aprovado, nunca prometer disponibilidade;
- QA com carrinho real e readback.

## Reminder OS

- **Reminder OS loop needed:** yes
- **Reminder OS owner:** lk-stock
- **Reminder OS next action:** devolver regra/lista priorizada de produtos/handles para cart drawer upsell, com evidência sanitizada.
- **Reminder OS review trigger:** antes de LK Shopify mudar a lógica de ordenação dos 4 produtos no cart drawer.
- **Reminder OS evidence:** este handoff + pedido do Lucas no Telegram em 2026-06-25.

## Guardrails

- LK Shopify não deve consultar Tiny/DB/planilha/cache de estoque diretamente.
- Não prometer disponibilidade sem resposta do lk-stock.
- Sem write Shopify/GitHub/Production até regra e aprovação explícita de Lucas para implementação.
- `values_printed=false`.
