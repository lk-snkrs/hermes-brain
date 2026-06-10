# Decisions and Guardrails — LK WhatsApp Integration Platform

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 6 prioriza frentes LK com alto risco de confundir preview/PRD/histórico com ação externa sensível.

## Guardrails

- Não enviar mensagem, ativar número, importar contatos, automatizar atendimento ou abrir campanha sem aprovação.
- `Bloquear preço, disponibilidade, reserva, negociação, reclamação, fornecedor, bulk/campanha/logística sem fonte/aprovação.`
- WhatsApp é canal externo sensível; preview local não implica envio.
- `Distinguir Chatwoot/Elle de wacli/OpenClaw e de Mordomo.`
