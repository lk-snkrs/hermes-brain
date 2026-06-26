# Receipt — AI Visibility v4 Air Jordan Travis Scott publicado

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Aprovação Lucas: “Aprovo publicar o AI Visibility v4 Air Jordan Travis Scott nos alvos listados.”
Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T184400Z-ai-visibility-v4-air-jordan-travis-scott-approval-packet.md`
Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v4-travis-scott-20260618/`

## Writes executados

Shopify theme main `155065417950`:
- `templates/llms.txt.liquid` — source map Air Jordan Travis Scott v4 + regra anti-inferência.
- `templates/agents.md.liquid` — guidance Air Jordan Travis Scott v4 + regra anti-inferência.
- `sections/lk-travis-scott-ai-visibility-v4.liquid` — seção condicional de collection criada.
- `templates/collection.json` — seção condicional adicionada após seções existentes.
- `sections/lk-travis-scott-guide-ai-visibility-v4.liquid` — seção dedicada de guia criada.
- `templates/page.travis-scott-ai-v4.json` — template dedicado criado para o guia.

Shopify resources:
- Smart collection `air-jordan-travis-scott` (`id=429966819550`) — `body_html` atualizado com bloco citável v4.
- Page `air-jordan-travis-scott-original-brasil-guia-lk` (`id=127337431262`) — `body_html` atualizado com bloco citável v4 e `template_suffix` alterado de `geo-source-d` para `travis-scott-ai-v4`.

## Conteúdo publicado

- Cluster Air Jordan Travis Scott original no Brasil.
- Source map para Air Jordan 1 Low, Air Jordan 1 High, Air Jordan 4, Reverse Mocha, Black Phantom, Medium Olive, Canary, Fragment e Mocha.
- Blocos citáveis para IA sobre autenticidade, alto ticket, procedência, Swoosh reverso, materiais, caixa/acessórios, colorways, forma e compra assistida.
- Regra explícita para assistentes: não inferir estoque, preço final, tamanho disponível ou prazo; encaminhar ao atendimento humano LK.

## Readback

Admin readback:
- `llms.txt`: marker `LK_TRAVIS_SCOTT_AI_V4_START` presente.
- `agents.md`: marker `LK_TRAVIS_SCOTT_AI_V4_START` presente.
- Collection body_html: marker `LK_AI_VISIBILITY_V4_TRAVIS_SCOTT_START` presente.
- Page body_html: marker `LK_AI_VISIBILITY_V4_TRAVIS_SCOTT_START` presente.
- `templates/collection.json`: seção `lk_travis_scott_ai_v4` presente.
- `templates/page.travis-scott-ai-v4.json`: existente.
- Sections `lk-travis-scott-ai-visibility-v4` e `lk-travis-scott-guide-ai-visibility-v4`: existentes.
- Page template_suffix: `travis-scott-ai-v4` confirmado.

Public readback:
- `https://lksneakers.com.br/llms.txt`: OK; marker v4 e regra anti-inferência visíveis.
- `https://lksneakers.com.br/agents.md`: OK; marker v4 e regra anti-inferência visíveis.
- `https://lksneakers.com.br/pages/air-jordan-travis-scott-original-brasil-guia-lk`: HTML bruto já acusa presença de classe/section `lk-goc-travis`; fetch simplificado ainda não extraiu o bloco completo. Sem `Liquid error`.
- `https://lksneakers.com.br/collections/air-jordan-travis-scott`: Admin/template OK, mas storefront público ainda serviu versão sem bloco no readback imediato. Sem `Liquid error`. Requer revalidação CDN/edge.

## Rollback

Snapshots:
- `snapshots-before/`
- `theme-snapshots-before-visible/`

Rollback recomendado:
1. Restaurar `templates/llms.txt.liquid` e `templates/agents.md.liquid` a partir de `snapshots-before/`.
2. Restaurar `collection__air-jordan-travis-scott.html` e `page__air-jordan-travis-scott-original-brasil-guia-lk.html`.
3. Restaurar `templates/collection.json` a partir de `theme-snapshots-before-visible/templates__collection.json`.
4. Voltar `page.template_suffix` para `geo-source-d` usando snapshot `theme-snapshots-before-visible/page__air-jordan-travis-scott-original-brasil-guia-lk.meta.json`.
5. Opcional: remover assets novos `sections/lk-travis-scott-ai-visibility-v4.liquid`, `sections/lk-travis-scott-guide-ai-visibility-v4.liquid` e `templates/page.travis-scott-ai-v4.json` após rollback.

## Status final

Publicado em Admin e source maps públicos.
Storefront visível com cache parcial nas páginas collection/guia; revalidação recomendada em 1–24h.
Impact review D+7: 2026-06-25.
