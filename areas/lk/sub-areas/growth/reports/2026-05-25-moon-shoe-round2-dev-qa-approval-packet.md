# LK Growth — Moon Shoe Round 2 dev QA / approval packet

Data: 2026-05-25  
Escopo: tema Shopify dev `lk-new-theme/dev` (`155065450718`)  
Status: **preview em dev atualizado; produção não alterada**.

## O que foi executado no dev theme

### Coleção Shopify personalizada

URL de preview:

`https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1&lkqa=20260525-121511`

Mudanças:

- Intro da coleção compactada para primeira dobra mais shoppable.
- Hero mantido com fotos editoriais/pessoas usando o produto; sem packshot no hero.
- Adicionada faixa de transição “Seleção LK” entre hero editorial e grid de produtos.
- Sidebar de filtros removida do desktop para limpar a vitrine de 6 itens.
- Botão “Filtros” oculto no desktop para não deixar trigger morto; mantidos contagem de itens e ordenação.
- Grid desktop em 3 colunas para leitura mais premium.

### Source Page / editorial

URL de preview:

`https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?view=moon-source&preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1&lkqa=20260525-121125`

Mudanças:

- Hero substituído: saiu imagem de produto isolado, entrou imagem editorial com pessoa/styling.
- Intro encurtada e mais direta.
- CTAs no hero: “Ver seleção LK” e “Perguntas frequentes”.
- Mantidos blocos citáveis, tabela de colorways, FAQ e seleção relacionada.

## QA feito

- Readback Shopify OK nos assets alterados.
- Tema verificado como `lk-new-theme/dev`, role `unpublished`.
- Nenhuma alteração em produção.
- Nenhuma alteração em Shopify SEO fields, coleção production, produto, preço, estoque, GMC, Klaviyo ou campanhas.
- Guardrail de termos públicos verificado nos assets alterados: sem `estoque`, `encomenda`, `pronta entrega`.
- Browser QA:
  - coleção renderiza intro compacta, bridge “Seleção LK”, grid 3 colunas e sem sidebar/filter button morto;
  - source page renderiza hero editorial com pessoa usando/styling, não packshot;
  - barra de preview Shopify atrapalha screenshots, mas não é parte da experiência final.

## Evidência visual

- Coleção: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_02c753cec9f64960b6e1a203f55a1ec3.png`
- Source page: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_a86756a7034b463687ddc721f093c4fe.png`

## Receipts / rollback

Receipts principais:

- Round 2 base: `areas/lk/sub-areas/growth/receipts/theme-dev/moon-shoe-round2-dev-20260525-120922/receipt.json`
- Bridge fix: `areas/lk/sub-areas/growth/receipts/theme-dev/moon-shoe-round2-bridge-fix-20260525-121125/receipt.json`
- Filter button cleanup: `areas/lk/sub-areas/growth/receipts/theme-dev/moon-shoe-filter-button-hide-20260525-121511/receipt.json`

Rollback:

- Reenviar os arquivos `*.before.liquid` dos receipts acima para o mesmo tema dev verificado.
- Como produção não foi alterada, não há rollback de production neste estágio.

## Veredito

Preview está mais alinhado com o padrão novo:

- coleção = comércio + curadoria compacta;
- source page = autoridade/GEO + narrativa citável;
- hero visual human-centric;
- FAQ mantida como suporte de busca/compra, não preenchimento genérico.

## Próxima decisão

Antes de produção, ainda recomendo Lucas revisar visualmente os dois links no celular. Se aprovado, preparar pacote separado de produção com escopo exato dos assets/fields a publicar, rollback e revisão de impacto em ~7 dias.
