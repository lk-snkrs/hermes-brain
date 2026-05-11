# LK OS Tiny Freshness Report — 2026-05-11

Gerado em: `2026-05-11T18:43:35.728034+00:00`.

Escopo: monitoramento read-only da disponibilidade, latência e cobertura do depósito oficial no Tiny ERP.

Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_tiny_freshness_report_20260511T184335Z.json`.

## Veredito

- Fonte: `Tiny`
- Rótulo: `fact_tiny_stock`
- Status: `green`
- OK operacional: `sim`

## Métricas

- Buscas OK: `6/6`
- Checks de estoque OK: `8/8`
- Depósito oficial visto: `8/8`
- Depósito oficial com saldo retornado: `8/8`
- Erros: `0`
- Latência mediana: `379 ms`
- Latência p95: `1442 ms`
- Latência máxima: `1480 ms`

## Interpretação

- API Tiny respondeu com depósito oficial visível na amostra.

## Amostra de buscas

- `Nike`: status Tiny `OK`, amostra `100`, latência `1422 ms`.
- `Adidas`: status Tiny `OK`, amostra `100`, latência `807 ms`.
- `New Balance`: status Tiny `OK`, amostra `100`, latência `700 ms`.
- `Asics`: status Tiny `OK`, amostra `100`, latência `1480 ms`.
- `Onitsuka`: status Tiny `OK`, amostra `100`, latência `537 ms`.
- `Jordan`: status Tiny `OK`, amostra `100`, latência `853 ms`.

## Limites da leitura

- Este relatório mede saúde e latência da API Tiny, não auditoria completa de estoque por SKU.
- A fonte da verdade de estoque continua sendo Tiny, depósito `LK | CONTROLE ESTOQUE`.
- Qualquer correção de SKU, estoque, preço ou cadastro continua exigindo preview, backup/rollback e aprovação Lucas.

## O que este script não fez

- Não alterou Tiny, Shopify, Supabase, Klaviyo, Meta, Google, Metricool, Notion, n8n ou banco de produção.
- Não enviou e-mail, WhatsApp, campanha ou mensagem externa.
- Não exportou PII para o repositório.
