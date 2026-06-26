# LC Mordomo OS — P1.5 Zipper packet editorial + delivery contract proposal

**Data:** 2026-06-05
**Escopo:** revisão editorial dos pacotes Zipper e proposta local de contrato de entrega.
**Modo:** local/read-only; nenhum Telegram, WhatsApp, e-mail, cron, Supabase, produção ou infraestrutura alterado.

---

## Resultado executivo

- Pacotes editoriais: 3
- Formato: decisão primeiro, contexto curto, cuidado operacional, recomendação, draft e opções.
- Ruído removido: timestamp/canais de outbound, códigos de risco no texto Lucas-facing e termos de classificador.
- Ativação: `blocked_pending_lucas_approval`
- Entrega: proposta apenas; sem cron e sem envio agora.

---

## Pacotes editoriais v2

### 1. Clau Xavier — Adriana Duque

```text
Aprovação necessária — Zipper

Decisão para Lucas: Aprovar ou não uma resposta para Clau Xavier — Adriana Duque sobre Adriana Duque.
Contexto: ZPR sobre Adriana Duque recebido e respondido pela Zipper em 2026-05-22.
Cuidado: Não enviar automaticamente; antes de qualquer envio, reconciliar histórico recente e bloquear se surgir preço, reserva, pagamento, desconto, negociação ou reclamação.
Recomendação: Não mandar follow-up genérico; pedir decisão do Lucas porque houve interação do cliente depois do contato inicial.
Draft:
Olá Clau, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.

Opções: aprovar / ajustar / não responder agora.
```

### 2. Camila Paschoalin

```text
Aprovação necessária — Zipper

Decisão para Lucas: Aprovar ou não uma resposta para Camila Paschoalin.
Contexto: Lucas respondeu que a obra Parque Lage está esgotada, mas explicou condições de pagamento. Follow-up deve buscar vender outras obras disponíveis do PDF, não encerrar o lead.
Cuidado: Não prometer disponibilidade, preço, reserva ou condição; só retomar alternativas já conhecidas se Lucas aprovar.
Recomendação: Usar como rascunho de retomada leve, mas só se Lucas quiser reabrir a conversa sobre alternativas.
Draft:
Oi Camila, tudo bem? Só passando para saber se alguma outra obra da seleção te chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.

Opções: aprovar / ajustar / não responder agora.
```

### 3. Rafaela Rocha — Rodrigo Braga

```text
Aprovação necessária — Zipper

Decisão para Lucas: Aprovar ou não uma resposta para Rafaela Rocha — Rodrigo Braga sobre Rodrigo Braga.
Contexto: ZPR sobre Rodrigo Braga recebido e respondido pela Zipper.
Cuidado: Não enviar automaticamente; antes de qualquer envio, reconciliar histórico recente e bloquear se surgir preço, reserva, pagamento, desconto, negociação ou reclamação.
Recomendação: Não mandar follow-up genérico; pedir decisão do Lucas porque houve interação do cliente depois do contato inicial.
Draft:
Olá Rafaela, tudo bem? Gostaria de saber se alguma das obras do PDF despertou seu interesse. Fico à disposição para te passar mais informações.

Opções: aprovar / ajustar / não responder agora.
```

---

## Proposta de contrato de entrega

- Destino proposto: `telegram:origin` — voltar para o chat do Lucas, não canal genérico.
- Frequência proposta: sob demanda ou 1 vez ao dia apenas se houver pacote real.
- Limite: até 3 pacotes por digest.
- Vazio: silencioso; sem recibo de sucesso rotineiro.
- Kill-switch: desativar se aparecer log/classificador, PII crua, pacote sem decisão ou mais de 3 pacotes por digest.
- Estado atual: proposta pendente; não cria cron e não envia agora.

Aprovação exigida antes de qualquer ativação:
- aprovar formato Lucas-facing
- aprovar destino de entrega
- aprovar cadência ou execução sob demanda
- aprovar kill-switch e limite máximo por digest

---

## Verificação P1.5

- Suíte P1.4/P1.5 ampliada para 7 testes.
- Renderer continua recompondo a classificação a partir do SQLite local.
- `activation_decision(..., explicit_approval=False)` continua bloqueando cron/Telegram.
- A prévia JSON local contém a proposta de entrega, mas sem side effect externo.

## Próxima frente segura

**P1.6 — approval packet para Lucas decidir ativação ou manter on-demand.**

Critério de pronto:

- apresentar os 3 pacotes v2 + contrato proposto em formato de decisão única;
- se Lucas aprovar explicitamente, preparar implementação de entrega mínima com kill-switch;
- se não aprovar, manter apenas renderer local/on-demand.
