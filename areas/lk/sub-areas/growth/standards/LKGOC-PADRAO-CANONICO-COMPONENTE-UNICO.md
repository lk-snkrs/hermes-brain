# LKGOC — padrão canônico de componente único

Atualizado em: 2026-06-05T19:06:12

## Princípio
LKGOC é um **sistema único de coleção otimizada**, não um conjunto de snippets por coleção.

## Componente canônico
- `snippets/lk-goc-collection.liquid`

## Render canônico no section
Hero:
```liquid
{% render 'lk-goc-collection', collection: collection, part: 'hero' %}
```
Guia pós-grid:
```liquid
{% render 'lk-goc-collection', collection: collection, part: 'guide' %}
```

## Dados por coleção
A variação por coleção deve ser tratada como **dados**, não como layout novo:
- título/headline;
- kicker;
- descrição curta;
- imagens editoriais;
- alt/caption;
- cards do guia;
- FAQ;
- CTA/link;
- schema.

Estado temporário permitido no DEV atual: branch `case collection.handle` dentro do componente único. Próxima evolução recomendada: migrar esses dados para metafields/metaobjects.

## Contratos visuais obrigatórios
- classes estruturais novas: `lk-goc-*`;
- Hero desktop: topo do bloco de imagens alinhado ao topo de `.coll-banner__crumbs`;
- “Ler mais” oculto no desktop;
- Hero de sneaker com imagem editorial/validação social, não foto de produto isolado;
- guia pós-grid no padrão LKGOC;
- FAQ legado `.coll-rich-content` suprimido em coleções otimizadas;
- dev/unpublished → QA → approval Lucas → Production.

## Coleções migradas para render canônico no DEV em 2026-06-05
- `new-balance-204l`
- `new-balance-9060`
- `new-balance-530`
- `onitsuka-tiger-mexico-66`
- `adidas-samba`

## Próximas padronizações recomendadas
1. Data contract em metafields/metaobjects.
2. Token único de espaçamento/tipografia.
3. Contrato único de imagens: proporção, object-position, fonte editorial e créditos internos.
4. QA automático obrigatório por coleção: Liquid error, hero, guia, FAQ legado, read-more desktop e alinhamento breadcrumb.
5. Schema/FAQ gerado do mesmo dataset visível.
6. Remoção progressiva dos snippets antigos por coleção após migração completa para dados.


## Priorização de novas coleções

Antes de escolher a próxima coleção, aplicar a regra: `rules/REGRA-LKGOC-PRIORIZACAO-POR-SCORE-DE-MARCA-E-FENOMENO.md`. Volume SEO sozinho não decide; o score de marca/modelo e o fenômeno LK vêm primeiro.

## Regras visuais complementares

- `rules/REGRA-LKGOC-IMAGENS-EM-USO-NAO-PACKSHOT.md` — heroes LKGOC devem usar imagens de pessoas usando o produto/contexto editorial, não packshot.

- `rules/REGRA-LKGOC-IMAGENS-ALINHAMENTO-BOTTOM.md` — imagens editoriais/de uso em heroes LKGOC devem alinhar pelo bottom, não pelo meio.

- `rules/REGRA-LKGOC-GUIA-POS-GRID-PADRAO.md` — guia pós-grid deve copiar a estrutura standard aprovada, sem variação visual por coleção.

- `rules/REGRA-LKGOC-FAQ-UNICA-DENTRO-DO-GUIA.md` — em LKGOC só pode haver uma FAQ visível, dentro do guia editorial.
