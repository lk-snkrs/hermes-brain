# Organograma de Orquestrador e Tarefas — Hermes COO

Data: 2026-05-24  
Status: aprovado para Fase 1 documental  
Fonte: PRD `areas/operacoes/prds/hermes-orquestrador-tarefas-organograma-prd-2026-05-24.md`

## Princípio

Hermes Geral não é executor universal. Hermes Geral é o **orquestrador central**: entende a intenção de Lucas, classifica risco/contexto, distribui a tarefa para o dono certo, cobra handoff e mantém o Brain como fonte de verdade.

```text
Lucas / Telegram
  ↓
Hermes Geral — Orquestrador Central / COO
  ↓
Task Router / Approval Gate
  ↓
Especialistas, profiles, bots, rotinas e scripts
  ↓
Hermes Brain — fonte de verdade, handoff, memória e evidência
```

Regra curta:

> Hermes Geral coordena. Especialistas executam. Brain registra. Produção/externo exige aprovação.

## Camadas

### 1. Entrada

- Lucas no Telegram principal.
- Bots especialistas quando existirem.
- Webhooks/eventos autorizados.
- Crons/rotinas documentadas.

A entrada não define o executor. O executor é definido pelo Task Router.

### 2. Orquestrador central — Hermes Geral

- Runtime: profile principal `/opt/data`.
- Documentação: `agentes/hermes-geral/`.
- Responsabilidades:
  - classificar empresa/área/contexto;
  - identificar especialista dono;
  - separar read-only/local de write externo/produção;
  - pedir aprovação quando necessário;
  - distribuir tarefa para profile/bot/rotina correta;
  - receber handoff;
  - registrar aprendizado/decisão no Brain;
  - manter visão multiempresa.

Hermes Geral pode executar diretamente tarefas centrais, documentação, auditoria local, roteamento, PRDs, consolidação e governança. Quando há especialista dono claro, ele deve rotear em vez de produzir no perfil errado.

### 3. Task Router / Approval Gate

- Documentação: `empresa/contexto/task-router-hermes.md`.
- Matriz: `empresa/contexto/matriz-roteamento-tarefas-hermes.md`.
- Responsabilidades:
  - decidir `executar aqui`, `delegar`, `preparar packet`, `bloquear`, ou `perguntar`;
  - aplicar guardrails A0-A4;
  - impedir produção acidental;
  - impedir especialistas isolados sem handoff.

### 4. Especialistas / braços executores

Especialistas não são cérebros separados. São braços de execução com escopo próprio, fontes próprias e handoff obrigatório.

```text
Especialistas ativos/documentados
├── Mordomo / Lucas pessoal
│   ├── Runtime: /opt/data/profiles/mordomo
│   ├── Escopo: intake pessoal, agenda, follow-ups permitidos, triagem WhatsApp
│   └── Handoff: decisões, contatos sensíveis, eventos, follow-ups relevantes
│
├── LK Growth OS
│   ├── Runtime: /opt/data/profiles/lk-growth
│   ├── Escopo: SEO, CRO, GEO, GMC, analytics, conteúdo/blog/source pages, approval packets
│   └── Handoff: drafts, packets, receipts, approvals, riscos, writes externos
│
├── SPITI OS
│   ├── Runtime: /opt/data/profiles/spiti
│   ├── Escopo: Hub, leilões, lotes, CRM, Financial read-only, Growth SPITI
│   └── Handoff: dados verificados, decisões, riscos, outputs, PRs/packets
│
├── Zipper OS
│   ├── Runtime dedicado: pendente/futuro
│   ├── Escopo atual: documental/read-only via Brain e fontes aprovadas
│   └── Handoff: CRM, comunicação, logística, obras, relatórios
│
└── Operações Hermes
    ├── Runtime: Hermes Geral + scripts/crons aprovados
    ├── Escopo: Brain hygiene, watchdogs, skills, rotinas, gateway/cron observability
    └── Handoff: governança, receipts, falhas, alterações documentais
```

### 5. Brain / fonte de verdade

- Repositório local: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Função:
  - guardar contexto durável;
  - mapear agentes e rotas;
  - manter decisões e guardrails;
  - receber outputs e handoffs;
  - transformar repetição em skill/rotina.

O Brain não substitui fonte viva. Para métricas, status, preço, estoque, lance, deploy, campanha ou pedido, consultar API/banco/fonte real antes de afirmar.

## Organograma operacional v1

```text
Hermes COO / Grande Mente
├── Hermes Geral — Orquestrador Central
│   ├── Roteamento multiempresa
│   ├── Approval gates
│   ├── Brain governance
│   ├── Mission Control / decisões
│   ├── PRDs e planos centrais
│   └── Handoff consolidado
│
├── Lucas pessoal / Mordomo
│   ├── Runtime: /opt/data/profiles/mordomo
│   ├── Tarefas: intake pessoal, agenda, follow-ups permitidos
│   ├── Fonte: WhatsApp pessoal, calendário, Brain, regras do Mordomo
│   └── Bloqueios: preço, disponibilidade, reserva, negociação, reclamação, bulk/campanha sem fonte/aprovação
│
├── LK OS — LK Sneakers
│   ├── LK Chief of Staff — planejado/futuro
│   ├── LK Growth OS
│   │   ├── Runtime: /opt/data/profiles/lk-growth
│   │   ├── Tarefas: SEO, CRO, GEO, GMC, analytics, blog/source pages, packets
│   │   └── Bloqueios: Shopify/GMC/Klaviyo/Meta/theme/produção sem aprovação
│   └── LK Operações/Atendimento — documental/rotinas
│
├── Zipper OS — Zipper Galeria
│   ├── Zipper Chief of Staff — planejado/futuro
│   ├── Comunicação/CRM/obras — documental/read-only
│   └── Bloqueios: cliente, artista, proposta, preço, disponibilidade e logística externa sem aprovação/fonte
│
├── SPITI OS — SPITI Auction
│   ├── Runtime: /opt/data/profiles/spiti
│   ├── Tarefas: Hub, leilões, lotes, CRM, descrições/IA, Growth SPITI, Financial read-only
│   └── Bloqueios: lance/lote sem fonte, deploy, banco/write, cliente/bidder sem aprovação
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

## Diferença entre camadas

| Camada | O que é | Exemplo |
|---|---|---|
| Negócio | Área ou empresa atendida | LK, Zipper, SPITI |
| Agente documental | Pasta com identidade, escopo e regras | `agentes/hermes-geral/` |
| Runtime profile/bot | Processo real do Hermes com HOME próprio | `/opt/data/profiles/lk-growth` |
| Rotina/cron | Execução recorrente documentada ou agendada | GMC Review, fechamento 23h |
| Tarefa | Unidade de trabalho roteável | “criar source page 530” |
| Handoff | Registro do que especialista fez | template em `templates/handoff-especialista.md` |

## Regra anti-erro

Se a tarefa for de conteúdo/blog/source page/SEO/GEO/CRO copy da LK:

1. Hermes Geral classifica como `LK Growth`.
2. Hermes Geral distribui para `/opt/data/profiles/lk-growth` ou registra `executor_pendente=lk-growth`.
3. Hermes Geral não escreve o conteúdo final por conveniência.
4. Output vai para `areas/lk/sub-areas/growth/`.
5. Publicação/Shopify/theme/Klaviyo/GMC/Meta exige approval packet e aprovação explícita.

## Relação com Amora/Bruno

Amora serve como referência de maturidade:

- `AGENTS.md` como contrato operacional e red lines;
- `MAPA.md` como navegação viva;
- memória escrita em arquivo, não “mental note”;
- proatividade com silêncio quando nada importa.

Adaptação Hermes:

- não copiar múltiplos crons/ações externas da Amora;
- preservar approval gates de Lucas;
- separar LK/Zipper/SPITI;
- usar profiles/bots como braços, não como cérebros separados;
- registrar handoff no Brain.

## Verificação antes de chamar algo de operacional

- Existe escopo documental?
- Existe runtime/profile real quando necessário?
- Existe fonte de verdade definida?
- Existe output path?
- Existe approval boundary?
- Existe handoff obrigatório?
- Existe rollback/receipt quando há write externo?
- Existe reconciliação com o Hermes Central?
