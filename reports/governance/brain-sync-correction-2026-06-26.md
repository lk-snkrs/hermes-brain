# Correção — Brain Sync não alimentar branch errado

Data UTC: 2026-06-26

## Pedido

Lucas pediu: `corrigir sync do Brain` após diagnóstico de que o Hermes Brain estava sendo salvo localmente e sincronizado no branch `consolidation/brain-filesystem-git-hygiene-20260516`, enquanto o `main` do GitHub `lk-snkrs/hermes-brain` estava parado desde 2026-06-11.

## Correção aplicada agora

Foi aplicada uma trava local no executor aprovado:

```text
/opt/data/scripts/brain_sync_safe.py
```

A rotina automática agora bloqueia commit/push quando o checkout operacional não está no branch canônico esperado (`main` por padrão, ou `BRAIN_SYNC_TARGET_BRANCH` se definido).

Comportamento verificado:

```text
python3 /opt/data/scripts/brain_sync_safe.py --dry-run --verbose
```

retorna código `5` e mensagem sanitizada:

```text
ERROR: Brain sync blocked: current branch 'consolidation/brain-filesystem-git-hygiene-20260516' is not canonical target 'main'. Refusing to commit/push silently to the wrong GitHub branch.
```

O modo manual de exceção existe, mas é break-glass explícito:

```text
--allow-noncanonical-branch
```

Com ele, o dry-run preserva o comportamento antigo e mostrou `allowed_files: 57`.

## Backup / rollback

Backup antes da alteração:

```text
/opt/data/backups/brain-sync-fix-20260626T094444Z/brain_sync_safe.py.before
/opt/data/backups/brain-sync-fix-20260626T094444Z/cron_jobs.json.before
```

Rollback local do script, se necessário:

```bash
cp /opt/data/backups/brain-sync-fix-20260626T094444Z/brain_sync_safe.py.before /opt/data/scripts/brain_sync_safe.py
python3 -m py_compile /opt/data/scripts/brain_sync_safe.py
```

## Reconciliation attempt

Foi criado worktree limpo de reconciliação:

```text
/opt/data/hermes-brain-sync-reconcile-20260626
```

Base: `origin/consolidation/brain-filesystem-git-hygiene-20260516` em `78a2ce70dea0`.

Ao tentar `git merge --no-commit --no-ff origin/main`, a fusão gerou 67 conflitos, principalmente em manifests/hubs Brain OS e alguns índices:

- `CHANGELOG.md`
- `areas/lk/sub-areas/growth/MAPA.md`
- múltiplos `manifest.json` em hubs de projeto
- `reports/governance/brain-os/brain-os-candidates-latest.json`
- `scripts/brain_os_scanner.py`

A fusão foi abortada/resetada no worktree auxiliar; nenhum merge foi commitado.

## Estado final

- O sync automático não deve mais continuar publicando silenciosamente no branch de consolidação.
- O `main` ainda não foi reconciliado, porque a reconciliação segura exige resolver 67 conflitos.
- Nenhum push GitHub foi feito nesta correção.
- Nenhum secret foi impresso.
- Nenhum cron registry foi modificado.
- Nenhum runtime/Docker/VPS/Shopify/Tiny foi alterado.

## Próximo passo necessário

Abrir uma frente de reconciliação protegida para resolver os 67 conflitos entre:

```text
origin/main
origin/consolidation/brain-filesystem-git-hygiene-20260516
```

Somente depois disso o Brain Sync deve voltar a publicar no branch canônico `main` ou em fluxo PR→merge aprovado.
