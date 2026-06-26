# Receipt — LK Stock no watchdog global de revival

- Data: 2026-06-08T19:00Z
- Escopo: `/opt/data/profiles/lk-stock` apenas.
- Pedido: colocar `lk-stock` no sistema de proteção/revival dos agentes quando o gateway/Main reinicia.

## Pré-estado

- `lk-stock` não tinha gateway vivo após restart.
- `gateway_state.json` antigo mostrava PID stale e estado `draining`.
- O watchdog global `/opt/data/scripts/hermes_all_gateway_watchdog.py` não incluía `lk-stock` no roster `EXPECTED`.

## Correção aplicada

- Adicionado `lk-stock` ao roster `EXPECTED` do watchdog global como `mode=managed`.
- `home`: `/opt/data/profiles/lk-stock`.
- `max_iterations`: `50`.
- `doppler_profile`: `lk-stock`.
- Como a credencial no Doppler existe sob alias específico, adicionado mapeamento runtime-only:
  - de `LK_STOCK_TELEGRAM_BOT_TOKEN`
  - para `TELEGRAM_BOT_TOKEN`
- O mapeamento acontece apenas no processo filho iniciado pelo watchdog, sem copiar secret para `.env`, Brain, logs ou Telegram.

## Backup / rollback

- Backup do watchdog antes da alteração:
  - `/opt/data/backups/runtime/hermes_all_gateway_watchdog.py.pre-lk-stock-20260608T185628Z.bak`
- Rollback: restaurar esse backup para `/opt/data/scripts/hermes_all_gateway_watchdog.py` e encerrar/reiniciar somente o gateway `lk-stock` se necessário.

## Verificação

- `python3 -m py_compile /opt/data/scripts/hermes_all_gateway_watchdog.py`: OK.
- Execução manual do watchdog: stdout vazio, conforme contrato silent-OK.
- Processo vivo final:
  - `HERMES_HOME=/opt/data/profiles/lk-stock`
  - `gateway_state=running`
  - `telegram_state=connected`
  - `API_SERVER_ENABLED=false`
  - `WEBHOOK_ENABLED=false`
  - `API_SERVER_KEY` ausente
  - `WEBHOOK_SECRET` ausente
  - `DOPPLER_TOKEN` ausente no processo filho
- Writes externos: `0`.
- Valores de secrets impressos: `false`.

## Observação

O primeiro start pós-patch subiu sem `TELEGRAM_BOT_TOKEN` porque o secret Doppler estava presente como alias específico `LK_STOCK_TELEGRAM_BOT_TOKEN`. O processo ruim foi encerrado e o watchdog subiu novo processo com alias mapeado corretamente.
