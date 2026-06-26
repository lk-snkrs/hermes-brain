# LKGOC Nike Vomero Premium — DEV preview

Registro: 2026-06-13T17:11:01Z

## Status
- Pedido Lucas: “Fazer do nike vomero Premium”.
- Execução feita apenas em DEV/unpublished. Sem write em Production.

## Tema
- Shopify DEV: `lk-new-theme/dev` — theme ID `155065450718` — role `unpublished`.
- Production não alterada.

## Git
- Branch: `feat/lkgoc-vomero-premium`
- Commit: `62969df Add LKGOC Nike Vomero Premium hero`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/75

## Arquivos
- `sections/lk-collection.liquid` — adiciona render do hero Vomero Premium.
- `snippets/lk-goc-nike-vomero-premium-hero-204l-clone.liquid` — novo hero no padrão aprovado 204L/LKGOC.
- Guia existente preservado: `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid`.

## QA
- Shopify push DEV com `--nodelete`: OK.
- Pull/readback DEV: OK.
- Preview mobile UA `/collections/nike-vomero-premium`: hero, headline, CSS mobile de “Ler mais”, guia e grid de produtos presentes.

## Observações
- Fonte visual usada: assets públicos oficiais Nike/Nike Running para Vomero Premium.
- Próximo passo exige aprovação explícita Lucas para Production.


## Ajuste Lucas — guia + foto principal
Registro: 2026-06-13T17:36:26Z

Pedido:
1. Refazer o guia do Nike Vomero Premium no padrão LKGOC.
2. Trocar a primeira foto principal, pois estava aparecendo símbolo da Nike.

Execução:
- Guia refeito em `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid` com padrão LKGOC: intro, card amplo, FAQ accordion/mobile, cards complementares, bloco citável e FAQPage JSON-LD.
- Foto principal do hero trocada em `snippets/lk-goc-nike-vomero-premium-hero-204l-clone.liquid`; removido asset `wzrqsjqpg6pslrevtkpl`.

Commit:
- `eaa6642 Refine Vomero Premium LKGOC guide and hero image`

QA DEV:
- Push Shopify DEV/unpublished #155065450718 OK.
- Pull/readback OK: imagem antiga ausente, nova imagem principal presente, guia LKGOC presente, FAQ com 5 details, CSS mobile e JSON-LD presentes.
- Preview mobile UA da coleção confirmou hero, guia, bloco citável e grid de produtos.

Production:
- Não alterada. PR #75 atualizado.


## Correção — página do guia completa
Registro: 2026-06-13T19:36:07Z

Lucas sinalizou que o link do guia ainda mostrava o conteúdo antigo. Correção aplicada:
- Criado `snippets/lk-goc-nike-vomero-premium-guide-page.liquid` com guia completo LKGOC.
- `sections/main-page.liquid` agora roteia `page.handle == nike-vomero-premium-guia` para o novo snippet e não renderiza o conteúdo antigo da página.
- DEV theme `155065450718` atualizado e validado por readback + fetch mobile.
- Marcadores antigos ausentes no HTML; marcador novo presente: `lk-goc-nike-vomero-premium-guide-page-20260613`.
- Commit: `bc50dae Add full LKGOC Vomero Premium guide page`.

Production não alterada.
