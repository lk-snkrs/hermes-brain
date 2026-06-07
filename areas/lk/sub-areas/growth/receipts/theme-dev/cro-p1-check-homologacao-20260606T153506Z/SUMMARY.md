# Receipt — CRO P1 preview aplicado em [Check] - Homologação

Status: aplicado em theme unpublished; produção não alterada.

Theme: [Check] - Homologação / ID 155010924766 / role unpublished
Snippet: `snippets/lk-cro-p1-growth-preview.liquid`
Layout: `layout/theme.liquid` — inserted_after_main_open

## Readback
- Snippet match: True
- Layout contém marker: True
- Produção alterada: false

## QA Playwright mobile
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: status=200, block_count=1, liquid_error=False, title=Nike Mind 001 Black Chrome Original | LK Sneakers
- https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: status=200, block_count=1, liquid_error=False, title=Nike Mind 001 Pearl Pink Original | LK Sneakers
- https://lksneakers.com.br/collections/new-balance-204l: status=200, block_count=1, liquid_error=False, title=New Balance 204L Original | Curadoria LK Sneakers
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: status=200, block_count=1, liquid_error=False, title=Onitsuka Tiger Original | Mexico 66 e Curadoria LK
- https://lksneakers.com.br/collections/lululemon: status=200, block_count=1, liquid_error=False, title=Lululemon Original | Curadoria Athleisure LK

Screenshots salvos em `screenshots/`.

## Preview URLs
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto?preview_theme_id=155010924766
- https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155010924766
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155010924766
- https://lksneakers.com.br/collections/lululemon?preview_theme_id=155010924766

## Rollback
- Restaurar `layout__theme.before.liquid` no theme 155010924766.
- Remover `snippets/lk-cro-p1-growth-preview.liquid` ou deixar sem render.
- Como é theme unpublished, rollback não impacta produção.
