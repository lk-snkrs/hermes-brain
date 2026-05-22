# LK CRO Dev Theme Preview — 2026-05-19

Status: executado em dev theme, sem publicação em produção
Horário: 2026-05-19 12:33:54 UTC

## Aprovação recebida

Lucas aprovou explicitamente preparar preview CRO no dev theme para Onitsuka/Mexico 66, New Balance 204L e Kill Bill, sem publicar produção, sem alterar preço/estoque/produtos/campanhas, com backup dos assets antes.

## Escopo executado

- Repositório: `lk-snkrs/lk-new-theme`
- Branch: `cro/weekly-preview-20260519`
- Base: `dev`
- PR theme: https://github.com/lk-snkrs/lk-new-theme/pull/15
- Commit theme: `689cf60` — `cro: add weekly revenue preview blocks`
- Shopify dev theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Assets alterados no dev theme:
  - `sections/lk-collection.liquid`
  - `sections/lk-pdp.liquid`

## Mudanças de CRO no preview

### Collections

Aplicado bloco `Curadoria LK` apenas para:

- `/collections/onitsuka-tiger-todos-os-modelos`
- `/collections/onitsuka-tiger-mexico-66`
- `/collections/new-balance-204l`

Conteúdo do bloco:

- reforço de autenticidade/curadoria;
- orientação humana para escolha, numeração, disponibilidade e prazo via chat;
- atalhos contextuais para Mexico 66, Kill Bill, mais vendidos/novidades e chat;
- sem alterar H1, body principal, produto, preço, estoque, desconto, campanha ou checkout.

### PDP Kill Bill

Aplicado bloco `Curadoria LK` apenas para:

- `/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`

Conteúdo do bloco:

- reforço de originalidade e compra segura;
- orientação para confirmar numeração/disponibilidade/prazo pelo chat;
- links para coleção Mexico 66, coleção Onitsuka e chat;
- sem alterar preço, variante, estoque, Add to Cart, Dynamic Checkout, descrição principal, schema ou checkout.

## Backup antes do upload

Backup local dos assets remotos antes do PUT no Shopify:

- Diretório: `/opt/data/hermes_bruno_ingest/shopify-theme-backups/lk-cro-weekly-preview-20260519`
- Manifest: `/opt/data/hermes_bruno_ingest/shopify-theme-backups/lk-cro-weekly-preview-20260519/manifest.json`
- `sections/lk-collection.liquid`
  - Backup: `/opt/data/hermes_bruno_ingest/shopify-theme-backups/lk-cro-weekly-preview-20260519/sections__lk-collection.liquid`
  - Remote updated_at antes: `2026-05-18T18:13:31-03:00`
  - Remote checksum antes: `2a67866c9854f8c1acebabc82b462c7c`
- `sections/lk-pdp.liquid`
  - Backup: `/opt/data/hermes_bruno_ingest/shopify-theme-backups/lk-cro-weekly-preview-20260519/sections__lk-pdp.liquid`
  - Remote updated_at antes: `2026-05-15T13:19:04-03:00`
  - Remote checksum antes: `28c53397144eb58dac2d389c496cc22b`

## Upload / readback

Upload via Shopify Admin API para dev theme:

- `sections/lk-collection.liquid`
  - Remote updated_at após: `2026-05-19T09:31:36-03:00`
  - Remote checksum após: `a6ba7a883043b57fadeeaaa4d9950fb0`
  - Readback: `matches_local=True`
  - Marker remoto: `data-lk-cro-weekly-preview` presente
- `sections/lk-pdp.liquid`
  - Remote updated_at após: `2026-05-19T09:31:37-03:00`
  - Remote checksum após: `adaca7de214489c03d5ce96dc0ee5bc0`
  - Readback: `matches_local=True`
  - Marker remoto: `data-lk-cro-weekly-preview` presente

## Validação visual / DOM

Validação no browser com preview ativo para `lk-new-theme/dev`:

- `/collections/onitsuka-tiger-todos-os-modelos`
  - Status visual: bloco `Curadoria LK` renderizado
  - Marker DOM: 1
- `/collections/onitsuka-tiger-mexico-66`
  - Status visual: bloco `Curadoria LK` renderizado
  - Marker DOM: 1
- `/collections/new-balance-204l`
  - Status visual: bloco `Curadoria LK` renderizado
  - Marker DOM: 1
- `/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
  - Status visual: bloco `Curadoria LK` renderizado abaixo do provador virtual e antes do trust grid
  - Marker DOM: 1

## Limites respeitados

- Produção publicada: não alterada.
- Preço: não alterado.
- Estoque/disponibilidade: não alterado.
- Produtos/variantes: não alterados.
- Campanhas: não alteradas.
- GMC/feed: não alterado.
- Klaviyo/WhatsApp: nenhum envio; apenas links existentes/CTA para chat no preview.
- Checkout: não alterado.

## Rollback

Rollback do preview no dev theme:

1. Usar os arquivos de backup no diretório acima.
2. Fazer PUT dos backups para o theme ID `155065450718` nos mesmos asset keys.
3. Confirmar readback `matches_backup=True`.
4. Revalidar URLs de preview.

Rollback Git:

- Fechar PR #15 ou reverter commit `689cf60` na branch `cro/weekly-preview-20260519`.

## Próxima decisão

Se Lucas aprovar visualmente o preview, próximo passo seguro é QA mobile/desktop mais profundo e eventual pacote de decisão para promover de dev theme para produção. Publicar em produção continua exigindo aprovação explícita nova.
