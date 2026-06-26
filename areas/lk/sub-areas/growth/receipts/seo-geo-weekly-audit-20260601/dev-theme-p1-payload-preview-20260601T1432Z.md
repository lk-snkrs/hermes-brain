# LK Sneakers — P1 Payload Preview em Dev Theme

Timestamp: 2026-06-01T14:32Z

## Escopo aprovado por Lucas

Implementar primeiro no tema dev os dois P1 permitidos:

1. Melhorar Judge.me/reviews sem remover o app.
2. Melhorar footer/payment/SVG/assets.

Fora de escopo: remover/desativar Variant King/StarApps, Rivo ou Simprosys; publicar em produção; alterar produto/preço/estoque/campanhas.

## Tema alvo

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role: `unpublished`

## Alterações aplicadas no dev theme

### 1. Judge.me

Arquivo alterado:

- `layout/theme.liquid`

Mudança:

- O loader customizado `https://cdn.judge.me/widget_preloader.js` passou a carregar apenas em `template.name == 'product'`.
- Mantém Judge.me nas PDPs, onde o tema renderiza `judgeme_preview_badge` e `judgeme_review_widget`.
- Evita esse request extra em homepage/collections, sem remover o app nem alterar as avaliações.

### 2. Footer/payment/SVG/assets

Arquivos alterados/criados:

- `sections/lk-footer.liquid`
- `assets/lk-footer.css`
- `assets/lk-footer.js`

Mudanças:

- CSS estático grande do footer extraído de inline `<style>` para asset cacheável `lk-footer.css`.
- JS estático do footer/newsletter extraído de inline `<script>` para asset cacheável `lk-footer.js` com `defer`.
- Ícones de pagamento do footer limitados a 6 tipos via `shop.enabled_payment_types limit: 6`.
- Foi mantido o pequeno CSS dinâmico de padding da seção no Liquid.

## Readback/API verification

Todos os assets foram enviados ao dev theme e lidos de volta por SHA com `readback_match: true`.

- `sections/lk-footer.liquid`: 25,251 bytes → 12,981 bytes
- `layout/theme.liquid`: 80,971 bytes → 81,189 bytes
- `assets/lk-footer.css`: novo asset, 8,304 bytes
- `assets/lk-footer.js`: novo asset, 4,310 bytes

Backup remoto antes do upload:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/seo-geo-weekly-audit-20260601/dev-theme-p1-payload-backup-20260601T143212Z/`

JSON técnico:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/seo-geo-weekly-audit-20260601/dev-theme-p1-payload-backup-20260601T143212Z/upload-report.json`

## Preview URLs para revisão manual

- Home: `https://lksneakers.com.br/?preview_theme_id=155065450718`
- PDP: `https://lksneakers.com.br/products/nike-dunk-low-rose-whisper?preview_theme_id=155065450718`
- Collection: `https://lksneakers.com.br/collections/air-jordan-1?preview_theme_id=155065450718`

## Limitação de QA visual

Fetch público sem sessão autenticada não renderizou o tema dev com `preview_theme_id`; retornou HTML do tema live/cached. Portanto a verificação conclusiva foi feita por Admin Asset API readback. A revisão visual deve ser feita por Lucas abrindo os links de preview no navegador autenticado/admin.

## Rollback

Rollback do dev theme: re-upar os assets de backup acima para o mesmo theme ID `155065450718`.

Arquivos de backup:

- `sections__lk-footer.liquid`
- `layout__theme.liquid`
- `assets__lk-footer.css` — vazio/não existia antes
- `assets__lk-footer.js` — vazio/não existia antes

## Não feito

- Não publiquei produção.
- Não alterei produtos, preço, estoque, checkout, campanhas, Klaviyo, Rivo, Simprosys ou Variant King.
- Não removi Judge.me.
