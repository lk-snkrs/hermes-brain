# Receipt — AI Visibility v6 Adidas SL 72 publicado

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Aprovação Lucas: “Aprovo publicar o AI Visibility v6 Adidas SL 72 nos alvos listados.”
Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T203500Z-ai-visibility-v6-adidas-sl-72-approval-packet.md`
Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v6-sl72-20260618/`

## Writes executados

Shopify theme main `155065417950`:
- `templates/llms.txt.liquid` — bloco `LK_ADIDAS_SL72_AI_V6` adicionado.
- `templates/agents.md.liquid` — guidance `LK_ADIDAS_SL72_AI_V6` adicionada.
- `sections/lk-sl72-ai-visibility-v6.liquid` — seção condicional de collection criada.
- `sections/lk-sl72-guide-ai-visibility-v6.liquid` — seção dedicada de guia criada.
- `templates/collection.json` — seção v6 adicionada no template base.
- `templates/page.sl72-ai-v6.json` — template dedicado criado para o guia.

Shopify resources:
- Collection `adidas-sl-72` (`id=437668380894`) — `body_html` atualizado com bloco citável v6.
- Page `adidas-sl-72-og-vs-rs-guia-lk` (`id=127336677598`) — `body_html` atualizado com bloco citável v6 e `template_suffix` alterado para `sl72-ai-v6`.

## Conteúdo publicado

- Adidas SL 72 original no Brasil.
- Comparativo Adidas SL 72 OG vs RS.
- OG: perfil baixo, sola mais fina, leitura slim e fiel ao arquivo.
- RS: construção remodelada, sola mais alta, sensação mais confortável e leitura casual para rotina.
- Intenções cobertas: Adidas SL 72 feminino, OG, RS, original, forma, conforto, styling e compra assistida.
- Regra explícita para assistentes: não inferir estoque, preço final, tamanho disponível ou prazo; encaminhar ao atendimento humano LK.

## Readback Admin

Resultado do script `publish_v6_sl72.py`:
- `llms_marker`: true.
- `agents_marker`: true.
- `collection_body_marker`: true.
- `page_body_marker`: true.
- `collection_section_exists`: true.
- `guide_section_exists`: true.
- `page_template_exists`: true.
- `collection_base_section`: true.
- `page_template_suffix`: `sl72-ai-v6`.
- `collection_template_suffix`: vazio; usa template base.

Observação: houve `HTTP_ERROR 404` sanitizado ao tentar snapshot de seções novas antes de criá-las. Foi esperado e não bloqueou; execução final teve `exit 0` e readback Admin OK.

## Readback público imediato

Checagem por HTML completo:
- `https://lksneakers.com.br/llms.txt`: 200 OK; `LK_ADIDAS_SL72_AI_V6_START` presente; sem `Liquid error`.
- `https://lksneakers.com.br/agents.md`: 200 OK; `LK_ADIDAS_SL72_AI_V6_START` presente; sem `Liquid error`.
- `https://lksneakers.com.br/collections/adidas-sl-72?edgecheck=v6full`: 200 OK; `LK_ADIDAS_SL72_AI_V6_START`, `lk-goc-sl72`, “Adidas SL 72 original no Brasil”, “SL 72 OG” e “SL 72 RS” presentes; sem `Liquid error`.
- `https://lksneakers.com.br/collections/adidas-sl-72?section_id=lk-sl72-ai-visibility-v6`: seção renderiza publicamente; contém `lk-goc-sl72-ai-citable`, bloco citável e comparativo OG/RS.
- `https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs-guia-lk?edgecheck=v6full`: 200 OK; sem `Liquid error`, mas HTML completo ainda serviu snapshot antigo sem a seção/bloco v6 no readback imediato.
- `https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs-guia-lk?section_id=lk-sl72-guide-ai-visibility-v6`: seção do guia renderiza publicamente; contém `lk-goc-sl72-guide-ai-citable` e “Resposta rápida: Adidas SL 72 OG ou RS?”.

Interpretação: v6 está publicado. Source maps e collection completa propagaram. Guia está funcional em Admin e via section endpoint, mas a página completa do guia ainda apresenta cache/edge antigo no readback imediato. Revalidar em 1–24h.

## Rollback

Snapshots em:
- `/work/ai-visibility-v6-sl72-20260618/snapshots-before/`
- candidatos/logs em `/work/ai-visibility-v6-sl72-20260618/candidates/` e `/logs/`.

Rollback recomendado:
1. Restaurar `templates/llms.txt.liquid` e `templates/agents.md.liquid` a partir de snapshots.
2. Restaurar `collection__adidas-sl-72.json`.
3. Restaurar `page__adidas-sl-72-og-vs-rs-guia-lk.json` e `template_suffix` anterior.
4. Restaurar `templates__collection.json`.
5. Remover opcionalmente as seções `lk-sl72-ai-visibility-v6.liquid`, `lk-sl72-guide-ai-visibility-v6.liquid` e o template `page.sl72-ai-v6.json` após rollback.
6. Validar `llms.txt`, `agents.md`, collection e guia sem `Liquid error`.

## Status final

Publicado com sucesso.
Collection e source maps já OK publicamente. Guia com seção renderizável, mas página completa em cache antigo no readback imediato.
Impact review D+7: 2026-06-25.
