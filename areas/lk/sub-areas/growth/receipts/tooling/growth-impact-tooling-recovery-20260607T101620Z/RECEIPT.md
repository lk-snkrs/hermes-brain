# LK Growth tooling recovery — impact reviews

Data UTC: 20260607T101620Z

## Incidente
Cron de D+7 Nike Mind respondeu como bloqueado porque tentou QA público por uma ferramenta de extração web indisponível e não fez fallback para fontes autenticadas.

## Correção implementada
- Criado script read-only: `/opt/data/profiles/lk-growth/scripts/lk_growth_impact_review.py`.
- Fontes cobertas pelo script: fetch público, Shopify Admin GraphQL, GA4 Data API REST, GSC Search Analytics, GMC Content API.
- DataForSEO validado no runtime atual via MCP para volume/SERP/concorrência.
- Prompts de jobs de impact review/D+7 atualizados para exigir fallback antes de declarar bloqueio.
- Backup do cron: `/opt/data/profiles/lk-growth/cron/jobs.json.bak-growth-impact-tooling-20260607T101620Z`.

## Jobs alterados
[
  {
    "id": "de3a45d36040",
    "name": "LK Experiment Ledger + Impact Review"
  },
  {
    "id": "e31070689c7c",
    "name": "LK Nike Mind guide 7-day impact review"
  },
  {
    "id": "1a813aaca13d",
    "name": "LK D+7 impact review — 3 collection guides published 2026-06-01"
  },
  {
    "id": "9a34dea6ee4b",
    "name": "LK CRO/PDP Funnel Review read-only"
  },
  {
    "id": "12b96a478751",
    "name": "LK Growth OS impact review D+7 — product operational copy cleanup"
  },
  {
    "id": "f0993178730a",
    "name": "LK D+7 impact review — SEO GSC P1 + hotfix Samba Jane"
  }
]

## Smoke tests
- Shopify Admin: OK.
- GSC: OK.
- GMC: OK.
- GA4 pacote Python base: falhou por ausência de `google.analytics`, mas GA4 REST com service account: OK.
- Readiness script: existe.
- DataForSEO: OK no MCP atual.

## Nike Mind recovery audit
Arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/nike-mind-d7-tool-recovery-20260607/impact-review.json`

Resumo executado:
- Collection pública: HTTP 200, title/meta/head OK, FAQPage JSON-LD detectado.
- Guia público: HTTP 200, FAQPage JSON-LD detectado.
- Shopify: coleção encontrada, productsCount=18.
- GA4: collection retornou rows na janela atual.
- GSC: fonte OK; rows da collection = 0 na janela com atraso, o que é dado válido, não falha.
- GMC: fonte OK, match Nike Mind encontrado.
- DataForSEO: demanda transacional alta para `nike mind 001` e `nike mind 002`; SERP mobile mostra Nike, Instagram, Shopping/Popular Products, Mercado Livre, PAA e concorrentes.

## Guardrail
Sem writes externos. Alteração foi local em scripts/cron prompt/Brain.


## Ads/social read-only check complementar
- Metricool: OK, brand `LK Sneakers` visível; conectores declarados incluem Instagram, Facebook Ads, Google Ads, GMB, YouTube, Pinterest, TikTok.
- Meta Ads read-only: OK; token identity respondeu. Contas visíveis incluem uma conta desativada e `LK.Sneakers - Conta de anúncios` ativa.
- Observação: para impact review SEO/CRO, paid/social entra como contexto/confounder, não como verdade final de conversão.
