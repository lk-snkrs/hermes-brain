# Mordomo — separação Strategy/Executor

Data: 2026-05-20
Contexto: aprendizado do Pixel AI Hub / Brainzinho sobre separar agentes por natureza de decisão.

## Decisão operacional

O Mordomo deve separar duas responsabilidades:

1. **Strategy / editorial decision**
   - Entende se faz sentido agir.
   - Classifica contexto, intenção, risco e prioridade.
   - Decide uma ação entre: suprimir, alertar Lucas, marcar como respondido, enviar follow-up seguro já autorizado, criar evento claro, registrar pendência.
   - Não executa efeitos externos diretamente.

2. **Executor / técnico-operacional**
   - Executa apenas a ação decidida pela camada estratégica.
   - Não reinterpretar o significado comercial da conversa.
   - Registra o resultado da execução.
   - Respeita guardrails de envio externo, calendário e risco A3/A4.

## Implementação inicial

Arquivo principal alterado:

- `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`

Mudanças:

- Criado `StrategicDecision` para transportar a decisão explícita.
- Criado `strategy_decide_due_followup(...)` para decidir o que fazer com follow-ups vencidos e pendências WhatsApp.
- Criado `executor_apply_due_followup_decision(...)` para executar a decisão sem reclassificar risco/intenção.
- Criado log auditável PII-minimizado em:
  - `/opt/data/profiles/mordomo/state/mordomo_strategy_executor_audit.jsonl`

## Regra de produto

- Strategy decide “deve agir?”.
- Executor decide apenas “como executar tecnicamente a decisão já tomada?”.
- Se a execução falhar, registrar falha e preservar rascunho/estado.
- Se o caso envolver preço, disponibilidade, Pix, reserva, negociação, reclamação ou resposta substantiva de cliente, strategy deve bloquear follow-up genérico e escalar para Lucas.

## Próximos passos naturais

- Expandir o mesmo padrão para criação automática de eventos de calendário a partir de conversas.
- Expandir o mesmo padrão para e-mail/Zipper draft engine.
- Criar testes de regressão para casos: silêncio pós-PDF, cliente analisando, Pix/preço, recusa cordial, evento com data+hora.
