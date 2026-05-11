# Plano — próximas melhorias Hermes v0.13 após `approvals.mode: off`

Data: 2026-05-10
Ambiente verificado: runtime Docker, hostname `46e218f8d4c9`, PID 1 `tini -- /opt/hermes/docker/entrypoint.sh gateway run`.

## Estado verificado

- Hermes ativo: `Hermes Agent v0.13.0 (2026.5.7)` em `/opt/hermes`.
- Config em uso: `/opt/data/config.yaml`.
- `approvals.mode`: `false` no YAML, equivalente a `off`.
- Gateway/cron: `hermes cron status` reporta gateway rodando e scheduler ativo.
- Crons ativos: 4.
- Watchdog `no_agent` runtime/cron: `edd06fe19397`, ativo, último run `ok`.
- Watchdog `no_agent` freshness artefatos: `e7a61e275c37`, ativo, último run `ok`.
- Board Kanban `lk-growth-ops`: 8 cards `ready`, todos `unassigned` por segurança.
- Assignees Kanban no disco: apenas `default`.

## Correção operacional importante

O Hermes de produção aqui roda em Docker. O processo atual confirma isso:

```text
inside_docker=yes
pid1=tini /opt/hermes/docker/entrypoint.sh gateway run
```

Portanto, qualquer melhoria que envolva imagem, compose, gateway, containers, volumes, redes, Traefik ou Hostinger deve ser tratada como mudança de infra/produção, com plano + rollback. `approvals.mode: off` remove prompts operacionais, mas não remove esse guardrail.

## O que já está seguro e operacional

### 1. Watchdogs `no_agent`

Contratos validados manualmente em 2026-05-10:

- `python3 /opt/data/scripts/hermes_runtime_cron_watchdog.py` → `rc=0`, stdout vazio.
- `python3 /opt/data/scripts/hermes_artifacts_freshness_watchdog.py` → `rc=0`, stdout vazio.
- `--verbose` confirma versão, config, gateway, jobs, report semanal LK e Kanban sem imprimir secrets.

Conclusão: os watchdogs já estão em produção silenciosa e compatíveis com o contrato `no_agent`.

### 2. Mission Control LK via Kanban

Board `lk-growth-ops` existe e está saudável, mas sem workers reais. Isso é intencional: evita execução automática antes de definir perfis, toolsets e limites por tipo de card.

## Próximas melhorias recomendadas

### A. Worker readiness sem ativar execução automática

Baixo risco. Criar documentação e configuração-modelo para perfis:

- `lk-analyst-readonly`: análise de Shopify/GA4/Meta/Tiny em modo read-only, sem envio e sem writes.
- `lk-content-reviewer`: QA de e-mail/brand/tom/preview, sem envio.
- `hermes-ops-readonly`: inspeção de runtime/logs/cron, sem restart/Docker writes.
- `brain-process`: atualização de docs/skills/rotinas no Hermes Brain.

Antes de ativar dispatch real:

- validar que cada perfil tem toolsets mínimos;
- validar que secrets só são acessados por Doppler/process env;
- criar um card piloto interno e não externo;
- verificar logs e output;
- manter rollback: desatribuir cards, reclaim de tarefas running e pausar qualquer cron/dispatcher adicional se criado.

### B. Dashboard local-only

Médio risco por tocar superfície de acesso. Caminho seguro:

1. Diagnóstico read-only dos comandos dashboard/kanban disponíveis.
2. Se dashboard já existir no gateway interno, expor apenas via bind local/container e túnel SSH.
3. Não publicar via Traefik/domínio público.
4. Rollback: matar processo/túnel local; nenhuma alteração permanente em compose sem PR/plano.

### C. Docker/imagem/runtime

Alto risco. Não repetir deploy às cegas. Antes de qualquer rebuild/troca de imagem:

1. Pegar logs reais do host: `/root/hermes-upgrade-backups/20260510T213142Z-deploy-v2.log`.
2. Confirmar compose/project path no Hostinger.
3. Backup de config, env refs, skills, cron, sessions e volumes relevantes.
4. Build paralelo com tag nova.
5. Healthcheck Telegram/cron antes e depois.
6. Rollback explícito para tag anterior.

Observação: o log citado não existe dentro do container atual; ele está no host. Acesso SSH/Hostinger precisa ser verificado antes.

### D. Shopify optional skill

Médio risco por secrets e potencial write. Caminho seguro:

1. Inventariar somente nomes de secrets no Doppler `lc-keys/prd`.
2. Criar skill/workflow Shopify LK read-only primeiro.
3. Proibir writes por padrão: produto, estoque, preço, tags, clientes, orders, campanhas.
4. Permitir apenas relatório/preview até Lucas aprovar cada ação externa ou mutação.

## Gate de ativação

A próxima ação segura é **A: worker readiness sem ativar execução automática**. Ela transforma o Kanban em operação real sem ainda mexer em Docker/Hostinger nem expor dashboard.
