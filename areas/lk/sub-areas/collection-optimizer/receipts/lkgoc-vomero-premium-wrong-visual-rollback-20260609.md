# LKGOC Vomero Premium — rollback por visual errado

Data: 2026-06-09T20:28:40.342556Z

## Motivo
Lucas apontou que a aplicação do padrão 204L na Vomero Premium ficou visualmente errada.

Problemas observados:
- Texto com contraste ruim/ilegível.
- Packshots em fundo branco dentro de hero escuro, sem linguagem editorial.
- Labels herdados da 204L/Rosalia.
- Resultado não segue o padrão premium definido para LKGOC.

## Ação executada
Rollback imediato no tema DEV/unpublished `155065450718`.

## Verificações pós-rollback
- Production: não alterada.
- Tema DEV role: unpublished.
- `sections/lk-collection.liquid` restaurado do backup.
- `snippets/lk-goc-nike-vomero-premium-hero-204l-clone.liquid` deletado.
- `templates/collection.vomero-premium-lkgoc.json` deletado.
- Readback normal e `view=vomero-premium-lkgoc`:
  - HTTP 200
  - Liquid error 0
  - `lk-goc-coll-preview--vomero-premium`: 0
  - texto ruim: 0
  - produtos Vomero: 20

## Decisão operacional
Parar execução visual em Shopify até redefinir o processo.
Próxima tentativa deve começar com mock/screenshot aprovado fora do tema, ou com imagem editorial adequada, não packshot em fundo branco.
