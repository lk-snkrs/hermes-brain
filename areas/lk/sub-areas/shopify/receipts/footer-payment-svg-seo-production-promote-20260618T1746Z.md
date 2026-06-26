# Receipt — Footer/payment SVG SEO técnico — Production promote — 20260618T1746Z

- values_printed: false
- escopo aprovado por Lucas: promover para Production o ajuste do footer validado em DEV
- Shopify write executado: `sections/lk-footer.liquid` no tema Production
- tema DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- tema Production: `155065417950` / `lk-new-theme/production` / role `main`

## Origem

DEV preview aprovado e validado no receipt:

`areas/lk/sub-areas/shopify/receipts/footer-payment-svg-seo-dev-preview-20260618T1741Z.md`

## Production promote/readback

Arquivo:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/prod_apply/production-footer-promote-20260618T174456Z.json`

Resultado:

- ok: true
- mode: `production_promoted_from_dev`
- dev_source_hash: `fe23e63953adc836de601c74e3af2a7b2ade6eb3d0e846717d09857b5a66ac3c`
- dev_after_hash: `fe23e63953adc836de601c74e3af2a7b2ade6eb3d0e846717d09857b5a66ac3c`
- prod_before_hash: `03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`
- prod_after_hash: `fe23e63953adc836de601c74e3af2a7b2ade6eb3d0e846717d09857b5a66ac3c`
- dev_prod_aligned: true
- prod_has_role_group: true
- prod_has_discover_skip: true
- prod_old_loop_count: 0
- prod_payment_svg_tag_count: 1

Rollback Production:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/prod_apply/rollback-before-footer-svg-production-20260618T174456Z.json`

## Mudança promovida

- `.ft__payments` agora usa `role="group"` junto com `aria-label`.
- O loop de payment icons pula apenas `type == 'discover'`.
- O footer mantém até 6 ícones quando disponíveis.
- No DEV preview, os 6 ícones renderizados foram:
  - American Express
  - Diners Club
  - Elo
  - JCB
  - Mastercard
  - Visa

## QA público imediato

Arquivos:

- `/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/prod_apply/production-footer-live-qa-20260618T174536Z.json`
- `/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/prod_apply/production-footer-live-qa-20260618T174651Z.json`

Resultado público imediato:

- Home: ainda servindo HTML antigo nas amostras.
- Collection `/collections/sneakers`: ainda servindo HTML antigo nas amostras.
- Cart: alternando entre novo e antigo.
- Validator externo ainda vê erros relevantes quando recebe HTML antigo.

Interpretação:

- Admin/readback Production está correto.
- O storefront público está em cache/page_cache misto, semelhante ao que aconteceu com a Home após a Opção C SWYM.
- Não há indicação de quebra funcional; é mudança de footer visual/HTML.
- Não foi feito rollback porque o asset Production está correto e o cache antigo ainda exibe o footer anterior funcional.

## Monitor em andamento

Monitor iniciado sem novos writes:

- processo: `proc_e4ba2f406475`
- script: `/opt/data/profiles/lk-shopify/runtime/monitor_footer_production_convergence.py`
- critério: 3 rodadas consecutivas com Home, Collection e Cart servindo `.ft__payments role="group"` e sem `pi-discover`.

## Próximo passo

Aguardar o monitor terminar. Se convergir, registrar fechamento final. Se não convergir, classificar como page_cache pendente e revalidar depois, sem rollback automático.
