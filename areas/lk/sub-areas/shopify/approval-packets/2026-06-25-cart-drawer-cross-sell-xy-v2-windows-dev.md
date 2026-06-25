# Approval packet — DEV cart drawer cross-sell X→Y v2 30/90/180

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — cart drawer `cart-drawer__upsell-inner`
- **Status:** aguardando aprovação explícita para DEV. Nenhum write deste packet executado.
- **Correção incorporada:** compra sequencial X→Y em janelas **30/90/180 dias**.

## Contexto

Lucas corrigiu que o bloco deve funcionar como cross-sell probabilístico:

```text
Cliente comprou/colocou X
→ historicamente tem % de chance de comprar Y
→ mostrar os 4 Y mais prováveis
```

## Evidência read-only corrigida

Packet v2:

- `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-xy-readonly-packet-v2-windows.md`

Resumo:

| Métrica | Resultado |
|---|---:|
| Pedidos escaneados | 2000 |
| Pedidos válidos agregados | 1691 |
| Cestas com 2+ produtos | 448 |
| Clientes com 2+ pedidos | 149 |
| Produtos únicos | 698 |
| Regras X→Y com support ≥ 2 | 270 |
| Handles com regra candidata support ≥ 3 e score ≥ 78 | 29 |
| Regras candidatas no mapa v2 | 52 |

Candidate map local corrigido:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v2_windows.json`

## Mudança proposta DEV

Arquivo alvo provável:

- `snippets/lk-cart-drawer.liquid`

Implementar:

1. Embutir/carregar mapa agregado X→Y v2.
2. Adicionar função `loadCrossSellRecommendations(container, cart, cartHandles)`.
3. Fluxo:
   - identificar handle/modelo de X no carrinho;
   - buscar `by_handle[X]` no mapa v2;
   - excluir X e itens já no carrinho;
   - validar produto publicável/comprável pelo JSON público;
   - renderizar top 4 por score;
   - fallback `by_model[model(X)]`;
   - se vazio, esconder bloco.
4. Título sugerido: `Também compram com este produto`.

## Não aprovado / fora do escopo

- Não alterar produto, preço, estoque, collection, metafield, checkout, cron, GMC, Klaviyo, ads, WhatsApp ou e-mail.
- Não usar margem/valor.
- Não usar `/collections/all`.
- Não usar prioridade de estoque como score.
- Não usar mapa v1; usar v2 com 30/90/180.

## QA DEV planejado

1. Readback SHA do snippet em `lk-new-theme/dev`.
2. Verificar que `/collections/all/products.json` continua ausente.
3. Testar produto com regra X→Y forte:
   - `jason-markk-essential-kit` → `jason-markk-repel-spray`.
4. Testar regra com sequência/janela:
   - exemplos do mapa v2 com `sequential_90d_support`/`sequential_180d_support` > 0.
5. Testar produto sem regra:
   - bloco deve esconder ou fallback por modelo, sem mesmos 4 genéricos.
6. Verificar exclusão do produto atual do carrinho.
7. Browser/public QA se rate limit permitir; caso contrário, Admin/source/readback + blocker.

## Risco

Médio:

- Cobertura ainda limitada: 29 handles com regra forte.
- Algumas regras são variações da mesma família/modelo, não sempre complemento clássico.
- Por isso deve ir primeiro para DEV.

## Rollback

- Restaurar `snippets/lk-cart-drawer.liquid` para estado PR #99.
- Remover mapa X→Y v2.
- Estado de rollback mantém correção anterior: sem `/collections/all` e sem “mesmos 4”.

## Decisão necessária

Para aplicar apenas em DEV:

`Aprovo DEV cart drawer cross-sell X→Y v2 30/90/180`

Para DEV + Production no mesmo fluxo, após QA DEV passar:

`Aprovo DEV e merge Production cart drawer cross-sell X→Y v2 30/90/180`
