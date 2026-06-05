# LC Mordomo OS — P1.2 Zipper Decision Inbox dry-run

**Data:** 2026-06-05T20:47:18.761618+00:00  
**Escopo:** consultas locais sobre `zipper_canonical.sqlite` para separar decisão real de ruído.  
**Modo:** dry-run local/read-only; nenhum Telegram, WhatsApp, e-mail, Supabase, cron ou infraestrutura alterado.

---

## Resultado executivo

- Candidatos brutos em `decision_packet`: 15
- Telegram-ready reais: 3
- `action_ready_candidate`: 3
- `hard_recipient_blocklist`: 2
- `needs_enrichment`: 1
- `review_before_alert`: 2
- `suppress_followup_noise`: 2
- `technical_error_local`: 5

Interpretação:

- `action_ready_candidate`: pode virar alerta/aprovação ao Lucas, mas ainda deve carregar fonte/draft antes de envio real.
- `suppress_followup_noise`: não deve ir para Decision Inbox; volta para automação/reconciliação de follow-up.
- `technical_error_local`: erro técnico para self-heal local antes de incomodar Lucas.
- `review_before_alert`/`needs_enrichment`: exige enriquecimento local antes de qualquer alerta.

---

## Itens por bucket

### hard_recipient_blocklist — Ivan Grilo

- Status origem: `needs_lucas_decision`
- Intent: `post_pdf_followup`
- Artista: n/a
- Telegram-ready: não
- Por quê: Destinatário bloqueado por regra operacional; nunca deve virar envio/alerta de aprovação comum.
- Ação local recomendada: Manter suprimido; só reabrir se Lucas der exceção explícita no turno atual.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### needs_enrichment — Cássia Olliveira

- Status origem: `needs_lucas_decision`
- Intent: `reply_in_active_thread`
- Artista: n/a
- Telegram-ready: não
- Por quê: Status pede Lucas, mas faltam fonte/draft/risco claros.
- Ação local recomendada: Enriquecer antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### hard_recipient_blocklist — LK Sneakers & Streetwear

- Status origem: `needs_lucas_decision`
- Intent: `post_pdf_followup`
- Artista: n/a
- Telegram-ready: não
- Por quê: Destinatário bloqueado por regra operacional; nunca deve virar envio/alerta de aprovação comum.
- Ação local recomendada: Manter suprimido; só reabrir se Lucas der exceção explícita no turno atual.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### suppress_followup_noise — Marcus Bitencourt

- Status origem: `needs_lucas_decision`
- Intent: `post_pdf_followup`
- Artista: n/a
- Telegram-ready: não
- Por quê: Marcado como decisão, mas parece follow-up seguro; deve voltar para automação A1/A2.
- Ação local recomendada: Reconciliar como follow-up automático ou waiting_client.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### suppress_followup_noise — Brenda

- Status origem: `needs_lucas_decision`
- Intent: `followup_or_interest`
- Artista: n/a
- Telegram-ready: não
- Por quê: Marcado como decisão, mas parece follow-up seguro; deve voltar para automação A1/A2.
- Ação local recomendada: Reconciliar como follow-up automático ou waiting_client.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### action_ready_candidate — Clau Xavier — Adriana Duque

- Status origem: `needs_lucas_decision`
- Intent: `post_pdf_followup`
- Artista: Adriana Duque
- Telegram-ready: sim
- Por quê: Há sinal material/comercial que exige decisão ou resposta aprovada.
- Ação local recomendada: Olá Clau, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
- Fonte follow-up: `mixed:zipper:[phone]:adriana-duque-clau-xavier`

### action_ready_candidate — Camila Paschoalin

- Status origem: `needs_lucas_decision`
- Intent: `post_unavailable_work_alternatives_followup`
- Artista: n/a
- Telegram-ready: sim
- Por quê: Há sinal material/comercial que exige decisão ou resposta aprovada.
- Ação local recomendada: Oi Camila, tudo bem? Só passando para saber se alguma outra obra da seleção te chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### action_ready_candidate — Rafaela Rocha — Rodrigo Braga

- Status origem: `needs_lucas_decision`
- Intent: `post_pdf_followup`
- Artista: Rodrigo Braga
- Telegram-ready: sim
- Por quê: Há sinal material/comercial que exige decisão ou resposta aprovada.
- Ação local recomendada: Olá Rafaela, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.
- Fonte follow-up: `mixed:zipper:[phone]:rodrigo-braga-rafaela-rocha`

### technical_error_local — Contato Zipper

- Status origem: `manual_send_failed`
- Intent: `n/a`
- Artista: n/a
- Telegram-ready: não
- Por quê: Erro técnico local; não é decisão comercial para Lucas até reconciliação.
- Ação local recomendada: Corrigir/reconciliar localmente antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper:history_pdf_followup_failed:20260602`

### technical_error_local — Contato Zipper

- Status origem: `manual_send_failed`
- Intent: `n/a`
- Artista: n/a
- Telegram-ready: não
- Por quê: Erro técnico local; não é decisão comercial para Lucas até reconciliação.
- Ação local recomendada: Corrigir/reconciliar localmente antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper:history_pdf_followup_failed:20260602`

### technical_error_local — Contato Zipper

- Status origem: `manual_send_failed`
- Intent: `n/a`
- Artista: n/a
- Telegram-ready: não
- Por quê: Erro técnico local; não é decisão comercial para Lucas até reconciliação.
- Ação local recomendada: Corrigir/reconciliar localmente antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper:history_pdf_followup_failed:20260602`

### technical_error_local — Contato Zipper

- Status origem: `manual_send_failed`
- Intent: `n/a`
- Artista: n/a
- Telegram-ready: não
- Por quê: Erro técnico local; não é decisão comercial para Lucas até reconciliação.
- Ação local recomendada: Corrigir/reconciliar localmente antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper:history_pdf_followup_failed:20260602`

### technical_error_local — Contato Zipper

- Status origem: `manual_send_failed`
- Intent: `n/a`
- Artista: n/a
- Telegram-ready: não
- Por quê: Erro técnico local; não é decisão comercial para Lucas até reconciliação.
- Ação local recomendada: Corrigir/reconciliar localmente antes de alertar.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper:history_pdf_followup_failed:20260602`

### review_before_alert — Olavo

- Status origem: `due_alerted`
- Intent: `price_or_availability_or_conditions`
- Artista: n/a
- Telegram-ready: não
- Por quê: Pode ser decisão material, mas veio de estado due_alerted; precisa pacote com fonte/draft antes de Telegram.
- Ação local recomendada: Enriquecer fonte e recomendação; não enviar alerta cru.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

### review_before_alert — Alipio

- Status origem: `due_alerted`
- Intent: `price_or_availability_or_conditions`
- Artista: n/a
- Telegram-ready: não
- Por quê: Pode ser decisão material, mas veio de estado due_alerted; precisa pacote com fonte/draft antes de Telegram.
- Ação local recomendada: Enriquecer fonte e recomendação; não enviar alerta cru.
- Fonte follow-up: `whatsapp:pessoal:[email]:zipper`

---

## Próximo passo

Implementar o formatador de pacote action-first apenas para os itens `action_ready_candidate`, com fonte, risco, recomendação e draft. Manter `technical_error_local` e `suppress_followup_noise` fora do Telegram.
