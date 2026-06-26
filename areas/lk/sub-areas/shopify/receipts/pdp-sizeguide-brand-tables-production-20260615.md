# Receipt — PDP size-guide brand tables Production

Data: 2026-06-15 20:26 UTC
Perfil: lk-shopify
Escopo aprovado por Lucas: `Aprovado Production — tabelas de tamanho`

## Escopo executado

Promovido para Production o lote aprovado em DEV de tabelas específicas no modal `Guia de tamanhos` do PDP.

Arquivo alterado:

- `sections/lk-pdp.liquid`

Marcas/modelos cobertos:

- Onitsuka Tiger / Mexico 66
- Adidas geral / Samba / Gazelle / Spezial
- Adidas Yeezy
- ASICS
- Nike geral
- UGG
- Birkenstock

Exceções preservadas:

- Nike Mind 001
- Nike Mind 002
- Jordan 1 Low
- Jordan 1 Mid
- Jordan 1 High
- Nike Vomero Premium

## GitHub / PR

- Branch Production scoped: `prod-sizeguide-brand-tables-20260615`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/80
- Base antes da promoção: `0bab7d98ffca`
- Commit scoped criado: `7f3e399b9cf6`
- Merge commit em `production`: `2bc245d1d7dc`
- Arquivos alterados no PR: 1
- Diff do PR: `sections/lk-pdp.liquid` com 164 inserções e 31 remoções
- Método: PR scoped a partir de `origin/production`; não foi feito merge amplo de `dev` para `production` porque havia drift/unrelated changes em DEV.

## Shopify Production readback

Tema Production verificado via Admin Asset API:

- Theme ID: `155065417950`
- Theme name: `lk-new-theme/production`
- Theme role: `main`
- Asset: `sections/lk-pdp.liquid`
- SHA local/readback: `7d223086fbc0`
- Match local vs Production: `true`

Marcadores confirmados em Production:

- `Onitsuka Tiger costuma ter forma justa`
- `Adidas costuma vestir normal`
- `ASICS lifestyle costuma vestir normal`
- `Yeezy, especialmente Boost 350 V2`
- `UGG costuma ceder`
- `Birkenstock usa grade europeia inteira`
- `Nike costuma vestir normal na maioria dos modelos`

## QA live cache-busted

Rodado QA público em 2 rounds com URLs cache-busted em `https://lksneakers.com.br/products/...`.

Resultado agregado: `all_pass=true`.

PDPs amostrados:

- Onitsuka: `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- Adidas: `samba-og-white-scarlet`
- ASICS: `tenis-asics-gt-2160-white-putty-branco`
- Yeezy: `yeezy-slide-glow-green`
- UGG: `tenis-ugg-zora-ballet-flat-chestnut-marrom`
- Nike geral: `nike-dunk-low-rose-whisper`
- Controle Jordan Mid: `air-jordan-1-mid-wolf-grey`
- Controle Vomero: `tenis-nike-vomero-premium-black-volt-preto`

Critérios por PDP:

- `curl_exit=0`
- HTML público carregado
- `id="lk-sizeguide-modal"` presente
- marcadores da tabela/copy esperada presentes
- sem `Liquid error` detectado nos HTMLs amostrados

## Não-ações / limites

- Nenhum produto, preço, estoque, disponibilidade, coleção, metafield ou conteúdo de produto foi alterado.
- Nenhum write em Tiny/GMC/Klaviyo/ads/WhatsApp.
- Nenhum merge amplo `dev → production`; só o asset aprovado foi promovido.
- Secrets usados apenas via wrappers/Doppler; valores não foram impressos.

## Rollback

Rollback recomendado se Lucas reprovar:

1. Reverter o merge commit `2bc245d1d7dc` em `production` via PR scoped.
2. Alternativamente, restaurar `sections/lk-pdp.liquid` para o SHA/estado anterior de Production (`0bab7d98ffca`) e verificar readback do tema `155065417950`.
3. Rodar o mesmo QA público cache-busted nos PDPs de controle.

## Status final

Production atualizado e verificado.
