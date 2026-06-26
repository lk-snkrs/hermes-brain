# Receipt — Skill quality drift — governance/routing mini-wave

- Data/hora: 2026-06-11T11:52:10.833460+00:00
- Agente/profile/cron: Hermes Geral / Operações Hermes
- Empresa/área: Operações Hermes / Governança / Skills
- Responsável humano: Hermes Geral
- Pedido original: Mesa COO 2026-06-11 Decisão 1/1: fazer mini-onda local para reduzir skill_quality_drift em skills críticas de governança/roteamento.
- Classificação: local-write
- Fontes usadas:
- reports/hermes-daily-score/latest.json; reports/hermes-continuous-improvement/latest.json; /opt/data/scripts/hermes_daily_intelligence_preflight.py skill_quality_audit; skills hermes-brain-governance e multiempresa-routing-lucas.
- O que foi feito:
- Corrigidas menções references/* quebradas em hermes-brain-governance e multiempresa-routing-lucas via 7 bridge references locais; nenhum runtime/cron/gateway/Docker/VPS/prod/external write.
- Output/artefato:
- /opt/data/skills/productivity/hermes-brain-governance/references/bruno-hermes-7-steps-agent-operating-model-20260604.md; /opt/data/skills/productivity/hermes-brain-governance/references/paused-cron-stale-status-remediation-20260610.md; /opt/data/skills/productivity/multiempresa-routing-lucas/references/hermes-governance-audit-runtime-readonly-20260525.md; /opt/data/skills/productivity/multiempresa-routing-lucas/references/lk-shopify-specialist-profile-prd-guardrail-20260526.md; /opt/data/skills/productivity/multiempresa-routing-lucas/references/lk-stock-routing-canon-pronta-entrega-estoque-20260608.md; /opt/data/skills/productivity/multiempresa-routing-lucas/references/seo-geo-handoff-20260518.md; /opt/data/skills/productivity/multiempresa-routing-lucas/references/zipper-artist-texts-map-20260518.md
- Aprovação: Lucas respondeu Fazer à decisão Mesa COO; escopo interpretado como local/documental/skills apenas.
- Envio/publicação: Telegram: resumo executivo; receipt Brain local.
- Writes externos: 0
- Riscos/bloqueios: Scanner skill_quality_audit ainda marca as duas skills por contains_staleness_marker porque termos legacy/deprecated/stale são vocabulário legítimo de governança; missing_reference_count ficou 0 nas duas.
- Rollback/mitigação: Remover os 7 bridge references criados ou substituir por cópias completas dos arquivos canônicos se a curadoria preferir.
- Próximos passos: Próxima onda: tratar falsos positivos de contains_staleness_marker no audit ou quebrar skills grandes/legadas por referências menores.
- Onde foi documentado no Brain: Receipt escrito via Memory OS writer; readback, Brain health, operational docs guard e focused secret scan executados.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
