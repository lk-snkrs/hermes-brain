# Runtime Truth Reconciler — 2026-06-18

Timestamp: 2026-06-18 11:21 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 40.
- Ativos: 36.
- Pausados: 4.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job: 0 observadas pela listagem resumida.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

Nenhuma anomalia de falha ativa observada: todos os jobs listados com execução registrada têm último status `ok`, e não há erro explícito de delivery na listagem.

Atenção documental/runtime:

- O one-shot `7ef586b9ec1a` — Reanalisar backlog Auto-Remediation em 72h — não aparece mais na evidência viva de 2026-06-18. Em 2026-06-17 ele era o único job ativo sem `Last run`. Tratar como item de reconciliação documental/histórico: não manter como job ativo pendente sem nova evidência viva.
- `2e5bc91d27d6` — Hermes Nightly Operations Audit OS — 02h50 BRT — continua ativo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.

## Mudança de inventário vs 2026-06-17

- Contagem estável: 40 jobs totais / 36 ativos / 4 pausados.
- Nenhum `last_status` não-ok ou delivery error explícito.
- Diferença notável: `7ef586b9ec1a` não aparece mais na listagem viva; o total permaneceu 40, então a reconciliação deve tratar esse one-shot como histórico/removido ou executado/limpo fora deste snapshot, sem inferir causa além da evidência disponível.
- Jobs previamente problemáticos continuam `ok` e não devem permanecer como falha ativa sem nova evidência: `d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`.

## Jobs pausados na evidência viva

- `ac0b440e2643` — Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` — SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

Documentação que ainda descreve esses watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## Jobs com `deliver=origin`

Saídas intencionais/condicionais observadas:

- `749ee30b51eb` — Mesa COO diária Telegram — ativo, `ok`.
- `98478b820720` — Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram — ativo, `ok`.
- `518634d5ea60` — Reminder OS — 2h open-loop watchdog — ativo, `ok`.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — configurado como `origin`, mas pausado.

## Gaps de reconciliação documental

Gaps acionáveis/documentais:

1. Reconciliar o destino histórico do one-shot `7ef586b9ec1a`: ele não está mais vivo em 2026-06-18; remover/baixar de pendência ativa nos docs que ainda o descrevam como ativo sem `Last run`.
2. Documentar/reconciliar `2e5bc91d27d6` em rodada própria, especialmente owner, finalidade e critério de sucesso.
3. Manter documentos de Mordomo/LK Growth/SPITI/LK specialist gateway watchdogs como históricos/pausados até nova evidência viva de reativação.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-18.md`
- `reports/brain-health-check-2026-06-18-runtime-truth-reconciler.json` (resultado final registrado após execução)

## Verificação

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-18-runtime-truth-reconciler.json`: `All checks passed` (`FAIL=0/WARN=0`).
- `git diff --check` escopado aos arquivos tocados nesta execução: ok.
- Secret scan escopado aos arquivos tocados nesta execução: `scoped_possible_secrets 0`.
