# Next P1 Factory — 2026-06-17

Status: read-only / approval packet. Nenhum write externo. values_printed=false.

## Veredito

A próxima página P1 é **Nike Mind 001 Black Chrome**:

`/products/slide-nike-mind-001-black-chrome-preto`

Motivo: maior assimetria entre demanda e captura. GSC mostra volume enorme com CTR praticamente zero, e o cluster Nike Mind tem sinal comercial real.

## Evidência principal

### GSC — janela 2026-05-18 → 2026-06-14

- Query `nike mind 001` → PDP Black Chrome: **4 cliques / 37.388 impressões / CTR 0,01% / posição 9,1**.
- Query `chinelo nike mind 001` → mesmo PDP: **6 cliques / 10.364 impressões / CTR 0,06% / posição 6,0**.
- PDP Pearl Pink também aparece como oportunidade secundária: **11 cliques / 30.802 impressões / CTR 0,04% / posição 9,0**.

### Demanda externa / DataForSEO

- `nike mind 001`: volume Google Brasil **27.100/mês**, maio 2026 com **110.000** buscas no histórico mensal retornado; intenção principal: transactional.
- SERP mobile Brasil para `nike mind 001`: Nike.com.br domina orgânico; LK aparece em Popular Products para Black Chrome, mas não ficou no orgânico top 10 DataForSEO. Há PAA/People Also Search com `Nike mind 001 brasil`, `Nike mind 001 original`, `Nike mind 001 preço`.

### Sinal comercial Shopify já existente no Brain

Fonte: `revenue-informed-priority-clusters-20260613.md`.

- Cluster Nike Mind: **R$ 231.199,30 / 70 unidades / 49 pedidos / 6,3% share** nos últimos 90 dias.
- Produtos Nike Mind aparecem entre top products: `Nike Mind 002 Light Smoke Grey` e `Slide Nike Mind 001 Light Smoke Grey`.

### HTML público atual

- Title atual: `Nike Mind 001 Black Chrome Original | LK Sneakers`.
- Meta atual: `Nike Mind 001 Black Chrome original na curadoria LK Sneakers...` — boa, mas não captura `Brasil`/`onde comprar`.
- H1 atual: `Nike Mind 001 Black Chrome original` — já bom; não mexeria primeiro.
- Schema: Product + FAQPage presentes.

## Ranking da shortlist

1. **Nike Mind 001 Black Chrome PDP** — P1 real. Maior GSC gap, cluster com receita, SERP com intenção transacional e LK já aparece em Popular Products.
2. Nike Mind 001 Pearl Pink PDP — mesmo cluster e mesmo problema; bom para lote 2 depois de validar Black Chrome.
3. Lululemon collection — GSC bom, mas receita 90d menor e intenção `lululemon` é mais navigational; eu deixaria depois.
4. Crocs Lightning McQueen PDP — volume externo enorme, mas baixa relevância comercial LK no histórico e risco de demanda mais mass-market/price-driven.
5. Air Jordan Travis Scott collection — comercialmente forte, mas oportunidade GSC menos concentrada que Nike Mind Black no output do router; merece factory própria depois.

## Proposta P1 — escopo mínimo

Aplicar primeiro no PDP Black Chrome:

- `seo.title`
- `seo.description`
- se permitido no produto sem theme: descrição/FAQ do produto, mantendo Product + FAQPage em paridade.

Não mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout ou mensagens externas.

### Title proposto

`Nike Mind 001 Black Chrome Original no Brasil | LK`

### Meta proposta

`Nike Mind 001 Black Chrome original no Brasil: slide escultural da linha Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`

### Bloco answer-first proposto

O Nike Mind 001 Black Chrome é o slide escultural da linha Nike Mind, reconhecido pelo formato anatômico, visual futurista e acabamento preto com efeito cromado. A busca pelo modelo cresceu porque ele mistura conforto sensorial, design de objeto e presença de moda — não é um chinelo básico, mas uma peça de styling para quem procura um Nike Mind original no Brasil. Na LK, a curadoria prioriza pares autênticos, seleção premium e atendimento humano para orientar modelo, tamanho e proposta de uso. Para quem está comparando versões, o Black Chrome tende a ser uma opção versátil: funciona com alfaiataria casual, denim, looks minimalistas e produções streetwear, mantendo a leitura experimental da linha Mind sem perder usabilidade.

### FAQ proposta

- O Nike Mind 001 Black Chrome é original?
- Onde comprar Nike Mind 001 original no Brasil?
- O Nike Mind 001 tem forma grande ou pequena?
- Qual a diferença entre Nike Mind 001 e Nike Mind 002?
- Como usar o Nike Mind 001 Black Chrome no dia a dia?


Payload exato: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ranking-goals/next-p1-factory-20260617/candidate-nike-mind-black-chrome-packet.json`

## Impacto esperado

- Query `nike mind 001`: CTR de **0,01%** para **0,30–0,50%** em D+14 se mantiver Top 10.
- Projeção simples nessa query: 4 cliques atuais → ~112 a 187 cliques em janela comparável; uplift potencial ~108 a 183 cliques.
- Métrica de revisão: GSC query+URL, page CTR, posição, GA4/Shopify organic landing/PDP/add-to-cart/receita quando disponível.

## Risco

- SEO: baixo/médio; title/meta podem oscilar ranking, mas o CTR atual é tão baixo que há assimetria favorável.
- CRO: baixo se mexer só em SEO fields; médio se alterar descrição/FAQ visível.
- Estoque/disponibilidade: não consultar/não prometer; se for necessário validar disponibilidade, handoff para `lk-stock`.

## Aprovação necessária

Para executar, Lucas precisa aprovar explicitamente o packet. Sugestão:

> Aprovo aplicar no PDP `/products/slide-nike-mind-001-black-chrome-preto` somente `seo.title`, `seo.description` e descrição/FAQ do produto conforme o packet Next P1 Factory 2026-06-17, sem mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout, Klaviyo/WhatsApp ou outros produtos, com backup, QA, rollback e revisão D+7/D+14.
