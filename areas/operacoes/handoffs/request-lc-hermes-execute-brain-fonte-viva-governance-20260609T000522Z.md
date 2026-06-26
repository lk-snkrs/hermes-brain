# Pedido de execução — Agente LC Hermes

Data/hora: 2026-06-09T00:05:22+00:00
Solicitante: Lucas Cimino via Mordomo
Destino: Agente LC Hermes Central / Hermes Geral
Tipo: governança Brain / rotina canônica
Risco: A1 — documentação local/read-only, sem runtime, sem deploy, sem dados sensíveis

## Pedido ao agente LC Hermes

Executar, como agente dono da governança central, a próxima ação recomendada no handoff:

`areas/operacoes/handoffs/handoff-lc-hermes-brain-fonte-viva-governance-20260609T000522Z.md`

## Ação solicitada

Criar a rotina canônica:

`areas/operacoes/rotinas/brain-fonte-viva-e-dados-grandes.md`

## Escopo esperado

A rotina deve formalizar a regra:

> Brain guarda contexto, decisões, resumos, índices, governança e receipts. Bases grandes/dados vivos ficam em fonte viva consultável — banco/API/runtime — e o Brain aponta para elas, não replica tudo.

Conteúdo mínimo:

1. Fronteira Brain vs fonte viva.
2. Matriz por tipo de dado:
   - guardar completo no Brain;
   - guardar resumo/índice;
   - consultar fonte viva;
   - proibido persistir bruto.
3. Checklist para novos PRDs, ingests, subagentes, Mission Control e skills.
4. Política de freshness/source confidence.
5. Exemplos por LK, Zipper, SPITI, Mordomo, Hermes/infra.
6. Guardrails de PII, mensagens brutas, dumps e logs.
7. Critério de exceção: quando um snapshot completo é aceitável e como expirar/rotular.

## Pós-execução esperado

- Atualizar `areas/operacoes/MAPA.md` apontando para a rotina.
- Registrar receipt curto em `areas/operacoes/receipts/`.
- Se a regra for aprovada/promovida, planejar patch nas skills relevantes sem misturar execução nesta mesma tarefa.

## Critério de pronto

- Rotina existe e está indexada.
- Handoff fica resolvido ou referenciado.
- Pendência em `memories/pending.md` pode ser marcada como concluída.
- Nenhuma mudança em runtime, produção, secrets, bancos ou integrações externas.
