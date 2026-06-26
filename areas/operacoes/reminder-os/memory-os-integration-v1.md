# Reminder OS × Memory OS integration v1

Data: 2026-06-12  
Status: especificação local/documental ativa; sem mutação de hook/runtime nesta fase.  
Owner: Hermes Geral / Operações  
Superfície: Hermes Agent nativo — Brain, ledger local, Kanban, cron/watchdog, agents/profiles. Mission Control fica fora.

## Objetivo

Definir como eventos do Memory OS podem virar loops Reminder OS sem duplicar ruído, sem vazar contexto e sem executar a tarefa lembrada.

Memory OS mantém contexto e higiene. Reminder OS garante retomada/fechamento de pendências.

## Gatilhos de criação de loop

Memory OS deve considerar criar ou recomendar loop Reminder OS quando um artefato recente tiver:

- `Próximo passo` aberto e não fechado;
- `Riscos/bloqueios` com dependência humana ou evento futuro;
- handoff/receipt com trabalho explicitamente adiado;
- decisão sequencial `N/M` ainda aberta;
- approval packet pendente de resposta do Lucas;
- daily/hot indicando frente em andamento sem fechamento;
- auto-heal local que corrigiu contexto mas deixou ação futura necessária.

Não criar loop para:

- receipt fechado sem próximo passo;
- rotina silent-OK saudável;
- log técnico sem decisão;
- artefato antigo já coberto por loop ativo;
- dados vivos sem fonte fresca.

## Campos mínimos ao criar loop

Usar `/opt/data/scripts/reminder_os_add.py` quando o hook for ativado em fase futura.

Campos obrigatórios:

- `title`: título curto do loop;
- `owner`: dono lógico/profile;
- `status`: um dos estados permitidos no ledger;
- `next_action`: próxima ação concreta;
- `source`: `memory-os` ou `memory-os:<subrotina>`;
- `evidence`: caminho Brain/report/receipt/handoff;
- `next_review_at` ou `due_at`: gatilho temporal quando existir.

## Dedupe key

Antes de criar loop, calcular chave determinística:

```text
sha1(normalized(owner) + "|" + normalized(next_action) + "|" + evidence_path)
```

Regra:

- se existir loop ativo (`open`, `waiting_lucas`, `waiting_event`, `scheduled_check`, `kanban_tracked`) com a mesma chave/evidência, atualizar/reusar; não criar novo;
- se o loop anterior estiver `done`/`expired`, criar novo apenas se houver evidência mais recente ou next action diferente;
- se a evidência for um card Kanban, preferir `kanban_tracked` e apontar para o card.

## Política de silêncio

- Estado verde: stdout vazio.
- Loop criado automaticamente por Memory OS: não enviar Telegram por padrão.
- Telegram só se o status for `waiting_lucas` high severity, ou se o watchdog de 2h detectar vencimento/risco real.
- Nunca imprimir JSON bruto do ledger, conteúdo integral de receipt, job ID, token, PII desnecessária ou wrappers.

## Comportamento em falha

Se Memory OS tentar criar loop e falhar:

1. não executar a ação lembrada;
2. registrar falha sanitizada em report local `reports/reminder-os/`;
3. se a falha impedir continuidade importante, imprimir alerta curto/actionable;
4. se falhou por enum/schema, corrigir artefato local antes de alertar Lucas;
5. se falhou por permissão/runtime/cron, abrir approval packet separado.

## Testes necessários antes de ativar hook real

Antes de qualquer mutação no hook Memory OS:

- teste de criação válida via helper;
- teste de dedupe por `owner + next_action + evidence`;
- teste de não criar loop para receipt fechado;
- teste de `waiting_lucas/high` virar candidato de alerta, mas não execução;
- teste de stdout vazio em sucesso;
- teste de sanitização contra marcadores de credencial: token assignment, API-key label, password label e HTTP authorization header;
- teste de replay de artefato antigo sem duplicar ledger.

## Guardrails

Esta especificação não autoriza alteração do cron Memory OS, hook, gateway, Docker/VPS, provider externo, banco ou writes de negócio. A ativação automática do hook Reminder OS exige fase separada com testes, backup e verificação.
