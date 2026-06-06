# Regra LKGOC — FAQ única dentro do guia editorial

Registrado em: 2026-06-05T22:07:31.237803+00:00

## Regra

Em coleção LKGOC, a única FAQ visível deve estar **dentro do guia editorial LKGOC** (`lk-goc-guide-faq lk-guide-standard-faq`).

Não pode haver uma segunda FAQ visível fora do guia, incluindo:

- `.coll-faq`
- `.collection-faq`
- `.faq-section`
- FAQ legado renderizado pela section/template
- blocos duplicados de perguntas abaixo/fora do guia

## QA obrigatório

Para cada coleção LKGOC:

- `details` visíveis fora do guia: 0
- `.coll-faq` visível fora do guia: false
- `.collection-faq` visível fora do guia: false
- `.faq-section` visível fora do guia: false
- FAQ dentro do guia: true
- número de perguntas dentro do guia: validado conforme dataset da coleção

## Correção originadora

No P0 `nike-x-jacquemus-moon-shoe-sp`, havia uma FAQ legada `.coll-faq` visível além da FAQ dentro do guia editorial. Corrigido no DEV para manter visível apenas a FAQ do guia LKGOC.
