# LK Growth Ranking Command Center — 2026-06-22

**Modo:** read-only / preview-only.  
**Writes externos:** 0. Sem Shopify/theme/GMC/feed/GA4/GSC/Klaviyo/WhatsApp/Ads/preço/estoque/desconto write.  
**values_printed:** false.  
**Owner:** LK Growth.  
**Rotina:** segunda-feira — Ranking Command Center / LK Growth Ranking OS v2.

## Veredito

Há achado material e decisão para a semana: a prioridade deve sair de um relatório genérico e virar **2 packets de ranking/GEO** — Nike Mind 001 e Nike Vomero Premium — porque ambos combinam demanda transacional alta, CTR baixo em posição 4–20 e problema técnico de FAQ/schema duplicado nas collections públicas. Onitsuka Tiger segue como maior ativo comercial/SEO e deve entrar como terceiro foco de proteção/expansão, não como retrabalho visual.

Status de decisão: **decision-grade para priorização semanal** por combinar GSC atualizado, Shopify/GA4 do decision refresh, GMC recente, DataForSEO keyword overview e QA público. Parcialidades: PageSpeed timeout, CrUX sem record no origin consultado, AI/LLM mentions bloqueado por subscription DataForSEO `40204`, e nenhum dado de estoque foi consultado por regra de handoff ao `lk-stock`.

## Fontes verificadas nesta execução

- `fact_gsc`: `reports/lk-search-console-readonly-router-2026-05-11.{json,md}` regenerado em `2026-06-22T11:33:59Z`, janela `2026-05-23 → 2026-06-19`, property `sc-domain:lksneakers.com.br`, 25.000 query/page rows, 11.767 páginas agregadas, 40 P1, writes 0.
- `fact_shopify/fact_ga4`: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.{json,md}` regenerado em `2026-06-22T11:33:37Z`, pedidos Shopify desde `2026-04-17`, 711 pagos/considerados, 19/19 lookups OK, 14 P1.
- `fact_gmc`: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-product-data-ranking-review-2026-06-18.{json,md}`; maior packet segue `mhlsf_full_missing_valid_link_template` em 11.267 local/LIA offers e `missing_item_attribute_for_product_type` em 2.530 produtos.
- `platform_signal / DataForSEO`: Keyword overview Brasil/pt para 6 termos; AI mentions para `lksneakers.com.br` em ChatGPT retornou `40204 Access denied`, então AI citation tracking ficou indisponível nesta passada.
- `public_html_diagnostic`: QA público leve de 4 collections foco por HTTP/raw HTML: todas HTTP 200 e H1 único; `nike-mind-001` e `nike-vomero-premium` têm 2 blocos `FAQPage` JSON-LD cada.
- `connector_probe`: GA4 canônico OK; outra property GA4 403; PageSpeed timeout; CrUX 404/sem record; api_key_present=true; secrets não impressos.

## Top 5 oportunidades da semana

| Rank | Oportunidade | Evidência | Hipótese | Métrica-alvo | Próximo passo |
|---:|---|---|---|---|---|
| 1 | **Nike Mind 001 — CTR + schema único** | GSC: query `nike mind 001` nos PDPs Black Chrome e Pearl Pink soma 68.133 impressões com CTR 0,01–0,04% e posição ~9; DataForSEO: 27.100 buscas/mês, maio 110.000, intenção transacional; Shopify refresh: collection Nike Mind 001 R$ 460.958,56 combinado | CTR está subcapturado e a collection tem FAQPage duplicado; consolidar snippet/FAQ/schema deve melhorar Google e LLM parsing | CTR query `nike mind 001` ≥0,5%; posição Top 10 mantida/melhorada; FAQPage único; AI visibility quando API liberar | Terça: approval packet de title/meta + schema/FAQ único; sem write até aprovação |
| 2 | **Nike Vomero Premium — demanda comercial + duplicidade FAQPage** | GSC: `vomero premium` 9.602 impressões no PDP White Bright Crimson, CTR 0,08%, posição 8,7; DataForSEO: 27.100 buscas/mês, intenção transacional; web QA: collection HTTP 200, H1 único, 2 FAQPage | Frente de alto valor com demanda transacional e possível ambiguidade schema; precisa packet de collection/guia antes de mexer | CTR para `vomero premium` ≥0,5%; collection sem FAQPage duplicado; sessões/conversão da landing; AI citations/mentions quando possível | Quarta: packet Vomero collection/guia/FAQ, rollback e QA público |
| 3 | **Onitsuka Tiger todos os modelos / Mexico 66** | GSC: collection todos modelos 112 cliques/30.932 impressões para `onitsuka tiger`, CTR 0,36%, posição 7,9; decision refresh: R$ 2.028.631,62 combinado; DataForSEO: 33.100 buscas/mês, intenção transacional | LK já tem força comercial, mas ainda pode capturar mais intenção `original / onde comprar / Mexico 66` com snippet e source-page/citability | CTR collection todos modelos ≥1,5%; posição média ~6–7; text citation para compra original, não só merchant/product card | Sexta: source-page/GEO brief e revisão FAQ real-intent |
| 4 | **New Balance 204L — proteger scaffold canônico** | Decision refresh: R$ 1.044.971,00 combinado; DataForSEO: 12.100 buscas/mês e crescimento anual forte; QA público: H1 único, 1 FAQPage | Manter 204L como benchmark LKGOC e usar só para impact/QA/paridade; não precisa nova variação agora | Manter Top 3–5 em termos core; preservar FAQ/schema limpo; usar como padrão de comparação | Sábado: impact/QA e paridade para novos packets |
| 5 | **Crocs Relâmpago McQueen / Lululemon — backlog P2 comercial** | Crocs: DataForSEO 33.100 buscas/mês e GSC 17.253 impressões/CTR 0,19%; Lululemon: DataForSEO 40.500 buscas/mês e GSC posição 4,8, mas intenção mais navegacional | Há demanda, mas menor alinhamento premium/receita que Mind/Vomero/Onitsuka; manter em backlog até os P1 virarem packets | Reavaliar CTR e conversão após P1; priorizar se houver sinal comercial/paid/influencer | Backlog: não executar esta semana sem novo sinal |

## 1–3 prioridades da semana

### Prioridade 1 — Nike Mind 001

- **URL/handle:** `/collections/nike-mind-001`; PDPs `/products/slide-nike-mind-001-black-chrome-preto` e `/products/slide-nike-mind-001-pearl-pink-rosa`.
- **Query alvo:** `nike mind 001`, `chinelo nike mind 001`, `nike mind 001 original`, `nike mind 001 brasil`.
- **Hipótese:** a demanda está alta e transacional, mas o snippet/PDP ainda captura poucos cliques; schema duplicado na collection pode reduzir clareza para Google/LLMs.
- **Métrica de sucesso:** CTR GSC de queries Nike Mind 001 ≥0,5%; cliques orgânicos semanais; FAQPage JSON-LD único; AI visibility classificada como `text_citation`, `merchant_card` ou `not_visible` quando a API liberar.
- **Risco:** médio/baixo; copy deve defender autenticidade/curadoria/atendimento humano, sem promessa operacional de disponibilidade/prazo.
- **Esforço:** médio.
- **Fonte de verdade:** GSC + Shopify/GA4 refresh + DataForSEO keyword overview + QA público.
- **Aprovação necessária:** Shopify SEO/content/schema/theme write exige aprovação explícita atual. Preparar packet é livre.

### Prioridade 2 — Nike Vomero Premium

- **URL/handle:** `/collections/nike-vomero-premium`; provável guia/source-page `nike-vomero-premium-guia` se o packet confirmar.
- **Query alvo:** `nike vomero premium`, `vomero premium`, `nike vomero premium original`.
- **Hipótese:** demanda transacional alta e collection pública com FAQPage duplicado; um packet de schema único + bloco demand-led pode capturar CTR e reduzir ambiguidade GEO.
- **Métrica de sucesso:** CTR GSC ≥0,5% nos termos foco; posição Top 10; 1 FAQPage; sessões/conversão por landing; futura AI mention/citation.
- **Risco:** médio; deve diferenciar versões/uso/material sem virar promessa de performance médica/corrida nem disponibilidade.
- **Esforço:** médio.
- **Fonte de verdade:** GSC + Shopify/GA4 + DataForSEO + public QA.
- **Aprovação necessária:** sim para qualquer Shopify/source-page/schema/theme write.

### Prioridade 3 — Onitsuka Tiger / Mexico 66 original

- **URL/handle:** `/collections/onitsuka-tiger-todos-os-modelos`, `/collections/onitsuka-tiger-mexico-66`, PDP Kill Bill.
- **Query alvo:** `onitsuka tiger`, `onitsuka tiger original`, `onitsuka tiger mexico 66`, `onde comprar onitsuka original`.
- **Hipótese:** maior ativo comercial e orgânico da semana; foco deve ser melhorar CTR e autoridade textual em intenção de compra segura, não reescrever layout aprovado.
- **Métrica de sucesso:** CTR collection todos modelos ≥1,5%; posição média ~6–7; aumento de cliques orgânicos; classificação AI text citation quando disponível.
- **Risco:** médio; SERP tem muitos sellers/brand assets, então LK deve competir por curadoria/autenticidade e guia de escolha.
- **Esforço:** médio/alto.
- **Fonte de verdade:** GSC + Shopify/GA4 refresh + DataForSEO + public QA.
- **Aprovação necessária:** sim para source-page/Shopify/schema writes.

## GMC/Product Data que impacta ranking/Shopping

- **Packet P1 GMC mantido:** `mhlsf_full_missing_valid_link_template` em 11.267 local/LIA offers. Tratar como contrato Local Inventory/LIA `link_template`/store_code, não como preço/404/PDP.
- **Packet P2 GMC:** `missing_item_attribute_for_product_type` em 2.530 produtos; usar só em micro-piloto priorizado por handles foco, não em massa sem cruzamento comercial.
- **Ação desta semana:** quinta-feira deve cruzar GMC residuals com Mind/Vomero/Onitsuka/204L antes de qualquer packet de write.

## Próximos crons/donos

- **Terça — Google SEO Opportunity Factory:** gerar packet exato para Nike Mind 001: title/meta, FAQ/schema único, internal links e QA esperado.
- **Quarta — Collection/PDP Optimization Factory:** gerar packet Nike Vomero Premium: collection/guia, FAQ real-intent, schema único e rollback.
- **Quinta — Merchant/Product Data Ranking Review:** cruzar GMC `link_template` e atributos faltantes com os handles foco; micro-piloto approval-only.
- **Sexta — GEO/LLM Citation Factory:** Onitsuka original/Mexico 66 source-page brief e AI-citable blocks; repetir AI visibility se DataForSEO liberar API.
- **Sábado — QA + Impact Review:** revalidar FAQPage duplicado, PageSpeed retry, CrUX/origin fallback e D+7 dos packets recentes.

## Approval packet recomendado para Lucas

**Recomendação LK Growth:** preparar primeiro o packet **Nike Mind 001 — CTR + FAQ/schema único** e, em seguida, **Nike Vomero Premium — collection/guia + FAQ/schema único**.

Approval wording futuro quando o preview exato existir:

> `Aprovo aplicar somente os campos/textos/schema listados no packet <nome>, nos handles exatos, com rollback e sem alterar preço, estoque, desconto, campanhas, feed/GMC, Klaviyo/WhatsApp ou theme production fora do escopo.`

## Limitações e não-ações

- Não consultei estoque/Tiny nem usei disponibilidade como critério; qualquer validação operacional é do `lk-stock`.
- Não executei Shopify, theme, GMC/feed, ProductInput/dataSource/fetchNow, GA4/GSC config, Ads, Klaviyo, WhatsApp, preço, estoque ou desconto.
- PageSpeed timeout e CrUX 404 deixam CWV parcial nesta passada.
- DataForSEO AI/LLM mentions retornou `40204 Access denied`; keyword overview funcionou.
- Caminho deste relatório: `areas/lk/sub-areas/growth/reports/ranking-goals/ranking-command-center-20260622.md`.
