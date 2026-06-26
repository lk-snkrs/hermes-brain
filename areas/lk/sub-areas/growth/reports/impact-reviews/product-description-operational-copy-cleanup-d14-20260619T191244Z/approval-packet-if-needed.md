# Approval packet — D+14 limpeza termos operacionais PDP/SEO

- Gerado: 2026-06-19T19:12:44.231977Z
- Status: read-only; nenhuma alteração executada.
- Aprovação necessária antes de qualquer write Shopify production/theme/GMC/CRM.
- values_printed=false.

## Regressão QA em Product SEO

- Produtos checados: 679/679; missing_nodes: 0.
- Hits: 172; por termo: {'envio_imediato': 172}; por superfície: {'seo_description': 172}.
- Padrão observado: `envio imediato` reapareceu em `product.seo.description` de 172 PDPs afetados.
- Ação proposta: preparar lote de substituição SEO description customer-safe (`atendimento humano`, `curadoria exclusiva`, autenticidade, confirmação via chat quando necessário), com backup field-level antes de qualquer write.
- Não corrigir sem aprovação explícita de Lucas no turno atual.

## Exemplos QA

- `adidas-japan-brain-dead-black-warm-vanilla-preto` — seo_description: envio imediato
- `camisa-check-zip-gray` — seo_description: envio imediato
- `kaws-holiday-singapore-vinyl-figure-brown-toy-art-marrom` — seo_description: envio imediato
- `kaws-holiday-taipei-vinyl-figure-black-brown-grey-set-toy-art` — seo_description: envio imediato
- `kaws-holiday-taipei-vinyl-figure-black-toy-art-preto` — seo_description: envio imediato
- `kaws-holiday-thailand-vinyl-figure-black-toy-art-preto` — seo_description: envio imediato
- `kaws-holiday-thailand-vinyl-figure-grey-toy-art-cinza` — seo_description: envio imediato
- `kaws-the-promise-vinyl-figure-brown-toy-art-marrom` — seo_description: envio imediato
- `kaws-the-promise-vinyl-figure-grey-toy-art-cinza` — seo_description: envio imediato
- `moletom-nude-project-beast-zip-up-ash-cinza` — seo_description: envio imediato
- `moletom-nude-project-beast-zip-up-grey-cinza` — seo_description: envio imediato
- `moletom-nude-project-brun-brown-marrom` — seo_description: envio imediato
- `moletom-nude-project-brun-marshmallow-off-white` — seo_description: envio imediato
- `moletom-nude-project-global-soon-ash-cinza` — seo_description: envio imediato
- `moletom-nude-project-global-soon-marshmallow-off-white` — seo_description: envio imediato
- `moletom-nude-project-kill-bill-zip-up-ash-cinza` — seo_description: envio imediato
- `moletom-nude-project-kill-bill-zip-up-marshmallow-off-white` — seo_description: envio imediato
- `moletom-nude-project-perfect-cropped-zip-up-grey-cinza` — seo_description: envio imediato
- `moletom-nude-project-poblenou-zipper-ash-cinza` — seo_description: envio imediato
- `moletom-nude-project-varsity-marshmallow-off-white` — seo_description: envio imediato

## PDPs priorizados por queda orgânica

### Short Alo Yoga Match Point (`short-alo-yoga-match-point`)
- GSC: 3 cliques pós; delta vs baseline 28d pró-rata: -9.54; CTR delta pp: -0.42.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Nike Travis Scott x Jordan Jumpman Jack TR 'University Red' (`tenis-nike-travis-scott-x-jordan-jumpman-jack-tr-university-red`)
- GSC: 1 cliques pós; delta vs baseline 28d pró-rata: -7.36; CTR delta pp: -1.86.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Adidas Samba Disney 101 Dalmatians Penny Branco (`tenis-adidas-samba-disney-101-dalmatians-penny-branco`)
- GSC: 11 cliques pós; delta vs baseline 28d pró-rata: -6.64; CTR delta pp: 0.56.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Nike Travis Scott x Nike Air Jordan 1 Retro Low OG SP Olive Branco (`tenis-travis-scott-x-nike-air-jordan-1-retro-low-og-sp-olive-suede`)
- GSC: 4 cliques pós; delta vs baseline 28d pró-rata: -5.29; CTR delta pp: -0.33.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Nike Vomero Premium White Bright Crimson Branco (`tenis-nike-vomero-premium-white-bright-crimson-branco`)
- GSC: 0 cliques pós; delta vs baseline 28d pró-rata: -5.11; CTR delta pp: -0.24.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Óculos Oakley Plantaris TI Raw Titanium Cinza (`oculos-oakley-plantaris-ti-raw-titanium-cinza`)
- GSC: 1 cliques pós; delta vs baseline 28d pró-rata: -5.04; CTR delta pp: -1.0.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Nike Air Force 1 Low x Nocta 'Certified Lover Boy' Branco (`tenis-nike-air-force-1-low-x-nocta-certified-lover-boy-branco`)
- GSC: 1 cliques pós; delta vs baseline 28d pró-rata: -4.57; CTR delta pp: -0.36.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Alo Yoga ALO Runner Branco (`tenis-alo-yoga-alo-runner-branco`)
- GSC: 7 cliques pós; delta vs baseline 28d pró-rata: -4.14; CTR delta pp: 0.18.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis Adidas Gazelle Indoor Maroon Almost Yellow Marrom (`tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom`)
- GSC: 1 cliques pós; delta vs baseline 28d pró-rata: -3.18; CTR delta pp: -0.54.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.

### Tênis New Balance 9060 Angora Sea Salt Bege (`tenis-new-balance-9060-angora-sea-salt-bege`)
- GSC: 2 cliques pós; delta vs baseline 28d pró-rata: -3.11; CTR delta pp: -1.32.
- Copy customer-safe: reforçar curadoria exclusiva, autenticidade e atendimento humano; evitar termos operacionais de estoque/prazo.
- CRO/PageSpeed: revisar acima da dobra mobile, mídia principal, CTA e trust blocks em preview.
- Rollback: snapshot body_html/seo antes do write e reversão campo a campo se D+7 não recuperar.
