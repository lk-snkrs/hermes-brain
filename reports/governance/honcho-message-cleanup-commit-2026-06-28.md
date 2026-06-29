# Honcho message-level cleanup COMMIT — 2026-06-28

## Escopo aprovado

Lucas aprovou o approval packet de COMMIT para limpeza message-level de contaminação histórica no Honcho. Execução feita com snapshot rollback existente, migrator transacional, preflight e readback pós-commit.

## Resultado

| Item | Status |
|---|---:|
| Snapshot rollback existente | OK |
| Preflight imediatamente antes | OK |
| COMMIT transacional | OK |
| Readback pós-commit | OK |
| Auditor quality Honcho | OK |
| Gateway health pós-commit | OK |
| Raw content/PII/IDs crus impressos | não |
| Secrets impressos | não |
| Workspace reset | não |
| Gateway/runtime restart | não |

## Preflight antes do COMMIT

| Métrica | Valor |
|---|---:|
| Candidate IDs | 173 |
| Matched messages | 173 |
| Distinct sessions | 173 |
| Distinct peers | 1 |
| Direct message embeddings | 173 |
| Direct queue rows | 0 |
| Document source refs | 0 |
| Messages workspace total antes | 12102 |
| Embeddings workspace total antes | 12102 |
| Queue unprocessed workspace antes | 8410 |

## COMMIT/readback

| Métrica | Valor |
|---|---:|
| Deleted queue rows | 0 |
| Deleted messages | 173 |
| Remaining matched messages | 0 |
| Remaining matched embeddings | 0 |
| Remaining matched queue rows | 0 |
| Messages workspace total depois | 11929 |
| Embeddings workspace total depois | 11929 |
| Queue unprocessed workspace depois | 8410 |

## Validações pós-commit

- Re-run do migrator contra o mesmo private map: `matched_message_count=0`.
- Honcho memory quality auditor: `status=ok`, `score=92`, `raw_session_ids_printed=false`.
- Gateway health: `status=ok`, versão `0.17.0`.
- Honcho API logs recentes: sem `ObserverException`, sem `Traceback`, sem erro de FK detectado; raw logs não impressos.
- Artifact scan: sem secret assignment hits, `values_printed=false`.

## Residual observado

Após remover os 173 candidatos originais, o exporter sanitizado ainda encontrou `52` candidatos residuais em novas posições de busca. Isso é esperado em limpeza por ranking/search: ao remover o primeiro lote, resultados mais antigos/menos ranqueados aparecem. Não removi esse segundo lote porque ele não fazia parte do private map aprovado para COMMIT.

## Artefatos

- Migrator: `/opt/data/scripts/honcho_message_cleanup_migrator.py`
- JSON COMMIT: `reports/memory-hygiene/honcho-message-cleanup-migrator-commit-2026-06-28.json`
- JSON dry-run pós-commit: `reports/memory-hygiene/honcho-message-cleanup-migrator-dry-run-2026-06-28.json`
- Snapshot rollback: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z`
- Private map usado: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z/private/honcho_cleanup_candidate_private_id_map.json`

## Veredito

A limpeza aprovada foi executada com sucesso: **173 mensagens contaminadas e 173 embeddings associados removidos**, com readback zero para o lote aprovado.

Próximo passo opcional: rodar uma nova etapa de snapshot/readiness/dry-run para os `52` candidatos residuais antes de qualquer segundo COMMIT.
