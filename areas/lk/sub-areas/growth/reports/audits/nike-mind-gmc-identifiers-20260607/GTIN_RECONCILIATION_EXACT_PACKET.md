# Nike Mind — GTIN reconciliation exact candidates

Data: 2026-06-07T21:32:10.093837+00:00
Modo: reconciliação GMC → Shopify por match exato `variant=<shopify_variant_id>`.

## Resumo

- Itens GMC Nike Mind com GTIN observado: `17`.
- Candidatos exatos para preencher barcode no Shopify: `0`.
- Conflitos/revisão: `0`.
- Variantes Shopify sem barcode no audit original: `123`.

## Critério de segurança

Aplicável somente quando:

1. item no GMC tem `gtin`;
2. link do GMC contém `variant=<id>`;
3. esse `<id>` é exatamente a variante Shopify auditada sem barcode;
4. SKU/offerId não apresenta conflito.

Não foi feita propagação por style, cor, grade ou tamanho.

## Arquivos

- `gtin_reconciliation_exact_candidates.json`
- `gtin_reconciliation_exact_candidates.csv`
- `gtin_reconciliation_conflicts_or_review.csv`

## Próxima ação

Se aprovado para write, aplicar esses `0` barcodes no Shopify, com snapshot por variante e readback pós-update.
