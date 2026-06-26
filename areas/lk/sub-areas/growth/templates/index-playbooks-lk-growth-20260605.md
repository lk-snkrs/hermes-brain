# Index — Playbooks práticos LK Growth

Data: 2026-06-05
Status: camada operacional local/read-only para o agente permanente LK Growth.

Use estes playbooks junto dos templates em `agentic-os/templates/` e `templates/growth-audit-output-template.md`.

## Playbooks ativos

1. `playbook-weekly-command-center-lk-growth-20260605.md`
   - Para transformar sinais GA4/GSC/GMC/Shopify/SERP em fila Top 3–5 com score 0–100.
2. `playbook-gmc-product-data-lk-growth-20260605.md`
   - Para Merchant/feed/product data, diagnósticos de link_template, cor, preço, landing e GTIN.
3. `playbook-seo-geo-non-lkgoc-lk-growth-20260605.md`
   - Para SEO/GEO/AI Search não-LKGOC: llms.txt, blocos citáveis, FAQ/schema, titles/metas e source pages não pertencentes a coleção otimizada.
4. `playbook-cro-pdp-collection-handoff-lk-growth-20260605.md`
   - Para hipóteses CRO/PDP/collection que exigem análise de impacto e handoff técnico para LK Shopify quando mexer na superfície Shopify.
5. `playbook-impact-review-lk-growth-20260605.md`
   - Para D+7/D+14/D+30 depois de mudanças aprovadas, separando efeito, hipótese, ruído e próximo aprendizado.

## Regra de seleção

Quando Lucas usa LK Growth para uma demanda de crescimento, o agente deve classificar a demanda, escolher o playbook canônico e acionar automaticamente o subconjunto mínimo de workers temporários necessário. Não rodar todos os workers por padrão.

## Guardrails

- LK Growth é agente permanente; não é subagente.
- Workers temporários são subtarefas internas por execução; não têm Telegram, memória própria, cron, nem write direto.
- LKGOC/coleções otimizadas/guias dedicados pertencem a `[LK] Otimização de Coleções`; Growth só fornece sinais e handoff.
- Shopify/theme/produto/coleção/page/metafield/SEO-field writes pertencem ao agente correto e exigem aprovação escopada com snapshot, rollback, readback e receipt.
- Growth não envia ruído no Telegram; só decisão/exceção/approval packet resumido.
