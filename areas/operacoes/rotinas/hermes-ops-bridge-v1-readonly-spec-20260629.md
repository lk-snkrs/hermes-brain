# Hermes Ops Bridge v1 — especificação read-only

Data: 2026-06-29  
Status: especificação local/documental; **Ops Bridge v1 local read-only implementado em 2026-06-29** após nova aprovação explícita de Lucas.  
Implementação: `/opt/data/scripts/hermes_ops_bridge_readonly.py`. Não implementado como runtime persistente, dashboard, API, cron ou superfície externa.

## Objetivo

Criar uma fachada operacional simples sobre ferramentas existentes, começando **somente read-only/local**, para reduzir custo cognitivo.

## Princípio

Ops Bridge não substitui:

- `hermes-cli-run`;
- `hermes-cli-integrations`;
- Doppler-first;
- Brain/receipts;
- approval packets;
- ferramentas oficiais como Shopify CLI.

Ele apenas organiza comandos seguros e outputs executivos.

## Comandos candidatos v1

| Comando lógico | Fonte atual | Mutação? | Saída esperada |
|---|---|---:|---|
| `status` | `hermes status --all`, `/proc`, cron registry | Não | resumo profiles/crons/gateway |
| `health` | Brain health, watchdog latest, Memory/Honcho reports | Não | green/watch/action_required |
| `smoke` | `hermes-cli-integrations smoke` | Não | integração/status/código sanitizado |
| `logs` | logs locais sanitizados | Não | últimos erros agrupados |
| `cron-inventory` | cron registries/list | Não | total, active, paused, non-ok |
| `profile-map` | profiles config + live PIDs | Não | configured/active/functioning |
| `packet` | templates Brain | Local-write docs | approval packet local |
| `receipt` | Memory OS receipt writer | Local-write docs | receipt local validado |

## Bloqueios v1

Não entra no v1 sem nova aprovação:

- restart;
- deploy;
- Docker/VPS/Traefik;
- cron create/update/remove/pause/resume;
- external sends;
- credential login/reauth;
- mutation Shopify/Tiny/Klaviyo/Supabase/Notion/etc.;
- dashboard/API pública;
- novos webhooks.

## Acceptance criteria para implementação futura

Antes de implementar como script/CLI:

1. Especificação aprovada por Lucas.
2. Lista de comandos e fontes com redaction.
3. Teste de higiene de credenciais.
4. Saída executiva Telegram-safe.
5. Sem side effects por padrão.
6. Todo comando mutável inexistente ou hard-blocked.
7. Receipt do piloto read-only.

## Primeiro piloto executado

Com nova aprovação explícita de Lucas, o primeiro piloto foi implementado como script local read-only persistente em `/opt/data/scripts/hermes_ops_bridge_readonly.py`. O script permanece sem runtime, cron, dashboard/API ou mutação externa; relatórios locais podem ser gerados por redirecionamento externo quando necessário.
