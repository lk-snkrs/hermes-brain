# Status mais recente — auto-ordenação LK piloto V2

Data: 2026-05-26
Destino: LK Growth / Shopify Collections
Status: repair V2 aplicado e verificado nas 10 coleções piloto; sem cron.

## Pedido limpo

Aplicar a correção V2 nas 10 coleções piloto: snapshot imediato; Tiny como fonte primária; override de vitrine quando Shopify tem qualquer variante com estoque positivo; fallback Shopify all-zero para bloco ESGOTADO; `collectionReorderProducts`; poll/readback; receipt; sem cron; sem alterar produto/preço/estoque/tema/SEO/tag/campanha.

## Execução

1. Foi gerado snapshot imediato antes do write V2.
2. Foi executado `collectionReorderProducts` nas 10 coleções piloto.
3. O primeiro apply V2 teve 9/10 coleções com readback OK e 1 mismatch em `Calça | Apparels`.
4. Foi executado repair sequencial a partir do snapshot V2 apenas para diferenças restantes.
5. Foi feita verificação read-only final contra o snapshot V2.

## Resultado verificado

Verificação final read-only:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/readonly-verify-20260526T173722Z/READONLY-VERIFICATION.md`

Resumo:

- 10/10 coleções com `readback_match=True`.
- Nude Project: `readback_match=True`, 90/90 produtos.
- Jacquemus: `readback_match=True`, 35/35 produtos.
- Saint Studio: `readback_match=True`, 82/82 produtos.
- Calça | Apparels: `readback_match=True`, 70/70 produtos, após 1 movimento de repair.
- Pace: `readback_match=True`, 75/75 produtos.
- Aimé Leon Dore: `readback_match=True`, 89/89 produtos.
- Nike Mind: `readback_match=True`, 18/18 produtos.
- Onitsuka Tiger Mexico 66: `readback_match=True`, 101/101 produtos.
- Onitsuka Tiger Mexico 66 Sabot: `readback_match=True`, 13/13 produtos.
- Shorts: `readback_match=True`, 28/28 produtos.

## Verificação específica Nude Project

Read-only pós-repair V2 confirmou:

- Top 12 da Nude Project não contém produto com todas as variantes Shopify em `inventory_quantity <= 0`.
- `Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo` está na posição 6 e tem estoque positivo no Shopify.
- `Moletom Nude Project Side-Eye Zip-Up Black Preto` está na posição 76 e não tem estoque positivo no Shopify.
- `Camiseta Baby Look Nude Project Juicy Cherry Preto` está na posição 19 e tem estoque positivo no Shopify.

## Artefatos

- Snapshot V2: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260526T171910Z/rollback-snapshot-pre-write-immediate.json`
- Receipt apply V2: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260526T171910Z/RECEIPT-FINAL.md`
- Receipt repair V2: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/repair-from-snapshot-20260526T173527Z/REPAIR-FROM-SNAPSHOT-RECEIPT.md`
- Verificação final read-only: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/readonly-verify-20260526T173722Z/READONLY-VERIFICATION.md`

## Não ações

- Nenhum cron criado.
- Nenhuma alteração em produto, preço, estoque/disponibilidade, tema, SEO/tags, checkout, campanha ou comunicação.

## Rollback

Rollback possível usando o snapshot V2 imediato e restaurando via `collectionReorderProducts`, com poll e readback. Requer nova aprovação explícita para executar rollback.
