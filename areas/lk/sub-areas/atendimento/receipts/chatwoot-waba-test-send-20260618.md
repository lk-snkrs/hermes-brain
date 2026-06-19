# Receipt — Chatwoot/WABA test send

Data: 2026-06-18
Área: LK Atendimento / Chatwoot

## Escopo aprovado

Lucas solicitou envio de teste para número próprio informado no Telegram. Envio customer-visible real, escopado a um único destinatário e uma única mensagem.

## Ação executada

- Canal: Chatwoot `LK WhatsApp`
- Inbox ID: 2
- Channel type: `Channel::Whatsapp`
- Caminho: `Messages::MessageBuilder` → `SendReplyJob` → `Whatsapp::SendOnWhatsappService` → WABA
- Template usado: `lk_teste_chatwoot_builder_20260603`
- Categoria do template: `MARKETING`
- Idioma: `pt_BR`
- Mensagem pública: sim
- `template_params` preservado: sim
- Conteúdo público presente no Chatwoot: sim

## Evidência sanitizada

- Conversation ID: 1894
- Message ID: 46518
- Status no readback: `delivered`
- `source_id` presente: sim
- `source_id` prefix: `wamid`
- Erro externo presente: não
- `values_printed=false`

## O que não foi feito

- Nenhum envio em massa.
- Nenhum reenvio histórico.
- Nenhum backfill.
- Nenhuma alteração em Shopify, Tiny, Meta template ou configuração externa.
- Nenhum segredo registrado.

## Observação de segurança

Saídas brutas de Rails podem conter metadados operacionais/PII; recibo mantém somente IDs internos e status sanitizado.
