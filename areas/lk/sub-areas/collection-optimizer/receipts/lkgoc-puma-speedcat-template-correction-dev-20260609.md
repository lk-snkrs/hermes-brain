# Receipt — Correção LKGOC Puma Speedcat DEV

Data: 2026-06-09
Tema: `lk-new-theme/dev`
Theme ID: `155065450718`
Role: `unpublished`

## Correção feita após feedback de Lucas
Lucas apontou que a execução anterior criou um caminho/template paralelo para Puma Speedcat, em vez de duplicar/adaptar o padrão Shopify já usado na 204L.

## Ajuste aplicado
- `templates/collection.puma-speedcat.json` foi corrigido para ser cópia exata de `templates/collection.json`, o template base usado pela coleção 204L.
- Foi removida a configuração diferente `lkgoc_template_mode: true` desse template específico.
- A coleção existente `puma-speedcat` permanece a coleção-alvo; nenhuma collection nova foi criada.
- Não houve alteração em Production.
- Não houve alteração global/admin da collection nesta correção, para evitar efeito customer-facing sem approval.

## QA pós-correção
Playwright DEV:
- mobile Speedcat: `roleUnpublished:true`, `liquid:false`, `hero:true`, `guide:true`, `productLinks:13`, `visibleBad:false`.
- desktop Speedcat: `roleUnpublished:true`, `liquid:false`, `hero:true`, `guide:true`, `productLinks:13`, `visibleBad:false`.
- comparação gold 204L executada no mesmo QA.

## Guardrail consolidado
Para próximas coleções LKGOC: primeiro duplicar/adaptar o padrão Shopify já aprovado da 204L; depois trocar texto, imagens, links, FAQ e nuances comerciais. Não criar arquitetura/template paralelo sem approval explícito.
