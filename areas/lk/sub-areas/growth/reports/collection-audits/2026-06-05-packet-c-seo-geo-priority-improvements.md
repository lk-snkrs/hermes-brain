# Packet C — SEO/GEO priority improvements para collections LK

Data: 2026-06-05
Status: **pronto para aprovação de produção; nenhum write executado neste packet**.

## Por que não escrevi direto

O pedido “aplicar as melhorias” é uma direção clara, mas as alterações abaixo mexem em **title/meta/SEO visível em produção**. Pelo guardrail LK, preciso deixar o escopo exato registrado antes do write. B1/B2 já foram writes escopados; Packet C é outra camada.

## Dados usados

- Shopify Admin read-only das 10 collections prioritárias.
- DataForSEO Keyword Overview Brasil/pt.
- SERP DataForSEO para:
  - `new balance 9060 original`;
  - `new balance 204l original`;
  - `adidas samba original`.
- Brain/SOP LK Growth e linguagem premium.
- QA público dos packets B1/B2.

## Principais sinais de demanda

- `Labubu`: 1.830.000 buscas/mês, intenção informacional; oportunidade GEO/conteúdo + collection.
- `Adidas Samba`: 246.000 buscas/mês, intenção transacional.
- `New Balance 9060`: 246.000 buscas/mês, intenção transacional.
- `Nike Dunk`: 90.500 buscas/mês, intenção transacional.
- `Nike Air Force 1`: 33.100 buscas/mês, intenção transacional.
- `Air Jordan 1`: 12.100 buscas/mês, intenção transacional.
- `New Balance 204L`: 9.900 buscas/mês, mas com tendência anual explosiva; LK aparece no top 10 para `new balance 204l original`.
- `Onitsuka Tiger Mexico 66`: 6.600 buscas/mês, tendência positiva.

## Oportunidades de SERP/GEO

- NB 9060: SERP tem PAA de autenticidade, preço no Brasil, EUA e mais vendido; copy deve reforçar originalidade, colorways e orientação humana.
- NB 204L: LK já aparece na SERP; prioridade é defender posição com title/meta mais premium e citável.
- Adidas Samba: SERP dominada por Adidas, varejo e PAA de originalidade/preço; LK precisa de meta mais precisa que `Frete grátis/Loja Jardins`.

## Alterações propostas

Arquivo JSON com before/after: `drafts/packet-c-seo-meta-priority-20260605/proposed-seo-meta.json`.

### 1) New Balance 204L

- Title: `New Balance 204L original | LK Sneakers`
- Meta: `New Balance 204L original na curadoria LK: silhueta slim, estética running retrô, colorways desejadas e atendimento humano para orientar tamanho e prazo.`

### 2) Adidas Samba

- Title: `Adidas Samba original | LK Sneakers`
- Meta: `Adidas Samba original na curadoria LK: OG, LT e colorways desejadas, autenticidade verificada e atendimento humano para orientar tamanho e prazo.`

### 3) Onitsuka Tiger Mexico 66

- Title: `Onitsuka Tiger Mexico 66 original | LK Sneakers`
- Meta: `Onitsuka Tiger Mexico 66 original na curadoria LK: herança japonesa, silhueta baixa, cores desejadas e atendimento humano para orientar tamanho e prazo.`

### 4) Collectibles

- Title: `Collectibles originais | Labubu, Pop Mart | LK Sneakers`
- Meta: `Collectibles originais na curadoria LK: Labubu, Pop Mart, Molly e figuras raras, com autenticidade, seleção exclusiva e atendimento humano.`

### 5) Labubu

- Title: `Labubu original Pop Mart | LK Sneakers`
- Meta: `Labubu original Pop Mart na curadoria LK: edições desejadas, Coca-Cola Edition e colecionáveis raros, com seleção exclusiva e atendimento humano.`

### 6) Pop Mart

- Title: `Pop Mart original | Labubu e Molly | LK Sneakers`
- Meta: `Pop Mart original na curadoria LK: Labubu, Molly, BE@RBRICK e toys colecionáveis, com seleção exclusiva, autenticidade e atendimento humano.`

### 7) New Balance 9060

- Sem mudança material proposta no Admin SEO atual; manter como está. O problema restante é render/meta stale público, não Admin.

### 8) Nike Dunk

- Title: `Nike Dunk original | Low, High e SB | LK Sneakers`
- Meta: `Nike Dunk original na curadoria LK: Low, High, SB e colorways desejadas, com autenticidade verificada e atendimento humano para orientar tamanho e prazo.`

### 9) Air Jordan 1

- Title: `Air Jordan 1 original | Low, Mid e High | LK Sneakers`
- Meta: `Air Jordan 1 original na curadoria LK: Low, Mid, High, OG e colorways desejadas, com autenticidade verificada e atendimento humano.`

### 10) Nike Air Force 1

- Sem mudança material necessária; manter como está.

## Risco

- Baixo/médio: alteração de snippets orgânicos pode afetar CTR após recrawl.
- Mitigação: backup, readback, public QA, rollback e revisão D+7.

## Rollback

- Antes do write: salvar `seo.title`, `seo.description`, metafields `global.title_tag` e `global.description_tag` quando existirem.
- Rollback: reaplicar os valores originais via Shopify Admin API.

## Aprovação necessária

Texto sugerido:

> Aprovo Packet C para aplicar exatamente os title/meta propostos em `proposed-seo-meta.json` nas collections listadas, sem alterar descriptionHtml, produto, preço, estoque, theme, campanhas, GMC, Klaviyo ou checkout; com backup, readback, public QA, rollback e revisão D+7.
