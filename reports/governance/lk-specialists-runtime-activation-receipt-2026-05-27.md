# LK specialists runtime activation — receipt

Data/hora: 2026-05-27 09:49 UTC  
Aprovação: Lucas aprovou ativação/verificação escopada via decisão da Mesa COO e confirmação de escopo.  
Escopo aprovado: LK Shopify, LK Trends e LK Ops/Atendimento; API/webhook off; sem Docker/VPS/Main Hermes; sem writes externos.

## Resultado

Ativação/verificação local concluída para os três especialistas LK.

## Profiles verificados

### LK Shopify

- Profile: `/opt/data/profiles/lk-shopify`.
- Runtime vivo: sim.
- Evidência `/proc`: `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- `HERMES_MAX_ITERATIONS=50`.
- `API_SERVER_ENABLED=false`.
- `WEBHOOK_ENABLED=false`.
- `API_SERVER_KEY` ausente no ambiente vivo.
- `WEBHOOK_SECRET` ausente no ambiente vivo.
- Log: `Starting Hermes Gateway`, `Agent budget: max_iterations=50`, `Connected to Telegram (polling mode)`, `Gateway running with 1 platform(s)` em 2026-05-27 09:48 UTC.

### LK Trends

- Profile: `/opt/data/profiles/lk-trends`.
- Runtime vivo: sim.
- Evidência `/proc`: `HERMES_HOME=/opt/data/profiles/lk-trends`.
- `HERMES_MAX_ITERATIONS=45`.
- `API_SERVER_ENABLED=false`.
- `WEBHOOK_ENABLED=false`.
- `API_SERVER_KEY` ausente no ambiente vivo.
- `WEBHOOK_SECRET` ausente no ambiente vivo.
- Log: `Starting Hermes Gateway`, `Agent budget: max_iterations=45`, `Connected to Telegram (polling mode)`, `Gateway running with 1 platform(s)` em 2026-05-27 09:48 UTC.

### LK Ops / Atendimento

- Profile: `/opt/data/profiles/lk-ops`.
- Runtime vivo: sim.
- Evidência `/proc`: `HERMES_HOME=/opt/data/profiles/lk-ops`.
- `HERMES_MAX_ITERATIONS=40`.
- `API_SERVER_ENABLED=false`.
- `WEBHOOK_ENABLED=false`.
- `API_SERVER_KEY` ausente no ambiente vivo.
- `WEBHOOK_SECRET` ausente no ambiente vivo.
- Log: `Starting Hermes Gateway`, `Agent budget: max_iterations=40`, `Connected to Telegram (polling mode)`, `Gateway running with 1 platform(s)` em 2026-05-27 09:48 UTC.

## Não ações

- Não houve Docker/VPS/Traefik/root/SSH/volume/network/compose.
- Não houve restart do Hermes Main (`HERMES_HOME=/opt/data`).
- Não houve alteração no LK Growth.
- Não houve Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/CRM write.
- Não houve WhatsApp/e-mail/cliente/fornecedor.
- Não houve cron novo.
- Nenhum token/secret foi impresso ou salvo no Brain.
- Webhook `lk-shopify-pos-restock` permaneceu desligado; nenhum HMAC/webhook foi ativado.

## Backup local

Backups pré-ativação foram salvos localmente em diretório restrito sob:

`/opt/data/backups/lk-specialists-runtime-activation-20260527T094817Z`

Inclui `config.yaml` e `.env` dos três profiles. O diretório é local/restrito e não deve ser publicado.

## Rollback

Para rollback, encerrar somente processos cujo ambiente vivo tenha:

- `HERMES_HOME=/opt/data/profiles/lk-shopify`; ou
- `HERMES_HOME=/opt/data/profiles/lk-trends`; ou
- `HERMES_HOME=/opt/data/profiles/lk-ops`.

Depois, restaurar `config.yaml`/`.env` a partir do backup local se necessário. Não tocar em `HERMES_HOME=/opt/data`, Docker, VPS ou Traefik.

## Pendência honesta

A prova técnica de runtime vivo está concluída por processo e logs. A prova de round-trip conversacional depende de mensagem real enviada/recebida em cada bot após esta ativação; quando Lucas mandar uma mensagem curta para cada especialista, registrar o receipt de resposta se necessário.
