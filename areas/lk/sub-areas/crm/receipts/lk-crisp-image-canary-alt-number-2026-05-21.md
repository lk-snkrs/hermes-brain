# LK Crisp image canary — alternate internal number — 2026-05-21

## Pedido
Lucas corrigiu o guardrail: WhatsApp CRM/testes nunca devem ser enviados sem imagem do produto. Pediu novo teste para `11974044616` para validar recebimento + Crisp Inbox.

## Guardrail registrado
- Memória de usuário atualizada: CRM/testes WhatsApp sempre com imagem produto/header.
- Skill `lk-whatsapp-crm-automation` atualizada com hard rule: não enviar variante sem imagem salvo override explícito no turno atual.

## Envio controlado
- Destino: final `4616`.
- Canal: Crisp WhatsApp Plugin Template API via n8n credential existente, sem expor secrets.
- Template: `lk_checkout_abandonado_30min_v4`.
- Imagem obrigatória: produto Shopify `adidas Taekwondo Mei Ballet Branco e Preto`.
- Image validation: HTTP 200, `image/jpeg`, content-length `69359`.
- Marker visível: `IMG9740065351`.
- n8n temp workflow: `JZch7XhmOATtw5XB`.
- Temp workflow status: ativado para execução única e desativado em seguida.
- n8n execution: `12251`, status `success`.
- Crisp response: `request_accepted`.
- Crisp request ID: `1ce5ddf6-e1e4-4af0-a446-5c3654976489`.

## Verificação inicial pós-envio
- n8n callback workflows recentes: nenhum hit para marker/request_id.
- Supabase `lk_crisp_whatsapp_receipts`: 0 linhas para request_id.
- Crisp REST últimas 80 conversas: nenhum marker/request_id encontrado.
- Falso positivo por final `4616` foi descartado; sessão encontrada era cliente não relacionada e não continha marker/request_id.

## Interpretação
`request_accepted` é aceite/enfileiramento, não confirmação de handset delivery nem Inbox. Até a primeira checagem, o teste ainda não tinha callback nem Inbox visível. Necessário aguardar confirmação humana do número final `4616` e/ou nova varredura posterior antes de classificar como entregue.
