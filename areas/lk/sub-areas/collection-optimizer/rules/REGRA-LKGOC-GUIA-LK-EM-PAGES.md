# REGRA LKGOC — Guia LK em `/pages`, não dentro da collection

Status: CANÔNICO / OPERACIONAL  
Owner: `[LK] Otimização de Coleções` / `lk-collection-optimizer`  
Data: 2026-06-09

## Decisão

O **Guia LK completo da coleção** deve ser produzido como **página Shopify em `/pages`**, usando template de página LKGOC, e **não como conteúdo longo dentro do template de collection**.

A collection otimizada continua sendo a vitrine comercial: hero curto, contexto mínimo, grid, filtros, CTAs e ponte para o guia. O guia completo vive em `/pages` para funcionar como asset editorial, SEO/GEO e citável.

## Arquitetura canônica

- Collection otimizada:
  - template: `templates/collection.lkgoc.json`;
  - objetivo: conversão, navegação, grid, CTA, confiança e entrada editorial curta;
  - pode ter bloco teaser/resumo do Guia LK;
  - deve linkar para o Guia LK completo.

- Guia LK completo:
  - URL pública esperada: `/pages/guia-[colecao]` ou slug equivalente aprovado;
  - template Shopify: `templates/page.guia-[colecao]-lkgoc.json` ou template escalável equivalente;
  - section base: `sections/lk-goc-guide-v1.liquid` ou sucessor canônico;
  - objetivo: intenção de busca, comparação, FAQ, blocos citáveis, GEO/AI Search e apoio à decisão.

## Padrão já existente no tema

Referências observadas no tema LK:

- `templates/page.nb204l-guide.json`
- `templates/page.guia-puma-speedcat-lkgoc.json`
- `templates/page.guia-adidas-gazelle-lkgoc.json`
- `templates/page.guia-nike-dunk-lkgoc.json`
- `templates/page.guia-yeezy-lkgoc.json`
- `templates/page.guia-labubu-lkgoc.json`
- `sections/lk-goc-guide-v1.liquid`
- `sections/lk-nb204l-guide-lkgoc.liquid` como referência histórica/204L

## Regra de conteúdo

O Guia LK em `/pages` deve nascer de:

1. evidence packet;
2. Claude SEO como camada de apoio semântico/FAQ/GEO;
3. text packet LK;
4. media manifest quando houver imagens;
5. QA editorial, SEO/GEO, schema e mobile.

## Bloqueios

- Não publicar guia completo diretamente dentro da collection como padrão.
- Não transformar collection em blog post.
- Não criar page guide sem link comercial claro para a collection correspondente.
- Não usar Claude SEO para inventar claims, disponibilidade, estoque ou promessas comerciais.
- Não alterar Production sem aprovação explícita de Lucas.

## Fluxo de publicação

1. Criar/ajustar template de página no theme DEV/unpublished.
2. Criar page/handle no Shopify somente após approval do escopo de write quando aplicável.
3. Validar preview/readback.
4. Linkar collection → Guia LK e Guia LK → collection.
5. QA desktop/mobile, schema/FAQ e leitura semântica.
6. Approval Lucas.
7. Merge/deploy controlado para Production.
8. Receipt + rollback.
