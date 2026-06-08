# Hermes Doppler-first — Fase 4 runtime scoped: lk-content

Data UTC: 2026-06-07T15:42:52Z

## Escopo aprovado

Lucas aprovou executar:

- item 1: fechar Fase 4 Doppler runtime;
- item 3: padronizar `lk-content` runtime.

Execução mantida no menor escopo operacional possível: `lk-content` + watchdog global que recupera esse perfil. Não houve Docker/VPS/Traefik/Shopify/Tiny/Klaviyo/email/WhatsApp write.

## Mudanças aplicadas

### Helper universal Doppler

Arquivo: `/opt/data/scripts/hermes_doppler.py`

- `run` deixou de depender de `doppler run` como child wrapper.
- O helper agora busca os secrets no processo curto do helper, injeta no ambiente do comando e executa o comando diretamente.
- `DOPPLER_TOKEN` é removido do ambiente do child antes do `exec`.
- Novo modo: `run --profile <profile> -- COMMAND ...` injeta apenas os secrets esperados do perfil.

### Watchdog global de gateways

Arquivo: `/opt/data/scripts/hermes_all_gateway_watchdog.py`

- Adicionado `DOPPLER_HELPER=/opt/data/scripts/hermes_doppler.py`.
- Todos os perfis `managed` esperados no watchdog ganharam `doppler_profile`: `mordomo`, `lk-growth`, `spiti`, `lk-ops`, `lk-shopify`, `lk-trends`, `lk-collection-optimizer`, `lk-content`.
- Quando o watchdog precisa iniciar um perfil `managed`, usa:
  - helper Doppler universal;
  - `run --profile <profile>`;
  - API Server e Webhook forçados off;
  - `DOPPLER_TOKEN` removido do child env.
- Reinício real feito agora apenas em `lk-content`; os demais perfis não foram reiniciados.

Backup criado antes do patch:

- `/opt/data/scripts/hermes_all_gateway_watchdog.py.bak-doppler-runtime-20260607T154050Z`

## Pre-state

- `lk-content` tinha gateway vivo antes da intervenção: PID `714`.
- `.env` do perfil: modo `600`, owner `root:root`.
- `HERMES_HOME=/opt/data/profiles/lk-content`.
- API Server e Webhook já estavam `false`.
- Doppler CLI/helper OK, `lc-keys/prd`, secrets esperados do perfil `6/6` presentes.
- `HERMES_HOME=/opt/data/profiles/lk-content hermes cron list`: nenhum job agendado no perfil.

## Restart controlado

Ação feita:

- SIGTERM somente no PID `714` de `lk-content`.
- Nenhum outro gateway foi parado.
- Watchdog global executado manualmente para recuperar `lk-content` pelo caminho Doppler-first.

Post-state observado:

- Novo PID `20911` para `lk-content`.
- `HERMES_HOME=/opt/data/profiles/lk-content`.
- `API_SERVER_ENABLED=false`.
- `WEBHOOK_ENABLED=false`.
- `DOPPLER_PROJECT=lc-keys`.
- `DOPPLER_CONFIG=prd`.
- `DOPPLER_TOKEN_in_child=false`.
- Secrets esperados do perfil presentes no processo: `6/6` por presença booleana, sem valores impressos.
- Telegram conectado em polling mode conforme logs.
- `hermes gateway status` confirmou `lk-content` rodando no PID `20911`.

Nota: `TELEGRAM_BOT_TOKEN` não apareceu em `/proc/<pid>/environ` do child pós-helper, mas o gateway conectou ao Telegram com sucesso. Isso indica que o Hermes/carregamento do perfil continua conseguindo ler a configuração/token do perfil sem precisar expor o token no ambiente do processo verificado.

## Validações realizadas

- `python3 -m py_compile` em helper e watchdog: OK.
- Inventory Doppler dos 8 perfis `managed` do watchdog: `missing_total=0`; presença esperada `mordomo 6/6`, `lk-growth 9/9`, `spiti 5/5`, `lk-ops 8/8`, `lk-shopify 6/6`, `lk-trends 6/6`, `lk-collection-optimizer 5/5`, `lk-content 6/6`.
- Execução direta do helper `run --profile lk-content` com teste booleano: `6/6` secrets esperados presentes; `DOPPLER_TOKEN_in_child=false`; `values_printed=false`.
- Execução manual do watchdog: `rc=0`, stdout vazio.
- Gateway status do perfil: running, PID `20911`.
- Logs recentes: Telegram `Connected to Telegram (polling mode)`, `Gateway running with 1 platform(s)`, cron ticker iniciado.
- Focused secret scan em 5 arquivos alterados/documentados: `0` hits.
- Brain health: `FAIL=0`, `WARN=0`, JSON em `/tmp/brain-health-doppler-phase4-lk-content-20260607.json`.
- Structural audit: `rc=0`, stdout vazio.

## Guardrails preservados

- Sem valores de secret em relatório/log/chat.
- Sem cópia de secrets para Brain/skill/`.env`.
- Sem alteração de Docker/VPS/Traefik/Main.
- Sem alteração externa em sistemas de negócio.
- API Server/Webhook do `lk-content` continuam off.
- Watchdog segue silent-OK.

## Rollback

Se necessário:

1. Restaurar watchdog pelo backup:
   `/opt/data/scripts/hermes_all_gateway_watchdog.py.bak-doppler-runtime-20260607T154050Z`.
2. Reverter o comportamento `run` do helper a partir do backup/git/registro anterior.
3. Reiniciar somente `lk-content` e validar `hermes gateway status` + logs.

## Status

Fase 4 scoped para `lk-content`: concluída e verificada.

`values_printed=false`.
