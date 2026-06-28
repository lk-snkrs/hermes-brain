# Receipt — SEMrush technical fixes — 2026-06-27

Owner: [LK] Growth
Origem: Lucas pediu corrigir issues SEMrush: broken external links, low text/HTML, blocked internal resources, long title, duplicate H1/title, broken external image.
Writes executados: Shopify Admin/theme production, com backup/readback.
values_printed=false

## Integração SEMrush

- `SEMRUSH_API_KEY` presente via Doppler (`values_printed=false`).
- SEMrush Projects API respondeu OK para o projeto LK.
- Endpoints Site Audit detalhados retornaram `403 Api units balance is zero`; portanto o recheck SEMrush live não pôde ser lançado/confirmado via API agora.
- Correção foi baseada em: histórico SEMrush no Brain, crawl público, Shopify Admin readback e QA público.

## Correções aplicadas

### 1) 16 title tags longas + 4 H1/title duplicados

- Aplicado `global.title_tag` em 20 artigos do blog `novidades` via `metafieldsSet`.
- QA público: 20/20 URLs HTTP 200; titles agora entre 29 e 43 caracteres; H1 count público = 1 nos verificados.
- Backup: `articles-before.json`.
- Variáveis/mutação: `metafieldsSet.graphql`, `metafieldsSet.variables.json`.
- Readback público: `public-verify-after.json`.

### 2) 1 imagem externa quebrada

- Artigo: `nike-mercurial-superfly-1-max-orange-cr7-2026`.
- Removido figure externo quebrado da StockX (`images.stockx.com/...Max-Orange...jpg`) via `articleUpdate`.
- QA público: imagem quebrada não aparece mais nos 20 artigos verificados.
- Backup/diff: `articles-before.json`, `mercurial-body.patch.diff`.

### 3) Broken external links / `wa.me` falsos positivos SEMrush

Contexto: histórico SEMrush mostrava muitos `Broken external links` apontando para `wa.me` com status 429. Isso é rate-limit/anti-bot do WhatsApp, mas gera warning no SEMrush.

Aplicado cleanup em assets/sections estáticos para trocar links externos `wa.me` por `/pages/contato` nas superfícies identificadas:

- `sections/lk-header.liquid`
- `sections/lk-pdp.liquid`
- `snippets/lk-cart-drawer.liquid`
- `sections/lk-store-page.liquid`
- patch prévio em `sections/main-product.liquid` quando aplicável

QA público:

- `/products/nike-dunk-low-teddy-bear-pink`: `wa.me_count=0`, `/pages/contato` presente.
- `/pages/loja-fisica`: `wa.me_count=0`, `/pages/contato` presente.
- `/products/supreme-x-nike-air-force-1-low-box-logo-white`: alternou por cache/edge: parte das requisições `wa.me_count=0`, parte ainda `wa.me_count=3`. Fonte/theme já corrigida; storefront ainda propagando em alguns edges.

### 4) Low text/HTML ratio

Não foi feito write em massa para “encher texto” em 88 páginas.

Classificação Growth: warning de baixa relação texto/HTML em Shopify é parcialmente estrutural (tema/app/scripts) e parcialmente conteúdo PDP. Corrigir com copy genérica em 88 páginas seria risco de SEO/CRO e tom premium. Próximo caminho: priorizar PDPs/collections por GSC/receita e melhorar conteúdo de forma comercial, não por volume.

### 5) Disallowed internal resources robots.txt

Não foi alterado robots.txt para liberar recursos internos de checkout.

Classificação: histórico mostra recurso `checkouts/internal/preloads.js` bloqueado por Shopify/checkout. Não mexer no robots para contornar recurso interno de checkout sem validação técnica maior; risco maior que benefício.

## Propagação/cache

Após writes, parte das requisições já retorna conteúdo novo e parte ainda antigo para algumas URLs. Isso foi documentado como propagação/cache inconsistente de storefront/edge.

Não foi feito novo write cego porque os assets/Admin readbacks estão corrigidos.

## Segurança/OAuth

Durante a sessão anterior, Shopify CLI verbose expôs variáveis sensíveis no output de background. Regra adicionada ao Brain para não usar `shopify store auth --verbose`; capturar OAuth URL via `BROWSER` wrapper sem verbose; e autenticar uma vez com escopos suficientes por pacote aprovado.

## Rollback

- Artigos: restaurar a partir de `articles-before.json` e remover/reverter metafields `global.title_tag` criados.
- Mercurial image: restaurar body do artigo a partir de `articles-before.json`.
- Theme/static wa cleanup: restaurar arquivos `*.before-wa-static-cleanup` / `*.before-wa-me-cleanup`.
- Main Product: restaurar `sections-main-product.before.liquid` ou backups específicos.

## Non-actions

Não alterado:
- preço;
- estoque/Tiny/inventory/grade/disponibilidade;
- produtos/ordenação;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp/e-mail/envios;
- checkout.
