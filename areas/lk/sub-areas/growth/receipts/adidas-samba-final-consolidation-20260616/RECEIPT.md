# Receipt — Adidas Samba Final Consolidation

Gerado: 2026-06-16T22:20:09.706144+00:00

## Aprovação recebida
Lucas aprovou finalizar Adidas Samba em `/collections/adidas-samba`: alterar o handle da coleção duplicada `/collections/samba` para um handle de backup, criar 301 de `/collections/samba` para `/collections/adidas-samba`, com backup, QA e rollback.

## Executado
- Backup completo antes do write: OK.
- Coleção principal mantida: `/collections/adidas-samba`.
- Coleção duplicada alterada de handle: `/collections/samba` → `/collections/samba-duplicata-backup-20260616`.
- Redirect criado: `/collections/samba` → `/collections/adidas-samba`.
- Produtos, preço, estoque, feed, campanhas, theme: sem alteração.

## QA público definitivo
- GET `/collections/samba`: 301.
- Location: `/collections/adidas-samba`.
- Follow `/collections/samba`: HTTP 200 em `https://lksneakers.com.br/collections/adidas-samba`.
- Canonical final: `https://lksneakers.com.br/collections/adidas-samba`.
- FAQ/conteúdo otimizado presente na URL final.
- `/collections/adidas-samba`: HTTP 200, canonical próprio.

## QA Admin
- `collectionByHandle("samba")`: não existe mais como coleção ativa.
- `collectionByHandle("adidas-samba")`: existe e segue principal.
- `collectionByHandle("samba-duplicata-backup-20260616")`: existe como backup da antiga duplicata.
- Redirect Admin criado: `gid://shopify/UrlRedirect/490900095198` path=`/collections/samba` target=`/collections/adidas-samba`.

## Pendência importante
A coleção de backup `/collections/samba-duplicata-backup-20260616` ainda é uma URL pública e apareceu no sitemap no spot-check. Isso é consequência de manter a duplicata como backup ativo. Não alterei publicação/arquivamento porque o approval foi para trocar handle e criar redirect, não para despublicar/ocultar a coleção de backup.

Recomendação próxima: aprovar despublicar/ocultar a coleção backup ou aplicar medida equivalente para que ela não vire nova duplicata indexável.

## Evidências
- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-final-consolidation-20260616/apply-20260616T221646Z/backup-before.json`
- Apply result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-final-consolidation-20260616/apply-20260616T221646Z/apply-result.json`
- QA público inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-final-consolidation-20260616/apply-20260616T221646Z/public-final-qa.json`
- QA definitivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-final-consolidation-20260616/apply-20260616T221646Z/final-definitive-qa.json`
- Rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-final-consolidation-20260616/apply-20260616T221646Z/rollback_final_adidas_samba_consolidation.py`

## Rollback
Rollback disponível mediante aprovação explícita: remove o redirect `/collections/samba -> /collections/adidas-samba` e restaura a coleção de backup para o handle `samba`, com os campos anteriores do backup.
