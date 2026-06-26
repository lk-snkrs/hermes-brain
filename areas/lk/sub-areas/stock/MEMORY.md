# MEMORY — [LK] Estoque Loja Física

## Fatos operacionais estáveis

- Tiny / `LK | CONTROLE ESTOQUE` é a verdade de estoque.
- Shopify é contexto/event trigger, não verdade final de estoque.
- Disponibilidade deve ser por SKU/variante/tamanho.
- Best seller deve ser derivado de vendas/demanda reais.
- Fixtures, probes e testes nunca contam como demanda/estoque operacional nem podem gerar P0/P1 ou recomendação.
- O agente v0.1 está preparado; gateway/bot/cron pendentes de aprovação.

## Decisões pendentes

- Quais depósitos/locais Tiny representam “loja física/pronta entrega”.
- Se haverá Telegram próprio ou uso via LK Ops/Main.
- Cadência de rotina e destino dos relatórios.
- Quem aprova compra/transferência: Lucas, Júlio, operação ou fluxo misto.
