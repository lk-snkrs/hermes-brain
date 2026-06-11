# Decisions and Guardrails — Zipper Cron Readiness Control

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 10 prioriza Zipper/SPITI/Kanban, onde preview documental pode ser confundido com ação externa ou runtime.

## Guardrails

- `Não criar/ativar cron Zipper sem aprovação escopada, cadência e kill criteria.`
- Cron OK deve ser silencioso; alerta só quando acionável.
- `Não enviar e-mail/WhatsApp/lead follow-up automaticamente sem aprovação.`
- Todo cron precisa rollback, fixture e readback.
