# Runtime Truth Reconciler — 2026-05-23

Timestamp: 2026-05-23 11:21 UTC

## Escopo

Reconciliação read-only da evidência viva de crons Hermes com a documentação do Hermes Brain.

## Fonte viva usada

- Tentativa obrigatória: `cronjob list` → indisponível neste shell (`command not found`).
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Nenhum job foi executado manualmente. Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, Shopify, GMC, Notion, WhatsApp, email, campanha, sistema externo ou secret foi alterado.

## Resumo da evidência viva

- Total listado: 23 jobs.
- Ativos: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0.
- Erros explícitos de delivery na listagem: 0.
- Jobs ativos sem `Last run` registrado: 1.

## Jobs ativos sem `Last run`

- `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, weekly, `origin`; acompanhar após a primeira execução semanal registrada.

## Delivery `origin` observado

Sem erro explícito, mas ainda relevante para governança de ruído/visibilidade:

- `LK Daily Sales Brief read-only mandatory delivery` (`7c688553e293`) — `origin`, último status `ok`.
- `LK Weekly CEO Review read-only mandatory delivery` (`953b9055458e`) — `origin`, último status `ok`.
- `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) — `origin`, último status `ok`.
- `Mesa COO diária Telegram` (`749ee30b51eb`) — `origin`, último status `ok`.
- `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — `origin`, sem `Last run` ainda.

Interpretação: não é falha por si só. Ação futura só se Lucas aprovar redução de ruído ou mudança de visibilidade.

## Drift/notas de reconciliação documental

- Contagem mudou em relação ao snapshot de 2026-05-22: `29 total / 23 ativos / 6 pausados` → `23 total / 23 ativos / 0 pausados listados`.
- Jobs pausados antigos citados no inventário anterior não aparecem mais na evidência viva com `--all`; o Brain deve tratá-los como histórico/arquivados até nova evidência viva.
- `Lembrete GMC Data Sources 10h` (`1d3a188b24f2`), ativo/one-shot sem execução no snapshot de 2026-05-22, não aparece mais na listagem viva atual.
- Docs de seções antigas ainda mencionam alguns watchdogs como `origin` quando a evidência viva atual mostra `local`: `Mordomo Telegram gateway watchdog`, `LK Growth Telegram gateway watchdog`, `SPITI Telegram gateway watchdog`, `Hermes runtime + cron watchdog no_agent` e `Hermes compression failure self-heal watchdog`. A seção datada de 2026-05-23 foi adicionada como fonte viva mais recente sem reescrever histórico.

## Gaps acionáveis

1. Atualizar/arquivar referências históricas a jobs pausados que não aparecem mais no `--all`, se a ausência se repetir no próximo ciclo.
2. Acompanhar a primeira execução do `Lucas Brain weekly Learning Loop report`.
3. Revisar, com aprovação de Lucas, se os cinco jobs `origin` devem continuar visíveis no Telegram/origem ou migrar para `local`/silent-OK.

## Verificação

- Health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-23-runtime-truth-reconciler.json` → `All checks passed`.
- Secret scan dos arquivos tocados nesta execução: `possible_secrets 0`.
- `git diff --check` nos arquivos tocados: sem problemas.
