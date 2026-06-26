# Execution Receipt — P1 fixes pós-audit

Data: 2026-06-07 UTC  
Aprovação: Lucas respondeu “Seguir”.  
Escopo: correções P1 do audit SEO/CRO/performance, sem alterar layout visual.

## Writes executados em produção

### 1. WhatsApp recovery mint CORS — mitigado

- Asset: `snippets/lk-whatsapp-widget.liquid`
- Tema: `lk-new-theme/production` (`155065417950`)
- Mudança: o mint `https://recovery.lucascimino.com/links/whatsapp/mint` ficou opt-in atrás de `window.__LK_RECOVERY_MINT_ENABLED === true`.
- Preservado: botão WhatsApp e mensagem com contexto da página.
- Trade-off: hash recovery fica pausado até o endpoint ter CORS correto.
- Readback: OK após retry Shopify.
- Rollback: restaurar `before__snippets__lk-whatsapp-widget.liquid` do diretório de execução.

### 2. n8n cart-intent CORS — mitigado

- Asset: `layout/theme.liquid`
- Mudança: endpoint `https://n8n.lucascimino.com/webhook/lk-cart-intent-v1` desativado e envio protegido por `if (endpoint)`.
- Preservado: `https://recovery.lucascimino.com/events/storefront` continua ativo e retornando 202 no browser.
- Readback: OK.
- Rollback: restaurar `before__layout__theme.liquid`.

### 3. ScriptTag estático ET tracker — removido

- ScriptTag removido: `https://track.lksneakers.com.br/static/tracker.js?client_id=lk-sneakers`
- ID: `240505454814`
- Motivo: emitia `[ET] tracker not configured: set data-client-id and data-api-url` e duplicava a camada `snippets/et-tracker.liquid`, que continua ativa.
- Readback: script tag não aparece mais na lista Shopify.
- Rollback: recriar script tag com o `target_src` salvo em `receipt_delete_static_tracker_script_tag.json`.

### 4. SEO page metafields — suporte no tema + batch de 5 páginas

- Asset: `layout/theme.liquid`
- Mudança: tema agora respeita `page.metafields.global.title_tag` e `page.metafields.global.description_tag` em Shopify Pages.
- Metafields aplicados em:
  - `/pages/reviews`
  - `/pages/acompanhe-seu-pedido`
  - `/pages/adidas-samba-vs-campus-00s`
  - `/pages/new-balance-530-vs-2002r`
  - `/pages/onitsuka-tiger-vs-asics-gel-1130`
- Readback público: OK para title/meta nas 5 páginas.

## Verificação Playwright

URLs verificadas mobile:

- `/collections/new-balance-204l`
  - recovery mint request: 0
  - n8n CORS: ausente no último check
  - ET tracker warning: ausente no último check
  - restante: Klaviyo session CORS ainda aparece.

- PDP Onitsuka Kill Bill
  - recovery mint request: 0
  - n8n CORS: ausente no último check após cache em rota nova
  - ET tracker warning: ausente após remoção do ScriptTag em rota nova
  - restante: Judge.me warning e Klaviyo session CORS.

## Pendências / riscos restantes

1. **Home ainda pode servir cache antigo temporariamente**
   - Em alguns checks, Home ainda vinha sem `__LK_RECOVERY_MINT_ENABLED` e com mint antigo.
   - Coleções/PDP já refletiram patch.
   - Provável cache Shopify/Cloudflare da Home; revalidar depois.

2. **Judge.me warning permanece em PDP**
   - Badge aparece com avaliações e widget recebe classes `jdgm--done-setup`.
   - Warning: `missing jdgm key`.
   - Não alterei app/token porque é configuração de app/runtime e o widget parcial funciona.

3. **Klaviyo session CORS permanece**
   - Origem: `https://a.klaviyo.com/client/sessions/?company_id=WnsRcu`.
   - Pode ser comportamento do SDK/app embed, não necessariamente correção via theme.

## Artefatos locais

Diretório de execução:

`/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/followup-write-20260607T004928Z`

Arquivos principais:

- `receipt_layout_n8n.json`
- `receipt_delete_static_tracker_script_tag.json`
- `receipt_layout_page_seo_support.json`
- `receipt_page_metafields_set.json`
- `verify_after_et_*.json`
