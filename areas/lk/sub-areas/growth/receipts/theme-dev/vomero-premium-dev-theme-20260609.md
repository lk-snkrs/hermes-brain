# Receipt — Vomero Premium dev theme atualizado

Data: 2026-06-09T19:48:38.095986+00:00
Escopo aprovado por Lucas: **dev theme atualizado**.

## Destino

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado antes do write: `unpublished`
- Production write: **não**

## O que foi atualizado no dev theme

1. Collection `/collections/nike-vomero-premium`
   - Override dev de SEO title/meta no layout:
     - Title: `Nike Vomero Premium Original | LK Sneakers`
     - Meta: `Nike Vomero Premium original na curadoria LK: ZoomX, Air Zoom, design running lifestyle e atendimento humano para escolher.`
   - Painel editorial pós-grid:
     - explicação citável;
     - FAQ;
     - CTA para o guia;
     - FAQPage JSON-LD.

2. Page `/pages/nike-vomero-premium-guia`
   - Bloco FAQ/GEO no fim do conteúdo padrão;
   - CTA para collection;
   - FAQPage JSON-LD.

## Assets alterados

- `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid`
- `snippets/lk-nike-vomero-premium-page-faq.liquid`
- `sections/lk-collection.liquid`
- `sections/main-page.liquid`
- `layout/theme.liquid`

## Preview URLs

- Collection dev preview:
  - `https://lksneakers.com.br/collections/nike-vomero-premium?preview_theme_id=155065450718`
- Guia dev preview:
  - `https://lksneakers.com.br/pages/nike-vomero-premium-guia?preview_theme_id=155065450718`

## QA realizado

Arquivo QA:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/vomero-premium-dev-theme-qa-clean-20260609T194814Z.json`

Resultados principais:

- Collection dev preview: 200
  - title override presente;
  - meta override presente;
  - painel Vomero presente;
  - FAQ schema presente.
- Guia dev preview: 200
  - bloco FAQ presente;
  - FAQ schema presente.
- Production/public clean collection: 200
  - title antigo preservado;
  - marcador dev ausente;
  - painel dev ausente.
- Production/public clean guia: 200
  - marcador dev ausente;
  - bloco dev ausente.

## Rollback

Backups e readback salvos em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/vomero-premium-dev-theme-20260609T194723Z`

Rollback completo:

1. Reaplicar os arquivos `*.before` do receipt nos mesmos asset keys:
   - `sections/lk-collection.liquid`
   - `sections/main-page.liquid`
   - `layout/theme.liquid`
2. Remover ou zerar os snippets novos:
   - `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid`
   - `snippets/lk-nike-vomero-premium-page-faq.liquid`
3. Revalidar preview e public clean.

## Próxima etapa

Se Lucas aprovar depois, promover o diff validado do dev para production seguindo a regra Dev → Production, com novo readback e impact review D+7.
