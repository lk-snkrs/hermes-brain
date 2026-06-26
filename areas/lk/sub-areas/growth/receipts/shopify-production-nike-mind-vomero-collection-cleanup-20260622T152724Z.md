# Receipt — Shopify production — Nike Mind/Vomero collection cleanup

- Data/hora: 2026-06-22T15:29:32.168894+00:00
- Agente/profile/cron: lk-growth
- Empresa/área: LK/Growth
- Responsável humano: LK Growth
- Pedido original: Lucas aprovou aplicar cleanup de conteúdo/schema do packet nike-mind-vomero-collection-cleanup-20260622 nas URLs /collections/nike-mind-001, /pages/guia-nike-mind-001-002 e /collections/nike-vomero-premium, com stop se exigisse theme.
- Classificação: external-write
- Fontes usadas:
- Aprovação explícita Telegram; packet /areas/lk/sub-areas/growth/approval-packets/nike-mind-vomero-collection-cleanup-20260622/APPROVAL_PACKET.md; Shopify Admin GraphQL readback; QA público HTML.
- O que foi feito:
- Aplicado collectionUpdate apenas em descriptionHtml das collections nike-mind-001 e nike-vomero-premium; SEO title/meta preservados; página guia-nike-mind-001-002 inspecionada e não alterada porque o body Admin não continha o bloco público duplicado.
- Output/artefato:
- Admin userErrors=[] para as duas collections; updatedAt 2026-06-22T15:27:23Z e 2026-06-22T15:27:24Z; public QA confirmou HTTP 200, H1 único e novo conteúdo visível; duplicidade schema restante exige sub-packet theme/dev preview.
- Aprovação: Lucas aprovou no turno atual a frase exata do packet, com limite de não tocar theme production se a duplicação exigisse theme.
- Envio/publicação: Telegram final com resumo e bloqueio/sub-packet.
- Writes externos: Shopify Admin GraphQL collectionUpdate em duas collections production; sem writes em página, theme, preço, estoque, produtos, ordenação, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout.
- Riscos/bloqueios: Schema/guia duplicado persiste em runtime/theme: Mind collection 2 FAQPage, Vomero collection 2 FAQPage parseados; por regra aprovada, parou e gerou sub-packet dev preview.
- Rollback/mitigação: Rollback script: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-collection-cleanup-20260622/rollback_collection_cleanup.py; backup: backup-before-apply.json; executar somente com aprovação explícita.
- Próximos passos: Aguardar aprovação do sub-packet theme dedupe dev preview; rodar impact review D+7 2026-06-29 e D+14 2026-07-06.
- Onde foi documentado no Brain: Workdir: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-collection-cleanup-20260622; apply-result.json; public-qa-after.json; subpacket /approval-packets/nike-mind-vomero-theme-schema-dedupe-20260622/SUBPACKET_THEME_DEDUPE.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.


---
Writer note: receipt content was generated through `/opt/data/scripts/hermes_memory_os_receipt_writer.py` in the active lk-growth profile path and mirrored into the canonical LK Growth Brain path for continuity. values_printed=false.
