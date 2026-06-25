# Handoff superseded — Cart drawer is cross-sell X→Y, not Stock priority ranking

- **Data:** 2026-06-25
- **Origem:** lk-shopify
- **Destino/owner original:** lk-stock / [LK] Estoque Loja Física
- **Status:** **superseded / não acionar LK Stock para ranking principal**
- **Correção de Lucas:** “tudo errado... não é isso.. tem que ser possibilidade de CROSS SELL. por exemplo, cliente comprou X, tem % de chances de comprar os produtos Y.”

## Correção de rota

O pedido original para LK Stock definir prioridade dos 4 cards estava errado.

A lógica correta do `cart-drawer__upsell-inner` é:

```text
cliente colocou/comprou X
→ calcular/usar probabilidade histórica de comprar Y
→ ordenar Y por chance de cross-sell
→ renderizar até 4 produtos
```

## Novo dono do ranking

- **Dono do ranking X→Y:** `lk-shopify`, via análise read-only/agregada de pedidos/co-compra.
- **Papel eventual do LK Stock:** somente filtro final de elegibilidade/comprabilidade se necessário; por exemplo, bloquear item sem disponibilidade confiável. LK Stock não deve decidir o score principal.

## Fonte correta

Análise agregada de pedidos/co-compra, sem dados pessoais no output:

- pares no mesmo pedido: `X + Y`;
- possível compra sequencial por mesmo cliente em janela curta, se seguro e permitido;
- agregação por produto e por modelo/silhueta;
- métricas: `confidence(X→Y)`, `lift(X,Y)`, `support`, recência;
- filtros: excluir item atual do carrinho, itens já no carrinho, produto indisponível/não comprável.

## Critérios fora do ranking

Não usar como critério principal de ranking:

- margem/valor;
- prioridade operacional de estoque/giro;
- coleção `/all`;
- escolha manual fixa sem evidência;
- estoque como score.

## Próxima ação correta

LK Shopify deve preparar um packet de análise read-only:

1. período analisado;
2. método de co-compra;
3. top regras X→Y;
4. risco de amostra pequena;
5. formato de artefato agregado para o tema;
6. proposta DEV + QA + rollback.

## Reminder OS

- **Reminder OS loop needed:** yes
- **Reminder OS owner:** lk-shopify
- **Reminder OS next action:** gerar análise read-only de co-compra/cross-sell X→Y para cart drawer; não aguardar LK Stock como dono do ranking.
- **Reminder OS review trigger:** antes de qualquer nova mudança na lógica dos 4 produtos do cart drawer.
- **Reminder OS evidence:** correção de Lucas no Telegram em 2026-06-25 + spec `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-upsell-stock-priority-technical-spec.md` corrigida para cross-sell.

## Guardrails

- Sem Shopify write até approval packet/DEV approval.
- Sem expor dados pessoais de pedidos/clientes; output deve ser agregado.
- Sem prometer disponibilidade sem filtro/evidência.
- `values_printed=false`.
