# LK Dia dos Namorados — checklist operacional + preview read-only

Status: `preview_readonly_no_external_write`
Fonte: Alinhamento Semanal LK + Check 2026-05-15 + SQLite local LK OS.

## Decisão operacional

Não esperar. A próxima ação segura é fechar o pacote operacional antes de qualquer disparo: produto elegível, gift card, segmentação, criativo, influenciadores e calendário.

## Guardrails

- Sem Klaviyo/e-mail/WhatsApp/campanha sem aprovação explícita de Lucas.
- Sem Shopify/Tiny/theme write sem preview + rollback + aprovação.
- Produto de campanha deve cruzar estoque Shopify/local e, quando possível, Tiny/alias; item sem SKU ou com dado ambíguo não entra em automação.

## Checklist Dia dos Namorados
- [ ] Fechar lista de produtos por categoria: pronta entrega, promoção, gift card.
- [ ] Validar estoque por SKU/tamanho antes de incluir produto em comunicação.
- [ ] Definir gift cards: R$ 500, R$ 1.000, R$ 1.500, R$ 2.000, R$ 2.500.
- [ ] Definir regras do gift card: validade, uso parcial/total, troca/devolução, atendimento e tracking.
- [ ] Fechar influenciadores: casal macro ou peças separadas por persona.
- [ ] Criar briefing de e-mails: presente para ele, presente para ela, last chance e gift card.
- [ ] Criar segmentação CRM/Klaviyo: clientes premium, compradores recentes, wishlist/interesse, abandono de carrinho.
- [ ] Definir calendário: primeiro disparo próxima semana; contingência na semana seguinte.
- [ ] Medir resultado por receita Shopify, conversão, add-to-cart e ticket médio; não usar métrica de plataforma como venda real.

## Preview de produtos — promoção
- **Tênis adidas Campus 00s Scarlet Red Vermelho** — SKU `H03474-4` — 37 — qtd local 4 — R$ 699.99 de R$ 1749.99 (60.0% off) — confiança `medium_local_shopify_stock_only`
- **Tênis Adidas Campus 00s Crystal White Branco** — SKU `GY0042-2` — 37 — qtd local 1 — R$ 699.99 de R$ 1599.99 (56.3% off) — confiança `medium_local_shopify_stock_only`
- **Tênis Adidas Campus 00s Grey Three Cinza** — SKU `HQ8707-4` — 34 — qtd local 2 — R$ 699.99 de R$ 1499.99 (53.3% off) — confiança `medium_local_shopify_stock_only`
- **Tênis adidas Campus 00s Ambient Sky Azul** — SKU `GY9473-4` — 37 — qtd local 1 — R$ 699.99 de R$ 1499.99 (53.3% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Peace Talk Preto** — SKU `PEACETALK2-2` — M — qtd local 3 — R$ 109.99 de R$ 229.99 (52.2% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Peace Talk Branco** — SKU `PEACKTALK1-2` — M — qtd local 2 — R$ 109.99 de R$ 229.99 (52.2% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Stunt Master Cinza** — SKU `STUNT2-1` — S/P — qtd local 2 — R$ 109.99 de R$ 229.99 (52.2% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Stunt Master Preto** — SKU `STUNT1-1` — S/P — qtd local 2 — R$ 109.99 de R$ 229.99 (52.2% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Stunt Master Azul** — SKU `STUNT3-1` — S/P — qtd local 1 — R$ 109.99 de R$ 229.99 (52.2% off) — confiança `medium_local_shopify_stock_only`
- **Tênis adidas Campus 00s Bliss Pink Rosa** — SKU `IF3968-1` — 34 — qtd local 1 — R$ 699.99 de R$ 1449.90 (51.7% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Basic Pack 5.8 Verde** — SKU `SF2BSP5-2` — P — qtd local 3 — R$ 74.99 de R$ 149.99 (50.0% off) — confiança `medium_local_shopify_stock_only`
- **Tênis Nike Sb Dunk Low x Futura Skateboard Bleached Aqua Azul** — SKU `HF6061-400-2` — 37 — qtd local 2 — R$ 2999.99 de R$ 5999.90 (50.0% off) — confiança `medium_local_shopify_stock_only`
- **Camiseta Sufgang Basic Pack 5.8 Azul** — SKU `SF2BSP7-1` — PP — qtd local 1 — R$ 74.99 de R$ 149.99 (50.0% off) — confiança `medium_local_shopify_stock_only`
- **Tênis Nike Air Jordan 1 Low Guava Ice Preto** — SKU `DC0774003` — 34 — qtd local 1 — R$ 2199.99 de R$ 3999.99 (45.0% off) — confiança `medium_local_shopify_stock_only`
- **Tênis Yeezy Boost 350 V2 Onyx Preto** — SKU `HQ4540-45` — 45 — qtd local 2 — R$ 1999.99 de R$ 3499.99 (42.9% off) — confiança `medium_local_shopify_stock_only`

## Preview de produtos — pronta entrega sem promoção
- **Adidas Taekwondo Mei Ballet Preto e Branco** — SKU `JR7031` — 42 — qtd local 1 — R$ 1999.99 — confiança `medium_local_shopify_stock_only`
- **Bermuda Chino Saint Studio Supima Caqui** — SKU `ST1-2` — 40 — qtd local 1 — R$ 369.99 — confiança `medium_local_shopify_stock_only`
- **Bermuda Nude Project Capicci Capri Jeans** — SKU `NP04-8` — Blue / L/G — qtd local 2 — R$ 1599.99 — confiança `medium_local_shopify_stock_only`
- **Bolsa Lululemon Slouchy Sling 6L** — SKU `11750230-3` — Black — qtd local 10 — R$ 999.99 — confiança `medium_local_shopify_stock_only`
- **Bolsa Minimal Saint Studio Cacto Caramelo (DF)** — SKU `ST4` — Default Title — qtd local 1 — R$ 629.99 — confiança `medium_local_shopify_stock_only`
- **Bolsa Nike x Jacquemus Small Swoosh Bag Branco (DF)** — SKU `NIKEXJAC1` — Default Title — qtd local 1 — R$ 3999.99 — confiança `medium_local_shopify_stock_only`
- **Bolsa Nike x Jacquemus Small Swoosh Bag Vermelho** — SKU `NIKEJAC2` — Default Title — qtd local 2 — R$ 3999.99 — confiança `medium_local_shopify_stock_only`
- **Boné 6 Panel Aimé Leon Dore Cycling Logo Azul** — SKU `Aime5` — Default Title — qtd local 2 — R$ 999.99 — confiança `medium_local_shopify_stock_only`
- **Boné 6 Panel Aimé Leon Dore Script Sport Black Preto** — SKU `SCRIPTSPORT` — Default Title — qtd local 1 — R$ 999.99 — confiança `medium_local_shopify_stock_only`
- **Boné 6 Panel Onitsuka Tiger x Astroboy Preto** — SKU `3183B170001` — Default Title — qtd local 2 — R$ 1499.99 — confiança `medium_local_shopify_stock_only`
- **Boné 6 Panel Onitsuka Tiger x Astroboy Washed Verde** — SKU `3183B151400` — Default Title — qtd local 2 — R$ 1499.99 — confiança `medium_local_shopify_stock_only`
- **Boné 6 Panel Supreme Pigment S Logo Rosa** — SKU `SUPPIGMENT2` — Default Title — qtd local 1 — R$ 899.99 — confiança `medium_local_shopify_stock_only`
- **Boné Alo Yoga Washed Off-Duty** — SKU `42337316700340-4` — Sand Dollar — qtd local 1 — R$ 999.99 — confiança `medium_local_shopify_stock_only`
- **Boné Lululemon Classic Ball Wordmark** — SKU `11700328-1` — Bone/White — qtd local 1 — R$ 599.99 — confiança `medium_local_shopify_stock_only`
- **Boné Supreme Military Camp Cap (SS25) Coral Laranja** — SKU `SUPSS2504` — Default Title — qtd local 1 — R$ 899.99 — confiança `medium_local_shopify_stock_only`
- **Boné Supreme Military Camp Cap (SS25) Tan Bege** — SKU `SUPSS2503` — Default Title — qtd local 1 — R$ 899.99 — confiança `medium_local_shopify_stock_only`
- **Calça Alo Yoga Serenity Wide Leg Preto** — SKU `w54162r-4` — L/G — qtd local 1 — R$ 1399.99 — confiança `medium_local_shopify_stock_only`
- **Calça Baggy Nude Project Old Jeans** — SKU `NP12-4` — Black / L/G — qtd local 1 — R$ 1999.99 — confiança `medium_local_shopify_stock_only`
- **Calça Baggy Nude Project Old Jeans Animal Print** — SKU `NP13-2` — L/G — qtd local 2 — R$ 2399.99 — confiança `medium_local_shopify_stock_only`
- **Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex® - Canvas Bege** — SKU `1022913-1` — 38 — qtd local 1 — R$ 899.99 — confiança `medium_local_shopify_stock_only`

## Backlog Check/CRO
- [ ] PDP: destacar modelos/variações sem poluir mobile.
- [ ] Ícone endereço/mapa com clique para localização da loja.
- [ ] Personas/influenciadores: usar apenas assets com evidência de engajamento/performance.
- [ ] Repositório cloud de fotos padronizado por influencer/persona/produto.
- [ ] Experimento CRO 0,13% → 0,20% com baseline e métrica antes/depois.

## Rarity / 3D spray
- [ ] Rarity como mini-lançamento premium, não só SKU novo.
- [ ] Confirmar data/evento antes de calendário final.
- [ ] Novo tênis 3D/spray: disparo só com conteúdo pronto.
- [ ] Primeiro disparo sem desconto; teste A/B com desconto apenas depois.

Relatório JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-dia-dos-namorados-product-selection-preview-2026-05-15.json`