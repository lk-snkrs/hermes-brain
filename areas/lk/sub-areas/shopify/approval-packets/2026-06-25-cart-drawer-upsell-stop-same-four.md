# Approval packet — Cart drawer upsell: parar de repetir os mesmos 4 produtos

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — cart drawer upsell / `cart-drawer__upsell-inner`
- **Correção do Lucas:** “na verdade, não... o cart drawer não está funcionando assim.. ele sempre mostra apenas 4 produtos os mesmos.”
- **Status:** patch local preparado; nenhum write Shopify/GitHub executado neste packet.

## Correção de diagnóstico

Meu diagnóstico anterior estava incompleto. O código tem uma tentativa de lógica por modelo, mas o comportamento observado pelo Lucas (“sempre os mesmos 4”) faz sentido porque há um fallback genérico:

```js
fetch('/collections/all/products.json?limit=16&sort_by=best-selling')
```

Quando o modelo não é detectado ou a collection do modelo falha, o drawer cai em `/collections/all`, que sempre entrega os mesmos primeiros produtos best-selling da loja.

Read-only probe público mostrou os 4 primeiros atuais de `/collections/all`:

1. `accolade-straight-leg-sweatpant-charcoal-green`
2. `adidas-taekwondo-mei-ballet-branco-e-preto`
3. `adidas-taekwondo-mei-ballet-preto-e-branco`
4. `basic-pack-5-8-sufgang-multicolor`

Isso explica a percepção de “mesmos 4” e também de pouca relevância.

## Patch proposto — fase 1 segura

Arquivo alvo:

- `snippets/lk-cart-drawer.liquid`

Target local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-upsell-inner-fix-20260625/target_no_generic_fallback_snippets__lk-cart-drawer.liquid`

Mudanças:

1. **Remover fallback genérico `/collections/all`**.
2. Se não houver modelo detectado, **não renderizar upsell genérico** em vez de mostrar os mesmos 4.
3. Ampliar mapeamento de modelos com padrões recentes:
   - `salomon xt-6` → `salomon-xt-6`
   - `autry medalist` → `autry-medalist`

## Static QA local

Arquivo:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-upsell-inner-fix-20260625/no_generic_fallback_static_qa.json`

Resultados:

| Check | Resultado |
|---|---:|
| `/collections/all/products.json` antes | `1` |
| `/collections/all/products.json` depois | `0` |
| fallback genérico escondido | **sim** |
| arquivo alterado | `snippets/lk-cart-drawer.liquid` |
| SHA antes | `30def861e4b4fff749088679d12bf786ce03f464b74b3267d3d83c71a2d04867` |
| SHA target | `b4242155f39146e036a9fe687b8412878b2d237720d3c8fdde508e709eebde72` |

## O que este patch resolve

- Para produtos sem modelo detectado, o drawer **para de mostrar os mesmos 4 produtos genéricos**.
- Para produtos com modelo detectado, continua mostrando “Mais vendidos do modelo”.
- Evita que apparel/acessório apareça como upsell genérico no fechamento.

## O que este patch ainda não resolve

Este patch **não conecta ainda com LK Stock**. Para isso, precisamos da resposta do `lk-stock` com:

- lista priorizada de handles; ou
- regra de score por prioridade operacional/estoque.

Handoff já criado para isso:

- `areas/lk/sub-areas/stock/handoffs/cart-drawer-upsell-priority-logic-request-20260625.md`

## QA planejado após aprovação

1. Aplicar em DEV `lk-new-theme/dev`.
2. Readback SHA do snippet.
3. Testar carrinho com produto de modelo mapeado:
   - deve mostrar recomendações do modelo.
4. Testar carrinho com produto não mapeado:
   - não deve cair nos mesmos 4 de `/collections/all`.
5. Confirmar via código/readback que `/collections/all/products.json` sumiu do snippet.
6. Se DEV passar e Lucas aprovar Production junto, PR/merge para `production`, Shopify readback e QA público.

## Risco

Baixo/médio:

- Pode esconder o bloco de upsell em produtos sem modelo detectado.
- Mas isso é melhor do que mostrar sempre os mesmos 4 produtos sem contexto.
- Próximo passo ideal é receber prioridade LK Stock para preencher esse fallback de forma inteligente.

## Rollback

- Reverter o hunk no `snippets/lk-cart-drawer.liquid`.
- Restaurar fallback anterior `/collections/all/products.json` se necessário.

## Próxima decisão

Para aplicar em DEV e, se QA passar, promover via PR/merge Production:

`Aprovo DEV e merge Production cart drawer stop same 4 upsell fallback`
