# PRD — Mordomo OS Context Intelligence antes de follow-up

Data: 2026-06-07
Status: aprovado para implementação local segura
Owner: Mordomo OS
Escopo: WhatsApp pessoal de Lucas, Zipper follow-ups, Decision Inbox e sugestões de resposta

## 1. Problema

O Mordomo OS ainda pode tratar um item marcado como follow-up como retomada genérica, mesmo quando a conversa real já mostra um estágio mais avançado. Exemplo corrigido por Lucas: José Luzada já demonstrou interesse por uma obra; a próxima ação não é perguntar se ele tem interesse, mas Lucas responder de forma contextual, possivelmente por áudio.

Esse erro cria sugestões ruins, aumenta ruído para Lucas e pode levar a mensagens externas inadequadas se a automação usar apenas intent/status/allowlist sem entender o contexto da conversa.

## 2. Objetivo

Antes de sugerir, alertar ou enviar qualquer follow-up, o Mordomo OS deve ler o contexto recente da conversa e classificar o estágio comercial/operacional real. O sistema deve decidir a ação pelo estágio da conversa, não apenas pelo rótulo `followup`.

## 3. Princípio de produto

Follow-up não é um template. Follow-up é uma decisão contextual.

O Mordomo deve responder a estas perguntas antes de agir:

1. O cliente ainda não respondeu ao PDF/material?
2. O cliente só acusou recebimento e disse que vai avaliar?
3. O cliente já demonstrou interesse por uma obra específica?
4. O cliente perguntou preço, disponibilidade, pagamento, reserva ou condição?
5. Lucas já respondeu ou encerrou a conversa?
6. A próxima ação deve ser mensagem escrita, áudio do Lucas, checagem interna, decisão manual ou silêncio?

## 4. Não objetivos

- Não enviar WhatsApp externo sem passar pelos guardrails existentes.
- Não prometer preço, disponibilidade, reserva, pagamento ou logística sem fonte segura.
- Não substituir Lucas em negociações comerciais sensíveis.
- Não expor telefone/e-mail bruto ou dados pessoais em alertas do Telegram.

## 5. Nova camada: Conversation Intelligence Gate

Criar uma etapa obrigatória antes de `auto_followup_decision`, `strategy_decide_due_followup` e qualquer `due_followup_alert`:

### 5.1 Entradas

- Mensagens recentes do chat, idealmente últimas 24h.
- `last_message_at` do follow-up.
- `last_summary` e `draft_message` existentes.
- Contexto de negócio (`zipper`, `lk`, `spiti`, `pessoal`).
- Intent e risk atuais.
- Sinais de PDF/material/obra/artista.

### 5.2 Saídas

Objeto `conversation_intelligence`:

- `stage`: estágio real da conversa.
- `confidence`: `low`, `medium`, `high`.
- `recommended_action`: ação recomendada.
- `reason`: explicação curta.
- `voice_recommended`: booleano.
- `blocks_generic_followup`: booleano.
- `risk_level`: A0-A4 ajustado se necessário.

### 5.3 Estágios mínimos

- `no_client_reply_after_material`: cliente ainda não respondeu depois do PDF/material; follow-up leve pode fazer sentido.
- `simple_ack_waiting_review`: cliente agradeceu/disse que vai avaliar; auto-ack/follow-up futuro, sem decisão manual.
- `specific_work_interest`: cliente já quer/manifestou interesse em obra específica; bloquear retomada genérica, recomendar resposta contextual de Lucas, muitas vezes por voz.
- `material_question`: preço, disponibilidade, pagamento, reserva, condição, desconto, obra específica com pedido concreto; escalar para Lucas com cuidado.
- `lucas_already_replied`: Lucas respondeu depois do gatilho; marcar como resolvido/respondido.
- `closed_or_declined`: cliente recusou ou Lucas encerrou; não gerar follow-up genérico.
- `ambiguous_needs_context`: contexto insuficiente; não enviar automaticamente, pedir revisão/contexto.

## 6. Regras de decisão

1. Se `stage=specific_work_interest`:
   - Não sugerir mensagem genérica de interesse.
   - Não auto-enviar follow-up.
   - Sugerir: “Lucas, responder contextual/pessoal; áudio recomendado se a conversa pede tom consultivo.”
   - `voice_recommended=true`.

2. Se `stage=material_question`:
   - Bloquear envio automático.
   - Escalar para Lucas com fonte e cuidado.

3. Se `stage=no_client_reply_after_material`:
   - Follow-up leve permitido, mantendo guardrails atuais.

4. Se `stage=simple_ack_waiting_review`:
   - Auto-ack curto ou follow-up futuro, sem alerta manual.

5. Se `stage=lucas_already_replied`:
   - Suprimir alerta e marcar respondido.

6. Se contexto não foi lido:
   - Falhar fechado. Não enviar nem sugerir rascunho definitivo.

## 7. UX/alertas para Lucas

Quando houver sugestão, o alerta deve mostrar:

- O que aconteceu: resumo da conversa real.
- Estágio: ex. “cliente já demonstrou interesse por obra específica”.
- Próxima ação: ex. “mandar áudio contextual”.
- Cuidado: preço/disponibilidade/reserva só com fonte.
- Sugestão: não deve parecer template genérico.

## 8. Critérios de aceite

- Um caso com texto “quero essa obra”, “tenho interesse nessa obra”, “gostei dessa obra”, “quero ficar com ela” não passa como follow-up genérico.
- O teste de regressão prova que `specific_work_interest` gera `alert_lucas`, `voice_recommended=true`, `allow_external_send=false` e draft sem pergunta genérica de interesse.
- Casos sem resposta do cliente após PDF continuam podendo seguir follow-up automático seguro.
- Casos com preço/disponibilidade/pagamento/reserva continuam escalando.
- Testes `test_mordomo*.py` e `py_compile` passam.

## 9. Implementação inicial segura

Fase 1, local e sem envio externo:

1. Adicionar helper determinístico `infer_conversation_intelligence` no watcher.
2. Integrar no `strategy_decide_due_followup` antes da decisão de follow-up Zipper.
3. Bloquear follow-up genérico quando `specific_work_interest` for detectado.
4. Ajustar alerta para recomendar áudio/resposta contextual quando aplicável.
5. Cobrir com teste de regressão.

## 10. Futuro

- Evoluir de regras determinísticas para classificador híbrido com LLM, mas só depois de fixture dataset e logs auditáveis.
- Salvar estágio no CRM/Customer 360.
- Mostrar “próxima melhor ação” por conversa no Dashboard.
- Criar fila de “responder por voz” separada de follow-ups automáticos.
