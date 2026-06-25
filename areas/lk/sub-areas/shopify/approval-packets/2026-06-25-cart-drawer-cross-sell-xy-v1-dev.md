# Approval packet — DEV cart drawer cross-sell X→Y v1

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — cart drawer `cart-drawer__upsell-inner`
- **Status:** aguardando aprovação explícita para DEV. Nenhum write deste packet executado.

## Contexto

Lucas corrigiu que o bloco não deve mostrar “4 produtos iguais/aleatórios” nem seguir margem/estoque. A regra correta é cross-sell:

```text
Cliente comprou/colocou X
→ historicamente tem % de chance de comprar Y
→ mostrar os 4 Y mais prováveis
```

## Evidência read-only

Packet v1:

- `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-xy-readonly-packet-v1.md`

Resumo:

| Métrica | Resultado |
|---|---:|
| Pedidos escaneados | 2000 |
| Pedidos válidos agregados | 1691 |
| Cestas com 2+ produtos | 448 |
| Clientes com 2+ pedidos | 149 |
| Produtos únicos | 698 |
| Regras X→Y com support ≥ 2 | 230 |
| Handles com regra candidata support ≥ 3 e score ≥ 78 | 27 |
| Regras candidatas no mapa v1 | 46 |

Candidate map local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v1.json`

## Mudança proposta DEV

Arquivos alvo prováveis:

- `snippets/lk-cart-drawer.liquid`

Implementar:

1. Embutir ou carregar mapa agregado X→Y v1.
2. Adicionar função `loadCrossSellRecommendations(container, cart, cartHandles)`.
3. Fluxo:
   - identificar handle/modelo de X no carrinho;
   - buscar `by_handle[X]`;
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
- Não prometer disponibilidade sem filtro de comprabilidade.

## QA DEV planejado

1. Readback SHA do snippet em `lk-new-theme/dev`.
2. Verificar que `/collections/all/products.json` continua ausente.
3. Testar produto com regra X→Y forte:
   - `jason-markk-essential-kit` → `jason-markk-repel-spray`.
4. Testar modelo/silhueta:
   - `new-balance-9060` deve puxar pares 9060 quando handle tiver regra.
5. Testar produto sem regra:
   - bloco deve esconder ou fallback por modelo, sem mesmos 4 genéricos.
6. Verificar exclusão do produto atual do carrinho.
7. Browser/public QA se rate limit permitir; caso contrário, Admin/source/readback + relatório de blocker.

## Risco

Médio:

- Regras ainda são v1 e podem favorecer variações do mesmo produto/modelo, não necessariamente complemento clássico.
- Cobertura por handle ainda limitada: 27 handles com regra forte.
- Por isso a implementação deve ser DEV primeiro, sem Production automática se Lucas quiser revisar visual/lista.

## Rollback

- Restaurar `snippets/lk-cart-drawer.liquid` para estado PR #99.
- Remover mapa X→Y embutido/carregado.
- Estado de rollback mantém correção anterior: sem `/collections/all` e sem “mesmos 4”.

## Decisão necessária

Para aplicar apenas em DEV:

`Aprovo DEV cart drawer cross-sell X→Y v1`

Para DEV + Production no mesmo fluxo, após QA DEV passar:

`Aprovo DEV e merge Production cart drawer cross-sell X→Y v1`
