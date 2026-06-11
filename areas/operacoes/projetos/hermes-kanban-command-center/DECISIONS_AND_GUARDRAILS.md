# Decisions and Guardrails — Hermes Kanban Command Center

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 10 prioriza Zipper/SPITI/Kanban, onde preview documental pode ser confundido com ação externa ou runtime.

## Guardrails

- Não ativar workers, profiles, crons ou comandos Telegram sem aprovação escopada.
- Subagentes devem respeitar contexto mínimo, fonte viva e guardrails do domínio dono.
- Kanban não autoriza write externo por si só; ação sensível continua bloqueada.
- Doppler-first para credenciais e sem impressão de secrets.
