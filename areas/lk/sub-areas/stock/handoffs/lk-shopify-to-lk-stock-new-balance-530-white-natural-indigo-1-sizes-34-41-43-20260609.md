---
title: Handoff LK Shopify → LK Stock — New Balance 530 White Natural Indigo tamanhos 34/41/43
created_at: 2026-06-09T14:03:12+00:00
source_agent: lk-shopify
target_owner: "[LK] Estoque Loja Física / lk-stock"
status: pending_stock_owner_validation
---

# Pedido recebido

Lucas pediu: "adicionar estoque disponivel para venda sem estoque, no 34, 41 e 43 por favor..."

URL enviada:
https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?_qa=main_preview_check

# Interpretação operacional

Pedido envolve estoque/disponibilidade/pronta entrega/grade por tamanho e possivelmente alteração de venda sem estoque/continue selling em variantes Shopify.

Pela regra canônica de LK, o dono obrigatório é `[LK] Estoque Loja Física` / `lk-stock` e Tiny / `LK | CONTROLE ESTOQUE` é a fonte de verdade.

# Escopo solicitado para validação do lk-stock

Produto/handle: `new-balance-530-white-natural-indigo-1`
Tamanhos: `34`, `41`, `43`
Ação desejada pelo Lucas: permitir venda/estoque disponível apesar de aparecer sem estoque.

# Bloqueio LK Shopify

LK Shopify não executou write em Shopify, Tiny, estoque, preço, disponibilidade ou checkout.

Antes de qualquer alteração, lk-stock deve confirmar a verdade de estoque/operacional no Tiny/controle interno e devolver um pacote claro:

- variantes/tamanhos exatos;
- evidência da fonte de estoque;
- ação permitida: ajuste de estoque real, ajuste de política de venda sem estoque, ou não alterar;
- riscos/observações de fulfillment;
- escopo autorizado para execução Shopify, se aplicável.

# Próxima decisão

Aguardar retorno do `lk-stock` com validação e, se houver Shopify write necessário, executar somente com aprovação explícita atual e readback/rollback.
