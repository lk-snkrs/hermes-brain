# Approval Packet — Prioridades Growth: Vomero Premium, Sneakerinas/Ballet Core e Samba Crochet

Data: 2026-06-14T15:49:36Z  
Status: **draft/read-only** — nenhum write externo/Shopify executado.  
Dono: LK Growth

## Decisão recebida
Lucas aprovou seguir com as prioridades definidas no chat:

1. **P1 imediato — Nike Vomero Premium**: maior evidência de receita e demanda; foco em collection/guia/PDPs/schema/links internos.
2. **P1/P2 editorial — Sneakerinas / Ballet Sneakers / Ballet Core**: guia novo focado nos modelos vendidos pela LK.
3. **P2 comercial — Samba Crochet**: corrigir leitura anterior; cluster que vendeu foi Crochet, não Samba Jane.

Este packet prepara a execução. Produção Shopify continua exigindo aprovação explícita por escopo/campos.

## Evidência resumida

### Shopify read-only — últimos 90 dias
Arquivos:
- `reports/vomero/vomero-vs-samba-terrada-shopify-readonly-20260614T151816Z.json`
- `reports/ballet-core/sneakerinas-samba-crochet-shopify-readonly-20260614T1548Z.json`

Resultados:
- **Vomero Premium**: R$ 173.999,60 · 40 un. · 31 pedidos.
- **Samba Crochet**: R$ 21.069,90 · 10 un. · 10 pedidos.
- **Ballet Core / Sneakerinas vendido no cluster**: R$ 11.999,95 · 5 un. · 5 pedidos.
- **Samba Jane**: R$ 15.998,91 · 10 un. · 9 pedidos.

Interpretação: Vomero Premium lidera com folga. Samba Crochet tem mais prioridade comercial que Samba Jane. Sneakerinas é menor em receita, mas forte como guia editorial/SEO/GEO por tendência e SERP.

### Demanda/SERP
- `nike vomero premium`: 22.200 buscas/mês no Brasil, intenção transacional, competição alta.
- `puma speedcat ballet`: 2.900 buscas/mês, intenção transacional.
- `sneakerina`: 590 buscas/mês, intenção informacional + transacional secundária.
- `adidas taekwondo mei ballet`: 390 buscas/mês, transacional.
- `ballet sneakers`: 170 buscas/mês, transacional.
- A LK já aparece orgânico #2 para SERP relacionada a `sneakerinas ballet sneakers modelos` com `/collections/ballet-core`.

## P1 — Nike Vomero Premium

### Objetivo
Transformar o cluster Vomero Premium em frente principal de SEO/GEO/CRO: collection como hub transacional, guia como apoio consultivo/AI Search, PDPs como conversão.

### Ações propostas para approval posterior de produção
1. Collection `/collections/nike-vomero-premium`
   - Remover contagem envelhecida de meta/snippet quando existir (`15 modelos` vs fetch público com 20 itens).
   - Ajustar FAQ que mistura `Vomero 5` com `Vomero Premium`.
   - Reforçar copy com: original, ZoomX, Air Zoom, amortecimento máximo, curadoria LK, atendimento humano.
2. Guia `/pages/nike-vomero-premium-guia`
   - Ativar/adicionar FAQPage schema já draftado no Brain.
   - Garantir links para collection e PDPs top.
3. PDPs top por receita
   - Black Volt, Sail Coconut Milk, Flat Stout, Barely Volt, White Bright Crimson.
   - Padronizar title/meta curtos, revisar cor/slug e evitar termos operacionais em SEO fields.
   - Termos de disponibilidade/prazo exigem handoff `lk-stock`, não alteração direta por Growth.

### Risco
Médio: Shopify SEO/descrição em produção é customer-facing. Exige snapshot, rollback e readback.

## P1/P2 — Guia Sneakerinas / Ballet Sneakers

### Objetivo
Criar guia editorial/source page independente, padrão Moon Shoe, para capturar tendência e orientar compra assistida dos modelos que a LK vende.

### URL proposta
`/pages/guia-sneakerinas-ballet-sneakers`

### SEO proposto
- Title: `Sneakerinas e Ballet Sneakers | Guia LK`
- Meta: `Guia LK de sneakerinas e ballet sneakers: Adidas Ballerina, Taekwondo Mei Ballet, Tokyo Mary Jane e modelos baixos com curadoria premium.`
- H1: `Sneakerinas e ballet sneakers: guia LK para escolher a silhueta certa`

### Produtos/coleções linkados
- `/collections/ballet-core`
- Adidas Ballerina Bad Bunny
- Adidas Taekwondo Mei Ballet
- Adidas Tokyo Mary Jane
- Puma Speedcat Ballet, se houver curadoria/produto validado
- Samba Crochet como adjacente de textura artesanal, não como sneakerina pura

### Drafts anexos
- `DRAFT-guia-sneakerinas-ballet-sneakers.md`
- `DRAFT-FAQPage-guia-sneakerinas-ballet-sneakers.json`

## P2 — Samba Crochet

### Objetivo
Separar Samba Crochet de Samba Jane e tratar como cluster próprio.

### Ações propostas
- Criar mini-cluster interno: `Adidas Samba Crochet` / `Samba OG Crochet Pack`.
- Reforçar PDPs Sand Strata e Orbit Green com links cruzados e copy de textura/crochet/looks leves.
- Avaliar collection/landing apenas se GSC/Shopify mostrar demanda suficiente; por ora, foco PDP + links internos.

## Aprovação necessária para próxima etapa

Sem aprovação adicional posso:
- finalizar drafts;
- rodar GA4/GSC/GMC read-only;
- montar payloads Shopify de preview;
- preparar rollback.

Precisa aprovação explícita de Lucas antes de:
- criar ou publicar página Shopify;
- alterar title/meta/descrição/FAQ em produção;
- alterar theme/schema em produção;
- qualquer alteração em disponibilidade, prazo, estoque ou preço.

## Rollback proposto para qualquer write aprovado
1. Snapshot antes por URL/campo/template.
2. Aplicar alteração escopada.
3. Readback público/admin.
4. Receipt no Brain.
5. Revisão de impacto em ~7 dias com Shopify/GA4/GSC.
