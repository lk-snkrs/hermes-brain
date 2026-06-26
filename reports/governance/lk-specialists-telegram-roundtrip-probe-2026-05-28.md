# LK Specialists — Telegram round-trip probe

Data: 2026-05-28  
Origem: Mesa COO — Decisão 2/3  
Resposta de Lucas: `Seguir`  
Status: probe enviado; round-trip conversacional depende da resposta de Lucas em cada bot

## Escopo aprovado

Validar a superfície conversacional dos especialistas LK Shopify, LK Trends e LK Ops/Atendimento, sem writes externos.

## Verificações locais/read-only

Profiles existentes e com runtime vivo:

- `lk-shopify` — PID observado `31088`, `HERMES_HOME=/opt/data/profiles/lk-shopify`, Telegram conectado, `API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false`, `HERMES_MAX_ITERATIONS=50`.
- `lk-trends` — PID observado `801`, `HERMES_HOME=/opt/data/profiles/lk-trends`, Telegram conectado, `API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false`, `HERMES_MAX_ITERATIONS=45`.
- `lk-ops` — PID observado `29310`, `HERMES_HOME=/opt/data/profiles/lk-ops`, Telegram conectado, `API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false`, `HERMES_MAX_ITERATIONS=40`.

Observação: `lk-ops` ainda tem estado histórico de webhook `retrying` por rota sem HMAC, mas o processo vivo foi verificado com `WEBHOOK_ENABLED=false`; a superfície Telegram aparece conectada.

## Probes enviados via Bot API

Foram enviados testes curtos para Lucas no Telegram, um por bot especialista:

- `@LKShopify_HermesBot` — `send_ok=true`, `message_id=350`.
- `@LKTrends_HermesBot` — `send_ok=true`, `message_id=127`.
- `@LKOps_HermesBot` — `send_ok=true`, `message_id=48`.

Tokens foram usados apenas localmente a partir dos profiles e não foram impressos no output.

## Limites preservados

Nenhum write executado em:

- Shopify;
- Tiny;
- cliente/fornecedor/WhatsApp/e-mail;
- GMC/Klaviyo/Meta/campanha;
- Docker/VPS/Main gateway;
- secrets/configs.

## Resultado

A prova de **outbound bot → Lucas** foi bem-sucedida para os três bots.

A prova de **round-trip real Lucas → bot → resposta do agente** ainda depende de Lucas responder nos três chats dos bots. Após as respostas, validar nos logs:

- inbound message no profile correto;
- resposta gerada no escopo do especialista;
- ausência de write externo;
- tempo de resposta aceitável;
- receipt final no Brain.

## Próximo passo da Mesa

Enviar Decisão 3/3: política de SPITI sobre crons/rituais locais.
