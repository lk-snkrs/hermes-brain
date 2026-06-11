# Decisions and Guardrails — Mesa COO

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Criado como Onda 2 local/documental, preservando originais.

## Guardrails

- `Telegram só com decisão/alerta acionável; sem wrapper/job_id/JSON/ruído técnico.`
- `Mesa COO não envia e-mail/WhatsApp nem toma decisão sensível sem aprovação.`
- `Preservar decisões do Lucas como ledger/contexto; não inferir aprovação por histórico fraco.`
- Se Lucas diz “não fazer”, registrar como estado e não executar.
