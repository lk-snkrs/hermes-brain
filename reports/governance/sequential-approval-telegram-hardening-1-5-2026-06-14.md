# Sequential hardening 1–5 — Approval packets + Telegram noise — 2026-06-14

## Pedido

Lucas pediu: "Fazer tudo acima, sequencialmente, do 1 ao 5. Me manda um relatório quando acabar e depois me avise se tem mais coisas a serem feitas."

## Escopo

Classificação: A1 local/documental/testes.

Não ações preservadas:

- nenhum approval packet executado;
- nenhuma aprovação nova assumida;
- nenhum Telegram enviado por scripts;
- sem runtime, Docker, VPS, Traefik, gateway, restart ou cron mutation;
- sem Shopify, Tiny, GMC, Klaviyo, Meta, WhatsApp, e-mail, banco ou integrações externas;
- nenhum secret impresso; `values_printed=false`.

## 1) Approval packets críticos corrigidos documentalmente

Corrigidos 3 packets críticos da amostra real, apenas adicionando campos mínimos ausentes/guardrails. Nenhuma ação operacional foi executada.

### 1. Supabase MCP read-only

Arquivo:

- `areas/hermes/operacoes/manual-producao/APPROVAL_PACKET_SUPABASE_MCP_READONLY.md`

Campos clarificados:

- target/owner;
- escopo permitido;
- exclusões explícitas;
- verificação;
- secret hygiene.

### 2. LK fallback correction — 10 coleções piloto

Arquivo:

- `areas/lk/reports/auto-sort-collections/2026-05-26-pilot-fallback-correction/APPROVAL-PACKET-FALLBACK-CORRECTION.md`

Campos clarificados:

- decisão/ação solicitada;
- escopo permitido;
- exclusões explícitas;
- opções de aprovação;
- secret hygiene.

### 3. LK Weekly Collection Sort Rule B APPLY recorrente

Arquivo:

- `areas/lk/reports/auto-sort-collections/approval-packets/ruleb-recurring-apply-approval-packet-20260604.md`

Campos clarificados:

- target/owner;
- escopo permitido;
- exclusões explícitas;
- secret hygiene.

Validação atual dos 3:

- `status=ok`
- `files_checked=3`
- `failures_count=0`
- `values_printed=false`

## 2) Telegram noise/actionability contract tests

Endurecido o validator local:

- `scripts/telegram_noise_contract_validator.py`

Testes cobertos:

- mensagem acionável passa;
- vazamento de `HERMES_INLINE_BUTTONS` falha;
- vazamento de `job_id` falha;
- vazamento de Task Router/preflight falha;
- JSON/log/traceback cru falha;
- alerta sem ação clara falha;
- silent-OK exige stdout vazio;
- CLI JSON conta achados sem imprimir valores.

Correção adicional feita nesta continuação:

- O validator agora reporta categorias granulares (`inline_button_marker`, `job_id_leak`, `router_preflight_leak`, `raw_log_or_json_dump`, `management_boilerplate`, `missing_actionability`) em vez de um bucket genérico.
- Discovery agora exclui receipts históricos por padrão, porque receipts podem documentar strings bloqueadas como evidência de correção passada e não são necessariamente mensagens Telegram Lucas-ready.

Amostra atual Telegram após filtro de discovery:

- `reports/telegram-noise-contract-sample-2026-06-14-after-discovery-filter.json`
- `status=ok`
- `files_checked=20`
- `failures_count=0`
- `values_printed=false`

## 3) Documentação/receipt/skills

Documentação atualizada:

- `reports/governance/approval-packet-and-telegram-noise-hardening-2026-06-14.md`
- `reports/governance/telegram-noise-contract-tests-2026-06-14.md`
- `reports/governance/sequential-approval-telegram-hardening-1-5-2026-06-14.md`

References de skills atualizadas:

- `hermes-brain-governance/references/approval-packet-completeness-hardening-20260614.md`
- `hermes-brain-governance/references/telegram-noise-contract-validator-20260614.md`
- `hermes-agent/references/telegram-noise-contract-validator-20260614.md`

Receipt desta continuação:

- `areas/operacoes/receipts/hermes-sequential-approval-telegram-hardening-1-5-20260614.md`

## 4) Verificação

Verificações executadas nesta continuação estão registradas no output final da sessão. Gates esperados:

- `py_compile` dos scripts/testes alterados;
- unit tests de approval packet e Telegram noise;
- validação JSON das amostras;
- validator dos 3 approval packets corrigidos;
- discovery Telegram atual com `failures_count=0`;
- Brain Health;
- Operational docs guard;
- focused credential hygiene scan;
- `git diff --check` nos artefatos relevantes.

## 5) Resultado e pendências

Resultado concluído:

- 3 approval packets críticos foram saneados documentalmente e agora passam no validator.
- Telegram noise/actionability tem gate local mais forte e amostra discovery atual sem falhas.
- Nenhuma ação externa, runtime ou produção foi executada.

Ainda há backlog:

- A amostra de approval packets depois dos 3 corrigidos caiu de 10 falhas para 7 falhas restantes em 10 arquivos.
- Esses 7 são backlog documental de completeness; não autorizam execução e não são incidentes de runtime.

Próximo passo recomendado:

- Fazer uma nova wave curta para corrigir os próximos 3 approval packets da amostra atual, ou transformar o validator em uma rotina local/silent-OK existente se Lucas quiser monitoramento recorrente sem Telegram noise.
