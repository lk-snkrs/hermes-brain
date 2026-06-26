# Regra LKGOC — componente genérico único

Registrado em: 2026-06-05T18:43:59

## Regra obrigatória
O LKGOC deve caminhar para **um componente estrutural único**, não um snippet por coleção.

Nome canônico preferencial:
- `snippets/lk-goc-collection.liquid`

Render canônico:
```liquid
{% render 'lk-goc-collection', collection: collection, part: 'hero' %}
{% render 'lk-goc-collection', collection: collection, part: 'guide' %}
```

## O que não fazer
Não criar novos snippets estruturais por coleção, como:
- `lk-goc-adidas-samba`
- `lk-goc-new-balance-9060-*`
- `lk-goc-onitsuka-*`
- `lk-samba-204l-*`

## Exceção temporária
Durante migração, dados podem ficar em `case collection.handle` dentro do componente genérico, mas o markup/CSS/JS estrutural deve ser único.

## Objetivo final
Dados por coleção devem migrar para metafields/metaobjects ou data map central, mantendo um único componente visual.

## QA obrigatório
Para qualquer coleção LKGOC:
- section chama `lk-goc-collection`;
- classes estruturais usam `lk-goc-*`;
- “Ler mais” oculto em desktop;
- topo das imagens alinhado com `.coll-banner__crumbs`;
- `.coll-rich-content` legado suprimido;
- hero de sneaker não usa foto de produto isolado.
