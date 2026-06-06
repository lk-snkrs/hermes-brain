# Receipt — correção DEV Guia LK canônico LKGOC

Data UTC: 2026-06-05T10:36:37Z

## Aprovação
Lucas aprovou seguir e corrigir o padrão do Guia LK dentro das coleções.

## Ambiente
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado por API antes do write: `unpublished`
- Produção/main: não tocada.

## Assets alterados em DEV
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-204l-guide-panel.liquid`
- `snippets/lk-goc-new-balance-9060-guide-panel.liquid`

## Correção
- Removido contrato específico do 9060: `lk-goc-nb9060-guide-204l-parity-20260605`.
- Criado contrato canônico: `lk-goc-guide-panel-canonical-contract-20260605`.
- Snippets 204L e 9060 agora carregam classe canônica `lk-goc-guide-panel` e aliases internos `lk-goc-guide-*`, mantendo compatibilidade com `lk-lkgoc-*` e `lk-guide-standard-*`.

## QA
- Mobile 390px: contrato canônico carregado, style específico removido, guia 9060 e 204L com `lk-goc-guide-panel`.
- Desktop 1440px: ambos com grid `919.281px 300px`, background `rgb(247,244,239)`, padding/margem/estrutura equivalentes.
- Título/subtítulo mobile do hero 9060 preservados após a mudança.

## Evidências
- `guide-canonical-compare-after.json`
- `new-balance-9060-390-after-canonical-guide.png`
- `new-balance-204l-390-after-canonical-guide.png`
- `new-balance-9060-1440-after-canonical-guide.png`
- `new-balance-204l-1440-after-canonical-guide.png`

## Rollback
Restaurar arquivos `.before` deste diretório para os três assets listados acima.
