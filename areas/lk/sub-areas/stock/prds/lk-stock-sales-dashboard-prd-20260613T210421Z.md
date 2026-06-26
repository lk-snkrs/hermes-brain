# PRD — LK Estoque + Vendas Dashboard

> **Status:** PRD/Design para aprovação antes de código produtivo.  
> **Data:** 2026-06-13T21:04:21Z  
> **Owner operacional:** `lk-stock`  
> **Superfície alvo:** dashboard interno de estoque LK (`estoque.lkskrs.online`) com dois universos: **Estoque** e **Vendas**, mais cruzamento para **Compra/Reposição**.

## 1. Problema

Hoje o dashboard de estoque já mostra disponibilidade interna, grade, ruptura, P0/P1/P2, qualidade da base e busca de vendedor. Mas a decisão mais importante ainda fica incompleta: **o que comprar agora e qual grade está faltando**.

Para isso, estoque sozinho não basta. Precisamos cruzar:

1. **Vendas reais** — o que vendeu mais, em quais tamanhos, canal, receita e recência.
2. **Estoque atual** — saldo por SKU/tamanho no depósito `LK | CONTROLE ESTOQUE`, com freshness e identidade SKU↔Tiny↔Shopify.
3. **Grade ideal/real** — quais tamanhos daquele produto venderam, quais ainda existem, quais zeraram e quais nunca apareceram.
4. **Regra de compra conservadora** — sugerir fila de decisão, não compra automática.

## 2. Objetivo

Criar dentro do dashboard um **universo de Vendas** e um **cruzamento Estoque × Vendas** para responder:

- O que mais vendeu hoje, D7, D30, MTD e D90/D180 quando disponível?
- Quais produtos vendem bem e estão zerados ou com grade quebrada?
- Qual tamanho falta em cada modelo campeão?
- O que é P0 de reposição agora?
- O que é P1 porque vende, mas a identidade SKU/Tiny/Shopify está bloqueada?
- O que parece vender, mas ainda não tem histórico suficiente para compra?

## 3. Não objetivos / bloqueios

Fora de escopo desta primeira implementação:

- Comprar produto automaticamente.
- Escrever no Tiny, Shopify, Notion, WhatsApp, Klaviyo ou fornecedor.
- Prometer disponibilidade pública.
- Alterar estoque.
- Criar cron/webhook/runtime novo.

Guardrails obrigatórios:

- `tiny_write = 0`
- `shopify_write = 0`
- `writes_externos = 0`
- `public_availability_safe = 0`
- `availability_claim_allowed = 0`

## 4. Fontes reais disponíveis hoje

### 4.1 Estoque

Fonte quente atual:

- Pointer: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- DB atual: `areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260613T093030ZS2.db`

Tabelas já verificadas:

- `current_local_stock` — 3746 linhas
- `current_stock_scored` — 903 linhas
- `demand_signals_stock_os` — 352 sinais
- `demand_score_summary` — 21 linhas
- `tiny_full_sync_runs`
- `tiny_full_sync_item_ledger`

### 4.2 Vendas

Fontes read-only encontradas:

- `reports/lk-sales-reports/*.json`
  - Exemplo: `lk-sales-reports-pulse-finance-16h-20260613T160000-0300.json`
  - Contém MTD, pulse 16h, loja, top_products, channels, revenue.
- `local_sql/lk_data_spine_snapshots/lk_os_daily_sales_brief_*.json`
  - Exemplo: `lk_os_daily_sales_brief_20260612_110133Z.json`
  - Contém Shopify sales, Tiny stock checks para SKUs vendidos, GA4.

Ponto crítico: essas fontes são boas para V1, mas podem ser agregadas/top-products, não necessariamente export full order-items histórico. V1 deve ser honesta sobre cobertura.

## 5. Modelo mental do produto

O dashboard passa a ter 3 áreas internas:

### A. Estoque

Já existe e continua:

- Produto/grade
- Cards
- SKU técnico
- ruptura/baixo estoque
- P0/P1/P2 operacional
- qualidade da base

### B. Vendas

Novo universo:

- Hoje/parcial
- Ontem fechado
- D7
- MTD
- D30 quando disponível
- Top produtos por unidades
- Top produtos por receita
- Top marcas
- Canal: loja física vs online
- Tamanhos que mais vendem por produto/família

### C. Compra / Reposição

Cruzamento dos dois:

- `Vendeu e zerou`
- `Vendeu e tem ≤1`
- `Vendeu em vários tamanhos, mas grade está quebrada`
- `Top seller com identidade bloqueada`
- `Tem estoque, mas não vendeu`
- `Vende bem online, mas loja física não tem grade`
- `Sugerir para Notion/Júlio` como draft local, sem write externo.

## 6. Entidades e métricas V1

### Sales product row

Campos normalizados:

- `sku`
- `sku_norm`
- `product_title`
- `handle_guess` quando possível
- `size_or_variant`
- `quantity`
- `line_revenue_estimate`
- `channels.online`
- `channels.loja` / `pos`
- `window_key`: `today`, `yesterday`, `d7`, `mtd`, `previous_mtd`, etc.
- `source_file`
- `source_freshness`

### Crossed stock-sales row

Campos derivados:

- Dados de venda acima
- `stock_quantity_max_observed`
- `stock_freshness`
- `canonical_status`
- `identity_resolved_safe`
- `local_consult_safe`
- `grade_status`: `OK`, `BAIXA`, `QUEBRADA`, `ZERADA`, `DESCONHECIDA`
- `missing_sizes`
- `available_sizes`
- `sell_through_signal`
- `purchase_lane`
- `purchase_priority`
- `suggested_next_action`

## 7. Regras de decisão de compra V1

### P0 — decisão de reposição agora

Condição V1:

- Vendeu no período recente ou MTD;
- SKU/produto com estoque `0` ou grade criticamente quebrada;
- identidade local resolvida ou suficientemente segura;
- não é fixture/probe/test;
- exige reconfirmação Tiny antes de qualquer compra/write externo.

Ação: `PREPARAR_DRAFT_NOTION_JULIO_LOCAL`, sem escrever no Notion.

### P1 — vende, mas identidade bloqueada

Condição:

- Produto aparece em vendas;
- estoque ou SKU não cruza com confiança;
- `canonical_status` bloqueado/ambíguo.

Ação: `RESOLVER_IDENTIDADE_ANTES_DE_COMPRA`.

### P2 — monitorar

Condição:

- Sinal de venda existe, mas estoque ainda está saudável ou histórico insuficiente.

Ação: `MONITORAR_D7_D30_D90`.

### P3 — sem ação

Sem venda relevante ou sem risco de estoque.

## 8. UX proposta

### Navegação principal

Adicionar no topo:

- `Estoque`
- `Vendas`
- `Compra / Reposição`

### Tela Vendas

Blocos:

- KPIs: pedidos, receita, unidades, ticket médio.
- Ranking: top produtos por unidades.
- Ranking: top produtos por receita.
- Top marcas.
- Mix loja física vs online.
- Ranking por tamanho/modelo.

### Tela Compra / Reposição

Blocos:

- P0: vendeu e zerou/grade crítica.
- P1: venda com identidade bloqueada.
- Grade faltante por produto.
- Draft local para Júlio/Notion.
- Filtros: marca, canal, janela, tamanho, prioridade.

## 9. Arquitetura técnica V1

### Backend Node/dashboard

Adicionar endpoints read-only:

- `GET /api/vendas/summary`
- `GET /api/vendas/products`
- `GET /api/estoque-vendas/replenishment`

Esses endpoints devem ler artefatos locais JSON já existentes e/ou um snapshot SQLite local gerado por script.

### Script local de agregação

Criar script offline/read-only:

- `areas/lk/sub-areas/stock/scripts/lk_stock_sales_crossing_build.py`

Responsável por:

1. Ler pointer Stock OS.
2. Ler reports de vendas locais.
3. Normalizar SKUs/títulos/tamanhos.
4. Cruzar com `current_local_stock`/`current_stock_scored`.
5. Gerar DB/JSON de read model:
   - `stock_sales_product_signals`
   - `stock_sales_grade_gaps`
   - `stock_sales_replenishment_queue`
6. Atualizar artefato/pointer local específico para dashboard.

### Frontend

Adicionar módulos em `dashboard-utils.js`:

- `buildSalesSummary`
- `normalizeSalesProduct`
- `crossSalesWithStock`
- `buildReplenishmentQueue`
- `groupSalesByProductGrade`

Adicionar UI em `index.html` com abas e cards.

## 10. Critérios de aceite V1

1. Dashboard mostra aba **Vendas** com dados vindos de reports reais.
2. Dashboard mostra aba **Compra / Reposição** cruzando vendas com estoque.
3. Cada recomendação mostra fonte e freshness.
4. Nenhum item vira compra automática.
5. P0/P1/P2 têm explicação clara.
6. SKU/tamanho permanece visível.
7. Produto é agrupado por modelo/grade, não explodido só por SKU.
8. Sem write externo.
9. Testes passam.
10. Smoke produção autenticado passa e sem senha continua 401.

## 11. Riscos

- Vendas disponíveis podem ser top-products e não order-item completo.
- SKUs `sem_sku` ou variant IDs precisam de fallback conservador.
- D90/D180 pode exigir fonte adicional/Shopify read-only direto se os snapshots atuais não cobrirem janela longa.
- Quantidade sugerida de compra não deve ser agressiva sem histórico longo.

## 12. Plano de implementação recomendado

### Fase 1 — Vendas no dashboard usando snapshots existentes

- Sem nova API externa.
- Sem cron.
- Ler JSONs locais já existentes.
- Exibir top vendas + cruzamento básico com estoque.

### Fase 2 — Read model local Stock × Sales

- Script Python gera SQLite/JSON próprio.
- Dashboard lê read model estável.
- Melhor ranking P0/P1/P2.

### Fase 3 — Janelas D30/D90/D180 decision-grade

- Se necessário, consultar Shopify read-only para order-items completos por janela.
- Calcular sell-through e grade ideal.
- Separar compra conservadora vs monitoramento.

### Fase 4 — Draft Notion/Júlio

- Gerar CSV/preview local importável.
- Escrever no Notion só com aprovação escopada.

## 13. Decisão pedida ao Lucas

Recomendação: aprovar implementação da **Fase 1 + Fase 2 local/read-only** agora.

Isso entrega valor rápido sem mexer em Tiny/Shopify/Notion e cria a base para compra real com menos risco.
