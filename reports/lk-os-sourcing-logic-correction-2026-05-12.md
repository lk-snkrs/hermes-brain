# LK OS — Correção de lógica de sourcing/reposição, 2026-05-12

## Correção recebida de Lucas

O preview anterior de cotação P1 por família/fornecedor genérico está **invalidado**. A LK não deve acionar fornecedor/grupo de compras apenas porque há uma oportunidade P1 ou sinal de receita.

## Lógica correta

1. O gatilho é uma venda/pedido/necessidade concreta de produto com estoque zerado/stockout confirmado.
2. Confirmar produto exato, SKU e tamanho.
3. Confirmar estoque zero na fonte correta antes de sourcing.
4. Consultar Droper primeiro para saber se o produto existe e quanto custa.
5. Se não houver na Droper, comparar StockX vs GOAT e escolher o menor custo viável, com normalização de tamanho.
6. Criar tarefa/automação Notion para Júlio comprar, contendo:
   - pedido/produto/SKU/tamanho;
   - fonte mais barata;
   - link;
   - custo;
   - ressalvas de tamanho/lead time.
7. Hermes nunca compra, reserva, cria PO, decide endereço, escolhe fornecedor/importador que traz ao Brasil, nem aciona grupo de compras autonomamente.

## Artefato invalidado

- `reports/lk-os-supplier-quote-send-preview-2026-05-12.md`
- `reports/lk-os-supplier-quote-send-preview-2026-05-12.json`
- `reports/lk-os-supplier-quote-send-preview-2026-05-12.csv`
- `areas/lk/rotinas/lk-os-supplier-quote-send-preview-2026-05-12.md`

Status: `superseded_do_not_send_lucas_sourcing_correction_2026_05_12`

## Não executado

- Nenhum fornecedor contatado.
- Nenhuma mensagem enviada.
- Nenhuma compra/reserva/PO.
- Nenhum Shopify/Tiny/banco/campanha alterado.
- Nenhum marketplace consultado neste ajuste.
- Nenhuma automação Notion criada ainda.
