# Receipt — Production theme — Nike Mind/Vomero schema dedupe merge

- Data/hora: 2026-06-22T17:06:17.359048+00:00
- Agente/profile/cron: lk-growth
- Empresa/área: LK/Growth
- Responsável humano: LK Growth
- Pedido original: Lucas aprovou aplicar no Shopify production theme 155065417950 somente o merge dos 4 snippets validados no DEV para deduplicar schema/blocos de Nike Mind e Vomero.
- Classificação: external-write
- Fontes usadas:
- Aprovação explícita Telegram; DEV preview QA; Shopify Theme API production; QA público production.
- O que foi feito:
- Aplicado write no production theme 155065417950 nos 4 snippets aprovados; backups production salvos; readback asset exact confirmado em verificação posterior.
- Output/artefato:
- Schema dedupe OK: Mind collection FAQPage=1, Mind guide FAQPage=1, Vomero collection FAQPage=1; HTTP 200, H1 único e sem Liquid error. Pendência: alguns blocos visuais legacy ainda aparecem por assets/sections/templates fora dos 4 aprovados.
- Aprovação: Lucas aprovou frase escopada para production theme 155065417950 e 4 snippets listados.
- Envio/publicação: Telegram com resumo, QA e pendência.
- Writes externos: Shopify Theme API write em production theme nos 4 snippets; sem theme publish, sem produtos, preço, estoque, ordenação, desconto, PDP, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout.
- Riscos/bloqueios: Objetivo de schema foi atingido; dedupe visual completo exige novo packet porque há blocos legacy fora dos 4 snippets aprovados.
- Rollback/mitigação: Rollback production script: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-production-merge-20260622/rollback_production_theme_merge.py; backups em production-backup-before/.
- Próximos passos: Preparar read-only asset map e novo approval packet/DEV preview para blocos visuais restantes se Lucas quiser finalizar visual cleanup.
- Onde foi documentado no Brain: Workdir: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-production-merge-20260622; production-public-qa-after.json; production-readback-verify.json; follow-up packet nike-mind-vomero-remaining-theme-blocks-20260622.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.


---
Mirrored from active lk-growth profile receipt_writer output to canonical Brain path. values_printed=false.
