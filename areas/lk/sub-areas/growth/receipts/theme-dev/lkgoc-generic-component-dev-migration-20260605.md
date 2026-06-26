# Receipt — LKGOC componente único no DEV

Data: 2026-06-05T19:06:12
Tema: DEV/unpublished `155065450718`

## Alterações aplicadas
- Criado/atualizado `snippets/lk-goc-collection.liquid` como entrypoint canônico único.
- `sections/lk-collection.liquid` agora chama `lk-goc-collection` para hero e guide das coleções otimizadas.
- Removidas do section chamadas específicas para:
  - `lk-goc-new-balance-9060-*`
  - `lk-goc-new-balance-530-*`
  - `lk-goc-onitsuka-tiger-mexico-66-*`
  - `lk-samba-204l-*`
- Alinhamento do Hero padronizado: collage top = `.coll-banner__crumbs` top.
- “Ler mais” oculto no desktop.

## Readback
- `sections/lk-collection.liquid`: 2 chamadas a `render 'lk-goc-collection'`.
- Section sem `lk-samba-204l` e sem renders específicos LKGOC por coleção.
- `snippets/lk-goc-collection.liquid`: sem renders legados/por coleção; dados ainda em branches internas temporárias.

## QA desktop DEV
```json
[
  {
    "handle": "new-balance-204l",
    "liquidError": false,
    "hero": true,
    "guide": true,
    "legacyCollRich": false,
    "readmoreVisible": false,
    "deltaTop": 0,
    "collageTransform": "matrix(1, 0, 0, 1, 0, -107)"
  },
  {
    "handle": "new-balance-9060",
    "liquidError": false,
    "hero": true,
    "guide": true,
    "legacyCollRich": false,
    "readmoreVisible": false,
    "deltaTop": 0,
    "collageTransform": "matrix(1, 0, 0, 1, 0, -107)"
  },
  {
    "handle": "new-balance-530",
    "liquidError": false,
    "hero": true,
    "guide": true,
    "legacyCollRich": false,
    "readmoreVisible": false,
    "deltaTop": 0,
    "collageTransform": "matrix(1, 0, 0, 1, 0, -107)"
  },
  {
    "handle": "onitsuka-tiger-mexico-66",
    "liquidError": false,
    "hero": true,
    "guide": true,
    "legacyCollRich": false,
    "readmoreVisible": false,
    "deltaTop": 0,
    "collageTransform": "matrix(1, 0, 0, 1, 0, -107)"
  },
  {
    "handle": "adidas-samba",
    "liquidError": false,
    "hero": true,
    "guide": true,
    "legacyCollRich": false,
    "readmoreVisible": false,
    "deltaTop": 0,
    "collageTransform": "matrix(1, 0, 0, 1, 0, -107)"
  }
]

```

## Observação
Production não foi alterado.
