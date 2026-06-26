# Receipt — Decisão 3/4 — Telegram `message_id` inválido

- Data/hora UTC: 2026-06-06T10:23:15+00:00
- Escopo aprovado: investigação read-only/local; patch local/teste somente com causa confirmada; sem gateway restart/reload/ativação.
- Status: causa confirmada; patch local preparado no arquivo instalado; **não ativado por restart/reload**.

## Sintoma observado

Logs locais mostravam falha de entrega Telegram:

```text
telegram.error.BadRequest: Field "message_id" must be a valid number
```

A falha ocorria ao enviar resposta após clique em botão de decisão cron/Mesa COO (`cj:<context>:<value>`), por exemplo `Resposta ao botão de decisão do Hermes: Fazer`.

## Root cause confirmado

No fluxo de callback de decisão cron em:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/telegram.py
```

o `MessageEvent.message_id` era montado com `query.id` — o ID da callback query do Telegram — em vez do `query.message.message_id` da mensagem original com o botão.

Esse `query.id` não é um número de mensagem Telegram válido para `reply_to_message_id`. Como a entrega posterior tenta responder ao `event.message_id`, o Bot API rejeita com:

```text
Field "message_id" must be a valid number
```

## Evidência RED

Reprodução local com o Python do venv instalado, sem rede e sem Bot API real:

```text
event.message_id= 9876543210123456789
event.reply_to_message_id= 123
source.message_id= 123
AssertionError: RED: cron callback event.message_id should be prompt Telegram message_id, not callback query id
```

## Patch local preparado

Backup antes da alteração:

```text
/opt/data/backups/hermes-telegram-message-id-20260606/telegram.py.bak
```

Alteração aplicada no arquivo instalado:

```diff
- message_id=str(getattr(query, "id", getattr(query.message, "message_id", ""))),
+ message_id=str(getattr(query.message, "message_id", "")),
```

Readback após patch:

```text
3487| event = MessageEvent(
3492|     message_id=str(getattr(query.message, "message_id", "")),
3494|     reply_to_message_id=str(getattr(query.message, "message_id", "")),
3498| await self.handle_message(event)
```

## Evidência GREEN

Reprodução local após patch:

```text
event.message_id= 123
event.reply_to_message_id= 123
source.message_id= 123
GREEN cron_decision_callback_uses_prompt_message_id
```

Verificações adicionais:

```text
py_compile_PASS
old_bad_line_count 0
new_good_line_count 3
targeted_secret_scan_PASS
```

## Guardrails preservados

- Não houve restart/reload/ativação do gateway.
- Não houve Docker/SSH/root/Traefik/rede/cron/secrets/produção.
- Não houve chamada real ao Telegram Bot API para teste.
- Patch é local no arquivo instalado; processo já carregado pode continuar usando código antigo até restart/reload aprovado.

## Próximo passo recomendado

Se Lucas aprovar ativação: fazer janela curta de `gateway restart/reload` com rollback explícito para:

```text
cp /opt/data/backups/hermes-telegram-message-id-20260606/telegram.py.bak /opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/telegram.py
```

e validação pós-ativação por novo clique em botão de decisão cron/Mesa COO e leitura de logs confirmando ausência de `Field "message_id" must be a valid number`.
