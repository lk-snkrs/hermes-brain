# SUPERSEDED — NÃO EXECUTAR

Este packet foi invalidado pelo Lucas em 2026-06-05 porque propunha subir snippets legados `lk-samba-204l-*`.

Correção correta: usar namespace canônico `lk-goc-*` e render `lk-goc-adidas-samba` com `part: hero`/`part: guide`.

---

# Approval packet — hotfix Production Adidas Samba LKGOC missing snippets

Data: 2026-06-05T18:25:29

## Problema reportado
URL production: `https://lksneakers.com.br/collections/adidas-samba?readmore_fix=1`

Erro visível: `Liquid error (sections/lk-collection line ...): Could not find asset snippets/lk-samba-204l-hero-v2.liquid`.

## Diagnóstico read-only
Tema Production `155065417950`:
- `sections/lk-collection.liquid`: existe e renderiza `lk-samba-204l-hero-v2` e `lk-samba-204l-guide-v2` para `collection.handle == 'adidas-samba'`.
- `snippets/lk-samba-204l-hero-v2.liquid`: AUSENTE.
- `snippets/lk-samba-204l-guide-v2.liquid`: AUSENTE.

Tema DEV `155065450718`:
- `snippets/lk-samba-204l-hero-v2.liquid`: presente.
- `snippets/lk-samba-204l-guide-v2.liquid`: presente.

## Hotfix proposto
Copiar do DEV para Production apenas estes dois snippets:
- `snippets/lk-samba-204l-hero-v2.liquid`
- `snippets/lk-samba-204l-guide-v2.liquid`

Sem alterar `sections/lk-collection.liquid`, preços, produtos, coleção, campanha ou checkout.

## Impacto esperado
- Remover erro Liquid visível em production.
- Restaurar Hero e guia LKGOC da coleção Adidas Samba.

## Risco
Baixo/médio: write em production, mas escopo restrito a dois snippets ausentes já referenciados pelo section live.

## Rollback
Remover os dois snippets de production ou restaurar estado anterior (ausência), se houver regressão — embora isso volte a exibir o erro Liquid.

## Evidências locais
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605`
- Production pull: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605/prod`
- DEV source: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605/dev`
