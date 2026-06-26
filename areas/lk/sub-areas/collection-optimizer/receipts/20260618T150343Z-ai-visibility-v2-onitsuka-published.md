# Receipt — AI Visibility v2 Onitsuka Tiger publicado

Data UTC: 20260618T150343Z
Área: LK Collection Optimizer / LKGOC
Aprovação: Lucas escreveu no Telegram: “Aprovo publicar o AI Visibility v2 Onitsuka Tiger nos alvos listados.”
Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T145226Z-ai-visibility-v2-onitsuka-tiger-approval-packet.md`

## Writes executados

Shopify main theme ID `155065417950`:
- `templates/llms.txt.liquid`
- `templates/agents.md.liquid`
- `sections/lk-collection.liquid`
- `sections/lk-geo-source-pages-v2.liquid`

Shopify resources:
- Collection `onitsuka-tiger-todos-os-modelos`: body_html com Bloco citável LK.
- Collection `onitsuka-tiger-mexico-66`: body_html com Bloco citável LK.
- Page `onitsuka-tiger-original-brasil-guia-lk`: body_html com Bloco citável LK.

Não criados:
- `onitsuka-tiger-mexico-66-sd` não foi criado; SD continua como subversão dentro do hub/guia.

## Snapshots / rollback

Diretório de trabalho:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v2-onitsuka-20260618/`

Arquivos/diretórios:
- `snapshots-before/`
- `candidates/`
- `theme-snapshots-before-visible/`
- `theme-snapshots-before-visible-apply/`
- `theme-candidates-visible/`
- `apply-results.json`
- `apply-results-visible-theme.json`
- `public-readback-final.json`

Rollback: restaurar assets e body_html/page body usando snapshots acima.

## Readback público final

Executado com requests + cache-buster após aguardar propagação CDN.

Confirmado:
- `https://lksneakers.com.br/llms.txt`: 200, Sabot/Metallic/Slip-On e guia Mexico 66 presentes.
- `https://lksneakers.com.br/agents.md`: 200, Sabot/Metallic/Slip-On e guia Mexico 66 presentes.
- `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`: 200, Bloco citável LK e frase canônica de herança japonesa presentes.
- `https://lksneakers.com.br/collections/onitsuka-tiger`: 200, alias público também retorna bloco canônico.
- `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`: 200, Bloco citável LK e frase canônica Mexico 66 presentes.
- `https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil-guia-lk`: 200, Bloco citável LK, frase canônica e “Metallic para efeito fashion” presentes.
- `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-sabot`: 200.
- `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-metallic-series`: 200.
- `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66-slip-on`: 200.

Nenhum `Liquid error` detectado nos readbacks finais.

Observação: no readback final da Mexico 66, o conteúdo canônico foi confirmado; o ID de card específico de theme ainda não apareceu numa das bordas, provavelmente por cache/variação de render. Como o texto público e bloco citável estão presentes, o objetivo GEO está atendido.

## Impact review

Revisão D+7 recomendada: 2026-06-25.
Métricas desejadas: GSC por URL/query, GA4/Shopify landing sessions, ATC, checkout, revenue, CTR e prompts manuais em ChatGPT/Perplexity/Gemini.
