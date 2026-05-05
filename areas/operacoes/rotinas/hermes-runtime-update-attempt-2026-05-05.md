# Registro — tentativa segura de update Hermes Runtime 2026-05-05

Status: executado com escopo limitado; imagem Hostinger `latest` não trouxe versão nova.

## Resumo executivo

Lucas autorizou explicitamente resetar a senha root da `lc.vps` via Hostinger e seguir com backup/update do Hermes Docker. A execução foi limitada aos serviços Hermes (`hermes-agent` e `hermes-telegram`) no Compose `/docker/hermes-agent-5ajw`.

Resultado principal: o pull de `ghcr.io/hostinger/hvps-hermes-agent:latest` não alterou o digest da imagem. Após `docker compose pull` e `docker compose up -d --no-deps`, os containers seguiram saudáveis, mas o runtime permaneceu em `Hermes Agent v0.9.0 (2026.4.13)`.

## Escopo aprovado e executado

Executado:

1. Reset de senha root da VM `lc.vps` via API Hostinger.
2. Salvamento da nova senha em Doppler como `VPS_ROOT_PASSWORD` sem imprimir valor.
3. Verificação de SSH root usando senha recuperada via Doppler.
4. Backup/inventário leve local, fora do repo Git.
5. Tag local de rollback da imagem Hermes antes do pull.
6. `docker compose pull` somente para serviços Hermes.
7. `docker compose up -d --no-deps` somente para serviços Hermes.
8. Verificação pós-update de containers, digest, versão, cron e processo gateway.

Não executado:

- Nenhuma alteração em Traefik, n8n, Paperclip, volumes, redes, firewall, DNS, Supabase, Vercel ou apps externos.
- Nenhum `docker compose down`, prune, remoção de volumes/imagens antigas ou alteração de compose/env.
- Nenhum valor de secret foi documentado.

## Ambiente observado

VPS Hostinger:

- VM: `lc.vps`.
- VM id: `1331756`.
- IPv4: `72.60.150.124`.
- Template: Ubuntu 24.04 with Docker and Traefik.

Docker runtime observado no backup:

- Docker: `29.4.0`.
- Docker Compose: `v5.1.2`.
- Compose Hermes: `/docker/hermes-agent-5ajw`.
- Imagem: `ghcr.io/hostinger/hvps-hermes-agent:latest`.

Containers Hermes pós-verificação:

| Container | Estado | Função |
|---|---:|---|
| `hermes-agent-5ajw-hermes-agent-1` | `Up 6 hours` | web/ttyd/API Hermes, porta host `32774 -> 4860/tcp` |
| `hermes-agent-5ajw-hermes-telegram-1` | `Up 6 hours` | gateway Telegram, comando `hermes gateway run` |

## Backup e rollback

Backup local leve, fora do repo Git:

```text
/opt/data/hermes_bruno_ingest/backups/lc-vps-hermes-20260505T011529Z
```

Arquivos preservados:

- `runtime-inventory.txt` — inventário runtime com env keys redigidas.
- `docker-compose.yml.redacted` — Compose redigido, sem valores de secrets.

Backups Hostinger existentes observados antes da mudança:

- `2026-05-04 13:34 UTC`.
- `2026-05-03 08:29 UTC`.
- `2026-04-29 03:58 UTC`.
- `2026-04-22 07:10 UTC`.

Tag de rollback criada na VPS antes do pull:

```text
ghcr.io/hostinger/hvps-hermes-agent:preupdate-20260505T011613Z
```

## Comandos de update executados

No diretório `/docker/hermes-agent-5ajw`:

```text
docker tag ghcr.io/hostinger/hvps-hermes-agent:latest ghcr.io/hostinger/hvps-hermes-agent:preupdate-20260505T011613Z
docker compose pull hermes-agent hermes-telegram
docker compose up -d --no-deps hermes-agent hermes-telegram
```

## Resultado de imagem e versão

Digest antes/depois do pull:

```text
ghcr.io/hostinger/hvps-hermes-agent@sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7
```

Versão reportada nos dois containers após o update:

```text
Hermes Agent v0.9.0 (2026.4.13)
Project: /opt/hermes
Python: 3.13.5
OpenAI SDK: 2.31.0
```

Conclusão: a imagem Hostinger `latest` atualmente publicada para esse ambiente não avançou para a release upstream `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`.

## Verificação pós-update

Verificação read-only pós-update em 2026-05-05 01:19 UTC:

- `docker compose ps`: os dois serviços Hermes estavam `Up`.
- `docker ps --filter name=hermes-agent-5ajw`: apenas containers Hermes esperados.
- `docker image inspect`: digest igual ao pré-update.
- `hermes --version`: `v0.9.0 (2026.4.13)` nos dois containers.
- Processo gateway no container Telegram:

```text
/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run
```

- `hermes cron list --all`: job `Hermes release watch` ativo, próxima execução `2026-05-11T09:00:00+00:00`, `Deliver: origin`.
- `hermes cron status`: continua reportando `Gateway is not running — cron jobs will NOT fire`, apesar do processo gateway estar rodando como PID 1. Manter como divergência de detector/observabilidade já registrada.
- Logs recentes ainda exibiram warning de `Telegram polling conflict`; tratar como alerta operacional, sem reiniciar ou matar processos sem nova aprovação.

## Fonte upstream vs imagem Hostinger

Consulta GitHub API em 2026-05-05 confirmou latest upstream:

```text
NousResearch/hermes-agent latest: v2026.4.30 — Hermes Agent v0.12.0 (2026.4.30)
published_at: 2026-04-30T18:31:21Z
url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.30
```

Probe read-only do GHCR para `ghcr.io/hostinger/hvps-hermes-agent` em 2026-05-05 confirmou que a registry aceita token bearer anônimo para pull e lista apenas 5 tags:

```text
8eb9eb9
ba03513
latest
sha256-6eeb47c07ff4003d3a50386b4453778fa21b96f5a5c3bb6567514b595c83056a
sha256-7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7
```

Manifest/digest observado por tag:

| Tag | Digest OCI index | Criado | Label `org.opencontainers.image.version` | Observação |
|---|---|---:|---|---|
| `latest` | `sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7` | 2026-04-15 14:45 UTC | `8eb9eb9` | mesma imagem atualmente rodando |
| `8eb9eb9` | `sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7` | 2026-04-15 14:45 UTC | `8eb9eb9` | alias de `latest` |
| `ba03513` | `sha256:6eeb47c07ff4003d3a50386b4453778fa21b96f5a5c3bb6567514b595c83056a` | 2026-04-15 13:44 UTC | `ba03513` | imagem anterior, não upgrade |

Labels da imagem Hostinger apontam para `https://github.com/hostinger/docker-compose-catalog` e não para tags upstream `NousResearch/hermes-agent`. Portanto, nesta data não havia tag pública Hostinger mais nova que `latest` para avançar o runtime acima de `v0.9.0` sem trocar fonte/estratégia de imagem.

## Próxima decisão

Se o objetivo for apenas garantir que o container Hostinger `latest` foi puxado com segurança, a fase está concluída: pull/up executados, containers saudáveis e rollback tag preservada.

Se o objetivo for de fato chegar em `v0.12.0`, a próxima fase deve ser investigação/aprovação separada para uma destas rotas:

1. confirmar com Hostinger/registry se existe tag nova suportada para `hvps-hermes-agent`;
2. aguardar o catálogo Hostinger atualizar `latest`;
3. avaliar imagem customizada baseada em `NousResearch/hermes-agent`, com plano explícito de build, teste, compose diff e rollback.

Não trocar repositório/tag de imagem nem editar Compose sem aprovação explícita do Lucas.
