# Migração WhatsApp Oficial — Crisp → Chatwoot (CONCLUÍDA)

Data: 2026-06-11 · Executada por Claude (Cowork) + Lucas · Validada ponta a ponta

## Resultado
O número oficial **+55 11 94956-5000** (WABA "LK Sneakers & Apparels", 1478026007140488, qualidade GREEN) saiu do Crisp e está **100% no Chatwoot self-hosted** (inbox #2 "LK WhatsApp", Channel::Whatsapp provider whatsapp_cloud, phone_number_id 1220780761111140).

- **Recebimento** ✅ cliente → Meta → `https://chat.lkskrs.online/webhooks/whatsapp/+5511949565000` → inbox 2 (Elle tria automaticamente: labels humano/whatsapp-api + atribuição).
- **Envio de agente** ✅ (conversas de serviço são GRATUITAS desde nov/2024 — funciona sem cartão).
- **Crisp removido** como parceiro da WABA (11/jun); 2FA do número foi desativado antes pelo Lucas.
- **Histórico unificado**: 589 conversas / ~11.000 mensagens do Crisp importadas na inbox 2, casadas por telefone (source_id = dígitos). 199 abertas (atividade ≤7d, label `lead-quente-crisp`), 390 resolvidas (label `historico-crisp`). Inbox 5 "Histórico Crisp" restou com 3 conversas web-chat sem telefone. Quando o lead responde, cai na MESMA conversa.

## Peças da configuração
- App Meta: **LK Wts** (1012898997763858), publicado (Live), categoria Compras, privacy policy lksneakers.com.br. Webhook configurado + campo `messages` assinado. App inscrito na WABA (subscribed_apps).
- Token permanente: system user **"Chatwoot"** (61590608915014) com acesso total à WABA e ao app; escopos whatsapp_business_messaging/management. Token guardado APENAS em `channel_whatsapp.provider_config['api_key']` (inbox 2).
- Webhook verify token em `provider_config['webhook_verify_token']`.
- 10 templates Meta sincronizados no canal.

## Lições/gotchas (importante p/ futuro)
1. **"Inactive WhatsApp channel"**: canal com `reauthorization_required` descarta webhooks silenciosamente → `ch.reauthorized!` resolve.
2. **Erro #200 ao enviar com Crisp ainda parceiro**: enquanto a WABA usava a linha de crédito do parceiro, apps próprios não enviavam. Resolvido ao remover o parceiro (conversas de serviço não precisam de cartão).
3. **Imports geram avalanche de jobs**: cada mensagem importada enfileira SendReplyJob (no-op com source_id, mas ~150ms) e WebhookJob p/ Elle. 8.047 webhooks de eco expurgados da fila medium; envios reais atrasam até a fila drenar.
4. Mensagens outgoing importadas DEVEM ter `source_id` (ex.: `crisp:<fingerprint>`) — é o que impede o Chatwoot de re-enviá-las ao cliente.
5. Telefones do Crisp com formato estranho: validador BR rejeita; como origem é WhatsApp, aceitar dígitos 10-15 como E.164.
6. Phone ID da UI do WhatsApp Manager pode vir truncado — confirmar via `GET /{waba}/phone_numbers`.

## Pendências
- **Cartão na WABA** (necessário SÓ para templates/jornadas pelo número oficial). Cartão do Lucas foi recusado ("tipo não aceito") — tentar crédito físico ou via Cobrança e pagamentos do BM.
- Apontar jornadas pro oficial (trocar `SHOPIFY_RECOVERY_INBOX_ID`/`KLAVIYO_RECOVERY_INBOX_ID` 3→2) QUANDO Lucas quiser + cartão ok. Hoje jornadas seguem no Evolution (inbox 3), desligadas.
- Avaliar desativar/cancelar assinatura do Crisp (export completo já salvo em /opt/data/crisp-export e entregue ao Lucas).
- Evolution (551123671467) segue ativo como canal secundário/backup.

## Atualização 11/jun (tarde) — Elle pausada a pedido do Lucas
- Lucas pediu remoção de TODAS as notas de triagem "Elle MVP 1C" (~5.5k deletadas, geradas em massa pelos imports).
- Webhook da conta Chatwoot -> elle.lkskrs.online REMOVIDO (URL preservada nos backups de webhook_subscriptions) e container `elle-chatwoot` PARADO (a fila persistente dela continuava repostando notas usando o access token do Lucas).
- Para religar a Elle: reconfigurar para NAO criar notas de triagem (ou ignora-las por inbox), recriar o webhook na conta 1 e dar docker start no elle-chatwoot.
