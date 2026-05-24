# Rotina — Auditoria de handoff de especialistas

Status: ativo como checklist de governança  
Criada: 2026-05-20  
Escopo: LK Growth, SPITI, Zipper, Mordomo, watchdogs e qualquer profile/bot especialista.

## Objetivo

Evitar que especialistas virem ilhas de dados. Toda execução relevante precisa deixar rastro no Hermes Brain para a Grande Mente consolidar.

## Frequência recomendada

- Diária no Fechamento Ágil 23h para sinais críticos.
- Semanal no Painel Semanal do Brain para cobertura completa.
- Sob demanda após campanha, envio, automação, write externo ou correção de Lucas.

## Fontes a verificar

- `areas/operacoes/inventarios/crons-agentes-profiles.md`;
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`;
- `reports/daily-consolidation/YYYY-MM-DD.md`;
- `areas/**/receipts/`;
- `areas/**/decisions/`;
- `areas/**/reports/`;
- cron list/runtime real quando for afirmar status ativo;
- session_search quando a execução pode ter ficado só no chat.

## Checklist

Para cada especialista/profile/bot ativo:

1. Houve conversa, execução, cron ou entrega relevante desde a última auditoria?
2. O evento gerou decisão, aprovação, envio, write externo, risco, pendência ou aprendizado?
3. Existe receipt/handoff mínimo no Brain?
4. Existe link no MAPA/rotina/área correta?
5. Existe fonte usada e status de aprovação?
6. Se houve envio externo, há evidência sem PII desnecessária?
7. Se houve falha, existe bloqueio/rollback/próximo passo?
8. O Hermes Central consegue retomar sem ler o chat bruto?

## Saída esperada

Criar ou atualizar um report curado com:

```md
# Auditoria de handoff — YYYY-MM-DD

## Cobertura por especialista
- LK Growth: ok / gap / sem atividade
- SPITI: ok / gap / sem atividade
- Zipper: ok / gap / sem atividade
- Mordomo: ok / gap / sem atividade
- Watchdogs/crons: ok / gap / sem atividade

## Gaps encontrados
- ...

## Correções aplicadas
- ...

## Bloqueios que exigem Lucas
- ...
```

## Critério de conclusão

Não declarar especialista “operacionalmente coberto” se:

- só existe documentação, sem evidência runtime quando status ativo é alegado;
- output relevante ficou apenas no chat;
- receipt não diz fonte, aprovação ou write externo;
- o MAPA da área não permite encontrar a decisão/entrega.
