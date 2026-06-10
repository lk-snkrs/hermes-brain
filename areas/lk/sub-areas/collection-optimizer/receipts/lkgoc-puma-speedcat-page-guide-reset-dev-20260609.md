# Receipt — Puma Speedcat Guia LK `/pages` Reset DEV

Data: 2026-06-09  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role: `unpublished`

## Contexto
Lucas reprovou a execução anterior porque a Speedcat estava sendo tratada como adaptação de collection, diferente do padrão correto. Diagnóstico confirmado: o gold source canônico para novos Guias LK é a página `/pages/new-balance-204l-original-brasil-guia-lk`, não a collection 204L.

## Ações executadas

### 1. Limpeza da tentativa errada na collection
Asset alterado em DEV:
- `sections/lk-collection.liquid`

Removido:
- bloco custom `collection.handle == 'puma-speedcat'`;
- render `lk-goc-puma-speedcat-guide-panel` no pós-grid;
- asset `snippets/lk-goc-puma-speedcat-guide-panel.liquid` deletado do DEV.

Readback da collection Speedcat DEV:
- status: `200`
- role unpublished: `1`
- `Liquid error`: `0`
- `Guia editorial Puma Speedcat`: `0`
- `Puma Speedcat original: guia LK`: `0`

### 2. Reconstrução correta como Guia LK em `/pages`
Gold source usado:
- `templates/page.nb204l-guide.json`
- section: `lk-goc-guide-v1`
- referência pública gold: `/pages/new-balance-204l-original-brasil-guia-lk`

Asset criado/atualizado em DEV:
- `templates/page.guia-puma-speedcat-lkgoc.json`

Page object atualizado como draft:
- id: `128209486046`
- handle: `guia-puma-speedcat`
- title: `Guia Puma Speedcat Original Brasil | LK Sneakers`
- template_suffix: `guia-puma-speedcat-lkgoc`
- published_at: `null`

## QA estático do template
Resultado: aprovado.

Checks:
- mesma section type do gold: true
- mesmo tamanho de block_order: true
- mesmos block IDs: true
- mesmos block types: true
- mesmas settings keys: true
- settings dentro do schema: true
- block settings dentro do schema: true
- referências `204L`: 0
- referências `New Balance`: 0
- contém `Puma Speedcat`: true
- linguagem proibida de estoque/pronta entrega: 0

Contagem:
- blocks: `49`
- order: `49`
- settings: `56`

## Bloqueio atual
A Page `guia-puma-speedcat` está `published_at: null`, então a URL pública/preview retorna 404 mesmo com `preview_theme_id`.

Publicar a Page é ação customer-facing. Pela regra LK, não foi executado sem aprovação explícita de Lucas.

## Próximo passo para QA visual real
Lucas precisa aprovar uma destas opções:
1. publicar temporariamente a Page draft para QA visual em DEV e depois decidir Production; ou
2. aprovar publicação definitiva da Page/Guia quando o QA visual for validado.

Production/theme `main` não foi alterado.
