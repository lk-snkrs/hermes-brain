# LK Growth — D+7 read-only — SEO GSC P1 + hotfix Samba Jane (2026-06-13)

## Veredito executivo

- **Veredito:** tecnicamente saudável. O hotfix não deixou `Liquid error`; 11/11 URLs públicas retornam 200, canonical correto e meta description presente.
- **Cache/stale:** o cache/stale reportado no receipt de 2026-06-06 está majoritariamente resolvido. A Home hoje bate com o asset atual do tema (`LK Sneakers Jardins | Curadoria de Sneakers Originais`), não com o HTML público antigo capturado no primeiro QA.
- **GSC:** sinais mistos em 6 dias pós-rollout vs 7 dias baseline. Melhoras claras de CTR/posição em Crocs McQueen e Adidas Samba Jane; Lululemon melhora CTR leve; Onitsuka e NB 204L caem em cliques/impressões no curto prazo; Nike Mind perdeu demanda pós-pico.
- **Comercial:** GA4 landing organic e Shopify landing-site estão disponíveis. Onitsuka sustentou compra orgânica/landing e aumentou Shopify landing orders; Crocs McQueen aparece como maior ganho novo. Ainda é cedo para causalidade forte porque a janela é curta e há sazonalidade/demanda de produto.
- **Ação recomendada:** não fazer rollback. Monitorar por mais 7 dias; priorizar investigação/copy adicional apenas para NB 204L e Nike Mind se a queda persistir no D+14.

## Escopo e janelas

- Rollout: 2026-06-06.
- Baseline usada: 2026-05-30 a 2026-06-05.
- Pós-mudança usada: 2026-06-07 a 2026-06-12.
- Writes externos executados nesta revisão: **0**. Apenas leitura pública, GSC, GA4 e Shopify Admin/orders read-only.
- values_printed=false; nenhum secret/token foi impresso.

## Fonte e cobertura

- Public fetch/head: 11/11 OK.
- GSC Search Analytics por URL: 11/11 OK.
- GA4 landing organic: 11/11 OK, com sessões, usuários, ATC, checkouts, ecommerce purchases e purchase revenue por landing page.
- Shopify orders por `landing_site`: OK; baseline 86 pedidos escaneados, pós 97 pedidos escaneados.
- Shopify theme read-only: OK, theme main `155065417950`, product metafield title logic presente: True. 
- Mandatory fallback helper `lk_growth_impact_review.py`: executado via Doppler para NB 204L, Onitsuka, Lululemon, Yeezy, Adidas Samba Jane e Guia Nike Mind; artefatos em `mandatory-helper/`.

## QA público — title/meta/canonical/Liquid

| URL | Status | Title atual | Canonical | Liquid error | Observação |
|---|---:|---|---|---:|---|
| Home | 200 | LK Sneakers Jardins | Curadoria de Sneakers Originais | https://lksneakers.com.br/ | False | Home agora bate com asset atual; difere do primeiro QA stale de 06-06. |
| NB 204L | 200 | New Balance 204L Original | Curadoria LK Sneakers | https://lksneakers.com.br/collections/new-balance-204l | False | OK |
| Onitsuka | 200 | Onitsuka Tiger Original | Mexico 66 e Curadoria LK | https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos | False | OK |
| Lululemon | 200 | Lululemon Original | Curadoria Athleisure LK | https://lksneakers.com.br/collections/lululemon | False | OK |
| Nike Mind Black | 200 | Nike Mind 001 Black Chrome Original | LK Sneakers | https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto | False | OK |
| Nike Mind Pink | 200 | Nike Mind 001 Pearl Pink Original | LK Sneakers | https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa | False | OK |
| Crocs McQueen | 200 | Crocs Relâmpago McQueen Original | LK Sneakers | https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho | False | OK |
| Yeezy | 200 | Yeezy Original | Slides, Foam Runner e 350 V2 na LK | https://lksneakers.com.br/collections/yeezy | False | OK |
| Nike Vomero Premium | 200 | Nike Vomero Premium Original | LK Sneakers | https://lksneakers.com.br/products/tenis-nike-vomero-premium-white-bright-crimson-branco | False | OK |
| Guia Nike Mind | 200 | Nike Mind 001 e 002: Guia LK de Escolha | https://lksneakers.com.br/pages/guia-nike-mind-001-002 | False | OK |
| Adidas Samba Jane | 200 | Adidas Samba Jane Original na LK Sneakers | https://lksneakers.com.br/collections/adidas-samba-jane | False | OK |

## GSC — query/page agregado

| Página | Cliques base → pós | Impressões base → pós | CTR base → pós | Posição base → pós | Leitura |
|---|---:|---:|---:|---:|---|
| Home | 69 → 47 (-22) | 7522 → 4856 (-2666) | 0.92% → 0.97% (+0.05 pp) | 7.94 → 8.00 (+0.06) | CTR melhor, volume menor |
| NB 204L | 23 → 14 (-9) | 2792 → 2075 (-717) | 0.82% → 0.67% (-0.15 pp) | 8.42 → 7.86 (-0.56) | atenção |
| Onitsuka | 151 → 120 (-31) | 11808 → 10421 (-1387) | 1.28% → 1.15% (-0.13 pp) | 6.65 → 7.40 (+0.75) | atenção |
| Lululemon | 172 → 144 (-28) | 7824 → 5739 (-2085) | 2.20% → 2.51% (+0.31 pp) | 4.47 → 4.42 (-0.04) | CTR melhor, volume menor |
| Nike Mind Black | 39 → 12 (-27) | 33022 → 5850 (-27172) | 0.12% → 0.21% (+0.09 pp) | 7.94 → 7.56 (-0.38) | CTR melhor, volume menor |
| Nike Mind Pink | 13 → 1 (-12) | 24853 → 2677 (-22176) | 0.05% → 0.04% (-0.01 pp) | 9.01 → 9.74 (+0.73) | atenção |
| Crocs McQueen | 22 → 53 (+31) | 16240 → 14609 (-1631) | 0.14% → 0.36% (+0.23 pp) | 7.85 → 7.13 (-0.72) | positivo |
| Yeezy | 18 → 14 (-4) | 5521 → 4326 (-1195) | 0.33% → 0.32% (-0.00 pp) | 9.00 → 8.54 (-0.46) | atenção |
| Nike Vomero Premium | 0 → 1 (+1) | 247 → 111 (-136) | 0.00% → 0.90% (+0.90 pp) | 4.84 → 5.30 (+0.46) | positivo |
| Guia Nike Mind | 0 → 0 (+0) | 571 → 150 (-421) | 0.00% → 0.00% (+0.00 pp) | 9.61 → 9.99 (+0.39) | neutro/misto |
| Adidas Samba Jane | 35 → 40 (+5) | 3668 → 3087 (-581) | 0.95% → 1.30% (+0.34 pp) | 6.41 → 5.68 (-0.73) | positivo |

## GA4 landing organic + Shopify landing orders

| Página | GA4 sessões org. base → pós | ATC base → pós | Checkout base → pós | Purchases/Revenue GA4 base → pós | Shopify orders/revenue landing base → pós |
|---|---:|---:|---:|---:|---:|
| Home | 166 → 150 (-16) | 44 → 11 | 2 → 1 | 0/R$ 0,00 → 0/R$ 0,00 | 19/R$ 56.861,00 → 16/R$ 40.035,99 |
| NB 204L | 44 → 30 (-14) | 2 → 2 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 1/R$ 3.999,99 → 0/R$ 0,00 |
| Onitsuka | 234 → 207 (-27) | 10 → 12 | 2 → 5 | 1/R$ 2.399,99 → 1/R$ 2.160,00 | 1/R$ 2.399,99 → 2/R$ 4.559,99 |
| Lululemon | 203 → 187 (-16) | 7 → 3 | 1 → 1 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Nike Mind Black | 107 → 45 (-62) | 3 → 0 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Nike Mind Pink | 19 → 4 (-15) | 0 → 0 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Crocs McQueen | 52 → 70 (+18) | 0 → 2 | 0 → 2 | 0/R$ 0,00 → 1/R$ 1.571,06 | 0/R$ 0,00 → 0/R$ 0,00 |
| Yeezy | 19 → 14 (-5) | 0 → 0 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Nike Vomero Premium | 6 → 2 (-4) | 0 → 0 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Guia Nike Mind | 2 → 3 (+1) | 0 → 0 | 0 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |
| Adidas Samba Jane | 41 → 43 (+2) | 2 → 2 | 1 → 0 | 0/R$ 0,00 → 0/R$ 0,00 | 0/R$ 0,00 → 0/R$ 0,00 |

## Regressões e riscos

- **Sem regressão técnica crítica:** status 200 em todas as URLs, canonical correto, sem `Liquid error`.
- **Home:** não é regressão; é resolução do stale/cache. O title/meta atual público coincide com o asset atual do tema, mas difere do `public-head-qa.json` capturado imediatamente após o rollout.
- **NB 204L:** GSC cliques 23→14 e CTR 0,82%→0,67%; GA4 organic sessions 44→30; Shopify landing order 1→0. Não aciona rollback sozinho, mas é o principal ponto de rechecagem D+14.
- **Nike Mind Black/Pink:** queda forte de demanda/impressões pós-pico; guia ainda tem baixa tração orgânica. Separar efeito de tendência do modelo vs SEO field.
- **Onitsuka:** GSC caiu em cliques/CTR/posição, mas GA4/Shopify comercial melhorou em pedidos/revenue; não tratar como perda comercial.
- **Adidas Samba Jane:** hotfix validado: sem Liquid error; CTR e posição GSC melhoraram; GA4 orgânico estável/levemente positivo; sem pedido landing no período.

## Recomendações read-only / próximas decisões

1. **Manter pacote em produção** — não há evidência técnica para rollback.
2. **D+14 obrigatório** em 2026-06-20: repetir GSC/GA4/Shopify com janela maior, especialmente NB 204L, Nike Mind e Onitsuka.
3. **NB 204L:** se D+14 confirmar queda, preparar packet de melhoria de conteúdo/GEO/FAQ ou ajuste de snippet; não executar write sem aprovação.
4. **Nike Mind:** reforçar distribuição/internal links do Guia Nike Mind e comparar contra sazonalidade/SERP antes de mexer no title.
5. **Samba Jane:** manter apenas monitoramento; hotfix resolveu o risco de Liquid error.

## Artefatos

- Relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/d7-readonly-review.md`
- Evidência pública/GSC: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/public-gsc-evidence.json`
- Evidência GA4 landing organic: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/ga4-organic-landing-evidence.json`
- Evidência Shopify landing orders: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/shopify-orders-landing-evidence.json`
- Evidência Shopify theme read-only: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/shopify-theme-current-readonly.json`
- Mandatory helper: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/mandatory-helper`

Reminder OS loop needed: yes
Reminder OS owner: LK Growth
Reminder OS next action: rodar D+14 read-only em 2026-06-20 para o mesmo pacote, sem writes.
Reminder OS review trigger: 2026-06-20 ou queda adicional material em GSC/GA4 antes disso.
Reminder OS evidence: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/seo-gsc-p1-hotfix-samba-d7-20260613/d7-readonly-review.md` e JSONs de evidência no mesmo diretório.
