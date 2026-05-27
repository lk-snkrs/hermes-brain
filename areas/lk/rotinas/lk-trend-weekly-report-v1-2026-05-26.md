# LK Trend Weekly v1 — primeira edição read-only

Status: relatório v1 gerado; sem writes externos.
Data de geração: 2026-05-26.
Escopo: LK Sneakers.
Modo: relatório semanal + fila de oportunidades.

## Fontes usadas

- Data Spine local LK: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite`.
- Janela interna de vendas disponível no snapshot: últimos 90 dias até `2026-04-16`.
- Tiny snapshot local: `tiny_stock_20260515T092206Z`, depósito oficial `LK | CONTROLE ESTOQUE` quando mapeado.
- Web/current trend read-only:
  - InStyle, abril/2026: ballet sneakers como tendência de verão, citando Puma Speedcat Ballet e Adidas Taekwondo Mei.
  - ELLE UK, 2026: Mary Jane-sneakers mainstream; StockX reporta +350% YoY em Q1 2026; top sellers concentrados em Nike Air Rift, Adidas Samba Jane e Onitsuka Tiger Mexico 66 TGRS.
  - Who What Wear, 2026: Nike Air Rift com demanda de revenda em alta, vendas +100% YoY e preço médio +50% segundo StockX.

## Leitura executiva

- A tendência externa mais forte para LK nesta semana é o bloco **ballet / Mary Jane / low-profile sneaker**.
- A demanda interna confirma que LK já vende bem famílias relacionadas: Onitsuka Mexico 66/Sabot, Adidas Samba Jane/Taekwondo, Puma Speedcat, Nike Air Rift e Nike Moon Shoe Jacquemus.
- A fila de **conteúdo** está mais pronta que a fila de compra: há boa evidência de tendência + histórico de vendas.
- A fila de **compra/reposição** só ficou segura para alguns SKUs de Alo Yoga, porque o snapshot local do Tiny mapeia esses SKUs com estoque oficial zerado/baixo. Para sneakers, muitos SKUs top aparecem como `blocked_tiny_not_mapped`, então não devem virar compra sem rodar validação Tiny live por SKU/tamanho.
- Não foi executado nenhum Shopify/Tiny/Merchant/Klaviyo/WhatsApp write, compra ou contato.

## Top oportunidades P1

### P1-1 — Conteúdo: Mary Jane / ballet sneakers para LK

- Categoria primária: conteúdo.
- Score: 91/100.
- Confiança: alta para conteúdo; média para qualquer compra.
- Sinal principal: tendência externa forte e concentrada em Nike Air Rift, Adidas Samba Jane, Onitsuka Tiger Mexico 66 TGRS, Adidas Taekwondo e Puma Speedcat.
- Evidência externa:
  - ELLE UK cita Mary Jane-sneakers como mainstream em 2026, +350% YoY no StockX Q1 2026 e top sellers concentrados em poucos modelos.
  - InStyle posiciona ballet sneakers como tendência de verão 2026.
- Evidência interna LK:
  - Adidas Samba Jane: 81 unidades históricas somando Scarlet Gum, Black White Gum, White Black, Cream Black Gum, Green White Gum e White Blue Gum.
  - Adidas Taekwondo: múltiplas cores vendidas; Preto e Branco teve 12 unidades históricas; Black Gum 8 unidades.
  - Nike Air Rift: 14 unidades históricas somando Light Orewood Brown, Triple Black e Sail.
  - Puma Speedcat: 40 unidades históricas em linhas OG/Archive/TTF/Pelé/Pink/Faded.
- Shopify/Tiny: usar como pauta/conteúdo, não como disponibilidade prometida.
- Risco: confundir trend editorial com compra imediata.
- Próxima ação segura: gerar preview interno de conteúdo/pauta com 3 blocos: “o que são”, “como usar”, “modelos LK relacionados”.
- Aprovação necessária: só se virar campanha/envio/publicação.

### P1-2 — Conteúdo + catálogo futuro: Onitsuka Mexico 66 / Sabot / TGRS

- Categoria primária: conteúdo.
- Score: 89/100.
- Confiança: alta para conteúdo; baixa/média para compra sem Tiny live.
- Evidência interna LK:
  - Onitsuka Tiger Mexico 66 Kill Bill: 53 unidades e R$ 127.199 em vendas nos últimos 90 dias do snapshot.
  - Onitsuka Tiger Mexico 66 Sabot Beige Green: 20 unidades e R$ 43.999 nos últimos 90 dias; histórico total consultado mostra 72 unidades.
  - Onitsuka Tiger Mexico 66 SD Cream Birch: 32 unidades e R$ 79.999 nos últimos 90 dias.
  - Mexico 66 White Black: 24 unidades e R$ 57.599 nos últimos 90 dias.
- Evidência externa: ELLE UK cita Onitsuka Tiger Mexico 66 TGRS entre os poucos modelos que concentram top sellers da tendência Mary Jane-sneaker.
- Shopify/Tiny: muitos SKUs Onitsuka top ainda aparecem não mapeados no snapshot local; não usar para compra automática.
- Risco: SKU/tamanho ambíguo, principalmente modelos com pontuação/espaço no código.
- Próxima ação segura: preview de conteúdo “Guia Onitsuka Mexico 66: normal, SD, Sabot e TGRS” + validação Tiny live só se Lucas quiser compra/reposição.
- Aprovação necessária: publicação/campanha ou sourcing.

### P1-3 — Conteúdo: Nike Moon Shoe SP Jacquemus como ponte fashion sneaker

- Categoria primária: conteúdo.
- Score: 86/100.
- Confiança: alta para conteúdo.
- Evidência interna LK:
  - Nike Moon Shoe SP Jacquemus Off White: 44 unidades e R$ 219.999 nos últimos 90 dias.
  - Medium Brown: 34 unidades e R$ 169.999 nos últimos 90 dias.
  - Alabaster: 21 unidades e R$ 113.399 nos últimos 90 dias.
  - University Red: 15 unidades e R$ 91.299 nos últimos 90 dias.
  - Off Noir: 15 unidades e R$ 82.999 nos últimos 90 dias.
- Evidência externa: tendência de low-profile/fashion-forward sneaker favorece narrativas de sneaker como objeto de moda, não só performance.
- Shopify/Tiny: vários SKUs com lacuna de mapeamento Tiny no snapshot; não transformar em compra sem resolver SKU/tamanho.
- Risco: conteúdo ficar muito genérico se não usar cor/modelo específico.
- Próxima ação segura: pauta editorial/CRM “Jacquemus x Nike e o tênis de moda baixo” com links internos dos produtos existentes.
- Aprovação necessária: publicação/envio.

### P1-4 — Compra/reposição: Alo Yoga Suit Up Trouser Preto — SKUs zerados com venda recente

- Categoria primária: compra/reposição.
- Score: 84/100.
- Confiança: alta dentro do snapshot local Tiny para os SKUs listados; média por causa da defasagem da base.
- Evidência interna LK + Tiny oficial:
  - Regular Preto XXS/PPP — SKU `w51432r_01-1`: 6 unidades vendidas nos últimos 90 dias; Tiny oficial `LK | CONTROLE ESTOQUE`: 0.
  - Regular Preto M/M — SKU `w51432r_01-4`: 4 unidades vendidas nos últimos 90 dias; Tiny oficial: 0.
  - Regular Preto L/G — SKU `w51432r_01-5`: 2 unidades vendidas nos últimos 90 dias; Tiny oficial: 0.
  - Long Preto S/P — SKU `w54187r_00-3`: 5 unidades vendidas nos últimos 90 dias; Tiny oficial: 0.
- Risco: não é sneaker trend; é reposição de apparel com demanda real. Precisa confirmar lead time/fornecedor antes de qualquer ação.
- Próxima ação segura: preparar pacote Júlio/compra com validação de fornecedor e custo, sem contato automático.
- Aprovação necessária: qualquer contato, compra, reserva ou Notion externo/produtivo.

### P1-5 — Conteúdo/watchlist: New Balance 204L

- Categoria primária: conteúdo.
- Score: 82/100.
- Confiança: alta para demanda interna; média para trend externo nesta rodada.
- Evidência interna LK:
  - New Balance 204L Mushroom Arid Stone: 45 unidades e R$ 125.999 nos últimos 90 dias; histórico total consultado: 119 unidades.
  - New Balance 204L Arid Timberwolf: 44 unidades e R$ 123.059 nos últimos 90 dias; histórico total consultado: 83 unidades.
  - Silver Metallic Black, Pastel Pink, Sea Salt Linen e outras variações com vendas menores recentes.
- Evidência externa: sinal genérico de slim/low-profile sneakers; não tão forte quanto Mary Jane/Air Rift nesta coleta.
- Shopify/Tiny: SKUs top não apareceram mapeados no Tiny snapshot local; não recomendar compra ainda.
- Risco: virar compra ampla demais sem validação por tamanho.
- Próxima ação segura: conteúdo/CRM “New Balance 204L: guia de cores neutras” e watchlist de ruptura por tamanho.
- Aprovação necessária: publicação/envio ou sourcing.

## Fila de conteúdo

1. Mary Jane / ballet sneakers LK
   - Tipo: blog/source page/newsletter/CRM.
   - Evidência: InStyle + ELLE UK + vendas internas de Samba Jane/Taekwondo/Air Rift/Speedcat/Onitsuka.
   - Próxima ação segura: preview de pauta/copy.

2. Onitsuka Mexico 66: normal vs SD vs Sabot vs TGRS
   - Tipo: SEO/source page/PDP storytelling.
   - Evidência: Onitsuka domina vendas internas recentes; TGRS citado como trend externo.
   - Próxima ação segura: preview de guia editorial.

3. Nike Moon Shoe Jacquemus
   - Tipo: CRM/editorial premium.
   - Evidência: alto GMV interno nos últimos 90 dias.
   - Próxima ação segura: preview de narrativa fashion sneaker.

4. New Balance 204L neutros
   - Tipo: CRM/SEO/collection copy.
   - Evidência: 204L Mushroom + Arid Timberwolf somam 89 unidades nos últimos 90 dias.
   - Próxima ação segura: preview de pauta/coleção.

5. Air Rift / tabi sneaker
   - Tipo: trend note/watchlist editorial.
   - Evidência: Who What Wear + ELLE UK; vendas internas menores mas coerentes.
   - Próxima ação segura: observar e incluir em conteúdo Mary Jane/tabi se houver estoque/produto ativo.

## Fila de compra/reposição

Somente itens com Tiny oficial mapeado no snapshot local:

1. Alo Yoga Suit Up Trouser Regular Preto — XXS/PPP
   - SKU: `w51432r_01-1`.
   - Vendas 90d: 6.
   - Tiny oficial: 0.
   - Próxima ação segura: pacote Júlio/fornecedor.

2. Alo Yoga Suit Up Trouser Long Preto — S/P
   - SKU: `w54187r_00-3`.
   - Vendas 90d: 5.
   - Tiny oficial: 0.
   - Próxima ação segura: pacote Júlio/fornecedor.

3. Alo Yoga Suit Up Trouser Regular Preto — M/M
   - SKU: `w51432r_01-4`.
   - Vendas 90d: 4.
   - Tiny oficial: 0.
   - Próxima ação segura: pacote Júlio/fornecedor.

4. Boné 5 Panel Aimé Leon Dore Unisphere Branco
   - SKU: `UNISPHERE`.
   - Vendas 90d: 3.
   - Tiny oficial: 0.
   - Próxima ação segura: observar/validar fornecedor; menor prioridade que Alo.

5. Alo Yoga Airlift High-Waist 7/8 Line Up Legging Gravel Bege — S/P
   - SKU: `w51154r13-3`.
   - Vendas 90d: 2.
   - Tiny oficial: 0.
   - Próxima ação segura: watchlist ou validação leve.

## Watchlist

- Puma Speedcat
  - Sinal: trend externo + 40 unidades históricas internas.
  - Por que não virou compra: precisa validação Tiny por tamanho e fonte.

- Adidas Samba Jane
  - Sinal: ELLE UK cita como top seller do trend; LK já vendeu bem.
  - Por que não virou compra: sem validação Tiny live nesta rodada.

- Nike Air Rift
  - Sinal: Who What Wear e ELLE UK fortes; LK tem histórico menor porém coerente.
  - Por que não virou compra: precisa checar produto ativo/estoque/tamanho atual.

- Nike Mind 001 / 002
  - Sinal: vendas internas fortes, especialmente Light Smoke Grey e Black Chrome.
  - Por que não virou conteúdo P1: sem sinal externo forte coletado nesta rodada.

## Bloqueios e dados faltantes

- Snapshot interno de vendas termina em `2026-04-16`; não use como “hoje vendeu” sem refresh.
- Tiny local está parcial/desalinhado para muitos SKUs de sneakers; Onitsuka, New Balance e Nike Moon aparecem majoritariamente sem match oficial no snapshot.
- Tentativa de consulta Tiny live pelo resolver v2 excedeu o tempo da rodada; portanto a compra de sneakers fica bloqueada até validação SKU/tamanho live.
- Muitos produtos têm variações sem SKU ou SKU com pontuação/espaço; risco de falso negativo Tiny.
- External market price não foi coletado nesta v1; não há margem/lead time para compra.

## Próxima decisão sugerida

Fazer: transformar os 3 P1 de conteúdo em previews internos, sem publicação/envio:

1. Mary Jane / ballet sneakers LK.
2. Guia Onitsuka Mexico 66 / SD / Sabot / TGRS.
3. Nike Moon Shoe Jacquemus como fashion sneaker premium.

Bloqueado sem nova aprovação: publicação, campanha, alteração Shopify, compra, contato com fornecedor, promessa de estoque/preço.
