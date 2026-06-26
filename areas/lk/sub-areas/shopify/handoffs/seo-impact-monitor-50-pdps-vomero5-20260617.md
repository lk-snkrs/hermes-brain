# Handoff — SEO Impact Monitor 50 PDPs + Nike Vomero 5

Data: 2026-06-17
values_printed=false

## Contexto
Lucas autorizou criar o monitor para medir efeito das mudanças SEO/GEO feitas em Shopify.

## Escopo
- 50 PDPs com `seo.title` e `seo.description` controlados.
- Coleção `nike-vomero-5` com SEO/GEO/FAQ/schema validado.
- Sem writes externos neste handoff; somente leitura e arquivos locais/Brain.

## Evidência criada
- Baseline D0: `areas/lk/sub-areas/shopify/reports/assets/seo-impact-monitor-20260617/baseline_d0.md`
- Dados completos: `areas/lk/sub-areas/shopify/reports/assets/seo-impact-monitor-20260617/baseline_d0.json`
- Targets: `areas/lk/sub-areas/shopify/reports/assets/seo-impact-monitor-20260617/monitor_targets.json`
- Schedule: `areas/lk/sub-areas/shopify/reports/assets/seo-impact-monitor-20260617/monitor_schedule.json`
- Runner: `/opt/data/hermes_bruno_ingest/scripts/lk_seo_impact_monitor.py`

## Baseline D0 resumido
- URLs monitoradas: 51.
- Public URLs OK: 51/51.
- Title/meta batendo na primeira rodada: 50/51.
- Observação: único mismatch público foi `tenis-adidas-tokyo-mj-core-black-cream-white-gold-metallic-preto`; retry lento alternou 2/4 novo e 2/4 antigo, compatível com cache/CDN intermitente. Admin/readback anterior estava correto; sem Liquid error.
- Liquid errors: 0.
- Vomero 5 FAQ/schema marker: true.
- GSC baseline 2026-05-18 → 2026-06-15: 9.742 impressões, 47 cliques, CTR agregado 0,48%, 49 páginas com impressões.
- GA4 baseline 2026-05-18 → 2026-06-15: 6.067 sessions, 5.707 totalUsers, 6.469 screenPageViews, 3.841 engagedSessions.

## Reminder OS loop needed
Yes.

## Reminder OS owner
LK Shopify / profile lk-shopify.

## Reminder OS next action
Rodar leitura read-only D+7/D+14/D+28 com o runner e comparar contra o baseline D0; não executar Shopify/GMC/Klaviyo/theme writes.

## Reminder OS review trigger
- D+7: 2026-06-24T12:00:00Z
- D+14: 2026-07-01T12:00:00Z
- D+28: 2026-07-15T12:00:00Z

## Reminder OS evidence
Este handoff + baseline/schedule listados acima. Entradas registradas em `areas/operacoes/reminder-os/reminders.jsonl`.

## Bloqueios / riscos
- GSC atrasa ~2-3 dias; análises devem usar janela encerrando 3 dias antes.
- Um PDP mostrou cache/CDN intermitente na primeira medição; acompanhar no D+7 se estabilizou.
- GA4 respondeu somente métricas de tráfego/engajamento no baseline gerado; se precisarmos conversão por PDP, validar disponibilidade de eventos/nomes no próximo ciclo.

## Writes externos
Nenhum.
