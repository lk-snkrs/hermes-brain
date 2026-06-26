# Receipt — Puma Speedcat LKGOC Zero Rebuild from 204L

Data: 2026-06-09  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role: `unpublished`

## Motivo
Lucas rejeitou a tentativa anterior porque estava diferente do tema/padrão correto. Regra aplicada: se está fora do padrão, rollback/limpeza primeiro e refazer do zero a partir do Gold Source real.

## Gold Source usado
- Coleção: `new-balance-204l`
- Asset/código base: `sections/lk-collection.liquid`, bloco `{% if collection.handle == 'new-balance-204l' %}`
- Guia base: `snippets/lk-goc-new-balance-204l-guide-panel.liquid`
- Regra: copiar/adaptar o 204L; só texto, imagens, links, FAQ e nuances mudam.

## O que foi removido/limpo
- Speedcat removido do componente errado `snippets/lk-goc-collection.liquid`.
- Speedcat removido dos renders genéricos `lk-goc-collection` em `sections/lk-collection.liquid`.
- Asset errado de página DEV removido: `templates/page.guia-puma-speedcat-lkgoc.json`.

## O que foi reconstruído
- Bloco Speedcat inserido em `sections/lk-collection.liquid` como clone do bloco 204L real.
- Classes shell 204L preservadas: `lk-goc-coll-preview--204l` e `lk-204l-coll-preview`.
- Modificador `lk-goc-coll-preview--speedcat` adicionado apenas como marcador, sem novo layout.
- Guia Speedcat criado como clone do guia 204L: `snippets/lk-goc-puma-speedcat-guide-panel.liquid`.
- `templates/collection.puma-speedcat.json` mantido como cópia exata de `templates/collection.json`, necessário porque a coleção real usa `template_suffix: puma-speedcat`.

## QA
Playwright DEV:
- Speedcat mobile: `roleUnpublished:true`, `liquid:false`, `hero:true`, `speedHero:true`, `guide:true`, `visibleBad:false`.
- Speedcat desktop: `roleUnpublished:true`, `liquid:false`, `hero:true`, `speedHero:true`, `guide:true`, `visibleBad:false`.
- Gold 204L capturado na mesma rodada.

## Evidências
- Preview: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`
- Side-by-side mobile: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-rebuild-zero-20260609/side-by-side-204l-vs-speedcat-mobile-zero-20260609.png`
- Side-by-side desktop: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-rebuild-zero-20260609/side-by-side-204l-vs-speedcat-desktop-zero-20260609.png`
- JSON QA: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-rebuild-zero-20260609/qa_zero_rebuild_result.json`

## Bloqueios
- Production não alterada.
- Media externo/editorial usado no DEV exige media manifest/validação de direito de uso antes de Production.
- Approval de Lucas obrigatório antes de qualquer promoção para `main`.
