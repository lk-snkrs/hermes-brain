# Regra LKGOC — “Ler mais” oculto no desktop

Registrado em: 2026-06-05T18:23:21

## Regra obrigatória
No Hero LKGOC desktop, o botão/link **“Ler mais” não deve aparecer**.

## Motivo
No desktop o bloco editorial já mostra texto suficiente e o Hero deve manter composição limpa/premium. “Ler mais” é affordance mobile/compacta ou estado de reveal específico; não deve ficar visível no desktop.

## QA obrigatório
- viewport desktop >= 990px: `.lk-goc-read-more`/`.lk-204l-read-more` deve estar `display:none` ou ausente visualmente;
- viewport mobile: pode aparecer quando fizer parte do padrão aprovado.

## Relação com outras regras
Continua obrigatório:
- topo das imagens alinhado a `.coll-banner__crumbs`;
- remover `.coll-rich-content` legado em coleções otimizadas;
- não usar foto de produto isolado no Hero.
