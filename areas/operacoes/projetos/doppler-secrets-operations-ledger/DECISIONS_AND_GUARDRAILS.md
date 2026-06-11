# Doppler / Secrets Operations Ledger — Decisions and Guardrails

## Decisão Brain OS

Criar um hub canônico para reduzir ambiguidade entre documentação histórica, configuração, runtime vivo e ação externa.

## Guardrails

1. Nunca registrar valores, previews, service-account JSON, refresh tokens, passwords ou tokens; apenas presença/ausência/status sanitizado.
2. Secret existente no Doppler não significa env/runtime injetado; separar secret_exists, doppler_access, runtime_injected e integration_active.
3. Não copiar secrets para Brain, skills, receipts, .env, cron output, Telegram ou logs.
4. Qualquer mudança em launcher/runtime/env exige aprovação escopada, backup/rollback e verificação.
