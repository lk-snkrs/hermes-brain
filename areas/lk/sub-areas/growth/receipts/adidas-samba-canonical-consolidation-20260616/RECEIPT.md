# Receipt — Adidas Samba Canonical Consolidation

Gerado: 2026-06-16T20:23:36.756815+00:00

## Aprovação recebida
Consolidar Adidas Samba em `/collections/samba`: copiar SEO/GEO otimizado para `/samba`, tentar redirect 301 de `/adidas-samba` para `/samba`, com backup e rollback. Se precisar despublicar/arquivar a duplicata para liberar o redirect, parar e pedir nova confirmação antes.

## Executado
- Backup das duas coleções: OK.
- Conteúdo SEO/GEO otimizado copiado de `/collections/adidas-samba` para `/collections/samba`: OK.
- Redirect criado no Shopify Admin: OK.
- Despublicar/arquivar duplicata: NÃO executado.
- Produtos, preço, estoque, feed, campanhas e theme: sem alteração.

## Resultado do redirect
- Redirect criado: `gid://shopify/UrlRedirect/490896425182`
- Path: `/collections/adidas-samba`
- Target: `/collections/samba`

## QA público
- `/collections/samba`: HTTP 200, canonical `/collections/samba`, conteúdo/FAQ otimizado renderizando.
- `/collections/adidas-samba`: ainda HTTP 200 e canonical próprio.
- Portanto: o redirect existe no Admin, mas não está efetivo publicamente enquanto a coleção duplicada continuar ativa.
- Conforme aprovado, parei antes de qualquer despublicação/arquivamento.

## Evidências
- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-20260616/apply-20260616T202219Z/backup-before.json`
- Apply result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-20260616/apply-20260616T202219Z/apply-result.json`
- Public redirect QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-20260616/apply-20260616T202219Z/public-redirect-qa.json`
- Rollback script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-20260616/apply-20260616T202219Z/rollback_adidas_samba_canonical.py`

## Status atual
- URL principal recomendada `/collections/samba` agora tem o conteúdo SEO/GEO otimizado.
- Duplicidade técnica ainda existe porque `/collections/adidas-samba` continua ativa.
- Próxima decisão: autorizar ou não o tratamento estrutural da duplicata para tornar o 301 efetivo.

## Rollback
Rollback disponível mediante aprovação explícita: restaura o conteúdo anterior de `/collections/samba` e remove o UrlRedirect criado.

## Próxima aprovação se quiser finalizar a consolidação
`Aprovo despublicar/arquivar a coleção duplicada /collections/adidas-samba somente se necessário para liberar o redirect 301 para /collections/samba, com backup, QA e rollback.`
