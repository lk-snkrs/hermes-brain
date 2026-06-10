# Handoff — LKGOC SEO/GSC + GEO: Onitsuka Tiger broad + New Balance 204L

Data: 2026-06-09  
Origem: LK Growth — rotina semanal SEO/GSC + GEO Opportunities Review  
Destino obrigatório: **[LK] Otimização de Coleção**  
Status: **handoff local / read-only / sem execução**  
Writes externos: **0**

## Motivo do handoff

As oportunidades abaixo envolvem coleção, copy/FAQ/schema/source/guia e potencial padrão LKGOC. Pela regra LK Growth, Growth entrega evidência, hipótese, métrica e approval surface; **não executa LKGOC**.

Relatório de origem: `areas/lk/sub-areas/growth/reports/weekly/lk-seo-gsc-geo-opportunities-2026-06-09.md`

## 1) Onitsuka Tiger — broad collection

- URL: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`
- Query/tema: `onitsuka tiger`, `tenis onitsuka tiger`, `onitsuka`, `tenis tiger`, `onde comprar onitsuka tiger no brasil`.
- Evidência GSC 2026-05-12 → 2026-06-06:
  - Agregado posição 4–15: **36.261 impressões / 194 cliques / CTR 0,54% / pos. 7,5**.
  - Query principal `onitsuka tiger`: **24.395 impressões / 73 cliques / CTR 0,30% / pos. 8,3**.
- Evidência GA4 orgânico: **879 sessões / 787 usuários / 1.787 pageviews / engagement 77,5%** — maior landing orgânica do recorte.
- Indexação: GSC URL Inspection PASS, Submitted and indexed, canonical self-match, crawled mobile em 2026-06-08.
- HTML/Shopify: title/meta atuais OK tecnicamente; H1 único; FAQPage/CollectionPage/ItemList presentes.
- GEO gap: `agents.md` contém a broad collection; `llms.txt`/`llms-full.txt` não contêm `onitsuka-tiger-todos-os-modelos`, só `onitsuka-tiger-mexico-66`.

### Hipótese

A página tem demanda e engajamento, mas a broad query está em posição média 8 com CTR 0,30%. O ganho provável vem de uma coleção LKGOC/source mais direta para intenção “Onitsuka Tiger original no Brasil”, diferenciando broad Onitsuka vs Mexico 66 e respondendo objeções reais de compra.

### Ação recomendada ao owner LKGOC

Preparar preview LKGOC dev-first com:

1. Bloco citável de 134–167 palavras para `Onitsuka Tiger original no Brasil`.
2. FAQ único e natural: originalidade, diferença de modelos, Mexico 66 vs outros, forma/modelagem com orientação humana sem claims não suportadas.
3. Revisão de linkagem interna entre broad collection, Mexico 66 e source/guide.
4. Proposta de inclusão da broad collection em `llms.txt`/`llms-full.txt`.
5. QA mobile/desktop e schema parity.

### Métrica esperada

- CTR query `onitsuka tiger` > 0,6% inicialmente.
- Posição média voltar para faixa <7.
- Sessões orgânicas da broad collection.
- Separar AI visibility em `text_citation`, `merchant_card` e `not_visible` quando DataForSEO/AI mentions estiver disponível.

### Risco/rollback

- Risco médio: mudança visível em coleção/source/schema.
- Rollback: snapshot de collection description/SEO fields/template/section/FAQ/schema; readback Admin e HTML.
- Produção só com aprovação explícita de Lucas.

## 2) New Balance 204L — refresh/queda

- URL: `https://lksneakers.com.br/collections/new-balance-204l`
- Query/tema: `new balance 204l`, `nb 204l`, `new balance 204 l`, `newbalance 204l`.
- Evidência GSC atual: **11.078 impressões / 59 cliques / CTR 0,53% / pos. 9,3** em queries posição 4–15.
- Queda principal vs período anterior:
  - Antes: **91 cliques / 18.427 impressões / CTR 0,49% / pos. 8,0**.
  - Atual: **18 cliques / 7.318 impressões / CTR 0,25% / pos. 10,3**.
  - Delta: **-73 cliques, -11.109 impressões, piora +2,3 posições**.
- GA4 orgânico: **231 sessões / engagement 71,0%**.
- Indexação: PASS, canonical self-match, crawled mobile em 2026-06-08.
- HTML/Shopify: title/meta atuais tecnicamente bons; H1 único; FAQPage/CollectionPage/ItemList presentes.

### Hipótese

Queda pode ter componente sazonal/SERP de lançamento, mas a CTR 0,25% e posição 10 sugerem refresh de conteúdo/FAQ/source baseado em SERP live e perguntas reais: versão, colorways, material, styling, “onde comprar original”, “forma grande ou pequena?”.

### Ação recomendada ao owner LKGOC

Anexar estes dados ao handoff LKGOC já existente de 2026-06-08 e revalidar:

1. SERP/DataForSEO antes de reescrever.
2. FAQ e bloco citável por dúvidas reais do comprador.
3. Guia/source se a coleção não estiver sendo text-cited por AI Search.
4. D+7/D+14 impact review pós-mudança.

### Métrica esperada

- Recuperar CTR query principal para >0,5%.
- Posição média <8.
- Recuperação de cliques/impressões e sessões orgânicas.

### Risco/rollback

- Risco médio: coleção canônica/padrão 204L; não reinventar layout.
- Rollback: snapshot de collection/source/theme/SEO/FAQ/schema.
- Produção só com aprovação explícita.

## Approval surface para Lucas

Preview wording sugerido:

> Lucas, encontrei duas oportunidades de coleção com demanda real: Onitsuka broad e refresh New Balance 204L. Growth não vai executar LKGOC; posso encaminhar para [LK] Otimização de Coleção preparar o preview dev-first com bloco citável, FAQ/schema e rollback, sem produção?

