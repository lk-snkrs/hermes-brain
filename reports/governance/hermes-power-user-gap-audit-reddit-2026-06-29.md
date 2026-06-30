# Hermes Power-User Gap Audit — Reddit benchmark

Data: 2026-06-29T09:32:03Z  
Pedido de Lucas: “Fazer a auditora do 1 ao 5” após comparar o setup Lucas/Cimino com o post Reddit “My Hermes setup, roast me”.

## Escopo

Auditoria read-only/local dos 5 eixos propostos:

1. Software factory
2. Bridge operacional
3. Task OS
4. Skills/runtime cleanup
5. Daily usage UX

## Fontes e evidências usadas

- Post Reddit consultado por `web_extract`/search; acesso direto Reddit `.json` bloqueado por `robots.txt`, browser exigiu login/minimal page.
- `hermes status --all`: Hermes Agent v0.17.0, provider OpenAI Codex, gateway docker foreground running, Telegram configured, 42 active / 46 total scheduled jobs, 4141 sessions.
- Runtime profiles read-only via `/opt/data/profiles/*/config.yaml` and `/proc/*/environ`:
  - perfis com gateway vivo: default, mordomo, lk-growth, spiti, spiti-atendimento, lk-ops, lk-shopify, lk-trends, lk-collection-optimizer, lk-stock, lk-finance, lk-content, lc-claude-cli.
  - perfis configurados adicionais/worker-ish: brain-process, hermes-ops-readonly, lk-analyst-readonly, lk-content-reviewer.
- Cron registry default: 46 jobs; registries especialistas com jobs locais: lk-shopify, lk-trends, mordomo, lk-finance, lk-ops, spiti-atendimento, lk-content, lk-stock, lk-growth.
- Scripts em `/opt/data/scripts`: 175 arquivos; 44 watchdogs; 16 auditores; brokers/wrappers como `hermes_cli_integrations.py` e `hermes_cli_run.py`.
- Brain governance evidence: Task OS, Mesa COO, handoff ledger, organogram/Amora audits, Kanban docs/receipts, Runtime Truth Reconciler, Memory OS/Honcho routines.
- Honcho context consulted: returned relevant recent messages only; useful for continuity of this request, not enough as a domain source. Brain/live evidence used as source of truth.

## Benchmark externo resumido

O post Reddit descreve um setup Hermes focado em desenvolvimento solo:

- perfis simples e funcionais: `local-admin`, `planner`, `coder`, `qa-tester`, `repository`;
- Docker/local stack com SearXNG, Hindsight/pgvector, Bitwarden Lite, pi-coding-agent;
- host-side `hermes-bridge.py` para build/deploy/logs/restart;
- Hermes abrindo tarefas, escrevendo código, rodando QA, deployando e mantendo documentação;
- Telegram como superfície de review pelo humano.

## Notas executivas por eixo

| Eixo | Nota | Veredito curto |
|---|---:|---|
| 1. Software factory | 6.5/10 | Base forte de agentes/subagentes, mas não há esteira padrão planner→coder→QA→review→receipt aplicada por default. |
| 2. Bridge operacional | 7.0/10 | Broker/Doppler/wrappers são mais seguros que o setup Reddit, porém menos simples/ergonômicos como “ponte única de operações”. |
| 3. Task OS | 7.5/10 | Governança madura; Kanban/Task OS existem, mas ainda não viraram fluxo cotidiano leve de execução e fechamento. |
| 4. Skills/runtime cleanup | 6.0/10 | Muito conhecimento acumulado, mas com sprawl, skills grandes, referências demais e toolsets heterogêneos. |
| 5. Daily usage UX | 7.0/10 | Mesa COO/Telegram/watchdogs são avançados; ainda há ruído, decision cards pouco previsíveis e gap entre relatório e ação. |

Nota geral: **6.8/10 em ergonomia power-user**; **8.2/10 em governança/safety multiempresa**.

## 1. Software factory

### O que já existe

- `delegate_task`, perfis especialistas, Codex/GPT-5.5, Claude CLI proxy, skills de desenvolvimento, Kanban/Task OS e scripts de auditoria.
- Perfis que poderiam compor lanes de fábrica:
  - default/Hermes Geral: orquestração;
  - `lc-claude-cli`: alternativa forte para raciocínio/código;
  - `hermes-ops-readonly` e `brain-process`: governança/ops read-only;
  - especialistas LK/SPITI/Mordomo.
- Evidência de práticas maduras: verification-before-completion, receipts, approval packets, Brain governance, runtime readbacks.

### Gap

O uso real ainda é mais “responder/incidente/governança” do que uma fábrica padronizada:

- não há um fluxo cotidiano obrigatório tipo `planner → builder → qa-tester → reviewer → receipt`;
- QA independente acontece, mas não como lane previsível;
- delegation/subagents são usados pontualmente, não como rotina de fechamento de todo trabalho material;
- Task OS existe, mas nem toda demanda operacional vira automaticamente card com dono, risco, status e evidência.

### Recomendação

Criar uma rotina/padrão chamado **Hermes Workcell v1**:

- Planner: quebra escopo e fontes.
- Executor: faz local/read-only ou prepara approval packet.
- QA: valida com evidência independente.
- Reviewer: checa segurança/segredos/fonte.
- Receipt: fecha no Brain/Task OS.

Começar sem novo runtime: apenas rotina + template + piloto em 1 tarefa local por dia.

## 2. Bridge operacional

### O que já existe

- Broker central Hermes/Doppler-first:
  - `hermes-cli-integrations`
  - `hermes-cli-run`
  - `hermes_doppler.py`
- Scripts/wrappers: 175 scripts, 44 watchdogs, 16 auditores.
- Integrações com políticas claras: Shopify CLI oficial, Google Workspace, Klaviyo, Supabase, GitHub, Vercel, Notion, etc.

### Gap

O setup é seguro, mas a ergonomia é fragmentada:

- o Reddit tem uma ponte operacional simples (`hermes-bridge.py`) para build/deploy/logs/restart;
- aqui temos wrappers e guardrails fortes, mas falta um **painel/CLI humano único** para “ações comuns seguras”: status, logs, QA, dry-run, smoke, report, approval packet;
- a complexidade do broker aumenta safety, mas também aumenta custo cognitivo para agentes e Lucas.

### Recomendação

Criar **Hermes Ops Bridge v1** como camada read-only/local primeiro:

- `status`: runtime/profile/crons resumidos;
- `smoke`: integrações via broker;
- `qa`: gates locais por tipo de tarefa;
- `logs`: últimos erros sanitizados;
- `packet`: cria approval packet para ações sensíveis;
- `receipt`: cria/registra receipt padronizado.

Não substituir os wrappers atuais. Seria uma fachada simples em cima deles.

## 3. Task OS

### O que já existe

- Política universal Task OS no Brain/AGENTS.
- Kanban interno documentado e já com receipts/relatórios de readiness/pilot.
- Mesa COO integrada como camada de decisões, não despejo de backlog.
- Regra de risco A0-A4 e guardrails de dispatch.

### Gap

Task OS ainda é mais forte como governança do que como hábito operacional:

- muitos outputs fecham com receipt, mas nem sempre com card vivo e owner claro;
- handoff ledger foi reconhecido anteriormente como risco de “virar documento morto” se não for usado nos ciclos materiais;
- há 46 jobs no cron default e vários registries especialistas, mas o link cron→card→owner→receipt nem sempre é visível em uma única tela.

### Recomendação

Ativar uma **rotina de Task OS minimalista**:

- toda frente não-trivial ganha `card_id` ou `receipt_id`;
- status permitido: `ready`, `running`, `blocked`, `done`, `archived/stale`;
- Mesa COO só sobe decisões/bloqueios, não backlog;
- toda conclusão material inclui: dono, evidência, rollback se aplicável, próximo gatilho.

Sem criar cron novo nesta etapa.

## 4. Skills/runtime cleanup

### O que já existe

- Skills ricas e extensas; vários perfis com 150–240+ skills disponíveis.
- Algumas skills especializadas são de altíssimo valor: Hermes Agent, Brain Governance, Lucas Runtime Ops, Honcho Memory Ops, Shopify, SEO, LK, etc.
- Memória/Brain/skills já guardam muitas correções de Lucas e pitfalls operacionais.

### Gap

A abundância virou custo:

- perfis como `lk-collection-optimizer`, `lk-shopify`, `lk-stock`, `lk-trends`, `mordomo`, `spiti` têm centenas de skills; isso melhora cobertura, mas aumenta carga de prompt/seleção e risco de skill errada.
- Há skills muito grandes e referências numerosas; algumas são melhores como `references/` do que como SKILL.md carregado.
- Toolsets Telegram variam bastante entre perfis; alguns são estreitos demais para manutenção, outros amplos demais para chat rápido.

### Recomendação

Fazer uma **Skill Surface Diet** por ondas:

1. Top 20 skills realmente usadas por profile.
2. Skills obrigatórias por classe: Hermes runtime, Brain, Shopify, LK, etc.
3. Arquivar/baixar prioridade de skills raras/duplicadas.
4. Splitar skills gigantes em SKILL.md curto + references.
5. Medir latência/contexto antes/depois.

Ação inicial segura: relatório read-only de `skills_count`, skill load frequency por sessão/log se disponível, e recomendações por profile.

## 5. Daily usage UX

### O que já existe

- Mesa COO diária Telegram.
- Relatório Hermes diário obrigatório no Telegram.
- Watchdogs silent-OK; alertas para falha/decisão.
- Inline decisions e policy de Telegram limpo.
- Honcho/Memory OS/Brain OS/Runtime Truth/Reminder OS.

### Gap

O UX ainda alterna entre “muito bom” e “muito técnico”:

- Lucas ainda recebe cards que geram decisões corretas, mas às vezes exigem entender runtime/cron/receipt para agir.
- Há risco de Telegram mostrar mais “estado do sistema” do que “decisão executiva”.
- Relatórios são numerosos; alguns são `local`, mas os que chegam ao Telegram precisam virar menos diagnóstico e mais decisão/ação.
- O recente caso do cron Honcho mostrou maturidade boa: detectar divergência, approval packet, wrapper, readback, receipt. Esse padrão deve virar default, não exceção.

### Recomendação

Criar o contrato **Telegram Executive UX v2**:

- 1 decisão por mensagem;
- sem job_id/JSON/wrapper salvo quando solicitado como evidência;
- sempre: “por que importa”, “ação proposta”, “risco”, “botões/opções”;
- quando for execução já aprovada: output de negócio primeiro, receipt como rodapé;
- silent-OK radical para rotina saudável.

## Priorização recomendada

### P0 — fazer agora/local/read-only

1. Registrar esta auditoria como benchmark de maturidade Hermes power-user.
2. Criar checklist **Hermes Workcell v1** em Brain: planner/executor/QA/reviewer/receipt.
3. Criar backlog/approval packet para **Hermes Ops Bridge v1** read-only.
4. Criar relatório de **Skill Surface Diet** por profile.
5. Ajustar Mesa/Telegram contract como UX v2, sem mexer em runtime.

### P1 — piloto com baixo risco

1. Rodar Workcell v1 em uma tarefa real local/read-only.
2. Usar subagente QA independente antes de fechar tarefa material.
3. Criar comando/script local read-only de status executivo de runtime.
4. Linkar card→receipt→source evidence em uma frente concreta.

### P2 — só com aprovação escopada

1. Mudar crons, schedules, delivery ou dispatch.
2. Reiniciar gateways/perfis.
3. Habilitar dashboard/API/plugin público.
4. Alterar Docker/VPS/Traefik.
5. Fazer writes externos/deploys/mutations.

## Veredito final

O setup Lucas/Cimino não está “menos avançado” que o do Reddit; ele está **mais governado e mais complexo**, mas menos ergonômico como fábrica diária.

O principal gap não é instalar mais coisas. É transformar a capacidade já existente em uma esteira simples:

`pedido → card/escopo → planner → executor → QA independente → receipt → Mesa só se decisão/bloqueio`.

Se fizermos isso, o Hermes deixa de ser um conjunto de agentes e rotinas poderosas e vira um **sistema operacional de trabalho** mais parecido com o power-user do Reddit, mas com a segurança multiempresa que Lucas precisa.

## Não realizado

- Nenhum cron alterado.
- Nenhum gateway/Docker/VPS/Traefik reiniciado.
- Nenhuma credencial lida ou impressa.
- Nenhuma integração externa acionada para write.
- Nenhum profile/toolset/config modificado.
