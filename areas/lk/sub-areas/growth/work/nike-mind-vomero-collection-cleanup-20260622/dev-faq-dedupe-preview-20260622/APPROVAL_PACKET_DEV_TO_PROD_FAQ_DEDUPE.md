# Approval packet — Nike Mind / Vomero FAQ schema dedupe DEV → Production

- Criado UTC: 2026-06-22T15:37:20.117817+00:00
- Owner: LK Growth + LKGOC surface.
- Escopo: corrigir duplicidade pública de FAQPage/schema em collections Nike Mind 001 e Nike Vomero Premium.
- DEV aplicado: `lk-new-theme/dev` / `155065450718` / role `unpublished` verificado por API.
- Production: **não alterada nesta etapa**.
- values_printed=false.

## Problema confirmado em production fresh

| URL | FAQPage JSON-LD | Outros sinais | Causa provável |
|---|---:|---|---|
| `/collections/nike-mind-001` | 2 | seção extra `lk-growth-nike-mind-geo` presente | snippet legado global `lk-growth-nike-mind-seo-geo-preview` renderizado no layout + guia da collection |
| `/collections/nike-vomero-premium` | 2 | microdata FAQPage também presente | schema global `lk-growth-geo-faq-schema` + guia Vomero com JSON-LD e microdata |

## Patch aplicado no DEV/unpublished

| Asset DEV | Ação |
|---|---|
| `snippets/lk-growth-nike-mind-seo-geo-preview.liquid` | Desativado no DEV com guard `{% if false %}` porque a collection já tem guia/schema canônico via `lk-nike-mind-guide-panel`. |
| `snippets/lk-growth-geo-faq-schema.liquid` | Desativado apenas o branch legado de `/collections/nike-vomero-premium` no DEV; demais branches preservados. |
| `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid` | Removidos atributos microdata do FAQ visual; JSON-LD único permanece como schema canônico. |

## QA DEV

Preview via `preview_theme_id=155065450718`:

| URL DEV | HTTP | H1 | FAQPage string | FAQPage JSON-LD | Liquid error |
|---|---:|---:|---:|---:|---|
| `/collections/nike-mind-001?preview_theme_id=155065450718` | 200 | 1 | 1 | 1 | false |
| `/collections/nike-vomero-premium?preview_theme_id=155065450718` | 200 | 1 | 1 | 1 | false |

## Evidências locais

- Receipt DEV: `dev-apply-receipt.json`
- Backup DEV antes dos assets: `backup-before-dev-faq-dedupe.json`
- QA DEV: `dev-preview-public-qa.json`
- Busca read-only de origem: `../theme-readonly-investigation/theme-faq-injection-search.json`

## Impacto esperado

- Reduzir ambiguidade de schema para Google/LLMs.
- Manter um único FAQPage canônico por collection.
- Remover bloco visual legado duplicado de Nike Mind sem tocar copy de produto/preço/estoque.

## Risco

- Baixo/médio: patch em snippets globais, mas escopado por condição.
- O branch global de Vomero deixa de emitir FAQPage legado; o guia da collection assume como fonte canônica.
- O snippet Nike Mind legado é desativado inteiro; hoje ele só renderiza quando canonical contém `/collections/nike-mind-001`.

## Rollback

- Restaurar os 3 assets production a partir do backup criado no momento do merge ou do backup DEV `backup-before-dev-faq-dedupe.json` se o merge replicar exatamente este patch.
- Revalidar as 2 URLs públicas: H1=1, HTTP=200, FAQPage retorna ao estado anterior se rollback for necessário.

## Aprovação necessária

Para aplicar em production, Lucas precisa aprovar explicitamente algo como:

> aprovado merge production dedupe FAQPage Nike Mind e Vomero

Sem aprovação explícita, manter somente em DEV/unpublished.
