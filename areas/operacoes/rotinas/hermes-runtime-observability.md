# Rotina — Hermes Runtime Observability

Última inspeção read-only: 2026-05-04 14:13 UTC. Ver também `hermes-gateway-readonly-diagnostic-2026-05-04.md`.

## Objetivo

Manter uma visão operacional do runtime Hermes na VPS `lc.vps` sem tocar em Docker/root/containers/volumes/redes/Traefik/n8n/Paperclip.

Esta rotina existe para responder perguntas como:

- qual versão do Hermes está rodando em produção;
- se os containers Hermes estão vivos;
- se o gateway Telegram aparenta estar rodando;
- se o cron interno do Hermes enxerga jobs ativos;
- quais alertas precisam de investigação antes de qualquer mudança.

## Evidência observada

Inspeção feita somente com comandos read-only (`docker ps`, `docker compose ps`, `docker exec` para comandos de leitura, `docker logs --tail`, `ps`). Nenhum container foi reiniciado, recriado, parado ou alterado.

### Containers Hermes

| Container | Estado observado | Função |
|---|---:|---|
| `hermes-agent-5ajw-hermes-agent-1` | `Up 20 hours` | serviço web/ttyd/API Hermes, porta host `32771 -> 4860/tcp` |
| `hermes-agent-5ajw-hermes-telegram-1` | `Up 18 hours` | gateway Telegram, comando `hermes gateway run` |

Imagem nos dois containers: `ghcr.io/hostinger/hvps-hermes-agent:latest`.

### Versão Hermes em produção

Ambos os containers reportaram:

```text
Hermes Agent v0.9.0 (2026.4.13)
Python: 3.13.5
OpenAI SDK: 2.31.0
```

### Release upstream consultada

GitHub Releases (`NousResearch/hermes-agent`) reportou como latest:

```text
v2026.4.30 — Hermes Agent v0.12.0 (2026.4.30)
```

Tema principal: “The Curator release”.

Interpretação: produção Hostinger está em `v0.9.0`, enquanto upstream mais recente está em `v0.12.0`. Isso é um gap de versão relevante, mas não autoriza update automático. Atualização do runtime Docker/Hostinger é ação de produção e exige aprovação Lucas + plano de backup/rollback.

## Estado de gateway e cron

Dentro do container `hermes-telegram`, foi observado processo principal:

```text
/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run
```

O cron interno do Hermes listou o job ativo:

```text
Hermes release watch
Schedule: 0 9 * * 1
Next run: 2026-05-11T09:00:00+00:00
Deliver: origin
```

Porém `hermes cron status` dentro do container também exibiu:

```text
Gateway is not running — cron jobs will NOT fire
```

Interpretação operacional: há divergência entre evidência de processo (`hermes gateway run` ativo) e o detector de status do CLI (`Gateway is not running`). Tratar como warning de observabilidade, não como prova de gateway parado.

## Alertas vistos nos logs

Logs recentes do container `hermes-telegram` mostraram:

```text
Telegram polling conflict: terminated by other getUpdates request; make sure that only one bot instance is running
```

Interpretação: pode existir outro poller/webhook usando o mesmo bot token ou houve conflito temporário. A evidência coletada não autoriza encerrar processos nem reiniciar containers. Próxima investigação deve continuar read-only.

## Procedimento read-only recomendado

1. Verificar containers:
   - `docker ps --filter 'name=hermes-agent-5ajw'`
   - `cd /docker/hermes-agent-5ajw && docker compose ps`
2. Verificar versão sem alterar runtime:
   - `docker exec hermes-agent-5ajw-hermes-telegram-1 /bin/zsh -lc 'hermes --version'`
3. Verificar cron interno:
   - `docker exec hermes-agent-5ajw-hermes-telegram-1 /bin/zsh -lc 'hermes cron status; hermes cron list --all'`
4. Verificar processos:
   - `docker exec hermes-agent-5ajw-hermes-telegram-1 /bin/zsh -lc "ps -eo pid,ppid,stat,comm,args | grep -E 'hermes gateway|python' | grep -v grep"`
5. Verificar logs redigindo tokens:
   - `docker logs --tail 120 hermes-agent-5ajw-hermes-telegram-1`
   - redigir token Telegram e qualquer secret antes de documentar.

## Ações proibidas sem aprovação explícita

- `docker restart`, `docker stop`, `docker compose up/down`, `docker compose restart`.
- Alterar `/docker/hermes-agent-5ajw/docker-compose.yml` ou `.env`.
- Atualizar imagem/container Hermes.
- Instalar nova versão Hermes na VPS.
- Matar processo gateway ou poller.
- Alterar token Telegram, webhook ou allowed users.
- Alterar crons/jobs ativos.

Qualquer uma dessas ações exige preview, aprovação Lucas e plano de backup/rollback.

## Próximas decisões possíveis

1. Investigar origem do `Telegram polling conflict` por vias read-only adicionais.
2. Decidir se o update de `v0.9.0` para `v0.12.0` entra em uma janela planejada.
3. Verificar se o alerta `Gateway is not running` é bug/limitação do detector em container foreground ou configuração faltante.
4. Manter monitoramento sem ação caso Telegram continue respondendo normalmente.

## Atualização — diagnóstico read-only 2026-05-04 14:13 UTC

Foi executada a sequência segura de diagnóstico descrita em `hermes-gateway-remediation-plan.md`, sem alterar produção. Resultado resumido:

- containers Hermes seguem `Up`;
- runtime segue em `Hermes Agent v0.9.0 (2026.4.13)`;
- `hermes gateway run` segue ativo como PID 1 no container Telegram;
- `hermes cron status` continua reportando gateway down;
- Telegram API `getMe` e `getWebhookInfo` retornaram OK;
- webhook não está configurado;
- `pending_update_count` estava 0;
- conflitos de polling aparecem em logs históricos, mas não reapareceram nos últimos 30 minutos da coleta.

Conclusão: H1 provável (limitação/divergência do detector de gateway em Docker foreground) e H3 plausível (conflito Telegram histórico/transitório). H2 não confirmada. Nenhuma ação corretiva foi executada.
