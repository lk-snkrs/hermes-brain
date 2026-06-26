# Receipt — Normalize gender/age upstream Shopify

- Criado: 2026-06-17T20:24:49.736610+00:00
- Escopo: normalizar valores existentes explícitos de `mm-google-shopping.gender` e `mm-google-shopping.age_group`.
- Produtos ativos escaneados: 1838
- Alterações tentadas: 719
- Readback OK: 719
- Falhas: 0
- Skipped não mapeado: 2

## Excluído
- Preencher ausentes por inferência, preço, estoque, variantes, SKU, MPN, GMC direto, campanhas, theme.

## Mapas usados
- Unissex/UNISEX/Unisex → unisex
- Feminino → female
- Masculino → male
- Adulto/ADULTO/adulto/Adult → adult
- Infantil → kids

## Rollback
- Restaurar valores antigos a partir de `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/product-data-upstream-normalize-gender-age-20260617T202334Z/backup-before.json`