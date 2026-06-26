# LK OS — Next Execution Queue, 2026-05-13

Generated at: `2026-05-13T03:33:24-03:00`

## Veredito

Lucas pediu para deixar **Customer Trust & Loyalty / LK Rewards / Judge.me** para depois. A frente foi reclassificada como `pending_future` e a execução volta para os próximos blocos não-Loyalty do PRD LK OS.

Modo desta rodada: read-only/local. Nenhum write, envio, campanha, compra, contato, cron, n8n, Shopify, Tiny, Klaviyo, Rivo, Judge.me, Notion, Merchant apply ou infra executado.

## Estado atualizado das frentes

### 1. GMC / Merchant Center — frente ativa recomendada

Últimos refreshes read-only executados agora:

- Post-cleanup monitor:
  - Merchant products: 23.194
  - Product statuses: 23.194
  - Online: 11.617
  - Local: 11.577
  - Local C/D antigos removidos continuam ausentes: 63/63
  - Replacements locais preservados: 14/14
  - Rows com item issues: 2.563
  - Issue instances: 11.791
  - Rows com destination problem: 17

- Diagnostics triage:
  - Issue instances: 11.791
  - Delta vs baseline Phase 7: 0
  - Top bucket P1: `attribute_completion_preview`
  - Affected product IDs: 2.100
  - Issue instances no top bucket: 10.162
  - Top issue: `missing_item_attribute_for_product_type`

- P1 attribute completion preview:
  - Produtos revisados: 2.100
  - Issue instances: 10.162
  - Candidate rows para approval packet futuro: 1.583
  - Blocked rows: 469
  - High-confidence candidates: 60
  - Medium-confidence candidates/review: 1.523
  - Missing attribute counts:
    - color: 524
    - size: 1.585
    - age group: 1.510
    - gender: 1.510
    - price: 10

Próximo bloco seguro:

1. gerar approval packet no-write separado por confiança/campo;
2. separar `high_confidence` vs `medium_needs_review`;
3. bloquear os 469 sem match Shopify exato;
4. não aplicar Merchant sem aprovação inline de Lucas.

### 2. Klaviyo CRM Draft — manter bloqueado para envio

Estado: campanha P1 continua em Draft por decisão Lucas anterior. Próximo seguro é só readiness/review no painel, sem send/schedule/flow.

Ação recomendada agora: manter em espera até Lucas querer revisar campanha. Não é a melhor frente para avançar se o objetivo é executar PRD amplo sem acionar cliente.

### 3. Sourcing / Compras — só por pedido + stockout

Estado: cotações genéricas antigas continuam supercedidas. O fluxo correto é:

```text
venda/pedido/solicitação concreta
→ SKU/tamanho e stockout confirmados
→ Droper primeiro
→ se não houver, StockX vs GOAT
→ tarefa Notion/Júlio preview
→ compra humana
```

Ação recomendada agora: não rodar sourcing genérico. Aguardar gatilho real de pedido/stockout ou criar apenas template/guard read-only.

### 4. WhatsApp wacli `hermes`

Estado: pendente porque Lucas está sem WhatsApp para parear. Processo de pareamento anterior foi pausado.

Ação recomendada agora: não insistir. Retomar quando Lucas puder digitar código no celular.

### 5. Customer Trust & Loyalty

Estado: `pending_future` por decisão Lucas. Documentação base já existe, mas não é frente ativa.

## Fila executiva recomendada

### P1 — GMC attribute completion packet v2, no-write

Ação: transformar o preview atual de 1.583 candidates em pacote de aprovação limpo, com campos, contagens, exemplos sanitizados e rollback/escopo definido.

Risco: baixo enquanto preview-only.

Bloqueado antes de apply: qualquer `products.update`, supplemental feed, feed rule ou `fetchNow` exige aprovação inline.

### P1 — Atualizar Mission Control snapshot

Ação: incorporar o novo estado do GMC e a decisão de Loyalty pending em snapshot executivo curto.

Risco: baixo se local/read-only.

Bloqueado: virar UI, cron próprio ou worker Kanban sem aprovação.

### P2 — Revisar Klaviyo Draft readiness

Ação: confirmar campanha/lista/template em Draft, sem envio/agendamento.

Risco: baixo se read-only.

Bloqueado: send/schedule/flow/customer contact.

### P2 — Lead time real por canal

Ação: substituir lead time padrão por parâmetros Monbam/Droper/interno quando Lucas/Júlio confirmarem números.

Risco: depende de dados humanos; sem write.

## Não executado

- Merchant write/apply/feed/fetchNow.
- Shopify write/theme/PDP.
- Tiny write.
- Klaviyo send/schedule/flow.
- WhatsApp send/sync novo/pareamento.
- Rivo/Judge.me access/write.
- Notion write.
- Sourcing marketplace call.
- Compra/PO/reserva/fornecedor.
- Cron/n8n/infra.

## Próximo passo recomendado

Executar **P1 GMC attribute completion packet v2 no-write**. Isso mantém o PRD andando em uma frente objetiva, mensurável e ainda segura.
