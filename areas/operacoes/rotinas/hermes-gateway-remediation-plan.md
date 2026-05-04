# Plano — Correção segura do Hermes Gateway/Telegram

Status: plano preparado; nenhuma alteração aplicada em produção.

## Contexto observado

A inspeção read-only de 2026-05-04 encontrou três sinais simultâneos:

1. O container `hermes-agent-5ajw-hermes-telegram-1` está rodando e tem `hermes gateway run` como processo principal.
2. `hermes cron list` mostra o job `Hermes release watch` ativo, com entrega `origin`.
3. `hermes cron status` reporta `Gateway is not running — cron jobs will NOT fire`.
4. Logs do gateway mostram conflito de polling Telegram: outro `getUpdates` parece concorrer com o mesmo bot/token, ou houve conflito recente.

Interpretação: isso é uma divergência de runtime/detector + possível conflito Telegram. Não é prova isolada de gateway parado, e não autoriza restart automático.

## Objetivo

Corrigir ou estabilizar o gateway Telegram e o cron Hermes sem colocar em risco:

- containers Hermes;
- Docker/compose/volumes/redes;
- Traefik, n8n e Paperclip;
- SSH/root/firewall;
- secrets e tokens;
- entrega de mensagens para Lucas.

## Escopo permitido sem nova aprovação

Somente L0/L2 read-only:

- `docker ps`, `docker inspect`, `docker compose ps`.
- `docker logs --tail` com redação de tokens.
- `docker exec` para comandos de leitura: `hermes --version`, `hermes cron status`, `hermes cron list`, `ps`, consultas Telegram API sem mutation.
- leitura redigida de compose/env para nomes de variáveis, nunca valores.
- documentação no Brain.

## Ações bloqueadas até aprovação explícita Lucas

- `docker restart`, `docker stop`, `docker kill`, `docker compose restart/up/down`.
- alteração de `/docker/hermes-agent-5ajw/docker-compose.yml`, `.env` ou `data/.env`.
- troca/rotação de `TELEGRAM_BOT_TOKEN`.
- alteração de webhook, allowed users ou crons Hermes.
- update de imagem/runtime Hermes.
- matar processos gateway/poller.
- qualquer mudança em Traefik/n8n/Paperclip/root/SSH/firewall.

## Hipóteses a testar antes de corrigir

### H1 — detector do `hermes cron status` não reconhece gateway foreground em container

Evidência a favor:

- `hermes gateway run` existe como PID 1 no container Telegram.
- O container está `Up`.

Teste read-only:

- comparar `hermes cron status`, `hermes cron list --all`, processos e logs na mesma janela.
- procurar no filesystem do container, sem alterar, se existe pidfile/socket/status file esperado pelo CLI.

### H2 — há outro poller Telegram usando o mesmo bot token

Evidência a favor:

- log: `terminated by other getUpdates request`.

Teste read-only:

- listar containers e processos Hermes/gateway no host e dentro dos containers.
- checar `getWebhookInfo` com token do ambiente sem imprimir token.
- checar se existe webhook configurado; webhook + polling simultâneo pode causar comportamento inesperado.
- procurar em n8n/workflows/compose/env apenas nomes/indícios de uso do mesmo bot, sem imprimir secrets.

### H3 — conflito temporário resolvido sozinho, mas logs preservaram alerta antigo

Teste read-only:

- coletar apenas logs recentes com timestamp.
- verificar se o warning continua aparecendo após nova mensagem de teste do Lucas.
- se Telegram responde normalmente e cron executar na data agendada, pode ser somente alerta histórico.

### H4 — runtime v0.9.0 tem bug/limitação já corrigida em v0.12.0

Teste read-only:

- comparar release notes upstream com sintomas de gateway/cron.
- não atualizar automaticamente; se a hipótese ficar forte, mover para plano de update com rollback.

## Sequência segura de diagnóstico

1. Registrar horário UTC da coleta.
2. Confirmar containers Hermes `Up`.
3. Confirmar versão nos dois containers.
4. Confirmar `hermes cron status` e `hermes cron list --all` no container Telegram.
5. Coletar processo gateway no host e no container Telegram.
6. Checar logs recentes do container Telegram com tokens redigidos.
7. Checar Telegram `getWebhookInfo` sem imprimir token.
8. Procurar duplicidade de gateway/poller em containers/processos sem matar nada.
9. Classificar a causa provável em H1/H2/H3/H4.
10. Só então propor uma ação corretiva mínima para aprovação.

## Plano de rollback exigido antes de qualquer correção

Antes de qualquer restart/update/alteração:

1. Registrar `docker ps` e `docker compose ps` atuais.
2. Registrar digest/imagem atual dos containers Hermes.
3. Copiar para arquivo local seguro, ou pelo menos registrar checksums, dos arquivos:
   - `/docker/hermes-agent-5ajw/docker-compose.yml`
   - `/docker/hermes-agent-5ajw/.env` somente redigido; não commitar nem imprimir valores.
   - `/docker/hermes-agent-5ajw/data/.env` somente redigido; não commitar nem imprimir valores.
4. Registrar `hermes --version` atual: `v0.9.0 (2026.4.13)`.
5. Ter comando de retorno ao estado anterior documentado, sem executar até necessário.
6. Confirmar com Lucas a janela de manutenção.

## Correções possíveis, dependentes da causa

### Se H1 for confirmada

Possível ação: não reiniciar nada; documentar limitação do detector e criar monitoramento alternativo baseado em processo/log/cron list até update futuro.

### Se H2 for confirmada

Possível ação: identificar o poller concorrente e decidir qual instância deve ficar ativa. Não matar ou parar sem aprovação, porque pode ser outra automação legítima.

### Se H3 for confirmada

Possível ação: manter observabilidade e aguardar próxima execução do cron release watch.

### Se H4 for confirmada

Possível ação: seguir o plano `hermes-runtime-update-plan.md` em janela aprovada.

## Critério de sucesso

- Telegram responde a Lucas.
- Logs deixam de mostrar conflitos recorrentes, ou a causa fica explicada e aceita.
- `Hermes release watch` segue ativo.
- Cron automático tem evidência de execução ou limitação documentada.
- Nenhum outro app Docker é afetado.
- Nenhum secret é exposto.


## Resultado do diagnóstico read-only — 2026-05-04 14:13 UTC

A sequência segura foi executada sem alterações de produção. Evidências completas em `hermes-gateway-readonly-diagnostic-2026-05-04.md`.

Resumo:

- containers `hermes-agent` e `hermes-telegram` ativos;
- `hermes-telegram` com `hermes gateway run` como PID 1;
- `hermes cron status` ainda reporta gateway down;
- `hermes cron list --all` mantém `Hermes release watch` ativo;
- `getMe` e `getWebhookInfo` OK;
- webhook ausente, como esperado para polling;
- `pending_update_count` 0;
- conflito Telegram aparece em logs históricos, mas não reapareceu nos últimos 30 minutos da coleta.

Classificação atual: H1 provável, H3 plausível, H2 não confirmada, H4 possível mas dependente de update planejado. Próximo passo seguro é observar a próxima execução do cron ou coletar logs imediatamente após uma mensagem de teste se Lucas notar silêncio.
