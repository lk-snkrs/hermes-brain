# Receipt — DEV theme preview — Nike Mind/Vomero schema dedupe

- Data/hora: 2026-06-22T16:49:06.001568+00:00
- Agente/profile/cron: lk-growth
- Empresa/área: LK/Growth
- Responsável humano: LK Growth
- Pedido original: Lucas aprovou criar dev preview para deduplicar blocos de theme/schema nas páginas Nike Mind e Vomero, sem publicar produção.
- Classificação: external-write
- Fontes usadas:
- Aprovação explícita Telegram; subpacket nike-mind-vomero-theme-schema-dedupe-20260622; Shopify Theme API DEV theme 155065450718; QA público preview.
- O que foi feito:
- Aplicado write somente no Shopify DEV theme 155065450718 em 4 snippets: desativação de blocos legacy duplicados e preservação de um FAQPage por collection.
- Output/artefato:
- Preview QA: Mind collection HTTP 200 H1=1 FAQPage=1; Mind guide HTTP 200 H1=1 FAQPage=1; Vomero collection HTTP 200 H1=1 FAQPage=1; sem Liquid error; production não alterada.
- Aprovação: Lucas: Aprovo / Liberei / Aprovei para executar dev preview; sem production publish.
- Envio/publicação: Telegram com resumo e próximos passos.
- Writes externos: Shopify Theme API write em DEV theme 155065450718 somente; zero production theme publish; zero product/collection/preço/estoque/GMC/campanhas/Klaviyo/checkout writes.
- Riscos/bloqueios: Preview altera aparência/schema apenas no dev theme; produção continua com duplicidade até aprovação específica de merge production.
- Rollback/mitigação: Rollback DEV script: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-theme-dedupe-dev-20260622/rollback_dev_theme_dedupe.py; backups em dev-theme-backup-before/.
- Próximos passos: Se Lucas aprovar após preview/QA, preparar production merge approval packet com diff/readback/rollback.
- Onde foi documentado no Brain: Workdir: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/nike-mind-vomero-theme-dedupe-dev-20260622; apply-dev-theme-result.json; preview-public-qa-after.json.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.


---
Mirrored from active lk-growth profile receipt_writer output to canonical Brain path. values_printed=false.
