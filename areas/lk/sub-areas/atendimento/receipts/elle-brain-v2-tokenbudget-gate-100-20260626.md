# Receipt — Elle Brain v2 — token budget gate 100 passed

- Data/hora: 2026-06-26T18:40:02.952105+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Hermes LK Ops
- Pedido original: Rodada-gate live_limit=100 com token budget novo para validar structured output antes de considerar canary.
- Classificação: local-write
- Fontes usadas:
- Runtime elle-chatwoot; shadow runner OpenRouter classify-only; report raw sanitizado; values_printed=false.
- O que foi feito:
- Copiado report bruto da rodada 100 para Brain; criado report executivo; gate técnico de structured output avaliado.
- Output/artefato:
- live_used=100; valid_json=99; invalid_json_or_empty=1; valid_json_rate=99%; finish_reason length=4; writes_external=0.
- Aprovação: Continuidade local/shadow aprovada por Lucas via “Seguir”; sem autorização para canary/prod/send.
- Envio/publicação: Nenhum envio a cliente; nenhum canary; nenhuma alteração do app.py produtivo; OpenRouter somente classify-only/shadow.
- Writes externos: 0
- Riscos/bloqueios: Gate técnico passou, mas canary ainda exige revisão qualitativa dos 57 category diffs e 44 handoff diffs vs legado, mais approval packet escopado.
- Rollback/mitigação: Nenhum rollback produtivo necessário; artefatos paralelos podem ser restaurados dos backups /opt/data/backups/elle-brain-v2-openrouter-tokenbudget/20260626T181839Z e /opt/data/backups/elle-brain-v2-openrouter-diagnostics/20260626T180956Z.
- Próximos passos: Revisar qualitativamente diffs vs legado e preparar approval packet de canary limitado se não houver promessa proibida/risco.
- Onde foi documentado no Brain: Report: areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-brain-v2-tokenbudget-gate-100-20260626.md; raw: reports/elle-brain-v2/tokenbudget-gate-100-raw-20260626/; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
