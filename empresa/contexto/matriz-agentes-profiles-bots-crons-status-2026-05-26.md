# Matriz — Agentes, profiles, bots, crons e status

Data: 2026-05-30  
Escopo: matriz local/read-only para alinhar organograma, runtime e donos lógicos.  
Produção/runtime: nenhuma alteração feita por este documento.

## Regra de leitura

- **Dono lógico** define quem responde pelo conteúdo/rotina.
- **Runtime atual** define onde o processo/profile roda hoje.
- **Cron registry** define onde a rotina está armazenada hoje, não necessariamente seu dono final.
- **Status** indica se está correto, precisa ajustar, migrar ou pausar.

## Matriz principal

### Hermes Geral / Main

- Dono lógico: Hermes COO / Governança central.
- Runtime profile: `/opt/data`.
- Bot/canal: Telegram principal de Lucas.
- Área Brain: `empresa/contexto/`, `areas/operacoes/`, `reports/governance/`.
- Cron registry: `/opt/data/cron/jobs.json`.
- Escopo permitido: governança, Brain, Mesa COO, watchdogs centrais, approval packets, auditorias, coordenação multiempresa.
- Writes permitidos: local/docs; produção/externo somente com aprovação explícita e escopada.
- Status: **correto; ajustar rotinas LK/Zipper hospedadas por histórico**.
- Watchdog/gateway: Main é check-only no watchdog global `b78ae7ac81d0`; não reiniciar automaticamente Docker/Main por script local.

### Mordomo

- Dono lógico: Lucas pessoal / intake.
- Runtime profile: `/opt/data/profiles/mordomo`.
- Bot/canal: Mordomo Telegram quando ativo.
- Área Brain: `agentes/mordomo/` e registros pessoais/multiempresa aplicáveis.
- Cron registry: `/opt/data/profiles/mordomo/cron/jobs.json`.
- Escopo permitido: agenda, follow-ups permitidos, triagem, rascunhos, lembretes, inbox pessoal.
- Writes permitidos: follow-up simples conhecido/verificado; contatos sensíveis e promessas materiais exigem aprovação/fonte.
- Status: **correto como Mordomo; pendente apenas classificar rotinas Zipper/LK WhatsApp hospedadas por histórico antes de qualquer migração**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### [LC] Claude Cli

- Dono lógico: Lucas / brainstorm de pautas.
- Runtime profile: `/opt/data/profiles/lc-claude-cli`.
- Bot/canal: CLI local preparado; Telegram/canal dedicado pendente de token/canal explícito.
- Área Brain: `agentes/lc-claude-cli/`.
- Modelo: Claude via Claude CLI/proxy local `http://127.0.0.1:3456/v1`.
- Cron registry: nenhum; sem proatividade automática por padrão.
- Escopo permitido: ideação de pautas, ângulos, títulos, perguntas, crítica editorial e briefs internos.
- Writes permitidos: local/docs; publicação/envio/campanha/cron/produção somente com aprovação explícita e roteamento ao especialista correto.
- Status: **profile criado e CLI validado; gateway parado intencionalmente até ativação de canal**.
- Watchdog/gateway: não coberto pelo watchdog global enquanto não for agente Telegram operacional.

### LK Growth

- Dono lógico: LK Growth.
- Runtime profile: `/opt/data/profiles/lk-growth`.
- Bot/canal: `@LKGrowth_HermesBot` quando ativo.
- Área Brain: `areas/lk/sub-areas/growth/`.
- Cron registry: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Escopo permitido: SEO, GEO, CRO, GMC, analytics, conteúdo, source pages, D+7 impact reviews.
- Writes permitidos: drafts/previews locais; Shopify/GMC/Klaviyo/ads/theme/feed somente com aprovação explícita e escopada.
- Status: **correto; classificar D+7 entre decisão Telegram e relatório local**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### LK Ops / Atendimento

- Dono lógico: LK Ops/Comercial/Atendimento.
- Runtime profile: `/opt/data/profiles/lk-ops`.
- Bot/canal: LK Ops Telegram quando ativo.
- Área Brain: `areas/lk/sub-areas/atendimento/`.
- Cron registry atual relacionado: Main e Mordomo enquanto migração não for aprovada.
- Escopo permitido: atendimento, loja, vendas operacionais, estoque, preço, disponibilidade, reservas, Tiny/Shopify operacional.
- Writes permitidos: somente quando Lucas aprovar item/ação; exigir fonte viva, snapshot, preview, readback, receipt e rollback.
- Status: **correto como dono lógico; pendência documentada é inventário/migração opcional de crons comerciais hoje espalhados**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### LK Shopify

- Dono lógico: LK Shopify.
- Runtime profile: `/opt/data/profiles/lk-shopify`.
- Bot/canal: LK Shopify Telegram ativo quando o gateway do profile está rodando.
- Área Brain: `areas/lk/sub-areas/shopify/`.
- Cron registry: sem registry próprio consolidado nesta auditoria.
- Escopo permitido: diagnóstico Shopify, preview, produto/upload, coleções, superfície de publicação, integração com Tiny quando aprovada.
- Writes permitidos: Shopify/Tiny somente com aprovação explícita e escopada, snapshot, readback, receipt e rollback.
- Status: **documentação mínima completa; não executar produção por padrão**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### LK Trends

- Dono lógico: LK Trends / Sourcing Intelligence.
- Runtime profile: `/opt/data/profiles/lk-trends`.
- Bot/canal: LK Trends Telegram quando ativo.
- Área Brain: `areas/lk/sub-areas/trends/`.
- Cron registry: sem registry próprio consolidado nesta auditoria.
- Escopo permitido: tendências, sourcing intelligence, validação de oportunidade, Droper/StockX/GOAT read-only, relatórios.
- Writes permitidos: compra/reserva/negociação/contato fornecedor somente com aprovação explícita e fonte.
- Status: **correto; fronteira documentada com Growth/Ops e sem write/compra por padrão**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### SPITI

- Dono lógico: SPITI OS.
- Runtime profile: `/opt/data/profiles/spiti`.
- Bot/canal: SPITI Telegram quando ativo.
- Área Brain: `areas/spiti/`, `agentes/spiti/`.
- Cron registry: `/opt/data/profiles/spiti/cron/jobs.json` não encontrado na auditoria.
- Escopo permitido: Hub, obras, leilões, lotes, clientes, CRM/admin, análise com fonte verificável.
- Writes permitidos: PR/branch/draft conforme escopo; deploy/banco/cliente/bidder/financeiro somente com aprovação explícita e escopada.
- Status: **correto; declarar ausência de crons como escolha ou pendência**.
- Watchdog/gateway: coberto pelo watchdog global `b78ae7ac81d0`.

### Zipper

- Dono lógico: Zipper OS.
- Runtime profile: nenhum dedicado hoje.
- Bot/canal: não criado.
- Área Brain: `areas/zipper/`, `agentes/zipper/`.
- Cron registry atual relacionado: Main e Mordomo.
- Escopo permitido: read-only/documental, CRM/Main e vendas como fonte, rascunhos internos, análise de artistas/obras/enquiries.
- Writes permitidos: nenhum externo sem aprovação explícita e escopada; e-mail/WhatsApp/CRM/preço/proposta/logística bloqueados por padrão.
- Status: **correto documental/read-only; runtime futuro só com gatilho objetivo de volume/risco/canal**.

### Brain Process / auxiliares read-only

- Dono lógico: Hermes Governança.
- Runtime profiles observados: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`.
- Bot/canal: não assumir público.
- Área Brain: governança e análises locais.
- Cron registry: não consolidado como dono de negócio.
- Escopo permitido: leitura, análise, documentação, experimentos locais.
- Writes permitidos: local/docs; produção/runtime somente com aprovação específica.
- Status: **classificados por política em `empresa/contexto/criterios-promocao-agentes-auxiliares.md`; preparados/read-only, não agentes operacionais por padrão**.
- Watchdog/gateway: não auto-startar por token; só entram no watchdog global se Lucas decidir que são agentes Telegram operacionais.

## Rotinas com dono lógico diferente do runtime atual

- LK Daily Sales / Weekly CEO / Pulso Comercial / Store Close: dono lógico LK Ops; runtime atual Main.
- Zipper Gmail/vendas/enquiry: dono lógico Zipper; runtime atual Main/Mordomo.
- LK WhatsApp responder: dono lógico LK Ops/Mordomo conforme canal e risco; exige classificação caso a caso.
- LK Growth D+7 impact reviews: dono lógico Growth; delivery deve separar decisão Telegram de relatório local.

## Próximas ações permitidas sem produção

1. Completar docs dos subespecialistas.
2. Classificar jobs linha a linha antes de qualquer migração.
3. Registrar receipts/handoffs para decisões materiais.
4. Preparar approval packets por lote para migração/restart/write externo.
