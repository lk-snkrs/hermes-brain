# Tiny Stock Resolver v2 — LK

Data: 2026-05-26T14:07:14+00:00

## O que foi feito

- Criado `tiny_stock_resolver_v2()` em `/opt/data/scripts/lk_hermes_whatsapp_responder.py`.
- `answer_stock()` passou a usar o resolver como caminho único para respostas de estoque.
- `tiny_stock_for_exact_sku()` passou a delegar para o resolver, removendo a lógica separada de busca Tiny na primeira página.
- `tiny_search_instock_variants()` passou a reaproveitar o resolver para fallback de venda assistida.
- Atualizada a referência operacional `lk-whatsapp-stock-responder-sku-size-20260521.md` no skill `lk-shopify-readonly`.

## Contrato do resolver

- Usa Tiny como fonte read-only.
- Considera apenas `LK | CONTROLE ESTOQUE` como saldo oficial.
- Pagina busca Tiny de forma limitada e segura.
- Expande parent products para variações quando necessário.
- Deduplica/agrega por produto + SKU + tamanho.
- Retorna fonte, confiança, tamanho explícito, SKU e saldo.
- Mensagem final sempre informa que Hermes não reservou, não alterou estoque e não prometeu entrega/preço.

## Testes/verificação

- RED criado para paginação profunda + soma de duplicados.
- RED criado para resposta padronizada com fonte/confiança/sem promessa.
- `py_compile`: OK.
- `pytest /opt/data/tests/test_lk_whatsapp_assisted_sale.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py -q`: 5 passed.
- `--selftest`: OK; resposta de exemplo contém fonte e confiança.
- Responder WhatsApp ativo na porta 8787 após reinício/watchdog.

## Segurança

- Nenhum write em Tiny.
- Nenhum write em Shopify.
- Nenhuma reserva, compra, preço ou contato externo.
- Sem exposição de segredo.
