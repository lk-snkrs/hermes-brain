# Skill Surface Diet — recurring audit cron setup

Data: 2026-06-29

## Decisão aplicada

Lucas aprovou seguir com a recomendação: diário read-only, semanal supervisionado e mensal de curadoria pesada.

## Jobs criados

| Job | ID | Schedule UTC | Script | Delivery | Auto-apply |
|---|---|---|---|---|---|
| Daily drift audit | `ce165b7246d3` | `30 5 * * *` | `skill_surface_diet_daily_drift_audit.sh` | origin | não |
| Weekly supervised review | `dbafe9b8bfca` | `45 5 * * 1` | `skill_surface_diet_weekly_review_digest.sh` | origin | não |
| Monthly heavy-skill audit | `27916e815136` | `15 6 1 * *` | `skill_surface_diet_monthly_heavy_audit.sh` | origin | não |

## Contrato

- Scripts no-agent, read-only.
- OK diário imprime stdout vazio, portanto Telegram fica silencioso.
- Weekly/monthly imprimem só quando há findings acionáveis/revisão recomendada.
- Não fazem patch, restart, disable automático, Docker/VPS/Traefik, write externo ou acesso a secrets.
- Relatórios locais em `reports/governance/skill-surface-diet-recurring/`.

## Correção feita durante o teste

O primeiro dry-run detectou `superpowers` desabilitada no `lk-collection-optimizer`. Corrigido com backup e restart scoped somente do LKGOC; novo PID validado: `203750`, Telegram connected, API/webhook off. Depois disso o daily audit ficou silent-OK (`stdout_bytes=0`, `issues=0`).

## Evidência

- `python3 -m py_compile /opt/data/scripts/skill_surface_diet_recurring_audit.py`: OK.
- Wrapper daily: stdout 0 bytes após correção.
- Wrapper weekly: gera digest de revisão quando há warnings/histórico.
- Wrapper monthly: aponta heavy skills enabled para curadoria futura.
- Brain health: ver receipt final.
