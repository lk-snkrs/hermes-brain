# Hermes Task OS — política universal para agentes

- Data: 2026-06-25
- Dono: Hermes Geral / Lucas Cimino
- Status: proposta canônica local; ativação cross-profile exige etapa controlada
- generated_at_utc: `2026-06-25T16:45:56.048151+00:00`
- values_printed: `false`

## Tese

Todo agente Hermes deve tratar trabalho não-trivial como **tarefa operacional rastreável**, não como conversa solta.

Isso não significa criar card para tudo. Significa aplicar o funil:

```text
pedido → classificar → fonte/histórico → decidir se vira card → executar/rotear → evidência → receipt/handoff → Mesa COO só se acionável
```

## Regra de decisão: quando criar card Kanban

Criar/usar card quando a tarefa tiver qualquer um destes sinais:

1. precisa sobreviver à sessão;
2. envolve mais de um agente/profile;
3. tem risco A2+ ou exige approval;
4. tem bloqueio ou depende de Lucas;
5. gera handoff/receipt/report;
6. pode rodar como worker;
7. precisa ser auditável ou retomável;
8. é parte de rotina/cron/operacional recorrente.

Não criar card para:

- resposta simples e imediata;
- pergunta factual curta;
- ação local trivial sem continuidade;
- status saudável/silent-OK.

## Regra de segurança

- `assignee` em card `ready` pode disparar execução se `dispatch_in_gateway=true`.
- Para backlog/passivo: usar `blocked` ou `ready` **sem assignee**.
- Não usar `--triage` para backlog passivo em produção; pode auto-especificar/decompor e spawnar child tasks.
- A3/A4 sempre requer approval packet com backup/rollback/verificação.

## Regra de Mesa COO / Telegram

Telegram não é board. Telegram recebe apenas:

- decisão real;
- bloqueio concreto;
- falha atual;
- aprovação necessária;
- alerta acionável.

Silent-OK fica local/Brain.

## Fechamento obrigatório

Toda tarefa operacional relevante deve terminar em um destes estados:

- done com evidência/receipt/handoff;
- blocked com pergunta clara para Lucas ou owner;
- archived/stale com motivo;
- scheduled/reminder com gatilho.

Não deixar trabalho importante só em transcript de chat.
