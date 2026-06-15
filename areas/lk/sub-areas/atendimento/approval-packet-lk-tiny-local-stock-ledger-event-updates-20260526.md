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

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — LK Tiny local stock DB + event-driven refresh` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — LK Tiny local stock DB + event-driven refresh` no caminho `areas/lk/sub-areas/atendimento/approval-packet-lk-tiny-local-stock-ledger-event-updates-20260526.md`.
- Owner operacional: LK Atendimento / LK Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer mensagem a cliente, contato externo, WhatsApp/e-mail, mudança de atendimento humano, Chatwoot/webhook/runtime, preço, disponibilidade, reembolso, reserva, negociação ou logística sem approval packet específico.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Verificação / readback
- Verificação obrigatória: readback do sistema de atendimento/Chatwoot quando aplicável, ledger/receipt local, amostragem de conversas/contatos afetados e confirmação de zero envio externo não aprovado.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
