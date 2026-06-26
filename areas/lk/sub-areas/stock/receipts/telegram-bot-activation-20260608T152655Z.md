---
title: LK Stock Telegram Bot Activation Receipt
date: 2026-06-08T15:26:55Z
area: lk/stock
status: active-awaiting-user-roundtrip
secret_values_printed: false
external_writes: 0
runtime_writes: local-profile-only-plus-doppler-secret-name
---

# LK Stock Telegram Bot Activation Receipt

## Resultado

O perfil Hermes `lk-stock` foi promovido de preparado/parado para gateway Telegram ativo.

## Bot

- Bot API `getMe`: OK.
- Bot username retornado pelo Telegram: `@lk_contentbot`.
- Bot first name retornado pelo Telegram: `[LK] Stock`.
- Secret usado no Doppler: `LK_STOCK_TELEGRAM_BOT_TOKEN`.
- Valor do token: não registrado neste receipt, Brain, `.env` ou logs intencionais.

## Perfil

- HERMES_HOME: `/opt/data/profiles/lk-stock`.
- Gateway: running.
- API server: disabled.
- Webhook: removed/disabled for this profile.
- Allowlist Telegram: Lucas private user id only.
- Token runtime: injected from Doppler by `/opt/data/scripts/lk_stock_gateway_launcher.sh`.
- `.env`: no `TELEGRAM_BOT_TOKEN` value stored.

## Correções aplicadas durante ativação

- Removida rota webhook herdada do clone do perfil para evitar tentativa de carregar `crisp-lk-canary`.
- Removida linha vazia `TELEGRAM_BOT_TOKEN=` do `.env`, pois ela sobrescrevia o token injetado em runtime.
- Removidos backups herdados do clone/sanitização que poderiam conter secrets antigos.

## Validação executada

- `telegram_getMe=OK` para o token recebido.
- Doppler secret `LK_STOCK_TELEGRAM_BOT_TOKEN` presente.
- Gateway log final: `Connected to Telegram (polling mode)`.
- Gateway log final: `Gateway running with 1 platform(s)`.
- `gateway_state.json`: `gateway_state=running`, `platforms=telegram`, `telegram_state=connected`, `webhook_present=False`.
- Processo vivo com `HERMES_HOME=/opt/data/profiles/lk-stock`.
- Processo vivo com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false`.
- Smoke test CLI do modelo no perfil: respondeu `LK Stock smoke OK`.
- Probe outbound enviada para Lucas no Telegram do bot; round-trip inbound ainda depende de Lucas responder no bot.
- Focused secret scan final: `focused_files_scanned=18`, `focused_secret_hits=0`.

## Não autorizado / não executado

- Sem writes Tiny.
- Sem writes Shopify.
- Sem cron novo.
- Sem webhook público.
- Sem API server.
- Sem Docker/VPS/Traefik.
- Sem contato com cliente/fornecedor.
