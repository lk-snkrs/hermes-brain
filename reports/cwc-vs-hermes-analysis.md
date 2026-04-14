# CWC vs Hermes — Análise Comparativa

*Documento gerado em: 2026-04-14*
*Contexto: CWC (cerebro-cimino via OpenClaw) vs Hermes Agent (Nous Research)*

---

## 1. Arquitetura de Memória

### CWC (Cerebro-Cimino)

CWC possui uma arquitetura de memória **distribuída, versionada e multi-camada**, completamente respaldada por Git:

```
cerebro-cimino/ (repositório Git — fonte de verdade permanente)
├── empresa/
│   ├── contexto/
│   │   ├── decisions.md       ← Decisões permanentes (infra, bancos, comunicação)
│   │   ├── lessons.md         ← Lições aprendidas (técnicas e de negócio)
│   │   ├── people.md          ← Equipe e parceiros
│   │   ├── metricas.md        ← KPIs e metas
│   │   └── channels.md        ← Canais de comunicação
│   ├── gestao/
│   │   ├── licoes.md          ← Lições consolidadas
│   │   ├── pendencias.md      ← Bloqueios e aguardando
│   │   ├── projetos.md        ← Status de projetos
│   │   └── reports/           ← Relatórios internos
│   └── decisoes/
│       ├── 2026-03.md         ← Decisões de março
│       ├── 2026-04.md         ← Decisões de abril
│       └── councils/          ← Decisões de conselho
├── areas/
│   ├── lk/                    ← LK Sneakers (spec + contexto)
│   ├── zipper/                ← Zipper Galeria
│   └── spiti/                 ← SPITI Auction
└── agentes/
    ├── claw/                  ← Agente principal (COO)
    │   ├── SOUL.md, AGENTS.md, HEARTBEAT.md, MEMORY.md, TOOLS.md
    │   └── memory/            ← Memória operacional do Claw
    ├── lk/, zipper/, spiti/, marketing/  ← Agentes especializados
    └── COMO-CONECTAR.md       ← Dokumentação de integração Git
```

**Flush de memória:** Ao atingir 40k tokens, categoriza em 5 tópicos:
1. Decisões → `memory/context/decisions.md`
2. Mudanças → `memory/context/decisions.md`
3. Lições → `memory/context/lessons.md`
4. Bloqueios → `memory/pending.md`
5. Fatos-chave → `memory/projects/*.md`

**Busca híbrida:** BM25 (palavras-chave exatas) + Vector (semântica).

### Hermes Agent

Hermes possui uma arquitetura de memória **simplificada, centralizada em arquivos Markdown**:

```
/root/hermes-brain/ (repositório Git — fonte de verdade)
├── memories/
│   ├── decisions.md   ← Decisões permanentes (copiado do cerebro-cimino)
│   ├── lessons.md     ← Lições aprendidas (copiado do cerebro-cimino)
│   ├── lk.md          ← Memória LK (contexto, KPIs, cross-sell)
│   ├── zipper.md      ← Memória Zipper (equipe, feiras)
│   └── spiti.md       ← Memória SPITI (lotes, canais)
├── skills/
│   ├── hermes-brain/SKILL.md       ← Skill central (índice)
│   ├── lk-crosssell/SKILL.md        ← Skill cross-sell
│   └── lk-leads-esfriando/SKILL.md  ← Skill leads dormentes
├── data/              ← (vazio)
└── reports/           ← (vazio — sem relatórios gerados)
```

**Estratégia de memória:** Leitura única no início da sessão. Sem flush automático documentado, sem categorização, sem busca híbrida.

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Fonte de verdade | Git (cerebro-cimino) | Git (hermes-brain) |
| Profundidade | Multi-camada (empresa/area/agente) | Plano (memories/*.md) |
| Flush automático | Sim (40k tokens, 5 categorias) | Não documentado |
| Busca híbrida | BM25 + Vector | Não implementada |
| Index de memória | MEMORY.md com caminhos detalhados | SKILL.md central como índice |
| Versionamento | Completo via Git | Completo via Git |

---

## 2. Loop de Boot

### CWC — Boot Sequence Completo (por exemplo, Claw)

```
1. Verificar data/hora atual via session_status
2. Ler cerebro-cimino/MAPA.md — navegar o segundo cérebro
3. Ler cerebro-cimino/empresa/contexto/decisions.md — regras permanentes e endpoints críticos
4. Ler cerebro-cimino/empresa/gestao/pendencias.md — o que está aguardando
5. Ler memory/sessions/YYYY-MM-DD.md (hoje e ontem) — contexto recente
6. Ler SOUL.md + AGENTS.md + TOOLS.md (arquivos do agente)
7. Se em sessão direta (não grupo): também ler MEMORY.md
8. Ao fim de cada tarefa → escrever no cerebro-cimino, não só no memory/
```

### Hermes Agent — Boot Sequence

Não há boot sequence formal documentado. O `SKILL.md` do hermes-brain indica:

```
1. No início de cada sessão, leia os arquivos de memória relevantes
2. Antes de tomar decisões, consulte decisions.md
3. Antes de afirmar dados, consulte as memórias correspondentes
4. Após sessões importantes, atualize as memórias
```

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Verificação de data/hora | Sim (explícita) | Não documentada |
| Leitura de MAPA/navegação | Sim (MAPA.md completo) | Não |
| Leitura de decisões | decisions.md + pendencias.md | decisions.md apenas |
| Memória de sessão recente | hoje + ontem | Não documentado |
| Git commit pós-tarefa | Obrigatório | Não documentado |
| Fontes consultadas | 5+ arquivos por sessão | ~5 arquivos (lessons, decisions, + 3 áreas) |

---

## 3. Skills & Tools

### CWC — Formato de Skill

Skills em CWC são **scripts Python completos** com documentação adjacente:

```
areas/lk/skills/
├── cross-sell/
│   ├── SKILL.md           ← Documentação (contexto, regras, credenciais)
│   └── scripts/
│       └── cross_sell_monitor.py
└── digest-diario/
    ├── SKILL.md
    └── scripts/digest_diario_lk.py
```

**Formato SKILL.md (CWC):**
```markdown
# Skill: Cross-Sell Monitor LK

## Input
- Pedidos fulfilled nas últimas 24h (Supabase LK)

## Processo
1. Busca pedidos com status `fulfilled` nas últimas 24h
2. Para cada cliente, analisa histórico de compras anteriores
3. Identifica padrões: quem comprou X também comprou Y
4. Aplica regras de cross-sell confirmadas
5. Gera sugestão de produto complementar por perfil
6. Envia preview para Lucas aprovar antes de disparar

## Output
- Preview no Telegram com lista de clientes + produtos sugeridos

## Credenciais (Doppler)
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`

## Cron
`LK Cross-Sell Monitor` — 9h10, 15h10 e 21h10 diariamente
```

**Triggers:** Crons agendados (via OpenClaw cron system).

### Hermes — Formato de Skill

Skills em Hermes seguem o padrão **YAML frontmatter + Markdown**:

```yaml
---
name: lk-crosssell
description: Monitor de cross-sell LK — detecta pedidos fulfilled e gera sugestões...
area: lk
version: 1.0.0
---

# Skill: Cross-Sell Monitor LK

## Fontes
- Scripts: /root/lk-price/ (monitor concorrentes)
- Docs: /root/hermes-brain/memories/lk.md
- Database: Supabase LK (cnjimxglpktznenpbail)

## Input
- Pedidos fulfilled nas últimas 24h (Supabase LK)

## Processo
1. Busca pedidos com status fulfilled nas últimas 24h
2. Para cada cliente, analisa histórico de compras anteriores
3. Identifica padrões: quem comprou X também comprou Y
4. Aplica regras de cross-sell confirmadas
5. Gera sugestão de produto complementar por perfil
6. Envia preview para Lucas aprovar antes de disparar

## Credenciais (Doppler)
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`

## Cron
`LK Cross-Sell Monitor` — 9h10, 15h10 e 21h10 diariamente
```

### TOOLS.md — CWC

O TOOLS.md do CWC é **extremamente detalhado** (~414 linhas):

- Lista todas as integrações ativas com status (✅/⏳/❌)
- Inclui troubleshoot para cada ferramenta
- Documenta protocolos de implementação (Phase 1, Phase 2)
- Lista todas as credenciais Doppler relevantes
- Inclui checklists de implementação

### Hermes — Sem TOOLS.md

Hermes **não possui TOOLS.md**. A documentação de ferramentas está dispersa:
- `AGENTS.md` → documentação de desenvolvimento (não operacional)
- `hermes_constants.py`, `config.yaml` → configuração de toolsets
- Sem documento unificado de credenciais ou integrais

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Formato | Markdown + scripts Python | YAML frontmatter + Markdown |
| Documentação de skill | Completa (input/output/credenciais/cron) | Completa (input/output/credenciais) |
| TOOLS.md | Sim (~414 linhas, detalhado) | **Não existe** |
| Integrações documentadas | 15+ integrações completas | Só 2 skills (LK cross-sell, leads) |
| Cron nativo | Sim (OpenClaw cron) | Sim (cron module) |
| Pasta de skills | `areas/*/skills/` (por área) | `skills/` (flat, 3 skills) |

---

## 4. Multi-Agent Architecture

### CWC — Arquitetura Multi-Agente Completa

```
Claw (main/COO) — Orquestrador
├── Acesso total ao cerebro-cimino + workspace
├── Monitora git log dos agentes especializados
├── Heartbeat de visibilidade (8h)
└── Delegação via sessions_spawn

agente-lk — Especialista LK Sneakers
├── SOUL.md: DNA mental (Hormozi, Schwartz, Virgil Abloh)
├── Escopo: areas/lk/ + empresa/contexto/ (leitura)
├── APIs: Supabase LK, Shopify, Klaviyo, Evolution Clo
└── Git commit obrigatório ao fim de sessão

agente-zipper — Especialista Zipper Galeria
├── SOUL.md: DNA mental (Obrist, Gagosian, Hormozi)
├── Escopo: areas/zipper/ + empresa/contexto/ (leitura)
├── APIs: Supabase Zipper Vendas (vendas_tango)
└── Git commit obrigatório ao fim de sessão

agente-spiti — Especialista SPITI Auction
├── Escopo: areas/spiti/ + Supabase SPITI
├── Monitor de lances (systemd + n8n)
└── Git commit obrigatório ao fim de sessão

agente-marketing — Especialista Marketing LK
├── Escopo: areas/lk/sub-areas/marketing/
├── APIs: Meta Ads, Klaviyo, GA4, Metricool, KicksDB
└── Alertas para Renan (criativo) + Lucas (aprovação)
```

**Roteamento por tópicos Telegram:**
| Tópico | Agente | Conteúdo |
|--------|--------|----------|
| topic:2 (COO) | main | Briefing, watchdog, revisão semanal |
| topic:3 (LK) | agente-lk | Digest, cross-sell, Meta Ads, churn |
| topic:4 (Zipper) | agente-zipper | Digest, CRM, alertas feiras |
| topic:5 (SPITI) | agente-spiti | GA4, monitor lances |

**Roteamento WhatsApp:**
| Grupo | Agente |
|-------|--------|
| [LK] IA Bot + Vendas | agente-lk |
| [ZPR] IA Bot + Claw Bot | agente-zipper |
| SPITI.M | agente-spiti |
| A Grande Família Zipper | main (COO) |

### Hermes — Arquitetura Single-Agent

Hermes opera como **agente único**. Existe `delegate_tool.py` para subagentes, mas:
- Não há multi-agent configurado
- Não há roteamento por área
- Não há especialização por domínio (LK, Zipper, SPITI)
- Comunicação entre agentes = inexistente

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Número de agentes | 5+ (Claw + 4 especializados) | 1 (principal) |
| Especialização por área | LK, Zipper, SPITI, Marketing | Não |
| Orquestrador (COO) | Sim (Claw) | Não |
| Roteamento por tópico | Sim (Telegram topics) | Não |
| Git como visibilidade | Sim (COO lê git log) | Não |
| Memória isolada por agente | Sim (agentDir separado) | N/A |

---

## 5. Heartbeats & Proatividade

### CWC — Sistema de Heartbeat Completo

O HEARTBEAT.md do Claw define **5 checks a cada 4h** (8h, 12h, 16h, 20h):

```markdown
### 1. Emails Urgentes (Gmail)
- Cliente incomodado? Pagamento importante? Erro de produção?
- Se SIM → avisar imediatamente

### 2. Agenda (Google Calendar — próximas 24-48h)
- Evento hoje que Lucas não viu? Reunião sem prep?
- Se SIM → avisar com contexto

### 3. Anomalias de Negócio (Supabase LK)
- Vendas caíram >20% vs ontem?
- Pedido travado >6h?
- Estoque crítico (<5 unidades)?
- Se SIM → avisar com % de impacto

### 4. Saúde de Automações (Crons)
- Cron falhou (Railway, GitHub Actions)?
- Cron atrasado >30min?
- Se SIM → avisar + tentar debug

### 5. Projetos Ativos (Memory + GitHub)
- Algo que Lucas pediu ficou >48h parado?
- PR aguardando review >24h?
- Se SIM → avisar + estado atual

### 6. 🧠 Visibilidade dos Agentes (COO Check)
git -C /root/cerebro-cimino log --oneline --since="8 hours ago"
- Algum agente commitou nas últimas 8h? → Registrar silenciosamente
- Agente >48h sem commit (mas deveria estar ativo)? → Avisar Lucas
```

**Economia de modelos:**
| Heartbeat | Modelo | Custo |
|-----------|--------|-------|
| Checagem (4h) | Haiku | $0.005 |
| Consolidação (seg) | Sonnet | $0.01 |
| Total/dia | — | ~$0.03 |
| Total/mês | — | ~$1 |

**Horários de silêncio:**
| Horário | Por quê | Exceção |
|---------|---------|---------|
| 06:00–08:00 | Filhos (manhã) | Nenhuma |
| 18:30–20:00 | Filhos (noite) | Nenhuma |
| 22:00–07:00 | Dorme | Só erro crítico |

**Semanal (segunda 09h):**
- Extrair lições da semana → `memory/context/lessons.md`
- Atualizar decisões → `memory/context/decisions.md`
- Deletar sessions antigos (>14 dias)

### Hermes — Heartbeat Mínimo

Hermes **não possui HEARTBEAT.md documentado**. O sistema de heartbeat existe (`cron/` module), mas:
- Não há checklist proativo definido
- Não há schedule de heartbeats com modelo econômico
- Não há horários de silêncio configurados
- Não há verificação de anomalias de negócio
- Não há visibilidade de "agentes" (é single-agent)

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| HEARTBEAT.md dedicado | Sim (Claw + cada agente) | **Não existe** |
| Frequência | 5x/dia (4h interval) | Não configurado |
| Checks de negócio | 4 categorias completas | Nenhum |
| Checks de visibilidade (git) | Sim (COO monitora outros) | Não |
| Modelo econômico (Haiku/Sonnet) | Sim (~$1/mês) | Não |
| Horários de silêncio | Sim (3 janelas) | Não |
| Consolidação semanal | Sim (segunda 09h) | Não |

---

## 6. Protocolos Operacionais

### CWC — Protocolos Explícitos Documentados

| # | Protocolo | Descrição | Arquivo |
|---|-----------|-----------|---------|
| 1 | **Anti-Amnésia** | Flush de memória 40k tokens → 5 categorias | AGENTS.md |
| 2 | **Visibilidade (Git)** | Git commit após sessão relevante | AGENTS.md |
| 3 | **Post-Mortem/Lições** | Extrair lições ANTES da compactação | AGENTS.md |
| 4 | **Heartbeat** | Checks proativos 5x/dia | HEARTBEAT.md |
| 5 | **Skill Suggestion** | Sugerir skill antes de executar tarefa repetível | SOUL.md + AGENTS.md |
| 6 | **Split de Modelos** | Haiku (heartbeat) / Sonnet (cron) / Opus (direto) | AGENTS.md |
| 7 | **Níveis de Autonomia** | L1 (Observer) → L2 (Executor) → L3 (Autonomous) | AGENTS.md |
| 8 | **Mission Control** | Integration inventory sync (6h), status validator (2h) | SOUL.md |
| 9 | **Integração Validada** | Registrar em Doppler + Supabase + .env + memory | AGENTS.md |
| 10 | **Padrão de Credenciais** | Só Doppler, nunca hardcode | AGENTS.md + TOOLS.md |
| 11 | **Anti-Padrões Críticos** | 10 regras invioláveis (Lucas Okamoto) | AGENTS.md |
| 12 | **Exec Sync** | Cron worker: isolated + agentTurn (não systemEvent) | AGENTS.md |
| 13 | **Webhook Async** | Responde 2xx imediato + thread separada | lessons.md |
| 14 | **Deduplicação** | TTL 24h, chave {lote_id}:{lance_atual} | lessons.md |

### Protocolos em Hermes

| # | Protocolo | Status |
|---|-----------|--------|
| 1 | **Anti-Amnésia** | ❌ Não existe |
| 2 | **Visibilidade (Git)** | ❌ Não existe |
| 3 | **Post-Mortem/Lições** | ⚠️ Parcial (lessons.md existe, mas sem processo) |
| 4 | **Heartbeat** | ❌ Não existe |
| 5 | **Skill Suggestion** | ❌ Não existe |
| 6 | **Split de Modelos** | ❌ Não existe |
| 7 | **Níveis de Autonomia** | ❌ Não existe |
| 8 | **Mission Control** | ❌ Não existe |
| 9 | **Integração Validada** | ❌ Não existe |
| 10 | **Padrão de Credenciais** | ⚠️ Parcial (usa Doppler concept) |
| 11 | **Anti-Padrões Críticos** | ❌ Não existe |
| 12 | **Exec Sync** | ❌ Não existe |
| 13 | **Webhook Async** | ❌ Não existe |
| 14 | **Deduplicação** | ❌ Não existe |

---

## 7. TOOLS.md Comparison

### CWC — TOOLS.md Completo (~414 linhas)

Seções:
1. **Armazenamento de Credenciais** — Doppler como fonte central
2. **INTEGRADAS & ATIVAS** (8 ferramentas):
   - Google Analytics (GA4) — Property: lksneakers.com.br + zippergaleria.com
   - Microsoft Clarity — Session recordings, heatmaps
   - Shopify — Store: lksneakers.com.br, API scopes, cron
   - Supabase — 3 projetos (LK, Zipper Vendas, SPITI)
   - Evolution API — Instâncias: SPITI, Pessoal, Clo
   - GitHub — Repo: lk-snkrs/lk-new-theme, SSH key configurada
   - Railway — Projetos: lc-whatsapp, zpr-cockpit, zpr-auto-like
   - Doppler — 40+ credenciais centralizadas
3. **IMPLEMENTANDO (Phase 1)**:
   - Google Calendar (OAuth2, cron daily briefing)
   - RapidAPI (Twitter trending, Instagram competitors, Reddit insights)
4. **PHASE 2**: Notion API, Klaviyo API, Zapier Integration
5. **Checklist de Implementação** — com horas estimadas
6. **Segurança & Hardening** — UFW, Cloudflare Tunnel
7. **Troubleshooting Rápido** — tabela com comandos
8. **Referências** — links para documentação oficial

### Hermes — TOOLS.md Inexistente

**O que Hermes TEM:**
- `hermes_cli/tools_config.py` — enable/disable de tools por plataforma
- `toolsets.py` — lista de toolsets (hermes_core, web, code_execution, etc.)
- `AGENTS.md` — documentação de desenvolvimento de tools

**O que Hermes NÃO TEM:**
- ❌ Nenhum documento TOOLS.md operacional
- ❌ Nenhuma documentação de integrações de negócio
- ❌ Nenhuma lista de credenciais (Doppler ou outras)
- ❌ Nenhum troubleshooting para APIs de negócio (Shopify, Supabase, etc.)
- ❌ Nenhum mapa de bancos de dados
- ❌ Nenhum checklist de implementação

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| TOOLS.md existe | ✅ ~414 linhas | ❌ Não existe |
| Integrações documentadas | 15+ (ativas + Phase 1 + Phase 2) | 0 |
| Credenciais mapeadas | Doppler completo (~40) | Nenhuma |
| Bancos de dados | 3 Supabase detalhados | Nenhum |
| Troubleshooting | Tabela completa | Nenhum |
| Phase planning | Phase 1 + Phase 2 | Nenhum |

---

## 8. Git as Accountability

### CWC — Git como Espinha Dorsal de Visibilidade

**Fluxo completo:**

```
1. Agente executa tarefa relevante
2. git add + git commit no cerebro-cimino
3. git push (automático ou manual)
4. COO (Claw) monitora: git log --oneline --since="8 hours ago"
5. Se agente >48h sem commit → alerta Lucas
```

**Regras de commit (CWC):**
- Sempre commit + push após mudanças
- Branch padrão: `dev` (não `main`)
- Padrão de mensagem: `🎨 {tipo}: {descrição} ({data})`
- Exemplos: `chore(lk): resumo da sessão`, `feat(zipper): atualização`

**Visibilidade do COO:**
```bash
git -C /root/cerebro-cimino log --oneline --since="8 hours ago" --format="%h %an %s"
```
- Algum agente commitou nas últimas 8h? → Registrar silenciosamente
- Agente >48h sem commit (mas deveria estar ativo)? → Avisar Lucas

### Hermes — GitExists, mas sem protocolo

Hermes está em `/root/hermes-brain/` (repositório Git), mas:
- ❌ Não há protocolo de commit pós-sessão
- ❌ Não há monitoramento de "atividade" via git log
- ❌ Não há regra de commit + push obrigatório
- ⚠️ O diretório `reports/` existe mas está vazio
- ⚠️ O diretório `data/` existe mas está vazio

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Git como visibilidade | ✅ Sistema completo | ❌ Existe repo mas sem uso |
| Commit pós-sessão | Obrigatório (protocolo) | Não documentado |
| Monitoramento de atividade | Sim (COO git log) | Não |
| Alerta por inatividade | Sim (>48h sem commit) | Não |
| Estrutura de diretórios | Completa e ativa | Parcial (reports/data vazios) |

---

## 9. Integrações

### CWC — Stack Completo de Integrações

| Integração | Status | Uso | Credencial (Doppler) |
|------------|--------|-----|----------------------|
| Shopify LK | ✅ Ativo | E-commerce, produtos, pedidos | `SHOPIFY_ACCESS_TOKEN` |
| Supabase LK | ✅ Ativo | Analytics, leads, RFM, customers | `SUPABASE_LK_SERVICE_KEY` |
| Supabase Zipper Vendas | ✅ Ativo | vendas_tango | `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY` |
| Supabase SPITI | ✅ Ativo | spiti_lotes, spiti_contacts | `SUPABASE_SPITI_SERVICE_KEY` |
| Evolution API (WhatsApp) | ✅ Ativo | 4 instâncias (Clo, SPITI, Pessoal, ZipperGaleria) | `EVOLUTION_API_KEY` |
| Google Analytics 4 | ✅ Ativo | Tráfego, conversões, comportamento | `GOOGLE_ANALYTICS_KEY` |
| Microsoft Clarity | ✅ Ativo | Session recordings, heatmaps | `CLARITY_API_KEY` |
| Klaviyo | ✅ Ativo | Email/SMS campaigns, segmentos | `KLAVIYO_API_KEY` |
| GitHub | ✅ Ativo | Versionamento, deploy automático | `GITHUB_TOKEN` |
| Railway | ✅ Ativo | Deploy de serviços backend | `RAILWAY_TOKEN` |
| Doppler | ✅ Ativo | Secrets manager central | — (CLI configurada) |
| Google Calendar | ⏳ Phase 1 | Daily briefing | `GOOGLE_CALENDAR_CREDENTIALS_JSON` |
| RapidAPI | ⏳ Phase 1 | Twitter/Instagram/Reddit trends | `RAPIDAPI_KEY` |
| Notion API | ⏳ Phase 2 | Docs como knowledge base | `NOTION_API_KEY` |
| Zapier | ⏳ Phase 2 | Workflows cross-platform | `ZAPIER_WEBHOOK_URL` |
| Attentive | ⏳ Phase 2 | SMS marketing | `ATTENTIVE_API_KEY` |
| Brave Search | ✅ Ativo | Pesquisa de mercado | `BRAVE_API_KEY` |
| KicksDB | ✅ Ativo | StockX/GOAT trends | `KICKSDB_API_KEY` |
| n8n | ✅ Ativo | Workflow automation | `N8N_API_KEY` |
| Metricool | ✅ Ativo | Agendamento Instagram | `METRICOOL_API_TOKEN` |
| Meta Ads | ⏳ Parcial | ROAS, CPM, CTR | `META_ACCESS_TOKEN` |
| GOG (Google Workspace) | ✅ Ativo | 4 contas email | `GMAIL_REFRESH_TOKEN_*` |
| Tiny ERP | ✅ Ativo | Financeiro (Júlio) | `TINY_API_TOKEN` |
| Judge.me | ✅ Ativo | Reviews | `JUDGEME_API_TOKEN` |
| Cloudflare | ✅ Ativo | DNS/CDN | — |

### Hermes — Integrações Mínimas

Hermes tem tools de **infraestrutura** (não de negócio):
- Terminal tool (local, SSH)
- File tools (read/write/search/patch)
- Web tools (search, extract, browser)
- Code execution (sandbox)
- MCP client (1050 linhas — para extensões)
- Delegate tool (subagents)
- Browser automation (Browserbase)

**Integrações de negócio:** Nenhuma documentada.

### Comparação

| Aspecto | CWC | Hermes |
|---------|-----|--------|
| Integrações de negócio | 25+ (ativas + planejadas) | 0 |
| Integrações de infraestrutura | 8+ | ~8 (file, terminal, web, etc.) |
| Secrets manager | Doppler (40+ secrets) | Nenhum |
| Mission Control | Sim (inventory + health check) | Não |
| Integrações Phase 1/2 | Sim (planejamento completo) | Não |

---

## 10. Gaps Críticos

### Gap 1: Ausência de Multi-Agent Architecture
CWC opera com 5+ agentes especializados (Claw/COO, LK, Zipper, SPITI, Marketing), cada um com escopo rigorosamente isolado e cooperando via git log. Hermes opera como **agente único**, sem especialização, sem roteamento, sem isolamento de escopo. Isso significa:
- Hermes não consegue atender LK + Zipper + SPITI simultaneamente sem mistura de contexto
- Não há "COO" monitorando outros agentes
- Não há progresso gradual de autonomia (L1 → L2 → L3)

### Gap 2: Ausência de Heartbeat Proativo
CWC tem 5 heartbeats/dia com checks de emails, agenda, anomalias de negócio, saúde de crons e visibilidade de agentes — tudo por ~$1/mês usando Haiku. Hermes **não tem heartbeat configurado**, então:
- Nunca verifica proativamente se algo está errado
- Não há alertas automáticos de anomalias
- Não há silêncio respeitoso (horários de família)
- Não há consolidação semanal de memória

### Gap 3: Ausência de Protocolos Operacionais
CWC tem 14 protocolos operacionais explícitos (Anti-Amnésia, Visibilidade Git, Post-Mortem, Split de Modelos, Níveis de Autonomia, Mission Control, etc.). Hermes tem **zero protocolos documentados**:
- Não há flush de memória
- Não há git como accountability
- Não há skill suggestion antes de tarefas repetíveis
- Não há níveis de autonomia

### Gap 4: TOOLS.md e Integrações de Negócio
CWC tem ~414 linhas de TOOLS.md detalhando 25+ integrações, bancos de dados, troubleshooting e Phase 1/2 planning. Hermes **não tem TOOLS.md** e nenhuma integração de negócio:
- Sem Supabase, Shopify, Klaviyo, Evolution API documentados
- Sem mapa de bancos de dados
- Sem Mission Control (inventory + health check)
- Sem Doppler secrets mapeados

### Gap 5: Memória Organizada e Flush Automático
CWC tem memória multi-camada (empresa/área/agente) com flush automático em 40k tokens categorizado em 5 tipos + busca híbrida BM25+Vector. Hermes tem:
- Memória plana (5 arquivos em memories/)
- Sem flush automático documentado
- Sem categorização de conteúdo
- Sem busca híbrida
- Diretórios reports/ e data/ vazios

---

## 11. Prioritized Recommendations

### Gap 1: Multi-Agent Architecture
| Atributo | Valor |
|----------|-------|
| **Esforço** | 🔴 Alto |
| **Impacto** | 🔴 Alto |

**Ação concreta:**
1. Criar `hermes-brain/agents/` com 3 especializações: `lk/`, `zipper/`, `spiti/`
2. Cada agente recebe: `SOUL.md`, `AGENTS.md`, `MEMORY.md` próprio
3. Implementar roteamento por prefixo de mensagem ou tópico
4. Agente principal (COO) monitora git log dos especializados
5. Adotar níveis de autonomia progressivos (L1 → L2 → L3)

### Gap 2: Heartbeat Proativo
| Atributo | Valor |
|----------|-------|
| **Esforço** | 🟡 Médio |
| **Impacto** | 🔴 Alto |

**Ação concreta:**
1. Criar `hermes-brain/HEARTBEAT.md` com checklist similar ao CWC
2. Configurar 3 heartbeats/dia (8h, 14h, 20h) usando cron do Hermes
3. Implementar modelo econômico: Haiku para checks rotineiros
4. Definir horários de silêncio (6-8h, 18h30-20h, 22h-7h)
5. Adicionar checks: emails, métricas LK (Supabase), status de serviços

### Gap 3: Protocolos Operacionais
| Atributo | Valor |
|----------|-------|
| **Esforço** | 🟡 Médio |
| **Impacto** | 🔴 Alto |

**Ação concreta:**
1. Implementar **Anti-Amnésia**: flush de memória ao atingir 30k tokens, categorizar em 5 tipos
2. Implementar **Git como Accountability**: `git add + commit + push` obrigatório após qualquer tarefa relevante
3. Implementar **Post-Mortem**: extrair lição aprendida antes de flush
4. Implementar **Split de Modelos**: Haiku (heartbeat) / Sonnet (execução) / Opus (análise estratégica)
5. Criar `hermes-brain/PROTOCOLS.md` documentando todos

### Gap 4: TOOLS.md e Integrações de Negócio
| Atributo | Valor |
|----------|-------|
| **Esforço** | 🟢 Baixo |
| **Impacto** | 🔴 Alto |

**Ação concreta:**
1. Criar `hermes-brain/TOOLS.md` copiando a estrutura do CWC
2. Mapear credenciais em Doppler (mesmas 40+ que CWC usa)
3. Implementar Mission Control: Integration inventory + health check
4. Documentar os 3 bancos Supabase (LK, Zipper Vendas, SPITI)
5. Criar troubleshooting para cada integração

### Gap 5: Memória Organizada e Flush
| Atributo | Valor |
|----------|-------|
| **Esforço** | 🟡 Médio |
| **Impacto** | 🟡 Médio |

**Ação concreta:**
1. Expandir estrutura de memória para `memories/lk/`, `memories/zipper/`, `memories/spiti/`
2. Implementar flush automático em `memories/flush/` categorizado
3. Criar `MEMORY_INDEX.md` como índice navegável (similar ao MEMORY.md do CWC)
4. Preencher `reports/` e `data/` com saídas reais
5. Adotar busca híbrida BM25+Vector (usar sqlite-vss ou similar)

---

## 12. Specific File Examples

### Gap 1: Multi-Agent — CWC vs Hermes

**CWC — Agente LK SOUL.md (especializado):**
```markdown
# SOUL.md — Agente LK

> Especialista em e-commerce premium de sneakers e streetwear.
> Pensa como o gerente de marketing e CRM que a LK ainda não tem.

## DNA Mental

**Hormozi (oferta):** Antes de pensar em campanha, verifico se o produto está bem posicionado.
**Eugene Schwartz (consciência de mercado):** O cliente que já comprou Onitsuka precisa de mensagem diferente.
**Virgil Abloh (linguagem de produto):** A LK não vende tênis. Vende identidade, raridade, pertencimento.

## Escopo de Acesso

**Posso acessar:**
- cerebro-cimino/areas/lk/ — tudo
- Supabase LK (cnjimxglpktznenpbail) — queries de análise e leitura
- Shopify LK, Klaviyo

**Não acesso:**
- Dados da Zipper ou SPITI
- cerebro-cimino/areas/zipper/ ou areas/spiti/
```

**Hermes — SOUL.md (genérico, único para tudo):**
```markdown
# Hermes Agent Persona

<!--
This file defines the agent's personality and tone.
The agent will embody whatever you write here.
Edit this to customize how Hermes communicates with you.

Examples:
  - "You are a warm, playful assistant who uses kaomoji occasionally."
  - "You are a concise technical expert. No fluff, just facts."
  - "You speak like a friendly coworker who happens to know everything."

This file is loaded fresh each message -- no restart needed.
Delete the contents (or this file) to use the default personality.
-->
```

### Gap 2: Heartbeat — CWC vs Hermes

**CWC — HEARTBEAT.md do Claw (completo, 244 linhas):**
```markdown
# HEARTBEAT.md — Pulso Proativo do Claw

## 🔴 Checklist (A Cada Heartbeat — 4h / 8h / 12h / 16h / 20h)
**Tempo estimado:** 2-3 min | **Custo:** ~$0.005 (Haiku)

### 1. Emails Urgentes (Gmail)
- [ ] Há cliente incomodado? (responder rápido)
- [ ] Há pagamento/transação importante?
- **Ação:** Se SIM → avisar imediatamente (respeitando silêncio)

### 2. Agenda (Google Calendar — próximas 24-48h)
- [ ] Evento hoje que Lucas não viu?
- [ ] Reunião que precisa prep?
- **Ação:** Se SIM → avisar com contexto

### 3. Anomalias de Negócio (Supabase LK)
- [ ] Vendas caíram >20% vs ontem?
- [ ] Pedido travado >6h sem processamento?
- [ ] Estoque crítico (<5 unidades)?
- **Ação:** Se SIM → avisar com % de impacto

### 4. Saúde de Automações (Crons)
- [ ] Algum cron falhou (Railway, GitHub Actions)?
- [ ] Algum cron está atrasado >30min?
- **Ação:** Se SIM → avisar + tentar debug rápido

### 5. 🧠 Visibilidade dos Agentes (COO Check)
git -C /root/cerebro-cimino log --oneline --since="8 hours ago"
- [ ] Algum agente commitou nas últimas 8h?
- [ ] Agente >48h sem commit (mas deveria estar ativo)?
```

**Hermes — HEARTBEAT.md:**
```markdown
# NÃO EXISTE
```

### Gap 4: TOOLS.md — CWC vs Hermes

**CWC — TOOLS.md (detalhado, 414 linhas):**
```markdown
# TOOLS.md — Infraestrutura e Integrações

## 🔐 Armazenamento de Credenciais
**REGRA OURO:** Todas as credenciais em Doppler (secretos manager centralizado).

## ✅ INTEGRADA & ATIVA — Shopify
**Status:** ✅ Ativo
**Store:** lksneakers.com.br (OS 2.0)
**API Key:** Doppler (SHOPIFY_ACCESS_TOKEN)
**Scopes:** read_products, read_orders, read_customers, write_inventory
**Uso:** Dados de vendas, estoque, clientes
**Cron:** Digest diário (8h15)

**Troubleshoot:**
bash
# Testar conexão Shopify
curl -X GET "https://lksneakers.myshopify.com/admin/api/2024-01/shops.json" \
  -H "X-Shopify-Access-Token: $(doppler secrets get SHOPIFY_API_TOKEN)"
```

**Hermes — TOOLS.md:**
```markdown
# NÃO EXISTE
```

### Gap 3: Protocolo Anti-Amnésia

**CWC — Flush Categories (AGENTS.md):**
```markdown
## Memória — Fase 4 (Março 2026) — CORRIGIDO

**Memory Flush Threshold:** 40.000 tokens
- Ao atingir 40k → rodar flush com 5 categorias

**Flush Categories (INVIOLÁVEL):**
1. **Decisões** → memory/context/decisions.md (O quê + Por quê + Data)
2. **Mudanças** → memory/context/decisions.md (De/Para + Impacto)
3. **Lições** → memory/context/lessons.md (🔒 estratégicas / ⏳ táticas)
4. **Bloqueios** → memory/pending.md (O que travou + Aguardando quê)
5. **Fatos-chave** → memory/projects/*.md (Status, métricas, roadmaps)

**Busca Híbrida (BM25 + Vector):**
- BM25: palavras-chave exatas (nomes, datas, termos)
- Vector: semântica (conceitos, contexto)
- Resultado: 50/50 para máxima precisão
```

**Hermes — equivalent:** NONE. No flush protocol, no categorização, no hybrid search.

### Gap 5: Estrutura de Memória

**CWC — MEMORY.md (índice completo, 96 linhas):**
```markdown
# MEMORY.md — Índice de Memória

## Onde encontrar cada coisa

### Empresa (cerebro-cimino — fonte de verdade permanente)
| O que | Onde no cerebro-cimino |
|-------|------------------------|
| Projetos ativos | empresa/gestao/projetos.md |
| Decisões estratégicas | empresa/decisoes/YYYY-MM.md |
| Lições aprendidas | empresa/gestao/licoes.md |
| Pendências | empresa/gestao/pendencias.md |
| Equipe e pessoas | empresa/contexto/people.md |
| Métricas | empresa/contexto/metricas.md |

### Áreas (cerebro-cimino)
| Área | Caminho |
|------|---------|
| LK Sneakers | areas/lk/ |
| Zipper Galeria | areas/zipper/ |
| SPITI Auction | areas/spiti/ |

**Regra inviolável:** Se importa, escreve no cerebro-cimino + git push.
```

**Hermes — memories/decisions.md (parcial, apenas 58 linhas):**
```markdown
# Decisões Permanentes — Grupo Cimino

## Infraestrutura
| Decisão | Motivo | Data |
|---------|--------|------|
| Doppler = fonte de verdade | Centralizado, rotacionável | 2026-03-17 |
| Evolution instância Clo | Separa envio de recebimento | 2026-03-24 |

## Bancos de Dados (definitivo)
| Banco | Project ID | Uso |
|-------|-----------|-----|
| LK Sneakers | cnjimxglpktznenpbail | pedidos, clientes |
| Zipper Vendas | pcstqxpdzibheuopjkas | vendas_tango |
| SPITI / Zipper CRM | rmdugdkantdydivgnimb | spiti_lotes |
```

---

## Resumo Executivo

| Dimensão | CWC (cerebro-cimino) | Hermes (hermes-brain) | Veredito |
|----------|----------------------|----------------------|----------|
| Arquitetura | Multi-agent (5+), COO, roteamento | Single-agent | **CWC +5** |
| Memória | Multi-camada, Git, flush 40k, BM25+Vector | Plano, ~5 arquivos | **CWC +5** |
| Boot | 5+ arquivos, MAPA, pendências, git | Leitura básica de memories/ | **CWC +4** |
| Skills | Por área, scripts Python, cron nativo | 3 skills flat, YAML frontmatter | **CWC +3** |
| Heartbeat | 5x/dia, 6 checks, ~$1/mês | ❌ Não existe | **CWC +5** |
| Protocolos | 14 explícitos | 0 | **CWC +5** |
| TOOLS.md | 414 linhas, 25+ integrações | ❌ Não existe | **CWC +5** |
| Git accountability | Commit + push + git log monitor | Existe repo mas não usa | **CWC +5** |
| Integrações negócio | 25+ (Shopify, Supabase, Klaviyo, etc.) | 0 | **CWC +5** |

**Conclusão:** CWC é um sistema operacional maduro com 14 protocolos, 5+ agentes, memória versionada e integrações completas. Hermes é um agente geral com memórias de contexto copiadas mas sem operacionais, protocolos ou heartbeat. A adoção dos Gap 4 (TOOLS.md) e Gap 2 (Heartbeat) seria de **esforço baixo/alto impacto** — o lugar mais eficiente para começar.

---

*Análise gerada por pesquisa detalhada em /root/cerebro-cimino/ e /root/hermes-brain/*
