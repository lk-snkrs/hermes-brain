# LK Sneakers — SEO/CRO quick audit

Data: 2026-06-18 11:06 BRT  
Escopo: read-only público, sem Shopify/Admin/theme/GMC/Klaviyo writes.  
Site: https://lksneakers.com.br

## Evidência coletada

- Homepage: HTTP 200, HTML ~585.798 bytes.
- Sitemap index: HTTP 200, contém:
  - `sitemap_agentic_discovery.xml` → 1 URL (`/agents.md`)
  - `sitemap_products_1.xml?...` → 1.813 locs no XML bruto, sendo ~1.812 produtos detectados
  - `sitemap_pages_1.xml?...` → 60 páginas
  - `sitemap_collections_1.xml?...` → 179 coleções
  - `sitemap_blogs_1.xml` → 74 URLs de blog
- Robots: HTTP 200, permite produtos/coleções/blogs e bots de AI relevantes; Lighthouse marcou 1 erro: `Sitemap: /sitemap.xml` é URL relativa inválida para validação Lighthouse.
- Lighthouse homepage desktop:
  - Performance: 54
  - SEO: 92
  - Accessibility: 92
  - Best Practices: 93
  - FCP: 0,8s; LCP: 1,6s; TBT: 1.900ms; CLS: 0,009; Speed Index: 7,1s; TTI: 6,4s
- Lighthouse homepage mobile:
  - Performance: 48
  - SEO: 92
  - Accessibility: 92
  - Best Practices: 93
  - FCP: 2,4s; LCP: 3,5s; TBT: 16.980ms; CLS: 0; Speed Index: 13,6s; TTI: 25,4s
  - Total payload: ~3.897 KiB
  - Main-thread work: 41,0s
- Terceiros com maior impacto mobile/TBT:
  - Shopify/SWYM: ~1.396ms blocking time, com `swym-ext-shopify.js` ~877ms.
  - Facebook: ~1.225ms blocking time.
  - Google Tag Manager/gtag: ~735ms blocking time.
  - Klaviyo: ~571ms blocking time.
  - Google Fonts: ~99ms blocking time, URL carrega muitas famílias.
- Amostra on-page:
  - Home: title 53 chars; meta 144 chars; 1 H1; 2 JSON-LD; 31 imagens, 0 sem alt.
  - Coleção todos produtos: title 58; meta 144; 1 H1; 3 JSON-LD; HTML ~859KB.
  - Loja física: title 31; meta 114; 1 H1; 2 JSON-LD.
  - Contato: title 21; meta 109; 1 H1; 1 JSON-LD.
  - Sobre: title 32; meta 123; 2 H1 (`O que é raro merece ser encontrado.` e `LK na Imprensa`).
- Amostra PDPs:
  - Product schema, BreadcrumbList e FAQPage aparecem em PDPs testados.
  - Titles e metas existem e estão em faixa aceitável; algumas metas antigas ainda usam copy genérica/truncável.

## Interpretação

### Saúde atual

- SEO técnico básico está bom: páginas indexáveis, sitemap robusto, canonicals presentes, títulos/metas/H1 majoritariamente preenchidos, alt de imagens na amostra sem falhas.
- O maior gargalo de CRO/SEO rápido não é falta de title/meta; é performance mobile e execução JavaScript de apps/tracking.
- A homepage tem bom posicionamento local/curadoria, mas ainda pode converter melhor se o primeiro scroll deixar mais explícito: autenticidade, Jardins/SP, atendimento humano, frete/parcelamento/troca e caminho rápido para categorias campeãs.
- Páginas institucionais estão bem encaminhadas, mas há ajuste pontual: Sobre com 2 H1.
- Robots tem erro pequeno mas corrigível: `Sitemap: /sitemap.xml` deveria ser absoluto (`https://lksneakers.com.br/sitemap.xml`) para evitar warning em validadores.

## Prioridades recomendadas

### P0 — sem write externo agora, preparar approval packet

1. Corrigir robots sitemap absoluto
   - De: `Sitemap: /sitemap.xml`
   - Para: `Sitemap: https://lksneakers.com.br/sitemap.xml`
   - Impacto: remove warning Lighthouse/SEO hygiene.
   - Risco: baixo, mas Shopify robots/theme write exige aprovação.

2. Corrigir estrutura H1 da página Sobre
   - Manter 1 H1 principal.
   - Rebaixar `LK na Imprensa` para H2.
   - Impacto: limpeza semântica e acessibilidade.
   - Risco: baixo, mas page/theme write exige aprovação.

3. Performance mobile: piloto de gating/defer controlado para scripts não essenciais acima da dobra
   - Candidatos a investigar em dev preview: SWYM/Wishlist, Klaviyo onsite/reviews, Facebook pixel, GTM/gtag duplicado, Google Fonts.
   - Objetivo: reduzir TBT/TTI sem quebrar wishlist, reviews, analytics, pixels ou carrinho.
   - Risco: médio/alto; exige dev theme preview + QA repetível antes de qualquer publicação.

### P1 — SEO/CRO conteúdo, baixo risco com preview

4. Fortalecer CTA e trust signals no primeiro scroll da home
   - Reforçar: 100% autêntico, Jardins/SP, atendimento humano, 10x sem juros, frete grátis acima de R$499, troca em 7 dias.
   - Preferir ajuste de copy/section em preview antes de write.

5. Revisar metas antigas/truncáveis em PDPs por lote
   - Amostra mostrou algumas descrições cortadas em ~110 chars no terminal por impressão, mas a página possui meta; o próximo passo é varrer todos os produtos para detectar metas <110, >160 ou genéricas.
   - Fazer por classe de produto/categoria e gerar CSV de preview.

6. Otimizar coleções campeãs com bloco curto de compra guiada
   - Nike Dunk, Air Jordan 1, Yeezy, New Balance 204L, Onitsuka, Nike Air Force 1.
   - Formato: 100–180 palavras + links internos + mini FAQ quando fizer sentido.
   - Escrever com foco em intenção transacional: originalidade, tamanho, ocasião, silhueta, entrega/troca.

### P2 — AI Search/GEO

7. Manter e expandir `/agents.md` e FAQPage nos PDPs
   - Já existe sitemap agentic discovery e FAQPage em PDPs testados.
   - Próximo ganho: respostas consistentes por modelo/silhueta para “qual tamanho escolher”, “é original?”, “onde comprar em SP?”.

8. Source pages / guias úteis
   - Criar/fortalecer guias evergreen: Nike Dunk vs Samba, Guia de tamanhos por marca, Sneaker store Jardins, New Balance 204L.
   - Usar como páginas citáveis para IA e interlink com coleções/PDPs.

## Risco

- Qualquer mudança em Shopify, tema, robots, páginas, metafields, apps, Klaviyo/GTM/Meta requer aprovação explícita atual.
- Performance é sensível porque SWYM, Rivo, Judge.me, Simprosys, Klaviyo, pixels e carrinho podem afetar conversão/attribution; não remover app por conveniência.
- Lighthouse é lab test; decisões finais devem combinar Lighthouse + QA manual + idealmente GSC/CrUX quando disponível.

## Rollback sugerido para execução futura

- Antes de qualquer theme/page/robots write: exportar arquivo/objeto atual, registrar rollback JSON/MD no Brain.
- Aplicar primeiro em dev/unpublished theme quando envolver tema/scripts.
- Validar:
  - homepage mobile/desktop visual;
  - wishlist/SWYM;
  - reviews/Judge.me/Klaviyo se presentes;
  - add to cart/cart drawer/checkout link;
  - analytics/pixels se escopo aprovado;
  - Lighthouse antes/depois;
  - public readback após cache.
- Rollback: restaurar snippet/theme/page/robots anterior ou republicar tema anterior, conforme escopo.

## Próxima decisão proposta

Recomendo começar com um pacote pequeno e seguro:

- Pacote A: robots absolute sitemap + H1 da página Sobre + varredura completa de PDP meta/title para gerar CSV de preview.
- Pacote B: performance dev-preview focado em reduzir TBT mobile, sem remover apps, apenas medindo/deferindo com QA.

Nenhum write externo executado neste audit.
