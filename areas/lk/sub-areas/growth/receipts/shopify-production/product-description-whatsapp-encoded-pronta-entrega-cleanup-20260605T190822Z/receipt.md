# Receipt — WhatsApp URL encoded pronta entrega cleanup

- Timestamp UTC: 20260605T190822Z
- Scope: product body_html only, WhatsApp `text=` URL parameter inside existing pre-order notice.
- Candidates: 3
- Applied: 3
- Errors: 0
- Change: `produto a pronta entrega` inside encoded WhatsApp message -> `disponibilidade do produto`.
- Preserved: visible `Produto sujeito a encomenda` notice, prazo 4 a 6 semanas, tags, variants, inventory, price, SEO, theme, checkout.
- Rollback: `rollback-payload-rest.json`.
- Post remaining pronta entrega encoded/plain in body_html: 0
