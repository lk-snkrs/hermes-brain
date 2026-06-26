---
title: Receipt — LK Stock routing canon for all LK agents
date: 2026-06-08T18:04:04Z
status: completed
external_writes: 0
secret_values_printed: false
---

# Receipt — LK Stock routing canon for all LK agents

## Pedido

Lucas pediu ensinar todos os agentes LK que qualquer pergunta sobre estoque/pronta entrega deve ser feita ao `lk-stock`; remover do `lk-ops`/Atendimento a opção/ownership de mapeamento/correção de estoque; criar PRD para as melhorias.

## Decisão aplicada

- `lk-stock` é autoridade obrigatória para estoque, pronta entrega, disponibilidade, grade/tamanho, ruptura/baixo estoque, reposição/transferência/compra e divergência SKU/Tiny/Shopify de estoque.
- `lk-ops`/Atendimento não corrige/mapeia disponibilidade por conta própria; deve handoff obrigatório para `lk-stock`.
- Tiny / `LK | CONTROLE ESTOQUE` continua fonte de verdade; Shopify é superfície/gatilho/contexto.

## Artefatos criados

- `areas/lk/sub-areas/stock/references/lk-stock-routing-canon-pronta-entrega-estoque-20260608.md`
- `areas/lk/sub-areas/stock/prd-lk-stock-authority-pronta-entrega-20260608.md`

## Artefatos atualizados

- Perfis LK: `lk-analyst-readonly`, `lk-collection-optimizer`, `lk-content`, `lk-content-reviewer`, `lk-growth`, `lk-ops`, `lk-shopify`, `lk-stock`, `lk-trends`.
- Arquivos de identidade/memória/tooling locais conforme existentes: `SOUL.md`, `MEMORY.md`, `AGENTS.md`, `TOOLS.md`.
- `areas/lk/MAPA.md`
- `areas/lk/templates/handoff-padrao-lk.md`
- skill central `multiempresa-routing-lucas`
- skills/referências locais do `lk-ops` relacionadas a Chatwoot/Shopify-readonly/WhatsApp stock responder.
- `/opt/data/scripts/hermes_memory_hygiene_watchdog.py` para não restaurar a memória antiga de `lk-ops`.

## Guardrails

- Writes externos executados: 0.
- Valores de secrets impressos: false.
- Mudança em gateway/runtime: não executada.
