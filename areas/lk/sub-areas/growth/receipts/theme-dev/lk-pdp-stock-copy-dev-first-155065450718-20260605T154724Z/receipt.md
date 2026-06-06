# Receipt — DEV-first PDP stock-copy guardrail

- Timestamp UTC: 20260605T154724Z
- Approval: Lucas via Telegram: "aprovo seguir"
- Theme DEV: `155065450718` (`lk-new-theme/dev`)
- Asset: `sections/lk-pdp.liquid`
- Scope: DEV theme only. No production merge/publish.
- Change: replaced FAQ/JSON-LD stock shipping sentence from operational `Produtos em estoque...` to premium neutral copy.
- Guardrail encomenda: operational badge/message `Sujeito a encomenda · 4-6 semanas ·` unchanged; counts before/after equal.
- Rollback: PUT `rollback.liquid` back to `sections/lk-pdp.liquid` on DEV theme.
- Preview: https://lksneakers.com.br/?preview_theme_id=155065450718

## QA

- Old exact text remaining: True
- New text count: 0
- `Sujeito a encomenda` badge count before/after: 1/1
- Production untouched: yes


## QA corrigido pós-readback

- DEV old exact count: 0
- DEV new exact count: 2
- Production old exact count: 2
- Production new exact count: 0
- DEV `Sujeito a encomenda` badge count: 1
- Production `Sujeito a encomenda` badge count: 1
- Preview URL testada: https://lksneakers.com.br/products/accolade-straight-leg-sweatpant-charcoal-green?preview_theme_id=155065450718&_qa=1780674492
