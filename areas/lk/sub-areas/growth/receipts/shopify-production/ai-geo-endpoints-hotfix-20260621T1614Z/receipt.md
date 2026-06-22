# LK Growth — AI/GEO endpoints hotfix — 2026-06-21

- Approval: Lucas respondeu `Fazer` após diagnóstico de regressão dos endpoints AI/GEO.
- Escopo executado: restauração de `templates/llms.txt.liquid` e `templates/llms-full.txt.liquid` no tema Shopify production para a baseline limpa aprovada em 2026-06-12.
- Causa provável: regressão por overwrite/regeneração do template público `/llms.txt` para versão dinâmica com catálogo/páginas/blogs, removendo `LK_GEO_SOURCE_MAP_START` e reintroduzindo termos operacionais.
- Resultado público após patch: `/llms.txt` status 200, len 5030, source map presente, zero termos proibidos; `/llms-full.txt` status 200, len 119031, source map presente, zero termos proibidos.
- Monitor ajustado: `/agents.md` não falha mais por `estoque` em guardrail negativo; continua falhando se houver `pronta entrega`, `encomenda`, `sob encomenda`, `prazo de entrega` ou `confirme disponibilidade` em `/agents.md`.
- Monitor pós-patch: OK, 0 falhas.
- Rollback assets: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/ai-geo-endpoints-hotfix-20260621T1614Z/before-current-assets`.
- Monitor backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/ai-endpoints-monitor-agents-guardrail-20260621T1614Z`.
- values_printed=false; nenhum secret impresso; estoque não consultado.

## Verificação

```
LK Growth — AI/GEO Endpoints Monitor — 2026-06-21
- Veredito: OK
- Endpoints verificados: 6
- Falhas: 0
- Sem alerta material: endpoints principais responderam, sem termos proibidos, source map presente e sem drift contra baseline aprovada nos arquivos AI principais.
- Relatório JSON: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/monitors/ai-endpoints/ai-endpoints-monitor-20260621T161434Z.json
- values_printed=false; nenhum secret usado ou impresso.

```
