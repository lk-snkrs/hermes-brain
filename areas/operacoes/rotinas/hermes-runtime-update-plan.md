# Plano — Update seguro Hermes Runtime v0.9.0 para v0.12.0

Status: tentativa segura executada em 2026-05-05; imagem Hostinger `latest` não trouxe versão nova.

## Contexto

Runtime observado na VPS `lc.vps`:

```text
Hermes Agent v0.9.0 (2026.4.13)
```

Release upstream consultada:

```text
v2026.4.30 — Hermes Agent v0.12.0 (2026.4.30)
```

O update pode trazer melhorias relevantes para gateway, cron, skills, Curator e observabilidade, mas é mudança de produção. Não deve ser feito automaticamente.

## Objetivo

Atualizar o runtime Hermes da VPS Hostinger com risco controlado, preservando:

- dados persistentes em `/docker/hermes-agent-5ajw/data`;
- containers e redes dos outros apps;
- acesso Telegram do Lucas;
- rollback rápido para o estado anterior.

## Pré-condições

1. Aprovação explícita Lucas para janela de manutenção.
2. Diagnóstico Gateway/Telegram concluído ou aceito como risco.
3. Backup/registro do estado atual feito antes do update.
4. Token Doppler e GitHub disponíveis sem exposição.
5. Plano de rollback revisado.

## O que NÃO fazer sem aprovação

- Não executar `docker compose pull`, `up`, `restart`, `down` ou `recreate`.
- Não alterar compose/env.
- Não apagar volumes, imagens antigas ou redes.
- Não rodar `docker prune`.
- Não mexer em Traefik/n8n/Paperclip.
- Não alterar SSH/root/firewall.

## Inventário pré-update obrigatório

Coletar e salvar em local seguro, sem commitar secrets:

1. `docker ps --filter name=hermes-agent-5ajw`.
2. `cd /docker/hermes-agent-5ajw && docker compose ps`.
3. `docker inspect` dos containers Hermes com digest/imagem/env redigido.
4. `docker image inspect ghcr.io/hostinger/hvps-hermes-agent:latest` para ID/digest local atual, se disponível.
5. Checksums de compose:
   - `/docker/hermes-agent-5ajw/docker-compose.yml`
   - env files somente com nomes de variáveis, nunca valores.
6. `hermes --version` nos dois containers.
7. `hermes cron list --all` no container Telegram.
8. logs recentes do gateway, redigidos.

## Estratégia de backup

Como o runtime usa bind mount:

```text
host: /docker/hermes-agent-5ajw/data
container: /opt/data
```

Antes do update, criar backup compactado do diretório de dados e compose/env em caminho fora do repo, com permissões restritas. O backup não deve ser enviado ao GitHub nem exibido em chat.

Itens mínimos:

- `docker-compose.yml`.
- `.env` e `data/.env` em arquivo protegido ou cópia redigida + backup privado.
- diretório `data/` completo ou snapshot equivalente.

## Estratégia de update proposta

Preferência: usar o mecanismo oficial Hostinger/Hermes se houver documentação do catálogo. Se não houver, tratar `ghcr.io/hostinger/hvps-hermes-agent:latest` com cautela porque `latest` pode mudar sem pinagem explícita.

Sequência conceitual, não executar sem aprovação:

1. Confirmar imagem/digest atual.
2. Fazer backup.
3. Puxar imagem nova sem remover a antiga.
4. Recriar somente serviços Hermes, nunca n8n/Paperclip/Traefik.
5. Verificar versão pós-update nos dois containers.
6. Verificar gateway/Telegram.
7. Verificar `hermes cron status` e `hermes cron list`.
8. Enviar mensagem de teste no Telegram.
9. Registrar resultado no Brain.

## Rollback conceitual

Se o update quebrar gateway, Telegram, cron ou web terminal:

1. Não mexer em outros apps.
2. Reverter para imagem/digest anterior ou restaurar compose/data backup.
3. Recriar somente serviços Hermes.
4. Verificar `hermes --version` voltou para o estado anterior.
5. Verificar Telegram/gateway.
6. Registrar incidente e causa provável no Brain.

## Critérios de sucesso

- Containers Hermes sobem saudáveis.
- `hermes --version` mostra a versão alvo ou versão esperada da imagem atualizada.
- Telegram responde no DM com Lucas.
- `Hermes release watch` segue listado e ativo.
- Não há conflitos Telegram recorrentes nos logs pós-update.
- Nenhum outro container/app sofre alteração.
- Secrets não aparecem em logs, docs ou commits.

## Decisão pendente

Este plano deixa o update pronto para aprovação, mas não recomenda execução automática. A próxima decisão de Lucas deve ser uma destas:

1. Aprovar somente diagnóstico adicional read-only do gateway.
2. Aprovar correção mínima do gateway após diagnóstico.
3. Aprovar janela de update v0.9.0 → v0.12.0 com backup/rollback.
4. Adiar update e seguir com playbooks do Brain.


## Execução registrada — 2026-05-05

Ver registro completo em `hermes-runtime-update-attempt-2026-05-05.md`.

Resumo:

- Lucas autorizou reset de senha root da `lc.vps` via Hostinger e backup/update do Hermes Docker.
- Nova senha root foi gerada e salva no Doppler como `VPS_ROOT_PASSWORD`, sem exposição de valor.
- Backup leve foi salvo fora do repo em `/opt/data/hermes_bruno_ingest/backups/lc-vps-hermes-20260505T011529Z`.
- Rollback tag criada: `ghcr.io/hostinger/hvps-hermes-agent:preupdate-20260505T011613Z`.
- Foram executados apenas `docker compose pull` e `docker compose up -d --no-deps` para `hermes-agent` e `hermes-telegram`.
- Digest antes/depois permaneceu `sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7`.
- Versão pós-update permaneceu `Hermes Agent v0.9.0 (2026.4.13)` nos dois containers.
- Containers Hermes seguiram `Up`; Traefik, n8n, Paperclip, volumes, redes, firewall e produção externa não foram alterados.

Conclusão: o fluxo seguro de pull/recreate limitado foi executado, mas a imagem `ghcr.io/hostinger/hvps-hermes-agent:latest` não continha a release upstream `v2026.4.30` / `v0.12.0`. Upgrade real para `v0.12.0` exige investigação/aprovação separada de tag oficial Hostinger ou imagem customizada.

## Decisão preparada — 2026-05-05

Documento de opções criado: `hermes-runtime-upgrade-options-2026-05-05.md`.

Recomendação atual: não instalar gateway systemd nem trocar imagem/compose sem aprovação. Como Telegram responde e não houve conflito novo nas últimas 2h, a opção de menor risco é aguardar a primeira execução real do `Hermes release watch` em 2026-05-11 para validar se o cron dispara apesar do warning; se não disparar, priorizar correção mínima do gateway/cron. Upgrade customizado para v0.12.0 fica como caminho planejado, não ação automática.
