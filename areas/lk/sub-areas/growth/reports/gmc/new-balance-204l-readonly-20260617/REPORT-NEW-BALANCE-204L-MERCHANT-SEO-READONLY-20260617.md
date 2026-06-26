# New Balance 204L — Merchant + SEO/GEO read-only — 2026-06-17

**Modo:** read-only autenticado + QA público.  
**Writes executados:** 0. Sem Shopify write, sem produto/preço/estoque, sem feed/GMC write, sem campanha, sem theme.  
**Segredos:** via Doppler/hermes wrapper; `values_printed=false`.

## Veredito executivo

A página `/collections/new-balance-204l` já está razoável em SEO/GEO público: title/meta atuais estão alinhados, FAQ existe, canonical OK e a collection tem 32 produtos no Shopify Admin. O gargalo mais material agora não é reescrever a coleção; é **Product/Merchant visibility**.

O cluster aparece em SERP altamente transacional, com Product/Shopping pack no topo e players fortes. A LK já aparece organicamente em `new balance 204l comprar` na posição orgânica 8 no DataForSEO mobile, mas para `new balance 204l` o topo é dominado por New Balance oficial + blocos de shopping/imagens/vídeos.

## Evidência coletada

### Shopify/Admin read-only
- Collection: `/collections/new-balance-204l`
- Products count: 32
- SEO title atual: `New Balance 204L Original | LK Sneakers`
- Meta atual: `New Balance 204L original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- FAQ detectado no conteúdo: True
- Variants/estoque não consultados.

### QA público
- HTTP: 200
- Title público: `New Balance 204L Original | LK Sneakers`
- Meta pública: `New Balance 204L original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- Canonical: `https://lksneakers.com.br/collections/new-balance-204l`
- Conteúdo contém New Balance 204L: True
- Conteúdo contém FAQ: True
- Conteúdo contém original/autenticidade: True
- Conteúdo contém perfil baixo: True

### GMC/Merchant autenticado — filtro New Balance 204L
- Produtos/statuses Merchant escaneados: 23747
- Itens 204L encontrados no Merchant: 228
- Canal: [['online', 129], ['local/LIA', 99]]
- Marca: [['New Balance', 228]]
- Data sources: [['accounts/5297679409/dataSources/10636492695', 123], ['accounts/5297679409/dataSources/10636384718', 99], ['accounts/5297679409/dataSources/10525577766', 6]]
- Issues principais no cluster:
  - `missing_item_attribute_for_product_type`: 260 instâncias
  - `mhlsf_full_missing_valid_link_template`: 66 instâncias
  - `landing_page_error`: 17 instâncias
  - `item_missing_required_attribute`: 10 instâncias
- Campos ausentes agregados no cluster: [['color', 67], ['size', 6], ['ageGroup', 6], ['gender', 6], ['productTypes', 6], ['googleProductCategory', 6]]

### Landing pages com erro no GMC — checagem pública
- `5706324928133224313` — `Tênis New Balance 204L x Atmos Cow Girl Brown Marrom - Tamanho 39` — HTTP 404 — https://lksneakers.com.br/products/tenis-new-balance-204l-x-atmos-cow-girl-brown-marrom
- `16066821251494448304` — `39` — HTTP 404 — https://lksneakers.com.br/products/tenis-new-balance-204l-raincloud-ash-wood-cinza?variant=48067171090654&_pos=20&_fid=d0e586b86&_ss=c
- `15014470994320532817` — `Tênis New Balance 204L Slate Grey Raincloud Cinza - Tamanho 36` — HTTP 404 — https://lksneakers.com.br/products/tenis-new-balance-204l-slate-grey-raincloud-cinza

## Interpretação

1. **SEO da collection não é o primeiro gargalo.** A página já tem title/meta bons, FAQ e canonical correto. Um ajuste fino pode aumentar CTR, mas o upside maior está em cobertura Product/Shopping.
2. **Atributos de produto/merchant estão travando parte do cluster.** O maior problema é falta de `color` em itens 204L e lacunas pontuais de `size/ageGroup/gender/productTypes/googleProductCategory`.
3. **Local/LIA tem problema estrutural de `link_template`.** Há 66 instâncias em 204L com `LIA_*` afetadas. Isso é feed/local contract, não copy da PDP.
4. **Há 3 landing pages retornando 404.** Isso é a correção mais objetiva para Merchant crawl, mas qualquer ação exige validação de origem do feed e approval porque mexe em feed/ProductInput/URL mapping.
5. **SERP confirma tese Product-first.** Para `new balance 204l comprar`, Google mostra shopping/knowledge graph antes ou junto do orgânico, e a LK aparece no orgânico; para ganhar mais, precisamos melhorar elegibilidade e qualidade dos produtos no Merchant.

## Recomendação P1 — sem write ainda

Preparar micro-piloto Merchant em 3 frentes, com aprovação explícita antes de executar:

1. **Corrigir/validar 3 `landing_page_error` do cluster 204L**
   - Checar se o handle correto existe ou se a oferta está órfã no feed.
   - Se houver URL correta, propor mapping/patch seguro.
   - Se a oferta for órfã, propor remoção/stop no feed de origem.

2. **Micro-piloto `color` em 20 offers 204L**
   - Priorizar online offers sem `color` e com title indicando cor: Bege/Cinza/Marrom/Prateado.
   - Não inventar cor quando title não sustenta evidência.
   - Não mexer em GTIN/MPN sem fonte confiável.

3. **Diagnóstico LIA/link_template separado**
   - 66 instâncias em 204L são parte do problema global local/LIA.
   - Não corrigir em massa dentro do batch 204L sem confirmar contrato Simprosys Local Feed.

## Aprovação necessária para executar próxima etapa

**Approval packet sugerido:** Merchant 204L micro-piloto read/write controlado.

Escopo proposto:
- até 3 correções/decisões de landing-page error 204L;
- até 20 patches de atributo `color` em offers 204L com evidência por title/link;
- backup antes, readback imediato e readback tardio;
- rollback por ProductInput anterior quando aplicável;
- sem alterar produto Shopify, preço, estoque, campanhas, theme ou checkout.

## Artefatos

- `nb-204l-merchant-items.json`
- `new-balance-204l-shopify-readonly.json`
- `new-balance-204l-public-qa.json`
- `nb-204l-landing-page-error-url-checks.json`

## 18 tópicos canônicos — cobertura nesta rodada

- GA4: não aberto nesta rodada; baseline comercial herdado do factory anterior.
- GSC: baseline herdado do factory anterior; não reconsultado neste run.
- GMC: coberto com leitura autenticada Merchant API.
- Shopify SEO: coberto read-only.
- Shopify CRO/theme: não aplicável ao microdiagnóstico Merchant; sem theme write.
- GEO/AI Search: coberto via FAQ/copy público e SERP/PAA.
- PageSpeed/CrUX/CWV: não aplicável nesta etapa.
- Schema: não auditado em profundidade nesta rodada.
- Reviews: não auditado nesta rodada.
- Paid media: SERP/Product visibility considerada; campanhas não alteradas.
- Influencer/social demand: SERP mostrou vídeo/social demand, sem ação.
- Concorrência/SERP: coberto via DataForSEO mobile.
- Google Business/local: LIA/link_template identificado, sem GBP write.
- Klaviyo/CRM: não aplicável.
- Catálogo/product data quality: coberto via Merchant attributes.
- Conteúdo/taxonomia comercial: collection revisada; sem taxonomia de disponibilidade.
- Mensuração/QA de eventos: não aplicável.
- Impact review/experimentation: recomendado D+7/D+14 após qualquer write aprovado.
