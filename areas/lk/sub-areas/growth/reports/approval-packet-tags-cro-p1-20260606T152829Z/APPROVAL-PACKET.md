# Approval Packet — LK Growth P1 Tags/Performance + CRO Preview

Status: preparação/read-only + código local de preview. Nenhum write em produção nesta etapa.

## Evidência
- `script-summary.json`: inventário por URL.
- `script-inventory.json`: scripts inline/src por página.
- `theme-source-map.json`: assets do theme de produção mapeados read-only.
- `theme-source-contexts.json`: contextos de origem dos scripts problemáticos.
- `preview-cro-blocks.liquid`: snippet local proposto para dev theme/preview.

## Diagnóstico técnico
- https://lksneakers.com.br/: html=522400 bytes, scripts=63, images=35, jsonld=2, top_hosts=[['inline', 52], ['cdn.shopify.com', 5], ['lksneakers.com.br', 4], ['', 1]], flags=[['shopify', 32], ['jdgm', 3], ['klaviyo', 3], ['judge', 2], ['recovery', 2], ['n8n', 1]]
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: html=636276 bytes, scripts=68, images=33, jsonld=4, top_hosts=[['inline', 55], ['lksneakers.com.br', 5], ['cdn.shopify.com', 5], ['', 1]], flags=[['shopify', 34], ['judge', 3], ['klaviyo', 3], ['jdgm', 3], ['recovery', 2], ['yotpo', 1]]
- https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: html=602129 bytes, scripts=68, images=23, jsonld=4, top_hosts=[['inline', 55], ['lksneakers.com.br', 5], ['cdn.shopify.com', 5], ['', 1]], flags=[['shopify', 34], ['judge', 3], ['klaviyo', 3], ['jdgm', 3], ['recovery', 2], ['yotpo', 1]]
- https://lksneakers.com.br/collections/new-balance-204l: html=628000 bytes, scripts=66, images=34, jsonld=4, top_hosts=[['inline', 55], ['cdn.shopify.com', 5], ['lksneakers.com.br', 4], ['', 1]], flags=[['shopify', 32], ['klaviyo', 3], ['jdgm', 3], ['judge', 2], ['recovery', 2], ['n8n', 1]]
- https://lksneakers.com.br/collections/adidas-samba-jane: html=601251 bytes, scripts=65, images=23, jsonld=4, top_hosts=[['inline', 54], ['cdn.shopify.com', 5], ['lksneakers.com.br', 4], ['', 1]], flags=[['shopify', 32], ['klaviyo', 3], ['jdgm', 3], ['judge', 2], ['recovery', 2], ['n8n', 1]]
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: html=725417 bytes, scripts=66, images=58, jsonld=4, top_hosts=[['inline', 55], ['cdn.shopify.com', 5], ['lksneakers.com.br', 4], ['', 1]], flags=[['shopify', 32], ['klaviyo', 3], ['jdgm', 3], ['judge', 2], ['recovery', 2], ['n8n', 1]]
- https://lksneakers.com.br/collections/lululemon: html=770130 bytes, scripts=66, images=54, jsonld=4, top_hosts=[['inline', 55], ['cdn.shopify.com', 5], ['lksneakers.com.br', 4], ['', 1]], flags=[['shopify', 32], ['klaviyo', 3], ['jdgm', 3], ['judge', 2], ['recovery', 2], ['n8n', 1]]

Principais fontes identificadas no theme principal:
- `assets/lk-footer.js`: hits=klaviyo, bytes=7533
- `assets/lk-judgeme.css`: hits=jdgm, judge.me, bytes=4552
- `layout/theme.liquid`: hits=recovery.lucascimino, n8n.lucascimino, window.__lkcartintent, jdgm, judge.me, klaviyo, lk-wa, bytes=90307
- `sections/lk-collection.liquid`: hits=lk-wa, bytes=248400
- `snippets/et-tracker.liquid`: hits=gtag, fbq, bytes=25108
- `snippets/judgeme_widgets.liquid`: hits=jdgm, bytes=552
- `snippets/lk-popup.liquid`: hits=lk-wa, bytes=16075
- `snippets/lk-whatsapp-widget.liquid`: hits=recovery.lucascimino, lk-wa, bytes=8836
- `snippets/product-structured-data.liquid`: hits=jdgm, judge.me, bytes=5088

## Problemas P1
1. Volume alto de JavaScript/HTML em páginas mobile: 63–68 scripts no HTML direto e 263–295 requests no Playwright mobile da rodada anterior.
2. `layout/theme.liquid` injeta `LK cart intent capture v2.4` com dual-write para `n8n.lucascimino.com/webhook/lk-cart-intent-v1` e `recovery.lucascimino.com/events/storefront`; Playwright viu CORS/failures nessa família.
3. `snippets/lk-whatsapp-widget.liquid` chama `https://recovery.lucascimino.com/links/whatsapp/mint`; quando falha, degrada funcionalmente, mas gera erro/ruído e custo no front.
4. `snippets/et-tracker.liquid` carrega Meta Pixel + Google Ads remarketing e expõe `w.ET`; console anterior apontou `[ET] tracker not configured`, então precisa validar configuração real antes de mexer.
5. Judge.me aparece por app embed + snippets/settings; console anterior apontou possível missing jdgm key em alguns contextos. Precisa validar app embed/config, não só CSS.

## Recomendações de execução
### Etapa A — sem risco comercial, dev/staging
- Criar branch/dev theme a partir do main ou usar `[Check] - Homologação`, com readback e rollback.
- Aplicar `preview-cro-blocks.liquid` apenas em dev theme, condicional por handle.
- Não remover tags ainda; primeiro instrumentar/mensurar chamadas quebradas.

### Etapa B — correções técnicas propostas
- Recovery/WhatsApp mint: mover chamada para clique no botão WhatsApp ou adicionar feature flag/timeout silencioso, evitando erro em page load.
- Cart intent dual-write: validar CORS nos endpoints ou trocar para endpoint com headers corretos; se não for necessário no client, mover para server-side/web pixel.
- ET tracker: validar se `CLIENT_ID` e `API_URL` estão renderizados; se não, não carregar snippet ou configurar corretamente.
- Judge.me: validar app embed/public token e evitar dupla inicialização entre app embed + snippet custom.
- Scripts não críticos: carregar depois de interação/idle quando não forem essenciais para primeira dobra.

### Etapa C — CRO preview
- Nike Mind PDP: bloco curto “o que é / para quem é / autenticidade / atendimento humano / link para guia”.
- NB 204L collection: guia rápido por cor/intenção e variações de busca.
- Onitsuka/Lululemon: orientação premium e prova de autenticidade.
- Samba Jane: substituir shim por editorial completo apenas se aprovado visualmente.

## Impacto esperado
- Menos ruído de console/CORS e menor risco de INP ruim.
- Tracking mais confiável antes de decisões de mídia/CRO.
- Melhor conversão do tráfego orgânico já existente em páginas com CTR/demanda alta.

## Risco
- Médio se mexer em tracking sem validação: pode afetar Meta/Ads/Klaviyo/Recovery.
- Baixo para CRO block em dev theme.
- Médio para publicação do CRO block se alterar layout above-the-fold sem QA mobile.

## Rollback
- Theme: restaurar asset anterior do dev/prod salvo no receipt antes de qualquer PUT.
- CRO block: remover include/snippet condicional.
- Tags: restaurar snippets `layout/theme.liquid`, `lk-whatsapp-widget.liquid`, `et-tracker.liquid`, Judge.me embed/config.

## Aprovação necessária para próxima etapa
Já há aprovação para preparar. Para aplicar em dev theme: OK se Lucas confirmar o theme-alvo. Para produção: precisa aprovação explícita separada após QA.

