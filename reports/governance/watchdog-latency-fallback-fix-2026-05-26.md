# Correção do watchdog de latência/fallback — 2026-05-26

## Problema

O watchdog `/opt/data/scripts/hermes_profile_latency_watchdog.py` estava contando linhas de rede do Telegram como se fossem fallback/failover de modelo/provedor.

Exemplos que geravam falso positivo:

- `Telegram fallback IPs active`
- `Auto-discovered Telegram fallback IPs`
- `using seed fallback IPs`
- `trying fallback IPs`

Essas linhas são fallback de transporte/rede do Telegram, não falha de `gpt-5.5` nem fallback para `gpt-5.4-mini`.

## Correção aplicada

- Adicionada regex específica `RE_TELEGRAM_NETWORK_FALLBACK`.
- Adicionado helper `_is_model_or_provider_fallback(line)`.
- O contador de fallback agora ignora fallback de IP do Telegram e mantém detecção de fallback/failover real de modelo/provedor.
- Backup criado antes da edição em `/opt/data/scripts/hermes_profile_latency_watchdog.py.bak-*`.

## Verificação

Com os mesmos logs recentes, o alerta deixou de listar falsos positivos em:

- hermes-geral
- mordomo
- lk-ops
- lk-shopify
- lk-trends
- spiti

O alerta restante ficou restrito a lentidão real do `lk-growth`:

- `lk-growth: 2 respostas ≥180s (máx 1335.1s); 2 respostas ≥300s`

## Estado atual

- Watchdog corrigido localmente.
- Sem restart necessário: o cron/script lê o arquivo a cada execução.
- Não houve alteração de Docker, gateway, secrets, containers ou envio externo.

## Pendente recomendado

- Tratar a causa da lentidão real no LK Growth: contexto pesado/compressão + tarefas longas.
- Se Lucas quiser silêncio total no Telegram para esse watchdog, mover delivery do cron para `local` em uma ação separada e explicitamente aprovada.
