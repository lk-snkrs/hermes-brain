# PRD — LC Mordomo OS: Follow-up e Auto-ack WhatsApp Pessoal

Data: 2026-06-05
Sistema: LC Mordomo OS / Subagente Zipper lógico / WhatsApp pessoal Lucas

## 1. Problema

O Mordomo falhou em responder automaticamente uma classe segura de mensagem no WhatsApp pessoal.

Caso observado:

- Lead: Lara Marson — Nina Pandolfo
- Canal: WhatsApp pessoal
- Contexto: Zipper / pós-envio de PDF de obras disponíveis
- Último outbound: envio de texto introdutório + PDF “Nina Pandolfo — Obras Disponíveis.pdf”
- Inbound cliente:
  - “Boa tarde!”
  - “Muito obrigada!”
- Resposta esperada A1/A2 automática:
  - “Imagina, Lara! Fico à disposição se alguma obra chamar sua atenção ou se quiser mais informações.”

## 2. Diagnóstico da falha

A falha teve duas causas combinadas:

1. **Watcher pausado**
   - O cron `Mordomo global WhatsApp watcher — Lucas pessoal` estava pausado desde 2026-06-02.
   - Isso impediu a varredura recorrente das respostas do WhatsApp pessoal.

2. **Contexto frágil para replies curtas**
   - O envio ZPR inicial criou uma linha na fila `mordomo_followup_queue.json`, mas não garantia que o chat ficasse ativo no estado do watcher.
   - Mensagens curtas como “Muito obrigada!” não têm palavras de negócio (“Zipper”, “obra”, “PDF”, “Nina Pandolfo”) e podem ser classificadas como `unknown` se o chat não estiver ativo.
   - Portanto, mesmo com a taxonomia de agradecimento seguro, o pipeline poderia não chegar ao auto-ack.

## 3. Objetivo

Garantir que clientes/leads Zipper que receberam PDF pelo WhatsApp pessoal tenham:

- auto-ack imediato para agradecimentos/recebimentos simples;
- follow-up pós-PDF em 2 dias quando aplicável;
- bloqueio para qualquer pedido material;
- deduplicação e auditoria local;
- cron ativo e silencioso quando não há trabalho.

## 4. Escopo funcional

### 4.1 Auto-ack seguro pós-PDF

Quando um lead Zipper registrado responde depois do envio de PDF com mensagem simples, responder automaticamente.

Exemplos seguros:

- “Obrigada”
- “Muito obrigada!”
- “Boa tarde! Muito obrigada!”
- “Recebido”
- “Ok, obrigada”
- “Vou olhar com calma”
- “Obrigado por fornecer o catálogo com as obras da Janaina Mello. Vou verificar a viabilidade de utilizá-las e qualquer coisa te retorno. Obrigado!”
- “Vou avaliar com a cliente e qualquer coisa te aviso.”
- “Vou encaminhar para o comprador e te retorno.”
- “👍”

Regra: quando o cliente agradece o PDF/catálogo/material e diz que vai verificar/analisar/avaliar/encaminhar para cliente/projeto e retorna se houver interesse, isso é **auto-ack + follow-up futuro**, não “Decisão WhatsApp”.

Template aprovado:

```text
Imagina, {{nome}}! Fico à disposição se alguma obra chamar sua atenção ou se quiser mais informações.
```

### 4.2 Bloqueadores

Nunca auto-responder quando houver pedido ou compromisso material:

- preço/valor;
- disponibilidade;
- pagamento/Pix/cartão/parcelamento;
- reserva/segurar obra;
- desconto/negociação;
- medida/dimensão;
- frete/entrega;
- reclamação/problema/urgência;
- pergunta com `?` ligada a negócio.

Esses casos viram decisão/draft para Lucas.

### 4.3 Ativação de contexto por fila

O watcher deve semear `active_chats` a partir da fila de follow-ups para leads Zipper pós-PDF recentes:

- `business_context=zipper`
- `intent=post_pdf_followup`
- `risk_level in A0/A1/A2`
- status ativo: `waiting_client`, `safe_to_review`, `safe_to_followup`, `auto_sent`, `manual_sent`
- WhatsApp DM individual validado
- janela recente: até 45 dias

Isso evita que replies curtas sejam ignoradas por falta de palavras-chave.

### 4.4 Contato não salvo, mas lead registrado

Se o WhatsApp mostra só o número/contato não salvo, mas a fila tem lead registrado com nome + número + artista/PDF, o auto-ack seguro pode enviar usando o contexto registrado.

Não vale para leads ambíguos ou sem registro confiável.

## 5. Auditoria e dedupe

Todo envio automático deve registrar em `mordomo_followup_queue.json.sent_actions`:

- kind: `whatsapp_zpr_pdf_thanks_ack`
- status
- sent_at
- contact_label
- hash do contato, não telefone cru em alertas
- business_context
- intent
- mensagem enviada
- provider result / message id quando disponível

A chave de dedupe principal é o ID da mensagem inbound quando disponível:

```text
zipper_pdf_thanks_ack:<inbound_message_id>
```

## 6. Cron / execução

Cron canônico:

- Nome: `Mordomo global WhatsApp watcher — Lucas pessoal`
- Script: `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`
- Frequência: every 5m
- Semântica: no-agent / silent OK
- Saída vazia com rc=0 significa: nenhuma ação necessária.

O cron não deve ficar pausado quando follow-ups de WhatsApp pessoal estiverem em produção. Se for pausado por manutenção, precisa haver watchdog/substituto ou registro de suspensão operacional.

## 7. Correção aplicada em 2026-06-05

- Resposta enviada para Lara e reconciliada no estado local.
- Resposta enviada para Henrique/Triptyque e reconciliada no follow-up canônico `mixed:zipper:henrique-takinaga-triptyque:janaina-mello-landini`; o follow-up paralelo `whatsapp:pessoal:5517996188729@s.whatsapp.net:zipper` foi tombado como `merged_into_canonical_followup` para não gerar “Decisão WhatsApp”.
- `mordomo_whatsapp_global_watch.py` atualizado para:
  - aceitar saudação prefixada em agradecimentos simples (`Boa tarde! Muito obrigada!`);
  - aceitar “obrigado pelo catálogo/PDF + vou verificar/analisar/avaliar viabilidade + retorno/aviso/falo” como A1 pós-PDF;
  - permitir auto-ack para contato não salvo quando o lead ZPR está registrado e validado;
  - semear chats ativos a partir da fila de follow-ups Zipper pós-PDF;
  - preferir/mesclar follow-ups canônicos pós-PDF em vez de criar decisão paralela por `whatsapp:pessoal:<chat>:zipper`.
- Cron `Mordomo global WhatsApp watcher — Lucas pessoal` reativado.
- Estado `last_run_at` avançado após reconciliação para evitar backlog antigo e duplicidades.

## 8. Critérios de aceite

- `python3 -m py_compile mordomo_whatsapp_global_watch.py` passa.
- Fixture positiva passa para agradecimentos simples.
- Fixture negativa bloqueia preço/disponibilidade/pagamento.
- Seed de `active_chats` reconhece Lara a partir da fila.
- Execução manual do watcher retorna `rc=0` e stdout vazio após reconciliação.
- Histórico do WhatsApp mostra uma única resposta automática, sem duplicata.
- Cron fica enabled/scheduled.

## 9. Princípio LC Mordomo OS

Follow-up seguro e auto-ack de baixo risco são responsabilidade operacional do Mordomo, não tarefa manual do Lucas. Quando o sistema falha, o comportamento correto é:

1. reconhecer o erro;
2. reconciliar o caso sem duplicar mensagem;
3. corrigir a classe inteira;
4. registrar no Brain/PRD;
5. verificar cron, regressões e idempotência.
