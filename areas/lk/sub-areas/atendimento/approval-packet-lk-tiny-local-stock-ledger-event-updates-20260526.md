# Approval Packet — LK Tiny local stock DB + event-driven refresh

## Destino
LK Ops / Atendimento / Shopify-Tiny inventory, com Hermes Geral como orquestrador.

## Pedido limpo
Evoluir o cache curto atual para uma base local de estoque por SKU/tamanho derivada do Tiny, atualizada por eventos de movimentação relevantes, para responder Telegram/WhatsApp em segundos sem abandonar o Tiny como fonte de verdade.

## Evidências
- Lucas reportou latência de ~180s em consulta ampla (`New Balance 9060 tamanho 38`).
- Patch atual reduziu consulta repetida para ~0.2s usando cache local Tiny de TTL curto.
- O TTL curto sozinho não garante atualização após movimentação; é aceleração, não sincronização.
- PRD existente já define o padrão correto: Shopify é evento/gatilho; Tiny é estoque oficial; nunca calcular saldo por delta local.
- Já existe processor dry-run `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py` para eventos `orders/paid` e `orders/cancelled`, sem write externo.

## Preview
Arquitetura recomendada em 3 camadas:

1. Base local `lk_tiny_stock_local.sqlite`
   - tabela `stock_by_sku`: sku, produto, tamanho, tiny_id, saldo `LK | CONTROLE ESTOQUE`, saldo total, fonte, confiança, last_tiny_read_at, stale_reason.
   - tabela `stock_events`: evento, delivery_id, order_id, line_item_id, sku, status, timestamps.
   - tabela `refresh_queue`: SKUs que precisam nova leitura Tiny.

2. Atualização event-driven
   - Shopify `orders/paid` / `orders/cancelled` enfileira SKUs afetados.
   - Worker lê Tiny por SKU exato e atualiza base local com saldo absoluto vindo do Tiny.
   - Não usa `- quantidade` nem `+ quantidade`; evento só dispara reconsulta.

3. Resposta Telegram/WhatsApp
   - consulta base local primeiro para resposta em segundos.
   - se SKU/tamanho está fresco: responde com fonte `Tiny local snapshot` + timestamp.
   - se está stale/ausente: faz consulta Tiny por SKU exato com timeout curto e atualiza a base.
   - se ainda incerto: responde como validação pendente, sem promessa.

## Risco
- Tiny pode rate-limitar se tentarmos snapshot de catálogo inteiro; usar somente refresh por SKU/evento e micro-batches.
- Tiny pode não oferecer webhook direto de movimentação; se não houver webhook Tiny confiável, usar eventos Shopify + refresh por SKU e, opcionalmente, reconciliação micro-batch controlada.
- Se SKU/Tiny estiver ambíguo, não atualizar cache como verdade.
- Base local desatualizada pode induzir promessa errada; resposta deve carregar timestamp/stale guardrail.

## Bloqueios
Sem aprovação explícita, não executar:
- criação/alteração de webhook Shopify/Tiny;
- worker/serviço de produção;
- cron recorrente;
- Shopify inventory write;
- Tiny write;
- mensagem externa a cliente/fornecedor;
- promessa de disponibilidade/reserva/preço.

## Rollback
- Desativar rota/worker/event handler.
- Responder volta ao modo live Tiny/TTL curto atual.
- Remover/ignorar base local `lk_tiny_stock_local.sqlite`.
- Tiny permanece intocado.
- Se houver webhook Shopify criado em fase futura, remover assinatura e manter ledger para auditoria.

## Decisão / próximo passo
Aprovar Fase A local sem writes externos:
- criar schema local `lk_tiny_stock_local.sqlite`;
- adaptar o responder para ler essa base antes do cache TTL atual;
- adaptar o processor dry-run de eventos Shopify para atualizar essa base local quando consultar Tiny;
- rodar testes e amostras locais;
- não criar webhooks, não cronar, não escrever Shopify/Tiny ainda.

Frase de aprovação sugerida:
"Aprovo Fase A local: criar base local Tiny stock por SKU/tamanho e ligar ao responder + processor dry-run, sem webhooks novos, sem cron, sem Shopify/Tiny writes e sem mensagens externas." 
