# Rotina — Aprendizado diário Larissa Crisp/Hugo

Horário desejado: 21h todos os dias.
Status: aguardando implementação técnica e credenciais Crisp/Hugo.

## Objetivo

Aprender com as respostas reais da Larissa no Crisp e atualizar o LK Response Brain sem perder guardrails.

## Entradas

- Conversas Crisp do dia.
- Mensagens enviadas pela Larissa.
- Mensagens imediatamente anteriores do cliente.
- Contexto da conversa quando necessário.

## Saídas

- `knowledge/lk-response-brain/daily-lessons/YYYY-MM-DD.md`
- Atualizações propostas em:
  - `knowledge/lk-response-brain/approved-answer-patterns.md`
  - `knowledge/lk-response-brain/larissa-tone.md`
  - `knowledge/lk-response-brain/blocked-topics.md`

## Processo

1. Buscar conversas do dia no Crisp.
2. Filtrar respostas da Larissa.
3. Montar pares pergunta/resposta.
4. Redigir lessons sem PII.
5. Classificar:
   - permitido e reutilizável;
   - permitido, mas exige fonte;
   - bloqueado/transbordo;
   - precisa aprovação Lucas.
6. Atualizar Brain com diff claro.
7. Enviar alerta ao Lucas apenas se houver decisão, falha, ou mudança de regra relevante.

## Guardrails

- Não aprender credenciais, dados pessoais, endereços, pedidos, rastreios ou detalhes financeiros.
- Não ativar automaticamente respostas sobre sob encomenda/status pedido/entrega; esses temas continuam bloqueados.
- Não transformar exceção da Larissa em regra geral sem evidência recorrente.
- Preferir exemplos de tom e estrutura, não cópia literal com dados do cliente.
