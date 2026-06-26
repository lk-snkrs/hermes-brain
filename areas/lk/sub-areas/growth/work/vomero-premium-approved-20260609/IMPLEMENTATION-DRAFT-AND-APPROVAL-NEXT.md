# Vomero Premium — execução aprovada para draft/read-only

Data: 2026-06-09T19:38:43.757426+00:00
Aprovação Lucas: "Aprovo" após recomendação de seguir com **Vomero Premium P1 em modo read-only/draft**.

## Importante

Nenhum write Shopify production foi executado nesta etapa.

## Snapshots salvos

- Shopify Admin read-only: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/vomero-premium-approved-20260609/shopify-admin-readonly-snapshot.json`
- HTML público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/vomero-premium-approved-20260609/public-html-snapshot.json`
- FAQ JSON-LD draft: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/vomero-premium-approved-20260609/DRAFT-FAQPage-vomero-premium-guia.json`

## Campos Shopify confirmados por leitura Admin

Collection `nike-vomero-premium`:

- id: `gid://shopify/Collection/457531982046`
- title: `Nike Vomero Premium`
- SEO title atual: `Nike Vomero Premium — Comprar | LK Sneakers`
- SEO description atual: `Nike Vomero Premium: running heritage com amortecimento Zoom Air e design contemporâneo. 15 modelos na LK Sneakers, Jardins SP. Frete grátis, 10x sem juros.`
- productsCount lido via Admin, mas não usado como critério de disponibilidade.

Page `nike-vomero-premium-guia`:

- id: `gid://shopify/Page/125780263134`
- title atual: `Nike Vomero Premium: Guia Completo 2026`

## Papel de cada URL no hub

- Collection `/collections/nike-vomero-premium`: página transacional principal para `nike vomero premium`, `comprar`, `original`, gênero/cor quando aplicável.
- Guia `/pages/nike-vomero-premium-guia`: apoio consultivo/GEO para perguntas PAA: o que é, serve para corrida, diferença entre Premium/Vomero 5, tamanho e autenticidade.
- PDPs: conversão por colorway/modelo, com snippets consistentes e sem promessa operacional de disponibilidade.
- Blog: descoberta e contexto editorial; deve linkar para collection/guia, não competir como landing transacional principal.

## Draft de mudanças propostas — produção exige novo approval específico

### 1. Collection SEO

URL: `https://lksneakers.com.br/collections/nike-vomero-premium`

Atual:
- Title: `Nike Vomero Premium — Comprar | LK Sneakers`
- Meta: `Nike Vomero Premium: running heritage com amortecimento Zoom Air e design contemporâneo. 15 modelos na LK Sneakers, Jardins SP. Frete grátis, 10x sem juros.`

Proposto:
- Title: `Nike Vomero Premium Original | LK Sneakers`
- Meta: `Nike Vomero Premium original na curadoria LK: ZoomX, Air Zoom, design running lifestyle e atendimento humano para escolher.`

Motivo:
- Remove contagem dinâmica de modelos.
- Reforça originalidade, tecnologia e curadoria.
- Evita linguagem operacional de disponibilidade.

### 2. Guia — FAQ/GEO

URL: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`

Adicionar bloco citável:

> O Nike Vomero Premium é uma leitura de amortecimento máximo da linha Vomero, com presença visual marcante, conforto elevado e tecnologias como ZoomX e Air Zoom. Na LK, a curadoria prioriza autenticidade, procedência e atendimento humano para orientar a escolha do modelo e da numeração.

FAQ sugerido:

1. O que é o Nike Vomero Premium?
2. Vomero Premium serve para corrida ou para uso casual?
3. Qual a diferença entre Nike Vomero Premium e Nike Vomero 5?
4. Como escolher o tamanho do Nike Vomero Premium?
5. O Nike Vomero Premium vendido pela LK é original?

JSON-LD draft salvo em `DRAFT-FAQPage-vomero-premium-guia.json`.

### 3. Links internos

Implementar ou revisar:

- Collection → Guia: anchor `Guia Nike Vomero Premium`.
- Guia → Collection: anchor `ver curadoria Nike Vomero Premium na LK`.
- Guia → PDPs prioritários: anchors por colorway, sem mencionar estoque/tamanho disponível.
- PDPs → Guia: bloco discreto `Dúvidas sobre tecnologia, caimento e escolha? Veja o Guia Nike Vomero Premium`.
- Blog Vomero → Collection como destino transacional principal.

### 4. PDP copy QA

Prioridade de QA:

- White Bright Crimson: já tem SEO premium consistente.
- Tangerine Tint: meta atual longa/truncada; revisar para versão premium curta.
- Sail Coconut Milk: meta atual ok, mas pode ficar mais premium.

Propostas:

- Tangerine Tint meta: `Nike Vomero Premium Tangerine Tint original na LK: ZoomX, Air Zoom, presença running premium e curadoria para escolher com segurança.`
- Sail Coconut Milk meta: `Nike Vomero Premium Sail Coconut Milk original na LK: estética clean, amortecimento máximo e atendimento humano para orientar a escolha.`

Atenção: PDPs têm termos operacionais no HTML público (`encomenda/sob encomenda/disponibilidade`). Qualquer cleanup desse tipo deve passar por `lk-stock` antes.

## Rollback

Antes de qualquer produção:

1. Exportar SEO title/meta/HTML do recurso Shopify alvo.
2. Aplicar alteração em escopo por URL/campo.
3. Readback Admin + fetch público.
4. Se CTR/indexação/conversão piorar ou houver erro de render, restaurar snapshot anterior.
5. Impact review D+7 via GSC/GA4/Shopify.

## Necessita novo approval para produção

Para aplicar em produção, pedir approval explícito por campos:

- Collection SEO title/meta.
- Page body/FAQ JSON-LD.
- PDP SEO meta de Tangerine/Sail.
- Blocos de links internos no tema/page/product.
