# Inventário vivo — crons, agentes, profiles e projetos

Data-base: 2026-05-19
Status: **Fase 1A aprovada por Lucas — inventário inicial + teste manual do Fechamento 23h**
Escopo: Hermes Brain / Grande Mente / profiles especialistas / crons Hermes.

## 1. Princípio

Este inventário existe para garantir que o **Fechamento Ágil 23h** não consolide apenas “agentes” em abstrato. Ele deve cobrir também:

- profiles/bots reais em runtime;
- canais de conversa;
- crons e watchdogs script-only;
- projetos/rotinas associados;
- destino do handoff no Brain;
- gaps de documentação ou cobertura.

Regra curta:

> Especialista executa. Grande Mente consolida. Conversa relevante vira decisão, pendência, receipt, handoff, rotina, skill, PRD/BRD ou relatório no Brain.

## 2. Critério de entrada no Fechamento 23h

Uma conversa, cron ou entrega entra no fechamento se gerar pelo menos um destes sinais:

- decisão de Lucas ou responsável autorizado;
- pendência ou follow-up;
- aprovação;
- bloqueio/risco;
- entrega/relatório/receipt;
- write externo aprovado;
- correção de Lucas;
- aprendizado durável;
- mudança em projeto/rotina;
- exceção/falha operacional.

O fechamento **não** deve virar transcrição de chat.

## 3. Cobertura por agente/profile/bot

### 3.1 Hermes Geral / Grande Mente

- Status: **ativo**.
- Runtime/profile: `/opt/data`.
- Superfície: Telegram principal de Lucas + API/gateway principal.
- Caminho documental: `agentes/hermes-geral/`, `empresa/`, `areas/operacoes/`, `MAPA.md`.
- Projetos/rotinas associados:
  - Hermes Brain;
  - Mission Control;
  - Mesa COO;
  - Fechamento Ágil 23h;
  - governança multiempresa;
  - skills/memória/crons;
  - health checks.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `reports/daily-consolidation/YYYY-MM-DD.md`, `empresa/gestao/pendencias.md`, `memories/`, rotinas/projetos correspondentes.
- Gap: nenhum bloqueante; deve ser a camada coordenadora.

### 3.2 Lucas pessoal / Mordomo

- Status: **ativo/parcialmente pausado conforme crons**.
- Runtime/profile conhecido: `/opt/data/profiles/mordomo`.
- Superfície: Telegram/bot Mordomo e WhatsApp pessoal via ferramentas locais quando habilitadas.
- Caminho documental atual: `areas/operacoes/` e docs de Mordomo; gap conhecido para pasta documental dedicada `agentes/mordomo/` ou `areas/lucas-pessoal/` se volume crescer.
- Projetos/rotinas associados:
  - intake pessoal;
  - follow-ups;
  - agenda/calendário;
  - WhatsApp pessoal;
  - CRM local/Mordomo;
  - drafts/previews internos.
- Crons relacionados:
  - `Mordomo Telegram gateway watchdog` — ativo, `origin`, script-only.
  - `Mordomo WhatsApp pessoal resumo 17h BRT` — pausado.
  - `Mordomo WhatsApp pessoal realtime scan` — pausado, local.
  - `Mordomo: confirmar entrega com Seda Embalagens` — pausado/one-shot antigo.
- Entra no Fechamento 23h: **sim, quando houver conversa com decisão, follow-up, risco ou entrega**.
- Destino de handoff: `areas/operacoes/calendar-intake/`, `areas/operacoes/decision-inbox/`, `empresa/gestao/pendencias.md`, relatório diário.
- Gap: separar melhor Lucas pessoal/Mordomo da área Operações no Brain.

### 3.3 LK OS — LK Sneakers

- Status: **ativo**.
- Runtime/profile: Hermes Geral + scripts/crons; especialista LK Growth separado.
- Superfícies:
  - Telegram principal para decisões/exceções;
  - WhatsApp grupo LK Vendas para relatórios aprovados;
  - email `lk@...` para companions aprovados;
  - Mission Control;
  - crons LK.
- Caminho documental: `areas/lk/`, `agentes/lk/`, rotinas LK, reports LK.
- Projetos/rotinas associados:
  - Daily Sales Brief;
  - Weekly CEO Review;
  - GMC/SEO/CRO/GEO;
  - Pulso 16h;
  - relatório 09h dia anterior;
  - fechamento loja física 19h30;
  - CRM/Klaviyo;
  - stock/sourcing;
  - paid/influencer intelligence.
- Crons relacionados:
  - `LK Daily Sales Brief read-only mandatory delivery` — ativo, `origin`.
  - `LK Weekly CEO Review read-only mandatory delivery` — ativo, `origin`.
  - `LK GMC Review read-only mandatory delivery` — pausado.
  - `LK Pulso Comercial 16h read-only delivery` — ativo, `local`.
  - `LK 09h previous-day sales report external delivery` — ativo, `origin`.
  - `LK 19h30 physical store close external delivery` — ativo, `local` após correção de Lucas para não enviar recibo/HTML de sucesso no Telegram.
  - `LK weekly influencer sales email` — pausado.
  - `LK SEO/CRO weekly Claude SEO improvement loop` — pausado.
  - `LK SEO/CRO impact review — SEO title/meta P1 packets` — pausado.
  - `LK WhatsApp Hermes responder watchdog` — ativo, `local`.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `areas/lk/`, `reports/`, `empresa/gestao/pendencias.md`, relatório diário.
- Gap: classificar quais crons LK devem ficar `local` por sucesso normal vs `origin` para decisões/exceções.

### 3.4 LK Growth OS

- Status: **ativo**.
- Runtime/profile conhecido: `/opt/data/profiles/lk-growth`.
- Bot conhecido: `@LKGrowth_HermesBot`.
- Caminho documental: `areas/lk/sub-areas/growth/` e referências nos mapas globais.
- Projetos/rotinas associados:
  - SEO/CRO/GEO;
  - conteúdo/newsletter;
  - Renan/Growth;
  - Klaviyo dentro do escopo de conteúdo;
  - impacto de mudanças SEO.
- Crons relacionados:
  - `LK Growth Telegram gateway watchdog` — ativo, `origin`.
  - rotinas SEO/CRO pausadas no Hermes Geral, a revisar se devem migrar/rodar no profile Growth.
- Entra no Fechamento 23h: **sim, se houver output, aprovação, campanha, conteúdo, decisão ou gap de handoff**.
- Destino de handoff: `areas/lk/sub-areas/growth/`, `areas/lk/`, relatório diário.
- Gap: link global ainda precisa ficar mais explícito para não parecer agente solto.

### 3.5 Zipper OS — Zipper Galeria

- Status: **ativo**.
- Runtime/profile: ainda não mapeado como profile próprio no inventário atual; operações rodam via Hermes Geral/scripts.
- Superfícies:
  - Zipper Vendas / reports;
  - Gmail/style learning;
  - WhatsApp Zipper quando aprovado;
  - Brain Zipper.
- Caminho documental: `areas/zipper/`, `agentes/zipper/`.
- Projetos/rotinas associados:
  - vendas de obras;
  - colecionadores;
  - artistas;
  - feiras;
  - comunicação;
  - logística de obras;
  - style learning.
- Crons relacionados:
  - `Zipper OS vendas 09h WhatsApp/email` — ativo, `origin`.
  - `Zipper Gmail style learning refresh` — ativo, `local`.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `areas/zipper/`, relatório diário, pendências globais se houver risco/decisão.
- Gap: confirmar se haverá profile/bot Zipper dedicado ou se continua via Hermes Geral + rotinas.

### 3.6 SPITI OS — SPITI Auction

- Status: **ativo**.
- Runtime/profile conhecido por memória operacional: `/opt/data/profiles/spiti`.
- Bot conhecido: `@SPITI_HermesBot`.
- Caminho documental: `areas/spiti/`, `agentes/spiti/`.
- Projetos/rotinas associados:
  - SPITI Hub;
  - SPITI Financial;
  - Supabase/CRM;
  - leilões/lances;
  - conteúdo/growth;
  - IA de obras;
  - public site futuro.
- Crons relacionados:
  - `SPITI Telegram gateway watchdog` — ativo, `origin`.
- Entra no Fechamento 23h: **sim, quando houver atividade/decisão/output/gap**.
- Destino de handoff: `areas/spiti/`, relatório diário, pendências globais se houver risco/decisão.
- Gap: organograma documental deve explicitar melhor o runtime/profile SPITI, não apenas o agente documental.

### 3.7 ZIZ OS

- Status: **desconhecido / previsto**.
- Runtime/profile: não verificado neste inventário inicial.
- Superfícies: a validar.
- Caminho documental: a validar.
- Projetos/rotinas associados: a validar.
- Crons relacionados: nenhum identificado pelo nome no `cronjob list` atual.
- Entra no Fechamento 23h: **sim quando houver profile, projeto, rotina ou conversa ativa**.
- Destino de handoff: a definir.
- Gap: validar existência, escopo e fonte documental antes de dizer que está operacionalmente coberto.

### 3.8 Watchdogs e crons script-only

- Status: **ativos e mistos**.
- Não são agentes conversacionais, mas podem gerar fatos operacionais relevantes.
- Exemplos atuais:
  - `Hermes runtime + cron watchdog no_agent` — ativo, `origin`.
  - `Hermes compression failure self-heal watchdog` — ativo, `origin`.
  - gateways Mordomo/LK Growth/SPITI — ativos.
  - LK WhatsApp responder — ativo/local.
- Entra no Fechamento 23h: **sim, por exceção/falha/alerta/ação tomada; não por sucesso silencioso normal**.
- Gap: revisar quais watchdogs deveriam ser `local` ou silent-OK para reduzir ruído.

## 4. Resumo dos crons atuais por cobertura

Snapshot inicial do `cronjob list`: 22 jobs.

- Ativos/scheduled: 15.
- Pausados: 7.
- `no_agent`/script-only: maioria dos watchdogs e relatórios operacionais.
- Entrega `local`: usada para alguns jobs que devem ser silenciosos/Brain-first.
- Entrega `origin`: ainda usada por vários jobs; deve ser revisada caso o sucesso normal gere ruído para Lucas.

## 5. Regras de delivery para Fechamento 23h

- Fechamento 23h: `local` por padrão.
- Telegram/origin: somente decisão, exceção, falha, risco crítico ou pedido explícito de Lucas.
- Relatórios LK com entrega externa aprovada: sucesso normal deve ficar em receipt/Brain/local, não necessariamente no Telegram.
- HTML/artefatos: não enviar no Telegram salvo pedido de revisão visual/arquivo.

## 6. Gaps para resolver antes do cron recorrente

1. Confirmar e documentar a cobertura real de ZIZ OS.
2. Decidir se Mordomo ganha `agentes/mordomo/` ou `areas/lucas-pessoal/` como pasta documental própria.
3. Atualizar organograma para explicitar SPITI runtime/profile.
4. Revisar entrega `origin` de watchdogs que só deveriam alertar exceção.
5. Decidir se SEO/CRO/LK Growth crons pausados devem continuar no Hermes Geral, migrar para profile LK Growth ou permanecer pausados.
6. Garantir que Mesa COO consuma `reports/daily-consolidation/YYYY-MM-DD.md` quando o cron 23h for ativado.

## 7. Status Fase 1A

- Inventário vivo criado: **sim**.
- Teste manual do Fechamento 23h: **concluído** em `reports/daily-consolidation/2026-05-19.md`.
- Rotina canônica criada: **sim**, `areas/operacoes/rotinas/fechamento-agil-23h.md`.
- Cron recorrente 23h criado: **sim**, delivery `local`, schedule UTC `0 2 * * *`.
