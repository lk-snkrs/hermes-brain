# LK POS restock webhook — approval packet de restart

> **Documento histórico / DO NOT RUN:** comandos e caminhos citados são evidência/registro; não executar sem aprovação escopada, backup, rollback e readback.


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

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `LK POS restock webhook — approval packet de restart` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `LK POS restock webhook — approval packet de restart` no caminho `areas/lk/sub-areas/atendimento/webhook-pos-restock-restart-approval-packet-20260607.md`.
- Owner operacional: LK Atendimento / CRM / Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos, coleções, arquivos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer mensagem a cliente, WhatsApp/e-mail, campanha, Chatwoot/webhook/runtime, contato externo, preço, disponibilidade, reserva, negociação, reembolso ou logística sem aprovação específica.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: readback do artefato/preview, ledger/receipt local, amostragem de contatos/conversas quando aplicável e confirmação de zero envio externo não aprovado.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
