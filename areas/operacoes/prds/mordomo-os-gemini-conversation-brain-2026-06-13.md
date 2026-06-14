# Mordomo OS Gemini Conversation Brain — decisão de produto

Data: 2026-06-13
Contexto: Operações / Mordomo / WhatsApp pessoal e atendimento a clientes

## Decisão

Lucas aprovou evoluir o Mordomo OS para usar Gemini como camada central de entendimento de mensagens de clientes e esclareceu que isso deve **substituir o sistema atual de follow-up**, não apenas adicionar uma IA auxiliar sobre a lógica antiga de palavras-chave.

## Direção aprovada

Fluxo alvo:

1. Entrada de mensagem WhatsApp/e-mail/intake.
2. Recuperação de histórico, contexto da empresa, CRM, PDFs/propostas e follow-ups anteriores.
3. Gemini/Conversation Brain classifica intenção, risco, próximo passo, follow-ups e CRM updates em JSON estruturado.
4. Guardrails determinísticos revisam e podem bloquear/downgradear qualquer recomendação.
5. Executor realiza apenas ações permitidas: draft, follow-up interno, CRM local, calendário, ou envio externo nas classes estreitas já aprovadas.
6. Recibos e evidência ficam no estado/Brain/CRM correto.

## Substituição do sistema antigo

- A lógica antiga baseada em regex/palavras-chave deve ser demovida para camada de **guardrail/compatibilidade**, não permanecer como estratégia principal.
- O novo dono da estratégia de follow-up deve ser o `mordomo_os_conversation_brain`.
- A troca operacional deve ser gradual: shadow mode, comparação, bridge com fila atual, CRM/score, approval packet e só então cutover.
- Nenhum envio externo novo ou cron cutover está implicitamente aprovado por esta decisão; cutover e writes externos continuam exigindo approval packet escopado.

## Guardrails que permanecem obrigatórios

Bloquear ou escalar para Lucas/fonte validada:

- preço, valor, desconto;
- disponibilidade, reserva, segurar obra/produto;
- pagamento, Pix, parcelamento, condição;
- negociação, reclamação, problema;
- SPITI/lance/leilão;
- LK estoque/disponibilidade, que deve ir ao dono `lk-stock`;
- identidade ambígua, grupo, cliente não validado ou risco A3/A4.

## Artefatos locais

- Plano de execução: `/opt/data/.hermes/plans/2026-06-13-mordomo-gemini-conversation-brain.md`
- Módulo inicial: `/opt/data/profiles/mordomo/scripts/mordomo_os_conversation_brain.py`
- Teste inicial: `/opt/data/profiles/mordomo/scripts/test_mordomo_os_conversation_brain.py`

## Estado inicial de execução

- Contrato puro do Conversation Brain criado em shadow/preparation mode.
- 4 testes novos passam.
- Testes de política/idempotência/sequence guard relevantes passam.
- Nenhum envio externo, CRM remoto, cron cutover ou alteração de produção executado nesta etapa.
