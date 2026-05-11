# Rotina — Operacionalização Hermes v0.13

Data: 2026-05-10
Escopo: Hermes/LK/Hermes Brain em produção Docker v0.13.0.

## Objetivo

Transformar as novidades do Hermes v0.13 em uso prático no dia a dia do Lucas sem mexer em produção, Docker, secrets, bancos, campanhas ou envios externos sem aprovação explícita.

## Estado operacional atual

- PRD de roteamento COO criado: `areas/operacoes/prds/hermes-coo-routing-layer-prd.md`. A regra é: Lucas define intenção; Hermes escolhe automaticamente entre execução direta, `/goal`, `/background`, cron `no_agent`, cron com agente, Kanban, skill, Brain doc/PRD ou subagentes conforme horizonte, risco e recorrência.
- Produção Hermes está Docker-first no projeto Hostinger `/docker/hermes-agent-5ajw`.
- Containers esperados: dashboard e Telegram usando imagem `hermes-agent-custom:v0.13.0-20260510`.
- Versão esperada nos containers: `Hermes Agent v0.13.0 (2026.5.7)`.
- Cron diário de melhoria contínua: `f5a23dd6a1bd`, 02:00 BRT.
- Watchdog runtime/cron `no_agent`: `edd06fe19397`, a cada 30 min, silencioso quando OK.
- Watchdog artefatos/freshness `no_agent`: `e7a61e275c37`, diário 09:00 BRT, silencioso quando OK.
- Mission Control Kanban criado: board `lk-growth-ops`, 7 cards iniciais, todos sem assignee para não disparar workers.
- O incidente do deploy v2 foi smoke test usando `python` puro dentro do container; smoke correto deve usar `/opt/hermes/.venv/bin/python` ou `python3`.

## Melhorias v0.13 adotadas agora — baixo risco

### 1. `/goal` como padrão para missões longas

Use quando a tarefa tiver várias etapas e não deve depender de Lucas mandar “seguir” repetidamente.

Estado operacional: ensinado como rotina e conectado ao board `lk-growth-ops`. Para missões longas, a resposta esperada do Hermes deve incluir checklist, artefato no Brain quando aplicável e separação entre ações autônomas e itens que exigem aprovação.

Prompt recomendado para uso imediato no Telegram:
- `/goal Tocar LK Growth Ops por 7 dias: manter board lk-growth-ops atualizado, validar relatório semanal de influenciadores produto+SKU+tamanho, registrar aprovações/correções no Brain e pedir aprovação antes de qualquer envio externo ou mudança em produção.`

Exemplos:
- `/goal Operacionalizar relatório semanal LK com fonte Shopify, Meta por ad_id, produto+SKU+tamanho, preview visual e aprovação antes de envio.`
- `/goal Auditar releases Hermes e transformar cada melhoria útil em skill, rotina ou checklist no Brain.`
- `/goal Preparar plano de dashboard local-only com riscos, rollback e sem exposição pública.`

Resultado esperado:
- objetivo persistente;
- checklist claro;
- retomada sem reexplicar contexto;
- separação entre baixo risco executável e passos que pedem aprovação.

Sinal de falha:
- objetivo genérico;
- perde contexto entre turnos;
- tenta executar produção/externo sem plano.

### 2. Kanban/Mission Control como sistema de trabalho, não chat solto

Primeiro board recomendado: `lk-growth-ops`.

Colunas iniciais:
- Backlog;
- Doing;
- Waiting Lucas;
- Waiting External;
- QA;
- Done.

Lanes/perfis conceituais para começar sem inflar agentes:
- `lk-data`: Shopify, Tiny, GA4, Meta, Pareto, Supabase;
- `lk-creative`: criativos, layout, email visual, assets;
- `lk-email`: Klaviyo/Gmail/Cloudflare previews, MIME, deliverability;
- `brain-docs`: PRDs, rotinas, skills, learning loop;
- `ops`: Hermes, cron, Docker read-only, observabilidade;
- `review`: QA final, secret scan, evidência.

Uso seguro agora:
- documentar board, colunas e critérios de pronto;
- usar como checklist operacional;
- não iniciar workers de produção nem alterar gateway sem aprovação.

Critério de “Done”:
- evidência anexada;
- fonte de dados declarada;
- riscos/aprovações registrados;
- Brain/skill atualizado se houver aprendizado.

### 3. `no_agent` cron como watchdog barato

Aplicar primeiro em checks read-only que só avisam quando há anomalia. Empty stdout deve ficar silencioso.

Estado operacional:
- `edd06fe19397`: runtime/cron health, schedule `*/30 * * * *`, script `/opt/data/scripts/hermes_runtime_cron_watchdog.py`.
- `e7a61e275c37`: freshness de artefatos v0.13, schedule `0 12 * * *` (09:00 BRT), script `/opt/data/scripts/hermes_artifacts_freshness_watchdog.py`.

Candidatos LK/Hermes:
- Hermes runtime drift: versão/container diferente do esperado;
- cron scheduler parado ou sem próximo run;
- relatório semanal LK não gerado até horário limite;
- gaps de dados Shopify/GA4/Meta/Tiny;
- logs recentes com traceback no Telegram container;
- email semanal sem raw MIME validado.

Guardrail:
- watchdog pode ler e alertar;
- não reinicia container;
- não corrige produção sozinho;
- não envia email/WhatsApp/campanha;
- não imprime secrets.

### 4. `[[as_document]]` para relatórios longos

Usar quando o output no Telegram ficar longo demais para leitura ou retenção.

Candidatos:
- auditoria mensal LK;
- matriz de atribuição influencer × produto × SKU × tamanho;
- relatório de release catch-up Hermes;
- PRD/decision brief de mudanças de runtime.

### 5. Segurança v0.13 incorporada ao processo

Toda rotina nova deve declarar:
- fonte de verdade;
- se é read-only ou write;
- quais ações exigem aprovação;
- secret scan antes de reportar;
- rollback quando tocar estado persistente.

Para logs e debug:
- qualquer token, password, connection string, cookie ou key deve sair como `[REDACTED]`;
- não colar secrets no Brain;
- preferir Doppler/env sob demanda.

## Itens que exigem aprovação antes de executar

- Criar/ativar board Kanban com workers reais no gateway de produção.
- Expor dashboard publicamente ou alterar Traefik/reverse proxy.
- Alterar Docker/compose/image/runtime/restart.
- Instalar Shopify optional skill com permissões além de leitura.
- Criar watchdog que execute correção automática em produção.
- Migrar envio real de e-mail semanal LK/Cloudflare/Klaviyo.

## Checklist ao aplicar uma novidade Hermes

1. A novidade resolve um problema real de Lucas/LK?
2. É read-only/documentação/skill/checklist ou muda produção?
3. Dá para operacionalizar sem restart?
4. Existe fonte de verdade e evidência?
5. Há risco de misturar LK/Zipper/SPITI?
6. Precisa de aprovação?
7. O resultado ficou registrado em Brain/skill/cron/checklist?

## Próximo plano pós-`approvals.mode: off`

Plano operacional: `areas/operacoes/rotinas/hermes-v013-next-improvements-plan-2026-05-10.md`.

Estado confirmado em 2026-05-10:

- runtime atual é Docker (`/.dockerenv` presente; PID 1 via `/opt/hermes/docker/entrypoint.sh gateway run`);
- config ativo em `/opt/data/config.yaml`;
- crons `no_agent` `edd06fe19397` e `e7a61e275c37` ativos, com `rc=0` e stdout vazio quando OK;
- board `lk-growth-ops` saudável com 8 cards `ready`, ainda sem workers reais;
- log de rollback `/root/hermes-upgrade-backups/20260510T213142Z-deploy-v2.log` não está dentro do container atual; para diagnóstico do deploy v2 é necessário acesso ao host Hostinger.

Próxima ação recomendada: preparar `worker readiness` e perfis/toolsets do Kanban sem ativar dispatch automático ainda.

## Run diário — 2026-05-11 02:00 BRT

Relatório: `reports/hermes-continuous-improvement/2026-05-11.md`.

Estado confirmado a partir do container atual:

- `/opt/hermes/.venv/bin/hermes --version` retorna `Hermes Agent v0.13.0 (2026.5.7)`;
- config ativo: `/opt/data/config.yaml`;
- gateway reportado por `hermes status --all` como `running`, manager `docker (foreground)`;
- 5 crons ativos, incluindo o diário `f5a23dd6a1bd`, os watchdogs `no_agent` `edd06fe19397` e `e7a61e275c37`, e o recheck one-shot `635d6bceab80`;
- watchdog runtime/cron e watchdog freshness continuam com contrato silencioso OK (`rc=0`, stdout vazio, stderr vazio);
- GitHub releases não mostrou release público posterior a `v2026.5.7`/v0.13.0.

Gap registrado: este cron roda dentro de container sem acesso ao Docker daemon (`/var/run/docker.sock` indisponível). Portanto, nesta execução, não foi possível confirmar via `docker ps` as imagens dos containers nem ler logs Docker diretamente. Fechar esse gap exige plano separado de observabilidade Docker read-only no host, socket controlado ou SSH, com aprovação Lucas por tocar superfície de infra.

## Relação com release catch-up

Matriz principal: `reports/hermes-release-catchup-2026-05-10/action-matrix.md`.

Esta rotina é a camada prática: converte a matriz em comportamento diário.
