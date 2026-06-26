# LK Weekly Catalog Badges BEST SELLER sync — cron receipt

Data: 2026-05-29T13:20:00Z

## Escopo

Automação semanal para sincronizar tags de badge do catálogo LK no Shopify:

- `NEW`: tag `new` baseada em janela de 90 dias.
- `BEST SELLER`: tags por coleção `best-seller--<collection-handle>`.
- Escopo de coleções: coleções do menu principal deduplicadas.
- Score BEST SELLER: 70% venda líquida/capturada Shopify + 30% GA4 page views.
- Regra crítica: produto esgotado/OOS não pode ser candidato a `BEST SELLER`, mesmo que venceria por score.

## Implementação

- Script de cálculo/aplicação: `/opt/data/hermes_bruno_ingest/scripts/lk_catalog_badges_sync_20260528.py`
- Wrapper semanal: `/opt/data/scripts/lk_catalog_badges_weekly_sync.sh`
- Logs locais: `/opt/data/profiles/lk-shopify/cron/output/lk_catalog_badges_weekly_sync/`

O wrapper executa `--apply`, salva receipt/snapshot no Brain, depois roda uma verificação pós-apply com retry para confirmar:

- `products_changed = 0` após aplicação;
- zero violações OOS/não elegível no Top 8 de `BEST SELLER`;
- receipt e rollback snapshot existem.

## Cron ativo

- Job ID: `a1d1e36f8075`
- Nome: `LK Weekly Catalog Badges BEST SELLER sync`
- Schedule: `30 9 * * 5` UTC = sexta-feira 06:30 BRT
- Delivery: `local`
- Script: `lk_catalog_badges_weekly_sync.sh`
- Mode: `no-agent`
- Próxima execução verificada: `2026-06-05T09:30:00+00:00`

## Última verificação manual

Rodado manualmente após criação do wrapper:

- Resultado: OK
- Pendências pós-apply: 0
- Violações OOS: 0
- Último receipt manual: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T131902Z/receipt.json`
- Rollback manual: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T131902Z/rollback-snapshot.json`

## Não ações

- Não alterou preço, estoque, produto, título, descrição, tema, ordenação de coleção, GMC, campanha, checkout ou cliente.
- Não substitui o cron separado de ordenação de coleções (`LK Weekly Collection Sort Rule B`).
