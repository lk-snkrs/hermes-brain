# Approval Packet — Correção total upstream Shopify — 2026-06-17

**Status:** preparado, não executado.  
**Writes externos:** 0.  
**Escopo:** corrigir todas as lacunas confiáveis na Shopify como fonte da verdade, em ondas controladas.

## Resposta executiva

Sim, devemos corrigir tudo — mas separado em três grupos:

1. **Corrigir agora em batch controlado:** campos de GMC/SEO com regra clara e backup.
2. **Corrigir após regra aprovada:** `google_product_category`, `gender`, `age_group` e copy SEO quando houver impacto visível.
3. **Não corrigir automaticamente:** MPN, SKU, status/publicação, preço, estoque, disponibilidade, variantes, feed, campanhas e theme.

## Contagem do audit atual
- Produtos/PDPs auditados: 60
- Itens com writes seguros imediatos sem regra pendente: 0
- Itens que precisam regra/copy antes do write: 37
- Itens bloqueados/não propostos agora: 23

## O que eu considero “TUDO” neste projeto

- Todos os PDPs prioritários por GA4 + GSC.
- Todas as lacunas de Shopify upstream que afetam GMC/Search/CTR/AI visibility.
- Depois, expandir para clusters inteiros e finalmente catálogo completo.

## O que NÃO entra em “tudo” sem outro dono/aprovação

- Estoque/disponibilidade/grade: dono é `lk-stock`.
- Produto novo, variante, SKU operacional: handoff `lk-shopify` quando necessário.
- MPN sem fonte confiável: não inferir.
- Feed/GMC direto: só depois que Shopify estiver corrigido ou se houver emergência.
- Theme/campanhas/preço/desconto: fora deste pacote.

## Ondas propostas

### Onda 1 — Top 60 PDPs auditados
- Corrigir `mm-google-shopping.google_product_category` com regra por categoria.
- Corrigir `mm-google-shopping.color` quando ausente e óbvio.
- Ajustar SEO title/description só nos casos com CTR/impressões relevantes e aprovação item a item.
- Backup JSON por produto antes de qualquer write.

### Onda 2 — Clusters comerciais
- 204L, Nike Mind, Onitsuka, Samba, Vomero, Travis, Crocs McQueen, Lululemon.
- Aplicar mesma regra Shopify upstream por cluster.

### Onda 3 — Catálogo completo
- Rodar auditoria Shopify completa.
- Gerar lista de lacunas por metafield.
- Corrigir em lotes com readback e amostragem GMC.

## Regra mínima antes de executar write

Aprovar valores canônicos:
- Categoria Google para sneakers/sapatos.
- Categoria Google para slides/mules/crocs.
- Categoria Google para vestuário/acessórios.
- `gender` padrão quando produto for unissex.
- `age_group` padrão.
- Política de MPN: fonte oficial ou deixar ausente/identifier_exists conforme caso.

## Arquivos
- `approval-packet.json` — plano estruturado produto a produto.

## Itens que precisam regra/copy — amostra top 20

### 1. crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho
- Score: 6.72 | GA4 views: 692 | GSC impr.: 76616
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 2. slide-nike-mind-001-light-smoke-grey-cinza
- Score: 6.07 | GA4 views: 3695 | GSC impr.: 3463
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 3. tenis-nike-vomero-premium-sail-coconut-milk-branco
- Score: 4.54 | GA4 views: 1832 | GSC impr.: 10176
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 4. travis-scott-x-air-jordan-1-low-og-reverse-mocha
- Score: 4.53 | GA4 views: 1224 | GSC impr.: 15209
- Writes candidatos:
  - SEO/descrição Shopify: PENDENTE_COPY
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 5. tenis-nike-x-nocta-hot-step-2-branco
- Score: 3.48 | GA4 views: 748 | GSC impr.: 10637
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 6. tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege
- Score: 3.44 | GA4 views: 2743 | GSC impr.: 0
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 7. slide-nike-mind-001-geode-teal-verde
- Score: 3.32 | GA4 views: 947 | GSC impr.: 3498
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 8. slide-nike-mind-001-light-bone-bege
- Score: 3.05 | GA4 views: 689 | GSC impr.: 3318
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 9. slide-nike-mind-001-black-chrome-preto
- Score: 3.04 | GA4 views: 2331 | GSC impr.: 167
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 10. tenis-on-running-loewe-lightspray-cloudmonster-branco
- Score: 2.92 | GA4 views: 458 | GSC impr.: 285
- Writes candidatos:
  - SEO/descrição Shopify: PENDENTE_COPY
  - SEO/descrição Shopify: PENDENTE_COPY
  - product.metafield mm-google-shopping.color: Branco
  - product.metafield mm-google-shopping.gender: PENDENTE_REGRA_GENDER
- Não automático agora:
  - status/publicação: publicação/despublicação exige decisão separada
  - variant.sku: SKU/variante pode afetar operação; exige lk-shopify/ops e não é Growth sozinho
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 11. ben-jerrys-x-dunk-low-sb-chunky-dunky
- Score: 2.8 | GA4 views: 330 | GSC impr.: 5318
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 12. tenis-adidas-samba-disney-101-dalmatians-penny-branco
- Score: 2.16 | GA4 views: 1420 | GSC impr.: 827
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 13. nike-sb-dunk-low-sandy-ebay-2022
- Score: 2.13 | GA4 views: 1078 | GSC impr.: 0
- Writes candidatos:
  - SEO/descrição Shopify: PENDENTE_COPY
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 14. mule-bravest-studios-bear-claw-black-preto
- Score: 2.04 | GA4 views: 1324 | GSC impr.: 403
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 15. tenis-onitsuka-tiger-mexico-66-sabot-beige-green-bege
- Score: 1.9 | GA4 views: 1197 | GSC impr.: 0
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 16. tenis-nike-vomero-premium-black-volt-preto
- Score: 1.9 | GA4 views: 1065 | GSC impr.: 2799
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 17. slide-nike-mind-001-team-red-vermelho
- Score: 1.56 | GA4 views: 509 | GSC impr.: 0
- Writes candidatos:
  - product.metafield mm-google-shopping.color: Vermelho
  - product.metafield mm-google-shopping.gender: PENDENTE_REGRA_GENDER
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 18. tenis-nike-moon-shoe-sp-jacquemus-off-white
- Score: 1.53 | GA4 views: 835 | GSC impr.: 0
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 19. tenis-nike-vomero-premium-white-bright-crimson-branco
- Score: 1.49 | GA4 views: 766 | GSC impr.: 559
- Writes candidatos:
  - product.metafield mm-google-shopping.google_product_category: PENDENTE_REGRA_CATEGORIA: Shoes/Apparel/Accessory conforme produto
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 20. tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto
- Score: 1.45 | GA4 views: 729 | GSC impr.: 367
- Writes candidatos:
  - SEO/descrição Shopify: PENDENTE_COPY
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor
## Bloqueados/não automáticos — amostra top 20

### 1. tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo
- Score: 4.49 | GA4 views: 2218 | GSC impr.: 8480
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 2. tenis-new-balance-9060-mushroom-arid-stone-camurca
- Score: 3.27 | GA4 views: 1261 | GSC impr.: 3143
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 3. tenis-adidas-samba-og-x-disney-pixar-toy-story
- Score: 2.99 | GA4 views: 962 | GSC impr.: 3619
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 4. tenis-onitsuka-tiger-mexico-66-white-black-branco
- Score: 2.89 | GA4 views: 447 | GSC impr.: 11945
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 5. tenis-nike-vomero-premium-flat-stout-marrom
- Score: 2.83 | GA4 views: 2409 | GSC impr.: 1388
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 6. tenis-adidas-sl72-og-maroon-almost-yellow-marrom
- Score: 2.42 | GA4 views: 406 | GSC impr.: 3356
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 7. tenis-adidas-samba-og-white-floral-embroidery-branco
- Score: 1.87 | GA4 views: 1476 | GSC impr.: 917
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 8. tenis-adidas-samba-og-crochet-pack-sand-strata-bege
- Score: 1.72 | GA4 views: 1106 | GSC impr.: 5229
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 9. tenis-nike-vomero-premium-alabaster-amarelo
- Score: 1.52 | GA4 views: 1127 | GSC impr.: 867
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 10. tenis-new-balance-204l-mushroom-arid-stone-marrom
- Score: 1.39 | GA4 views: 925 | GSC impr.: 2316
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 11. tenis-new-balance-530-turtledove-mushroom-mesh-casual
- Score: 1.24 | GA4 views: 814 | GSC impr.: 1518
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 12. tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo
- Score: 1.22 | GA4 views: 732 | GSC impr.: 2770
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 13. tenis-nike-mind-002-light-khaki-bege
- Score: 1.14 | GA4 views: 793 | GSC impr.: 0
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 14. tenis-new-balance-204l-timberwolf-bege
- Score: 1.08 | GA4 views: 670 | GSC impr.: 1233
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 15. tenis-nike-mind-002-light-smoke-grey-cinza
- Score: 0.97 | GA4 views: 522 | GSC impr.: 1997
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 16. tenis-onitsuka-tiger-mexico-66-sd-beige-beet-juice-bege
- Score: 0.88 | GA4 views: 501 | GSC impr.: 529
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 17. tenis-new-balance-9060-sea-salt-moonbeam-branco
- Score: 0.84 | GA4 views: 377 | GSC impr.: 2267
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 18. tenis-onitsuka-tiger-mexico-66-sd-cream-birch-bege
- Score: 0.77 | GA4 views: 423 | GSC impr.: 0
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 19. tenis-adidas-samba-og-earth-strata-wonder-white-marrom
- Score: 0.73 | GA4 views: 381 | GSC impr.: 0
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor

### 20. tenis-onitsuka-tiger-mexico-66-sabot-dark-brown-marrom
- Score: 0.68 | GA4 views: 326 | GSC impr.: 0
- Não automático agora:
  - variant.metafield mm-google-shopping.mpn: não inferir MPN em massa sem fonte confiável/modelo/SKU/fornecedor