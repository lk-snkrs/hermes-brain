# Receipt — Collection SEO/GEO Batch 7

Gerado: 2026-06-16T20:07:54.364653+00:00

## Escopo aprovado
Aplicar o batch Collection SEO/GEO nas 7 coleções existentes, com backup e rollback. Não aplicar Nike Shox TL ainda.

## Status
- Shopify production write: executado.
- Coleções aplicadas: 7/7.
- Nike Shox TL: não aplicada / fora do escopo.
- Tema, preço, estoque, feed, campanhas e Klaviyo: sem alteração.
- Secrets: não impressos (`values_printed=false`).

## Coleções aplicadas
- `adidas-samba`
- `adidas-samba-jane`
- `nike-mind-001`
- `new-balance-204l`
- `onitsuka-tiger-mexico-66`
- `puma-speedcat`
- `asics-gel-kayano-14`

## Evidência técnica
- Backup antes do write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/backup-before.json`
- Resultado do apply/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/apply-result.json`
- Readback semântico Admin: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/semantic-readback.json`
- QA público por frases globais: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/public-render-qa.json`
- QA público por frases únicas: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/public-unique-phrase-qa.json`
- Rollback script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-batch-20260616/apply-20260616T200441Z/rollback_collection_batch_from_backup.py`

## QA Admin / Shopify GraphQL
- `adidas-samba`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `adidas-samba-jane`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `nike-mind-001`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `new-balance-204l`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `onitsuka-tiger-mexico-66`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `puma-speedcat`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.
- `asics-gel-kayano-14`: descrição OK por frases 8/8; SEO title OK=True; meta OK=True.

## QA termos proibidos nos campos editados
- `adidas-samba`: forbidden_hits=[]
- `adidas-samba-jane`: forbidden_hits=[]
- `nike-mind-001`: forbidden_hits=[]
- `new-balance-204l`: forbidden_hits=[]
- `onitsuka-tiger-mexico-66`: forbidden_hits=[]
- `puma-speedcat`: forbidden_hits=[]
- `asics-gel-kayano-14`: forbidden_hits=[]

## QA público
- Páginas retornaram HTTP 200.
- SEO title/meta públicos confirmados em spot-check, incluindo Samba Jane e New Balance 204L.
- Frases únicas da descrição renderizadas publicamente em 5/7 no primeiro check.
- Samba Jane e New Balance 204L: SEO/meta e FAQ aparecem no HTML público; marcador único anterior foi frágil, não bloqueante.
- Termos como `10x`, `pix` e `frete grátis` ainda aparecem no HTML público por blocos globais do tema/benefícios, não nos campos editados das coleções.

## Riscos / pendências
- Duplicidade Adidas Samba permanece: `/collections/samba` vs `/collections/adidas-samba` exigem decisão separada de canonical/redirect.
- Nike Shox TL segue como oportunidade não aplicada por ausência de coleção mapeada.
- Recomendado recheck de cache/render em D+1 e análise GSC em 7-14 dias.

## Rollback
Rollback reversível pelo script acima, restaurando `descriptionHtml` e `seo` a partir do `backup-before.json`. Exige aprovação explícita antes de executar.
