# Rollback aplicado — Puma Speedcat LKGOC errado DEV

Data: 2026-06-06T16:27:22.130607+00:00

## Escopo
Rollback do rebuild rejeitado por Lucas em Puma Speedcat. Apenas tema DEV.

## Tema DEV
- ID: 155065450718
- Nome: lk-new-theme/dev
- Role: unpublished
- Section SHA: 1aa02cf2d306fc0fa3673c6c1b38626981c1fd81ce24a587e976f818b7147e41
- Marker `lk-goc-puma-speedcat`: False
- Marker `lk-goc5`: False
- Handle `puma-speedcat` na section: False

## Snippets rejeitados
- `snippets/lk-goc-puma-speedcat-hero.liquid`: exists=False
- `snippets/lk-goc-puma-speedcat-guide-panel.liquid`: exists=False

## Produção
- ID: 155065417950
- Role: main
- Marker `lk-goc-puma-speedcat`: False
- Marker `lk-goc5`: False

## Próximo gate
Não refazer por snippets soltos. Próxima implementação deve entrar via `snippets/lk-goc-collection.liquid`, componente único.
