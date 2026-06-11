# Decisions and Guardrails — Hermes Runtime Observability

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 9 prioriza governança operacional Hermes onde estado documental pode ser confundido com runtime vivo.

## Guardrails

- Não reiniciar gateway, Docker, VPS, serviço, profile ou container sem aprovação escopada.
- Estado documental não substitui verificação runtime viva antes de afirmar ativação.
- Não expor secrets, tokens, URLs sensíveis ou previews de credenciais.
- `Planos de update/remediation precisam de backup, rollback e verificação antes de execução.`
