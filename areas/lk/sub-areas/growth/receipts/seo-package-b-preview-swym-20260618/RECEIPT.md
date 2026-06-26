# Receipt — Pacote B B1 + preview B2 SWYM/Wishlist

Data: 2026-06-18

## Escopo aprovado

Lucas pediu: inventário profundo de tags/pixels e preparar um teste em tema dev/unpublished para reduzir SWYM/Wishlist, sem publicar nada em produção.

## Status

- Produção não publicada/alterada.
- Nenhum app/pixel foi desativado em produção.
- Nenhum secret foi impresso; execução Shopify via Doppler helper com `values_printed=false`.
- O tema `lk-new-theme/dev` já estava em condição ideal para teste A/B técnico: é idêntico ao `lk-new-theme/production` nos assets principais comparados, com diferença concentrada nos app embeds SWYM/Wishlist em `config/settings_data.json`.

## Temas relevantes

- Produção: `155065417950` — `lk-new-theme/production` — role `main`
- Preview/dev escolhido: `155065450718` — `lk-new-theme/dev` — role `unpublished`

## Evidência de paridade produção vs dev

Arquivos comparados:

- `layout/theme.liquid`: igual
- `sections/header.liquid`: igual
- `sections/lk-product.liquid`: igual
- `config/settings_data.json`: diferente apenas pelo bloco SWYM/Wishlist Plus ausente no dev

Blocos SWYM presentes na produção e ausentes no dev:

- `wishlist-plus / wishlist-app-embed`
- `wishlist-plus / storefront-ui-elements`

## Inventário principal de tags/pixels/scripts

Baseline produção mobile:

- Performance: 43
- LCP: 4.4s
- TBT: 12.950ms
- TTI: 22.5s
- Third-party blocking: 4.800ms
- Requests: 381
- Scripts: 124 requests / ~1.7MB
- Third-party: 160 requests / ~1.58MB

Principais causadores:

- SWYM/Wishlist via Shopify app extension: 41 requests / ~317KB; maior impacto individual de blocking dentro de Shopify.
- Facebook Pixel: 3 requests / ~228KB; ~925ms blocking no baseline.
- Klaviyo: 21 requests / ~117KB; ~456ms blocking no baseline.
- Google Tag Manager/Google Ads/GA4: 26 requests / ~651KB; ~366ms blocking no baseline.
- Crisp: 2 requests / ~4.3KB.
- Attentive: 1 request / ~0.3KB.

## Preview B2 — SWYM off em tema dev/unpublished

Preview URL:

`https://lksneakers.com.br/?preview_theme_id=155065450718`

Resultado Lighthouse mobile no preview dev:

- Performance: 42
- LCP: 4.4s
- TBT: 5.710ms
- TTI: 21.0s
- Third-party blocking: 1.650ms
- SWYM requests: 0

Comparativo principal:

- SWYM requests: 41 → 0
- TBT: 12.950ms → 5.710ms
- Redução estimada de TBT: ~56%
- Third-party blocking: 4.800ms → 1.650ms

## QA básico do preview

Executado via Chromium headless com renderização DOM em:

- Home preview
- Coleção `adidas-samba` preview

Checks:

- HTML renderizou com título válido.
- Script local `LK Wishlist — localStorage` presente.
- Botões `.pc__wishlist` presentes.
- URLs `swym-relay` / `wishlist-plus` ausentes no DOM renderizado do preview.

## Interpretação

O teste confirma que remover/desativar o embed SWYM/Wishlist Plus tem impacto grande em TBT e third-party blocking, sem remover os botões visuais locais de wishlist. A implementação atual do tema já tem fallback localStorage para coração/favoritos, mas a sincronização com a conta/lista real do SWYM deixa de ocorrer quando `window._swat` não existe.

## Riscos

- Médio: desativar SWYM em produção pode quebrar sincronização real de wishlist entre dispositivos/conta.
- Baixo para visual imediato: coração e contador local continuam disponíveis no preview.
- Médio para operação/CRM: se wishlist real alimenta remarketing ou recuperação, precisa validação antes de produção.

## Rollback planejado

Como nenhuma alteração foi feita no dev nesta etapa, não houve snapshot de write novo. Para uma eventual produção futura:

1. Fazer snapshot de `config/settings_data.json` produção.
2. Desativar apenas os blocos SWYM/Wishlist Plus na configuração do tema, sem remover app.
3. Readback público e Lighthouse.
4. Rollback: restaurar os blocos SWYM originais em `config/settings_data.json`.

## Próxima decisão recomendada

Não publicar ainda.

Próximo passo seguro: Lucas validar visualmente o preview e aprovar ou não um teste controlado em produção fora de horário de pico, com janela curta e rollback imediato.

Arquivos técnicos gerados:

- `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/themes_inventory.json`
- `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/theme_tag_inventory.json`
- `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/lighthouse-mobile.json`
- `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/lighthouse-mobile-dev-preview.json`
