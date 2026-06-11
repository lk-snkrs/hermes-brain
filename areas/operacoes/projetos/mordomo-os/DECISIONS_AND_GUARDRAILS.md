# Decisions and Guardrails — Mordomo OS

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Criado como Onda 2 local/documental, preservando originais.

## Guardrails

- `Follow-up simples/verificado pode ser autônomo conforme política ativa; preço, disponibilidade, reserva, negociação, reclamação, fornecedor, bulk/campanha exigem fonte/aprovação.`
- Não alterar cron, gateway, Docker, VPS, profile ou runtime sem aprovação escopada.
- Não enviar mensagem externa a partir deste hub; hub é camada documental.
- `Antes de afirmar ativo, verificar runtime/cron vivo.`
