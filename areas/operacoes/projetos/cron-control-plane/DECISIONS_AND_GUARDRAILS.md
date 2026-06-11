# Decisions and Guardrails — Hermes Cron Control Plane

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 9 prioriza governança operacional Hermes onde estado documental pode ser confundido com runtime vivo.

## Guardrails

- `Não criar, alterar, pausar ou remover cron sem aprovação quando houver efeito runtime/externo.`
- `Telegram de Lucas deve receber decisão/exceção/falha/resumo desejado, não ruído operacional.`
- Cron OK deve ficar silencioso; falhas devem explicar causa sanitizada e ação necessária.
- Não imprimir secrets ou dados sensíveis em output de cron.
