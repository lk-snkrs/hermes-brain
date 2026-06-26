# Shopify Production Apply Receipt — PDP CRO Copy/FAQ/Trust

Data UTC: 20260618T183125Z
Status: aplicado e verificado por readback via Admin API.
Escopo: somente `body_html` textual dos 5 PDPs.
Sem alterações em estoque, preço, variantes, tema, SEO title/meta, tags, collections, schema ou campanhas.
values_printed=false

## Resultados
- Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege — `tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege` — verified=True — len 1983 → 1983
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — `nike-moon-shoe-sp-jacquemus-alabaster-amarelo` — verified=True — len 1822 → 1943
- Tênis Onitsuka Tiger Mexico 66 Sabot Crystal Pink Cream Rosa — `tenis-onitsuka-tiger-mexico-66-sabot-crystal-pink-cream-rosa` — verified=True — len 2030 → 1893
- Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — `tenis-adidas-samba-og-crochet-pack-sand-strata-bege` — verified=True — len 3092 → 1851
- Tênis New Balance 1906L Khaki Bege — `tenis-new-balance-1906l-khaki-bege` — verified=True — len 2035 → 1830

## Observação de rollback
`backup-before-each-write.jsonl` contém o body_html anterior salvo antes de cada PUT. Observação: no item 1, o backup foi capturado após a primeira tentativa ter aplicado o novo texto, porque a primeira execução falhou apenas na verificação por hash estrito após o PUT.

## Revisão de impacto
Revisar em ~7 dias: PDP views, add_to_cart rate, begin_checkout rate, purchase rate, receita por PDP e sinais de chat quando disponíveis.

## Public storefront QA
Initial plain fetch showed stale cache on 2 URLs; cache-bust readback verified all required markers on all 5 PDPs. Evidence: `public-readback-check-cachebust.json`.
