# Diagnóstico — Chatwoot não importa contatos Shopify automaticamente

Data: 2026-06-03
Perfil: lk-ops

## Pergunta
Lucas perguntou por que os contatos não estão sendo importados do Shopify para o Chatwoot.

## Evidência consultada
- Chatwoot API `GET /api/v1/accounts/1/integrations/apps`.
- Chatwoot API `GET /api/v1/accounts/1/contacts?page=1`.
- Chatwoot API `GET /api/v1/accounts/1/inboxes`.
- Shopify Admin REST read-only `GET /customers/count.json` e amostra de clientes.

## Achados
- Integração Shopify no Chatwoot está habilitada e possui hook `shopify` com `reference_id=lk-sneakerss.myshopify.com`.
- Chatwoot contatos: `meta.count=0`; página 1 sem contatos.
- Inbox existente no Chatwoot: `Shopify Carrinho Abandonado`, tipo `Channel::Api`; não há inbox WhatsApp Cloud conectado no readback consultado.
- Shopify possui clientes: count observado `29000`, com amostra contendo clientes com e-mail e/ou telefone.

## Interpretação
O problema não parece ser falta de clientes no Shopify nem ausência total da integração Shopify no Chatwoot. A integração nativa Shopify do Chatwoot serve para contexto de pedidos/clientes dentro de conversas, via OAuth/hook, mas não fez importação em massa/população automática da tabela de contatos. Para campanhas WhatsApp no Chatwoot, são necessários contatos dentro do Chatwoot com telefone/labels e um inbox real `Channel::Whatsapp`/`whatsapp_cloud`; a inbox atual é `Channel::Api`.

## Limites mantidos
- Nenhum write no Chatwoot.
- Nenhum write no Shopify.
- Nenhum envio externo/WhatsApp/campanha.
- Nenhum token registrado.

## Próximo passo recomendado
Preparar plano/preview de importação controlada Shopify → Chatwoot somente após aprovação explícita: filtro de clientes com telefone, normalização E.164/BR, labels (`shopify`, segmento), dedupe por telefone/e-mail, dry-run CSV/JSON, depois import via API se aprovado. Antes de campanha, conectar/verificar inbox WhatsApp Cloud real e template aprovado.
