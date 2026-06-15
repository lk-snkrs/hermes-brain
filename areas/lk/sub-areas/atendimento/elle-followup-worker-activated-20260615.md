# Elle — follow-up 60min/23h ativado

Data: 2026-06-15
Origem: Lucas Telegram: “Então ative meu amor”
Responsável: lk-ops
Sistema: `/opt/elle-chatwoot` no VPS

## Escopo ativado
Worker local para follow-up conversacional da Elle no Chatwoot/LK WhatsApp:
- 1º follow-up: 60 minutos depois da última mensagem da cliente.
- 2º follow-up: 23 horas depois da última mensagem da cliente.
- Base: última mensagem **incoming** da cliente.
- Janela máxima: até 23h45 para evitar envio fora da janela de 24h do WhatsApp.

## Segurança aplicada
- Filtrado somente inbox `LK WhatsApp` (`inbox_id=2`, `Channel::Whatsapp`, provider `whatsapp_cloud`).
- Não envia para conversas antigas anteriores à ativação (`activation_at` no ledger).
- Não envia se já existe mensagem outgoing depois da última mensagem da cliente.
- Não envia se houver human takeover lock.
- Não envia para confirmações curtas/encerramento como `ok`, `obrigado`, `valeu`, `.`.
- Usa ledger idempotente por `conversation_id` + `last_in_id`.
- Marca mensagens com `content_attributes`: `elle_generated=true`, `elle_followup=true`, `elle_followup_stage=stage1|stage2`.
- Usa `flock` no cron para evitar sobreposição.

## Arquivos/cron
- Worker: `/opt/elle-chatwoot/elle_followup_worker.py`
- Estado: `/opt/elle-chatwoot/data/followup_state.json` montado como `/data/followup_state.json` no container.
- Eventos: `/opt/elle-chatwoot/logs/followup_events.jsonl` montado como `/var/log/elle/followup_events.jsonl`.
- Cron: `/etc/cron.d/elle-followup`
- Frequência: a cada 10 minutos.
- Comando: `docker exec elle-chatwoot python /app/elle_followup_worker.py`

## Backup
Backup criado antes da alteração:
- `/opt/elle-chatwoot/backups/elle-followup-worker-20260615T013739Z/`

## Deploy/verificação
- `python3 -m py_compile app.py elle_followup_worker.py elle_observer_summary.py`: OK.
- Dockerfile atualizado para copiar `elle_followup_worker.py` para `/app/`.
- `docker compose build elle-chatwoot`: OK.
- `docker compose up -d elle-chatwoot`: OK.
- Health pós-deploy: `ok=true`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `observer_enabled=true`.
- Smoke dry-run: `checked=112`, `eligible=0`, `sent=0`; pulou antigas por `before_activation` e outros filtros.
- Primeira execução live: `checked=112`, `eligible=0`, `sent=0`; não disparou follow-up antigo em massa.
- Cron service: `active`.

## Cópias ativadas
Stage 1:
> Olá! Passando para saber se consigo te ajudar com alguma dúvida antes de finalizar. Se quiser, é só me chamar por aqui.

2º follow-up:
> Olá! Ainda posso te ajudar por aqui? Se quiser seguir com a compra ou tirar alguma dúvida, me manda uma mensagem que eu te ajudo.

## Rollback
Para desativar envio automático:
1. Remover ou comentar `/etc/cron.d/elle-followup`.
2. Opcionalmente manter ledger/logs para auditoria.
3. Se precisar remover código do container, restaurar backup e rebuildar `/opt/elle-chatwoot`.
