# Validation addendum — corrected collection order final21

Data: 2026-05-28T14:47:23Z

## Summary

- Coleções processadas: 21
- Shopify `collectionReorderProducts` userErrors: 0
- Total de moves aplicados: 118
- Admin top 8 = regra comercial recomputada: 21/21
- Admin full order = regra comercial recomputada: 21/21
- Público top = Admin top, comparação estrita: 18/21

## Public storefront divergences

As 3 divergências públicas são falsas divergências para a regra comercial: em todos os casos, o prefixo de produtos vendáveis do público bate com o prefixo vendável do Admin; a diferença aparece apenas no 8º slot público por produtos sem disponibilidade/ocultos que o `products.json` ainda retorna de forma diferente do Admin top 8.

### Jason Markk (`jason-markk`)

- Admin/regra comercial: OK
- Público: primeiros 5 produtos vendáveis batem com Admin
- Divergência: 6º item público é unavailable (`Jason Markk Premium Shoe Cleaner (236ml)`) enquanto o Admin top 8 contém itens classificados como `not_storefront_available_final`

### Sufgang (`sufgang`)

- Admin/regra comercial: OK
- Público: primeiros 7 produtos vendáveis batem com Admin
- Divergência: 8º item público é unavailable (`Camiseta Sufgang Basic Pack 5.8 Cinza`) enquanto o Admin top 8 contém item `not_storefront_available_final`

### Dane-se x Rubem Valentim (`dane-se-x-rubem-valentim`)

- Admin/regra comercial: OK
- Público: primeiros 7 produtos vendáveis batem com Admin
- Divergência: 8º item público é unavailable (`Camiseta Dane-se x Rubem Valentim Pintura Verde`) enquanto o Admin top 8 contém item `not_storefront_available_final`

## Interpretação

O lote está comercialmente validado. A regra aprovada foi preservada: produtos vendáveis aparecem primeiro; produtos sem disponibilidade ficam no bucket final. A divergência pública estrita vem de diferenças de exposição/availability no storefront para itens finais, não de inversão de produtos vendáveis.

## Não ações

- Nenhum cron ativado.
- Nenhum produto, preço, estoque, tag, tema, SEO, GMC, checkout ou campanha alterado.
- Mudança restrita à ordenação de coleções MANUAL aprovadas.

## Rollback

Rollback snapshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/corrected-apply-final21-CORRECT-20260528T144723Z/rollback-snapshot-pre-write-immediate.json`
