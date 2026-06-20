# Approval packet — LKGOC v4 slim dominance hotfix DEV → Production

- Data UTC: 2026-06-19T16:20:12.206024+00:00
- Origem: QA production encontrou CSS duplicado/competindo nas 4 coleções.
- DEV aplicado: `lk-new-theme/dev` / `155065450718` / role `unpublished`.
- Asset alterado no DEV: `assets/lk-collection-v2.css`.
- Production: **não alterada ainda**.

## O que o hotfix faz

- Consolida o padrão v4 slim como regra dominante do bloco `.coll-rich-content`.
- Remove grid antigo de duas colunas do wrapper interno.
- Mantém desktop compacto com cards em 3 colunas.
- Mantém mobile empilhado.
- Troca o Resumo LK para fundo branco/claro, sem bloco preto.
- Mantém labels editoriais `Guia LK` e `Resumo LK`.

## QA DEV

Status: OK

Evidência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260619T-dev-v4-slim-dominance-hotfix-qa/QA-REPORT.md`

## Impacto esperado

- Estabilizar as 4 coleções atuais antes de escalar novo batch.
- Reduzir inconsistência visual por CSS antigo/fallback.
- Manter conteúdo GEO/AI visibility sem alterar copy visível de produto/preço/estoque.

## Risco

- Baixo a médio: CSS global para `.coll-rich-content` em collection pages.
- Mitigação: QA DEV desktop/mobile já feito; rollback por asset CSS.

## Rollback

- Restaurar asset production anterior `assets/lk-collection-v2.css` a partir do backup criado no momento do merge.
- Revalidar 4 URLs públicas.

## Aprovação necessária

Para aplicar em production, Lucas precisa aprovar explicitamente algo como:

> aprovado merge production do hotfix v4 slim dominance

Sem essa frase/aprovação, não executar write em production.
