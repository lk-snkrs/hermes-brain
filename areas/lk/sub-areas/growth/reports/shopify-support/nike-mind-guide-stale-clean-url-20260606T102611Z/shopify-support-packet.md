# Shopify stale clean URL — Nike Mind guide LKGOC

Data UTC: 20260606T102611Z
URL: https://lksneakers.com.br/pages/guia-nike-mind-001-002
Preview funcional: https://lk-sneakerss.myshopify.com/pages/guia-nike-mind-001-002?_ab=0&_fd=0&_sc=1&preview_theme_id=155065417950

## Estado verificado

- Admin REST Page `127519064286` tem `body_html` novo com marcador `lk-goc-nike-mind-guide-rewrite-20260606T094233Z`.
- Production theme `155065417950` (`lk-new-theme/production`, role `main`) tem `sections/main-page.liquid` com branch LKGOC para `page.handle == 'guia-nike-mind-001-002'`.
- Preview do próprio tema de produção com `preview_theme_id=155065417950` renderiza o novo guia corretamente.
- Clean URL pública continua servindo HTML antigo com marcador `lk-recreate-gap-publish-20260531T112815Z`, mesmo com querystring variável e `cf-cache-status: DYNAMIC`.

## Ações já tentadas

1. Touch no Page body com comentário invisível de cache bust.
2. Touch em `sections/main-page.liquid` no production theme.
3. Republish do mesmo theme `155065417950` como `main` — sem troca de tema.
4. Criação/atribuição de template dedicado `page.nike-mind-lkgoc.json`.
5. Unpublish/republish rápido da Page para forçar invalidação de rota.

## Evidência de bloqueio

- Admin/readback: novo conteúdo OK.
- Preview production theme: novo conteúdo OK.
- Clean public URL: conteúdo antigo persistente em múltiplas rodadas.

## Receipts locais

- `receipts/theme-production/nike-mind-guide-lkgoc-production-cache-touch-20260606T102027Z/receipt.json`
- `receipts/theme-production/nike-mind-guide-republish-same-main-20260606T102114Z/receipt.json`
- `receipts/theme-production/nike-mind-guide-custom-template-force-20260606T102222Z/receipt.json`
- `receipts/theme-production/nike-mind-guide-page-republish-force-20260606T102523Z/receipt.json`

## Diagnóstico

Provável stale rendered HTML/route cache do Shopify para Page, semelhante ao problema anterior de stale PDP/collection HTML: source/admin corretos, preview correto, clean URL público preso em HTML antigo.

## Próximo passo recomendado

Abrir ticket/contato com Shopify Support ou resolver manualmente no Admin se houver painel/cache interno. Se aparecer login/captcha, Lucas precisa autenticar manualmente.
