# Approval Packet — Batch Collection SEO/GEO Prioridades

Gerado: 2026-06-16T19:50:34.519604+00:00

## Status
- New Balance 9060: já aplicado com receipt separado.
- Este packet cobre as próximas 7 coleções existentes.
- Writes deste packet: ainda 0.
- Drafts prontos e QA sem termos proibidos.

## Coleções prontas para aplicar
### Adidas Samba
- Handle: `adidas-samba`
- URL: https://lksneakers.com.br/collections/adidas-samba
- Keyword foco: `adidas samba`
- Volume: 246000/mês
- Produtos na coleção: 95
- Risco atual detectado: nenhum nos campos lidos
- QA draft: OK

### Adidas Samba Jane
- Handle: `adidas-samba-jane`
- URL: https://lksneakers.com.br/collections/adidas-samba-jane
- Keyword foco: `adidas samba jane`
- Volume: 2400/mês
- Produtos na coleção: 12
- Risco atual detectado: nenhum nos campos lidos
- QA draft: OK

### Nike Mind 001 e 002
- Handle: `nike-mind-001`
- URL: https://lksneakers.com.br/collections/nike-mind-001
- Keyword foco: `nike mind 001`
- Volume: 27100/mês
- Produtos na coleção: 18
- Risco atual detectado: disponibilidade
- QA draft: OK

### New Balance 204L
- Handle: `new-balance-204l`
- URL: https://lksneakers.com.br/collections/new-balance-204l
- Keyword foco: `new balance 204l`
- Volume: 12100/mês
- Produtos na coleção: 32
- Risco atual detectado: estoque, disponibilidade, frete grátis, desconto no pix, 10x sem juros
- QA draft: OK

### Onitsuka Tiger Mexico 66
- Handle: `onitsuka-tiger-mexico-66`
- URL: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66
- Keyword foco: `onitsuka tiger mexico 66`
- Volume: 8100/mês
- Produtos na coleção: 102
- Risco atual detectado: disponibilidade, frete grátis, desconto no pix, 10x sem juros
- QA draft: OK

### Puma Speedcat
- Handle: `puma-speedcat`
- URL: https://lksneakers.com.br/collections/puma-speedcat
- Keyword foco: `puma speedcat`
- Volume: 18100/mês
- Produtos na coleção: 13
- Risco atual detectado: estoque, disponibilidade, frete grátis, desconto no pix, 10x sem juros, entrega rápida
- QA draft: OK

### Asics Gel-Kayano 14
- Handle: `asics-gel-kayano-14`
- URL: https://lksneakers.com.br/collections/asics-gel-kayano-14
- Keyword foco: `asics gel kayano 14`
- Volume: 8100/mês
- Produtos na coleção: 3
- Risco atual detectado: nenhum nos campos lidos
- QA draft: OK

## Alertas
- Adidas Samba tem duplicidade/canibalização potencial: `/collections/samba` e `/collections/adidas-samba` estão 200 e canônicas. O draft foi preparado para `/collections/adidas-samba`, mas recomendo decidir depois redirect/canonical interno entre as duas.
- Nike Shox TL tem 9.900 buscas/mês, mas não encontrei coleção Shopify por `shox`, `nike shox`, `shox tl` ou `nike shox r4`. Requer criação de coleção ou confirmação de handle antes de qualquer write.

## Mudança proposta
Para cada coleção existente:
- Substituir `descriptionHtml` por texto premium, seguro e citável.
- Atualizar SEO title/meta.
- Remover linguagem pública de estoque, sob encomenda, prazo fixo, frete grátis, Pix, 10x e disponibilidade.
- Adicionar FAQ de coleção com respostas sobre conforto, tamanho, look e originalidade.

## Risco
- Médio/baixo: são páginas de coleção visíveis e algumas com alto tráfego.
- Reversível via backup individual de cada coleção.
- Não mexe em tema, produtos, preço, estoque, feed, campanhas ou Klaviyo.

## Rollback
Antes do write: salvar backup de `descriptionHtml` e `seo` de cada coleção. Rollback: restaurar esses campos por Shopify Admin GraphQL.

## Arquivos
- Drafts: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/batch-collection-drafts.json`
- Read-only selections: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/selected-collections-readonly.json`
- Search summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/shopify-collection-search-batch-summary.json`

## Aprovação necessária
Para aplicar as 7 coleções existentes em produção, preciso da frase explícita:
`Aprovo aplicar o batch Collection SEO/GEO nas 7 coleções existentes, com backup e rollback. Não aplicar Nike Shox TL ainda.`

## Fora deste approval
- Resolver duplicidade `/collections/samba` vs `/collections/adidas-samba`.
- Criar coleção Nike Shox TL.
- Qualquer alteração de produto, estoque, preço, feed, campanhas ou theme.