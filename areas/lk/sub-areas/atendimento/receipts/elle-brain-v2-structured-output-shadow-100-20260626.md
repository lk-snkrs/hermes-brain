# Receipt — Elle Brain v2 — shadow live 100 structured output result

- Data/hora: 2026-06-26T17:45:18.756294+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Hermes LK Ops
- Pedido original: Rodada assíncrona maior live_limit=100 para validar se structured output/retry da Elle Brain v2 sustentava o critério antes de canary.
- Classificação: local-write
- Fontes usadas:
- Runtime elle-chatwoot; report do runner resgatado de /tmp/elle-brain-v2-structured-shadow-100 no container; logs sanitizados; values_printed=false.
- O que foi feito:
- Copiado report bruto da rodada 100 para Brain; report principal atualizado com resultado real; canary mantido no-go.
- Output/artefato:
- live_openrouter_used=100; valid_json=76; invalid_json_or_empty=24; valid_json_rate=76%; processed_seen=156; category_diff_count=55; handoff_diff_count=41; writes_external=0.
- Aprovação: Continuidade local/shadow aprovada por Lucas via “Seguir”; sem autorização para canary/prod/send.
- Envio/publicação: Nenhum envio a cliente; nenhum canary; nenhuma alteração do app.py produtivo; OpenRouter somente classify-only/shadow.
- Writes externos: 0
- Riscos/bloqueios: Structured output ainda abaixo do critério >=95%; canary bloqueado. Background process exit code 1 foi erro de caminho host pós-run, não falha do runner principal.
- Rollback/mitigação: Nenhum rollback necessário para cliente/prod; artefatos paralelos podem ser restaurados a partir de /opt/data/backups/elle-brain-v2-structured-output/20260626T171047Z.
- Próximos passos: Instrumentar diagnóstico sanitizado dos invalid_json_or_empty: finish_reason, content_present, campos alternativos, HTTP/provider shape; avaliar modelo/provider/schema antes de nova rodada 100.
- Onde foi documentado no Brain: Report atualizado: areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-brain-v2-structured-output-shadow-followup-20260626.md; raw: reports/elle-brain-v2/structured-output-shadow-100-raw-20260626/; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
