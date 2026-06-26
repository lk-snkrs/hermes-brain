# Elle — Guardrail de transbordo para Larissa

Data: 2026-06-10
Decisão: Lucas aprovou que a Elle **nunca** deve responder informações sobre status de pedido nem disponibilidade de produto em loja.

## Regra operacional

A Elle deve transbordar para Larissa quando a conversa envolver:

- status de pedido;
- número de pedido;
- rastreio/rastreamento;
- prazo/entrega relacionado a pedido;
- disponibilidade de produto;
- pronta entrega;
- produto/tamanho em loja;
- estoque/grade/tamanho.

## Motivo

Esses temas exigem fonte viva e podem gerar promessa operacional errada. Para estoque/pronta entrega, a fonte de verdade continua Tiny via lk-stock. Para pedido/status, a fonte precisa ser conferida por atendimento humano na fonte oficial antes da resposta final.

## Implementação local aplicada

Arquivos atualizados:

- `areas/lk/sub-areas/atendimento/policies/elle_intents.yaml`
- `areas/lk/sub-areas/atendimento/policies/elle_guardrails.yaml`
- `areas/lk/sub-areas/atendimento/scripts/elle_dryrun_classifier.py`

Mudanças:

- intents `pedido`, `prazo` e `estoque` agora são `default_risk: alto`;
- `handoff_always: true`;
- label `larissa-handoff` adicionada;
- bloqueios explícitos:
  - `answer_order_status`
  - `answer_store_availability`
- nota privada instrui transbordo para Larissa.

## Verificação

Dry-run local executado com 3 exemplos:

1. “Qual o status do meu pedido?”
   - intent: `pedido`
   - risco: alto
   - handoff: true
   - label: `larissa-handoff`
   - ação pública proibida

2. “Tem esse tênis tamanho 38 na loja?”
   - intents: `estoque`, `produto`
   - risco: alto
   - handoff: true
   - label: `larissa-handoff`
   - ação pública proibida

3. “Bom dia”
   - intent: `saudacao`
   - risco: baixo
   - sem handoff obrigatório

## Observação

Isso ainda é ajuste local/Brain/política de dry-run. Qualquer ativação produtiva de resposta pública, write no Chatwoot ou mudança no serviço Elle em produção continua exigindo aprovação escopada.
