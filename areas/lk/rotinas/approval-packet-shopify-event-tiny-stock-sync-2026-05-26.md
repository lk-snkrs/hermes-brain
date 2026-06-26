# Approval Packet — Shopify event → Tiny stock truth → Shopify inventory

Status: preparado; não executado.
Data: 2026-05-26.

## Destino

LK Operações / LK Shopify, com governança Hermes Geral.

## Pedido limpo

Quando um produto for vendido ou um pedido for cancelado no Shopify, usar o evento Shopify apenas como aviso. Para cada item afetado, buscar o estoque verdadeiro no Tiny, no depósito `LK | CONTROLE ESTOQUE`, e atualizar o estoque correspondente no Shopify para refletir o saldo oficial Tiny.

## Evidências / decisões já fixadas

- Shopify não é fonte de verdade de estoque.
- Tiny é fonte oficial de estoque.
- Shopify serve como evento de venda/cancelamento e como superfície a ser atualizada.
- Não se deve calcular estoque por subtração/soma com base no Shopify.
- Venda e cancelamento devem apenas disparar nova consulta ao Tiny.
- SKU/tamanho precisam ser resolvidos por variante exata antes de qualquer update.

## Preview técnico

Eventos:

- `orders/paid`
- `orders/cancelled`

Para cada line item:

1. Validar assinatura Shopify.
2. Deduplicar evento por idempotency key.
3. Resolver `variant_id`, SKU e tamanho.
4. Buscar Tiny por SKU/código canônico.
5. Validar match único no depósito `LK | CONTROLE ESTOQUE`.
6. Ler saldo Tiny.
7. Atualizar `InventoryLevel` Shopify da variante/location para o saldo Tiny.
8. Fazer readback Shopify.
9. Gravar receipt/ledger.

## Risco

- Duplicidade de webhook pode repetir evento se idempotência falhar.
- SKU mal mapeado pode atualizar variante errada.
- Tiny rate-limit pode bloquear leitura; nesse caso o sistema deve não escrever.
- Cancelamento/refund parcial não deve ser interpretado como estoque a devolver; só deve disparar consulta Tiny.
- Location Shopify incorreta pode atualizar o estoque no local errado.

## Bloqueios atuais

Ainda não executar sem aprovação explícita:

- criação/alteração de webhook Shopify;
- write de estoque Shopify;
- mudança em gateway/webhook runtime;
- cron ou worker recorrente;
- qualquer alteração em Tiny;
- qualquer mensagem externa a cliente/fornecedor.

## Rollback

- Pausar/remover rota de webhook.
- Desabilitar write mode; manter dry-run.
- Usar ledger com `shopify_inventory_before` para reverter updates se necessário.
- Tiny permanece intocado.

## Decisão 1/1

Aprovar Fase A + B em modo seguro:

- implementar processor e testes;
- validar webhook HMAC;
- rodar com eventos reais em **dry-run**;
- consultar Tiny;
- gerar ledger e relatório;
- **sem write Shopify ainda**.

Aprovação sugerida:

> Aprovo Fase A+B: implementar e ativar o dry-run do sync Shopify evento → Tiny estoque, para `orders/paid` e `orders/cancelled`, sem write Shopify/Tiny e com ledger de bloqueios.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: aprovar ou bloquear a Fase A+B em modo dry-run para o fluxo Shopify event → Tiny stock truth → Shopify inventory.
- Ação proposta nesta fase: implementar/validar processor, HMAC, idempotência, consulta Tiny, ledger e relatório, sem write Shopify/Tiny.

### Target / owner
- Target: eventos Shopify `orders/paid` e `orders/cancelled` da LK Sneakers e consulta de estoque Tiny no depósito `LK | CONTROLE ESTOQUE`.
- Owner operacional: LK Operações / LK Shopify, com governança Hermes Geral e aprovação Lucas.

### Escopo permitido
- Escopo permitido para Fase A+B: dry-run, testes locais, validação HMAC, deduplicação, resolução de SKU/variante, consulta Tiny read-only, ledger e relatório de bloqueios.
- Pode fazer readback/validação local e registrar receipt; não pode efetuar write de estoque.

### Secret hygiene
- Usar Shopify/Tiny somente via Doppler/wrappers aprovados; não imprimir tokens, API keys, passwords, refresh tokens, service-account JSON ou connection strings.
- Logs, ledger e receipts devem declarar `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
