# Honcho provider snapshot + cleanup readiness — 2026-06-28

## Escopo aprovado

Lucas aprovou seguir com a etapa segura do packet: snapshot/rollback + confirmação de granularidade + dry-run sanitizado.

## Resultado

| Item | Status |
|---|---:|
| Snapshot lógico PostgreSQL do Honcho | OK |
| Smoke de leitura do gzip | OK |
| SHA256 do artefato | OK |
| Granularidade de delete confirmada | OK |
| Dry-run sanitizado | OK |
| Raw content impresso | não |
| Raw IDs impressos | não |
| Secrets impressos | não |
| Honcho deletion/mutation | não |
| Workspace reset | não |
| Gateway/runtime restart | não |
| Writes externos | 0 |

## Snapshot / rollback

- Backup local: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z`
- Manifest: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z/MANIFEST.json`
- Artefato: `honcho_pg_dumpall.sql.gz`
- Tamanho: `263192576` bytes
- Smoke gzip: OK
- Checksum: `SHA256SUMS`
- `raw_sql_printed=false`
- `values_printed=false`

Rollback futuro, se necessário, exige aprovação separada: restaurar o dump em janela controlada e validar Honcho `/health`, `hermes memory status`/probe equivalente, busca controlada e watchdogs.

## Granularidade confirmada

| Nível | Suporte | Observação |
|---|---:|---|
| `message_delete` via SDK público | não | `Message` não expõe delete; `Session.update_message` só atualiza metadata |
| `session_delete` via SDK público | sim | `Session.delete()` apaga sessão e dados associados; blast radius maior |
| `session_peer_remove` via SDK público | sim | Remove peer da sessão, não resolve conteúdo histórico sozinho |
| `conclusion_delete` via SDK público | sim | `ConclusionScope.delete(conclusion_id)` |
| `workspace_delete` via SDK público | sim | amplo demais; fora do escopo |
| message-level delete via DB | tecnicamente possível | exige migrator DB-level + readback + aprovação separada |

## Dry-run sanitizado

- Plano público hash-only: `reports/memory-hygiene/honcho-cleanup-readiness-dry-run-2026-06-28.json`
- State latest: `/opt/data/state/honcho-cleanup-candidates/cleanup-readiness-dry-run-latest.json`
- Candidate count: `173`
- Private exact-ID map local/restrito: `/opt/data/backups/honcho-provider-snapshot-20260628T200831Z/private/honcho_cleanup_candidate_private_id_map.json`
- Permissão do private map: `0600`
- Private map guarda IDs exatos para futura execução aprovada, mas **não guarda raw content**.
- `raw_content_printed=false`; `raw_ids_printed=false`; `values_printed=false`.

## Veredito

`safe_to_delete_now=false`.

Motivo: agora existe snapshot e a granularidade foi confirmada, mas o SDK público não oferece delete por mensagem. A limpeza destrutiva precisa escolher entre:

1. apagar sessões inteiras contaminadas, se blast radius for aceitável; ou
2. criar um migrator DB-level message-delete, com SQL transacional, readback e rollback testado.

Recomendação: **não apagar sessão inteira por enquanto**. Próximo passo mais seguro é aprovar somente um migrator DB-level em modo `--dry-run --readback`, ainda sem commit, para provar exatamente quais linhas seriam afetadas (`messages`, `message_embeddings`, `queue`/derivados) antes de qualquer delete real.

## Non-actions

- Nenhum deletion Honcho.
- Nenhum reset de workspace.
- Nenhum restart de gateway/runtime.
- Nenhum Docker/VPS/Traefik change além de `docker exec/cp` para snapshot lógico autorizado.
- Nenhum raw content, PII, IDs crus ou secrets impressos.
