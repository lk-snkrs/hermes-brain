# Receipt — correção do cron do ordenador LK Sort Manual Regra B

Data: 2026-05-29T14:38Z

## Escopo

Correção local da automação semanal do ordenador de produtos por coleção da LK.

## Evidência

- Job do ordenador: `787134d4ac5c`
- Schedule anterior observado: `0 6 * * 5`, com próximo run `2026-06-05T06:00:00+00:00` (03:00 BRT)
- Schedule corrigido: `0 9 * * 5`, com próximo run `2026-06-05T09:00:00+00:00` (06:00 BRT)
- Último erro histórico antes da correção: `Script timed out after 120s`
- Timeout global de scripts cron ajustado em `/opt/data/config.yaml`: `cron.script_timeout_seconds: 3600`
- Backup de config antes do ajuste: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/config-backup-before-cron-timeout-20260529T143408Z.yaml`

## Verificação read-only pós-correção

Comando executado sem write Shopify:

```bash
/opt/hermes/.venv/bin/python /opt/data/hermes_bruno_ingest/scripts/apply_all_manual_collections_ruleB_net_sales_ga4_20260528.py --offset 0 --limit 0 --dry-run
```

Resultado:

- `selected_count`: 144 coleções manuais
- `would_reorder`: 33 coleções
- Snapshot dry-run: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260529T143443Z/rollback-snapshot-pre-write.json`
- Logs:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/weekly-logs/verify-dry-run-after-cron-fix-20260529.out`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/weekly-logs/verify-dry-run-after-cron-fix-20260529.err`
- Duração aproximada do dry-run: 160s, confirmando que o limite antigo de 120s era insuficiente e que o novo limite de 3600s cobre a execução.

## Não ações

- Nenhum `collectionReorderProducts` foi executado nesta correção.
- Nenhuma alteração em produtos, tags, preços, estoque, tema, SEO, GMC, campanhas, checkout ou clientes.

## Próxima decisão

Para zerar o `would_reorder` e deixar o storefront alinhado antes da próxima sexta, executar um apply aprovado do ordenador, com snapshot, readback Admin + público e receipt final.
