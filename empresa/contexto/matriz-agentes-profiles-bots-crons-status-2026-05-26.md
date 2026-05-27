# Matriz — Agentes, profiles, bots, crons e status

Data: 2026-05-26  
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

### Mordomo

- Dono lógico: Lucas pessoal / intake.
- Runtime profile: `/opt/data/profiles/mordomo`.
- Bot/canal: Mordomo Telegram quando ativo.
- Área Brain: `agentes/mordomo/` e registros pessoais/multiempresa aplicáveis.
- Cron registry: `/opt/data/profiles/mordomo/cron/jobs.json`.
- Escopo permitido: agenda, follow-ups permitidos, triagem, rascunhos, lembretes, inbox pessoal.
- Writes permitidos: follow-up simples conhecido/verificado; contatos sensíveis e promessas materiais exigem aprovação/fonte.
- Status: **ajustar; contém rotinas Zipper/LK WhatsApp que precisam dono lógico e eventual migração**.

### LK Growth

- Dono lógico: LK Growth.
- Runtime profile: `/opt/data/profiles/lk-growth`.
- Bot/canal: `@LKGrowth_HermesBot` quando ativo.
- Área Brain: `areas/lk/sub-areas/growth/`.
- Cron registry: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Escopo permitido: SEO, GEO, CRO, GMC, analytics, conteúdo, source pages, D+7 impact reviews.
- Writes permitidos: drafts/previews locais; Shopify/GMC/Klaviyo/ads/theme/feed somente com aprovação explícita e escopada.
- Status: **correto; classificar D+7 entre decisão Telegram e relatório local**.

### LK Ops / Atendimento

- Dono lógico: LK Ops/Comercial/Atendimento.
- Runtime profile: `/opt/data/profiles/lk-ops`.
- Bot/canal: LK Ops Telegram quando ativo.
- Área Brain: `areas/lk/sub-areas/atendimento/`.
- Cron registry atual relacionado: Main e Mordomo enquanto migração não for aprovada.
- Escopo permitido: atendimento, loja, vendas operacionais, estoque, preço, disponibilidade, reservas, Tiny/Shopify operacional.
- Writes permitidos: somente quando Lucas aprovar item/ação; exigir fonte viva, snapshot, preview, readback, receipt e rollback.
- Status: **ajustar; dono lógico correto, crons ainda espalhados**.

### LK Shopify

- Dono lógico: LK Shopify.
- Runtime profile: `/opt/data/profiles/lk-shopify`.
- Bot/canal: LK Shopify Telegram quando ativo/preparado.
- Área Brain: `areas/lk/sub-areas/shopify/`.
- Cron registry: sem registry próprio consolidado nesta auditoria.
- Escopo permitido: diagnóstico Shopify, preview, produto/upload, coleções, superfície de publicação, integração com Tiny quando aprovada.
- Writes permitidos: Shopify/Tiny somente com aprovação explícita e escopada, snapshot, readback, receipt e rollback.
- Status: **ajustar documentação; não executar produção por padrão**.

### LK Trends

- Dono lógico: LK Trends / Sourcing Intelligence.
- Runtime profile: `/opt/data/profiles/lk-trends`.
- Bot/canal: LK Trends Telegram quando ativo.
- Área Brain: `areas/lk/sub-areas/trends/`.
- Cron registry: sem registry próprio consolidado nesta auditoria.
- Escopo permitido: tendências, sourcing intelligence, validação de oportunidade, Droper/StockX/GOAT read-only, relatórios.
- Writes permitidos: compra/reserva/negociação/contato fornecedor somente com aprovação explícita e fonte.
- Status: **ajustar escopo para não conflitar com Growth/Ops**.

### SPITI

- Dono lógico: SPITI OS.
- Runtime profile: `/opt/data/profiles/spiti`.
- Bot/canal: SPITI Telegram quando ativo.
- Área Brain: `areas/spiti/`, `agentes/spiti/`.
- Cron registry: `/opt/data/profiles/spiti/cron/jobs.json` não encontrado na auditoria.
- Escopo permitido: Hub, obras, leilões, lotes, clientes, CRM/admin, análise com fonte verificável.
- Writes permitidos: PR/branch/draft conforme escopo; deploy/banco/cliente/bidder/financeiro somente com aprovação explícita e escopada.
- Status: **correto; declarar ausência de crons como escolha ou pendência**.

### Zipper

- Dono lógico: Zipper OS.
- Runtime profile: nenhum dedicado hoje.
- Bot/canal: não criado.
- Área Brain: `areas/zipper/`, `agentes/zipper/`.
- Cron registry atual relacionado: Main e Mordomo.
- Escopo permitido: read-only/documental, CRM/Main e vendas como fonte, rascunhos internos, análise de artistas/obras/enquiries.
- Writes permitidos: nenhum externo sem aprovação explícita e escopada; e-mail/WhatsApp/CRM/preço/proposta/logística bloqueados por padrão.
- Status: **ajustar; runtime futuro só com gatilho de volume/risco/canal**.

### Brain Process / auxiliares read-only

- Dono lógico: Hermes Governança.
- Runtime profiles observados: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`.
- Bot/canal: não assumir público.
- Área Brain: governança e análises locais.
- Cron registry: não consolidado como dono de negócio.
- Escopo permitido: leitura, análise, documentação, experimentos locais.
- Writes permitidos: local/docs; produção/runtime somente com aprovação específica.
- Status: **classificar como ativo/experimento/arquivo/candidato a pausa**.

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
