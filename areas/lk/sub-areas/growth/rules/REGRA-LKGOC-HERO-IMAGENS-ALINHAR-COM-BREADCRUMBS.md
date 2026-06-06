# Regra LKGOC — topo das imagens do Hero alinhado ao breadcrumb

Registrado em: 2026-06-05T18:16:56

## Regra obrigatória
Em todo Hero LKGOC desktop, o **topo visual do bloco de imagens/collage** deve alinhar com o topo de `.coll-banner__crumbs`.

## Interpretação visual
- A primeira linha visual do collage não começa abaixo do título nem no meio do banner.
- O topo das imagens deve nascer na mesma altura do breadcrumb `HOME / ...`.
- O texto editorial fica à esquerda; as imagens entram como bloco superior alinhado ao breadcrumb, criando composição premium/editorial.

## QA obrigatório
Antes de aprovar qualquer nova coleção LKGOC:
- medir `.coll-banner__crumbs.getBoundingClientRect().top`;
- medir o topo do bloco de imagens (`.lk-goc-collage`, `.lk-204l-collage` ou equivalente);
- diferença aceitável desktop: até 4px;
- se passar disso, corrigir antes de preview/merge.

## Relação com outras regras
Continua valendo:
- não usar foto de produto isolado no Hero;
- remover/ocultar `.coll-rich-content` legado em coleção otimizada;
- não inventar layout novo: adaptar o padrão LKGOC aprovado.
