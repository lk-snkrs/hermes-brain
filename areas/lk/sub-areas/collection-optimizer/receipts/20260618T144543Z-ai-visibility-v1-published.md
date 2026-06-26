# Receipt — AI Visibility v1 publicado

Data UTC: 20260618T144543Z
Área: LK Collection Optimizer / LKGOC
Aprovação: Lucas respondeu “Aprovo” no Telegram em reply ao Approval Packet AI Visibility v1.
Pacote aprovado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T141200Z-ai-visibility-source-map-and-citable-blocks-v1.md`

## Writes executados

- Shopify main theme ID `155065417950`:
  - `templates/llms.txt.liquid`
  - `templates/agents.md.liquid`
  - `snippets/lk-goc-collection.liquid`
  - `snippets/lk-nike-mind-guide-panel.liquid`
  - `sections/lk-authenticity-hub-v2.liquid`
  - `sections/lk-authenticity-hub.liquid`
- Shopify collections:
  - `nike-x-jacquemus-moon-shoe-sp` body_html com bloco citável LK
  - `nike-mind-001` body_html com bloco citável LK
  - `nike-vomero-premium` SEO description sem número volátil “15 modelos”
- Shopify pages:
  - `nike-mind-001-guia` title/body_html com bloco citável e FAQ
  - `autenticidade` body_html com bloco citável

## Snapshots / rollback

Snapshots e candidatos salvos em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v1-20260618/`

Arquivos principais:
- `snapshots-before/`
- `snapshots-during-apply/`
- `theme-snapshots-before-visible/`
- `candidates/`
- `theme-candidates-visible/`
- `apply-results.json`
- `apply-results-visible-theme.json`
- `public-readback-final.json`

Rollback: reverter assets/theme e body_html/SEO/page fields usando snapshots acima.

## Readback público

Readback público executado com requests e cache-buster.
Resultado final após aguardar propagação CDN:
- `https://lksneakers.com.br/llms.txt`: 200, source map contém Jacquemus/Mind hub.
- `https://lksneakers.com.br/agents.md`: 200, source map contém Jacquemus/Mind hub.
- `https://lksneakers.com.br/collections/nike-vomero-premium`: meta nova confirmada em 3/3 leituras, sem “15 modelos”.
- `https://lksneakers.com.br/collections/nike-mind-001`: bloco citável/termos confirmados em 3/3 leituras.
- `https://lksneakers.com.br/pages/autenticidade`: bloco visível confirmado após propagação.
- `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp`: bloco confirmado em 2/3 leituras; uma borda de CDN ainda serviu cache antigo durante a janela de verificação.
- `https://lksneakers.com.br/pages/nike-mind-001-guia`: bloco confirmado em 2/3 leituras; uma borda de CDN ainda serviu cache antigo durante a janela de verificação.

Nenhum `Liquid error` detectado nas leituras.

## Pendências de revisão

- Revalidar CDN/public readback em ~24h para Jacquemus e guia Nike Mind 001.
- Impact review D+7 em 2026-06-25: GSC/GA4/CTR/queries/impressões se disponíveis.
- Métrica LLM decision-grade continua bloqueada por limitação de plano DataForSEO LLM mentions.
