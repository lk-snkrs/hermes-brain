# Decisão — Crisp grande cérebro via Plugin, não Hugo — 2026-05-21

## Decisão

Lucas confirmou: o grande cérebro de resposta do Crisp deve ser feito **via Crisp Marketplace Plugin / Hermes Brain**, e **não via Hugo** como núcleo da automação.

## Interpretação operacional

- O Crisp Plugin será a camada oficial de integração com o Crisp.
- Hermes/Brain será a fonte de verdade para decisão, contexto, guardrails e resposta.
- Hugo não entra no MVP como motor principal.
- Token Hugo / Workflow API permanece pendente apenas como possibilidade futura, se Lucas pedir explicitamente.

## Arquitetura alvo

```text
Crisp Chat
  → Plugin Hooks / evento de mensagem
  → Hermes Crisp Gateway
  → Hermes Brain + fontes vivas + regras LK
  → decisão segura
  → REST API Crisp para responder OU escalonamento humano
```

## Guardrails

- Não responder preço, disponibilidade, reserva, status de pedido, reclamação ou negociação sem fonte viva/regra aprovada.
- Escalar para Larissa/humano em sob encomenda/status/entrega/reclamação quando não houver base segura.
- Credenciais ficam no Doppler `lc-keys/prd`; nunca em arquivos locais/logs.
- Não alterar Docker/VPS/gateway produtivo sem plano, rollback e aprovação.

## Próximo passo recomendado

Produzir PRD técnico do Plugin Crisp Hermes com:

1. endpoints;
2. eventos Plugin Hooks;
3. escopos mínimos;
4. fluxo de decisão;
5. API REST de resposta;
6. fila/logs/receipts;
7. modo manual/canary;
8. rollback;
9. plano de teste sem impacto em produção.
