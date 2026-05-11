# LK OS — Weekly CEO Review read-only v0.1

Status: v0.1 executado em 2026-05-11 para a semana fechada 2026-05-04 a 2026-05-10.

## Objetivo

Transformar o Data Spine em revisão semanal executiva, separando receita real, sinais de mídia, tráfego, estoque crítico e aprovações necessárias.

## Script

- `scripts/lk_os_weekly_ceo_review_20260511.py`

## Fontes usadas

- Shopify: `fact_shopify` para pedidos, receita, ticket, produtos, SKUs, tamanhos, landing/referrer e cupons.
- GA4: `fact_ga4` para sessões, canais, transações GA4 e conversão/funil.
- Tiny: `fact_tiny_stock` para estoque no depósito `LK | CONTROLE ESTOQUE`, apenas nos SKUs vendidos na semana.
- Meta Ads: `platform_signal` para gasto, impressões, cliques, compras e valor de plataforma. Não é receita operacional.
- Metricool/Google Ads: `platform_signal` para leitura de presença/linhas de campanhas Google Ads. Não é receita operacional.
- Recomendações: `derived_reconciliation` quando cruzam fonte real + sinal de plataforma.

## Resultado 2026-05-04 a 2026-05-10

- Receita Shopify: `R$ 312.261,74`.
- Pedidos Shopify: `97`.
- Ticket médio Shopify: `R$ 3.219,19`.
- GA4: `29.605` sessões, `55` transações GA4, receita GA4 `R$ 164.657,24`.
- Conversão aproximada pedidos Shopify / sessões GA4: `0,33%`.
- Tiny nos SKUs vendidos: `8` ruptura, `3` baixo estoque vs venda da semana, `3` desconhecidos/mapeamento sem candidato seguro ou saldo legível, `1` OK na amostra.
- Meta Ads: gasto sinalizado `R$ 9.374,42`, compras plataforma `62`, valor plataforma `R$ 140.697,30`, ROAS plataforma `15,01`, mantido como `platform_signal`.
- Metricool/Google Ads: `21` linhas, status `200`, mantido como `platform_signal`.

## Artefatos

- Relatório público: `reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.md`.
- JSON público sanitizado: `reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.json`.
- Preview Telegram curto: `reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.md`.
- Decisão estruturada de silêncio/alerta: `reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.json`.
- JSON privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/`.

## Leitura operacional

1. Shopify confirma uma semana forte em receita, mas GA4 mede menos transações e menos receita, portanto GA4 fica como funil/canal, não financeiro.
2. A principal fila P0/P1 é estoque e saneamento SKU: ruptura, baixo estoque e unknown nos SKUs vendidos.
3. Meta e Metricool agora entram no Weekly Review sem virar ROAS operacional. O script registra o sinal e obriga reconciliação com Shopify/GA4 antes de ação de campanha.
4. O review para em recomendações aprováveis, sem compra, fornecedor, campanha, cadastro ou envio.

## Contrato de silêncio Telegram

Implementado como preview, sem envio externo:

- `would_notify=true` apenas quando houver P0/P1, falha de API ou pedido explícito do Lucas.
- `would_notify=false` mantém silêncio quando não houver anomalia operacional.
- O preview conserva os rótulos `fact_shopify`, `fact_ga4`, `fact_tiny_stock`, `platform_signal` e `derived_reconciliation`.
- O texto deixa claro que é preview interno e não automação enviada.

Para 2026-05-04 a 2026-05-10, o gatilho foi `p0_p1_anomaly`, por ruptura/baixo estoque/mapeamento desconhecido em SKUs vendidos.

## Próximo passo seguro

Criar fila P0/P1 de Stock/SKU para os itens do Weekly Review, ainda read-only, com preview de ação: `repor`, `sourcing`, `mapear SKU Tiny` ou `não agir`.

## O que não foi feito

- Não houve cron.
- Não houve envio externo.
- Não houve campanha, WhatsApp, Klaviyo ou e-mail.
- Não houve alteração em Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.
- Não houve contato com fornecedor ou compra.
