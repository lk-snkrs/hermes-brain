# LK GMC Executable Previews, 2026-05-12

Status: `gmc_executable_previews_ready_preview_only`

## Resumo executivo
- Itens P0/P1 com preview executável: 4671
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json`
- Registros no snapshot privado: 4671
- Escritas executadas: 0

## Pacotes prontos para aprovação futura
### A_online_stale_triage
- Itens: 2415
- Prioridades: {'P0': 2383, 'P1': 32}
- Canais: {'online': 2415}
- Buckets: {'online_unmatched_possible_stale': 2415}
- Gate: Approval required to delete/suppress exact Merchant online product IDs or change source feed/app.
- Amostra product IDs: ['online:pt:BR:10002025469927148791', 'online:pt:BR:10131134412697596529', 'online:pt:BR:10310578515087778063', 'online:pt:BR:10312083433143971915', 'online:pt:BR:10339778285846091232', 'online:pt:BR:10494354248419479343', 'online:pt:BR:10588380249806721771', 'online:pt:BR:10591784840915585992', 'online:pt:BR:10621083909303937387', 'online:pt:BR:1066317393403197052']

### B_online_identifier_fix
- Itens: 954
- Prioridades: {'P1': 954}
- Canais: {'online': 954}
- Buckets: {'online_identifier_mismatch': 954}
- Gate: Approval required for exact identifier mapping write in Merchant/feed/Shopify/app.
- Amostra product IDs: ['online:pt:BR:11020158', 'online:pt:BR:1183A592200', 'online:pt:BR:1183B566 021-1', 'online:pt:BR:1183B566 021-2', 'online:pt:BR:1183B566 021-3', 'online:pt:BR:1183B566 021-4', 'online:pt:BR:1183B566 021-5', 'online:pt:BR:1183B566 021-6', 'online:pt:BR:1183B566 021-9', 'online:pt:BR:1183C102 751-1']

### D_local_stale_triage
- Itens: 455
- Prioridades: {'P1': 455}
- Canais: {'local': 455}
- Buckets: {'local_unmatched_after_normalization': 455}
- Gate: Approval required to delete/suppress exact local Merchant product IDs after POS/Tiny validation.
- Amostra product IDs: ['local:pt:BR:LIA_1201A256-113-34', 'local:pt:BR:LIA_1201A256-113-35', 'local:pt:BR:LIA_1201A256-113-36', 'local:pt:BR:LIA_1201A256-113-37', 'local:pt:BR:LIA_1201A256-113-38', 'local:pt:BR:LIA_1201A256-113-39', 'local:pt:BR:LIA_1201A256-113-40', 'local:pt:BR:LIA_1201A256-113-41', 'local:pt:BR:LIA_1201A256-113-42', 'local:pt:BR:LIA_1201A256-113-43']

### C_local_identifier_fix
- Itens: 847
- Prioridades: {'P1': 847}
- Canais: {'local': 847}
- Buckets: {'local_identifier_mismatch': 847}
- Gate: Approval required for local inventory/POS/Merchant mapping write; do not disable local channel.
- Amostra product IDs: ['local:pt:BR:LIA_11020158', 'local:pt:BR:LIA_1183A592200', 'local:pt:BR:LIA_1183B566 021-1', 'local:pt:BR:LIA_1183B566 021-2', 'local:pt:BR:LIA_1183B566 021-3', 'local:pt:BR:LIA_1183B566 021-4', 'local:pt:BR:LIA_1183B566 021-5', 'local:pt:BR:LIA_1183B566 021-6', 'local:pt:BR:LIA_1183B566 021-9', 'local:pt:BR:LIA_1183C102 751-1']

## Contrato de execução
- Este artefato não autoriza execução sozinho.
- Qualquer delete/update/feed/app/Shopify/local inventory ainda exige aprovação atual do Lucas por pacote.
- O rollback privado guarda o recurso Merchant/status atual por product ID para restauração caso uma ação aprovada precise ser revertida.

## Não executado
- delete
- insert
- update
- custombatch
- fetchNow
- shopify_write
- feed_write
- database_write
- campaign_or_external_send
- local_inventory_disable
- gmb_update
- pos_inventory_write
