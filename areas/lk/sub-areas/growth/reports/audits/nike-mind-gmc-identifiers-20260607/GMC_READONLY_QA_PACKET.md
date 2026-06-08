# Nike Mind — GMC read-only QA de identificadores

Data: 2026-06-07T21:27:21.143188+00:00
Modo: read-only, sem writes.
Decision-grade: `False`

## Resumo

- Produtos GMC carregados: `6000` em `120` páginas.
- Próxima página remanescente: `True`.
- Erros de fetch: `0`.
- Linhas candidatas do pacote anterior: `104`.
- Linhas bloqueadas do pacote anterior: `19`.
- Já OK no GMC (`brand=Nike` e `mpn=style_sku`): `0`.
- Precisam `brand/mpn`: `0`.
- Não encontradas: `0`.
- Ambíguas: `104`.

## Recomendação

Aplicar futuramente, em write separado, somente as `0` linhas não ambíguas em `NEEDS_BRAND_MPN`, após confirmar o mecanismo de atualização Merchant/feed.

- `brand`: Nike
- `mpn`: style SKU confiável
- `gtin`: manter vazio até fonte real
- `identifier_exists`: não forçar false como default

Manter bloqueadas ou revisar manualmente:

- `19` linhas do pacote anterior com SKU vazio/style inválido;
- `104` linhas ambíguas;
- `0` linhas não encontradas no Merchant.

## Arquivos

- `gmc_products_list_full_or_bounded.json`
- `gmc_readonly_qa_summary.json`
- `gmc_readonly_qa_matches.json`
- `gmc_readonly_qa_matches.csv`

## Agregado por handle/status

- `slide-nike-mind-001-blackened-blue-azul`: AMBIGUOUS_NEEDS_BRAND_MPN=7
- `slide-nike-mind-001-mineral-slate-verde`: AMBIGUOUS_NEEDS_BRAND_MPN=7
- `slide-nike-mind-001-pearl-pink-rosa`: AMBIGUOUS_NEEDS_BRAND_MPN=7
- `slide-nike-mind-001-sail-bege`: AMBIGUOUS_NEEDS_BRAND_MPN=13
- `slide-nike-mind-001-team-red-vermelho`: AMBIGUOUS_ALREADY_OK=1, AMBIGUOUS_NEEDS_BRAND_MPN=8
- `slide-nike-mind-001-white-speed-red-branco`: AMBIGUOUS_NEEDS_BRAND_MPN=13
- `tenis-nike-mind-002-black-hyper-crimson-preto`: AMBIGUOUS_NEEDS_BRAND_MPN=13
- `tenis-nike-mind-002-grey-football-grey-cinza`: AMBIGUOUS_NEEDS_BRAND_MPN=9
- `tenis-nike-mind-002-light-smoke-grey-cinza`: AMBIGUOUS_NEEDS_BRAND_MPN=13
- `tenis-nike-mind-002-sail-bege`: AMBIGUOUS_NEEDS_BRAND_MPN=13
