# LK Sourcing Ops v2 — markup 2 + tamanho exato obrigatório

Generated: `2026-05-15T00:15:49.582776+00:00`

## Veredito

- Correção aplicada: **não existe mais x2 dentro do custo**.
- Fórmula correta: `custo landed = (preço exato USD do tamanho + custo trazer USD) × (dólar × 1,05)`.
- Markup 2: `preço de venda ideal = custo landed × 2`.
- Correção aplicada: **não usar preço product-level do KicksDev/StockX como custo do tamanho**. Ele fica só como sinal/foto.
- Correção Lucas 2026-05-15: **Júlio nunca preenche valor**; Hermes deve buscar/validar o preço exato por tamanho.
- Cards Notion atualizados com campos de decisão e guardrail de preço exato por tamanho.
- API do Notion não cria/edita views; a Mesa Júlio foi materializada como campos + Mission Control + instrução. A view visual deve ser criada/ajustada na UI filtrando esses campos.

## Mesa de Revisão Diária Júlio

Filtro sugerido no Notion:
- `Status da Compra` = `Aguardando Aprovação`
- `Decisão Sourcing` = `Hermes validar preço/tamanho` ou `Comprar nacional`
- ordenar por prioridade/demanda no título/relatório

Colunas sugeridas: Foto Produto, Nome, Modelo, Tamanho, Custo, Preço exato tam USD, Custo trazer USD, Custo landed BRL, Venda ideal BRL, Margem venda atual %, Fonte preço tam, Decisão Sourcing, Link.

## Cards
### Tênis New Balance 204L Arid Timberwolf Bege — Tam 37 — `U204LMMC-4`
- Foto: https://images.stockx.com/images/New-Balance-204L-Timberwolf-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1755810545
- Custo nacional: R$ 1.999,90 · margem nacional: 28.6%
- StockX product-level sinal min: US$ 73.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-New-Balance-204L-Arid-Timberwolf-Bege-Tam-37-U204LMMC-4-36027dc9e03381c98ea4c56e8009b997

### Tênis New Balance 204L Arid Timberwolf Bege — Tam 39 — `U204LMMC-6`
- Foto: https://images.stockx.com/images/New-Balance-204L-Timberwolf-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1755810545
- Custo nacional: R$ 2.380,00 · margem nacional: 15.0%
- StockX product-level sinal min: US$ 73.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-New-Balance-204L-Arid-Timberwolf-Bege-Tam-39-U204LMMC-6-36027dc9e033810e92bcc95b198f12bb

### Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 38 — `1183A201-126-5`
- Foto: https://images.stockx.com/images/Onitsuka-Tiger-Mexico-66-SD-White-Black-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1762290768
- Custo nacional: R$ 1.890,00 · margem nacional: 21.2%
- StockX product-level sinal min: US$ 127.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Onitsuka-Tiger-Mexico-66-White-Black-Branco-Tam-38-1183A201-126-5-36027dc9e03381918781ec911b85568a

### Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 37 — `1183A201-126-4`
- Foto: https://images.stockx.com/images/Onitsuka-Tiger-Mexico-66-SD-White-Black-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1762290768
- Custo nacional: R$ 1.890,00 · margem nacional: 21.2%
- StockX product-level sinal min: US$ 127.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Onitsuka-Tiger-Mexico-66-White-Black-Branco-Tam-37-1183A201-126-4-36027dc9e03381648fdbfb85da79665f

### Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 38 — `HV8547-700-5`
- Foto: https://images.stockx.com/images/Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1759525738
- Custo nacional: R$ 6.500,00 · margem nacional: -8.3%
- StockX product-level sinal min: US$ 410.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Amarelo-Tam-38-HV8547-700-5-36027dc9e03381c4aee2ece6179732eb

### Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 37 — `HV8547-700-4`
- Foto: https://images.stockx.com/images/Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1759525738
- Custo nacional: R$ 6.500,00 · margem nacional: -30.0%
- StockX product-level sinal min: US$ 410.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Amarelo-Tam-37-HV8547-700-4-36027dc9e03381d7ac1dcf165f293ae7

### Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — Tam 41.5 — `1183C102.751`
- Foto: https://images.stockx.com/images/Onitsuka-Tiger-Mexico-66-Kill-Bill-2022-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1738193358
- Custo nacional: R$ 1.890,00 · margem nacional: 21.2%
- StockX product-level sinal min: US$ 142.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Onitsuka-Tiger-Mexico-66-Kill-Bill-Amarelo-Tam-41-5-1183C102-751-36027dc9e033815a9d91d43d26514ecb

### Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — Tam 35 — `JR9446-2`
- Foto: https://images.stockx.com/images/adidas-Samba-OG-Crochet-Pack-Sand-Strata-Womens-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1751922766
- Custo nacional: R$ 1.299,99 · margem nacional: 40.9%
- StockX product-level sinal min: US$ 90.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Comprar nacional`
- Notion: https://www.notion.so/Sourcing-T-nis-Adidas-Samba-OG-Crochet-Pack-Sand-Strata-Bege-Tam-35-JR9446-2-36027dc9e03381c28bf4c5fc04218d6a

### Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 36 — `HV8547-700-3`
- Foto: https://images.stockx.com/images/Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1759525738
- Custo nacional: n/d · margem nacional: n/d
- StockX product-level sinal min: US$ 410.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Nike-Moon-Shoe-SP-Jacquemus-Alabaster-Amarelo-Tam-36-HV8547-700-3-36027dc9e03381fcb001f6fdd137a1af

### Tênis New Balance 204L Arid Timberwolf Bege — Tam 38 — `U204LMMC-5`
- Foto: https://images.stockx.com/images/New-Balance-204L-Timberwolf-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1755810545
- Custo nacional: R$ 1.999,90 · margem nacional: 28.6%
- StockX product-level sinal min: US$ 73.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-New-Balance-204L-Arid-Timberwolf-Bege-Tam-38-U204LMMC-5-36027dc9e03381fdbddae164276c8065

### Tênis New Balance 204L Arid Timberwolf Bege — Tam 40 — `U204LMMC-7`
- Foto: https://images.stockx.com/images/New-Balance-204L-Timberwolf-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1755810545
- Custo nacional: R$ 2.380,00 · margem nacional: 15.0%
- StockX product-level sinal min: US$ 73.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-New-Balance-204L-Arid-Timberwolf-Bege-Tam-40-U204LMMC-7-36027dc9e03381c68b73e983dae0d7ea

### Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 36 — `1183A201-126-3`
- Foto: https://images.stockx.com/images/Onitsuka-Tiger-Mexico-66-SD-White-Black-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1762290768
- Custo nacional: R$ 1.999,99 · margem nacional: 16.7%
- StockX product-level sinal min: US$ 127.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Onitsuka-Tiger-Mexico-66-White-Black-Branco-Tam-36-1183A201-126-3-36027dc9e03381719a11c33a182b4a48

### Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 40 — `1183A201-126-7`
- Foto: https://images.stockx.com/images/Onitsuka-Tiger-Mexico-66-SD-White-Black-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1762290768
- Custo nacional: R$ 2.389,70 · margem nacional: 0.4%
- StockX product-level sinal min: US$ 127.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Hermes validar preço/tamanho`
- Notion: https://www.notion.so/Sourcing-T-nis-Onitsuka-Tiger-Mexico-66-White-Black-Branco-Tam-40-1183A201-126-7-36027dc9e03381fcbd2cfe91afe856e7

### Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — Tam 36 — `JR9446-3`
- Foto: https://images.stockx.com/images/adidas-Samba-OG-Crochet-Pack-Sand-Strata-Womens-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1751922766
- Custo nacional: R$ 899,00 · margem nacional: 59.1%
- StockX product-level sinal min: US$ 90.00 — **não usado como custo**
- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher
- Decisão inicial: `Comprar nacional`
- Notion: https://www.notion.so/Sourcing-T-nis-Adidas-Samba-OG-Crochet-Pack-Sand-Strata-Bege-Tam-36-JR9446-3-36027dc9e033817f8c4de25549ed69f7

