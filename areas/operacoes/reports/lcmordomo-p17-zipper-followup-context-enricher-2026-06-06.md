# LC Mordomo OS — P1.7 Zipper context enricher de follow-ups

**Data:** 2026-06-06T01:37:46.392854+00:00
**Modo:** local/read-only; nenhum Telegram, WhatsApp, e-mail, cron, Supabase, produção ou infraestrutura alterado.
**Objetivo:** enriquecer a fila de follow-ups importantes com contexto local e classificar o próximo passo seguro antes de qualquer executor.

---

## Resultado executivo

- Itens enriquecidos: 5
- `blocked_sensitive_material`: 2
- `needs_lucas_context`: 3
- Envios liberados agora por este passo: 0

Interpretação:

- `blocked_sensitive_material`: contém sinal material/comercial; não enviar sem Lucas.
- `needs_lucas_context`: falta histórico bruto ou há conflito/idempotência; não enviar agora.
- `safe_to_autofollowup_pending_live_idempotency`: só pode ir para executor futuro com checagem live do canal; este report não envia.

---

## Itens

### 1. Rafaela Rocha — Rodrigo Braga — Rodrigo Braga

- Classificação: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Vencimento/fonte local: `2026-05-22T21:22:12-03:00`
- Motivo: fonte local registra conflito ou instrução de revisão humana antes de follow-up
- Próximo passo: Buscar histórico bruto adicional ou pedir contexto pontual ao Lucas; não enviar agora.
- Envio agora: não — P1.7 é enriquecimento local; executor live/idempotente ainda não ativado por este script.
- Contexto local:
  - último resumo: Lead ZPR Chatbot Rodrigo Braga enviado por WhatsApp e e-mail; sem preço/reserva/condições específicas.
  - motivo do bloqueio/autonomia: cliente respondeu depois do PDF/último outbound; não é follow-up normal, Lucas precisa responder
  - próxima ação registrada: cliente respondeu/perguntou; Lucas precisa responder, não enviar follow-up genérico
  - nota do draft: draft Zipper pós-PDF sem resposta; antes de enviar, conferir histórico recente e bloquear se houver preço/disponibilidade/negociação.
  - mensagem/draft atual: Olá Rafaela, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
  - datas locais relevantes: last_manual_sent_at=2026-05-21T00:22:12.740695+00:00; due_at=2026-05-22T21:22:12-03:00; updated_at=2026-05-23T00:22:27.431966+00:00
- Draft preservado localmente:
```
Olá Rafaela, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
```

### 2. Camila Paschoalin — sem artista específico

- Classificação: `blocked_sensitive_material`
- Intent: `post_unavailable_work_alternatives_followup`
- Vencimento/fonte local: `2026-05-23T16:47:44.171903+00:00`
- Motivo: envolve obra indisponível/esgotada ou alternativa comercial; não é follow-up puro
- Próximo passo: Escalar para Lucas com contexto específico antes de qualquer resposta.
- Envio agora: não — P1.7 é enriquecimento local; executor live/idempotente ainda não ativado por este script.
- Contexto local:
  - último resumo: Lucas respondeu que a obra Parque Lage está esgotada, mas explicou condições de pagamento. Follow-up deve buscar vender outras obras disponíveis do PDF, não encerrar o lead.
  - motivo do bloqueio/autonomia: cliente respondeu depois do último outbound ou trouxe preço/disponibilidade/pagamento/negociação; known-answer anexado sem envio externo
  - próxima ação registrada: cliente respondeu/perguntou; Lucas precisa responder, não enviar follow-up genérico
  - nota do draft: draft Zipper para obra esgotada/indisponível: oferecer alternativas do PDF/seleção; bloquear se houver preço, disponibilidade, reserva, condição ou resposta material do cliente.
  - mensagem/draft atual: Oi Camila, tudo bem? Só passando para saber se alguma outra obra da seleção te chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.
  - datas locais relevantes: last_message_at=2026-05-20T13:49:17Z; due_at=2026-05-23T16:47:44.171903+00:00; created_at=2026-05-21T16:47:44.171903+00:00; updated_at=2026-05-23T16:48:18.998009+00:00
- Draft preservado localmente:
```
Oi Camila, tudo bem? Só passando para saber se alguma outra obra da seleção te chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.
```

### 3. Clau Xavier — Adriana Duque — Adriana Duque

- Classificação: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Vencimento/fonte local: `2026-05-24T11:26:00-03:00`
- Motivo: fonte local registra conflito ou instrução de revisão humana antes de follow-up
- Próximo passo: Buscar histórico bruto adicional ou pedir contexto pontual ao Lucas; não enviar agora.
- Envio agora: não — P1.7 é enriquecimento local; executor live/idempotente ainda não ativado por este script.
- Contexto local:
  - último resumo: Lead ZPR Chatbot Adriana Duque enviado por WhatsApp e e-mail em 2026-05-22; sem preço/reserva/condições específicas.
  - motivo do bloqueio/autonomia: cliente respondeu depois do PDF/último outbound; não é follow-up normal, Lucas precisa responder
  - próxima ação registrada: cliente respondeu/perguntou; Lucas precisa responder, não enviar follow-up genérico
  - nota do draft: draft Zipper pós-PDF sem resposta; antes de enviar, conferir histórico recente e bloquear se houver preço/disponibilidade/negociação.
  - mensagem/draft atual: Olá Clau, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
  - datas locais relevantes: due_at=2026-05-24T11:26:00-03:00; updated_at=2026-05-24T14:28:41.581889+00:00
- Draft preservado localmente:
```
Olá Clau, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
```

### 4. Brenda — sem artista específico

- Classificação: `blocked_sensitive_material`
- Intent: `followup_or_interest`
- Vencimento/fonte local: `2026-05-28T18:28:34+00:00`
- Motivo: histórico local contém termo material: preço/disponibilidade/reserva/pagamento/negociação ou equivalente
- Próximo passo: Não enviar; preparar pergunta/pacote específico para Lucas se ainda for atual.
- Envio agora: não — P1.7 é enriquecimento local; executor live/idempotente ainda não ativado por este script.
- Contexto local:
  - último resumo: Boa tarde, tudo bem? Montamos uma apresentação e hoje a tarde vamos passar para o nosso cliente. Assim que tiver resposta te retorno, obrigada!
  - motivo do bloqueio/autonomia: cliente perguntou preço/disponibilidade/pagamento/negociação no histórico recente; bloquear follow-up e escalar
  - próxima ação registrada: cliente respondeu/perguntou; Lucas precisa responder, não enviar follow-up genérico
  - nota do draft: draft genérico; requer revisão contextual antes de envio.
  - mensagem/draft atual: Olá Brenda, tudo bem? Passando para retomar esse ponto.
  - datas locais relevantes: last_message_at=2026-05-28T16:28:34Z; last_sent_at=2026-05-28T13:36:52.664998+00:00; last_auto_sent_at=2026-05-28T13:36:52.664998+00:00; due_at=2026-05-28T18:28:34+00:00; updated_at=2026-05-28T18:39:03.381563+00:00
- Draft preservado localmente:
```
Olá Brenda, tudo bem? Passando para retomar esse ponto.
```

### 5. Marcus Bitencourt — sem artista específico

- Classificação: `needs_lucas_context`
- Intent: `post_pdf_followup`
- Vencimento/fonte local: `2026-06-01T00:40:16.093094+00:00`
- Motivo: fonte local registra conflito ou instrução de revisão humana antes de follow-up
- Próximo passo: Buscar histórico bruto adicional ou pedir contexto pontual ao Lucas; não enviar agora.
- Envio agora: não — P1.7 é enriquecimento local; executor live/idempotente ainda não ativado por este script.
- Contexto local:
  - último resumo: Eu estou interessado. Falamos há algum tempo. Meu nome é Marcus Bitencourt
  - motivo do bloqueio/autonomia: cliente respondeu depois do PDF/último outbound; não é follow-up normal, Lucas precisa responder
  - próxima ação registrada: cliente respondeu/perguntou; Lucas precisa responder, não enviar follow-up genérico
  - nota do draft: draft Zipper pós-PDF sem resposta; antes de enviar, conferir histórico recente e bloquear se houver preço/disponibilidade/negociação.
  - mensagem/draft atual: Olá Marcus, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
  - datas locais relevantes: last_message_at=2026-05-24T19:17:29Z; auto_ack_sent_at=2026-05-30T00:40:16.093015+00:00; last_client_thanks_at=2026-05-30T00:35:14Z; due_at=2026-06-01T00:40:16.093094+00:00; updated_at=2026-06-01T00:42:10.315420+00:00
- Draft preservado localmente:
```
Olá Marcus, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
```

---

## Gate para P1.8

Antes de qualquer envio autônomo, o próximo passo precisa de executor live/idempotente que leia o histórico bruto do mesmo canal, bloqueie termos materiais e registre sent_action de forma idempotente. Este P1.7 não ativa entrega.
