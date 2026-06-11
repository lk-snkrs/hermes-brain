# Pronta Entrega / POS / LK Stock

**Projeto Brain OS:** `pronta-entrega-pos`
**Owner area:** `areas/lk/sub-areas/stock`
**Status:** hub canônico Brain OS Onda 14 criado em 2026-06-11
**Modo:** índice canônico preservando originais
**Writes externos:** 0

## Objetivo

Canonical Brain OS hub for physical-store ready-stock/POS/pronta-entrega decisions: best sellers, size availability, transfer/replenishment evidence, and approval packets.

## Estado resumido

Hub created to close the scanner gap beside Tiny source-of-truth. Live availability must be checked in Tiny/POS before any customer-facing or purchase decision.

## Fonte da verdade

- Tiny / LK | CONTROLE ESTOQUE as live stock truth when consulted
- Shopify orders/items and POS/sales reports as demand evidence
- Brain as historical evidence and approval ledger

## Arquivos do hub

- README.md
- CURRENT_STATE.md
- DECISIONS_AND_GUARDRAILS.md
- ARTIFACT_INDEX.md
- TIMELINE.md
- NEXT_STEPS.md
- manifest.json

## Evidência do scanner

- Scanner candidate: `lk-stock-tiny-pos`
- Score observado: `90`
- Scanner: `scripts/brain_os_scanner.py`

## Nota

Este hub não moveu nem apagou artefatos históricos. Ele é uma camada de leitura, roteamento e decisão.
