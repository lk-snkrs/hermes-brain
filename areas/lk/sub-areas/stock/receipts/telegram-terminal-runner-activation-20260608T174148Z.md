---
title: LK Stock Telegram Terminal Runner Activation Receipt
date: 2026-06-08T17:41:48Z
area: lk/stock
status: active
secret_values_printed: false
external_writes: 0
runtime_writes: local-profile-only
---

# LK Stock Telegram Terminal Runner Activation Receipt

## Resultado

Ativado no perfil `lk-stock` o uso de runner/terminal no Telegram para validações locais do próprio agente.

## Configuração aplicada

`platform_toolsets.telegram` agora inclui:

- `skills`
- `session_search`
- `file`
- `cronjob`
- `clarify`
- `terminal`
- `code_execution`
- `todo`

## Escopo autorizado

Permitido:

- executar `python -m unittest`;
- executar `python -m pytest`/`pytest` quando disponível no runtime Hermes;
- rodar validações locais, testes offline e scripts do próprio `lk-stock`.

Bloqueado sem aprovação escopada:

- writes Tiny;
- writes Shopify/POS/Merchant/Klaviyo/Meta;
- contato externo;
- secrets em stdout/log/Brain;
- Docker/VPS/Traefik/Main Hermes.

## Validação executada

- Gateway `lk-stock` reiniciado isoladamente.
- `gateway_state=running`.
- `telegram_state=connected`.
- `webhook_present=False`.
- Processo vivo com `HERMES_HOME=/opt/data/profiles/lk-stock`.
- Processo vivo com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false`.
- `python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'`: 11 testes OK.
- `/opt/hermes/.venv/bin/python -m pytest areas/lk/sub-areas/stock/evaluation -q`: 11 passed.
- PATH do launcher `lk-stock`: `python -m pytest areas/lk/sub-areas/stock/evaluation -q`: 11 passed.

## Observação

`/usr/bin/python3 -m pytest` não possui módulo `pytest`; o runner validado é o Python do runtime Hermes, que é o usado no PATH do launcher do `lk-stock`.
