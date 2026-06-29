# Approval packet — ativação controlada do main/default gateway para política Shopify CLI oficial — 2026-06-28

- **Status:** prepared / aguardando aprovação separada para executar restart
- **Pedido Mesa COO:** `Fazer` na decisão 1/3 de 2026-06-28
- **Dono:** Operações Hermes / Gateway principal
- **Risco:** A3 runtime sensível (gateway principal pode interromper Telegram/API/webhook/cron)
- **values_printed:** false
- **External writes:** 0
- **Shopify/Tiny/GMC/Klaviyo/Meta writes:** 0
- **Docker/VPS/Traefik changes:** 0
- **Preparado em:** 2026-06-28T10:46:47.840216+00:00

## 1. Objetivo

Recarregar o **gateway main/default** (`HERMES_HOME=/opt/data`, PID 1 atual) para que o runtime principal carregue a regra nova de Shopify Admin GraphQL:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'
```

A política documental e os especialistas já foram atualizados/reiniciados; a lacuna restante é **runtime activation do main/default**, não auth/config Shopify.

## 2. Evidência consultada

- `reports/daily-consolidation/2026-06-28.md` linhas 24–27, 42–47 e 75–79: política aplicada, especialistas reiniciados, main/default pendente.
- `reports/governance/shopify-official-cli-all-agents-force-2026-06-27.md`: 59/59 instruções, 28/28 jobs Shopify-related e 109 skill files com regra oficial; mutation block OK.
- `reports/governance/shopify-official-cli-gateway-restart-2026-06-27.md`: 11 gateways secundários reiniciados e validados; main/default não reiniciado por guardrail de execução dentro do gateway.
- `reports/hermes-continuous-improvement/2026-06-28.md`: gateway restart/Docker/VPS/Traefik não tocados no run diário.
- Snapshot sanitizado atual: `reports/governance/main-default-gateway-shopify-cli-activation-prestate-2026-06-28.json`.

## 3. Pré-estado atual resumido

Leitura read-only atual por `/proc` e `hermes gateway status`:

- Main/default: `HERMES_HOME=/opt/data`, PID 1, API/webhook habilitados como esperado para o gateway principal.
- Especialistas vivos: `lc-claude-cli`, `lk-collection-optimizer`, `lk-content`, `lk-finance`, `lk-growth`, `lk-ops`, `lk-shopify`, `lk-stock`, `lk-trends`, `mordomo`, `spiti`, `spiti-atendimento`.
- Especialistas: API/webhook fechados no env vivo (`API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false`) no snapshot atual.
- Valores de token/API key/webhook secret não foram impressos; só booleans.

## 4. Escopo autorizado por este packet

Se Lucas aprovar este packet separadamente, executar **somente** o restart do `main/default` fora do processo do gateway, seguido de readback.

### Permitido

1. Capturar roster pré-restart dos gateways (`/proc/*/cmdline` + `/proc/*/environ`, sanitizado).
2. Rodar o comando de restart do default fora do processo do gateway.
3. Validar main/default e restaurar apenas especialistas que estavam vivos antes, caso o restart do default derrube algum sibling.
4. Rodar smoke read-only do Shopify CLI oficial e bloqueio de mutation sem `--allow-mutations`.
5. Registrar receipt sanitizado no Brain.

### Bloqueado sem nova aprovação

- Docker/VPS/Traefik/system service changes.
- `--replace`/kill amplo de gateways sem diagnóstico pós-restart.
- Mutations Shopify, Tiny, GMC, Klaviyo, Meta, Supabase, banco, e-mail/WhatsApp/customer sends.
- Mover/copiar secrets, imprimir tokens/cache OAuth/API keys/webhook secrets.
- Alterar cron schedule/delivery.

## 5. Comando exato de execução (fora do gateway)

Rodar de uma shell **fora do processo do gateway principal**. Não executar pela Mesa/cron atual.

```bash
cd /opt/data
HERMES_HOME=/opt/data PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages env -u _HERMES_GATEWAY   /opt/data/hermes-0.15.1-venv/bin/hermes gateway restart
```

Alternativa operacional equivalente: Lucas enviar `/restart` ao bot do gateway principal, se esse canal estiver disponível e a interrupção temporária for aceitável.

## 6. Readback obrigatório pós-restart

Depois do retorno do gateway, validar antes de declarar completo:

```bash
# versão/runtime ativo
HERMES_HOME=/opt/data PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages   /opt/data/hermes-0.15.1-venv/bin/hermes --version

# health local do API principal
curl -fsS --max-time 5 http://127.0.0.1:8642/health

# estado gateway/cron/webhook
HERMES_HOME=/opt/data PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages   /opt/data/hermes-0.15.1-venv/bin/hermes gateway status
HERMES_HOME=/opt/data PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages   /opt/data/hermes-0.15.1-venv/bin/hermes cron status
HERMES_HOME=/opt/data PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages   /opt/data/hermes-0.15.1-venv/bin/hermes webhook list
```

Também validar:

- PID main/default novo ou start time posterior à aprovação.
- `HERMES_HOME=/opt/data` no env vivo do PID main/default.
- logs com startup completo: Telegram/API/webhook conectados e `Cron ticker started`.
- roster final contém todos os especialistas que estavam vivos no pré-estado.
- API/webhook continuam fechados nos especialistas.
- `hermes_all_gateway_watchdog.py` silent-OK.
- Shopify CLI oficial read-only OK e mutation sem `--allow-mutations` bloqueada.

## 7. Rollback / contenção

Se o restart falhar ou deixar especialista ausente:

1. Não escalar para Docker/VPS/Traefik automaticamente.
2. Reenumerar `/proc` e `gateway status`; se houver corrida `already running`, tratar como não-fatal até confirmar estado vivo.
3. Restaurar somente especialistas que estavam vivos no pré-estado via watchdog local:

```bash
/opt/data/scripts/hermes_all_gateway_watchdog.py
```

4. Se o main/default não voltar, bloquear como incidente A3/A4 e pedir aprovação específica para intervenção fora do gateway/container.

## 8. Critério de sucesso

- Main/default reiniciado e vivo com `HERMES_HOME=/opt/data`.
- Telegram/API/webhook/cron do main validados.
- Todos os especialistas do pré-estado contabilizados pós-restart.
- Shopify CLI oficial carregado/validado no runtime principal; raw/wrapper não usado como caminho normal.
- Receipt criado com `values_printed=false` e `external_writes=0`.

## 9. Próxima decisão para Lucas

Aprovar ou não a execução do restart controlado acima.

Se aprovado, aceitar a interrupção temporária do Telegram/API principal durante o restart e executar somente o escopo do item 4.
