# LK Growth — Packet B draft: FAQ/corpo público de collections

Data: 2026-06-05  
Status: **preparado em draft; nenhum write executado**.  
Draft local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/collection-packet-b-faq-guardrail-20260605`

## Escopo do Packet B

Corrigir termos operacionais no corpo/FAQ público das collections, principalmente:

- `Produtos em estoque`
- `Pronta entrega`
- `Entrega SP`
- `Sujeito a encomenda`
- `Estoque limitado`
- `rodar`

## Estado encontrado

- 155 collections têm termo operacional no `descriptionHtml`/FAQ/corpo.
- 58 usam `rodar` em perguntas/respostas de tamanho.
- A origem principal é o `descriptionHtml` das collections, não um snippet único do tema. O tema `sections/lk-collection.liquid` tem muitos blocos específicos e FAQs, mas os termos problemáticos recorrentes vieram das descrições salvas nas collections.
- `sections/lk-collection.liquid` foi lido em produção apenas read-only; nenhum asset alterado.

## Candidate batch preparado

Arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/collection-packet-b-faq-guardrail-20260605/candidate-batch.json`  
Resumo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/collection-packet-b-faq-guardrail-20260605/candidate-summary.csv`

Resultado do candidato local:

- 155/155 descriptions teriam alteração.
- 155/155 ficam sem os termos bloqueados avaliados após substituição local.
- Nenhum write foi executado.

## Copy padrão proposta

### Prazo/disponibilidade

Substituir linguagem operacional pública como:

> Produtos em estoque: envio em até 2 dias úteis...

por:

> A equipe LK orienta a confirmação de prazo, tamanho e disponibilidade pelo chat, considerando modelo, numeração e localidade antes da finalização da compra.

### Tamanho/forma

Substituir:

> roda grande ou pequeno?

por:

> tem forma grande ou pequena?

E trocar `rodar` por `ter ajuste`, `tem forma ampla` ou `tem forma pequena`, conforme contexto.

## Fontes usadas nesta preparação

### Shopify/Admin

- 179 collections lidas.
- Candidatos gerados a partir do `descriptionHtml` atual, com before/after local.

### Público

- Spot-check público confirmou a ocorrência em `new-balance-9060`, `lancamentos` e `adidas-todos-os-modelos`.

### DataForSEO/SERP

- SERP e volume confirmam que algumas pages afetadas têm busca real e snippet sensível: `new balance 9060`, `nike dunk sb`, `adidas original`, `nike air force 1`.

### Ahrefs

- Ahrefs domain probe OK: DR 35.
- Sem gap por URL neste run.

### GSC/GA4

- Não disponível no runtime por dependências ausentes; Packet B **não deve ir para produção em massa** sem priorização por GSC/GA4 ou sem aceitar explicitamente que é correção de guardrail/copy.

### Claude SEO skill

- Checklist local aplicado: e-commerce SEO, conteúdo/taxonomia, GEO, FAQ único, tom premium, evitar taxonomia pública de estoque/encomenda.

## Risco

- **Médio** se aplicado em 155 collections direto, porque altera corpo público e pode afetar FAQ/schema/snippet.
- **Baixo/médio** se aplicado primeiro em lote pequeno P0 + readback + QA público.
- **Médio/alto** se mexer em `sections/lk-collection.liquid` production sem DEV.

## Recomendação de execução

Não executar 155 em massa agora.

### B1 — piloto recomendado

Aplicar em 10–20 collections P0/P1 já priorizadas no Packet A, com backup individual:

- `lancamentos`
- `nike-todos-os-modelos`
- `adidas-todos-os-modelos`
- `air-jordan-1`
- `new-balance-9060`
- `nike-dunk-sb`
- `yeezy`
- `fear-of-god`
- `jacquemus`
- `nike-air-force-1`

### B2 — DEV/theme só se necessário

Se o problema reaparecer por template/snippet, preparar dev theme primeiro. Neste audit, o principal parece collection `descriptionHtml`, então B1 pode ser collectionUpdate com backup/readback, não theme.

## Approval packet — para botão inline

Título do botão: `Aprovar B1 piloto FAQ/corpo`

Texto:

> Aprovo aplicar o Packet B1 piloto nas 10 collections listadas, alterando somente descriptionHtml/FAQ para remover linguagem operacional (`Produtos em estoque`, `Pronta entrega`, `Entrega SP`, `rodar`), sem alterar produto, preço, estoque, campanhas, GMC, Klaviyo, checkout ou theme production; com backup, readback público, rollback e D+7.

## Rollback

Antes de qualquer write, salvar `descriptionHtml` original de cada collection em receipt. Rollback por Shopify `collectionUpdate` restaurando o HTML anterior.
