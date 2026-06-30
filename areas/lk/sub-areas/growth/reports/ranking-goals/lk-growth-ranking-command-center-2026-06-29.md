# LK Growth — Ranking Command Center — 2026-06-29

- **Rotina:** Monday Ranking OS v2
- **Gerado em:** 2026-06-29 08:34 BRT
- **Modo:** read-only / preview-only
- **Writes externos:** 0
- **values_printed:** false
- **Status:** decision-grade para priorização semanal de ranking/GEO com base em GSC + GMC + DataForSEO SERP/volume + QA público + Brain receipts; parcial para impacto comercial final porque GA4/Shopify conversão não foi reprocessado nesta rodada e AI LLM Mentions retornou bloqueio de assinatura.

## Fontes verificadas

- `fact_gsc`: `python3 scripts/lk_search_console_readonly_router_20260511.py` executado em 2026-06-29; property `sc-domain:lksneakers.com.br`; 25.000 linhas query/page; 11.024 páginas agregadas; 40 oportunidades P1; writes 0.
- `fact_gmc`: último Ranking/Product Data Review de 2026-06-25; 21.805 products/statuses; issue prioritário atual `landing_page_error` com 161 produtos / 483 instâncias; `mhlsf_full_missing_valid_link_template=0`.
- `DataForSEO live`: keyword overview/search intent para NB740, Nike Mind, Vomero, Onitsuka, Lululemon, Crocs McQueen, Adidas Tokyo e Puma Speedcat; SERP live para NB740, Nike Mind e Puma Speedcat.
- `AI visibility`: DataForSEO LLM mentions para `lksneakers.com.br` retornou `40204 Access denied`; SERP live trouxe AI Overview para Nike Mind com LK citada no corpo/resposta.
- `Shopify read-only`: broker `shopify_lk` smoke OK via central wrapper (`values_printed=false`); query ampla de coleções não retornou nodes para a string testada, então usei QA público/canonical para validar superfícies.
- `Brain/histórico`: revisados sábado QA/impact review 2026-06-27, GEO/LLM Citation Factory 2026-06-26, GMC 2026-06-25 e receipt SEMrush Ideas 2026-06-27.
- `Honcho`: ferramentas Honcho não estavam expostas neste runtime; usei Brain/receipts como fonte canônica e declarei a limitação.

## Top 5 oportunidades da semana

1. **Nike Mind 001 — CTR/GEO/AI Overview**  
   - GSC: PDP Pearl Pink `12 / 27.550` clicks/impressões, posição `9,0`; PDP Black Chrome `4 / 24.086`, posição `9,2`; guia `18 / 7.213`, posição `9,6`.
   - DataForSEO: `nike mind 001` volume BR `27.100`, pico recente `110.000` em 2026-05, intenção transacional + informacional.
   - SERP live: AI Overview já cita **LK Sneakers** como loja especializada ao lado de Nike/Droper/Mercado Livre/Lowbank; oportunidade é transformar merchant/text citation em CTR e resposta própria mais forte.
   - QA público: collection `/collections/nike-mind-001` HTTP 200/canonical OK, mas `FAQPage=0` no raw check atual.

2. **New Balance 740 — superfície canônica ausente**  
   - DataForSEO: `new balance 740` volume BR `27.100`, tendência anual `+235%`, intenção transacional/informacional.
   - SERP live: AI Overview presente; top orgânicos dominados por New Balance oficial, Artwalk, Netshoes, Ostore e outros sellers; LK não aparece no top 10 orgânico verificado.
   - QA público: `/collections/new-balance-740` finaliza em `/collections/new-balance-todos-os-modelos`, canonical/title da coleção geral e `FAQPage=0`.
   - Decisão: primeiro validar/criar collection/hub canônico com LK Shopify; depois Growth prepara guia/FAQ/schema/llms.

3. **Crocs McQueen — grande impressão, CTR muito baixo**  
   - GSC: PDP Crocs McQueen `199 / 81.735`, CTR `0,24%`, posição `7,1`; queries `crocs mcqueen`, `crocs relampago mcqueen`, `crocs do relâmpago mcqueen` somam forte demanda.
   - DataForSEO: `crocs mcqueen` volume BR `49.500`, intenção informacional pela classificação standalone, mas SERP/queries indicam compra/consulta de modelo.
   - Oportunidade: packet de title/meta + bloco de autenticidade/modelo/personagem + FAQ real-intent sem promessa operacional.

4. **Puma Speedcat — demanda forte + schema inconsistente**  
   - DataForSEO: `puma speedcat` volume BR `18.100`, tendência anual `+83%`, KD `16`, intenção informacional com PAA de origem/autenticidade/preço.
   - SERP live: PUMA oficial domina top orgânico; PAA inclui `Qual a origem do Puma Speedcat?` e `Como saber se o tênis é original da Puma?`.
   - QA público: `/collections/puma-speedcat` HTTP 200/canonical OK, mas `FAQPage=0` no raw check atual; sábado já apontou divergência pós-receipt.

5. **GMC landing_page_error — elegibilidade Merchant/Shopping**  
   - GMC 2026-06-25: `landing_page_error` em 161 produtos / 483 instâncias, +152 produtos vs 18/06.
   - Impacto: risco de perda de Shopping/Surfaces; não é correção cega de HTML, porque 58/80 URLs públicas `.js` testadas estavam OK e 20/80 deram 429.
   - Próximo passo: approval packet de micro-triagem 20–50 offers com snapshot/readback/rollback; sem `fetchNow`, ProductInput, feed ou Shopify write sem aprovação.

## 1–3 prioridades foco da semana

### Prioridade 1 — Nike Mind 001

- **URL/handle:** `https://lksneakers.com.br/collections/nike-mind-001` + PDPs `slide-nike-mind-001-pearl-pink-rosa`, `slide-nike-mind-001-black-chrome-preto`, `slide-nike-mind-001-light-smoke-grey-cinza`.
- **Query alvo:** `nike mind 001`, `chinelo nike mind 001`, `nike mind 001 comprar Brasil`.
- **Hipótese:** consolidar collection/guia/PDP com FAQPage único e resposta answer-first reduz dispersão entre PDPs e aumenta CTR; como o AI Overview já cita LK, o ganho provável é capturar cliques e reforçar `text_citation`.
- **Métrica de sucesso:** CTR de `nike mind 001` nas PDPs/collection; posição média 4–8; cliques orgânicos; permanência em AI Overview/text citation; sessões/conversão orgânica quando GA4/Shopify refresh estiver disponível.
- **Risco/esforço:** médio; risco de duplicar FAQ/schema e repetir termos operacionais proibidos; esforço M.
- **Fonte de verdade:** GSC + DataForSEO SERP/keyword + QA público + Shopify Admin readback antes de qualquer packet.
- **Aprovação necessária:** qualquer alteração em Shopify/theme/SEO fields/FAQ/schema/llms exige packet e aprovação explícita.

### Prioridade 2 — New Balance 740

- **URL/handle:** alvo `/collections/new-balance-740`; status atual redireciona/canonicaliza para `/collections/new-balance-todos-os-modelos`.
- **Query alvo:** `new balance 740`, `new balance 740 original`, `new balance 740 feminino`.
- **Hipótese:** criar/validar superfície canônica específica desbloqueia ranking orgânico e GEO; hoje a demanda cai em páginas genéricas ou não específicas da LK.
- **Métrica de sucesso:** indexação/canonical correto; entrada em `llms.txt`/`llms-full.txt` após live; GSC query/page para NB740; primeiras impressões/cliques; AI citation/merchant card quando disponível.
- **Risco/esforço:** médio/alto porque envolve superfície Shopify; LK Growth só entrega escopo/SEO/GEO, LK Shopify valida/cria collection. Não consultar estoque.
- **Fonte de verdade:** DataForSEO volume/SERP + GSC filtered + public canonical + Shopify readback/handoff.
- **Aprovação necessária:** validação/criação de collection/Shopify e publicação de FAQ/schema/guia exigem aprovação; sem alteração de preço/estoque/desconto/GMC/campanhas.

### Prioridade 3 — Crocs McQueen ou Puma Speedcat, escolher pelo owner do dia

- **Opção A / Crocs McQueen:** foco de CTR em PDP com 81.735 impressões e CTR 0,24%; packet de SERP snippet + FAQ real-intent.
- **Opção B / Puma Speedcat:** foco GEO/schema em collection com demanda 18.100 e FAQPage ausente; packet schema/FAQ após readback técnico da divergência pós-receipt.
- **Métrica de sucesso:** CTR por query/PDP/collection; presença em PAA/AI answers; `FAQPage=1` quando aprovado e visível; ausência de termos operacionais públicos.
- **Aprovação necessária:** preview/packet antes de qualquer write.

## Próximos crons / responsáveis

- **Terça — CRO/PDP Sprint:** preparar packet/preview para Nike Mind 001 e decidir Crocs vs Puma Speedcat; owner LK Growth, execution Shopify somente após aprovação.
- **Quarta — SEO/GEO Demand Capture:** NB740 handoff para LK Shopify + brief de guia/FAQ/schema/llms; owner LK Growth + LK Shopify.
- **Quinta — GMC/Product Data:** retomar `landing_page_error` micro-triagem 20–50 offers; owner LK Growth/Product Data.
- **Sábado — QA/Impact Review:** medir D+7/D+14 dos writes SEMrush/collection/schema e checar propagação pública; owner LK Growth.

## Cobertura dos 18 tópicos

- Cobertos: GSC, GMC, Shopify SEO público/Admin-smoke, GEO/AI Search parcial, schema/FAQPage, concorrência/SERP, catálogo/product data, conteúdo/taxonomia, impact review/histórico.
- Parciais: GA4/Shopify conversão, PageSpeed/CrUX, reviews/Judge.me, paid/influencer, Google Business/local, Klaviyo/CRM, mensuração/eventos.
- Não aplicável nesta rotina: consulta de estoque/Tiny; qualquer disponibilidade operacional deve ir para `lk-stock`.

## Non-actions

- Não consultei estoque/Tiny/disponibilidade.
- Não executei Shopify/theme/GMC/feed/GA4/GSC config/Ads/Klaviyo/WhatsApp/e-mail/preço/estoque/desconto write.
- Não imprimi secrets/tokens/service-account JSON.
- Não usei HTML público como único critério: GSC/DataForSEO/GMC e histórico venceram o raw QA.

## Approval packets recomendados

1. **Nike Mind 001 CTR + FAQ/schema único** — exact preview de title/meta/FAQ/schema/llms, com rollback/readback e QA de duplicidade.
2. **NB740 collection canônica + guia GEO** — handoff LK Shopify para validar/criar collection; depois Growth prepara guia/FAQ/schema/llms em preview.
3. **GMC landing_page_error micro-triagem** — 20–50 offers, snapshot/readback/rollback; sem `fetchNow`/feed/ProductInput/Shopify write sem nova aprovação.

## Caminho

`areas/lk/sub-areas/growth/reports/ranking-goals/lk-growth-ranking-command-center-2026-06-29.md`
