# Receipt — Production merge FAQPage dedupe Nike Mind + Vomero

- Data UTC: 2026-06-22T16:15:52.781484+00:00
- Aprovação Lucas: `Aprovo merge`
- Tema production: `lk-new-theme/production` / `155065417950` / role `main` verificado por API.
- Escopo: deduplicação de `FAQPage` nas collections Nike Mind 001 e Nike Vomero Premium.
- values_printed=false.

## Writes executados

| Asset production | Status |
|---|---|
| `snippets/lk-growth-nike-mind-seo-geo-preview.liquid` | Desativado para não duplicar schema/guia da collection Nike Mind |
| `snippets/lk-growth-geo-faq-schema.liquid` | Branch legado de `/collections/nike-vomero-premium` desativado |
| `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid` | Microdata FAQ removido; JSON-LD único mantido |

## QA público final

| URL | HTTP | H1 | FAQPage string | FAQPage JSON-LD | Legado removido | Liquid error |
|---|---:|---:|---:|---:|---|---|
| `/collections/nike-mind-001` | 200 | 1 | 1 | 1 | `lk-growth-nike-mind-geo=false` | false |
| `/collections/nike-vomero-premium` | 200 | 1 | 1 | 1 | schema global/microdata=false | false |

## Observação técnica

O primeiro receipt teve `readback_ok=false` no asset Nike Mind por comparação imediata, mas o readback posterior confirmou o marker production e o guard `if false` aplicados. O QA público final confirmou o efeito real: 1 único `FAQPage`.

## Rollback

Backup completo antes do merge:

`backup-before-production-merge.json`

Para rollback:
1. Restaurar os 3 assets production a partir do backup.
2. Revalidar `/collections/nike-mind-001` e `/collections/nike-vomero-premium`.
3. Confirmar HTTP 200, H1 único e retorno ao estado anterior se necessário.

## Evidências

- Receipt JSON: `production-merge-receipt.json`
- QA público: `production-public-qa-after-merge.json`
- HTML pós-merge salvo em `public-prod-after-mind.html` e `public-prod-after-vomero.html`
