# Daily Intelligence P1 hardening — 2026-06-08

## Escopo aprovado por Lucas

Lucas aprovou executar a próxima leva P1 local para o cron 02h, sem Docker/SSH/Hostinger/gateway/externos/secrets.

## Implementado

1. `hermes_daily_intelligence_preflight.py` evoluiu para schema `lc_hermes_daily_intelligence_preflight.v2`.
2. Preflight agora inclui:
   - tendência de score dos últimos 7 dias (`score_trend_7d`);
   - deduplicação local de alertas (`reports/hermes-alert-dedupe/latest.json`);
   - presença Doppler por mapa universal do helper, sem valores (`values_printed=false`);
   - lista estruturada `blocked_by_approval`;
   - release watch local (`reports/hermes-release-watch/latest.json`).
3. Novo validador pós-run:
   - script: `/opt/data/scripts/hermes_daily_intelligence_artifact_validator.py`;
   - recibos: `reports/governance/daily-intelligence-artifact-validation-YYYY-MM-DD.json` e `latest.json`.
4. Cron 02h `f5a23dd6a1bd` atualizado para usar os novos campos e rodar o validador pós-run depois de escrever artefatos.

## Guardrails preservados

- Sem Docker/VPS/SSH/Traefik/gateway restart.
- Sem mudanças em secrets ou impressão de valores.
- Sem writes externos, Shopify/Tiny/GMC/Ads/WhatsApp/email/customer/supplier.
- Sem novo cron criado; apenas prompt do cron 02h existente foi atualizado conforme aprovação explícita.

## Verificação

- `python3 -m py_compile /opt/data/scripts/hermes_daily_intelligence_preflight.py /opt/data/scripts/hermes_daily_intelligence_artifact_validator.py`: OK.
- `python3 /opt/data/scripts/hermes_daily_intelligence_preflight.py`: OK; schema v2; 15 perfis no inventário Doppler; tendência 7 dias estável; 4 itens estruturados em `blocked_by_approval`; release watch sem nova tag após segunda execução.
- `python3 /opt/data/scripts/hermes_daily_intelligence_artifact_validator.py --date 2026-06-08`: OK; `failures=[]`.
- Recibos locais criados e lidos.

## Observações

O preflight encontrou alertas recorrentes locais via dedupe. Eles serão classificados como recorrentes no próximo 02h, evitando que o relatório trate tudo como novidade.

`values_printed=false`.
