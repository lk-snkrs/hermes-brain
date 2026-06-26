# Receipt — product description fix

- Timestamp UTC: 20260605T155707Z
- Approval: Lucas via Telegram: corrigir produto informado e procurar outros errados.
- Product: `tenis-air-jordan-1-mid-glitter-swoosh-azul` — Tênis Nike Air Jordan 1 Mid Glitter Swoosh Azul
- Scope executed: only `product.descriptionHtml`.
- Guardrail encomenda: did not alter tag `encomenda`, variants, inventory, availability, operational badge/message, price, SEO, theme or checkout.
- Change: removed product-description FAQ wording `Produtos em estoque: envio em até 2 dias úteis...` and replaced with neutral availability/prazo wording.
- Rollback: reapply `rollback-payload.json` descriptionHtml.

## QA

- Admin description exact: True
- Admin term hits after: []
- Tags unchanged: True
- Public URL: https://lksneakers.com.br/products/tenis-air-jordan-1-mid-glitter-swoosh-azul?_qa=1780675028
- Public new sentence present now: False
- Public term hits after: ['Produtos em estoque', 'produtos em estoque', 'Sujeito a encomenda', 'envio em até 2 dias']
