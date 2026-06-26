# Receipt — Hotfix escopo template SL72

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Motivo: auditoria pós-v6 detectou bloco SL72 renderizando em collections que usavam o template base `collection.json`, incluindo Adidas Samba e New Balance 204L.

## Problema

O bloco visual v6 SL72 foi adicionado ao `templates/collection.json` base. Como algumas collections usam esse template global, o bloco apareceu fora do cluster SL72.

## Correção executada

- Criado `templates/collection.sl72-ai-v6.json` com a seção `lk_sl72_ai_v6`.
- Removido `lk_sl72_ai_v6` de `templates/collection.json` global.
- Collection `adidas-sl-72` teve `template_suffix` ajustado para `sl72-ai-v6`.

## Readback Admin

- `base_has_sl72`: false.
- `dedicated_has_sl72`: true.
- `collection_template_suffix`: `sl72-ai-v6`.
- `collection_id`: `437668380894`.

## Readback público por script

- `/collections/adidas-samba`: sem `lk-goc-sl72`, sem texto “Adidas SL 72 original no Brasil”, sem `Liquid error`.
- `/collections/new-balance-204l`: sem `lk-goc-sl72`, sem texto “Adidas SL 72 original no Brasil”, sem `Liquid error`.
- `/collections/adidas-sl-72`: mantém `lk-goc-sl72`, texto SL72 e sem `Liquid error`.

## Regra adicionada ao padrão operacional

Para próximos lotes: nunca adicionar seção de cluster específico diretamente ao `templates/collection.json` base sem condicional ou template dedicado. Preferência: `templates/collection.<cluster>.json` + `template_suffix` da collection alvo.

## Rollback

Snapshots em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/fix-sl72-template-scope-20260618/snapshots-before/`
