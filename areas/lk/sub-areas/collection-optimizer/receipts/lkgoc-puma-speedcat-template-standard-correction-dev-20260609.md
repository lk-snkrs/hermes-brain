# Receipt — Puma Speedcat via template padrão LKGOC DEV

Data: 2026-06-09  
Theme DEV: `155065450718` / `lk-new-theme/dev` / `unpublished`

## Correção de direção
Lucas apontou que a correção anterior ainda estava errada: a Speedcat não deveria ser tratada como template/classe/HTML próprio por coleção.

Regra canônica aplicada:
- usar o template padrão Shopify cadastrado para coleções otimizadas: `templates/collection.lkgoc.json`;
- preview seguro por `?view=lkgoc` no tema DEV;
- não depender de `templates/collection.puma-speedcat.json` como template por coleção;
- manter shell visual compartilhado e alterar somente conteúdo específico.

## Diagnóstico verificado por API
- Collection Speedcat atual: `template_suffix = puma-speedcat`.
- DEV possui `templates/collection.lkgoc.json` com `lkgoc_template_mode: true`.
- Production/main não possui `templates/collection.lkgoc.json`.
- Portanto, alterar `template_suffix` da collection para `lkgoc` agora seria write customer-facing/arriscado e não foi feito.

## Correção aplicada em DEV
Asset alterado:
- `snippets/lk-goc-collection.liquid`

Correção:
- conteúdo Speedcat dentro do componente padrão foi limpo para remover texto herdado de 204L;
- hero Speedcat agora fala de Puma Speedcat/motorsport;
- guide Speedcat agora tem ID `lk-guia-puma-speedcat` e texto Speedcat;
- estrutura visual/HTML shell do gold 204L preservada.

## Preview correto
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`

## QA estrito
- role DEV/unpublished: true
- `Liquid error`: false
- template custom marker `collection.puma-speedcat`: false
- hero Speedcat existe: true
- guide Speedcat existe: true
- grid existe: true
- grid antes do guide: true
- hero contém Speedcat: true
- guide contém Speedcat: true
- hero contém New Balance/204L herdado: false
- guide contém New Balance/204L herdado: false
- linguagem proibida estoque/pronta entrega: false

## Evidências
- QA JSON: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/qa_view_lkgoc_strict_result.json`
- Mobile screenshot: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/speedcat-mobile-view-lkgoc.png`
- Desktop screenshot: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/speedcat-desktop-view-lkgoc.png`

## Bloqueio para ativação real na collection
Para a collection usar `template_suffix=lkgoc` de forma permanente, precisa de aprovação explícita porque é write em objeto Shopify e pode afetar Production. Antes disso, Production/main deve receber `collection.lkgoc.json` e section compatível via fluxo DEV → QA → approval → merge/promoção.
