# LK OS — Correção: sourcing é decisão econômica única, não Droper vs StockX/GOAT separado

Status: `corrected_by_lucas_no_external_writes`
Data: 2026-05-14

## Correção de Lucas

Lucas corrigiu que as opções “Droper/grupo de compras” e “trazer de fora” não são etapas separadas. Elas são alternativas dentro do mesmo processo de sourcing.

Exemplo de regra: se a LK vende um tênis por R$ 2.399, não faz sentido pagar R$ 2.200 na Droper. Se quiser lucro, precisa trazer de fora ou pular.

## Regra operacional corrigida

1. Sourcing nasce de venda/demanda + stockout.
2. Para cada produto/tamanho, criar um card único de decisão.
3. No mesmo card comparar:
   - preço de venda esperado/real da LK;
   - custo Droper/grupo nacional;
   - custo fora/importação/StockX/GOAT se necessário;
   - margem bruta antes de frete/taxas/impostos;
   - logística/prazo/risco.
4. Droper é sinal de disponibilidade/preço nacional, não recomendação automática de compra.
5. Se nacional não fecha margem, rota correta é fora/importação ou não comprar.
6. Júlio/Notion deve receber decisão comparativa, não cards separados por marketplace.

## Artefatos corrigidos

- `reports/lk-compras-sourcing-economic-correction-2026-05-14.md`
- `reports/lk-compras-sourcing-economic-correction-2026-05-14.json`

## Artefatos anteriores com caveat

Os payloads Droper/StockX gerados antes desta correção devem ser tratados como insumos de preço/disponibilidade, não como recomendação de compra ou fluxo operacional final.

## Não executado

- Notion write.
- Compra/reserva/pagamento.
- Contato fornecedor/vendedor.
- WhatsApp.
- StockX/GOAT lookup.
- Shopify/Tiny/Merchant write.
