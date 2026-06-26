# Rotina semanal — Scorecard de orquestração Hermes COO

Status: ativa como rotina documental  
Owner: Hermes Geral / COO  
Cadência: semanal  
Dia recomendado: segunda-feira após revisar a semana anterior  
Entrega padrão: Brain/local; Telegram só se houver decisão, exceção, falha ou aprovação necessária  
Writes externos: não

## Objetivo

Medir se a orquestração do Hermes está funcionando na prática, não só documentada.

O scorecard responde:

- O pedido caiu no executor certo?
- Houve handoff quando deveria?
- Houve receipt/verificação?
- O bloqueio foi correto ou excessivo?
- Houve ruído no Telegram?
- Algum erro se repetiu apesar de skill/rotina?

## Escopo semanal

Auditar a semana anterior em:

- conversas e handoffs relevantes;
- `empresa/contexto/handoffs/YYYY-MM-DD.md`;
- `reports/governance/`;
- receipts de especialistas;
- cron registry em modo read-only;
- hot context;
- skills ou rotinas atualizadas.

## Métricas

### 1. Roteamento

- Total de tarefas materiais:
- Rota correta:
- Rota corrigida durante execução:
- Hermes Geral executou algo que deveria ser especialista:
- Especialista executou sem handoff:

Nota 0-10:

### 2. Handoff/receipt

- Outputs materiais com handoff:
- Outputs materiais sem handoff:
- Receipts com fonte/rollback/readback:
- Receipts incompletos:

Nota 0-10:

### 3. Approval gates

- Bloqueios corretos:
- Bloqueios excessivos:
- Writes externos evitados corretamente:
- Aprovações amplas interpretadas com risco:

Nota 0-10:

### 4. UX Telegram

- Mensagens úteis:
- Ruído/status desnecessário:
- Metadata técnica vazada:
- Decisões 1/N bem formatadas:

Nota 0-10:

### 5. Aprendizado/skills

- Correções de Lucas capturadas:
- Skills/rotinas atualizadas:
- Erros repetidos após skill patch:
- Procedimentos novos candidatos a skill:

Nota 0-10:

## Nota final

Calcular média ponderada:

- Roteamento: 25%
- Handoff/receipt: 25%
- Approval gates: 20%
- UX Telegram: 20%
- Aprendizado/skills: 10%

## Template de relatório semanal

Salvar em:

`reports/governance/orquestracao-scorecard-semanal-YYYY-WW.md`

```md
# Scorecard semanal — Orquestração Hermes COO

Semana:
Owner: Hermes Geral / COO
Escopo:

## Resumo executivo

Nota geral:
Status: melhorou | estável | piorou
Principal risco:
Principal melhoria:

## Métricas

### Roteamento
Nota:
Evidências:
Achados:

### Handoff/receipt
Nota:
Evidências:
Achados:

### Approval gates
Nota:
Evidências:
Achados:

### UX Telegram
Nota:
Evidências:
Achados:

### Aprendizado/skills
Nota:
Evidências:
Achados:

## Top 3 ações da próxima semana

1.
2.
3.

## Bloqueios que exigem Lucas

- 

## Não fazer

- Não criar cron/alterar gateway/Docker/VPS sem aprovação.
- Não reportar sucesso normal no Telegram.
```

## Critério de promoção para cron

Só propor cron depois de 2 execuções semanais manuais úteis, com baixo ruído e formato estável. Mesmo assim, cron novo exige aprovação explícita de Lucas.
