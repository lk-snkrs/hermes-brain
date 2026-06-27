# Receipt — Elle Brain v2 — do 1 ao 4 shadow live

- Data/hora: 2026-06-26T16:17:25.692621+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas pediu fazer itens 1 a 4: revisar diffs, ampliar regressões, rodar shadow live OpenRouter classify-only e preparar approval packet de canary.
- Classificação: local-write
- Fontes usadas:
- Runtime elle-chatwoot, logs locais /var/log/elle/events.jsonl, artefatos /app/elle_brain_v2.py e Brain PRD; OpenRouter classify-only sem impressão de valores; values_printed=false.
- O que foi feito:
- Regressões ampliadas para 30 casos; runner atualizado para heuristic/live_openrouter; shadow heuristic e live executados; diff review e approval packet gerados; app.py produtivo não alterado.
- Output/artefato:
- Tests 30 OK; shadow live 36 processed/35 calls/27 valid_json/8 invalid_or_empty/0 writes externos; approval packet recomenda no-go para canary até structured output melhorar.
- Aprovação: Aprovado por Lucas no Telegram: Fazer do 1 ao 4.
- Envio/publicação: Nenhum envio a cliente; somente arquivos locais/container e Brain.
- Writes externos: 0
- Riscos/bloqueios: Canary ainda no-go: valid_json live 27/35 abaixo do alvo; 19 diffs categoria e 16 diffs handoff exigem revisão qualitativa.
- Rollback/mitigação: Restaurar/remover artefatos paralelos a partir de /root/elle-brain-v2-do-1-4-backups/20260626T160752Z; /app/app.py não foi alterado.
- Próximos passos: Corrigir retry/structured output OpenRouter e rodar novo shadow live maior antes de qualquer canary.
- Onde foi documentado no Brain: Review: areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-brain-v2-do-1-4-shadow-live-review-20260626.md; approval: areas/lk/sub-areas/atendimento/approval-packets/elle-brain-v2/elle-brain-v2-canary-approval-packet-20260626.md; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
