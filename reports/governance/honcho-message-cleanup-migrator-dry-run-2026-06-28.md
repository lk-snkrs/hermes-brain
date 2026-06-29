# Honcho message-level cleanup migrator dry-run/readback — 2026-06-28

## Escopo aprovado

Lucas aprovou a próxima etapa segura após snapshot/readiness: criar e executar migrator DB-level somente em `--dry-run --readback`, sem commit/delete.

## Resultado

| Item | Status |
|---|---:|
| Script migrator criado | OK |
| `py_compile` | OK |
| Dry-run/readback executado | OK |
| Commit guard testado | OK — bloqueia |
| Delete/COMMIT executado | não |
| Raw content impresso | não |
| Raw IDs impressos | não |
| Secrets impressos | não |
| Gateway health pós-run | OK |

## Artefatos

- Script: `/opt/data/scripts/honcho_message_cleanup_migrator.py`
- JSON do dry-run: `reports/memory-hygiene/honcho-message-cleanup-migrator-dry-run-2026-06-28.json`
- State latest: `/opt/data/state/honcho-cleanup-candidates/message-cleanup-migrator-dry-run-latest.json`
- Snapshot usado: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z/honcho_pg_dumpall.sql.gz`
- Private map usado: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z/private/honcho_cleanup_candidate_private_id_map.json`

## Blast radius calculado

| Métrica | Valor |
|---|---:|
| Candidate IDs | 173 |
| Matched messages | 173 |
| Match rate | 100% |
| Distinct sessions | 173 |
| Distinct peers | 1 |
| Direct message embeddings | 173 |
| Direct queue rows | 0 |
| Document source refs | 0 |
| Messages workspace total antes | 12100 |
| Embeddings workspace total antes | 12100 |
| Queue unprocessed workspace antes | 8409 |

## Interpretação

O dry-run encontrou 173 mensagens contaminadas e 173 embeddings diretos. Não encontrou queue rows diretos nem document source refs para esses candidatos.

Isso torna a limpeza message-level tecnicamente mais segura do que apagar sessões inteiras, porque cada candidato está distribuído em uma sessão distinta (`173` sessões) e apagar sessões inteiras teria blast radius maior.

## Guardrails ativos

- O script roda em modo read-only por padrão.
- `--commit` sem approval reference é bloqueado.
- Mesmo com approval reference, o script atual ainda bloqueia commit destrutivo e exige etapa separada/revisada.
- O relatório público é hash-only e não imprime IDs crus/conteúdo.

## Veredito

`safe_to_commit_now=false`.

Motivo: etapa aprovada era somente dry-run/readback. Para delete real, precisa nova aprovação explícita para uma versão commit do migrator com:

1. SQL transacional;
2. delete order documentada;
3. readback antes/depois;
4. rollback pelo snapshot já criado;
5. execução preferencialmente em janela curta e monitorada.

## Non-actions

- Nenhum `DELETE` executado.
- Nenhum `COMMIT` executado.
- Nenhum reset de workspace.
- Nenhum restart de gateway/runtime.
- Nenhum raw content, PII, ID cru ou secret impresso.
