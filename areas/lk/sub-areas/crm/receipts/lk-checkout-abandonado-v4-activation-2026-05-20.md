# Receipt — ativação checkout abandonado LK v4 via n8n/Crisp

Data UTC: 2026-05-20T13:35Z
Área: LK CRM / WhatsApp / n8n / Crisp / Meta Templates

## Aprovação

Lucas aprovou no Telegram com: “Seguir”.

## Ações executadas

1. Criado/submetido template Meta WhatsApp:
   - Nome: `lk_checkout_abandonado_30min_v4`
   - WABA: `1478026007140488` (`LK Sneakers & Apparels`)
   - Categoria: `MARKETING`
   - Idioma: `pt_BR`
   - Header: `IMAGE`
   - CTA: `Finalizar compra`
   - Status final verificado: `APPROVED`

2. Copy aprovada no template:

> Oi {{1}}, aqui é da LK. Vi que você estava olhando {{2}} e seu checkout ficou salvo por aqui.
>
> Na LK, todos os produtos têm garantia de originalidade. Se quiser, nosso atendimento está à disposição para te ajudar e finalizar sua compra com segurança.

3. Workflow n8n atualizado:
   - ID: `kWQbmEMuvdipcGjd`
   - Nome após ativação: `LK - Checkout Abandonado 30min MVP - Crisp (ATIVO)`
   - Node de envio: `Crisp Send lk_checkout_abandonado_30min_v4`
   - Template no payload: `lk_checkout_abandonado_30min_v4`
   - `HEADER IMAGE`: usa `{{$json.productImage}}`
   - `crisp_options`: `{ "type": "note" }`
   - Workflow ativo: `true`

4. Gates de dados adicionados no node `Preparar dados`:
   - normalização de telefone BR/WhatsApp;
   - bloqueio de envio se telefone inválido/vazio;
   - bloqueio se checkout já vier com `completed_at`, `order_id` ou `order`;
   - fallback de produto para `sua seleção` quando houver múltiplos itens;
   - extração de imagem por múltiplos campos de `line_items`;
   - extração de token/path por `abandoned_checkout_url`, `recovery_url`, `web_url`, `checkout_url`, `token` ou `cart_token`;
   - se faltarem telefone, link/token ou produto mínimo, retorna `[]` e não chama a Crisp.

## Verificações

- Template v4 lido na Meta: `APPROVED`.
- Workflow n8n readback: `active=true`.
- Nodes readback:
  - `Shopify Checkout Webhook`
  - `Wait 30min`
  - `Preparar dados`
  - `Crisp Send lk_checkout_abandonado_30min_v4`
- Execuções recentes no workflow imediatamente após ativação: `[]` (nenhum disparo retroativo observado no readback).

## Backups / rollback

Backups brutos pré-patch salvos em área restrita porque podem conter headers de integração:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-v4-copy-data-gates-retry-20260520T133113Z.json`
- Backup anterior também existente: `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-v4-copy-data-gates-20260520T132937Z.json`

Rollback operacional:

1. Desativar workflow `kWQbmEMuvdipcGjd` no n8n.
2. Restaurar o backup pré-v4 via n8n API/UI.
3. Confirmar `active=false` ou reativar versão anterior apenas se aprovado.
4. Conferir ausência de novas execuções/erros no n8n e callbacks Crisp.

## Observações / risco residual

- O MVP agora está ativo, mas ainda é um fluxo 30min simples.
- Há gate contra payload já concluído, mas o recheck ativo contra Shopify Admin imediatamente antes do envio deve ser a próxima melhoria para ficar mais robusto contra compras concluídas dentro da janela de 30min.
- Monitorar callbacks Crisp/WhatsApp nas próximas primeiras execuções; sucesso real é `message_status_sent`, não apenas aceite HTTP.
