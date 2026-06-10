# Diagnóstico Chatwoot `data_services` — 2026-06-09-090732 -03

## Escopo

Lucas pediu “Fazer apenas o 1”, referente a diagnosticar `data_services=failing` do Chatwoot.

Executado em modo read-only:

- Sem restart.
- Sem `docker compose up/down`.
- Sem alteração de arquivos, containers, volumes, rede, Traefik, DNS ou secrets.
- Sem envio de mensagens.
- Logs brutos não foram salvos porque Chatwoot pode imprimir argumentos de webhook com secrets.

## Evidência inicial anterior

No diagnóstico anterior, endpoint público `https://chat.lkskrs.online/api` retornou:

```json
{
  "version": "4.14.1",
  "queue_services": "ok",
  "data_services": "failing"
}
```

## Evidência atual

Acesso SSH read-only ao VPS `lc` funcionou por chave.

Host:

- hostname: `lc`
- user: `root`
- kernel: `Linux 6.8.0-111-generic`

Endpoint local dentro do VPS:

```json
{
  "version": "4.14.1",
  "queue_services": "ok",
  "data_services": "ok"
}
```

Endpoint público testado depois, 3 vezes seguidas:

- `queue_services=ok`
- `data_services=ok`

Confirmação final em 2026-06-09-090732 -03:

- Público `https://chat.lkskrs.online/api`: `queue_services=ok`, `data_services=ok`.
- Local `http://127.0.0.1:3000/api`: `queue_services=ok`, `data_services=ok`.

## Containers observados

Compose em `/opt/chatwoot`.

Containers Chatwoot principais:

- `chatwoot-rails-1` — imagem `lk-chatwoot:v2-recovery12`, running, restart count 0, started `2026-06-06T14:14:42Z`.
- `chatwoot-sidekiq-1` — imagem `lk-chatwoot:v2-recovery12`, running, restart count 0, started `2026-06-06T14:14:42Z`.
- `chatwoot-postgres-1` — imagem `pgvector/pgvector:pg16`, running, restart count 0, started `2026-06-02T14:29:08Z`.
- `chatwoot-redis-1` — imagem `redis:alpine`, running, restart count 0, started `2026-06-02T14:29:08Z`.

Recursos do host:

- Disco `/`: 33% usado.
- Memória: 31 GiB total, ~18 GiB disponível.
- Swap: 0 B.

## Logs recentes sanitizados

Postgres, últimas ~2h:

- Sem `ERROR`, `FATAL`, `PANIC` ou restart observado.
- Apenas checkpoints normais.

Redis, últimas ~2h:

- Sem erro observado.
- BGSAVE periódico concluindo com sucesso.

Docker events recentes para containers Chatwoot principais:

- Sem eventos relevantes no período consultado.

Rails/Sidekiq:

- Jobs rodando e WebhookJob concluindo.
- Observada atividade de conversas/notas privadas via `Channel::Api`/Shopify.
- Não salvar logs brutos porque podem conter URL/secrets de webhook em argumentos ActiveJob.

## Diagnóstico

O `data_services=failing` não está presente no momento. O estado atual é saudável tanto pelo endpoint público quanto pelo endpoint local dentro do VPS.

Causa mais provável: falha transitória/temporária no probe de data services, possivelmente uma oscilação curta de conexão Rails -> Postgres/Redis no momento da primeira checagem. Não há evidência, neste diagnóstico read-only, de queda persistente de Postgres/Redis, restart de container, falta de disco/memória ou problema ativo de proxy.

## Recomendação

- Não fazer restart agora: o serviço está saudável.
- Se voltar a aparecer `data_services=failing`, capturar imediatamente:
  - `curl http://127.0.0.1:3000/api` dentro do VPS;
  - logs de `chatwoot-rails-1`, `chatwoot-postgres-1`, `chatwoot-redis-1` nos 5 minutos ao redor;
  - `docker inspect` de restart/status;
  - uso de disco/memória.
- Se Lucas quiser, próximo passo seguro é criar/validar um monitor read-only de saúde que alerte só quando `data_services` ficar failing por N checagens consecutivas. Isso seria nova etapa e exigiria aprovação de cron/monitor se for produção.

## Guardrails

- Nenhuma ação de correção foi executada.
- Nenhum segredo foi salvo.
- Nenhuma mensagem externa foi enviada.
