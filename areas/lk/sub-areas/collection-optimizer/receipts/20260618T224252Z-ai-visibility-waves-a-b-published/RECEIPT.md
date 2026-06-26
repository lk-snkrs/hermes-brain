# Receipt — AI Visibility / LKGOC Ondas A+B publicado

Data UTC: 2026-06-18T22:44:02Z
Aprovação Lucas: “APROVO ONDA A E ONDA B”.

## Escopo executado
- Writes Shopify production em coleções aprovadas: **sim**.
- Alteração de tema Shopify: **não**.
- Alteração de estoque/preço/campanha/Klaviyo/GMC: **não**.
- Secrets impressos: **não** (`values_printed=false`).

## Coleções atualizadas
- `/collections/new-balance-9060`
- `/collections/new-balance-530`
- `/collections/alo-yoga-1`
- `/collections/air-jordan-1-low`
- `/collections/adidas-tokyo`
- `/collections/nike-air-rift`

## O que foi atualizado
- `body_html` das 6 coleções com copy premium, FAQ e bloco citável.
- SEO title/meta das 6 coleções via GraphQL `collectionUpdate`.
- Removidas/promessas evitadas: entrega rápida, frete grátis, pix, parcelamento, prazo, disponibilidade, encomenda e termos operacionais sensíveis.

## Evidência
- Backup antes: `backup-before.json`.
- Summary: `apply-summary.json`.
- GraphQL SEO: userErrors vazios no readback de execução.
- QA anti-inferência: sem hits sensíveis no readback admin após publish.

## Rollback
- Restaurar `body_html` por collection a partir de `backup-before.json`.
- Restaurar SEO via GraphQL `collectionUpdate` caso necessário.

## Impact review
Plano criado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/impact-reviews/20260625-ai-visibility-waves-a-b-impact-review-plan.md`.


## Atualização adicional — source maps públicos

Data UTC: 2026-06-18T22:47:11Z

Após o primeiro patch, foi detectado que `assets/llms.txt` não era a fonte servida em `/llms.txt`. A fonte pública real é:
- `templates/llms.txt.liquid`
- `templates/agents.md.liquid`

Ação executada:
- Bloco `LK_AI_VISIBILITY_WAVES_AB` aplicado nos dois templates públicos.
- Readback público confirmou as 6 coleções em `/llms.txt` e `/agents.md`.
- Backups salvos: `llms-template-before.txt`, `agents-template-before.txt`, além dos assets auxiliares `asset-llms-before.txt` e `asset-agents-before.md`.

## QA final
- Shopify collection body: 6/6 atualizadas.
- SEO title/meta: 6/6 confirmadas via GraphQL `collectionUpdate` sem `userErrors`.
- `llms.txt`: 6/6 handles presentes publicamente.
- `agents.md`: 6/6 handles presentes publicamente.
- Termos sensíveis removidos/ausentes no body admin: `frete grátis`, `pix`, `parcelamento`, `prazo`, `disponibilidade`, `sob encomenda`, `estoque`, `pronta entrega`.
- Tema visual/Liquid de coleção: não alterado.
