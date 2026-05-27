# LK Growth — Revisão D+7 read-only do preview CRO 2026-05-19

Data: 2026-05-26  
Escopo: Onitsuka Tiger todos os modelos, Onitsuka Tiger Mexico 66, New Balance 204L e PDP Kill Bill.  
Modo: read-only / sem writes externos.

## Fontes verificadas

- Contexto base: `reports/lk-cro-dev-theme-preview-2026-05-19.md`.
- Contexto de priorização: `reports/lk-cro-weekly-preview-top-priorities-2026-05-19.md` e `reports/lk-growth-weekly-revenue-opportunity-2026-05-19.md`.
- PR informado: `https://github.com/lk-snkrs/lk-new-theme/pull/15`; extração pública retornou 404, então o PR não foi usado como fonte primária nesta revisão.
- Receipts de tema lidos no Brain:
  - `theme-production/204l-mobile-reveal-publish-20260525-000532/receipt.json`.
  - `theme-production/all-collection-reveals-publish-20260525-013441/receipt.json`.
  - `theme-dev/204l-mobile-reveal-20260525-000157/receipt.json`.
  - `theme-dev/dev-phase1-onitsuka-samba-guides-20260526-013141/receipt.json`.
- Checks públicos via browser nas páginas live/preview disponíveis.

## Estado por página

| Página | Status D+7 | Evidência | Leitura |
|---|---:|---|---|
| Onitsuka Tiger todos os modelos | Parcialmente promovido para produção em 2026-05-25 | Receipt `all-collection-reveals-publish-20260525-013441`: produção aprovada por Lucas no turno corrente, asset `sections/lk-collection.liquid`, live URL `/collections/onitsuka-tiger-todos-os-modelos`, readback OK. Browser live mostrou bloco editorial `CURADORIA LK · ONITSUKA TIGER`. | O preview original de 19/05 não ficou apenas em dev: houve evolução posterior e publicação de bloco editorial/reveal em produção. |
| Onitsuka Tiger Mexico 66 | Ainda não promovido como produção; existe evolução em dev em 2026-05-26 | Live mostra descrição/trust strip padrão, sem o bloco editorial/reveal do dev. Preview dev atual mostra `CURADORIA LK`, guia `lk-guia-onitsuka-tiger-mexico-66` e FAQ/guia pós-grid; receipt dev `dev-phase1-onitsuka-samba-guides-20260526-013141`, role `unpublished`. | O escopo de 19/05 ficou superado por um preview dev mais completo; produção ainda exige aprovação específica. |
| New Balance 204L | Promovido para produção em 2026-05-25 | Receipt `204l-mobile-reveal-publish-20260525-000532`: produção aprovada por Lucas, aplicado somente reveal 204L, readback OK, live URL `/collections/new-balance-204l`. Browser live mostrou `CURADORIA LK · NEW BALANCE 204L`, reveal de imagens e copy editorial. | Aqui há promoção real; impacto precisa ser medido a partir de 25/05, não 19/05. |
| PDP Kill Bill | Permanece sem evidência de promoção do bloco CRO de 19/05 | Browser live do PDP não mostrou `Curadoria LK` nem marker `data-lk-cro-weekly-preview`; mostrou H1/PDP normal, reviews, trust grid e conteúdo de detalhes. | Bloco PDP do preview parece seguir não publicado em produção. |

## Métricas antes/depois disponíveis

### Baseline usado em 19/05

- Onitsuka todos os modelos: 1.132 sessões; CVR landing 0,09%; 55.903 impressões; CTR 1,14%; venda combinada R$ 1.773.432,62.
- Mexico 66: 748 sessões; CVR landing 0,00%; 31.659 impressões; CTR 1,96%; venda combinada R$ 1.727.732,80.
- New Balance 204L: 454 sessões; CVR landing 0,22%; 43.484 impressões; CTR 0,77%; venda combinada R$ 941.371,37.
- Kill Bill PDP: 146 sessões; CVR landing 0,68%; 11.070 impressões; CTR 0,42%; venda combinada R$ 254.398,94.

### Pós-preview

- Não há, neste pacote, refresh autenticado GA4/GSC/Shopify D+7 registrado de forma comparável para 19–25/05 por página.
- Além disso, a maior parte do que chegou a produção foi publicada apenas em 25/05; portanto, uma janela “D+7 desde 19/05” seria enganosa para Onitsuka todos e 204L.
- Veredito de impacto quantitativo: **não decision-grade ainda**. O que é decision-grade aqui é o status de promoção/risco por receipts e HTML público.

## Impacto observado

- **Impacto visual/produto:** positivo em produção para 204L e Onitsuka todos: páginas agora têm bloco editorial premium, contexto de escolha e reveal visual sem depender de preço/desconto.
- **Impacto comercial mensurado:** inconclusivo; precisa GA4/GSC/Shopify após a data real de publicação em produção.
- **Impacto de SEO/GEO:** potencialmente positivo para collections com bloco citável; Mexico 66 dev atual é mais forte que o preview de 19/05 por incluir guia/FAQ/schema em dev.
- **PDP Kill Bill:** sem impacto observado do preview, porque não há evidência pública de promoção do bloco.

## Riscos

1. **Janela de medição incorreta:** medir 19–25/05 como se tudo estivesse em produção distorce o resultado; 204L/Onitsuka todos só entram como produção em 25/05.
2. **PDP Kill Bill tem linguagem operacional sensível live:** o browser público mostrou `Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp`. Isso é um risco de guardrail de copy pública, separado do preview de 19/05.
3. **Mexico 66 dev atual ainda precisa QA visual final:** bom em SEO/GEO, mas produção não deve ser assumida sem aprovação e rollback.
4. **PR #15 não auditável publicamente:** GitHub retornou 404 sem autenticação; receipts locais e Browser foram usados como fonte.

## Rollback disponível

- 204L produção: re-upload do backup indicado em `theme-production/204l-mobile-reveal-publish-20260525-000532/sections__lk-collection.production.before.liquid` para production theme `155065417950`.
- Blocos de collections publicados em 25/05: re-upload do backup indicado em `theme-production/all-collection-reveals-publish-20260525-013441/sections__lk-collection.production.before.liquid` para production theme `155065417950`.
- Dev Mexico 66/Samba: re-upload do `sections__lk-collection.before.liquid` no receipt `theme-dev/dev-phase1-onitsuka-samba-guides-20260526-013141` para dev theme `155065450718`.
- PDP Kill Bill preview 19/05: rollback original em `reports/lk-cro-dev-theme-preview-2026-05-19.md`, asset `sections/lk-pdp.liquid`, theme dev `155065450718`.

## 18 tópicos canônicos — status

- GA4: baseline usado; refresh D+7 não disponível neste pacote.
- GSC: baseline usado; refresh D+7 não disponível neste pacote.
- GMC: não aplicável ao preview visual; sem write/feed.
- Shopify SEO: sem alteração de title/meta/H1 neste review.
- Shopify CRO/theme: verificado por receipts e browser; 204L/Onitsuka todos promovidos, Mexico 66/PDP Kill Bill não promovidos como produção do preview original.
- GEO/AI Search: Mexico 66 dev atual tem avanço de guia/FAQ; produção pendente.
- PageSpeed/CrUX/CWV: não reavaliado; necessário antes de ampliar blocos/imagens em produção.
- Schema: dev Mexico 66 reporta FAQPage; produção não validada para esse bloco.
- Reviews: PDP Kill Bill tem 9 avaliações/4,78 no browser; sem mudança nesta revisão.
- Paid media: não usado como driver.
- Influencer/social demand: não usado como driver.
- Concorrência/SERP: já considerado em packets posteriores, mas não medido neste D+7.
- Google Business/local: só aparece como trust/local em UI; não é foco.
- Klaviyo/CRM: não usado; nenhum envio.
- Catálogo/product data quality: não auditado; sem feed/write.
- Conteúdo/taxonomia comercial: risco público encontrado no PDP Kill Bill pela frase de prazo/encomenda.
- Mensuração/QA de eventos: pendente para cliques de reveal/lightbox/guia se virar experimento formal.
- Impact review/experimentation: precisa nova janela a partir de 25/05 para o que foi publicado.

## Recomendação

- **Não promover nada novo agora.**
- Rodar impacto real de 204L + Onitsuka todos com janela correta: D+7 a partir de 25/05, comparando GA4 landing, Shopify pedidos/receita por landing/produto e GSC página/query.
- Manter Mexico 66 em dev até QA visual e aprovação explícita de produção.
- Criar packet separado para limpar a linguagem operacional sensível do PDP Kill Bill; não aplicar sem aprovação de Lucas.
