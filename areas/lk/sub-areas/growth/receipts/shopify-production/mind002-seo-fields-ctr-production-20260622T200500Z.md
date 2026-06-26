# Receipt — Production Nike Mind 002 SEO fields CTR update

- Data/hora: 2026-06-22T20:06:09.086865+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Growth / Shopify SEO
- Responsável humano: lk-growth
- Pedido original: Lucas aprovou aplicar em produção somente seo.title e seo.description dos 4 PDPs Nike Mind 002 listados no packet mind002-canonical-ctr-packet-20260622, sem body/theme/templates/snippets/collection/produtos além desses campos/preço/estoque/ordenação/descontos/GMC/campanhas/Klaviyo/checkout.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin GraphQL via Doppler; GSC/GA4 read-only; public QA; values_printed=false
- O que foi feito:
- Backup dos 4 produtos; ProductUpdate apenas para seo.title e seo.description; readback Admin dos 4 produtos; QA público head/canonical/schema com amostras cachebuster; rollback script criado.
- Output/artefato:
- growth/work/mind002-ctr-canonical-20260622/apply-seo-result.json; readback-seo-after.json; public-qa-final-seo-samples.json; rollback_mind002_seo.py
- Aprovação: Aprovação explícita de Lucas no turno atual para os 4 PDPs e somente campos SEO.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Shopify Admin productUpdate em 4 produtos; somente seo.title e seo.description.
- Riscos/bloqueios: Algumas amostras públicas ainda refletiram title/meta antigo por cache/propagação Shopify/CDN; Admin readback está correto e maioria das amostras já atualizou. Google pode levar dias/semanas para recrawlar snippets.
- Rollback/mitigação: Executar /opt/data/scripts/hermes_doppler.py run -- python3 growth/work/mind002-ctr-canonical-20260622/rollback_mind002_seo.py para restaurar SEO fields do backup.
- Próximos passos: Revalidar cache em 24h; impact review D+7/D+14 para query nike mind 002, PDPs Mind 002 e hub Mind 001/002.
- Onde foi documentado no Brain: Brain workdir + receipt; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
