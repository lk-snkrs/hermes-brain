# Brain OS — Manifest Standard

## Objetivo

Cada hub canônico deve ter `manifest.json` para permitir auditoria automática.

## Campos mínimos

```json
{
  "schema": "brain_os_project_manifest_v1",
  "project_id": "slug",
  "title": "Nome humano",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "owner_area": "areas/...",
  "hub_path": "areas/.../projetos/slug",
  "mode": "canonical_index_preserve_originals",
  "external_writes": false,
  "source_of_truth": ["..."],
  "guardrails": ["..."],
  "artifact_count": 0,
  "artifact_sample": ["relative/path.md"],
  "required_files": ["README.md", "CURRENT_STATE.md", "DECISIONS_AND_GUARDRAILS.md", "ARTIFACT_INDEX.md", "TIMELINE.md", "NEXT_STEPS.md"]
}
```

## Regras

- `external_writes` deve ser `false` para hubs documentais.
- `artifact_sample` deve usar paths relativos e sanitizados.
- Não incluir tokens, IDs secretos, payloads sensíveis ou dados pessoais desnecessários.


## Semântica por caminho

- `areas/**/projetos/*/manifest.json`: candidato a hub canônico vivo, desde que o pacote mínimo exista.
- `reports/**`, `receipts/**`: evidência/receipt; exige reconciliação antes de virar estado atual.
- `backups/**`: snapshot/rollback; nunca é fonte ativa.
- `scripts/**` ou `work/**`: artefato operacional; indexável, mas não hub vivo por padrão.

Ver `MANIFEST_SEMANTICS.md` para regras de precedência.
