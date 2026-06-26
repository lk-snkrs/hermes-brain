# LK Growth — Packet A v2: SEO/meta guardrail em coleções P0

Data: 2026-06-05  
Status: **executado após aprovação explícita de Lucas**, com re-documentação decision-grade parcial.  
Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/collection-seo-p0-guardrail-hotfix-20260605T095201Z`

## Escopo executado

- Alteração apenas de `seo.title` e `seo.description` de 20 collections P0.
- Nenhum produto, preço, estoque, campanha, GMC, Klaviyo, checkout ou PDP alterado.
- Backup/readback/rollback salvos por collection.

## Por que refazer o Packet A

Lucas pediu refazer a lógica com fontes corretas antes de avançar Packet B. Este documento registra o Packet A na nova régua: Shopify + Search/AI/SERP + Ahrefs + limitações de GSC/GA4 + camada Claude SEO local.

## Fatos verificados

### Shopify/Admin

- 179 collections lidas via Shopify Admin GraphQL.
- 46 collections com termo operacional em SEO/meta antes do hotfix.
- 20 collections P0 corrigidas.
- Admin readback: 20/20 batendo com candidato.

### Público/cache

- Público inicial: 18/20 limpas na primeira checagem.
- `camiseta-1` e `new-balance-9060` tiveram comportamento de cache/propagação na URL limpa; Admin e preview do tema principal mostravam o valor novo.
- Não foi feito override em `theme.liquid`; seria outro write em theme production.

### DataForSEO / demanda e SERP

Consultas rodadas para termos P0:

- `new balance 9060`: volume BR 246.000; tendência anual +82%; intenção mista com forte componente transacional/informacional.
- `adidas original`: volume BR 18.100; competição alta.
- `nike air force 1`: volume BR 33.100; competição alta.
- `nike dunk sb`: volume BR 2.900; intenção transacional.
- `fear of god essentials`: volume BR 880; intenção majoritariamente informacional.
- `air jordan 1 original`: volume BR 390; competição alta.
- SERP `nike dunk sb original brasil`: LK aparece orgânico #5, mas DataForSEO ainda capturou snippet antigo com `Pronta entrega`; confirma risco real de snippet e necessidade do hotfix/cache recheck.
- SERP `new balance 9060 original brasil`: SERP dominada por New Balance oficial, Netshoes, Mercado Livre, Artwalk etc.; PAA inclui preço, autenticidade e “mais vendido”.

### Ahrefs

- Probe Ahrefs read-only OK.
- `lksneakers.com.br`: DR 35; Ahrefs rank 2.372.902.
- Granularidade usada: domínio, não URL/collection.

### GSC/GA4

- Tentativa local feita.
- GSC bloqueado neste runtime por falta de `google-api-python-client`.
- GA4 bloqueado neste runtime por falta de `google-analytics-data`.
- `pip` não está disponível neste host para instalar dependências durante o run.
- Portanto: **Packet A v2 é decision-grade técnico/copy, mas não decision-grade completo de impacto comercial**.

### AI visibility

- `/llms.txt`, `/llms-full.txt`, `/agents.md` já estavam 8/8 após hotfix anterior.
- DataForSEO LLM mentions retornou 402/subscription para AI visibility; limitação registrada.

### Claude SEO skill

- Skill local `seo` e `lk-seo-weekly-improvement` carregadas/consultadas.
- Aplicado checklist local: SEO e-commerce, meta/snippet, GEO, conteúdo/taxonomia, guardrails de LKGOC.
- Não houve chamada externa ao Claude; classificação correta: **Claude SEO skill checklist aplicado localmente**.

## Coleções P0 atualizadas

- `lancamentos`
- `nike-todos-os-modelos`
- `camiseta-1`
- `adidas-todos-os-modelos`
- `air-jordan-1`
- `todos-special-collections`
- `athleisure`
- `moletom-1`
- `nude-project`
- `aime-leon-dore`
- `bone-streetwear`
- `acessorios-best-sellers`
- `cloud-dancer`
- `calca-streetwear`
- `nike-dunk-sb`
- `new-balance-9060`
- `yeezy`
- `fear-of-god`
- `jacquemus`
- `nike-air-force-1`

## Interpretação

O Packet A foi correto como hotfix de guardrail: remove risco de termos operacionais em SEO/meta nas páginas prioritárias. A limitação é que a priorização foi por risco/volume de catálogo e demanda externa, não por GSC/GA4 live.

## Próximos controles

- Recheck público/cache para `camiseta-1` e `new-balance-9060`.
- D+7: GSC/GA4/Shopify quando dependências estiverem funcionais.
- Não aplicar novos hotfixes sem approval packet com botão inline.

## Rollback

Restaurar `seo.title` e `seo.description` dos `*.before.json` no receipt via Shopify `collectionUpdate`.
