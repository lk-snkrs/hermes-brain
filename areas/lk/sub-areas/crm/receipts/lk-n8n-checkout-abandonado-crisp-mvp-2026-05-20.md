# Receipt — n8n LK Checkout Abandonado 30min MVP via Crisp

Data: 2026-05-20
Área: LK CRM / WhatsApp / n8n / Crisp
Aprovação: Lucas aprovou no Telegram com “Aprovado” após pacote de decisão para opção 2: Crisp/n8n como arquitetura canônica, sem envio e sem ativar produção.

## Escopo aprovado

- Atualizar/criar workflow n8n MVP 30min usando Crisp + template aprovado.
- Manter workflow inativo.
- Não disparar mensagem.
- Não ativar produção.

## Ação executada

Workflow n8n atualizado:

- ID: `kWQbmEMuvdipcGjd`
- Nome final: `LK - Checkout Abandonado 30min MVP - Crisp (INATIVO)`
- Status verificado: `active=false`
- Canal de envio no workflow: Crisp Template API
- Endpoint shape: `plugins.crisp.chat/.../template/send`
- Template configurado: `lk_checkout_abandonado_30min_v3`
- Template Meta/Crisp: `APPROVED`, `MARKETING`, `pt_BR`, com `HEADER IMAGE`, `BODY`, `BUTTON`

## Verificações pós-write

- Workflow permaneceu inativo: sim.
- Rota Meta direta removida deste MVP: sim (`graph.facebook.com` ausente no workflow final).
- Template antigo `carrinho_abandonado_30min` ausente: sim.
- Template novo `lk_checkout_abandonado_30min_v3` presente: sim.
- Payload Crisp tem `HEADER IMAGE`: sim.
- BODY usa 2 parâmetros, conforme template aprovado: sim.
- BUTTON URL usa 1 parâmetro de checkout token/path: sim.
- `crisp_options` normalizado para `{ type: "text", new_session: false }`: sim.
- Nó `Preparar dados` gera campos usados no payload: `firstName`, `productName`, `productImage`, `checkoutToken`, `phone`.
- Referência interna corrigida para o novo nome do trigger: `Shopify Checkout Webhook`.

## Backups / rollback

Backups n8n brutos foram salvos localmente em diretório restrito porque podem conter headers de autenticação:

- Diretório: `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/`
- Permissões: diretório `700`, arquivos `600`

Rollback operacional:

1. Reimportar/restaurar o JSON de backup do workflow `kWQbmEMuvdipcGjd` via n8n API/UI.
2. Confirmar `active=false` após restauração.
3. Validar ausência de disparos recentes.

## Não executado

- Nenhuma mensagem WhatsApp enviada.
- Nenhum workflow ativado.
- Nenhum cliente impactado.
- Nenhum cupom/desconto criado.
- Nenhuma alteração Shopify/Meta/Crisp de produção fora do workflow n8n inativo.

## Próxima aprovação necessária

Para enviar teste real ao número interno de Lucas, é necessária nova aprovação explícita no turno atual, incluindo o destinatário.
Para ativar produção, é necessária aprovação explícita separada após teste e revisão de receipts.
