# Approval packet — correção LKGOC para componente único genérico

Data: 2026-06-05T18:44:23

## Motivo
Lucas corrigiu a arquitetura: o padrão LKGOC não deve ser um snippet por coleção. Deve ser um componente único `lk-goc-collection`, com dados por coleção.

## Incidente
Resposta anterior propôs subir snippets `lk-samba-204l-*` para Production. Isso foi erro técnico e já foi marcado como superseded.

## Estado auditado
DEV theme `155065450718`:
- `sections/lk-collection.liquid` ainda tem renders antigos da Samba: `lk-samba-204l-*`.
- há snippets específicos por coleção: `lk-goc-adidas-samba`, `lk-goc-new-balance-9060-*`, `lk-goc-new-balance-530-*`, `lk-goc-onitsuka-*`.

Production theme `155065417950`:
- `sections/lk-collection.liquid` ainda chama `lk-samba-204l-*` para Adidas Samba e causa erro se snippets ausentes.
- 9060/530 ainda usam snippets por coleção.
- não existe `lk-goc-collection`.

## Correção canônica
Criar/migrar para:
- `snippets/lk-goc-collection.liquid`

Chamadas padrão:
```liquid
{% render 'lk-goc-collection', collection: collection, part: 'hero' %}
{% render 'lk-goc-collection', collection: collection, part: 'guide' %}
```

## Coleções no escopo inicial
- `new-balance-204l` — gold source, deve virar referência/dados no componente.
- `new-balance-9060`
- `new-balance-530`
- `onitsuka-tiger-mexico-66`
- `adidas-samba`
- revisar depois: `adidas-samba-jane`, `adidas-sambae` por histórico separado/mais antigo.

## Regras obrigatórias incorporadas
- namespace estrutural `lk-goc-*`;
- não criar novos snippets estruturais por coleção;
- “Ler mais” oculto no desktop;
- topo das imagens alinhado com `.coll-banner__crumbs`;
- sem foto de produto isolado no Hero de sneaker;
- `.coll-rich-content` legado suprimido em coleções otimizadas.

## Execução segura
1. Aplicar primeiro no DEV/unpublished.
2. QA visual por coleção desktop/mobile.
3. Só depois solicitar aprovação de Production.
4. Production rollback: restaurar `sections/lk-collection.liquid` e remover/ignorar snippet genérico.

## Workdir
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-generic-component-migration-20260605`
