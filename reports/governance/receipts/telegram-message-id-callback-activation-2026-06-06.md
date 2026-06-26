# Receipt — Ativação do patch Telegram `message_id` callback

- Data/hora UTC: 2026-06-06T10:38:51+00:00
- Pedido/autorização: Lucas — `Seguir ativar`
- Escopo executado: ativar patch local já preparado para erro Telegram `Field "message_id" must be a valid number`.
- Status: **ativado e verificado**.

## Patch ativado

Arquivo instalado:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/telegram.py
```

Linha crítica após patch:

```python
message_id=str(getattr(query.message, "message_id", "")),
reply_to_message_id=str(getattr(query.message, "message_id", "")),
```

Backup/rollback:

```text
/opt/data/backups/hermes-telegram-message-id-20260606/telegram.py.bak
```

Rollback manual, se necessário:

```bash
cp /opt/data/backups/hermes-telegram-message-id-20260606/telegram.py.bak /opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/telegram.py
# depois reiniciar/recarregar o gateway para reativar o código antigo
```

## Evidência de ativação

- `telegram.py` patch mtime: 2026-06-06T10:22:22+00:00
- Gateway principal `HERMES_HOME=/opt/data` iniciou depois do patch:
  - PID: 1
  - start: 2026-06-06T10:36:56+00:00
  - `start_after_patch=True`

Logs pós-restart:

```text
2026-06-06 10:37:04 INFO gateway.run: Starting Hermes Gateway...
2026-06-06 10:37:07 INFO gateway.platforms.telegram: [Telegram] Connected to Telegram (polling mode)
```

Saúde local:

```text
http://127.0.0.1:8642/health -> {"status": "ok", "platform": "hermes-agent"}
http://127.0.0.1:8644/health -> {"status": "ok", "platform": "webhook"}
```

Verificações:

```text
py_compile_PASS
callback_regression_after_restart_PASS
post_restart_telegram_send_errors 0
```

## Guardrails preservados

- A ativação ficou restrita ao gateway/Hermes local default necessário para carregar o patch.
- Não houve alteração em Docker compose, Traefik, SSH/root, rede, cron jobs, secrets ou produção Shopify/Tiny/GitHub.
- Nenhum token/segredo foi impresso no receipt.

## Observação

A validação automatizada cobre o caminho do callback `cj:mesa:fazer` e confirma que o `MessageEvent.message_id` agora usa o `query.message.message_id` real da mensagem Telegram. A validação final de produto é o próximo clique real em botão de decisão cron/Mesa COO; os logs pós-restart até este receipt não mostram novos erros `Field "message_id" must be a valid number`.
