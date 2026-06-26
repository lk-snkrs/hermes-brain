# LK OS — CRO Baseline 0,13% → 0,20% Read-only

Gerado em: `2026-05-15T09:58:00Z`
Status: `baseline_read_only_preview`
Modo: public live check + artefatos GA4/GSC existentes; sem Shopify/theme/write.

## Veredito

A meta 0,13% → 0,20% é pequena em pontos absolutos, mas exige **+53,8% de lift relativo**. Em escala, isso equivale a aproximadamente **+70 pedidos a cada 100.000 sessões**.

O baseline P1 mais acionável está nas páginas já priorizadas pelo router GA4+GSC de baixa conversão: 8 páginas somam `3.535` sessões e só `4` compras atribuídas na janela auditada, CVR agregado `0,113%`, abaixo da meta.

## Fontes

- `fact_ga4`/`fact_gsc`: `reports/lk-p1-seo-cro-approval-packets-2026-05-11.json` e router low-conversion 2026-05-11.
- `public_live_snapshot`: HTML público lido hoje em modo read-only para confirmar que as URLs respondem e capturar sinais básicos de confiança/conversão.
- `derived_reconciliation`: cálculo Hermes de gap para meta 0,20%.

## Métrica alvo

- Baseline citado: `0.13%`
- Meta: `0.2%`
- Lift relativo necessário: `53.8%`
- Pedidos incrementais por 100.000 sessões: `70`

## Fila P1 de CRO sem write

### 1. P1 · collection · Nike Travis Scott

- URL: https://lksneakers.com.br/collections/air-jordan-travis-scott
- GA4: `254` sessões, `0` compras, CVR `0.0%`, receita `R$ 0.0`
- GSC: `28235` impressões, CTR `0.8%`, posição `6.5`, query `nike travis scott`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: collection com CVR landing abaixo da meta.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 2. P1 · collection · New Balance 204L

- URL: https://lksneakers.com.br/collections/new-balance-204l
- GA4: `545` sessões, `1` compras, CVR `0.18%`, receita `R$ 2644.96`
- GSC: `50536` impressões, CTR `0.85%`, posição `7.4`, query `new balance 204l`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: collection com CVR landing abaixo da meta.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 3. P1 · pdp · Crocs Relampago Mcqueen

- URL: https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho
- GA4: `188` sessões, `0` compras, CVR `0.0%`, receita `R$ 0.0`
- GSC: `35931` impressões, CTR `0.31%`, posição `7.5`, query `crocs relampago mcqueen`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: PDP com tráfego e zero compra atribuída.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 4. P1 · collection · Onitsuka Tiger

- URL: https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos
- GA4: `1067` sessões, `1` compras, CVR `0.09%`, receita `R$ 2499.99`
- GSC: `54015` impressões, CTR `1.16%`, posição `6.5`, query `onitsuka tiger`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: collection com CVR landing abaixo da meta.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 5. P1 · collection · Onitsuka Tiger Mexico 66

- URL: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66
- GA4: `698` sessões, `2` compras, CVR `0.29%`, receita `R$ 4899.98`
- GSC: `29581` impressões, CTR `1.93%`, posição `4.1`, query `onitsuka tiger mexico 66`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: manter como otimização incremental.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 6. P1 · pdp · Slide Nike Mind 001 Black Chrome Preto

- URL: https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto
- GA4: `108` sessões, `0` compras, CVR `0.0%`, receita `R$ 0.0`
- GSC: `7664` impressões, CTR `0.63%`, posição `7.7`, query `None`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: PDP com tráfego e zero compra atribuída.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 7. P1 · pdp · Bone 5 Panel Aime Leon Dore Unisphere Branco

- URL: https://lksneakers.com.br/products/bone-5-panel-aime-leon-dore-unisphere-branco
- GA4: `476` sessões, `0` compras, CVR `0.0%`, receita `R$ 0.0`
- GSC: `None` impressões, CTR `None%`, posição `None`, query `None`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: PDP com tráfego e zero compra atribuída.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

### 8. P1 · collection · Adidas Samba Jane

- URL: https://lksneakers.com.br/collections/adidas-samba-jane
- GA4: `199` sessões, `0` compras, CVR `0.0%`, receita `R$ 0.0`
- GSC: `19402` impressões, CTR `1.12%`, posição `6.9`, query `adidas samba jane`
- Public live: status `200`; H1 `n/a`
- Sinais públicos: autenticidade=`True`, loja física=`True`, 10x=`True`, frete=`False`, reviews=`True`
- Hipótese de gargalo: collection com CVR landing abaixo da meta.
- Preview recomendado sem write: bloco acima da dobra com confiança + disponibilidade/curadoria + CTA/grade focada; manter SEO title/meta já tratado separado.

## Backlog de testes/preview

### Experimento A — Trust strip acima da dobra

- Escopo: bloco visual/textual curto em PDP/collection com `100% original`, `loja física Jardins`, `atendimento humano`, `até 10x`, `frete/retirada quando aplicável`.
- Risco: médio se alterar layout/tema; baixo se for só copy preview.
- Status: `preview_only_needs_design_approval`.

### Experimento B — Collections com ordenação/grade comercial

- Escopo: nas collections P1, priorizar cards com maior disponibilidade/margem/sinal de demanda acima da dobra.
- Dependência: Tiny snapshot completo para não promover tamanho indisponível como se fosse operacionalmente pronto.
- Status: `blocked_by_partial_tiny_stock_for_operational_sorting`.

### Experimento C — PDP zero-compra

- Escopo: PDPs com tráfego e 0 compra recebem checklist visual: foto principal, preço/parcelamento, tamanhos visíveis, CTA, prova de originalidade e links de ajuda/WhatsApp.
- Status: `manual_ui_preview_needed_before_theme_write`.

## Decisão operacional

A meta 0,20% não deve começar por mudança de tema. O primeiro passo seguro é transformar esta fila em **pacote visual de preview** para 3 páginas P1: uma collection forte, uma collection com alto tráfego e um PDP com zero compra. Só depois pedir aprovação para qualquer H1/body/layout/theme write.

## O que não foi feito

- Nenhum Shopify write.
- Nenhum theme/Liquid/app write.
- Nenhum Merchant/GMC write.
- Nenhum preço/estoque/campanha/Klaviyo/WhatsApp.
- Nenhum cron novo.

## Próximo passo recomendado

Criar `CRO Preview Pack v0` para 3 páginas: New Balance 204L, Onitsuka Tiger geral e Crocs Lightning McQueen. Entrega: texto/estrutura visual inline e checklist de aprovação; ainda sem aplicar nada no site.
