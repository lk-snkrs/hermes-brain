# LKGOC — próxima coleção candidata: Adidas Gazelle

Criado em: 2026-06-05T19:38:02

## Decisão operacional
Após migração do padrão LKGOC para componente único em Production, a próxima candidata recomendada é `adidas-gazelle`.

## Por quê
- Collection pública existe: `/collections/adidas-gazelle`.
- Pré-checagem pública: ainda sem Hero/Guide LKGOC renderizado.
- Search demand Brasil/DataForSEO: `adidas gazelle` ~40.500 buscas/mês, intenção principal transacional.
- Boa aderência ao padrão editorial LK: silhueta terrace, suede, colorways, moda/casual e comparação com Samba/Spezial/Campus.

## Padrão obrigatório
- Usar somente `snippets/lk-goc-collection.liquid`.
- Não criar snippet estrutural novo.
- Adicionar novo branch de dados para `collection.handle == 'adidas-gazelle'`.
- QA DEV: Liquid error, Hero, Guide, `.coll-rich-content` ausente, Ler mais desktop oculto, deltaTop 0px.
- DEV/unpublished → QA → approval Lucas → Production.

## Escopo que pode ser feito sem approval adicional
- Preparar conteúdo local.
- Preparar patch no DEV/unpublished.
- Criar preview e QA.

## Escopo que exigirá approval
- Merge para Production.
- Qualquer alteração de SEO title/meta/description pública fora do tema.
