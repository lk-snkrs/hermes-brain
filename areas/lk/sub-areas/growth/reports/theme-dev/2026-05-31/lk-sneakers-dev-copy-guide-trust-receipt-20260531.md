# LK Sneakers — ajuste Dev Sneakers: intro em 2 parágrafos + guia padrão + confiança loja

Data: 2026-05-31 21:02 UTC

## Escopo

Refinamento aplicado somente no tema Dev da Shopify para `/collections/sneakers`.

- Theme Dev: `155065450718` (`lk-new-theme/dev`, unpublished)
- Theme Production: `155065417950` (`lk-new-theme/production`, main)
- Asset: `sections/lk-collection.liquid`
- Preview: https://www.lksneakers.com.br/collections/sneakers?preview_theme_id=155065450718

## Mudanças aplicadas no Dev

1. Intro da coleção Sneakers passou a renderizar como dois parágrafos reais no hero, preservando o clamp/read-more existente.
2. Copy ampliada para SEO/GEO com termos de intenção:
   - sneakers originais
   - Nike, Adidas, New Balance, Air Jordan, Onitsuka Tiger
   - clássicos, lançamentos, pares premium, modelos para o dia a dia
   - loja física nos Jardins
   - produtos originais, atendimento online e compra segura no Brasil
3. Painel pós-grid refeito no padrão `lk-guide-standard-panel`, alinhado ao modelo usado por New Balance 204L / Nike x Jacquemus / coleções guia.
4. Bloco de confiança adicionado com imagem existente da loja:
   - `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/Loja-LK.jpg?v=1705163797`
   - alt: `Loja física da LK Sneakers nos Jardins em São Paulo`
5. CTA do painel: `Saiba mais sobre a LK` apontando para `/pages/loja-fisica`.
6. Links internos mantidos para New Balance, Adidas, Nike, Air Jordan, Onitsuka Tiger, lançamentos e Sale.
7. FAQ visível e FAQPage JSON-LD preservados, incluindo pergunta sobre loja física.

## Validação

Execução final: `20260531T210225Z`

- Dev readback matches target: `true`
- Production unchanged: `true`
- Marcadores obrigatórios presentes:
  - `collection.handle == 'sneakers'`
  - `Sneakers originais para diferentes estilos, marcas e momentos`
  - `lk-sneakers-hub-panel`
  - `Como escolher sneakers originais na LK`
  - `Perguntas frequentes sobre sneakers na LK`
  - `Loja física da LK Sneakers nos Jardins em São Paulo`
  - `Saiba mais sobre a LK`
  - FAQPage JSON-LD
  - links internos principais
- Copy proibida ausente: `sneakers selecionados pela curadoria`
- Painel continua depois da paginação/grid: `true`

## Production

Não alterado.

- `prod_before_sha256`: `7be7f692f7a484b116fcb2608f6c0e535032223fb3c8f7a4cfe66366bf4f5804`
- `prod_after_sha256`: `7be7f692f7a484b116fcb2608f6c0e535032223fb3c8f7a4cfe66366bf4f5804`

## Receipt técnico

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T210225Z`

## Rollback Dev

Reverter o Dev com:

`sections.lk-collection.dev.before.liquid`

Do diretório:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T210225Z/`

para o asset `sections/lk-collection.liquid` do tema Dev `155065450718`.

## Não-ações

- Sem write em Production
- Sem write em produto
- Sem write em collection admin
- Sem write em preço/estoque/disponibilidade
- Sem write em GMC/feed
- Sem campanha/envio para cliente
