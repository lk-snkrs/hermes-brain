# Receipt — LK CRM T3 coupon test sends

Data: 2026-05-21
Área: LK CRM / WhatsApp / Crisp / n8n / Shopify / Supabase

## Pedido

Lucas aprovou disparar o teste 3 para contatos anteriores com carrinho/checkout abandonado para validar envio e visibilidade.

## Escopo executado

Ação customer-facing aprovada no turno atual:

- Template: `lk_checkout_abandonado_72h_cupom10_v1`
- Canal: Crisp WhatsApp Plugin via n8n credential existente
- Header: imagem do produto incluída
- Corpo: T3 aprovado com cupom de 10%
- CTA: checkout abandonado
- `crisp_options`: `{ as: "text", type: "text", new_session: false }`
- `BODY.text`: fallback renderizado incluído
- Workflow temporário usado para credencial Crisp: `JZch7XhmOATtw5XB`
- Workflow temporário foi ativado apenas para envio e desativado ao final

## Seleção

Selecionados contatos únicos a partir da tabela Supabase `lk_crm_checkout_sequences` com T1/30min anterior, checkout ainda não concluído na Shopify e telefone válido. Duplicidade por telefone foi evitada.

## Envios executados

Foram disparados 4 testes T3:

1. Checkout `39388469035230`, telefone final `7793`, produto `Shorts Saint Studio Everywear Preto`, cupom `LK10T3-69035230-7793`, request_id `a62162a6-ccfe-49d6-94f3-3d199e4faa58`
2. Checkout `39501064339678`, telefone final `9623`, produto `Tênis On Running Cloudsolo Loewe Sand Burgundy Bege`, cupom `LK10T3-64339678-9623`, request_id `2929a66a-f842-4381-94a3-777bf961ba8e`
3. Checkout `39499747229918`, telefone final `3361`, produto `sua seleção`, cupom `LK10T3-47229918-3361`, request_id `77bad476-c0fa-41e3-acd9-a8fd1492744b`
4. Checkout `39499768103134`, telefone final `9631`, produto `sua seleção`, cupom `LK10T3-68103134-9631`, request_id `576a4024-40c8-4482-978d-3afe718b5b5f`

Todos os cupons foram criados com:

- desconto: 10%
- validade: 24h
- limite de uso: 1
- expiração: `2026-05-22T11:34:57Z`

## Evidência n8n/Crisp

Execuções n8n do workflow temporário:

- `14234`: success, Crisp `request_accepted`
- `14235`: success, Crisp `request_accepted`
- `14236`: success, Crisp `request_accepted`
- `14238`: success, Crisp `request_accepted`

Os request IDs foram persistidos no Supabase nas linhas T3 correspondentes.

## Rechecagem Inbox/callback

Rechecagem read-only feita após o disparo:

- Callback workflows recentes auditados: não houve callback encontrado para os 4 request IDs.
- Crisp REST Inbox/conversations: 100 conversas recentes escaneadas; nenhum dos 4 códigos apareceu nas mensagens visíveis da Inbox até o momento da auditoria.

## Diagnóstico

O provedor/Crisp aceitou os 4 disparos (`request_accepted`), mas ainda não há prova de:

- entrega no aparelho;
- callback assíncrono;
- visibilidade na Crisp Inbox.

Portanto, estes envios estão em estado **aceito/enfileirado**, não **confirmado entregue/visível**.

## Observação operacional

Não reenviar estes mesmos T3 sem nova aprovação explícita, para evitar duplicidade customer-facing. Próxima ação recomendada é investigar por request_id no callback/Crisp e/ou testar uma única variação controlada de session anchoring em número interno, não em cliente.
