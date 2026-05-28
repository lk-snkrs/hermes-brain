# LK specialists runtime activation — approval packet

Data/hora de preparo: 2026-05-27 09:44 UTC  
Origem: Mesa COO — decisão 1/4 aprovada por Lucas como `Fazer`  
Escopo deste documento: preparar pacote read-only para provar vivos os especialistas LK Shopify, LK Trends e LK Ops/Atendimento sem misturar execução no perfil errado.

## Pedido limpo

Executar uma ativação/verificação escopada dos três especialistas LK abaixo, somente para provar runtime Telegram vivo no perfil correto:

1. LK Shopify — profile `/opt/data/profiles/lk-shopify`.
2. LK Trends — profile `/opt/data/profiles/lk-trends`.
3. LK Ops/Atendimento — profile `/opt/data/profiles/lk-ops`.

## Evidência read-only coletada

### Estado local de configuração

- Os três profiles existem em `/opt/data/profiles/`.
- Os três profiles têm `TELEGRAM_BOT_TOKEN` presente localmente; valores não foram lidos nem documentados.
- Os três profiles têm `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` no `.env`.
- Nenhum `API_SERVER_KEY` ou `WEBHOOK_SECRET` está presente nos `.env` dos três profiles.
- `HERMES_MAX_ITERATIONS` local:
  - LK Shopify: `50`.
  - LK Trends: `45`.
  - LK Ops: `40`.

### Toolsets Telegram verificados

- LK Shopify Telegram: `clarify`, `file`, `memory`, `session_search`, `skills`, `todo`, `web`.
- LK Trends Telegram: `browser`, `clarify`, `file`, `memory`, `session_search`, `skills`, `todo`, `web`.
- LK Ops Telegram: `clarify`, `file`, `memory`, `session_search`, `skills`, `todo`.
- `terminal` não está habilitado no Telegram desses três profiles.

### Logs recentes

- LK Shopify: logs mostram start em 2026-05-27 01:30 UTC com `max_iterations=50`, `Connected to Telegram (polling mode)`, `Gateway running with 1 platform(s)` e respostas posteriores.
- LK Trends: logs mostram start em 2026-05-26 20:55 UTC com `max_iterations=45`, `Connected to Telegram (polling mode)` e `Gateway running with 1 platform(s)`; havia histórico anterior de tarefas muito lentas, então precisa prova viva atual.
- LK Ops: logs mostram start em 2026-05-26 20:55 UTC com `max_iterations=40`, `Connected to Telegram (polling mode)` e `Gateway running with 1 platform(s)`.

### Processos vivos no namespace inspecionado

- Processo principal Hermes: `HERMES_HOME=/opt/data` ativo.
- LK Growth: `HERMES_HOME=/opt/data/profiles/lk-growth` ativo.
- Não foi observado processo vivo atual para `lk-shopify`, `lk-trends` ou `lk-ops` durante a inspeção read-only desta sessão.

## Ação proposta se Lucas aprovar este pacote

Executar apenas a ativação/verificação local dos três profiles LK:

1. Fazer backup leve dos arquivos de runtime antes de tocar em qualquer coisa:
   - `/opt/data/profiles/lk-shopify/.env` e `config.yaml`.
   - `/opt/data/profiles/lk-trends/.env` e `config.yaml`.
   - `/opt/data/profiles/lk-ops/.env` e `config.yaml`.
2. Start/restart somente dos gateways dos três profiles:
   - `HERMES_HOME=/opt/data/profiles/lk-shopify`.
   - `HERMES_HOME=/opt/data/profiles/lk-trends`.
   - `HERMES_HOME=/opt/data/profiles/lk-ops`.
3. Forçar runtime local seguro para esses profiles:
   - API server off.
   - Webhook off.
   - Sem Docker/VPS/Traefik/Main Hermes.
4. Verificar por `/proc/<pid>/environ`:
   - `HERMES_HOME` exato de cada profile.
   - `HERMES_MAX_ITERATIONS` esperado.
   - `API_SERVER_ENABLED=false`.
   - `WEBHOOK_ENABLED=false`.
5. Verificar logs:
   - `Agent budget: max_iterations=...` correto.
   - `Connected to Telegram (polling mode)`.
   - `Gateway running with 1 platform(s)`.
   - Ausência de `Port already in use`, webhook retry, API bind, token error ou provider-auth failure.
6. Pedir/usar teste mínimo de round-trip Telegram quando necessário:
   - Lucas envia mensagem curta para cada bot ou Hermes registra o próximo inbound já existente.
   - Confirmar resposta sem vazar metadados técnicos.
7. Registrar receipt sanitizado no Brain com:
   - profile, status, horário, evidência de log, PID/HERMES_HOME, limites ativos e não-ações.

## O que permanece bloqueado

- Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/CRM writes.
- Preço, estoque, disponibilidade, reserva, promessa comercial ou campanha.
- WhatsApp/e-mail/cliente/fornecedor.
- Docker, VPS, Traefik, root/SSH, volumes, networks, compose e restart do Main Hermes.
- Criação de cron novo ou mudança de delivery/cadência.
- Exposição, impressão ou cópia de tokens/secrets.
- Ativação de webhook `lk-shopify-pos-restock` no LK Ops; permanece `webhook.enabled=false` até pacote separado de HMAC/webhook.

## Risco

- Baixo se limitado aos três profiles e com API/webhook off.
- Risco principal: iniciar profile com env herdado errado e tentar bind de API/webhook; mitigação: limpar/forçar env off e verificar `/proc`.
- Risco secundário: bot conectado mas lento; mitigação: testar round-trip e manter `max_iterations` reduzido.

## Rollback

- Encerrar somente os processos dos profiles afetados, identificados por `HERMES_HOME=/opt/data/profiles/<profile>` e `hermes gateway run`.
- Restaurar backups de `.env`/`config.yaml` se algum ajuste local for necessário durante a ativação.
- Não tocar no processo principal `HERMES_HOME=/opt/data`, LK Growth, Docker, VPS ou Traefik.

## Frase de aprovação sugerida

Aprovo ativar/verificar somente LK Shopify, LK Trends e LK Ops, com API/webhook off, sem Docker/VPS/Main Hermes e sem writes externos; registrar receipt e rollback no Brain.

## Status deste pacote

Preparado em modo read-only/local. Nenhum gateway foi iniciado/reiniciado por este pacote; nenhuma ação externa foi executada.
