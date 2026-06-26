# HEARTBEAT — LK Shopify Hermes

## Status inicial

- Documentação Brain: preparada.
- Runtime/profile: pendente de ativação porque ações de terminal/runtime foram bloqueadas pelo guardrail da sessão atual.
- Bot Telegram: token fornecido por Lucas, mas não deve ser registrado em docs.

## Cadência operacional futura

- Silent-OK: não enviar recibo de sucesso recorrente.
- Alertar apenas falha, bloqueio, decisão necessária ou risco.
- Após execução aprovada, registrar receipt + rollback + evidência no Brain.

## Verificações quando ativado

- `getMe` do Telegram OK sem imprimir token.
- Gateway do profile `lk-shopify` conectado.
- Main Hermes não re-tokenado/reiniciado.
- API/webhook desabilitados para evitar conflito.
- Watchdog silent-OK testado.