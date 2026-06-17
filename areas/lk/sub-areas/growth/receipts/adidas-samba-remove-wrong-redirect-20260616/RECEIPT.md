# Receipt — Remove Wrong Adidas Samba Redirect

Gerado: 2026-06-16T20:30:53.525696+00:00

## Aprovação recebida
Remover apenas o redirect anterior `/collections/adidas-samba -> /collections/samba` e manter `/collections/adidas-samba` como principal, sem mexer na `/collections/samba` ainda.

## Executado
- Redirect removido no Shopify Admin: OK.
- Coleção `/collections/adidas-samba`: não alterada; continua ativa e otimizada.
- Coleção `/collections/samba`: não alterada; continua ativa.
- Handles, produtos, preço, estoque, feed, campanhas, theme: sem alteração.

## QA público
- `/collections/adidas-samba`: HTTP 200, sem Location/redirect, canonical próprio, conteúdo otimizado e FAQ presentes.
- `/collections/samba`: HTTP 200, sem Location/redirect, canonical próprio; mantida intocada conforme aprovação.

## Evidências
- Backup antes de deletar redirect: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-reverse-20260616/remove-redirect-20260616T203005Z/backup-before-delete.json`
- Resultado delete: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-reverse-20260616/remove-redirect-20260616T203005Z/delete-result.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-reverse-20260616/remove-redirect-20260616T203005Z/public-qa-after-delete.json`
- Rollback para recriar o redirect removido: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-canonical-reverse-20260616/remove-redirect-20260616T203005Z/rollback_recreate_removed_redirect.py`

## Status estratégico
- Decisão corrigida: URL principal SEO deve ser `/collections/adidas-samba`.
- Pendência futura: resolver a duplicata `/collections/samba` quando aprovado, idealmente fazendo `/collections/samba -> /collections/adidas-samba`.
