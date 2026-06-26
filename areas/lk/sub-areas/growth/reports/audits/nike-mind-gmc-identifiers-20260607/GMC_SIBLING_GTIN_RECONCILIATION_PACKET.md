# Nike Mind — GMC sibling GTIN reconciliation

Data: 2026-06-07T21:32:45.441386+00:00
Modo: read-only.

## Resumo

- Grupos por `offerId` normalizado + `variant_id`: `83`.
- Candidatos Local/LIA para receber GTIN via GMC/feed: `5`.
- Candidatos Online para receber GTIN via GMC/feed: `0`.
- Grupos ambíguos com múltiplos GTINs: `0`.

## Critério

Candidato só entra quando:

- existe item irmão no GMC com o mesmo `offerId` normalizado;
- existe o mesmo `variant_id` Shopify no link;
- o item irmão tem GTIN;
- o item alvo não tem GTIN;
- há exatamente 1 GTIN no grupo.

## Interpretação

Esses candidatos são para ajuste **GMC/feed**, não Shopify, porque a variante Shopify equivalente já aparece com GTIN no canal irmão.

## Arquivos

- `gmc_sibling_gtin_reconciliation.json`
- `gmc_sibling_gtin_local_lia_candidates.csv`
- `gmc_sibling_gtin_online_candidates.csv`

## Próxima ação

Se houver candidatos, preparar supplemental/feed update com rollback. Não aplicar `identifier_exists=false`.
