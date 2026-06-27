# Receipt — Elle Brain v2 — OpenRouter diagnostics and token budget fix

- Data/hora: 2026-06-26T18:26:24.064733+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas disse seguir após rodada 100 indicar 76/100 valid_json; investigar invalid_json_or_empty sem conteúdo sensível e melhorar structured output.
- Classificação: local-write
- Fontes usadas:
- Runtime elle-chatwoot; shadow runner com diagnostics sanitizados; OpenRouter classify-only; reports raw sanitizados no Brain; values_printed=false.
- O que foi feito:
- Adicionada observabilidade sanitizada de provider response shape; diagnosticado finish_reason=length como causa principal; aumentado token budget no v2 paralelo; regressões 34 OK.
- Output/artefato:
- Antes do token budget: 42/50 valid_json, 8 invalid, finish_reason length=22. Depois: 49/50 valid_json, 1 invalid, finish_reason length=1; app_py_matches_backup=true; writes_external=0.
- Aprovação: Continuidade local/shadow aprovada por Lucas via “Seguir”; sem autorização para canary/prod/send.
- Envio/publicação: Nenhum envio a cliente; nenhum canary; nenhuma alteração do app.py produtivo; OpenRouter somente classify-only/shadow.
- Writes externos: 0
- Riscos/bloqueios: Amostra 50 bateu 98%, mas gate oficial ainda exige live_limit=100 >=95% e revisão qualitativa dos diffs; canary segue no-go até isso.
- Rollback/mitigação: Restaurar /app/elle_brain_v2.py a partir de /opt/data/backups/elle-brain-v2-openrouter-tokenbudget/20260626T181839Z ou /opt/data/backups/elle-brain-v2-openrouter-diagnostics/20260626T180956Z; app.py não foi alterado.
- Próximos passos: Rodar rodada-gate live_limit=100 com novo token budget; se >=95%, revisar diffs qualitativos antes de approval packet de canary.
- Onde foi documentado no Brain: Report: areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-brain-v2-openrouter-diagnostics-tokenbudget-20260626.md; raw: reports/elle-brain-v2/openrouter-diagnostics-tokenbudget-raw-20260626/; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
