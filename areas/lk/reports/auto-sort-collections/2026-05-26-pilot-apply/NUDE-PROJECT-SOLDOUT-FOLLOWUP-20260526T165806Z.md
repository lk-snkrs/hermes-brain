# Follow-up — Nude Project sold-out ordering

Data: 2026-05-26T16:58:06Z

## Pedido limpo

Corrigir a coleção Nude Project porque um produto disponível no storefront aparece entre produtos esgotados no bloco final.

## Evidências

- Print do Lucas mostra, no final da coleção Nude Project:
  - `Moletom Nude Project Side-Eye Zip-Up Black Preto` no bloco de esgotados/zero estoque.
  - `Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo` visualmente disponível entre itens esgotados.
  - `Camiseta Baby Look Nude Project Juicy Cherry Branca` com selo `ESGOTADO`.
  - `Boné Nude Project New Varsity Bege` com selo `ESGOTADO`.
- Storefront público (`/products/*.js`) confirmou:
  - `calca-nude-project-jeans-old-baggy-black-preto`: `available=true`; variantes disponíveis `M/M` e `L/G`.
  - `moletom-nude-project-side-eye-zip-up-black-preto`: `available=false`; todas variantes indisponíveis.
  - `camiseta-baby-look-nude-projet-juicy-cherry-branca`: `available=false`; todas variantes indisponíveis.
  - `bone-nude-project-new-varsity-bege`: `available=false`.
- Admin read-only atual confirmou conflito de fonte:
  - Tiny snapshot usado: `tiny_stock_20260515T092206Z`.
  - A calça Black/Purple tinha `tiny_stock_status=out_of_stock_tiny_signal`, mas Shopify variants tinham `[0, 0, 1, 1, 0]`.

## Interpretação

A falha não foi mais o `out_of_stock_shopify_fallback`; foi conflito entre Tiny stale/zerado e storefront Shopify visivelmente disponível.

Para merchandising de coleção, o bloco final deve refletir o que o cliente vê no storefront: produtos com algum tamanho comprável não devem ficar misturados entre produtos `ESGOTADO`.

Tiny continua sendo a verdade operacional de estoque, mas para ordenação visual da coleção a regra precisa ter um override rotulado quando Shopify tem variante positiva.

## Preview técnico local

Patch local já preparado em:

`/opt/data/hermes_bruno_ingest/scripts/lk_collection_auto_sort_apply_pilot_20260526.py`

Mudança lógica:

- adiciona `shopify_any_variant_positive(product)`;
- se Tiny diz zero para todos os SKUs, mas Shopify tem alguma variante com `inventory_quantity > 0`, classifica como `in_stock_shopify_visible_override_tiny_zero`;
- esse status não entra no bucket final `out_of_stock_*`.

Resultado do dry-run/read-only pós-patch na Nude Project:

- `Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo`
  - posição atual admin: 69
  - posição proposta: 6
  - status proposto: `in_stock_shopify_visible_override_tiny_zero`
- `Moletom Nude Project Side-Eye Zip-Up Black Preto`
  - posição atual admin: 68
  - posição proposta: 76
  - status: `out_of_stock_shopify_fallback`
- `Camiseta Baby Look Nude Project Juicy Cherry Branca`
  - posição atual admin: 70
  - posição proposta: 77
  - status: `out_of_stock_shopify_fallback`
- `Boné Nude Project New Varsity Bege`
  - posição atual admin: 71
  - posição proposta: 78
  - status: `out_of_stock_shopify_fallback`

## Risco

- Shopify positive inventory pode divergir de Tiny operacional. Por isso o status é rotulado como override visual, não como confirmação definitiva de estoque.
- A correção proposta pode mover a calça para o top 8 porque ela também entra na regra de produto novo/performance. Se Lucas quiser apenas tirar a calça do bloco esgotado sem promovê-la tanto, ajustar a regra antes do apply.

## Bloqueio

Não executei novo `collectionReorderProducts` neste follow-up. A mudança real na coleção é Shopify write/storefront-affecting e precisa de aprovação explícita atual para aplicar o repair.

## Rollback

Rollback da aplicação anterior continua disponível em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260526T160317Z/rollback-snapshot-pre-write-immediate.json`

Para o próximo apply seguro: gerar snapshot imediato novo antes do write e usar readback pós-mutation.

## Próxima decisão

Aprovar um repair scoped para as 10 coleções piloto, com a nova regra de override visual Shopify-positive:

`Aprovado aplicar repair da auto-ordenação nas 10 coleções piloto com snapshot imediato, regra Shopify-positive fora do bucket ESGOTADO, collectionReorderProducts, poll, readback e receipt; sem cron e sem alterar produto/preço/estoque/tema/SEO/tag/campanha.`
