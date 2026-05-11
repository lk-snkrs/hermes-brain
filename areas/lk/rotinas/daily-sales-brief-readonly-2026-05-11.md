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
- Tiny nos SKUs vendidos: `4` ruptura, `1` baixo estoque vs venda do dia, `5` desconhecidos/mapeamento sem candidato seguro ou saldo legível.

## Artefatos

- Relatório público: `reports/lk-os-daily-sales-brief-2026-05-10.md`.
- JSON público sanitizado: `reports/lk-os-daily-sales-brief-2026-05-10.json`.
- JSON privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/`.

## Leitura operacional

O primeiro Daily Brief real confirmou que o fluxo já consegue sair do inventário de fontes e virar prioridade operacional:

1. Vendas e produtos vêm do Shopify, sem PII.
2. Canais e tráfego vêm do GA4, sem promover receita GA4 a verdade financeira.
3. Estoque crítico vem do Tiny, com depósito oficial.
4. Recomendações param em preview/aprovação, sem compra, fornecedor, campanha ou alteração de cadastro.

## Próximo passo seguro

Criar uma versão Telegram curta a partir do MD/JSON, com contrato de silêncio:

- enviar/mostrar só quando houver P0/P1 ou quando Lucas pedir;
- manter relatório detalhado no Brain;
- antes de cron, definir o que é alerta real vs ruído.

## O que não foi feito

- Não houve cron.
- Não houve envio externo.
- Não houve campanha, WhatsApp, Klaviyo ou e-mail.
- Não houve alteração em Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.
- Não houve contato com fornecedor ou compra.
