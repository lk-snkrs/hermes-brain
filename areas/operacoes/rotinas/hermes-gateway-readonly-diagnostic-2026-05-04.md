# Diagnóstico read-only — Hermes Gateway/Telegram — 2026-05-04

Status: diagnóstico coletado em modo read-only; nenhuma alteração aplicada em produção.

Coleta UTC: `2026-05-04T14:12:55Z` e verificação complementar `2026-05-04T14:13:15Z`.

## Escopo executado

Comandos usados somente para leitura:

- `docker ps --filter name=hermes-agent-5ajw`.
- `docker compose ps` no diretório `/docker/hermes-agent-5ajw`.
- `docker exec` para `hermes --version`, `hermes cron status`, `hermes cron list --all` e `ps`.
- `docker logs --tail` e `docker logs --since 30m --timestamps`.
- leitura de nomes de variáveis Telegram nos env files, sem imprimir valores.
- chamadas Telegram API somente read-only: `getMe` e `getWebhookInfo`, com token lido do ambiente e nunca impresso.

Não foram executados: restart, stop, kill, compose up/down/restart/pull, alteração de env/compose, alteração de webhook, troca de token, alteração de cron, update de imagem/runtime, ou mudança em root/Docker/Traefik/n8n/Paperclip.

## Evidências coletadas

### Containers

| Container | Imagem | Estado |
|---|---|---|
| `hermes-agent-5ajw-hermes-telegram-1` | `ghcr.io/hostinger/hvps-hermes-agent:latest` | `Up 19 hours` |
| `hermes-agent-5ajw-hermes-agent-1` | `ghcr.io/hostinger/hvps-hermes-agent:latest` | `Up 21 hours`, porta host `32771 -> 4860/tcp` |

`docker compose ps` confirmou os serviços `hermes-telegram` e `hermes-agent` ativos no projeto `/docker/hermes-agent-5ajw`.

### Versão Hermes

Ambos os containers reportaram:

```text
Hermes Agent v0.9.0 (2026.4.13)
Project: /opt/hermes
Python: 3.13.5
OpenAI SDK: 2.31.0
```

### Cron interno Hermes

No container Telegram:

```text
Gateway is not running — cron jobs will NOT fire
1 active job(s)
Next run: 2026-05-11T09:00:00+00:00
```

`hermes cron list --all` confirmou o job ativo:

```text
6ff1ad725ae2 [active]
Name: Hermes release watch
Schedule: 0 9 * * 1
Repeat: ∞
Next run: 2026-05-11T09:00:00+00:00
Deliver: origin
```

### Processos

Host e container Telegram continuam mostrando gateway foreground:

```text
/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run
```

No container Telegram:

```text
PID 1: hermes gateway run
child: /opt/hermes/.venv/bin/python3 script.py
```

No container agent há `ttyd` e processos de chat Hermes. A credencial `ttyd/basic-auth` aparece em argumentos de processo e deve continuar tratada como secret operacional; o valor não foi registrado neste documento.

### Env Telegram

Foram encontrados nomes de variáveis, sem valores, em `/docker/hermes-agent-5ajw/data/.env`:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_HOME_CHANNEL
TELEGRAM_ALLOWED_USERS
```

Nenhum valor foi impresso ou salvo.

### Telegram API read-only

Com o token lido do ambiente do container, sem imprimir o valor:

```json
{"method":"getMe","ok":true,"id_present":true,"username_present":true}
{"method":"getWebhookInfo","ok":true,"webhook_configured":false,"pending_update_count":0,"last_error_date_present":false,"last_error_message_present":false}
```

Interpretação:

- O token configurado no container é válido.
- Não há webhook configurado para o bot.
- Não havia updates pendentes no momento da coleta.
- Não havia erro recente registrado por `getWebhookInfo`.
- O modelo atual é polling, não webhook.

### Logs recentes

`docker logs --tail 160` ainda mostra conflitos históricos de polling Telegram:

```text
Telegram polling conflict (1/3), will retry in 10s. Error: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
```

A verificação com `docker logs --since 30m --timestamps` mostrou apenas warnings de compressão de sessão no período recente; não apareceu novo `Telegram polling conflict` nos últimos 30 minutos da coleta.

## Classificação das hipóteses

### H1 — detector do `hermes cron status` não reconhece gateway foreground em container

Status: provável.

Evidências:

- `hermes gateway run` está ativo como PID 1 no container Telegram.
- `hermes cron status` continua reportando gateway down.
- `hermes cron list` vê o job ativo, mas replica o mesmo warning.
- Não há webhook configurado nem erro recente de Telegram API.

Próximo teste seguro: aguardar/verificar execução real do cron `Hermes release watch` em `2026-05-11T09:00:00+00:00`, ou usar observabilidade read-only próxima da janela.

### H2 — outro poller Telegram usando o mesmo bot token

Status: não confirmado no momento da coleta.

Evidências:

- Logs históricos mostram conflito de polling.
- Porém processos atuais não revelam outro `hermes gateway run` além do container Telegram.
- `getWebhookInfo` não mostra webhook configurado.
- Logs dos últimos 30 minutos não repetiram o conflito.

Próximo teste seguro: se Lucas observar silêncio no bot, enviar mensagem de teste e coletar logs imediatamente, sem rodar `getUpdates` para não competir com polling.

### H3 — conflito temporário resolvido sozinho, logs preservaram alerta antigo

Status: plausível.

Evidências:

- Conflitos aparecem no tail histórico.
- Não reapareceram nos logs dos últimos 30 minutos.
- `getWebhookInfo` está limpo.

### H4 — bug/limitação do runtime v0.9.0 corrigida em v0.12.0

Status: possível, mas ainda não provado.

Evidências:

- Produção está em `v0.9.0`; upstream consultado está em `v0.12.0`.
- Há warning de detector/cron que pode ter sido melhorado em versões posteriores.

Ação: manter plano de update separado em `hermes-runtime-update-plan.md`; não executar update sem aprovação explícita, janela e rollback.

## Conclusão operacional

O estado atual sugere mais fortemente uma limitação/divergência do detector de gateway em runtime Docker foreground, combinada com conflito Telegram histórico ou transitório. Não há evidência suficiente para restart, kill, troca de token ou update automático.

Recomendação segura:

1. Manter containers sem alteração.
2. Não chamar `getUpdates` manualmente enquanto o gateway está em polling, para não criar conflito artificial.
3. Se Lucas notar silêncio no bot, coletar logs imediatamente após a mensagem de teste.
4. Verificar a execução automática do cron no próximo horário agendado.
5. Planejar update `v0.9.0 -> v0.12.0` somente com aprovação e rollback.
