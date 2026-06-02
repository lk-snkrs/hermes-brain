# LK Sneakers — Shopify Template Payload Re-audit

Data UTC: 20260601T153551Z
Escopo: leitura pública do storefront pós-promoção para Production. Sem writes Shopify/GMC/Klaviyo/ads.

## Veredito

A mudança reduziu o HTML inicial, mas a redução imediata é pequena no peso total da página porque o gargalo principal do template Shopify continua sendo dados/scripts inline de apps e seções, especialmente Variant King/StarApps (`window.vkcl_data` ~460 KB por página). A melhora mais relevante é qualitativa: Judge.me preloader saiu de home/collection e o footer passou a usar assets cacheáveis, reduzindo parsing repetido no documento HTML.

## Amostras medidas

- Home: https://www.lksneakers.com.br/
- Collection: https://www.lksneakers.com.br/collections/sale
- PDP: https://www.lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco

## Comparativo de tamanho HTML decodificado

- Home antes: ~1,149,219 bytes
- Home agora: 1,136,013 bytes
- Delta home: -13,206 bytes (-1.15%)

- PDP antes aproximado: ~1,240,000 bytes
- PDP agora: 1,220,631 bytes
- Delta PDP aprox.: -19,369 bytes (-1.56%)

- Collection antes aproximado: ~1,310,000 bytes
- Collection agora: 1,305,036 bytes
- Delta collection aprox.: -4,964 bytes (-0.38%)

## Medições atuais por template

### Home

- Status: 200
- HTML decodificado: 1,136,013 bytes
- Transferência medida: 113,536 bytes
- Script tags: 66
- External scripts: 14
- Inline script bytes: 750,813
- Style tags: 41
- Inline style bytes: 285,344
- External CSS links: 8
- JSON-LD blocks: 2
- Schema types: Organization/ShoeStore/ClothingStore, WebSite
- Judge.me preloader: 0
- Variant King `window.vkcl_data`: 1
- `lk-footer.css`: 1
- `lk-footer.js`: 1
- Liquid errors: 0

### Collection

- Status: 200
- HTML decodificado: 1,305,036 bytes
- Transferência medida: 125,576 bytes
- Script tags: 68
- External scripts: 14
- Inline script bytes: 798,937
- Style tags: 24
- Inline style bytes: 323,545
- External CSS links: 8
- JSON-LD blocks: 3
- Schema types: Organization/ShoeStore/ClothingStore, BreadcrumbList, CollectionPage
- Judge.me preloader: 0
- Variant King `window.vkcl_data`: 1
- `lk-footer.css`: 1
- `lk-footer.js`: 1
- Liquid errors: 0

### PDP

- Status: 200
- HTML decodificado: 1,220,631 bytes
- Transferência medida: 125,520 bytes
- Script tags: 71
- External scripts: 16
- Inline script bytes: 825,022
- Style tags: 22
- Inline style bytes: 296,664
- External CSS links: 9
- JSON-LD blocks: 4
- Schema types: Organization/ShoeStore/ClothingStore, Product, BreadcrumbList, FAQPage
- Judge.me preloader: 1 (esperado na PDP)
- Variant King `window.vkcl_data`: 1
- `lk-footer.css`: 1
- `lk-footer.js`: 1
- Liquid errors: 0

## Principais fontes de peso atuais

- Variant King / StarApps: `window.vkcl_data` ~460 KB inline por página.
- Rivo/Judge.me app settings: ~95–101 KB inline por página.
- App script Simprosys/GSF: ~48 KB inline por página.
- Custom/cart/theme scripts inline: ~15–36 KB em blocos separados.
- CSS inline remanescente por template: ~285–323 KB.

## Leitura Shopify-template

Em Shopify, o tamanho bruto do HTML não cai dramaticamente quando apps injetam dados globais inline. A melhora mais segura vem de:

1. Gate por template: carregar scripts/widgets só onde precisam existir.
2. Externalizar CSS/JS de seções do tema para assets cacheáveis.
3. Reduzir DOM/loops de Liquid em seções repetidas.
4. Evitar app embeds globais quando o app só é útil em PDP/cart.
5. Preservar apps obrigatórios e medir impacto por template: home, collection, PDP.

## Próximos alvos recomendados

P1 — Collection template:
- Auditar `sections/lk-collection.liquid` e blocos relacionados.
- Extrair CSS/JS inline grande para assets cacheáveis.
- Reduzir lógica/markup duplicado de cards/filtros/trust strips.

P1 — Apps globais:
- Verificar se Rivo/Judge.me settings precisam aparecer em home/collection ou se podem ser gateados com segurança.
- Não remover Rivo/Judge.me; só condicionar onde não afeta funcionalidade.

P2 — Variant King:
- Não remover, conforme decisão do Lucas.
- Investigar se há configuração de app para reduzir escopo/dados em páginas sem variante ativa, mas qualquer mudança de app/admin exige preview e aprovação.

P2 — Performance lab:
- Medir Lighthouse/PSI mobile quando quota/Chrome estiver disponível.
- O peso HTML menor não garante LCP/INP melhor sem medir parse/execute JS.

## Não realizado

- Nenhum write Shopify.
- Nenhum app/admin setting alterado.
- Nenhum produto/preço/estoque/checkout alterado.
- Nenhum GMC/Klaviyo/Meta/WhatsApp/e-mail/campanha alterado.
