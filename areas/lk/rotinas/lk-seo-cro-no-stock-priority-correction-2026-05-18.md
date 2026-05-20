# Correção Lucas — SEO/CRO LK não prioriza estoque — 2026-05-18

## Correção

Lucas corrigiu que, para LK Sneakers, **quantidade em estoque não é critério decisivo para SEO/CRO**, porque a loja vende sob encomenda.

## Regra operacional

Para SEO/CRO, priorizar:

1. Conversão.
2. Visitas/sessões.
3. Receita/vendas.
4. GSC: impressões, cliques, CTR e posição.
5. Merchant/search demand quando afetar visibilidade/conversão.
6. Diagnóstico Claude SEO/HTML como camada secundária, depois da fila comercial.

Não priorizar/depriorizar uma página apenas por:

- estoque zero;
- baixo estoque;
- Tiny parcial/rate-limited;
- quantidade Shopify/Tiny divergente.

Estoque/Tiny pode continuar existindo em rotinas de operações, sourcing ou logística, mas **fora da fila decisória SEO/CRO**.

## Plano revisado

O próximo bloco SEO/CRO deixa de ser Data Quality por variante/tamanho e passa a ser:

- CRO/Conversion Preview v0;
- reordenação por conversão, visitas/sessões, GSC CTR e receita;
- preview visual/dev-theme apenas com aprovação explícita antes de qualquer write.

## Arquivos atualizados

- `areas/lk/projetos/lk-os-implementation-control.md`
- skill runtime `lk-seo-weekly-improvement`
- memória Hermes: regra LK SEO/CRO sem estoque como critério decisivo
