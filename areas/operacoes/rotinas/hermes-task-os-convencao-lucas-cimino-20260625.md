# Hermes Task OS — Convenção Lucas/Cimino de campos, status e execução

- Data: 2026-06-25
- Board canônico: `hermes-task-os`
- Card executado manualmente: `t_5e84b76c`
- Execução: local/documental, sem assignee, sem dispatch, sem worker
- generated_at_utc: `2026-06-25T14:31:32.616431+00:00`
- values_printed: `false`

## Objetivo

Padronizar como o Hermes usa o Kanban nativo como **Linear interno** para Lucas/Cimino, sem transformar cards em execução automática indevida.

O Kanban é a fila/estado operacional. O Brain continua sendo a fonte de verdade para evidência, receipts, reports, rotinas e decisões.

## Princípios

1. **Task OS não é chat backlog.** Só entra card se houver dono lógico, próxima ação e critério de fechamento.
2. **Ready não significa autorizado.** Em produção atual, `kanban.dispatch_in_gateway=true`; portanto card `ready` com assignee pode executar.
3. **Assignee é ato operacional.** Atribuir profile executor só depois de approval packet quando houver risco A2+ ou qualquer write externo/prod.
4. **Brain guarda evidência.** Card aponta para relatório/receipt; não vira repositório de longos outputs.
5. **Telegram só decisão/alerta acionável.** Silent-OK fica em Brain/Kanban, não em mensagem.
6. **Histórico antes de sugestão.** Antes de criar execução para superfície já trabalhada, verificar receipts/packets/workdirs/readback aplicáveis.

## Campos obrigatórios no corpo de cards

Use este template para novos cards operacionais:

```text
Empresa/área:
Dono lógico:
Profile executor candidato:
Risco: A0/A1/A2/A3/A4
Precisa Lucas: sim/não
Tipo: decisão | execução local | execução externa | auditoria | follow-up | approval packet
Fonte canônica:
Histórico verificado:
Evidência/receipt/report:
Próxima ação:
Critério de pronto:
Bloqueio atual:
Writes externos: nenhum | preview-only | requer aprovação escopada
Rollback/verificação:
Telegram: silencioso | decisão | alerta acionável
```

## Risco A0–A4

| Risco | Significado | Autonomia padrão |
|---|---|---|
| A0 | leitura local, organização, documentação, classificação sem efeito externo | executar autonomamente |
| A1 | write local/Brain/receipt/relatório, sem produção e sem segredo | executar e verificar |
| A2 | mudança operacional reversível/local, ou preparação de approval packet | executar se escopo claro; sem external write |
| A3 | API externa, loja, campanha, cron/delivery, worker real, dados sensíveis ou possível impacto comercial | approval packet obrigatório |
| A4 | prod/VPS/Docker/Traefik/secrets/deploy/env/restart/migração/ação destrutiva | aprovação escopada + backup + rollback + verificação |

## Status Kanban no padrão Lucas

| Status nativo | Uso no Task OS | Regra |
|---|---|---|
| `triage` | entrada ambígua ou pedido bruto | precisa especificação antes de virar trabalho |
| `todo` | especificado mas aguardando dependência | não executar ainda |
| `ready` | pronto para decisão/manual routing | manter `unassigned` salvo aprovação de worker |
| `scheduled` | aguardando tempo/evento | precisa trigger claro e silent-OK |
| `running` | worker/execução ativa | só com assignee aprovado ou execução manual declarada |
| `blocked` | precisa Lucas/fonte/approval/dado/evento | bloqueio deve pedir uma decisão específica |
| `review` | precisa validação humana/QA | não fechar sem evidência |
| `done` | encerrado com evidência | precisa resumo, receipt/report ou justificativa |
| `archived` | removido da operação ativa | usar para stale/histórico sem ação |

## Tipos de cards

### 1. Decisão Lucas

Use quando existe trade-off real. Telegram pode ser usado, mas deve explicar gatilho e ação.

Campos adicionais:

```text
Opções:
Recomendação Hermes:
Consequência de não agir:
Prazo:
```

### 2. Execução local/documental

Exemplos: relatório Brain, receipt, índice, classificação, auditoria read-only.

Regra: pode ser executado manualmente sem assignee; ao fim, comentar e completar card.

### 3. Approval packet

Use antes de qualquer ação A3/A4.

Campos adicionais:

```text
Escopo exato:
Comandos/API pretendidos:
Backup:
Rollback:
Readback/verificação:
Critério de sucesso:
Critério de abortar:
```

### 4. Worker read-only

Só depois de escolher profile restrito e explicar toolset/fonte. Mesmo read-only pode gerar ruído se mandar Telegram ou tocar API externa.

### 5. Follow-up/stale review

Use para cards antigos ou superfícies já trabalhadas.

Regra obrigatória: verificar histórico antes de sugerir ação nova.

## Política de assignee

- `assignee=null`: backlog/governança/decisão/manual.
- `assignee=<profile>`: autorização operacional para worker, potencialmente executável.
- Cards `ready` A2+ ficam sem assignee até approval packet.
- Cards antigos `ready` com mais de 30 dias viram `review_stale` antes de qualquer execução.

## Mesa COO + Kanban

Mesa COO deve ler Kanban para achar decisões, mas não deve despejar backlog no Telegram.

Eleva para Telegram apenas se:

1. `blocked` com decisão Lucas clara;
2. A3/A4 aguardando aprovação;
3. prazo/evento relevante;
4. falha de runtime atual verificada;
5. oportunidade/risco com próxima ação concreta.

Não eleva:

- card antigo sem revalidação;
- done/histórico;
- silent-OK;
- erro recuperado;
- card sem dono lógico/próxima ação.

## Fechamento de card

Para fechar card manualmente:

1. gerar/atualizar artefato Brain quando aplicável;
2. criar receipt se houve decisão, write local relevante, mudança de rotina ou risco;
3. comentar no card com caminho do relatório/receipt;
4. completar com resumo curto;
5. verificar `running=0`, `diagnostics=0`, secret scan e Brain health quando houver artefato.

## Convenção de títulos

Formato recomendado:

```text
[Área][Tipo][Risco] ação concreta
```

Exemplos:

```text
[Hermes][Convenção][A1] definir campos Task OS
[LK Growth][Stale Review][A1] revalidar cards antigos lk-growth-ops
[Mesa COO][Design][A2] integrar Kanban sem spam Telegram
[Kanban][Worker Pilot][A3-prep] approval packet primeiro worker read-only
```

## Decisão atual

- `hermes-task-os` é o board central para governança do Linear interno.
- Boards de domínio podem existir, mas execução/stale/riscos sobem para Task OS antes de worker.
- Próximo passo após esta convenção: card `t_1ed3d96d` — integrar Mesa COO com Kanban sem spam.
