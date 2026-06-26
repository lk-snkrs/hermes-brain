# GMC final residual classification — 2026-06-08

Status: read-only / sem write

## Summary
- total_products: `22663`
- residual_products: `364`

## Issue attribute instances
- size: 1035
- age group: 895
- gender: 895
- color: 885

## Classes
- size ainda pendente: 207
- fileInput/fonte externa: 182
- categoria/product_type ausentes: 182
- age/gender pendente: 179
- color ausente sem inferência segura: 177
- title quebrado/tamanho-only: 162
- categoria Google incoerente: não-sapato como Sapatos: 34

## By data source
- accounts/5297679409/dataSources/10525577766: 182
- accounts/5297679409/dataSources/10636492695: 182

## Top product types
- unknown: 182
- Tênis: 106
- Sneakers: 33
- Colecionável: 17
- Jaqueta: 9
- Óculos: 8
- Manutenção: 6
- Boné: 2
- Livro: 1

## Próximas frentes recomendadas

1. **fileInput/fonte externa**: tratar via fonte/feed/supplemental, não via Merchant API direta.
2. **categoria Google incoerente**: preparar batch de `googleProductCategory` para não-sapatos e roupas, com preview/aprovação.
3. **title quebrado/tamanho-only**: precisa corrigir fonte do produto/feed; risco alto de patch sintomático.
4. **color ausente sem inferência segura**: enrichment manual por marca/modelo ou supplemental feed.

## Files

- Classified items: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/final-residual-classification-20260608/residual_items_classified.json`
- Buckets: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/final-residual-classification-20260608/buckets.json`