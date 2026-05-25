# Organograma de Agentes — Hermes Brain

Última atualização: 2026-05-24

## Status curto

O organograma estratégico está correto: uma Grande Mente central, com Lucas pessoal e os OSs das empresas abaixo. O que faltava era explicitar a diferença entre **camadas de negócio**, **agentes documentais** e **profiles/bots reais em runtime**.

Complemento 2026-05-24: o organograma agora também explicita **orquestrador, tarefa, executor, approval boundary e handoff**. Referências canônicas: `organograma-orquestrador-tarefas-hermes.md`, `matriz-roteamento-tarefas-hermes.md` e `task-router-hermes.md`.

## Hierarquia canônica

```text
Lucas / Telegram
  ↓
Hermes Geral — profile principal `/opt/data`
  ↓
Grande Mente — Hermes Brain / Hermes COO
  ├── Lucas pessoal / Mordomo
  │   └── runtime profile: `/opt/data/profiles/mordomo`
  ├── LK OS — LK Sneakers
  │   ├── agente documental: `agentes/lk/`
  │   └── especialista ativo: LK Growth OS
  │       └── runtime profile: `/opt/data/profiles/lk-growth` / bot `@LKGrowth_HermesBot`
  ├── Zipper OS — Zipper Galeria
  │   └── agente documental: `agentes/zipper/`
  ├── SPITI OS — SPITI Auction
  │   └── agente documental: `agentes/spiti/`
  ├── Operações Hermes
  ├── Tecnologia / Infraestrutura
  └── Governança / Segurança / Aprovações
```

## Tipos de agente

### 1. Hermes Geral

- Caminho documental: `agentes/hermes-geral/`.
- Runtime: profile principal `/opt/data`.
- Papel: Chief of Staff/COO central, roteamento, Brain, decisões, Mission Control, crons, skills, integrações e guardrails.
- É a entrada padrão para Lucas no Telegram principal.
- Limite: não é executor universal; quando a matriz define especialista dono, deve rotear e cobrar handoff.

### 2. Mordomo / Lucas pessoal

- Runtime: `/opt/data/profiles/mordomo`.
- Papel: intake pessoal, follow-ups, inbox, drafts internos, agenda e roteamento pessoal/multiempresa.
- Regra: nunca envia e-mail/WhatsApp/cliente/fornecedor sozinho; prepara preview/draft interno e espera aprovação explícita no turno atual quando houver contato externo.
- Gap documental: precisa ganhar pasta documental própria em `agentes/mordomo/` ou `areas/lucas-pessoal/` se o volume continuar crescendo.

### 3. LK OS

- Caminho operacional: `areas/lk/`.
- Agente documental legado: `agentes/lk/`.
- Especialista ativo recente: LK Growth OS em `areas/lk/sub-areas/growth/`.
- Runtime Growth: `/opt/data/profiles/lk-growth` / bot `@LKGrowth_HermesBot`.
- Regra: Growth é read-only/preview por padrão; Shopify/GMC/GA4/GSC/Klaviyo/Meta writes exigem approval packet e aprovação explícita.
- Regra de roteamento: conteúdo/blog/source page/copy SEO/GEO/CRO/FAQ/schema editorial da LK pertence a `lk-growth`; Hermes Geral só orquestra, valida guardrails e entrega preview/packet.

### 4. Zipper OS

- Caminho operacional: `areas/zipper/`.
- Agente documental: `agentes/zipper/`.
- Fontes: Zipper Vendas `vendas_tango`, CRM/Main quando aplicável e textos institucionais no Brain.
- Regra: rascunhos e análises internas OK; colecionadores, artistas, propostas e comunicação externa exigem aprovação.

### 5. SPITI OS

- Caminho operacional: `areas/spiti/`.
- Agente documental: `agentes/spiti/`.
- Fonte: Spiti Hub/repo, Supabase/CRM e fontes verificadas de leilão/lances.
- Regra: silêncio é melhor que dado errado; lance/lote só com fonte verificável.

## O que é fonte de verdade

- Organograma global: `empresa/contexto/organograma-operacional-hermes-brain.md`.
- Este arquivo: mapa agente/runtime/profile.
- Orquestração por tarefa: `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`.
- Matriz executor/aprovação/handoff: `empresa/contexto/matriz-roteamento-tarefas-hermes.md`.
- Algoritmo operacional: `empresa/contexto/task-router-hermes.md`.
- Regras globais: `AGENTS.md` e `agentes/hermes-geral/AGENTS.md`.
- Regras por negócio: `areas/<empresa>/MAPA.md` + documentação em `agentes/<empresa>/`.
- Runtime real: processos `hermes gateway run`, `HERMES_HOME`, `cronjob list` e configs dos profiles.

## Gaps conhecidos

1. `agentes/lk/AGENTS.md` e `agentes/zipper/AGENTS.md` ainda têm marcas legadas de `cerebro-cimino`, `/root` e `Claw`; já possuem aviso de manutenção, mas devem ser normalizados gradualmente para linguagem Hermes-native.
2. Mordomo, LK, Zipper e SPITI agora têm pacote documental mínimo no padrão Amora/Hermes (`SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS`, `MEMORY`). O próximo gap não é criar arquivo, é manter consistência entre esses arquivos e runtime real.
3. LK Growth está bem documentado em `areas/lk/sub-areas/growth/` e referenciado nos mapas globais como especialista ativo; deve continuar sendo executor de conteúdo/SEO/GEO/CRO, não subpasta solta.
4. Zipper permanece sem runtime dedicado; tratá-lo como documental/read-only até decisão de criar profile/bot próprio.
5. O organograma deve separar sempre:
   - camada de negócio;
   - agente documental;
   - runtime profile/bot ativo;
   - cron/rotina;
   - tarefa roteável;
   - handoff/receipt.

## Regra curta

**A Grande Mente coordena. Profiles e bots são superfícies de execução. Agentes documentais explicam escopo e guardrails. Nenhum especialista vira uma mente separada.**

Complemento operacional aprovado por Lucas: todo profile/bot especialista deve reportar trabalho relevante ao Hermes Central e/ou registrar no Brain, no mínimo em fechamento diário quando não for urgente. Handoff canônico: `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`.

## Base Bruno/OpenClaw usada

A lógica vem da Aula 13 do Bruno/OpenClaw: `AGENTS.md` é o **organograma vivo** do time digital, contendo quem é cada agente, quem chama quem, onde vive, permissões cruzadas e governança. A Aula 06 complementa com `MAPA.md` distribuído por pasta; a Aula 07 complementa com a regra de memória: conversa/sessão não basta, conhecimento importante precisa virar arquivo no Brain/workspace.

Síntese aplicada ao Hermes: `areas/operacoes/base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md`.
