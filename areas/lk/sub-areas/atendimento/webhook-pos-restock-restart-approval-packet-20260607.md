# LK POS restock webhook — approval packet de restart

Data UTC: 2026-06-07T12:00:29Z

## Contexto

Fluxo esperado:

Shopify `orders/paid` POS → Vercel Hermes Webhook → Hermes Gateway público → handler determinístico `lk_shopify_pos_restock` → `/opt/data/scripts/lk_store_sale_restock_alert.py` → WhatsApp grupo LK Team.

## Evidência atual

- Endpoint local/público do gateway responde health OK.
- A rota `/webhooks/lk-shopify-pos-restock` ainda caiu em retorno genérico `202 {"status":"accepted", ...}` no probe assinado anterior.
- Esse retorno não prova execução do handler POS; indica caminho genérico/LLM.
- Handler/config estão presentes em `/opt/data/config.yaml` e no código instalado, mas o processo vivo é anterior à ativação/carregamento esperado.

## Alvo real identificado

- Container: `hermes-agent-5ajw-hermes-telegram-1`
- Container id/hostname: `a921c308b1df`
- Processo dono da porta 8644: PID 1 dentro do container
- `HERMES_HOME=/opt/data`
- `WEBHOOK_ENABLED=true`
- `WEBHOOK_PORT=8644`
- Docker restart policy: `unless-stopped`
- Serviço compose: `hermes-telegram`
- Projeto compose: `hermes-agent-5ajw`
- Config compose origem: `/docker/hermes-agent-5ajw/docker-compose.yml`
- Traefik expõe `crisp-hooks.srv1331756.hstgr.cloud` e `hermes-webhooks.lucascimino.com` para porta interna 8644.
- URL canônica operacional preferida neste fluxo: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.

## Ação produtiva proposta

Restart controlado somente do container `hermes-agent-5ajw-hermes-telegram-1`, sem backfill e sem disparo real de WhatsApp:

1. Snapshot read-only pré-restart:
   - `docker inspect hermes-agent-5ajw-hermes-telegram-1`
   - health local `http://127.0.0.1:8644/health`
   - registrar `StartedAt` e `RestartCount`.
2. Executar `docker restart --time 30 hermes-agent-5ajw-hermes-telegram-1`.
3. Verificar:
   - novo `StartedAt`/`RestartCount`;
   - `http://127.0.0.1:8644/health` OK;
   - domínio público/Traefik OK;
   - probe Shopify-assinado não-POS contra Vercel;
   - retorno determinístico do handler, não `202 accepted` genérico.
4. Se falhar:
   - checar `docker logs --since` e health;
   - se container não voltar: `docker start hermes-agent-5ajw-hermes-telegram-1`;
   - se rota continuar genérica: não declarar OK; reportar bloqueio com logs e próximo patch necessário.

## Guardrails

- Não alterar Shopify/Tiny/WhatsApp/n8n/Klaviyo/CRM.
- Não fazer backfill.
- Não enviar mensagem real ao grupo LK Team no teste.
- Não expor segredos; usar Doppler/helper só para assinatura de probe, sem imprimir valor.
- Não reiniciar outros containers/perfis.

## Status

Aguardando aprovação explícita do Lucas para restart produtivo do container `hermes-agent-5ajw-hermes-telegram-1` e probe não-POS.
