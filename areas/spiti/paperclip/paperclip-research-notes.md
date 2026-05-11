# Paperclip — notas de pesquisa para implantação SPITI

> Data: 2026-05-05
> Fontes principais: `https://paperclip.ing`, `https://docs.paperclip.ing`, `https://github.com/paperclipai/paperclip`, `https://github.com/AgriciDaniel/claude-seo`, `https://github.com/AgriciDaniel/codex-seo`.

---

## 1. O que é Paperclip

Paperclip é um **sistema operacional/control plane para empresas rodadas por agentes de IA**. A analogia da documentação é: se OpenClaw/Claude/Codex/Hermes são funcionários, Paperclip é a empresa, o organograma, o task board, o orçamento, a governança e o audit trail.

Ele não é apenas um chat. Ele organiza agentes em uma Company, com missão, projetos, issues, managers, rotinas, aprovações, budgets, custos e skills.

---

## 2. Conceitos centrais

### Company

Boundary principal. Contém:

- missão/goal;
- agentes;
- tasks/issues;
- projetos;
- budgets;
- skills;
- approvals;
- activity log.

Para Lucas/SPITI, a Company deve isolar SPITI da LK Sneakers.

### Agent

Funcionário IA. Tem:

- nome;
- cargo/title;
- role;
- manager/reportsTo;
- adapter;
- orçamento mensal;
- run policy;
- skills.

Agentes não precisam rodar continuamente. Ideal é acordarem por assignment, rotina ou manual wake.

### Task/Issue

Unidade de trabalho rastreável. Status típicos:

```text
backlog → todo → in_progress → in_review → done
```

Também pode ter `blocked` ou `cancelled`.

### Project

Agrupa issues relacionados a um repo, workspace, produto ou objetivo. Em SPITI, os projetos naturais são:

- Spiti Hub;
- SEO & Content;
- Newsletter;
- Paid Social Creative;
- Analytics;
- Future Public Site.

### Heartbeat

Janela de execução do agente. Pode ser acionado por:

- timer;
- assignment;
- wake manual;
- rotina;
- webhook.

Recomendação Paperclip: timer desligado por padrão, porque heartbeat em intervalo gera ruído e custo.

### Routine

Job recorrente ou webhook que cria/atribui issue para um agente. Melhor para tarefas agendadas do que heartbeat de poucos minutos.

### Approval

Camada de governança. Tipos relevantes:

- `hire_agent`;
- `approve_ceo_strategy`;
- `budget_override_required`;
- `request_board_approval`.

Para SPITI, approvals são obrigatórios para qualquer ação externa: WhatsApp, email, newsletter, post, ads, deploy prod, Supabase write/migration, merge main, export de dados pessoais.

### Skills

Procedimentos reutilizáveis. Podem vir de:

- GitHub repo;
- gist;
- pasta local;
- skills.sh;
- criação manual.

Para SPITI, criar skills próprios:

- `spiti-brand-voice`;
- `spiti-data-safety`;
- `spiti-hub-pr-workflow`;
- `spiti-content-factuality-check`.

---

## 3. Adapters relevantes

Paperclip suporta adapters como:

- `claude_local` — Claude Code local;
- `codex_local` — Codex CLI local;
- `gemini_local`;
- `opencode_local`;
- `cursor`;
- `pi_local`;
- `hermes_local`;
- `openclaw_gateway`;
- HTTP/webhook/process/custom.

### Hermes Local

`hermes_local` roda Hermes Agent na mesma máquina do Paperclip.

Quando usar:

- já existe Hermes instalado;
- precisa memória persistente;
- precisa session search;
- precisa subagent delegation;
- precisa 30+ ferramentas e 80+ skills;
- precisa model routing multi-provider;
- precisa MCP.

Campos comuns:

- `model` — formato provider/model;
- `provider` — `auto`, `openrouter`, `nous`, `openai-codex`, etc.;
- `timeoutSec`;
- `toolsets`;
- `persistSession`;
- `worktreeMode`;
- `checkpoints`;
- `hermesCommand`;
- `env`;
- `paperclipApiUrl`.

Para Lucas, Hermes atual está em GPT-5.5 via `openai-codex`, com terminal local e skills. Faz sentido testar `hermes_local` para o Chief of Staff.

### Claude/Codex Local

Bom para agentes de coding e SEO quando a skill específica é do ecossistema Claude/Codex.

- `claude_local` combina com `claude-seo`.
- `codex_local` combina com `codex-seo` e com o provider atual do Hermes.

---

## 4. Deployment

Paperclip pode rodar:

- desktop macOS;
- terminal local;
- server/VPS;
- Docker.

Docker quickstart usa porta padrão `3100` e persistência em `PAPERCLIP_HOME`/bind mount.

Variáveis importantes:

- `PORT`
- `HOST`
- `DATABASE_URL`
- `PAPERCLIP_HOME`
- `PAPERCLIP_INSTANCE_ID`
- `PAPERCLIP_DEPLOYMENT_MODE`
- `PAPERCLIP_PUBLIC_URL`
- `PAPERCLIP_AGENT_JWT_SECRET`
- `PAPERCLIP_SECRETS_MASTER_KEY`
- `HEARTBEAT_SCHEDULER_ENABLED`
- `HEARTBEAT_SCHEDULER_INTERVAL_MS`

Para SPITI, antes de configurar produção, confirmar onde o Paperclip da LK Sneakers está rodando e se a SPITI será uma Company na mesma instância ou instância separada.

Recomendação: Company separada no mínimo. Instância separada se houver risco de mistura de secrets/clientes.

---

## 5. API Paperclip

API base: `/api`.

Recursos pesquisados:

- `GET /api/companies`
- `POST /api/companies`
- `GET /api/companies/{companyId}/agents`
- `GET /api/companies/{companyId}/issues`
- `GET /api/companies/{companyId}/approvals`
- `POST /api/companies/{companyId}/approvals`
- `GET /api/companies/{companyId}/routines`
- `POST /api/companies/{companyId}/routines`

Autenticação:

- modo local trusted: board implícito;
- modo authenticated: cookie/session;
- API token board;
- agent bearer/JWT.

Para automação programática futura, podemos usar API em vez de UI, mas primeiro fazer setup inicial manual/assistido.

---

## 6. Claude SEO / Codex SEO

### Claude SEO

Repo: `AgriciDaniel/claude-seo`.

Descrição: suíte SEO para Claude Code com sub-skills, subagents e extensões.

Cobertura:

- technical SEO;
- on-page;
- content quality/E-E-A-T;
- schema;
- image optimization;
- sitemap architecture;
- GEO/AEO;
- local SEO;
- maps intelligence;
- semantic topic clustering;
- SXO;
- drift monitoring;
- ecommerce;
- international SEO/hreflang;
- Google APIs: GSC, PageSpeed, CrUX, GA4;
- PDF/HTML reports;
- DataForSEO;
- Firecrawl;
- Banana/image generation extension.

Comandos principais:

- `/seo audit <url>`
- `/seo page <url>`
- `/seo sitemap <url>`
- `/seo sitemap generate`
- `/seo schema <url>`
- `/seo images <url>`
- `/seo technical <url>`
- `/seo content <url>`
- `/seo geo <url>`
- `/seo plan <type>`
- `/seo local <url>`
- `/seo maps [command]`
- `/seo hreflang <url>`
- `/seo google [command] [url]`
- `/seo google report [type]`

### Codex SEO

Repo: `AgriciDaniel/codex-seo`.

Port Codex-first com TOML agents, workflows e runners determinísticos. Útil para ambientes baseados em Codex/OpenAI.

Para Lucas/Hermes atual em GPT-5.5 via `openai-codex`, avaliar `codex-seo` como alternativa natural ao `claude-seo`.

---

## 7. Aplicação SPITI

### Onde Paperclip brilha para SPITI

- Coordenar vários workstreams ao mesmo tempo sem perder contexto.
- Transformar ideias do Lucas em issues e rotinas.
- Manter PRs do Spiti Hub rastreáveis.
- Criar calendário e linha de produção SEO.
- Criar relatórios recorrentes de GA4/GSC.
- Gerar drafts de newsletter e criativos com aprovação.
- Dar governança para agentes que poderiam fazer coisas arriscadas.

### O que Paperclip não deve fazer sozinho

- Enviar comunicação externa.
- Publicar posts.
- Lançar campanhas pagas.
- Fazer deploy prod.
- Alterar Supabase produção.
- Inventar dados curatoriais/comerciais.

---

## 8. Config inicial recomendada

Company:

- `SPITI Auction Growth & Product OS`

Missão:

- Ver PRD de implantação.

Primeiro agente:

- `SPITI Chief of Staff`
- role CEO / Chief of Staff
- adapter preferencial: `hermes_local` se disponível.

Projetos:

1. Spiti Hub — Produto & Engenharia
2. SPITI SEO & Content Engine
3. SPITI Newsletter & CRM Activation
4. SPITI Paid Social Creative Studio
5. SPITI Analytics & Growth Intelligence
6. Future SPITI Public Site

Rotinas:

- Weekly Spiti Hub Triage
- Weekly SEO Opportunity Scan
- Monthly SEO Audit Lite
- Editorial Calendar Planning
- Paid Social Creative Sprint
- Newsletter Draft Review

---

## 9. Próximo checklist operacional

1. Confirmar onde Paperclip da LK está rodando.
2. Decidir mesma instância vs instância separada para SPITI.
3. Criar Company com nome/missão do PRD.
4. Criar Chief of Staff.
5. Criar projetos.
6. Criar/importar skills SPITI.
7. Testar adapter com uma issue read-only.
8. Testar GitHub PR workflow em mudança pequena no Spiti Hub.
9. Testar auditoria SEO read-only no site atual.
10. Só depois ativar rotinas recorrentes.
