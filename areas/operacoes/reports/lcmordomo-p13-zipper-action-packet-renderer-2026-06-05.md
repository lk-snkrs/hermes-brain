# LC Mordomo OS — P1.3 Zipper action packet renderer

**Data:** 2026-06-05T21:10:19.013233+00:00
**Escopo:** renderização local dos pacotes action-first para os candidatos Zipper validados.
**Modo:** preview local/read-only; nenhum Telegram, WhatsApp, e-mail, Supabase, cron ou infraestrutura alterado.

---

## Resultado executivo

- Pacotes action-first gerados: 3
- Fonte local: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
- Contrato de entrega: prévia local; envio externo bloqueado sem aprovação explícita.

Itens mantidos fora do alerta:
- `hard_recipient_blocklist`: 2
- `needs_enrichment`: 1
- `review_before_alert`: 2
- `suppress_followup_noise`: 2
- `technical_error_local`: 5

---

## Pacotes renderizados

### Pacote 1 — Clau Xavier — Adriana Duque

- Tema/artista: Adriana Duque
- Canal provável: WhatsApp
- Risco: `A3`
- Fonte follow-up: `mixed:zipper:[phone]:adriana-duque-clau-xavier`
- Due/atualização: `2026-05-24T11:26:00-03:00` / `2026-05-24T14:28:41.581889+00:00`

```text
Aprovação necessária — Zipper

Cliente/contexto: Clau Xavier — Adriana Duque — Adriana Duque
O que aconteceu: Lead ZPR Chatbot Adriana Duque enviado por WhatsApp e e-mail em 2026-05-22; sem preço/reserva/condições específicas. Último registro de outbound verificado: 2026-06-05T20:12:33.963852+00:00 (n/a, whatsapp, whatsapp_text).
Por que importa: Há sinal material/comercial que exige decisão ou resposta aprovada.
Cuidado: Risco A3: não enviar nada ao cliente sem aprovação explícita do Lucas neste turno. Reconciliar histórico recente antes de qualquer envio; bloquear se houver preço, disponibilidade, pagamento, reserva, desconto, negociação ou reclamação.
Minha recomendação: Não mandar follow-up genérico automaticamente; pedir decisão do Lucas porque houve resposta/interação do cliente após o outbound.
Draft sugerido:
Olá Clau, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.

Decisão: aprovar este draft / pedir ajuste / não responder agora.
```

### Pacote 2 — Camila Paschoalin

- Tema/artista: sem artista específico
- Canal provável: WhatsApp
- Risco: `A3`
- Fonte follow-up: `whatsapp:pessoal:[phone]:zipper`
- Due/atualização: `2026-05-23T16:47:44.171903+00:00` / `2026-05-23T16:48:18.998009+00:00`

```text
Aprovação necessária — Zipper

Cliente/contexto: Camila Paschoalin — sem artista específico
O que aconteceu: Lucas respondeu que a obra Parque Lage está esgotada, mas explicou condições de pagamento. Follow-up deve buscar vender outras obras disponíveis do PDF, não encerrar o lead. Último registro de outbound verificado: 2026-06-05T20:12:33.963852+00:00 (n/a, whatsapp, whatsapp_text).
Por que importa: Há sinal material/comercial que exige decisão ou resposta aprovada.
Cuidado: Risco A3: não enviar nada ao cliente sem aprovação explícita do Lucas neste turno. Não prometer disponibilidade, preço, reserva ou condição; só oferecer conversa sobre alternativas já conhecidas.
Minha recomendação: Usar como rascunho de retomada leve, mas só após Lucas confirmar que quer reabrir a conversa sobre alternativas.
Draft sugerido:
Oi Camila, tudo bem? Só passando para saber se alguma outra obra da seleção te chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.

Decisão: aprovar este draft / pedir ajuste / não responder agora.
```

### Pacote 3 — Rafaela Rocha — Rodrigo Braga

- Tema/artista: Rodrigo Braga
- Canal provável: WhatsApp
- Risco: `A3`
- Fonte follow-up: `mixed:zipper:[phone]:rodrigo-braga-rafaela-rocha`
- Due/atualização: `2026-05-22T21:22:12-03:00` / `2026-05-23T00:22:27.431966+00:00`

```text
Aprovação necessária — Zipper

Cliente/contexto: Rafaela Rocha — Rodrigo Braga — Rodrigo Braga
O que aconteceu: Lead ZPR Chatbot Rodrigo Braga enviado por WhatsApp e e-mail; sem preço/reserva/condições específicas. Último registro de outbound verificado: 2026-06-05T20:12:33.963852+00:00 (n/a, whatsapp, whatsapp_text).
Por que importa: Há sinal material/comercial que exige decisão ou resposta aprovada.
Cuidado: Risco A3: não enviar nada ao cliente sem aprovação explícita do Lucas neste turno. Reconciliar histórico recente antes de qualquer envio; bloquear se houver preço, disponibilidade, pagamento, reserva, desconto, negociação ou reclamação.
Minha recomendação: Não mandar follow-up genérico automaticamente; pedir decisão do Lucas porque houve resposta/interação do cliente após o outbound.
Draft sugerido:
Olá Rafaela, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.

Decisão: aprovar este draft / pedir ajuste / não responder agora.
```

---

## QA aplicado

- Renderer recompõe a classificação a partir do SQLite local antes de renderizar.
- Apenas candidatos action-ready viram pacote.
- IDs sensíveis, telefones, e-mails e JIDs são mascarados no relatório Brain.
- Termos de cron/log/classificador são proibidos na prévia Lucas-facing.

## Próximo passo

Revisar se esses 3 pacotes são bons o suficiente como formato. Só depois considerar reativar um digest/cron limpo; envio real continua bloqueado sem aprovação.
