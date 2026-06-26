# Receipt — Production merge PDP FAQ stock-copy

- Timestamp UTC: 20260605T155356Z
- Approval: Lucas Cimino via Telegram: "Aprovo merge PDP FAQ para produção"
- Production theme: `155065417950` (`lk-new-theme/production`)
- DEV reference theme: `155065450718` (`lk-new-theme/dev`)
- Asset: `sections/lk-pdp.liquid`
- Scope: production merge of approved DEV change only.
- Change: replaced fixed PDP FAQ/JSON-LD sentence `Produtos em estoque...` with neutral premium copy.
- Guardrail encomenda: operational badge/message `Sujeito a encomenda · 4-6 semanas ·` unchanged; count before/after 1/1.
- No product, variant, price, stock, tag, metafield operational, checkout, campaign, GMC or Klaviyo changes.
- Rollback: PUT `rollback.liquid` back to `sections/lk-pdp.liquid` on production theme.

## QA

- Old exact text after: 2
- New exact text after: 0
- `produtos em estoque` in asset after: 2
- Public URL tested: https://lksneakers.com.br/products/accolade-straight-leg-sweatpant-charcoal-green?_qa=1780674838
- Public old exact in fixed FAQ: True
- Public new exact in fixed FAQ: False
- Note: if `Produtos em estoque` still appears publicly, it can come from individual product description data, not this fixed theme FAQ.


## QA público pós-propagação

- Public old exact fixed FAQ: True
- Public new exact fixed FAQ: False
- Public `produtos em estoque` total count: 4 — pode vir de descrição de produto, fora deste asset.
- Public `Sujeito a encomenda` count: 1 — guardrail preservado.


## Admin asset QA corrigido

- Admin asset old exact count after: 0
- Admin asset new exact count after: 2
- Admin asset `produtos em estoque` count after: 0
- Admin asset `Sujeito a encomenda` badge count after: 1
