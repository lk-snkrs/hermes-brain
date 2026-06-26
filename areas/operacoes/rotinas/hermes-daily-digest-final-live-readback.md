# Hermes Daily Digest — final live readback before action-needed

- Data: 2026-06-24
- Origem: correção aprovada por Lucas após digest/score tratar `cron_non_ok` Zipper como atenção aberta quando o cron já havia recuperado no estado vivo.
- Escopo: relatório/digest/checklist local; sem writes externos; sem mudança de schedule/delivery; sem Docker/VPS/gateway/secrets.
- values_printed: false

## Regra

O digest diário 03h deve separar **atenção histórica** de **atenção atual**.

Antes de enviar `Status geral: Ação necessária`, ou antes de apresentar uma nota como falha viva, deve fazer um readback final do estado atual:

1. Usar artefatos da madrugada (`reports/nightly-ops-audit/latest.json`, Daily Intelligence, scorecard) como evidência histórica.
2. Reconsultar o estado vivo de crons com `/opt/hermes/.venv/bin/hermes cron list --all`; se indisponível, ler `/opt/data/cron/jobs.json` de forma sanitizada.
3. Para cada `active_cron_non_ok`, `cron_non_ok`, `stale_active_cron_run` ou falha de entrega citada, comparar timestamp/status histórico com o último run vivo.
4. Se houve run posterior `ok`, classificar como `atenção histórica resolvida` e `monitorar próximo run`, não como `Ação necessária`.
5. Se a nota auditada ainda reflete o débito histórico, escrever `score auditado X/100; estado atual recuperado/monitorado`.

## Padrão humano

Ruim:

> Geral: 84/100 — ação necessária por cron Zipper não-ok.

Bom quando o live readback recuperou:

> Geral auditado: 84/100, mas estado atual recuperado. O Zipper falhou ontem, hoje rodou OK; próximo passo é monitorar a próxima janela.

## Zipper/WACLI

Para Zipper vendas 09h, sempre separar:

- geração do relatório;
- e-mail interno obrigatório;
- WhatsApp/WACLI best-effort.

Se e-mail obrigatório passou e WhatsApp/WACLI falhou, reportar como status parcial/canal degradado, não como `cron quebrado` genérico.

## Superfícies atualizadas

- Prompt vivo do cron `Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram`.
- Skill `lucas-hermes-continuous-improvement`, referência `daily-digest-final-live-readback-20260624.md`.
- Este documento canônico no Brain.
