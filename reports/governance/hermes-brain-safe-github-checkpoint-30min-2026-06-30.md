# Hermes Brain safe GitHub checkpoint 30min

Data: 2026-06-30

## Decisão

Lucas aprovou implementar a recomendação do Bruno: checkpoint GitHub do Hermes Brain a cada 30 minutos.

Implementação escolhida: **safe checkpoint**, não `git add .` bruto.

## O que foi executado agora

1. Auditoria do working tree do Brain.
2. Dry-run programático da allowlist do `brain_sync_safe.py`.
3. Sync imediato com `brain_sync_safe.py --push --verbose`.
4. Criação do wrapper no-agent silent-OK:
   - `/opt/data/scripts/brain_sync_safe_30min_checkpoint.sh`
5. Criação do cron:
   - job id: `ec0473a3a010`
   - nome: `Hermes Brain safe GitHub checkpoint 30min`
   - schedule: `*/30 * * * *`
   - deliver: `local`
   - no_agent: `true`
6. Smoke manual do wrapper: `rc=0`, stdout/stderr vazios.

## Resultado do dry-run inicial

| Métrica | Resultado |
|---|---:|
| Changed total | `1848` |
| Allowed pela allowlist | `172` |
| Skipped | `1676` |
| Secret findings nos allowed | `0` |

Principais motivos de skip:

| Motivo | Quantidade |
|---|---:|
| `not_in_allowlist` | `1377` |
| `suffix_not_allowed` | `251` |
| `deny_suffix` | `28` |
| `too_large` | `5` |
| `deny_part` | `15` |

## Commit/push imediato

Commit criado e publicado:

```text
916c96dc24d59ad4b1aa6062ac52be01a06508f1
2026-06-30T01:16:19Z
docs: sync Hermes Brain daily consolidation 2026-06-30
```

Verificação Git:

```text
HEAD...origin/main = 0 ahead / 0 behind
```

Working tree pós-sync ainda possui itens locais fora da allowlist:

```text
1676 entradas
```

Isso é esperado: backups, DBs, HTML, stdout/stderr, dumps, artefatos grandes e paths não-canonizados não entram no checkpoint automático.

## Wrapper 30min

Arquivo:

`/opt/data/scripts/brain_sync_safe_30min_checkpoint.sh`

Gates antes de push:

- branch atual precisa ser `main`;
- remote precisa ser `https://github.com/lk-snkrs/hermes-brain.git`;
- `git diff --check` precisa passar;
- `python3 scripts/brain_health_check.py` precisa passar;
- `brain_sync_safe.py --push` aplica allowlist + tamanho máximo + secret scan + branch guard;
- stdout vazio quando OK;
- falhas imprimem só erro sanitizado.

Smoke manual:

```text
rc=0
stdout_bytes=0
stderr_bytes=0
```

## Cron criado

```text
job_id: ec0473a3a010
name: Hermes Brain safe GitHub checkpoint 30min
schedule: */30 * * * *
deliver: local
no_agent: true
script: brain_sync_safe_30min_checkpoint.sh
```

## Guardrails

- Não faz `git add .`.
- Não comita arquivos fora da allowlist.
- Não comita `.db`, `.env`, `.key`, HTML, PDFs, imagens, caches, backups `.before`, scripts/configs fora de escopo e arquivos grandes.
- Não imprime token/GitHub PAT/Doppler/token Telegram.
- Não cria PR nem merge.
- Não reinicia runtime.
- Não toca Docker/VPS/Traefik.
- Não altera dados externos exceto o push GitHub do repositório aprovado.

## Status final

O Hermes Brain agora tem:

- sync imediato publicado em GitHub;
- checkpoint seguro a cada 30 minutos;
- silent-OK quando saudável;
- falha acionável se branch, remote, health, diff, allowlist ou secret scan bloquear.
