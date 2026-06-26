# Approval packet — Provador Virtual mKFashion PDP

Data: 2026-06-09
Owner: LK Shopify
Status: read-only diagnostic + local code preview; no Shopify/theme upload executed.

## Pedido

Arrumar o Provador Virtual na PDP LK.

## Diagnóstico read-only

PDP testada: `/products/new-balance-530-white-natural-indigo-1`.

Evidências:

- Storefront público retorna HTML 200 e contém o snippet `mkfashion` / botão `Provador Virtual`.
- SDK `https://unpkg.com/mkfashion-sdk/src/mkfashion.js` retorna 200.
- Snippet live em Production (`lk-new-theme/production`, theme `155065417950`, role `main`) usa:
  - `product.selected_or_first_available_variant.sku`
  - `mkfashion.isAvailable(PROJECT_ID, sku)`
  - `mkfashion.open(... identifier: sku)`
- No produto testado, a PDP seleciona SKU `MR530SG-1` como primeiro disponível no Shopify, mas a API mKFashion retorna `available=false` para esse SKU.
- A mesma API retorna `available=true` para o `product.id` Shopify `8274815058142` e para o SKU base cadastrado no mKFashion `MR530SG-5`.

Conclusão: o botão fica oculto em produtos integrados quando o SKU selecionado/primeiro disponível do Shopify não é o SKU usado pelo mKFashion. O identificador mais estável para abrir/verificar o provador é o `product.id` Shopify (`externalId` no mKFashion), não o SKU da variante selecionada.

## Preview local preparado

Worktree local isolada:

`/opt/data/worktrees/lk-new-theme-mkfashion-tryon-fix-20260609`

Arquivo alterado localmente:

`snippets/mkfashion-tryon.liquid`

Mudança proposta:

1. Criar `mkfashionIdentifier = product.id || sku`.
2. Usar `mkfashionIdentifier` em:
   - `mkfashion.isAvailable(PROJECT_ID, mkfashionIdentifier)`
   - `mkfashion.open({ projectId, identifier: mkfashionIdentifier })`
3. Criar mapas locais de variantes do produto (`sku`, `variant id`, `size`) para resolver corretamente o `cart/add.js` a partir do payload do mKFashion.
4. Manter fallback para a variante selecionada caso o payload não traga identificador resolvível.

## Verificação local feita

Static checks:

- `uses_product_id_identifier`: OK
- `availability_uses_identifier`: OK
- `open_uses_identifier`: OK
- `cart_resolver_present`: OK
- `old_availability_removed`: OK
- `old_open_removed`: OK
- `liquid_for_balance`: OK
- `liquid_if_balance`: OK

API mKFashion testada:

- `availability(... sku=MR530SG-1)`: `available=false`
- `availability(... sku=8274815058142)`: `available=true`

Shopify readback Production:

- Production theme atual: `155065417950`, `lk-new-theme/production`, role `main`.
- Asset live ainda usa o padrão antigo por SKU.
- Nenhum upload feito.

## Risco

- Baixo/médio: altera snippet PDP que carrega SDK externo e afeta o botão do Provador Virtual.
- Risco principal é no fluxo `Adicionar ao carrinho` vindo do provador; mitigado com resolução por `produtoVarianteId`, `productVariantId`, `selectedIdentifier`, SKU e tamanho.
- Precisa DEV preview antes de Production.

## Rollback

- Reverter `snippets/mkfashion-tryon.liquid` para o asset atual da Production/branch production.
- Como ainda não houve upload, rollback atual é simplesmente descartar a worktree local.

## Bloqueio

Qualquer upload para tema Shopify, mesmo DEV/unpublished, exige aprovação explícita atual do Lucas.

## Próxima decisão

Aprovar upload do `snippets/mkfashion-tryon.liquid` para o tema DEV/unpublished `155065450718` (`lk-new-theme/dev`) para QA visual e funcional do Provador Virtual.

Escopo da aprovação DEV:

- Target: Shopify theme `155065450718` (`lk-new-theme/dev`, role `unpublished`, a reconfirmar antes do PUT).
- Asset: `snippets/mkfashion-tryon.liquid`.
- Não mexer em Production.
- Não mexer em produto, preço, estoque, checkout, app config ou campanhas.

## Worker receipt

- demand_classification: Shopify theme/PDP app-surface fix — Provador Virtual mKFashion.
- canonical_playbook: Shopify theme/CRO DEV preview with Production-gated promotion.
- workers_selected: code/local-diff QA + public/API diagnostic.
- workers_skipped: visual browser worker unavailable in this runtime; no production deploy worker before approval.
- delegation_tool_used: no.
- reason_if_no_delegation: no delegate_task tool available; task small enough for local diagnostic + patch preview.
- owner_agent_final_decision: LK Shopify owns the packet; DEV theme upload requires Lucas approval.
