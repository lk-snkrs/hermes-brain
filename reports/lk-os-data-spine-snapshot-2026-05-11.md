# LK OS Data Spine — snapshot read-only 2026-05-11

Gerado em: `2026-05-11T18:32:19.040318+00:00`.

Escopo: snapshot operacional read-only de frescor/contagem/status. Não executa writes, envios, campanhas, alterações de estoque, alterações de preço ou banco de produção.

Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_data_spine_snapshot_20260511T183245Z.json`.

## Resultado por fonte

### Shopify

- Status: `OK`
- Rótulo: `fact_shopify`
- product_count: `2279`
- orders_7d_count: `89`
- products_sample_count: `10`
- orders_sample_count: `10`
- Freshness: `{"max_product_updated_at_sample": "2026-05-08T12:13:14-03:00", "max_order_updated_at_sample": "2026-05-11T14:49:17-03:00"}`

### Tiny

- Status: `OK`
- Rótulo: `fact_tiny_stock`
- stock_checks_sample_count: `6`
- official_deposit_seen_in_sample: `6`

### GA4

- Status: `OK`
- Rótulo: `fact_ga4`
- row_count: `12`
- Janela: `2026-05-04` a `2026-05-10`

### Meta Ads

- Status: `OK`
- Rótulo: `platform_signal`
- rows: `1`
- Nota: Meta é diagnóstico de plataforma, não receita operacional final.

### Metricool Google Ads

- Status: `OK`
- Rótulo: `platform_signal`
- google_ads_rows: `21`
- Janela: `2026-05-04` a `2026-05-10`
- Nota: Metricool/Google Ads é custo e diagnóstico de plataforma, não receita final.

### Klaviyo

- Status: `OK`
- Rótulo: `platform_signal`
- lists_sample_count: `10`
- campaigns_sample_count: `10`
- Nota: Read-only; não cria, agenda nem envia campanha.

## Leitura executiva

- Fontes OK: `6/6`.
- Shopify continua sendo `fact_shopify` para pedidos, vendas, catálogo e SKU canônico.
- Tiny continua sendo `fact_tiny_stock`; o depósito oficial é `LK | CONTROLE ESTOQUE`.
- GA4 é `fact_ga4` para tráfego/canal/funil, não receita final.
- Meta, Google/Metricool e Klaviyo entram como `platform_signal` até reconciliação com Shopify/GA4.

## O que este script não fez

- Não enviou e-mail, WhatsApp ou campanha.
- Não alterou Shopify, Tiny, Klaviyo, Meta, Google, Metricool, Supabase, Notion, n8n ou banco de produção.
- Não exportou PII para o repositório.
