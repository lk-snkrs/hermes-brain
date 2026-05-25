# PRD — Organograma de Orquestrador e Tarefas do Hermes

Data: 2026-05-24  
Status: draft para aprovação  
Dono: Hermes Geral / Lucas Cimino  
Escopo: Hermes Brain + runtime profiles + roteamento de tarefas  
Inspiração: Bruno/OpenClaw/Amora, adaptado para Hermes-native

## 1. Problema

O Hermes já possui uma Grande Mente central e alguns profiles/bots especialistas, mas ainda falta um **organograma operacional de orquestração e tarefas** que responda de forma prática:

1. Quem é o orquestrador de cada tipo de tarefa?
2. Qual especialista/profile deve executar?
3. O que o Hermes principal pode fazer sozinho?
4. Quando deve apenas rotear/distribuir?
5. Onde cada output deve ser salvo?
6. Qual handoff volta para o Brain/Hermes Central?
7. Quais ações exigem aprovação explícita de Lucas?

A falha mais recente expôs o problema: o Hermes Geral produziu conteúdo de LK Growth diretamente, quando a tarefa deveria ter sido distribuída ao especialista `lk-growth`.

## 2. Decisão de produto

Criar uma camada formal chamada:

**Organograma de Orquestração e Tarefas — Hermes COO**

Ela não substitui o Brain existente. Ela fica por cima dos documentos atuais e conecta quatro camadas:

```text
Lucas / Telegram
  ↓
Hermes Geral — Orquestrador Central
  ↓
Roteador de Tarefas / Approval Gate
  ↓
Especialistas / Profiles / Bots / Rotinas
  ↓
Hermes Brain — Fonte de verdade, handoff, memória e evidência
```

Regra principal:

> Hermes Geral coordena, decide rota e cobra handoff. Especialistas executam no próprio domínio. O Brain registra a verdade durável.

## 3. Referências usadas

### Internas Hermes Brain

- `START-HERE.md`
- `MAPA.md`
- `AGENTS.md`
- `empresa/contexto/organograma-operacional-hermes-brain.md`
- `empresa/contexto/organograma-agentes-hermes.md`
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `areas/operacoes/base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md`

### Bruno/OpenClaw/Amora

- Amora como referência madura, não cópia literal.
- `LEIA-PRIMEIRO-amora.md`: usar como referência de profundidade, adaptando ao contexto.
- `AGENTS-amora.md`: boot sequence, regras de sessão, memória, red lines, external/internal resolver e heartbeats.
- `MAPA-amora.md`: navegação por arquivos raiz, pastas principais, sub-MAPAs e evolução progressiva.

### Princípio Bruno/OpenClaw já aprovado

> O agente não é o cérebro. O agente lê e escreve o cérebro.

Versão Hermes:

> O profile/bot não é uma mente separada. Ele é um braço executor da Grande Mente, com handoff obrigatório.

## 4. Objetivos

### Objetivo 1 — Organograma vivo

Criar um documento canônico que mostre:

- Hermes Geral / Orquestrador Central.
- Especialistas ativos por profile/bot.
- Agentes documentais por área.
- Rotinas/crons por domínio.
- Fontes de verdade por tarefa.
- Approval boundaries por classe de ação.

### Objetivo 2 — Matriz de roteamento de tarefas

Criar uma matriz onde cada tipo de trabalho tenha um dono claro.

Exemplo:

```text
Tarefa: conteúdo/blog/source page LK
Orquestrador: Hermes Geral
Executor: LK Growth profile
Fonte: areas/lk/sub-areas/growth + dados públicos/read-only
Output: draft/packet em growth/drafts ou growth/reports
Aprovação: Lucas antes de Shopify/theme/publicação
Handoff: resumo para Hermes Central/Brain
```

### Objetivo 3 — Handoff obrigatório

Todo especialista que produz output relevante deve registrar:

- o que fez;
- fonte consultada;
- arquivo/output gerado;
- risco;
- aprovação pendente;
- próximos passos;
- se houve ou não ação externa.

### Objetivo 4 — UX operacional no Telegram

Quando Lucas pedir algo, o Hermes deve responder no padrão:

```text
Entendi. Isso é tarefa de [especialista].
Vou rotear para [profile/bot] e volto com o output/preview.
Sem write externo/produção até aprovação.
```

Não deve fazer a tarefa no perfil errado “por conveniência”.

## 5. Não objetivos

- Não criar múltiplos cérebros isolados.
- Não criar crons novos automaticamente.
- Não alterar Docker/gateway/profile runtime sem aprovação.
- Não migrar arquivos em massa ainda.
- Não publicar conteúdo em Shopify/blog/tema.
- Não transformar a estrutura em burocracia estética.

## 6. Arquitetura proposta

## 6.1 Camadas

```text
1. Entrada
   Lucas / Telegram / bots especialistas / webhooks

2. Orquestração
   Hermes Geral — profile principal `/opt/data`
   Responsável por entender intenção, risco, empresa, especialista e aprovação.

3. Roteamento
   Task Router — matriz documental + skill/memory/runtime checks
   Decide: executar aqui, delegar, abrir approval packet, ou bloquear.

4. Execução especialista
   - Mordomo — `/opt/data/profiles/mordomo`
   - LK Growth — `/opt/data/profiles/lk-growth`
   - SPITI — `/opt/data/profiles/spiti`
   - futuros: Zipper, LK Chief of Staff, etc.

5. Registro
   Hermes Brain — outputs, handoffs, decisões, skills, rotinas.

6. Supervisão
   Fechamento diário / daily reconciliation / watchdogs silent-OK.
```

## 6.2 Organograma inicial

```text
Hermes COO / Grande Mente
├── Hermes Geral — Orquestrador Central
│   ├── Roteamento multiempresa
│   ├── Approval gates
│   ├── Brain governance
│   ├── Mission Control / decisões
│   └── Handoff consolidado
│
├── Lucas Pessoal / Mordomo
│   ├── Runtime: /opt/data/profiles/mordomo
│   ├── Tarefas: intake pessoal, agenda, follow-ups permitidos
│   └── Bloqueios: preço, disponibilidade, negociação, reclamação, bulk/campanha sem fonte/aprovação
│
├── LK OS
│   ├── LK Chief of Staff — futuro/planejado
│   ├── LK Growth OS
│   │   ├── Runtime: /opt/data/profiles/lk-growth
│   │   ├── Tarefas: SEO, CRO, GEO, GMC, conteúdo/blog/source pages, analytics, packets
│   │   └── Bloqueios: Shopify/GMC/Klaviyo/Meta writes sem aprovação
│   └── LK Operações/Atendimento — documental/rotinas
│
├── Zipper OS
│   ├── Zipper Chief of Staff — futuro/planejado
│   ├── Comunicação/CRM/obras — documental/read-only
│   └── Bloqueios: cliente, artista, proposta, logística externa sem aprovação/fonte
│
├── SPITI OS
│   ├── Runtime: /opt/data/profiles/spiti
│   ├── Tarefas: Hub, leilões, lotes, CRM, Growth SPITI, Financial read-only
│   └── Bloqueios: lance/lote sem fonte, deploy, cliente, banco/write sem aprovação
│
├── Operações Hermes
│   ├── Crons/watchdogs
│   ├── Brain hygiene
│   ├── Skills/rotinas
│   └── Silent-OK supervision
│
└── Governança / Segurança
    ├── Aprovações A0-A4
    ├── Secrets/Doppler
    ├── Produção/Docker/VPS
    └── Rollback/evidência
```

## 7. Matriz de roteamento v1

## 7.1 Classes de tarefa

### A. Roteamento e decisão central

- Executor: Hermes Geral.
- Exemplos: “o que faço agora?”, “prioriza meu dia”, “qual especialista chama?”, “Mesa COO”.
- Output: decisão curta, botões/approval, handoff.

### B. Conteúdo/Growth LK

- Executor: LK Growth.
- Exemplos: blog, source page, SEO title/meta, GEO blocks, FAQ, schema, CRO copy, approval packets.
- Hermes Geral: apenas roteia, valida guardrails e entrega o artefato.
- Output: `areas/lk/sub-areas/growth/drafts/` ou `reports/`.
- Aprovação exigida: qualquer publicação, Shopify/page/theme/Klaviyo/GMC/Meta write.

### C. Operação pessoal / inbox / agenda

- Executor: Mordomo.
- Exemplos: follow-up pessoal, calendário, leitura/triagem WhatsApp pessoal conforme guardrails.
- Hermes Geral: recebe exceções/decisões.
- Aprovação exigida: contato externo sensível, preço, negociação, campanha, reclamação.

### D. Zipper

- Executor: Zipper OS/documental; futuro profile Zipper quando existir.
- Exemplos: obra, artista, colecionador, CRM, logística, relatório vendas.
- Aprovação exigida: contato externo, proposta, preço, disponibilidade, logística com cliente/artista.

### E. SPITI

- Executor: SPITI profile.
- Exemplos: Hub, lotes, lances, CRM, análise visual/descrição de obras, growth SPITI.
- Aprovação exigida: site/deploy, banco/write, cliente/bidder, afirmação de lance/lote sem fonte verificada.

### F. Infra/Hermes

- Executor: Hermes Geral, com plano/rollback antes de mudanças.
- Exemplos: cron, gateway, Docker, VPS, skills, plugins.
- Aprovação exigida: Docker/Traefik/volumes/root/SSH/portas/gateway restart arriscado.

## 8. Regras de decisão do Task Router

## 8.1 Algoritmo

Para cada pedido de Lucas:

1. Classificar contexto: Lucas pessoal, LK, LK Growth, Zipper, SPITI, Operações, Tecnologia, Governança ou multiempresa.
2. Classificar tipo: pergunta, análise, conteúdo, rotina, write externo, produção, destrutivo, cron, cliente.
3. Consultar matriz de roteamento.
4. Decidir ação:
   - executar no Hermes Geral;
   - delegar ao especialista/profile;
   - criar approval packet;
   - bloquear e pedir aprovação;
   - pedir clarificação só se rota mudar materialmente.
5. Registrar output no Brain quando relevante.
6. Gerar handoff se especialista executou.
7. Responder a Lucas com status curto e link/arquivo/preview.

## 8.2 Regra anti-erro recente

Se a tarefa for `conteúdo/blog/source page/copy SEO/GEO` de LK:

- Hermes Geral **não escreve o conteúdo final**.
- Hermes Geral chama `lk-growth`.
- Se `lk-growth` estiver indisponível, Hermes Geral pode preparar apenas briefing/roteiro/requirements, marcando `executor_pendente=lk-growth`.

## 9. Artefatos a criar/alterar

### 9.1 Novos arquivos

1. `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
   - Organograma visual/textual canônico.

2. `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
   - Tabela por tarefa → orquestrador → executor → output → aprovação → handoff.

3. `empresa/contexto/task-router-hermes.md`
   - Algoritmo operacional e exemplos.

4. `templates/handoff-especialista.md`
   - Template curto para especialistas.

5. `areas/operacoes/rotinas/task-router-handoff-especialistas.md`
   - Rotina documental: como distribuir, cobrar e consolidar.

### 9.2 Arquivos a atualizar

1. `START-HERE.md`
   - Adicionar regra de roteamento por especialista antes de executar.

2. `MAPA.md`
   - Linkar organograma de orquestração e matriz de tarefas.

3. `AGENTS.md`
   - Adicionar: “se houver especialista dono, rotear; não executar no perfil errado”.

4. `empresa/contexto/organograma-agentes-hermes.md`
   - Expandir com dimensão de tarefas e handoff.

5. `agentes/hermes-geral/AGENTS.md`
   - Colocar Hermes Geral como orquestrador, não executor universal.

6. Skill `multiempresa-routing-lucas`
   - Adicionar referência à matriz.

7. Skill `lk-seo-weekly-improvement`
   - Já recebeu correção inicial: conteúdo/blog/source page LK deve ir para LK Growth.

## 10. Modelo de dados mínimo

Cada rota da matriz deve ter campos:

```yaml
id: lk-growth-content
contexto: LK Sneakers / Growth
triggers:
  - blog
  - source page
  - SEO copy
  - GEO blocks
  - FAQ/schema editorial
orquestrador: Hermes Geral
executor: lk-growth
runtime_profile: /opt/data/profiles/lk-growth
brain_path: areas/lk/sub-areas/growth/
allowed_without_approval:
  - pesquisa read-only
  - briefing
  - draft local
  - approval packet
requires_approval:
  - Shopify write
  - theme upload
  - publicação
  - Klaviyo/send
  - GMC/feed write
handoff_required: true
```

## 11. UX esperada

## 11.1 Quando roteia

Resposta ideal:

```text
Entendi. Isso é LK Growth, não Hermes Geral.
Vou distribuir para o profile LK Growth e volto com o draft/preview.
Nada será publicado ou escrito em Shopify.
```

## 11.2 Quando volta com output

```text
LK Growth entregou.
Arquivo: [path/link]
Status: draft local, sem publicação.
Principais mudanças: [...]
Próxima decisão: aprovar preview dev/local ou pedir revisão.
```

## 11.3 Quando bloqueia

```text
Isso exigiria write externo/produção.
Posso preparar o packet, mas para executar preciso de aprovação explícita com escopo.
```

## 12. Fases de implementação

## Fase 0 — PRD e aprovação

- Criar este PRD.
- Lucas aprova direção: organograma de orquestrador + matriz de tarefas.
- Nenhuma alteração runtime.

## Fase 1 — Documentação canônica

Criar os cinco artefatos novos:

- organograma;
- matriz;
- task router;
- template de handoff;
- rotina de handoff.

Verificação:

- Todos linkados no `MAPA.md`.
- Nenhuma referência a comandos OpenClaw como executáveis.
- Nenhuma duplicação de “cérebro”.

## Fase 2 — Atualizar regras do Hermes Geral

Atualizar:

- `AGENTS.md` global;
- `agentes/hermes-geral/AGENTS.md`;
- `START-HERE.md`;
- skills relevantes.

Verificação:

- Pedido de conteúdo LK routeia para `lk-growth`.
- Pedido de Mordomo routeia para `mordomo`.
- Pedido SPITI routeia para `spiti`.
- Zipper permanece documental/read-only até profile dedicado existir.

## Fase 3 — Inventário de runtime

Read-only:

- listar profiles existentes;
- listar crons por profile;
- listar bots/canais conhecidos;
- comparar com organograma documental.

Output:

- `reports/governance/runtime-vs-organograma-YYYY-MM-DD.md`

Sem restart, sem Docker, sem mutação.

## Fase 4 — Task Router operacional

Implementar como rotina/skill, não como runtime novo inicialmente:

- checklist carregável;
- exemplos de rotas;
- regras de bloqueio;
- handoff.

Depois avaliar se precisa virar tool/plugin/Mission Control surface.

## Fase 5 — Mission Control / UI futura

Opcional depois:

- tela “Orquestrador”;
- cards por tarefa;
- dono/executor/status/aprovação;
- histórico de handoffs;
- botão “distribuir para especialista”.

## 13. Critérios de aceite

1. Dado um pedido de Lucas, o Hermes consegue dizer qual especialista é dono.
2. Conteúdo LK é roteado para `lk-growth`, não produzido pelo Hermes Geral.
3. Cada profile/bot tem escopo, output path e aprovação clara.
4. Handoff obrigatório está documentado e curto o bastante para ser usado.
5. O Brain continua sendo uma Grande Mente única.
6. Nenhum write externo é autorizado por “seguir”, `/background` ou botão genérico.
7. O organograma diferencia:
   - camada de negócio;
   - agente documental;
   - runtime profile/bot;
   - rotina/cron;
   - tarefa.
8. A implementação é auditável por arquivos e não depende de memória de chat.

## 14. Riscos

### Risco 1 — Burocracia demais

Mitigação: começar com matriz pequena v1, crescer só por erro/repetição real.

### Risco 2 — Especialistas virarem cérebros isolados

Mitigação: handoff obrigatório e Brain Central como fonte final.

### Risco 3 — Roteamento bloquear execução simples

Mitigação: Hermes Geral continua executando tarefas centrais/read-only de baixa complexidade; só roteia quando há dono claro.

### Risco 4 — Runtime divergente da documentação

Mitigação: inventário read-only e reconciliation periódico.

### Risco 5 — Produção acidental

Mitigação: Approval Gate explícito por rota e lista de ações bloqueadas.

## 15. Próxima decisão para Lucas

Decisão 1/3: Aprovar a criação da camada documental de organograma + matriz de tarefas.

Se aprovado, executar Fase 1:

- criar `organograma-orquestrador-tarefas-hermes.md`;
- criar `matriz-roteamento-tarefas-hermes.md`;
- criar `task-router-hermes.md`;
- criar template de handoff;
- atualizar links no `MAPA.md`.

Sem mudar runtime, sem cron novo, sem Docker, sem publicação externa.
