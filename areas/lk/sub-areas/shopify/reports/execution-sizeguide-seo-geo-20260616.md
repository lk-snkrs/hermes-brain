# LK Shopify — Execução read-only 2026-06-16

Status: QA visual Size Guide concluído; pacote SEO PDP e auditoria GEO/source pages preparados sem writes externos.

## 1) QA visual mobile — Guia de Tamanhos

Escopo: browser headless mobile 390x844 em Production, clique real no botão `.pi-size-guide`, screenshot antes/depois e inspeção DOM/computed-style.

Resultado: **PASSOU nos 5 PDPs críticos**.

Evidência comum dos 5 testes:
- URL final permaneceu no PDP correto após clique.
- Botão clicado: `.pi-size-guide` / texto `Guia de tamanhos`.
- `Liquid error`: falso.
- Backdrop: `.sg-modal__backdrop` em `rgba(0, 0, 0, 0.7)`.
- Top viewport: `elementFromPoint(20,20)` bateu no backdrop, não no conteúdo do PDP.
- Modal aberto: `.sg-modal.is-open`, `z-index: 9999`, viewport `390x844`.
- Painel: `.sg-modal__panel`, largura 390px, altura 786px; conteúdo com scroll interno quando necessário.

PDPs auditados:
- Yeezy Slide: `/products/yeezy-slide-onyx` — passou.
- Yeezy 350: `/products/yeezy-350-v2-carbon-beluga` — passou.
- Nike Mind 001: `/products/slide-nike-mind-001-black-chrome-preto` — passou.
- Jordan 1 Mid: `/products/air-jordan-1-mid-carbon-fiber` — passou.
- Jordan 1 Low: `/products/tenis-air-jordan-1-low-og-obsidian-unc-azul` — passou.

Observação: a primeira amostra antiga de Jordan Mid Aqua não renderizava o trigger no browser; troquei para um Jordan 1 Mid público com trigger ativo (`air-jordan-1-mid-carbon-fiber`) para validar a regra da família Mid.

Screenshots:
- `assets/sizeguide-mobile-visual-qa-20260616/yeezy-slide-before.png`
- `assets/sizeguide-mobile-visual-qa-20260616/yeezy-slide-after.png`
- `assets/sizeguide-mobile-visual-qa-20260616/yeezy-350-before.png`
- `assets/sizeguide-mobile-visual-qa-20260616/yeezy-350-after.png`
- `assets/sizeguide-mobile-visual-qa-20260616/nike-mind-001-before.png`
- `assets/sizeguide-mobile-visual-qa-20260616/nike-mind-001-after.png`
- `assets/sizeguide-mobile-visual-qa-20260616/jordan-1-mid-before.png`
- `assets/sizeguide-mobile-visual-qa-20260616/jordan-1-mid-after.png`
- `assets/sizeguide-mobile-visual-qa-20260616/jordan-1-low-before.png`
- `assets/sizeguide-mobile-visual-qa-20260616/jordan-1-low-after.png`

Dados brutos: `assets/sizeguide-mobile-visual-qa-20260616/summary.json`

## 2) Pacote SEO PDP — proposta read-only

Escopo: Shopify Admin GraphQL read-only + HTML público. Foram escaneados 300 produtos ativos; 209 têm defeito SEO objetivo detectável, principalmente `seo.title` vazio, `seo.description` vazio/longa ou snippet antigo demais.

Critérios de prioridade:
- P1: SEO title vazio e/ou description vazia.
- P2: title > 60 caracteres ou description > 155 caracteres.
- P3: snippet com copy genérica/antiga ou pública gerada com preço no title.

Proposta de lote inicial — **não aplicado**:

1. `tenis-nike-sb-air-jordan-4-x-retro-sp-navy-branco`
   - Problema: SEO title vazio; description vazia.
   - Title proposto: `Nike SB Air Jordan 4 Retro SP Navy | LK Sneakers` — 48 chars.
   - Meta proposta: `Nike SB Air Jordan 4 Retro SP Navy original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano para comprar com segurança.` — 151 chars.

2. `tenis-nike-air-jordan-1-low-og-chinese-new-year-2026-cinza`
   - Problema: SEO title vazio; description vazia.
   - Title proposto: `Air Jordan 1 Low OG CNY 2026 Cinza | LK Sneakers` — 48 chars.
   - Meta proposta: `Air Jordan 1 Low OG Chinese New Year 2026 original na LK Sneakers. Curadoria premium e atendimento humano para comprar com segurança.` — 133 chars.

3. `tenis-nike-vomero-premium-alabaster-amarelo`
   - Problema: SEO title vazio.
   - Title proposto: `Nike Vomero Premium Alabaster | LK Sneakers` — 43 chars.
   - Meta proposta: `Nike Vomero Premium Alabaster original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.` — 119 chars.

4. `tenis-nike-vomero-premium-realtree-camo-black-preto`
   - Problema: SEO title vazio.
   - Title proposto: `Nike Vomero Premium Realtree Camo | LK Sneakers` — 47 chars.
   - Meta proposta: `Nike Vomero Premium Realtree Camo original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.` — 123 chars.

5. `tenis-new-balance-204l-reflection-bege`
   - Problema: SEO title vazio.
   - Title proposto: `New Balance 204L Reflection Bege | LK Sneakers` — 46 chars.
   - Meta proposta: `New Balance 204L Reflection Bege original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano para comprar com segurança.` — 149 chars.

6. `tenis-new-balance-204l-lone-star-grey-cinza`
   - Problema: SEO title vazio.
   - Title proposto: `New Balance 204L Lone Star Grey | LK Sneakers` — 45 chars.
   - Meta proposta: `New Balance 204L Lone Star Grey original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.` — 121 chars.

7. `a-ma-maniere-x-air-jordan-1-sail-and-burgundy`
   - Problema: title 70 chars; description 170 chars.
   - Title proposto: `A Ma Maniére x Air Jordan 1 Burgundy | LK Sneakers` — 50 chars.
   - Meta proposta: `A Ma Maniére x Air Jordan 1 Sail and Burgundy original na LK Sneakers. Curadoria premium e atendimento humano para comprar com segurança.` — 137 chars.

8. `tenis-air-jordan-1-retro-high-rare-air-sail-cinnabar-bege`
   - Problema: title 62 chars; description 220 chars.
   - Title proposto: `Air Jordan 1 High Rare Air Cinnabar | LK Sneakers` — 49 chars.
   - Meta proposta: `Air Jordan 1 Retro High Rare Air Sail Cinnabar original na LK Sneakers. Curadoria premium e atendimento humano para comprar com segurança.` — 138 chars.

9. `tenis-air-jordan-1-low-multicolor-sashiko-colorido`
   - Problema: title 66 chars; description 161 chars.
   - Title proposto: `Air Jordan 1 Low Multicolor Sashiko | LK Sneakers` — 49 chars.
   - Meta proposta: `Air Jordan 1 Low Multicolor Sashiko original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.` — 125 chars.

10. `tenis-onitsuka-tiger-mexico-66-sabot-natural-cream-bege-1070119339`
   - Problema: SEO title vazio; description 160 chars.
   - Title proposto: `Onitsuka Tiger Mexico 66 Sabot Bege | LK Sneakers` — 49 chars.
   - Meta proposta: `Onitsuka Tiger Mexico 66 Sabot Natural Cream original na LK Sneakers. Curadoria premium e atendimento humano para comprar com segurança.` — 136 chars.

Dados brutos: `assets/seo-pdp-packet-20260616/seo_pdp_candidates.json`

Risco: baixo se aprovado por lote; altera apenas SEO title/description de produtos, mas é Shopify product write.
Rollback: snapshot dos campos atuais por handle antes de aplicar; reversão por Admin GraphQL para valores anteriores.
Bloqueio: precisa aprovação explícita de Lucas para aplicar qualquer Product SEO field.

## 3) Auditoria GEO/source pages — coleções estratégicas

Escopo: HTML público + `/products.json` público por coleção. Sem write.

Coleções auditadas:

1. `nike-mind-001`
   - Status: 200; sem Liquid error.
   - Title: 43 chars; meta: 127 chars.
   - FAQPage JSON-LD: sim.
   - Sinais de trust/citabilidade: fortes.
   - Produto count público: 18.
   - Leitura: saudável; sem ação imediata.

2. `nike-vomero-premium`
   - Status: 200; sem Liquid error.
   - Title: 43 chars; meta: 156 chars.
   - FAQPage JSON-LD: sim.
   - Sinais de trust/citabilidade: fortes.
   - Produto count público: 20.
   - Oportunidade: encurtar meta description em 1-5 caracteres para ficar dentro do range clássico; baixa prioridade.

3. `nike-vomero-5`
   - Status: 200; sem Liquid error.
   - Title: 55 chars; meta: 102 chars.
   - FAQPage JSON-LD: não detectado.
   - Produto count público: 4.
   - Oportunidades: adicionar FAQ visível + FAQPage JSON-LD se houver FAQ real; fortalecer meta para 120-155 chars.
   - Leitura: melhor candidata do bloco GEO.

4. `new-balance-204l`
   - Status: 200; sem Liquid error.
   - Title: 49 chars; meta: 143 chars.
   - FAQPage JSON-LD: sim.
   - Produto count público: 12.
   - Leitura: saudável; manter como referência de padrão.

5. `adidas-samba`
   - Status: 200; sem Liquid error.
   - Title: 45 chars; meta: 112 chars.
   - FAQPage JSON-LD: sim.
   - Produto count público: 87.
   - Leitura: saudável.

6. `yeezy`
   - Status: 200; sem Liquid error.
   - Title: 51 chars; meta: 122 chars.
   - FAQPage JSON-LD: sim.
   - Produto count público: 40.
   - Leitura: saudável.

Dados brutos: `assets/geo-collections-audit-20260616/geo_collections_audit.json`

## Recomendações

Ordem sugerida:

1. Aplicar, se aprovado, o lote SEO PDP de 10 produtos acima.
2. Preparar melhoria específica para `/collections/nike-vomero-5`: FAQ visível + FAQPage JSON-LD + meta description mais completa.
3. Deixar Nike Mind 001, 204L, Samba e Yeezy sem alteração por enquanto; estão saudáveis para o nível atual.

## Bloqueio / próxima decisão

Nada foi alterado externamente.

Para seguir com write, decisão necessária:
- Aprovar aplicação do lote SEO PDP de 10 produtos, somente campos `seo.title` e `seo.description`; ou
- Pedir revisão textual de algum title/meta antes de aplicar; ou
- Aprovar apenas preparar DEV/approval packet para a melhoria da coleção `nike-vomero-5`.
