# LKGOC — Workflow DEV → approval → production

## Fluxo obrigatório

1. Abrir `LKGOC-PADRAO-CANONICO.md` e `references/LKGOC-BEFORE-NEW-COLLECTION-CHECKLIST-20260605.md`.
2. Definir nível: Full / Lite / Correção / Não-LKGOC.
3. Preencher `LKGOC-INPUT-CONTRACT.md`.
4. Preencher `LKGOC-EVIDENCE-PACKET.md`.
5. Aplicar Claude SEO: `seo-content`, `seo-ecommerce`, `seo-page`, `seo-geo`, `seo-dataforseo` quando houver SERP/dados.
6. Criar copy usando `templates/lkgoc-copy-template.md`.
7. Criar/validar visual usando `templates/lkgoc-liquid-contract.md`.
8. Preparar coleção + guia juntos.
9. Materializar em Shopify DEV/preview quando houver visual.
10. Fazer readback de asset/HTML/SEO relevante.
11. Tirar screenshot desktop e mobile.
12. Rodar `LKGOC-SCORECARD-100.md`; score mínimo recomendado para approval: 85/100.
13. Enviar approval packet curto no Telegram com links diretos, score, evidências, limitações e decisão pedida.
14. Só aplicar production com aprovação explícita atual.
15. Production: backup/rollback, diff/readback, receipt, cache check.
16. Agendar ou registrar impacto D+7/D+14/D+30 conforme `LKGOC-IMPACT-REVIEW.md`.

## Approval packet mínimo

- Nível LKGOC:
- Link preview Shopify DEV (`preview_theme_id` quando aplicável):
- Coleção:
- Guia:
- Score LKGOC:
- Evidências usadas:
- Limitações:
- Riscos/rollback:
- Decisão pedida:
