# LK Growth — Claude SEO audit rápido

Status: read-only, parcialmente decision-grade. GSC está decision-grade para demanda/CTR; GA4 smoke test OK, mas este relatório ainda não cruza receita/conversão por página; PageSpeed/CrUX público bloqueou por quota/timeout; GMC não foi reconsultado nesta rodada.

## Fontes usadas

- Skill lk-seo-weekly-improvement + camada Claude SEO: seo-audit, seo-page, seo-geo, seo-google.
- GSC read-only router: janela 2026-05-07..2026-06-03, 25.000 linhas query/página, 12.276 páginas agregadas.
- GA4 connector probe: GA4_LK_PROPERTY_ID OK, row_count 1; outra property histórica 403.
- DataForSEO: volumes/concorrentes/SERP para termos selecionados.
- Playwright/CDP privado: homepage, coleções, páginas, robots e llms.

## Principais problemas encontrados

### P0/P1 — Liquid error visível na coleção Adidas Samba Jane

URL: https://lksneakers.com.br/collections/adidas-samba-jane

Texto público visível na página: Liquid error (sections/lk-collection line 951): Could not find asset snippets/lk-samba-jane-editorial-v3.liquid

Impacto: quebra visual/confiabilidade em coleção com demanda forte. DataForSEO indica adidas samba jane com 2.400 buscas/mês no Brasil e pico recente de 8.100/mês; intenção transacional.

Recomendação: corrigir asset/snippet ausente ou remover include condicional. Fazer em dev theme e QA desktop/mobile antes de produção.

### P1 — CTR muito baixo em páginas com impressão alta e posição boa

GSC roteou 40 oportunidades P1. As primeiras:

- nike mind 001 -> PDP Black Chrome: 5 cliques / 30.305 impressões / CTR 0,02% / posição 9,0.
- onitsuka tiger -> collection Onitsuka: 66 / 25.976 / CTR 0,25% / posição 8,3.
- nike mind 001 -> PDP Pearl Pink: 9 / 25.038 / CTR 0,04% / posição 8,9.
- lululemon -> collection Lululemon: 124 / 17.661 / CTR 0,70% / posição 5,5.
- lk -> homepage: 19 / 13.223 / CTR 0,14% / posição 6,3.
- new balance 204l -> collection: 28 / 10.615 / CTR 0,26% / posição 9,7.

Impacto: há demanda real; o gargalo principal é snippet/title/meta e/ou mismatch de intenção, não descoberta.

Recomendação: pacotes de title/meta + on-page acima da dobra para Nike Mind, Onitsuka, Lululemon, NB 204L e brand query lk. Produção só com aprovação.

### P1 — Nike Mind meta description truncada/ruim

URL: https://lksneakers.com.br/pages/guia-nike-mind-001-002

- Title: 36 chars, OK.
- Meta description: 320 chars, gerada como trecho corrido de conteúdo; tende a truncar e começa duplicando Guia LK · Nike Mind Nike Mind...

Impacto: página informacional/assistiva existe, mas snippet está fraco justamente para uma query de alta demanda. DataForSEO: nike mind 001 18.100 buscas/mês; picos de 49.500–74.000/mês no início de 2026. GSC mostra CTR crítico nos PDPs.

Recomendação: meta de 145–155 chars e bloco citável no topo conectando 001/002 + autenticidade + atendimento humano.

### P1 — Homepage title/meta longos e brand SERP não domina orgânico

Homepage:

- Title: 78 chars — acima do padrão 50–60.
- Meta: 187 chars — acima de 150–160 e termina truncado/estranho: Frete grátis acima de R.
- SERP mobile lk sneakers: Google mostra GBP/reviews e Instagram antes do orgânico principal; LK aparece orgânico rank group 2/rank absoluto 5. Reclame Aqui também aparece forte.

Impacto: para busca de marca, a experiência é boa por GBP 4,9/409 reviews, mas o site oficial deveria capturar melhor o clique orgânico e reforçar autenticidade/loja física.

Recomendação: ajustar title/meta de homepage para marca + Jardins + autenticidade; reforçar links internos para Sobre/Loja Física/Autenticidade.

### P1 — Performance/front-end pesado

Playwright mobile observou:

- Homepage: networkidle não estabilizou em 45s; 234 resources; 86 scripts; 103 other; 30 imagens; load aproximado 3,36s, DOMContentLoaded 1,99s.
- Adidas Samba Jane: networkidle não estabilizou em 45s; 233 resources; 87 scripts; load aproximado 4,44s.
- Duplicação de gtag/Ads detectada em requests: GA4 e Ads aparecem mais de uma vez.
- PageSpeed API sem key usable nesta chamada retornou 429; probe com API key deu timeout; portanto sem score Lighthouse confiável nesta rodada.

Impacto: risco direto em LCP/INP mobile, especialmente em PDP/collection com mídia e scripts de checkout/ads.

Recomendação: auditoria de tags e carregamento: GTM/gtag duplicado, scripts de checkout/shopify, pixel Meta, lazy/defer, tamanho de hero. Primeiro em dev theme/QA.

### P2 — GEO/AI Search: llms existe, mas precisa ficar mais citável/comercial

/llms.txt está acessível via Playwright e contém descrição institucional. Porém:

- Fetch público simples às vezes recebe 503, então crawler/AI access deve ser monitorado.
- O texto é institucional; falta estrutura de respostas curtas para perguntas reais da SERP: Que marca é LK? Onde fica a loja LK Sneakers? LK Sneakers é confiável? LK Sneakers é original?

Recomendação: criar seções em formato pergunta/resposta, com facts auto-contidos: endereço, curadoria, autenticidade, reviews Google, atendimento humano.

### P2 — Parâmetros srsltid aparecendo em SERP/GSC

SERP de marca retornou URLs com ?srsltid=... para homepage, loja física e sobre. GSC também capturou PDP com currency/country/variant/utm_source/google.

Impacto: não parece crítico se canonical estiver correto, mas polui relatórios e pode diluir sinais se páginas parametrizadas forem indexadas/renderizadas em excesso.

Recomendação: confirmar canonical/self canonical nos templates e configurar reporting/normalização nos roteadores; avaliar se Shopify/GMC está injetando parâmetros inevitáveis.

## O que melhorar primeiro

1. Corrigir Liquid error Adidas Samba Jane.
2. Preparar pacote de title/meta para top 10 GSC P1: Nike Mind PDPs, Onitsuka Tiger, Lululemon, homepage, NB 204L, Crocs McQueen, Yeezy, Vomero Premium.
3. Corrigir meta description Nike Mind guia.
4. Auditar e reduzir duplicação de tags/scripts no mobile.
5. Atualizar llms.txt e páginas Sobre/Loja Física com blocos citáveis para brand/entity queries.
6. Criar/validar source pages/collection guides para queries transacionais com pico: Nike Mind 001/002, NB 204L, Adidas Samba Jane, Onitsuka Tiger.

## Checklist 18 tópicos LK Growth

- GA4: conector smoke OK; falta cruzar receita/conversão por página nesta rodada.
- GSC: OK; fonte principal desta auditoria.
- GMC: não reconsultado nesta rodada; usar próximo para Nike Mind/feeds/parametrização.
- Shopify SEO: problemas claros em meta/title e Liquid error.
- Shopify CRO/theme: coleção com erro visível; performance/scripts pesados.
- GEO/AI Search: llms.txt existe; precisa blocos citáveis e crawler monitoring.
- PageSpeed/CrUX/CWV: não decision-grade; API quota/timeout, mas Playwright sugere excesso de scripts/resources.
- Schema: presente em páginas testadas; precisa validação profunda de tipos e Product/FAQ/Breadcrumb por template.
- Reviews: GBP forte 4,9/409; falta explorar em snippets/páginas citáveis sem exagero.
- Paid media: sinais de Google Shopping/Ads aparecem em URLs e scripts; precisa QA de tags.
- Influencer/social demand: homepage usa influenciadores; não cruzado com demanda nesta rodada.
- Concorrência/SERP: DataForSEO indica concorrência com Mercado Livre, Enjoei, Netshoes, Artwalk, Droper, Nike, Farfetch, Shopee, Maze.
- Google Business/local: GBP forte; oportunidade de fortalecer Página Loja Física/LocalBusiness schema.
- Klaviyo/CRM signals: não avaliado nesta rodada.
- Catálogo/product data quality: sinais de PDPs com alto volume/baixo CTR; GMC precisa confirmar atributos.
- Conteúdo/taxonomia comercial: coleções LKGOC boas, mas erros/snippets e metas precisam manutenção.
- Mensuração/QA eventos: duplicação provável de tags; precisa auditoria GTM/GA4/Ads.
- Impact review/experimentation: sugerir lotes com review em 7 dias após qualquer write aprovado.

## Aprovação necessária

Sem aprovação atual, só read-only/previews. Precisam aprovação antes de executar em produção:

- title/meta/descrição em Shopify;
- correção de theme production/snippet;
- mudanças em llms.txt se publicadas na loja;
- alterações de tags/analytics/GMC.
