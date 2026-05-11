# LK OS — Daily Sales Brief read-only v0.1

Status: v0.1 executado em 2026-05-11 para o dia fechado 2026-05-10.

## Objetivo

Transformar o Data Spine em briefing operacional curto, separando fato, sinal de plataforma, reconciliação e aprovação necessária.

## Script

- `scripts/lk_os_daily_sales_brief_20260511.py`

## Fontes usadas

- Shopify: `fact_shopify` para pedidos, receita, produtos, SKUs, tamanhos, landing/referrer.
- GA4: `fact_ga4` para sessões, canais, transações GA4 e leitura de conversão/funil.
- Tiny: `fact_tiny_stock` para estoque no depósito `LK | CONTROLE ESTOQUE`, apenas nos SKUs vendidos no dia.
- Recomendações: `derived_reconciliation` quando cruzam Shopify + GA4 + Tiny.

## Resultado 2026-05-10

- Receita Shopify: `R$ 34.809,92`.
- Pedidos Shopify: `9`.
- Ticket médio: `R$ 3.867,77`.
- GA4: `4.301` sessões, `8` transações GA4, receita GA4 `R$ 33.009,93`.
- Conversão aproximada pedidos Shopify / sessões GA4: `0,21%`.
- Tiny nos SKUs vendidos, reexecução 2026-05-11 19:01 UTC: `4` ruptura, `3` baixo estoque vs venda do dia, `3` desconhecidos/mapeamento sem candidato seguro ou saldo legível.

## Artefatos

- Relatório público: `reports/lk-os-daily-sales-brief-2026-05-10.md`.
- JSON público sanitizado: `reports/lk-os-daily-sales-brief-2026-05-10.json`.
- Preview Telegram curto: `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.md`.
- Decisão estruturada de silêncio/alerta: `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.json`.
- JSON privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/`.

## Leitura operacional

O primeiro Daily Brief real confirmou que o fluxo já consegue sair do inventário de fontes e virar prioridade operacional:

1. Vendas e produtos vêm do Shopify, sem PII.
2. Canais e tráfego vêm do GA4, sem promover receita GA4 a verdade financeira.
3. Estoque crítico vem do Tiny, com depósito oficial.
4. Recomendações param em preview/aprovação, sem compra, fornecedor, campanha ou alteração de cadastro.

## Contrato de silêncio Telegram

Implementado como preview, sem envio externo:

- `would_notify=true` apenas quando houver P0/P1, falha de API ou pedido explícito do Lucas.
- `would_notify=false` mantém silêncio quando não houver anomalia operacional.
- O preview conserva os rótulos `fact_shopify`, `fact_ga4`, `fact_tiny_stock` e `derived_reconciliation`.
- O texto deixa claro que é preview interno e não automação enviada.

Para 2026-05-10, o gatilho foi `p0_p1_anomaly`, porque há ruptura/baixo estoque/mapeamento desconhecido em SKUs vendidos.

## Próximo passo seguro

Criar o módulo Weekly CEO Review read-only, com Meta/Google/Metricool como `platform_signal`, reconciliação contra Shopify/GA4 e sem cron/envio até aprovação.

## O que não foi feito

- Não houve cron.
- Não houve envio externo.
- Não houve campanha, WhatsApp, Klaviyo ou e-mail.
- Não houve alteração em Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.
- Não houve contato com fornecedor ou compra.
