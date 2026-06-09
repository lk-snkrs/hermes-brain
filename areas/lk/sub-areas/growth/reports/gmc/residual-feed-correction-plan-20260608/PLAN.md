# GMC residual feed correction plan — 2026-06-08

Status: read-only plan / sem write

## Summary
- total_products: `22595`
- residual_products: `263`

## Lanes de correção
- manual-enrichment: 148
- supplemental/feed-source: 115

## Fontes
- accounts/5297679409/dataSources/10636492695: 148
- accounts/5297679409/dataSources/10525577766: 115

## Atributos em issue
- color: 850
- age group: 555
- gender: 555
- size: 535

## Classes principais
- color sem inferência segura: 170
- fileInput/fonte externa: 115
- product_type/category ausentes: 115
- age/gender pendente: 111
- size pendente: 107
- title quebrado/tamanho-only: 95

## Pacotes de trabalho recomendados

### 1. Supplemental/feed-source
- Objetivo: resolver itens fileInput/fonte externa e product_type/category ausentes.
- Aprovação: necessária para criar/alterar supplemental feed ou origem.
- Risco: médio; afeta elegibilidade Shopping.
- Rollback: snapshot + remover supplemental rules/voltar arquivo anterior.

### 2. Feed attribute fix
- Objetivo: corrigir size/age_group/gender na fonte correta.
- Não recomendo novo patch amplo até validar por amostra o comportamento de `size` no processed product.
- Aprovação: necessária para write em feed/GMC.

### 3. Manual enrichment de color
- Objetivo: tratar color sem inferência segura.
- Método: revisar modelo/handle/brand manualmente ou planilha de supplemental feed.
- Aprovação: necessária antes de write.

### 4. Source-root-fix para title quebrado
- Objetivo: corrigir itens com title igual a tamanho (`37`, `G/l`, etc.).
- Prioridade alta: isso é raiz de múltiplos issues e prejudica Shopping/SEO.
- Owner provável: fonte do feed/Shopify app/supplemental, não Merchant API direta.

## Próxima decisão sugerida

Preparar um approval packet de **Supplemental Feed Residual Fix Batch 8** com CSV preview para os itens fileInput/source-root-fix, sem executar write ainda.

## Files

- Items: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/residual-feed-correction-plan-20260608/residual_feed_plan_items.json`
- Work packages: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/residual-feed-correction-plan-20260608/work_packages.json`