# LK Growth Ranking OS v2 — Collection/PDP Optimization Factory — 2026-06-17

Status: read-only / approval packet.  
Rotina: quarta-feira — melhorar uma página comercial por semana para SEO + CRO + GEO.  
Página foco: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`.

## 1. Veredito

Escolha da semana: **Collection Onitsuka Tiger — todos os modelos**.

Motivo: é a página com maior intersecção de potencial comercial + demanda orgânica + gargalo de CTR/conversão. A página já tem base SEO/GEO boa, schema e FAQ, mas ainda pode capturar mais demanda de `onitsuka tiger`, `tênis onitsuka tiger` e intenção de escolha entre Mexico 66 / Sabot / SD / modelos derivados com uma correção LKGOC/SEO-CRO-GEO mais precisa.

Decision-grade: **ready for preview / não executar produção**. Há evidência Shopify + GSC + HTML/schema; GA4 está OK no conector, mas este packet usa a última fila de decisão e não reabre escrita nem impacto pós-mudança.

Writes: **0**. Secrets: `values_printed=false`.

## 2. Fontes e evidência usada

- Connector probe Growth 2026-06-17: Google token OK; GA4 `GA4_LK_PROPERTY_ID` OK; PageSpeed timeout; CrUX sem record para origem consultada.
- GSC read-only router 2026-06-17, janela `2026-05-18` a `2026-06-14`:
  - Página `/collections/onitsuka-tiger-todos-os-modelos`: **861 cliques / 66.479 impressões / CTR 1,30% / posição 6,8**.
  - Query `onitsuka tiger`: **102 cliques / 29.510 impressões / CTR 0,35% / posição 8,2**.
  - Query `tenis onitsuka tiger`: **55 cliques / 4.078 impressões / CTR 1,35% / posição 4,2**.
- Decision-grade refresh read-only:
  - prioridade P1, score pós-refresh **100**;
  - vendas recentes Shopify na coleção: **194 unidades / R$ 488.898,06**;
  - vendas combinadas local + recentes: **836 unidades / R$ 2.013.531,68**;
  - membership Shopify: `exact_collection_membership_first_120`.
- Shopify read-only / storefront HTML:
  - H1: `Onitsuka Tiger`;
  - SEO title atual: `Onitsuka Tiger Original | Mexico 66 e Curadoria LK` — 50 caracteres;
  - meta atual: `Onitsuka Tiger original na LK Sneakers: Mexico 66 e modelos selecionados com curadoria premium, autenticidade e atendimento humano.` — 131 caracteres;
  - schema detectado: `Organization`, `ShoeStore`, `ClothingStore`, `BreadcrumbList`, `CollectionPage`, `FAQPage`;
  - `/llms.txt`: HTTP 200, menciona Onitsuka.

## 3. Diagnóstico SEO / CRO / GEO

### SEO

- Ponto forte: title/meta já estão dentro de tamanho seguro e a página rankeia com volume relevante.
- Gargalo: CTR muito baixo para a query principal (`onitsuka tiger`, 0,35% na posição 8,2), sugerindo que o snippet ainda pode ser mais específico em **Mexico 66 + modelos + original no Brasil + curadoria LK**.
- Risco atual de copy: trecho legado no `descriptionHtml` tem frases com sensação operacional ou redundante (`numerações completas`, `curadoria verificada`) e pode ser mais premium/preciso sem prometer disponibilidade.

### CRO

- Página tem produto + guia/FAQ, mas a proposta de decisão pode ficar mais clara:
  - separar escolha por silhueta: Mexico 66, Mexico 66 SD, Sabot, Delegation/Serrano;
  - reforçar autenticidade e atendimento humano sem repetir texto genérico;
  - linkar internamente para subcoleções Onitsuka relevantes.
- Métrica de sucesso CRO: PDP views a partir da collection, add-to-cart, conversão de landing page e receita atribuída/assistida.

### GEO / AI Search

- Ponto forte: `/llms.txt` presente e `FAQPage` existe.
- Gap: FAQ atual é boa, mas pode ficar mais intent-led e menos genérica; precisa cobrir comparação entre versões e escolha por uso/material/proporção.
- Métrica de sucesso GEO: ganho de CTR orgânico em queries Onitsuka, presença como `text_citation`/resposta citável para “onde comprar Onitsuka Tiger original no Brasil” e “qual Onitsuka Tiger escolher”.

## 4. Proposta concreta de approval packet

### 4.1 SEO fields — preview

**SEO title atual**  
`Onitsuka Tiger Original | Mexico 66 e Curadoria LK`  
Caracteres: 50

**SEO title proposto**  
`Onitsuka Tiger Original: Mexico 66 e Modelos LK`  
Caracteres: 49

Hipótese: mantém a entidade principal e adiciona “modelos” para ampliar correspondência com busca de coleção, sem perder Mexico 66.

**Meta atual**  
`Onitsuka Tiger original na LK Sneakers: Mexico 66 e modelos selecionados com curadoria premium, autenticidade e atendimento humano.`  
Caracteres: 131

**Meta proposta**  
`Compre Onitsuka Tiger original na LK: Mexico 66, SD, Sabot e modelos selecionados com curadoria exclusiva, autenticidade e atendimento humano.`  
Caracteres: 144

Hipótese: melhora CTR para busca comercial e ajuda o usuário a entender amplitude da coleção sem falar estoque/prazo como taxonomia.

### 4.2 Bloco hero / abertura — preview de copy

> A seleção Onitsuka Tiger da LK reúne a leitura mais desejada da marca japonesa: Mexico 66, Mexico 66 SD, Sabot e variações de perfil baixo com herança esportiva e proporção fashion. A curadoria prioriza pares originais, materiais como couro e camurça, colorways versáteis e modelos que funcionam do look minimalista ao streetwear premium. Para escolher com segurança, compare silhueta, acabamento e uso esperado; se precisar, nosso atendimento humano ajuda a confirmar a melhor versão para você.

Caracteres aproximados: 505.  
Objetivo: cumprir LKGOC hero robusto 500–700 chars, com entidade/modelos/material/styling/atendimento humano.

### 4.3 FAQ — Real Intent Gate

Todas as perguntas abaixo devem substituir/ajustar o FAQ canônico da coleção, mantendo **FAQ único** e `FAQPage` com nomes idênticos às perguntas visíveis.

| Pergunta proposta | Fonte de intenção | generic-filler |
|---|---|---|
| Qual Onitsuka Tiger escolher: Mexico 66, SD ou Sabot? | GSC `onitsuka tiger`, GSC `onitsuka tiger mexico 66`, objeção comercial/comparação entre versões | false |
| O Onitsuka Tiger tem a forma grande ou pequena? | dúvida de tamanho/modelagem específica de calçado | false |
| Qual a diferença entre Onitsuka Tiger e ASICS? | intenção de comparação/entidade da marca | false |
| Onitsuka Tiger combina com que tipo de look? | styling e decisão de compra | false |
| Onde comprar Onitsuka Tiger original no Brasil com segurança? | SERP/GEO/buying-safety + autenticidade específica | false |

Notas de resposta:
- Não prometer disponibilidade, prazo, estoque, pronta entrega ou encomenda.
- Usar linguagem: curadoria exclusiva, autenticidade, atendimento humano e confirmação individual via chat quando necessário.

### 4.4 Links internos / estrutura

- Manter linkagem para subcoleções: `/collections/onitsuka-tiger-mexico-66`, `/collections/onitsuka-tiger-mexico-66-sabot`, `/collections/onitsuka-tiger-mexico-mid`, `/collections/onitsuka-tiger-moage-co`, `/collections/onitsuka-tiger-otiger-court`.
- Criar, em preview/dev se layout for alterado, um bloco “Como escolher” com 3 caminhos:
  1. `Mexico 66` — perfil baixo e clássico;
  2. `SD / plataforma` — mais presença visual;
  3. `Sabot / variações` — leitura fashion e uso casual.

### 4.5 Schema

- Preservar `CollectionPage`, `BreadcrumbList` e `FAQPage`.
- QA obrigatório antes de qualquer publicação:
  - um único FAQ visível;
  - um único `FAQPage` correspondente;
  - perguntas no JSON-LD idênticas às visíveis;
  - sem FAQ global legado duplicado.

## 5. Métrica de sucesso

Janela: D+7 e D+14 após eventual publicação aprovada.

- GSC: CTR da página para `onitsuka tiger` subir de 0,35% para meta inicial ≥0,60%; CTR page-level sair de 1,30% para ≥1,60% sem perda de posição média.
- GA4/Shopify: aumentar PDP views originados da collection e add-to-cart rate; manter ou melhorar landing CVR vs baseline da fila.
- GEO: página continuar em `llms.txt`, FAQ citável e monitorar se LK aparece como `text_citation` para buscas de compra/autenticidade Onitsuka.

## 6. Risco, rollback e aprovação necessária

- Risco SEO: baixo/moderado; title/meta mexem em CTR e podem oscilar ranking temporariamente.
- Risco CRO/GEO: baixo se for apenas copy/FAQ; médio se envolver layout/tema LKGOC.
- Rollback: snapshot de `seo.title`, `seo.description`, `descriptionHtml` e asset/section do dev theme antes de qualquer mutation; reverter campos/asset ao snapshot se CTR, conversão ou renderização piorarem.
- Aprovação necessária:
  - Shopify SEO fields e `descriptionHtml`: aprovação explícita atual de Lucas.
  - Qualquer layout/theme: primeiro em **dev/unpublished theme**, com preview e QA desktop/mobile; produção só com nova aprovação explícita.

## 7. Não executado

- Nenhum write em Shopify, theme, GMC/feed, GA4/GSC config, Google/Meta Ads, Klaviyo, WhatsApp, preço, desconto ou estoque.
- Não consultei Tiny nem validei disponibilidade operacional; estoque/grade pertence ao `lk-stock`.
- Não publiquei schema, FAQ, copy ou title/meta.
