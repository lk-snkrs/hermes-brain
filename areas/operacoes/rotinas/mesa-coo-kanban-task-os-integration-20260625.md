# Mesa COO × Hermes Task OS — Integração sem spam

- Data: 2026-06-25
- Board canônico Task OS: `hermes-task-os`
- Card executado manualmente: `t_1ed3d96d`
- Execução: local/documental, sem assignee, sem dispatch, sem worker, sem cron mutation
- generated_at_utc: `2026-06-25T14:36:52.817484+00:00`
- values_printed: `false`

## Objetivo

Permitir que a Mesa COO use o Kanban nativo do Hermes como fonte de pendências/decisões sem transformar Telegram em backlog barulhento.

A Mesa deve funcionar como **filtro executivo**, não como espelho do board.

## Fonte de verdade por camada

| Camada | Papel |
|---|---|
| Hermes Kanban / `hermes-task-os` | fila operacional, status, dono lógico, bloqueio, execução/worker quando aprovado |
| Brain | evidência canônica: receipts, reports, rotinas, decisões, handoffs |
| Mesa COO | seleção de decisões acionáveis para Lucas |
| Telegram | canal de decisão/alerta, não backlog |

## Regra de ouro

**A Mesa só eleva card Kanban para Telegram se houver decisão real ou alerta acionável.**

Card aberto não é, por si só, motivo para Telegram.

## Critérios para elevar um card à Mesa

Um card pode virar decisão Mesa se atender pelo menos 1 critério abaixo:

1. `blocked` com decisão Lucas clara.
2. Risco A3/A4 aguardando approval packet.
3. `ready` com `Precisa Lucas: sim` e próxima ação específica.
4. Prazo/evento relevante nas próximas 24–72h.
5. Falha runtime/tool atual verificada e não recuperada.
6. Divergência entre fonte viva e documentação com impacto prático.
7. Oportunidade/risco comercial com ação concreta, fonte viva e dono lógico.

## Critérios para NÃO elevar

Não enviar para Telegram:

- cards `done` ou `archived`;
- `ready` antigo sem revalidação/stale review;
- backlog sem prazo;
- silent-OK;
- health check saudável;
- erro recuperado;
- card sem dono lógico;
- card sem próxima ação;
- lista bruta de todos os cards;
- IDs técnicos sem contexto;
- IMBOX/Inbox salvo pedido explícito do Lucas.

## Mapeamento Kanban → Mesa

| Kanban | Mesa COO |
|---|---|
| `triage` | não eleva; precisa especificação |
| `todo` | não eleva salvo bloqueio crítico |
| `ready` unassigned A0/A1 | local/silent; não eleva |
| `ready` unassigned A2/A3/A4 com `Precisa Lucas: sim` | decisão candidata |
| `ready` com assignee | verificar se execução foi aprovada; se não, risco operacional |
| `running` | só alertar se travado/falhou/TTL excedido |
| `blocked` | decisão candidata se bloqueio pedir escolha clara |
| `scheduled` | só alertar se prazo/evento exigir Lucas |
| `done` | não eleva; citar só como evidência se necessário |
| `archived` | não eleva |

## Scoring simples de prioridade

Pontuar candidatos internamente, sem mostrar score bruto no Telegram:

```text
+3 blocked com decisão Lucas
+3 A4
+2 A3
+2 prazo <= 72h
+2 impacto comercial/operacional claro
+1 fonte viva verificada
+1 dono lógico claro
-3 stale >30 dias sem revalidação
-3 sem próxima ação
-5 silent-OK/status saudável
-5 done/archived
```

Elevar no máximo 4 decisões por ciclo, uma por vez.

## Forma da decisão no Telegram

Formato limpo:

```md
## Mesa COO — YYYY-MM-DD

**Decisão 1/N:** decidir se ...
- Dono: ...
- Por que importa: ...
- Se escolher Fazer: ...
- Evidência: ...
- Limite/risco: ...
```

Para ações A3/A4, `Fazer` significa preparar/validar approval packet/read-only, não executar produção.

## Query operacional sugerida

A Mesa pode ler os boards nesta ordem:

1. `hermes-task-os`
2. boards de domínio com abertos: `lk-growth-ops`, `hermes-lk-improvements`, outros se existirem
3. `reminder-os` apenas para loops acionáveis

Para cada card aberto:

1. ler status, assignee, idade, título e corpo;
2. descartar done/archived/status saudável/stale sem revalidação;
3. verificar Brain report/receipt indicado no corpo;
4. checar se há histórico recente antes de sugerir melhoria;
5. montar decisão só se existir ação concreta.

## Handoff/ledger

Quando a Mesa envia uma decisão originada de Kanban, registrar no decision sequence ledger:

```json
{
  "source": "kanban",
  "board": "hermes-task-os",
  "task_id": "t_xxxxxxxx",
  "risk": "A3-prep",
  "safe_action": "preparar approval packet read-only",
  "blocked_actions": ["external_write", "dispatch", "prod"],
  "evidence_paths": ["..."],
  "external_writes": false
}
```

## Política para cards stale

Cards `ready` com mais de 30 dias não devem virar decisão direta. Primeiro:

1. verificar histórico recente;
2. confirmar se ainda são relevantes;
3. atualizar fonte viva;
4. decidir arquivar, migrar ou transformar em approval packet novo.

## Estado atual após esta integração

- A integração é documental/operacional, não mutação de cron.
- Não alterei o prompt vivo do cron Mesa COO.
- Não alterei delivery do cron.
- Não adicionei assignee nem dispatch.
- Próximo passo seguro: preparar o card `t_6d7720a2` — approval packet para primeiro worker read-only.

## Critério de sucesso

A Mesa melhora se Lucas receber menos ruído e mais decisões reais. Métrica qualitativa:

- menos cards genéricos;
- menos repetição de itens já feitos;
- zero backlog bruto no Telegram;
- decisions com fonte + limite claro;
- cards Kanban servindo como memória operacional, não como fila de spam.
