# LK OS — Next Decision Queue, 2026-05-13

Generated at: `2026-05-13T21:02:19.320394+00:00`

## Veredito

Status: `continue_readonly_while_gmc_p2a_runs`

Continuar LK OS agora é seguro em modo **read-only/local**: acompanhar GMC P2A em andamento e preparar a próxima fila executiva, sem tocar WhatsApp/fornecedores/clientes/campanhas.

## Estado atual
- GMC P2A finalize: rodando
- WhatsApp `hermes`: authenticated=True, final=5245
- WhatsApp `lk-compras`: authenticated=True, final=9821
- WhatsApp `spiti`: authenticated=True, final=0369
- WhatsApp `zipper`: authenticated=True, final=4306
- Crons LK obrigatórios: Daily Sales Brief, Weekly CEO Review, SEO/CRO Weekly, GMC Review — ativos no scheduler observado
- Loyalty/Rivo/Judge.me: pending_future; não retomar sem Lucas reabrir essa frente

## Próximo bloco recomendado

- Monitorar processo GMC P2A até relatório final; não reexecutar patches em paralelo.
- Atualizar fila de decisões de sourcing a partir de artifacts existentes, sem consultar marketplace/fornecedor.
- Manter Klaviyo P1 em draft/no-send; se Lucas quiser, preparar pacote de revisão inline antes de qualquer envio.
- Usar WhatsApp Hermes/lk-compras apenas como canal preparado; não ler conversas nem enviar mensagens sem novo escopo explícito.

## Decisões abertas de sourcing — legado, não executar sem revalidação

Estas 5 decisões vêm do router antigo de cotação. Pela correção posterior do Lucas, **não devem virar contato com fornecedor automaticamente**. Antes de qualquer contato/compra, o fluxo correto é revalidar: produto vendido/solicitado → stockout real por SKU/tamanho → Droper primeiro → se não tiver, StockX vs GOAT → preview Notion/Júlio.

- Nike Moon Shoe SP Jacquemus: legado approval_needed; qty_ref=10; revenue_signal_fact_shopify=48999.92; próximo seguro agora=fresh stockout validation, sem contato
- New Balance 9060: legado approval_needed; qty_ref=8; revenue_signal_fact_shopify=18799.93; próximo seguro agora=fresh stockout validation, sem contato
- Nike Mind 002: legado approval_needed; qty_ref=3; revenue_signal_fact_shopify=6399.98; próximo seguro agora=fresh stockout validation, sem contato
- Comme des Garçons PLAY Polo: legado approval_needed; qty_ref=3; revenue_signal_fact_shopify=3599.98; próximo seguro agora=fresh stockout validation, sem contato
- New Balance 530: legado hold/bundle; qty_ref=2; revenue_signal_fact_shopify=5999.97; próximo seguro agora=fresh stockout validation, sem contato

## Não executado
- message_read
- whatsapp_send
- supplier_contact
- purchase
- notion_write
- shopify_write
- tiny_write
- klaviyo_send_or_schedule
- new_merchant_write
- database_write
