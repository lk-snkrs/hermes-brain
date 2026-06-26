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

Fonte completa: `reports/lk-sourcing-ops-v2-markup2-exact-size-2026-05-15.md`
