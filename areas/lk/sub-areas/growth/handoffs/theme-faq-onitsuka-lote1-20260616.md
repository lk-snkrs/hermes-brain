# Handoff — Theme FAQ override Onitsuka Lote 1

Gerado: 2026-06-16T17:12:26.586470+00:00

## Contexto
Após aplicação aprovada do Lote 1 Top 50 PDP FAQ/GEO, Shopify readback confirmou `descriptionHtml` atualizado em 10/10 PDPs.

Fetch público final confirmou novo FAQ visível em 8/10 PDPs. Os 2 PDPs Onitsuka abaixo continuam exibindo FAQ antigo no HTML público:

- `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- `tenis-onitsuka-tiger-mexico-66-white-black-branco`

## Diagnóstico read-only
Busca em theme assets encontrou o texto antigo em:

- `sections/lk-collection.liquid`

Arquivo de evidência:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-lote1-20260616/apply-20260616T165923Z/theme-assets-onitsuka-faq-readonly.json`

## Importante
Não foi feito write em theme production. O escopo aprovado por Lucas excluía theme production.

## Próxima ação recomendada
Criar dev-preview/approval packet separado para remover/substituir o bloco FAQ antigo/legado do theme/section que está sobrescrevendo ou competindo com o `descriptionHtml` dos PDPs Onitsuka.

## Reminder OS
- Reminder OS loop needed: yes
- Reminder OS owner: lk-growth
- Reminder OS next action: preparar dev-preview/packet theme FAQ Onitsuka/global legado
- Reminder OS review trigger: após Lucas aprovar frente visual/theme ou se D0/D1 fetch continuar mostrando FAQ antigo
- Reminder OS evidence: readback-after.json, public-fetch-last-check.json, theme-assets-onitsuka-faq-readonly.json

## Writes externos
- Neste handoff: 0
- Na aplicação anterior aprovada: Shopify productUpdate descriptionHtml em 10 PDPs
