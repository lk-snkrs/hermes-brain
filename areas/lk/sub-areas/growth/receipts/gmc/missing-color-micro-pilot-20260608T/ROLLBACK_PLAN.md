# Rollback Plan — GMC Missing Color Micro-pilot — 2026-06-08

Escopo: 50 ProductInput patches em GMC, campo `productAttributes.color`.

Snapshot pré-write: `snapshot_before_patch.json`.

Rollback lógico:
1. Usar `snapshot_before_patch.json` para localizar `offerId`, `dataSource` e `snapshot_color` anterior.
2. Como todos os 50 candidatos tinham `snapshot_color: null`, rollback de campo exigiria remover/neutralizar o valor na fonte ProductInput/feed ou reprocessar pela fonte original sem `color`.
3. Não executar rollback/delete sem aprovação explícita, porque remover `color` recriaria issue de qualidade do Merchant.
4. Se algum item apresentar cor incorreta, aplicar patch pontual com a cor correta aprovada e readback.

Campos não alterados: preço, estoque, disponibilidade, GTIN, título, link, Shopify e campanhas.
