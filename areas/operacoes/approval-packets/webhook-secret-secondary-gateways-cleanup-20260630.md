# Approval packet — limpar WEBHOOK_SECRET herdado em gateways secundários

Data: 2026-06-30
Dono: Operações Hermes / runtime governance
Status: **executado em 2026-06-30T10:17Z com aprovação de Lucas “Fazer do 1 ao 4”; readback OK**
Classificação: A2/A3 runtime scoped restart de gateways secundários

## Pedido / decisão Mesa COO

Lucas escolheu **Fazer** na decisão Mesa COO 2026-06-30 para validar o packet de limpeza da superfície `WEBHOOK_SECRET` herdada em gateways secundários.

Escopo desta etapa: **pré-check read-only + packet escopado/validado**.

Não executado nesta etapa:

- nenhum restart;
- nenhum kill/SIGTERM;
- nenhum Docker/VPS/Traefik;
- nenhuma alteração de cron;
- nenhuma alteração de secret/Doppler;
- nenhum write externo;
- nenhum valor de secret impresso.

## Evidência read-only

Fonte: inspeção `/proc/<pid>/environ` por `HERMES_HOME` exato, sem imprimir valores.

```json
{
  "values_printed": false,
  "profiles": [
    {
      "profile": "lk-finance",
      "pid": 75795,
      "home": "/opt/data/profiles/lk-finance",
      "start_utc": "2026-06-29T16:56:24Z",
      "api_enabled": false,
      "api_key_present": false,
      "webhook_enabled": false,
      "webhook_secret_present": true,
      "webhook_port_present": false,
      "webhook_host_present": false,
      "telegram_token_present": true,
      "doppler_token_present": false,
      "max_iterations": "90"
    },
    {
      "profile": "spiti-atendimento",
      "pid": 76408,
      "home": "/opt/data/profiles/spiti-atendimento",
      "start_utc": "2026-06-29T16:56:36Z",
      "api_enabled": false,
      "api_key_present": false,
      "webhook_enabled": false,
      "webhook_secret_present": true,
      "webhook_port_present": false,
      "webhook_host_present": false,
      "telegram_token_present": true,
      "doppler_token_present": false,
      "max_iterations": "90"
    }
  ]
}
```

## Leitura de arquivos de profile

Fonte: `.env` e `config.yaml`, reportando apenas presença/ausência/status.

- `spiti-atendimento`:
  - `.env` existe;
  - `.env` **não** contém `WEBHOOK_SECRET`;
  - `.env` **não** contém `API_SERVER_KEY`;
  - `TELEGRAM_ALLOWED_USERS` presente;
  - `config_version=30`.
- `lk-finance`:
  - `.env` existe;
  - `.env` tem `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false`;
  - `.env` **não** contém `WEBHOOK_SECRET`;
  - `.env` **não** contém `API_SERVER_KEY`;
  - `TELEGRAM_ALLOWED_USERS` presente;
  - `config_version=30`.

Conclusão: está **correto** que `WEBHOOK_SECRET` não esteja no `.env` dos profiles. A fonte canônica de secrets deve ser Doppler/broker central, não `.env` local. O problema não é ausência no `.env`; o problema é o segredo aparecer no **ambiente vivo** de profiles secundários que não possuem superfície webhook.

## Diagnóstico

Os dois gateways estão conectados, mas vivos com `WEBHOOK_SECRET` presente no ambiente apesar de `WEBHOOK_ENABLED=false`.

Isso viola o contrato de runtime scoped:

- secrets não devem ser persistidos em `.env` local;
- integrações/CLIs devem passar pelo Central Integration Auth Broker;
- runtime secrets necessários devem vir do Doppler/helper/broker em processo escopado;
- profiles secundários sem API/webhook própria devem nascer sem `API_SERVER_KEY`/`WEBHOOK_SECRET` no env vivo.

Portanto, a correção não é “colocar no `.env`”; é limpar herança indevida do processo vivo e garantir injeção escopada somente quando o profile realmente precisa daquele secret.

Também há indício de env/runtime antigo: ambos estão com `HERMES_MAX_ITERATIONS=90`, enquanto o watchdog global atual declara:

- `spiti-atendimento`: `max_iterations=55`;
- `lk-finance`: `max_iterations=50`.

O script atual `/opt/data/scripts/hermes_all_gateway_watchdog.py` já contém lógica para limpar no start:

- `API_SERVER_ENABLED=false`;
- `WEBHOOK_ENABLED=false`;
- unset `API_SERVER_KEY`, `API_SERVER_PORT`, `API_SERVER_HOST`;
- unset `WEBHOOK_PORT`, `WEBHOOK_SECRET`, `WEBHOOK_HOST`;
- unset `DOPPLER_TOKEN`;
- mapear apenas o token Telegram necessário por alias Doppler quando aplicável.

Portanto, a correção provável não exige editar secrets nem config: basta **drain/restart escopado** dos dois gateways para nascerem pelo launcher atual limpo.

## Execução proposta — Opção A recomendada

Executar somente se Lucas aprovar a execução runtime.

Alvos exatos:

- `spiti-atendimento` — `HERMES_HOME=/opt/data/profiles/spiti-atendimento` — PID atual pré-check `76408`.
- `lk-finance` — `HERMES_HOME=/opt/data/profiles/lk-finance` — PID atual pré-check `75795`.

Ação:

1. Revalidar imediatamente antes da ação que os PIDs ainda são gateways reais com `HERMES_HOME` exato.
2. Enviar `SIGTERM` somente para esses PIDs se continuarem correspondendo ao escopo.
3. Aguardar drenagem curta.
4. Iniciar somente os dois profiles pelo mesmo contrato do watchdog atual:
   - `spiti-atendimento`: `max_iterations=55`, `telegram_token_env=SPITI_ATENDIMENTO_TELEGRAM_BOT_TOKEN`;
   - `lk-finance`: `max_iterations=50`, `doppler_profile=lk-finance`, `telegram_token_env=LK_FINANCE_TELEGRAM_BOT_TOKEN`.
5. Verificar `/proc/<new_pid>/environ` com booleans apenas.
6. Verificar `gateway_state.json`/log recente e Telegram `connected` sem imprimir tokens.
7. Registrar receipt.

## Comando de execução sugerido

> Executar somente após aprovação explícita da execução runtime.

```bash
python3 - <<'PY'
import importlib.util, os, signal, time
from pathlib import Path

spec = importlib.util.spec_from_file_location('gw', '/opt/data/scripts/hermes_all_gateway_watchdog.py')
gw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gw)

targets = {
    'lk-finance': {
        'home': '/opt/data/profiles/lk-finance',
        'pid': '75795',
        'max_iterations': '50',
        'doppler_profile': 'lk-finance',
        'telegram_token_env': 'LK_FINANCE_TELEGRAM_BOT_TOKEN',
    },
    'spiti-atendimento': {
        'home': '/opt/data/profiles/spiti-atendimento',
        'pid': '76408',
        'max_iterations': '55',
        'doppler_profile': None,
        'telegram_token_env': 'SPITI_ATENDIMENTO_TELEGRAM_BOT_TOKEN',
    },
}

for name, t in targets.items():
    pid = t['pid']
    live = gw.live_gateways(t['home'])
    pids = [p for p, env, argv in live]
    if pid not in pids:
        raise SystemExit(f'{name}: scoped pid mismatch before restart; live={pids}')
    os.kill(int(pid), signal.SIGTERM)

for name, t in targets.items():
    deadline = time.time() + 20
    while time.time() < deadline:
        if not Path(f"/proc/{t['pid']}").exists():
            break
        time.sleep(0.5)
    gw.start_profile(name, t['home'], t['max_iterations'], t['doppler_profile'], t['telegram_token_env'])

# bounded wait; verification should be performed separately and printed sanitized
for _ in range(25):
    time.sleep(1)
    ok = True
    for name, t in targets.items():
        live = gw.live_gateways(t['home'])
        safe = [p for p, env, argv in live if not gw.unsafe_surface(env)]
        if len(safe) != 1:
            ok = False
    if ok:
        break
PY
```

## Readback obrigatório após execução

Critérios de sucesso para cada profile:

| Gate | Esperado |
|---|---|
| gateway vivo por `HERMES_HOME` exato | `1` processo |
| PID novo | diferente do PID pré-check |
| Telegram token | presente |
| `DOPPLER_TOKEN` no filho | ausente |
| `API_SERVER_ENABLED` | `false` ou ausente |
| `API_SERVER_KEY` | ausente |
| `WEBHOOK_ENABLED` | `false` ou ausente |
| `WEBHOOK_SECRET` | ausente |
| `WEBHOOK_PORT/HOST` | ausentes |
| `HERMES_MAX_ITERATIONS` | `55` para SPITI Atendimento; `50` para LK Finance |
| logs/gateway state | Telegram connected/polling |

## Rollback

Se um profile não voltar:

1. Não tocar Docker/VPS/Traefik/Main.
2. Reexecutar somente `start_profile(...)` do profile afetado com o contrato acima.
3. Se token Doppler/alias falhar, bloquear e reportar presença/ausência do secret por nome apenas:
   - `SPITI_ATENDIMENTO_TELEGRAM_BOT_TOKEN`;
   - `LK_FINANCE_TELEGRAM_BOT_TOKEN`.
4. Se continuar falhando, manter apenas o profile afetado como incidente e não reiniciar outros gateways.

## Não-ações preservadas

- Não altera Doppler/secrets.
- Não imprime secret/token/preview.
- Não muda `.env`/`config.yaml` nesta opção.
- Não muda cron registry.
- Não cria gateway novo fora desses dois profiles.
- Não toca Main/default, Docker, VPS, Traefik ou rede.
- Não faz write externo de negócio.

## Execução realizada

Aprovação explícita posterior de Lucas: **“Fazer do 1 ao 4”**.

Execução em `2026-06-30T10:17Z`:

- Revalidado antes da ação que os PIDs antigos ainda correspondiam ao `HERMES_HOME` exato.
- Enviado `SIGTERM` somente para:
  - `lk-finance` PID antigo `75795`;
  - `spiti-atendimento` PID antigo `76408`.
- Ambos drenaram (`drained=true`).
- Reiniciados somente os dois profiles pelo `start_profile(...)` do watchdog atual.

Readback pós-execução:

| Profile | PID novo | PID mudou | Telegram | API key | Webhook secret | `DOPPLER_TOKEN` | `HERMES_MAX_ITERATIONS` |
|---|---:|---|---|---|---|---|---:|
| `lk-finance` | `870870` | sim | connected | ausente | ausente | ausente | `50` |
| `spiti-atendimento` | `870871` | sim | connected | ausente | ausente | ausente | `55` |

Critérios de sucesso atingidos:

- `unsafe_surface=[]` nos dois profiles;
- `WEBHOOK_SECRET` ausente no env vivo;
- `WEBHOOK_ENABLED=false`;
- `API_SERVER_KEY` ausente;
- `telegram_token_present=true`;
- `gateway_state=running` e Telegram `connected`;
- nenhum Docker/VPS/Traefik/Main/default/cron/secrets tocado.

## Status

Execução escopada concluída e validada.
