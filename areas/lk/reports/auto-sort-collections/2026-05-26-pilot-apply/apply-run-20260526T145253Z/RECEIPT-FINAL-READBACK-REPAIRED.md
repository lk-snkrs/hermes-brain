# Receipt final corrigido — readback pós-apply LK

Readback repair: 2026-05-26T14:54:16Z

## Resultado por coleção

- Nude Project (`nude-project`): applied_and_verified_after_poll_error; moves=79; readback_match=True; esgotados_final=0

- Jacquemus (`jacquemus`): applied_readback_mismatch_after_poll_error; moves=17; readback_match=False; esgotados_final=0
  - first_mismatch_position: 24

- Saint Studio (`saint-studio`): applied_and_verified_after_poll_error; moves=82; readback_match=True; esgotados_final=0

- Calça | Apparels (`calca-streetwear`): applied_readback_mismatch_after_poll_error; moves=68; readback_match=False; esgotados_final=0
  - first_mismatch_position: 20

- Pace (`pace`): applied_and_verified_after_poll_error; moves=75; readback_match=True; esgotados_final=0

- Aimé Leon Dore (`aime-leon-dore`): applied_and_verified_after_poll_error; moves=89; readback_match=True; esgotados_final=0

- Nike Mind (`nike-mind-001`): applied_readback_mismatch_after_poll_error; moves=12; readback_match=False; esgotados_final=0
  - first_mismatch_position: 3

- Onitsuka Tiger Mexico 66 (`onitsuka-tiger-mexico-66`): applied_readback_mismatch_after_poll_error; moves=98; readback_match=False; esgotados_final=0
  - first_mismatch_position: 14

- Onitsuka Tiger Mexico 66 Sabot (`onitsuka-tiger-mexico-66-sabot`): applied_readback_mismatch_after_poll_error; moves=10; readback_match=False; esgotados_final=0
  - first_mismatch_position: 9

- Shorts (`shorts`): applied_readback_mismatch_after_poll_error; moves=24; readback_match=False; esgotados_final=0
  - first_mismatch_position: 10

## Artefatos

- Snapshot rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260526T145253Z/rollback-snapshot-pre-write-immediate.json`
- Receipt JSON corrigido: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260526T145253Z/receipt-final-readback-repaired.json`

## Observação

- As mutations foram enviadas na primeira execução; o erro foi apenas na query de poll do Job. Este arquivo faz readback REST posterior e compara a ordem live contra a ordem proposta.
