# Audit — LK Weekly Badges + Collection Sort

Data: 2026-05-29T16:35:00Z
Escopo: auditoria read-only dos dois sistemas semanais da LK (badges BEST SELLER/NEW e ordenação de coleções Regra B). Nenhum write em Shopify foi executado neste audit.

## Scheduler / Hermes cron

- Gateway cron: running.
- `cron.script_timeout_seconds`: 3600 em `/opt/data/config.yaml`.
- Ordenador `787134d4ac5c`: active, schedule `0 9 * * 5`, próxima execução `2026-06-05T09:00:00+00:00` = sexta 06:00 BRT, script `lk_weekly_collection_sort_ruleB.sh`, modo `no-agent`. Último status listado ainda é histórico: timeout antigo em `2026-05-29T06:02:39Z` com 120s, anterior ao ajuste de timeout/manual apply.
- Badges `a1d1e36f8075`: active, schedule `30 9 * * 5`, próxima execução `2026-06-05T09:30:00+00:00` = sexta 06:30 BRT, script `lk_catalog_badges_weekly_sync.sh`, modo `no-agent`.

## Badges audit

Dry-run/readback executado sem `--apply`:

- Log: `/opt/data/profiles/lk-shopify/cron/output/lk_weekly_automation_audit-20260529T163500Z/badges-dry-run.log`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T163500Z/rollback-snapshot.json`
- Produtos escaneados: 2318
- Coleções alvo: 48
- GA4 disponível: sim, 2423 rows
- Produtos com mudança pendente: 4
- Violações OOS/não elegível em BEST SELLER Top 8: 0

Mudanças pendentes detectadas pelo dry-run:

- `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco`: remover tag `new`.
- `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-sail-tropical-pink-rosa`: adicionar tag `new`.
- `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-shy-pink-bege`: adicionar tag `new`.
- `tenis-nike-mind-002-light-violet-ore-roxo`: remover tag `new`.

Interpretação: a correção crítica está OK — nenhum esgotado aparece como BEST SELLER. Porém o sistema de badges não está 100% sincronizado hoje, pois há 4 ajustes de tag `new` pendentes para o próximo apply.

## Ordenador audit

Dry-run/readback executado via wrapper sem `APPLY=1`:

- Log: `/opt/data/profiles/lk-shopify/cron/output/lk_weekly_automation_audit-20260529T163500Z/sorting-dry-run-wrapper.log`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260529T163726Z/rollback-snapshot-pre-write.json`
- Coleções selecionadas: 141
- `would_reorder`: 7
- Wrapper terminou com marcador `done`: sim

Coleções com diferença pendente vs Regra B atual:

- `ultimos-lancamentos-2` — Todos os Produtos — top 4 igual; diferença profunda além do top12.
- `sneakers` — Tênis e Sneakers Originais — top 4 igual; diferença profunda além do top12.
- `nike-todos-os-modelos` — Nike — top 4 igual; diferença profunda além do top12.
- `adidas-todos-os-modelos` — Adidas — top 4 igual; diferença profunda além do top12.
- `onitsuka-tiger-todos-os-modelos` — Onitsuka Tiger — top 4 igual; primeira diferença no top12 na posição 9.
- `onitsuka-tiger-mexico-66` — Onitsuka Tiger Mexico 66 — top 4 igual; primeira diferença no top12 na posição 9.
- `puma-todos-os-modelos` — Puma — top 4 igual; primeira diferença no top12 na posição 7; top8 alvo inclui produtos não disponíveis porque a coleção parece não ter sellable suficientes no universo atual.

Último receipt de apply manual permanece válido como evidência histórica:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260529T153046Z/RECEIPT.md`
- Naquele apply: 141 coleções, 62 movimentos, Admin full ok 141/141, público top12 ok 141/141.

Interpretação: o ordenador está configurado corretamente e o último apply foi validado, mas o estado vivo já tem 7 diferenças pendentes pelo dry-run atual. Portanto não é correto afirmar “100% sincronizado” neste momento sem novo apply aprovado/executado.

## Conclusão

- Scheduler: OK.
- Timeout: OK.
- Badges wrapper: OK.
- Badges regra OOS: OK, 0 violações.
- Badges sincronização total: NÃO 100%, 4 mudanças `new` pendentes.
- Ordenador wrapper: OK.
- Ordenador sincronização total: NÃO 100%, `would_reorder=7` no dry-run atual.

## Risco

Baixo. As divergências são de vitrine/merchandising e tag `new`, não de preço, estoque, checkout, campanha ou cliente. O ponto crítico pedido por Lucas — nenhum esgotado como BEST SELLER — está confirmado.

## Próxima decisão

Se Lucas quiser deixar 100% agora, precisa aprovar o apply dos dois escopos:

1. Badges: executar `lk_catalog_badges_sync_20260528.py --apply` e validar `products_changed=0` + `violacoes_oos=0` no pós-apply.
2. Ordenador: executar `APPLY=1 /bin/bash /opt/data/scripts/lk_weekly_collection_sort_ruleB.sh` e validar dry-run/readback com `would_reorder=0`.

Sem aprovação atual, manter apenas no próximo ciclo semanal de sexta 06:00/06:30 BRT.
