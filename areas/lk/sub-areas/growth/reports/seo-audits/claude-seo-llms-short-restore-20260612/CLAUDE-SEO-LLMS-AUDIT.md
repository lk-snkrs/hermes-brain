# Claude SEO audit — LK AI/GEO `/llms.txt` strategic restore — 2026-06-12

Gerado em UTC: 2026-06-12T18:04:54.771359+00:00

## Skill usada

- Skill local: `/opt/data/profiles/lk-growth/skills/content-seo/seo/SKILL.md`
- Padrão Claude SEO aplicado: auditoria técnica + GEO/AI Search + drift guard para endpoints `llms`.
- Scripts usados: `fetch_page.py`, `parse_html.py` e checks próprios de GEO/AI Source Map.

## Veredito

- **Corrigir era recomendado.**
- O `/llms.txt` estava seguro contra termos proibidos, mas ainda estava pesado demais para a função de mapa AI/GEO curto.
- O candidato de `llms-fix-all-20260609` era superior para `/llms.txt`: curto, explícito, citável, com todos os hubs prioritários e sem taxonomia operacional.

## Evidência antes

- `/llms.txt` atual antes da correção:
  - len: `47754`
  - linhas: `254`
  - source map: `True`
  - header estratégico AI Search: `False`
  - termos proibidos: `{'pronta entrega': 0, 'encomenda': 0, 'estoque': 0, 'sob encomenda': 0, 'prazo de entrega': 0, 'confirme disponibilidade': 0}`
  - gap: `onitsuka-tiger-todos-os-modelos` não aparecia como priority marker.
- `/llms-full.txt` atual:
  - len: `119031`
  - source map: `True`
  - termos proibidos: `{'pronta entrega': 0, 'encomenda': 0, 'estoque': 0, 'sob encomenda': 0, 'prazo de entrega': 0, 'confirme disponibilidade': 0}`

## Candidato auditado

- Fonte: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/llms-fix-all-20260609/assets-candidate-finalpatch/templates__llms.txt.liquid`
- `/llms.txt` candidato:
  - len Liquid: `5047`
  - linhas: `57`
  - source map: `True`
  - header estratégico AI Search: `True`
  - layout none presente: `True`
  - termos proibidos: `{'pronta entrega': 0, 'encomenda': 0, 'estoque': 0, 'sob encomenda': 0, 'prazo de entrega': 0, 'confirme disponibilidade': 0}`
  - priority markers: `{'nike-vomero-premium': True, 'crocs-relampago-mcqueen-guia': True, 'lululemon': True, 'adidas-samba-jane': True, 'air-jordan-travis-scott': True, 'onitsuka-tiger-todos-os-modelos': True, 'nike-mind-001': True, 'new-balance-204l': True}`

## Correção executada

- Theme production Shopify: `155065417950`.
- Asset alterado: `templates/llms.txt.liquid`.
- `/llms-full.txt` não foi alterado nesta etapa porque estava seguro e tem função de versão completa.
- Backup antes do write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/llms-short-strategic-restore-20260612T1803Z/before/templates__llms.txt.liquid`
- Candidate aplicado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/llms-short-strategic-restore-20260612T1803Z/candidate/templates__llms.txt.liquid`

## QA público depois

- `/llms.txt` público após correção:
  - status: `200`
  - len: `5030`
  - source map: `True`
  - header estratégico: `True`
  - termos proibidos: `{'pronta entrega': 0, 'encomenda': 0, 'estoque': 0, 'sob encomenda': 0, 'prazo de entrega': 0, 'confirme disponibilidade': 0}`
  - priority markers: `{'nike-vomero-premium': True, 'crocs-relampago-mcqueen-guia': True, 'lululemon': True, 'adidas-samba-jane': True, 'air-jordan-travis-scott': True, 'onitsuka-tiger-todos-os-modelos': True, 'nike-mind-001': True, 'new-balance-204l': True}`
- Monitor final pós-baseline:
  - `Veredito: OK`
  - `Falhas: 0`
  - relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/monitors/ai-endpoints/ai-endpoints-monitor-20260612T180348Z.json`

## Baseline atualizada

- Baseline aprovada atualizada em:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/monitors/ai-endpoints/ai-endpoints-approved-baseline.json`
- Agora o drift guard espera:
  - `/llms.txt` curto (~5k), source map presente e sem termos proibidos;
  - `/llms-full.txt` completo, source map presente e sem termos proibidos.

## Rollback

- Reaplicar backup anterior via Shopify Asset PUT:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/llms-short-strategic-restore-20260612T1803Z/before/templates__llms.txt.liquid`
- Risco de rollback: volta ao `/llms.txt` longo, menos adequado para AI Source Map curto.

## Segurança

- Secrets não foram impressos.
- `values_printed=false`.
- Nenhum preço, estoque, campanha, feed GMC, Klaviyo ou checkout foi alterado.
