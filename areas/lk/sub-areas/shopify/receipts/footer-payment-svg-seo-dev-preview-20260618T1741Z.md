# Receipt — Footer/payment SVG SEO técnico — DEV preview — 20260618T1741Z

- values_printed: false
- escopo aprovado por Lucas: DEV preview da correção mínima do footer
- tema DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- tema Production: `155065417950` / `lk-new-theme/production` / role `main`
- Shopify write executado: somente `sections/lk-footer.liquid` no DEV theme
- Production write: não executado

## Problema revalidado

Páginas públicas validadas antes do DEV write:

- Home: `https://lksneakers.com.br/`
- Collection: `https://lksneakers.com.br/collections/sneakers`
- Cart: `https://lksneakers.com.br/cart`

Artefatos:

- Summary: `/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/summary-20260618T173020Z.json`
- Approval packet: `areas/lk/sub-areas/shopify/approval-packets/footer-payment-svg-seo-technical-dev-preview-20260618.md`

Achados:

- `.ft__payments` presente nas 3 páginas;
- `pi-discover` presente antes;
- W3C/Nu apontou erros relevantes globais no footer:
  - `aria-label` em `div` sem role semântico;
  - `Element “stop” is missing required attribute “offset”` nos gradientes do SVG Discover.

## Fonte no Production antes do DEV write

Readback Admin Production:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/production-footer-source-readback-20260618T173110Z.json`

Hash Production antes:

`03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`

Trecho original:

```liquid
<div class="ft__payments" aria-label="Formas de pagamento aceitas">
  {%- for type in shop.enabled_payment_types limit: 6 -%}
    {{ type | payment_type_svg_tag: class: 'ft__payment' }}
  {%- endfor -%}
</div>
```

## Mudança aplicada no DEV

Arquivo:

`sections/lk-footer.liquid`

Mudança:

- `.ft__payments` agora usa `role="group"` com `aria-label`;
- loop passa a pular apenas `type == 'discover'`;
- mantém até 6 payment icons quando disponíveis.

Diff local:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/proposed-lk-footer-skip-discover-role-group.diff`

## Readback pós-upload DEV

Arquivo:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/dev_apply/dev-footer-apply-20260618T173954Z.json`

Resultado:

- ok: true
- dev_before_hash: `03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`
- dev_after_hash: `fe23e63953adc836de601c74e3af2a7b2ade6eb3d0e846717d09857b5a66ac3c`
- prod_before_hash: `03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`
- prod_after_hash: `03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`
- production_unchanged: true
- dev_has_role_group: true
- dev_has_discover_skip: true
- dev_old_loop_count: 0
- dev_payment_svg_tag_count: 1

Rollback DEV:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/dev_apply/rollback-before-footer-svg-dev-20260618T173954Z.json`

## Browser QA DEV preview

Arquivo:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/dev_apply/dev-footer-preview-qa-20260618T174106Z.json`

Screenshot:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/dev_apply/dev-footer-preview-20260618T174106Z.png`

Resultado:

- ok: true
- footerFound: true
- role: `group`
- ariaLabel: `Formas de pagamento aceitas`
- svgCount: 6
- hasDiscover: false
- ids renderizados:
  - `pi-american_express`
  - `pi-diners_club`
  - `pi-elo`
  - `pi-jcb`
  - `pi-master`
  - `pi-visa`
- errors: []

## Interpretação

A correção mínima funcionou em DEV:

- remove o SVG Discover problemático do footer;
- corrige o `aria-label` sem role;
- preserva 6 ícones de pagamento no preview;
- não gerou erro JS;
- Production ficou intacto.

## Risco para Production

Baixo, mas existe mudança visual discreta:

- Discover deixa de aparecer no footer;
- Visa aparece como sexto ícone no lugar do Discover no preview;
- pagamento real/checkout não é alterado, apenas badge visual do footer.

## Próxima decisão

Se Lucas aprovar Production, promover o mesmo diff DEV→Production com:

1. snapshot Production;
2. PR/merge ou patch escopado conforme fluxo do tema;
3. upload/merge Production somente deste asset;
4. readback hash;
5. QA público Home/Collection/Cart;
6. validação pública do footer e receipt.
