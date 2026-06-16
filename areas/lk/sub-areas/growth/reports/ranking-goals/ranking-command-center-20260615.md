# LK Growth Ranking Command Center — 2026-06-15

**Modo:** read-only / preview-only.
**Writes externos:** 0. Sem Shopify/theme/GMC/feed/GA4/GSC/Klaviyo/WhatsApp/Ads write.
**values_printed:** false.
**Owner:** LK Growth.
**Rotina:** segunda-feira — Ranking Command Center / LK Growth Ranking OS v2.

## Veredito

A semana tem oportunidade material e acionável: o GSC voltou com **40 oportunidades P1** em `sc-domain:lksneakers.com.br`, com forte padrão de **alta impressão + CTR baixa em posições 4–20**. A prioridade deve ser um bloco misto Google + LLM, mas sem executar writes ainda: transformar as frentes abaixo em approval packets de title/meta, copy demand-led, FAQ/GEO/schema e links internos.

Status de decisão: **decision-grade para demanda GSC e prioridade comercial por Shopify/reports existentes; parcial para GA4/PageSpeed/CrUX**, pois PageSpeed deu timeout no probe e CrUX não teve field record para o origin consultado. GMC é decision-grade no snapshot de saúde de 2026-06-11, mas exige cruzamento por SKU/URL antes de ação por offer.

## Fontes verificadas nesta execução

- `fact_gsc`: `reports/lk-search-console-readonly-router-2026-05-11.md`, regenerado em 2026-06-15, janela `2026-05-16 → 2026-06-12`, 25.000 query/page rows, 12.241 páginas agregadas, 40 P1, writes 0.
- `fact_shopify`: `areas/lk/sub-areas/growth/reports/ranking-goals/revenue-informed-priority-clusters-20260613.md`, Shopify Admin read-only últimos 90d, 1.019 pedidos, values_printed=false.
- `fact_shopify`: `areas/lk/sub-areas/growth/reports/vomero/vomero-priority-refresh-lucas-signal-20260614T151816Z.md`, validação Vomero vs Samba/Terrada últimos 90d.
- `fact_gmc`: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-product-data-local-inventory-review-2026-06-11.md`.
- `platform_signal / live_serp`: DataForSEO Brazil/pt para `nike mind 001`, `onitsuka tiger original` e keyword overview parcial para termos prioritários.
- `Brain`: rotina `areas/lk/sub-areas/growth/rotinas/lk-growth-ranking-os-v2-crons-20260613.md`.

## Top 5 oportunidades da semana

| Rank | Oportunidade | Evidência | Hipótese | Métrica-alvo | Próximo passo |
|---:|---|---|---|---|---|
| 1 | **Nike Vomero Premium** | Shopify read-only confirma R$ 173.999,60 / 40 unid / 31 pedidos em 90d; DataForSEO: `nike vomero premium` 22.200 buscas/mês e SERP com LK em Popular Products | Frente comercial mais forte para subir antes de Samba Jane/Terrada; ajustar collection/guia/PDPs deve capturar CTR e GEO | GSC: cliques, CTR e posição da collection/guia; Shopify: sessões/conversão por landing; AI citations/mentions para guia | Terça: packet Google SEO + Quinta GMC por SKUs Vomero + Sexta GEO/FAQ do guia |
| 2 | **Nike Mind 001** | GSC P1: `nike mind 001` em PDPs com 37.476 e 30.802 impressões, CTR 0,01–0,04%, posição ~9; Nike Mind cluster R$ 231.199,30 / 70 unid / 49 pedidos | Há demanda enorme e CTR subcapturado; precisa consolidar collection/PDP snippet, FAQ e guia/answer blocks para queries `brasil`, `original`, `preço`, `feminino` | CTR por query `nike mind 001` sair de <0,1% para ≥0,5%; manter/ganhar Top 10; cliques orgânicos semanais | Terça: approval packet de title/meta + intro/FAQ GEO sem mexer em preço/disponibilidade |
| 3 | **Onitsuka Tiger / Mexico 66 original** | GSC: collection todos modelos 492 cliques/39.112 impressões, CTR 1,18%, posição 8; Onitsuka cluster R$ 810.696,90 / 313 unid / 256 pedidos; DataForSEO mostra LK em Popular Products para `onitsuka tiger original` | LK já tem autoridade comercial, mas pode capturar mais “original / onde comprar / feminino” com source-page/FAQ/schema e snippet menos genérico | CTR collection todos modelos ≥1,5%; posição média melhorar de ~8 para 6–7; AI text citation além de merchant card | Quarta/Sexta: reforçar collection/source-page e FAQ único, com aprovação antes de Shopify write |
| 4 | **New Balance 204L / 204L Arid Timberwolf** | New Balance cluster R$ 729.216,18 / 285 unid / 236 pedidos; top produto 204L Arid Timberwolf R$ 111.999,60 / 40 unid / 38 pedidos; GMC report valida 204L com schema/FAQ público | 204L segue como scaffold canônico e ativo comercial; oportunidade é proteger ranking e usar como padrão/paridade para próximas collections | Manter Top 3/Top 5 em termos principais; aumentar AI citation para guia/collection; monitorar CTR em queries 204L | Sábado impact/QA + usar 204L como benchmark para packets de outras collections |
| 5 | **Sneakerinas / Ballet Core + Samba Crochet** | Shopify: Samba Crochet R$ 21.069,90 / 10 pedidos; LK já aparece #2 no SERP `sneakerinas ballet sneakers modelos`; DataForSEO: `puma speedcat ballet` 2.900/mês, `sneakerina` 590/mês | Menor receita que Vomero, mas excelente oportunidade editorial/GEO porque LK já tem ranking e tendência emergente | Manter/ganhar Top 3 no termo editorial; gerar AI citation para definição/guia; cliques para `/collections/ballet-core` | Sexta: packet de guia `/pages/guia-sneakerinas-ballet-sneakers`; publicar só com aprovação |

## 1–3 páginas foco da semana

### Foco 1 — Nike Vomero Premium

- **URL/handle:** `https://lksneakers.com.br/collections/nike-vomero-premium` + `https://lksneakers.com.br/pages/nike-vomero-premium-guia`.
- **Query alvo:** `nike vomero premium`, `lk sneakers vomero premium`, PAA sobre diferença/uso/conforto.
- **Hipótese:** corrigir snippet, FAQ confuso e ativar FAQ/GEO do guia aumenta CTR e autoridade textual sem mexer em produção antes da aprovação.
- **Métrica de sucesso:** CTR GSC da collection/guia, cliques orgânicos, posição Top 10, sessões/conversão da landing, AI citation/mentions do guia.
- **Risco:** conteúdo público não pode virar disponibilidade/estoque; qualquer remoção de termo operacional precisa handoff `lk-stock` se tocar disponibilidade.
- **Esforço:** médio.
- **Fonte de verdade:** Shopify orders read-only + GSC + DataForSEO/SERP + Shopify public QA.
- **Aprovação necessária:** sim para Shopify SEO/content/schema/theme production; não para preparar packet.

### Foco 2 — Nike Mind 001

- **URL/handle:** `/collections/nike-mind-001` e PDPs `slide-nike-mind-001-black-chrome-preto`, `slide-nike-mind-001-pearl-pink-rosa`.
- **Query alvo:** `nike mind 001`, `nike mind 001 brasil`, `nike mind 001 original`, `chinelo nike mind 001`.
- **Hipótese:** altíssima impressão com CTR quase nulo indica mismatch de SERP/snippet e concorrência oficial; um packet de title/meta + bloco answer-first + links internos pode converter posição 8–12 em cliques qualificados.
- **Métrica de sucesso:** CTR de `nike mind 001` nos PDPs de <0,1% para ≥0,5%; cliques semanais; posição média estável/melhorando; presença em AI/merchant card separada de text citation.
- **Risco:** preço alto no SERP exige defesa premium por autenticidade/curadoria/atendimento humano, não por promessa de preço/estoque.
- **Esforço:** médio.
- **Fonte de verdade:** GSC P1 + Shopify revenue cluster + DataForSEO SERP.
- **Aprovação necessária:** sim para qualquer Shopify write; packet é livre.

### Foco 3 — Onitsuka Tiger todos os modelos / original

- **URL/handle:** `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos` e cluster Mexico 66.
- **Query alvo:** `onitsuka tiger`, `onitsuka tiger original`, `onitsuka tiger mexico 66`, `onitsuka tiger brasil onde comprar`.
- **Hipótese:** LK já é forte em produto e receita; reforçar intenção “original/onde comprar” com FAQ/citability/source-page deve melhorar CTR e AI text citation, não só merchant card.
- **Métrica de sucesso:** CTR da collection todos modelos de 1,18% para ≥1,5%; posição média ~8 para 6–7; citações textuais em queries de compra original.
- **Risco:** alta competição e muitos sellers baratos; LK deve comunicar segurança/curadoria/autenticidade sem linguagem operacional de estoque.
- **Esforço:** médio/alto.
- **Fonte de verdade:** GSC + Shopify revenue + DataForSEO SERP.
- **Aprovação necessária:** sim para Shopify/source-page/schema writes.

## GMC/Product Data que pode impactar ranking/Shopping

- Prioridade Merchant da semana: não misturar com SEO copy. O gargalo `mhlsf_full_missing_valid_link_template` segue como **Local Inventory/LIA / Simprosys link_template**, não PDP/SEO/price.
- O maior issue de escala é `missing_item_attribute_for_product_type`: 2.577 produtos / 5.496 instâncias, com 2.135 sugestões de cor de alta confiança em preview. Deve entrar na quinta-feira como micro-piloto approval packet, priorizando SKUs dos focos comerciais se houver match.
- `landing_page_error` tem 16 produtos / 34 instâncias e inclui handles estratégicos como 204L/Samba Jane; precisa triagem por offer antes de qualquer update/delete.

## Próximos crons/donos

- **Terça — Google SEO Opportunity Factory:** transformar Nike Mind 001 ou Vomero em packet de title/meta/H1/copy/FAQ/schema/internal links.
- **Quarta — Collection/PDP Optimization Factory:** se Lucas priorizar comercial imediato, preparar Vomero Premium; se priorizar GSC CTR puro, preparar Nike Mind 001.
- **Quinta — Merchant/Product Data Ranking Review:** cruzar GMC missing attributes/landing errors com Vomero, Nike Mind, Onitsuka e 204L; packet micro-piloto, sem write.
- **Sexta — GEO/LLM Citation Factory:** Onitsuka original ou Sneakerinas guide como asset citável.
- **Sábado — QA + Impact Review:** revisar 204L/Vomero/Onitsuka, PageSpeed retry e event/impact ledger; silent se nada material.

## Approval packet recomendado desta semana

**Recomendação de LK Growth:** preparar primeiro o packet **Nike Vomero Premium** porque o sinal comercial de Lucas foi confirmado por Shopify; em paralelo, deixar **Nike Mind 001** como packet de CTR GSC.

Approval wording futuro quando houver preview exato: `Aprovo aplicar somente os campos/textos listados no packet <nome>, nos handles exatos, com rollback e sem alterar preço, estoque, desconto, campanhas ou tema production fora do escopo.`

## Não executado

- Não alterei Shopify, theme, GMC/feed, GSC/GA4, Meta/Google Ads, Klaviyo, WhatsApp, preço, estoque ou desconto.
- Não consultei estoque operacional; disponibilidade segue com `lk-stock`.
- Não publiquei guia/source page nem schema.
- Não usei PageSpeed/CrUX como diagnóstico final porque o probe retornou timeout/404; fica para retry no QA/Sábado.
