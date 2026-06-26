# Task OS — recomendação de UX de acompanhamento

- Data: 2026-06-25
- Fonte: worker `hermes-ops-readonly`, card `hermes-task-os/t_6d995d67`
- Status do card: `done`
- Observação: o artifact original foi produzido em workspace `scratch`, que é efêmero após conclusão; este relatório preserva o handoff no Brain.
- generated_at_utc: `2026-06-25T15:43:31.714932+00:00`
- values_printed: `false`

## Recomendação executiva

Usar uma arquitetura híbrida:

1. **Hermes Kanban** como backoffice interno/operacional.
2. **Mesa COO no Telegram** como superfície principal para Lucas.
3. **Comandos Telegram sob demanda** apenas para consulta resumida, se aprovados depois.

Não recomendar dashboard/API público nesta fase.

## Por quê

O Kanban é excelente como fila operacional: status, assignee, runs, bloqueios, handoffs e logs. Mas expor isso diretamente para Lucas tende a gerar ruído: IDs técnicos, estados transitórios, diagnostics e backlog bruto.

A Mesa COO deve continuar sendo o filtro executivo: mostrar decisões, aprovações, bloqueios e alertas acionáveis — não o board inteiro.

## Contrato de UX

Lucas deve ver:

- decisões reais;
- aprovações A3/A4;
- bloqueios com escolha clara;
- alertas acionáveis atuais;
- resumos executivos curtos.

Lucas não deve ver por padrão:

- backlog bruto;
- `run_id`;
- diagnostics técnicos;
- IDs sem contexto;
- silent-OK;
- cards `done`/`archived`;
- erro recuperado;
- lista inteira de tarefas.

## Superfícies

### 1. Kanban Hermes

Uso: backoffice interno, fila, handoffs, worker state e auditoria.

Guardrail: dashboard/API público só com approval A3/A4 separado, autenticação, rollback e verificação.

### 2. Mesa COO Telegram

Uso: superfície principal de decisão.

Critério: no máximo poucas decisões por ciclo, uma de cada vez, com dono, motivo, ação segura e limite.

### 3. Comandos Telegram sob demanda

Possíveis comandos futuros:

```text
Task OS agora
Task OS decisões
Task OS bloqueios
```

Esses comandos devem ser consulta resumida, não execução implícita.

## Histórico verificado pelo worker

O worker leu/verificou:

- convenção Task OS;
- integração Mesa COO × Kanban;
- reconciliação de boards;
- resultado do piloto worker read-only.

## Guardrails preservados

- Sem dashboard público.
- Sem API/Traefik/Docker.
- Sem gateway/cron mutation.
- Sem Telegram automático.
- Sem writes externos.
- Sem secrets ou valores sensíveis.

## Decisão prática

Próxima evolução do Task OS deve ser **manual/Brain/Mesa-first**. Antes de qualquer dashboard/API público ou comandos Telegram novos, preparar approval packet próprio.
