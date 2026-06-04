# LK Growth Tooling Hardening — PageSpeed/Klaviyo/Backlinks

Data UTC: 2026-06-03T15:27:03.152148+00:00
Status: aplicado localmente
Writes externos: não

## 1. PageSpeed / CrUX / CWV

Caminho correto da skill Claude-SEO:

```bash
/opt/data/profiles/lk-growth/skills/content-seo/seo/.venv/bin/python   /opt/data/profiles/lk-growth/skills/content-seo/seo/scripts/pagespeed_check.py   https://lksneakers.com.br --strategy both --json
```

Readiness:

```bash
/opt/data/profiles/lk-growth/scripts/lk_growth_tooling_readiness.py
```

Estado atual: a camada GSC/GA4 funciona na `.venv`, mas PageSpeed/CrUX precisa de `GOOGLE_API_KEY` ou `api_key` em `/opt/data/profiles/lk-growth/home/.config/claude-seo/google-api.json`.

Guardrail: não instalar pacotes de sistema nem gravar credenciais sem aprovação explícita. A alternativa `blog-google` falha por falta de `python3.13-venv`; usar a camada `seo` existente.

## 2. Klaviyo analytics read-only

Script preparado:

```bash
KLAVIYO_API_KEY=[REDACTED] /opt/data/profiles/lk-growth/scripts/lk_klaviyo_readonly_analytics.py --days 7 --json
```

O script usa apenas endpoints de leitura/consulta. Não envia, agenda, muda lista, perfil, campanha ou flow.

Métricas alvo:

- Opened Email
- Clicked Email
- Received Email
- Placed Order
- Started Checkout
- Added to Cart
- Active on Site

Uso nos crons:

- Weekly: sinal CRM de demanda e receita atribuída.
- CRO: abandono/intenção por produto ou campanha quando disponível.
- Impact Review: confounder/contexto para mudanças que receberam campanha/newsletter.

Pendente: disponibilizar `KLAVIYO_API_KEY`/`KLAVIYO_PRIVATE_API_KEY` no runtime seguro, sem salvar em Brain.

## 3. Ahrefs / off-site / backlinks

Ahrefs autenticado não foi confirmado.

Readiness atual da skill backlink:

```bash
/opt/data/profiles/lk-growth/skills/content-seo/seo/.venv/bin/python   /opt/data/profiles/lk-growth/skills/content-seo/seo/scripts/backlinks_auth.py --check --json
```

Disponível agora:

- Common Crawl domain graph.
- Backlink verification crawler.
- DataForSEO MCP para SERP/competição/keyword/AI visibility.

Pendente opcional:

- `MOZ_API_KEY` para DA/PA/spam scoring.
- `BING_WEBMASTER_API_KEY` para Bing Webmaster.
- Ahrefs só se Lucas fornecer/autorizar conector específico.

Regra de comunicação: não prometer “Ahrefs” nos relatórios; dizer “off-site/backlink signals via CommonCrawl/DataForSEO/Moz quando disponível”.

## Cron behavior esperado

Os crons devem declarar em todo relatório material:

- Fontes verificadas.
- Fontes indisponíveis.
- Nível de confiança.
- Se é decision-grade ou não.
- Próxima ação com aprovação/rollback quando houver write.


## Atualização 2026-06-03T17:50:02+00:00 — Doppler confirmado

Secrets encontrados em Doppler `lc-keys/prd` (nomes apenas, valores nunca persistidos):
- `PAGESPEED_API_KEY` / `GOOGLE_API_KEY`: presentes; PageSpeed/CrUX operacional via wrapper local.
- `KLAVIYO_API_KEY`: presente; Klaviyo analytics read-only operacional via wrapper local.
- `AHREFS_API_KEY` / `AHREFS_API_TOKEN`: presentes; Ahrefs Site Explorer domain-rating validado.

Wrappers locais read-only:
- `/opt/data/profiles/lk-growth/scripts/lk_pagespeed_crux_readonly.py <url> --crux-only --strategy mobile --json`
- `/opt/data/profiles/lk-growth/scripts/lk_klaviyo_readonly_analytics.py --days 7 --json`
- `/opt/data/profiles/lk-growth/scripts/lk_ahrefs_readonly_probe.py --target lksneakers.com.br`

Validação:
- PageSpeed/CrUX homepage: OK, sem erro; field data disponível.
- Klaviyo probe: OK; 7 métricas principais deduplicadas e agregação 1d sem erro após throttle control.
- Ahrefs: OK; endpoint `site-explorer/domain-rating` validado para `lksneakers.com.br`.

Guardrail: scripts carregam secrets em runtime a partir do Doppler/token local, não gravam valores e não imprimem chaves.
