# LC Mordomo OS — P1.6 correção Zipper: follow-up autônomo com contexto

**Data:** 2026-06-05
**Origem:** correção verbal do Lucas após ver os 3 pacotes P1.6.
**Modo:** local/read-only; nenhum Telegram, WhatsApp, e-mail, cron, Supabase, produção ou infraestrutura alterado.

---

## Correção recebida

Lucas corrigiu que os 3 exemplos apresentados eram péssimos como Decision Inbox porque eram follow-ups. Regra ajustada:

- follow-up puro não deve virar aprovação para Lucas;
- Mordomo deve fazer follow-ups sozinho quando a classe for segura;
- quando o follow-up for importante, antes de executar é obrigatório buscar o contexto das mensagens anteriores ligadas ao lead/contato;
- só depois de contexto + reconciliação/idempotência o follow-up pode ser executado autonomamente, se continuar seguro.

---

## Mudança operacional aplicada

O classificador local deixou de transformar esses casos em `action_ready_candidate`.

Novo bucket:

- `important_followup_needs_context`: follow-up importante, não Decision Inbox; precisa enriquecimento com histórico encadeado antes de envio autônomo.

Resultado atualizado do dry-run:

- Telegram-ready reais: 0
- `important_followup_needs_context`: 5
- `hard_recipient_blocklist`: 2
- `technical_error_local`: 5
- `review_before_alert`: 2
- `needs_enrichment`: 1

O renderer de pacotes Decision Inbox agora gera 0 pacotes para esses follow-ups.

---

## Fila local criada

Arquivo local:

`/opt/data/profiles/mordomo/state/zipper_important_followup_context_queue.json`

Itens atuais na fila de contexto:

1. Marcus Bitencourt
2. Brenda
3. Clau Xavier — Adriana Duque
4. Camila Paschoalin
5. Rafaela Rocha — Rodrigo Braga

Ação local por item:

1. buscar mensagens anteriores ligadas ao lead/contato no WhatsApp/e-mail;
2. reconciliar duplicidade/idempotência;
3. confirmar que continua follow-up sem preço/reserva/negociação/reclamação nova;
4. executar follow-up autonomamente se seguro.

---

## Regressão adicionada

A suíte local agora valida que:

- follow-ups puros não geram pacote Decision Inbox;
- `telegram_ready_count` fica 0;
- os 5 follow-ups importantes vão para `important_followup_needs_context`;
- cada item exige histórico encadeado antes de envio;
- renderer continua sem envio externo.

---

## Próxima frente segura

**P1.7 — context enricher + executor seguro de follow-up.**

Sequência:

1. Para cada item da fila, buscar histórico encadeado nas fontes locais disponíveis.
2. Gerar resumo de contexto por lead sem PII crua no Brain.
3. Classificar como:
   - `safe_to_autofollowup`, ou
   - `needs_lucas_context`, ou
   - `blocked_sensitive_material`.
4. Só enviar automaticamente os `safe_to_autofollowup` com idempotência; itens sensíveis voltam para Lucas com pergunta específica.
