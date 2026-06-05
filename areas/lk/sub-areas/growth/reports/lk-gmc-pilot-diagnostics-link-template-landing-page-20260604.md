# LK GMC — pilot diagnostics: link_template + landing_page_error — 2026-06-04

Modo: read-only/public QA. Nenhum write em GMC, feed, Simprosys ou Shopify.

## Resumo
- Landing page URLs checadas: 44
  - public_qa_rate_limited_429_retry_later: 27
  - mixed_needs_manual_review: 5
  - public_ok_status_lag_or_googlebot_specific: 12
- Ofertas LIA checadas: 50
  - public_qa_rate_limited_429_retry_later: 50
- Limitação: o QA público bateu em 429/rate limit em parte relevante das URLs; isso é limitação do checker público, não confirmação de página quebrada.

## LIA/link_template — conclusão
- O diagnóstico Merchant anterior segue forte: 10.436–10.441 ofertas `local:*` / `LIA_*` vêm de `Simprosys Local Feed (Merchant API)` e estão sem `link_template`/`mobile_link_template` e sem sinal de `store_code`.
- O piloto público atual sofreu 429 nas 50 checagens; uso o relatório de 2026-05-31 como evidência mais limpa de que as PDPs existem/estavam OK em amostra e que a causa-raiz é o contrato do feed local.
- Preview anterior propõe `&store_code={store_code}`, mas isso ainda precisa de confirmação do contrato Simprosys/GBP antes de qualquer write.

## Landing page error — leitura
- 12 URLs retornaram HTML 200 + `.js` 200 no QA atual: provável lag/status Googlebot-specific/reatualização Merchant, não 404 público.
- 32 URLs bateram em 429 no QA público: inconclusivas agora; precisam retry controlado mais lento ou leitura via Shopify/GMC autenticada, sem write.

### Landing URLs OK no QA atual
- `online:pt:BR:20046-3` · HTML 200 / JS 200 · Jaqueta Aphase Relaxed Denim- Black Preto
  - https://lksneakers.com.br/products/jaqueta-aphase-relaxed-denim-black-preto?currency=BRL&country=BR&variant=47007281283294&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:7866599083713103688` · HTML 200 / JS 200 · 38
  - https://lksneakers.com.br/products/tenis-adidas-samba-og-cream-white-cardboard-creme
- `online:pt:BR:DD1873102-11` · HTML 200 / JS 200 · Tênis Nike Dunk Low Next Nature Black White Preto
  - https://lksneakers.com.br/products/nike-dunk-low-next-nature-black-white?currency=BRL&country=BR&variant=44265093464286&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DD1873102-5` · HTML 200 / JS 200 · Tênis Nike Dunk Low Next Nature Black White Preto
  - https://lksneakers.com.br/products/nike-dunk-low-next-nature-black-white?currency=BRL&country=BR&variant=44265093267678&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH4401100-40` · HTML 200 / JS 200 · Tênis Nike Dunk Low Black Paisley Preto
  - https://lksneakers.com.br/products/nike-dunk-low-black-paisley?currency=BRL&country=BR&variant=44265080586462&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH7577001-44` · HTML 200 / JS 200 · Tênis Nike Dunk Low Fossil Rose Azul/Rosa
  - https://lksneakers.com.br/products/nike-dunk-low-fossil-rose?currency=BRL&country=BR&variant=44265073148126&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH9764001-2` · HTML 200 / JS 200 · Tênis Nike Dunk Low GS Black/White Metallic Preto
  - https://lksneakers.com.br/products/nike-dunk-low-gs-black-white-metallic?currency=BRL&country=BR&variant=45739470323934&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH9764001-4` · HTML 200 / JS 200 · Tênis Nike Dunk Low GS Black/White Metallic Preto
  - https://lksneakers.com.br/products/nike-dunk-low-gs-black-white-metallic?currency=BRL&country=BR&variant=45739470258398&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:FQ9112100-3` · HTML 200 / JS 200 · Tênis Nike Air Jordan 1 Low Se "Glitter Swoosh" Branco
  - https://lksneakers.com.br/products/tenis-air-jordan-1-low-se-gs-glitter-swoosh-branco-1?currency=BRL&country=BR&variant=44746890608862&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:HQ6998-600-11` · HTML 200 / JS 200 · Tênis Nike Air Jordan 1 Retro Low OG Chicago (2025) Vermelho
  - https://lksneakers.com.br/products/tenis-nike-air-jordan-1-retro-low-og-chicago-2025-vermelho?currency=BRL&country=BR&variant=47670376661214&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:HQ6998-600-9` · HTML 200 / JS 200 · Tênis Nike Air Jordan 1 Retro Low OG Chicago (2025) Vermelho
  - https://lksneakers.com.br/products/tenis-nike-air-jordan-1-retro-low-og-chicago-2025-vermelho?currency=BRL&country=BR&variant=47670376595678&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:dd1873-100-1` · HTML 200 / JS 200 · Tênis Dunk Low Next Nature Pink Pale Coral Rosa
  - https://lksneakers.com.br/products/dunk-low-next-nature-pink-pale-coral?currency=BRL&country=BR&variant=44269130940638&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e

## Próxima decisão
1. LIA: aprovar contato/check com Simprosys ou leitura de configuração no app para confirmar `store_code` e local `link_template`; sem isso, não recomendo patch em massa.
2. Landing: rodar retry lento das 32 URLs 429 + cruzar com Shopify status/variant se conector read-only estiver disponível.
3. Qualquer alteração de feed/GMC/Shopify continua bloqueada até aprovação explícita.

JSON completo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-gmc-pilot-diagnostics-link-template-landing-page-20260604.json`