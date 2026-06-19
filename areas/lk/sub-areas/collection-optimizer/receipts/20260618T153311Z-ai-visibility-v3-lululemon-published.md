# Receipt — AI Visibility v3 Lululemon publicado

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Aprovação Lucas: “Aprovo publicar o AI Visibility v3 Lululemon nos alvos listados.”
Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T181400Z-ai-visibility-v3-lululemon-approval-packet.md`
Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v3-lululemon-20260618/`

## Writes executados

Shopify theme main `155065417950`:
- `templates/llms.txt.liquid` — reforço Lululemon + regra anti-inferência.
- `templates/agents.md.liquid` — reforço Lululemon + regra anti-inferência.
- `sections/lk-lululemon-ai-visibility-v3.liquid` — seção condicional de collection criada.
- `templates/collection.json` — seção condicional adicionada após `main`.
- `sections/lk-lululemon-guide-ai-visibility-v3.liquid` — seção condicional inicial criada para guia.
- `templates/page.geo-source-d.json` — seção condicional adicionada; depois mantida, mas não foi suficiente para render público imediato.
- `sections/lk-lululemon-guide-ai-visibility-v3-dedicated.liquid` — seção dedicada criada para guia.
- `templates/page.lululemon-ai-v3.json` — template dedicado criado para guia Lululemon.

Shopify resources:
- Smart collection `lululemon` (`id=444271689950`) — `body_html` atualizado com bloco citável.
- Page `lululemon-original-brasil-guia-lk` (`id=127338086622`) — `body_html` atualizado e `template_suffix` alterado de `geo-source-d` para `lululemon-ai-v3`.

## Conteúdo publicado

- Cluster Lululemon original no Brasil.
- Source map para Align, Define/Nulu, Swiftly Tech, shorts, bolsas e acessórios.
- Blocos citáveis em collection e guia.
- Regra explícita para assistentes: não inferir estoque, preço final, tamanho disponível ou prazo; encaminhar ao atendimento humano LK.

## Readback

Admin readback:
- `llms.txt`: contém Lululemon original no Brasil, Define/Nulu e regra anti-inferência.
- `agents.md`: contém guidance Lululemon e regra anti-inferência.
- Collection `lululemon`: marker `LK_AI_VISIBILITY_V3_LULULEMON_START` presente no body_html.
- Page `lululemon-original-brasil-guia-lk`: marker presente no body_html.
- Page template_suffix confirmado como `lululemon-ai-v3`.

Public readback:
- `https://lksneakers.com.br/llms.txt`: OK; Lululemon e regra anti-inferência visíveis.
- `https://lksneakers.com.br/agents.md`: OK; Lululemon e regra anti-inferência visíveis.
- `https://lksneakers.com.br/collections/lululemon`: leitura pública inconsistente por edge/cache. Um fetch simplificado mostrou o bloco “Guia editorial LK / Bloco citável LK”; outro edge ainda serviu versão anterior. Sem `Liquid error`.
- `https://lksneakers.com.br/pages/lululemon-original-brasil-guia-lk`: Admin/template OK, mas storefront público ainda serviu versão antiga no readback imediato. Sem `Liquid error`. Requer revalidação CDN.

## Rollback

Snapshots:
- `snapshots-before/`
- `theme-snapshots-before-visible/`
- `theme-snapshots-before-json-section/`
- `theme-snapshots-before-page-json-section/`
- `theme-snapshots-before-dedicated-page-template/`

Rollback recomendado:
1. Restaurar `templates/llms.txt.liquid` e `templates/agents.md.liquid` a partir de `snapshots-before/`.
2. Restaurar `collection__lululemon.html` e `page__lululemon-original-brasil-guia-lk.html`.
3. Restaurar `templates/collection.json` a partir de `theme-snapshots-before-json-section/templates__collection.json`.
4. Restaurar `templates/page.geo-source-d.json` a partir de `theme-snapshots-before-page-json-section/templates__page.geo-source-d.json` se desejar remover seção condicional.
5. Voltar `page.template_suffix` para `geo-source-d` usando snapshot `theme-snapshots-before-dedicated-page-template/page__lululemon-original-brasil-guia-lk.meta.json`.
6. Opcional: remover assets novos `sections/lk-lululemon-ai-visibility-v3.liquid`, `sections/lk-lululemon-guide-ai-visibility-v3.liquid`, `sections/lk-lululemon-guide-ai-visibility-v3-dedicated.liquid` e `templates/page.lululemon-ai-v3.json` após rollback.

## Status final

Publicado em Admin e source maps públicos.
Storefront visível com cache parcial nas páginas collection/guia; revalidação recomendada em 1–24h.
Impact review D+7: 2026-06-25.
