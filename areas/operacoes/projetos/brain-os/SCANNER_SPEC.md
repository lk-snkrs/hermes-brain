# Brain OS — Scanner Spec

## Objetivo

Detectar candidatos a hubs canônicos de forma local/read-only.

## Script

- Cópia operacional: `/opt/data/scripts/brain_os_scanner.py`
- Cópia versionável no Brain repo: `scripts/brain_os_scanner.py`

## Comando

```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain
/opt/hermes/.venv/bin/python scripts/brain_os_scanner.py \
  --root /opt/data/hermes_bruno_ingest/hermes-brain \
  --output reports/governance/brain-os/brain-os-candidates-latest.json
```

## Saída

JSON com:

- `generated_at`;
- `root`;
- `mode=read_only_scan`;
- `scanner_version`;
- `total_text_files_scanned`;
- candidatos com score, wave, risco, owner_area, hubs sugeridos e amostras de artefatos.

## Critérios de score

- volume do owner area;
- quantidade de hits de termos;
- hub existente ou ausente;
- risco externo/fonte viva;
- prioridade da onda.

## Segurança

- Não escreve no Brain exceto quando `--output` é explicitamente passado.
- Não lê binários.
- Não imprime secrets.
- Não chama APIs externas.
- Não altera Git.
