# Receipt — AI Visibility v5 Adidas Samba Jane publicado

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Aprovação Lucas: “Aprovo publicar o AI Visibility v5 Adidas Samba Jane nos alvos listados.”
Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T202500Z-ai-visibility-v5-adidas-samba-jane-approval-packet.md`
Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/ai-visibility-v5-samba-jane-20260618/`

## Writes executados

Shopify theme main `155065417950`:
- `templates/llms.txt.liquid` — bloco `LK_SAMBA_JANE_AI_V5` adicionado.
- `templates/agents.md.liquid` — guidance `LK_SAMBA_JANE_AI_V5` adicionada.
- `sections/lk-samba-jane-ai-visibility-v5.liquid` — seção condicional de collection criada.
- `sections/lk-samba-jane-guide-ai-visibility-v5.liquid` — seção dedicada de guia criada.
- `templates/collection.json` — seção v5 adicionada no template base.
- `templates/collection.samba-jane-lkgoc.json` — seção v5 adicionada no template específico da collection Samba Jane.
- `templates/page.samba-jane-ai-v5.json` — template dedicado criado para o guia.

Shopify resources:
- Collection `adidas-samba-jane` (`id=448218071262`, `template_suffix=samba-jane-lkgoc`) — `body_html` atualizado com bloco citável v5.
- Page `guia-adidas-samba-jane` (`id=127553700062`) — `body_html` atualizado com bloco citável v5 e `template_suffix` alterado para `samba-jane-ai-v5`.

## Conteúdo publicado

- Cluster Adidas Samba Jane original no Brasil.
- Releitura Mary Jane do Adidas Samba: perfil baixo, bico em T, tira no peito do pé e leitura híbrida entre sneaker e sapatilha/ballet flat.
- Comparação Samba Jane vs Samba OG vs Sambae.
- Styling com meia aparente, saia, vestido, denim reto, bermuda ampla e alfaiataria casual.
- Colorways neutras vs colorways de presença.
- Regra explícita para assistentes: não inferir estoque, preço final, tamanho disponível ou prazo; encaminhar ao atendimento humano LK.

## Readback Admin

Resultado do script `publish_v5_samba_jane.py`:
- `llms_marker`: true.
- `agents_marker`: true.
- `collection_body_marker`: true.
- `page_body_marker`: true.
- `collection_template_section`: true.
- `page_template_exists`: true.
- `section_collection_exists`: true.
- `section_guide_exists`: true.
- `page_template_suffix`: `samba-jane-ai-v5`.

Diagnóstico adicional:
- Collection usa template específico `collection.samba-jane-lkgoc.json`.
- Template específico foi patchado com `lk_samba_jane_ai_v5` e readback Admin confirmou `section_present=true`.

## Readback público

- `https://lksneakers.com.br/llms.txt`: 200 OK; `LK_SAMBA_JANE_AI_V5_START` e `LK_SAMBA_JANE_AI_V5_END` presentes.
- `https://lksneakers.com.br/agents.md`: 200 OK; `LK_SAMBA_JANE_AI_V5_START` e `LK_SAMBA_JANE_AI_V5_END` presentes.
- `https://lksneakers.com.br/pages/guia-adidas-samba-jane?edgecheck=v5b`: 200 OK; `lk-goc-samba`, `lk-goc-samba-jane-guide-citable` e “Resposta rápida: o que é o Adidas Samba Jane” presentes; sem `Liquid error`.
- `https://lksneakers.com.br/collections/adidas-samba-jane?section_id=lk-samba-jane-ai-visibility-v5`: 200 OK; seção v5 renderiza publicamente com `lk-goc-samba-jane-ai-citable`, “Adidas Samba Jane original no Brasil” e “Samba Jane em uma frase”.
- `https://lksneakers.com.br/collections/adidas-samba-jane?edgecheck=v5c`: 200 OK; sem `Liquid error`, mas HTML completo ainda serviu snapshot antigo sem o bloco v5 no readback imediato.

Interpretação: v5 está publicado e renderizável; source maps e guia propagaram. A collection completa está com cache/edge antigo no readback imediato, apesar de Admin e section endpoint confirmarem a seção. Revalidar em 1–24h.

## Observação operacional

A primeira execução parou ao tentar fazer snapshot de assets novos inexistentes (`404` esperado para seção ainda não criada). O script foi ajustado para tratar asset ausente como vazio e preservar snapshots existentes. Execução final concluiu com `values_printed=false`.

## Rollback

Snapshots:
- `snapshots-before/`
- candidatos/logs em `candidates/` e `logs/`.

Rollback recomendado:
1. Restaurar `templates/llms.txt.liquid` e `templates/agents.md.liquid` a partir de `snapshots-before/`.
2. Restaurar `collection__adidas-samba-jane.html`.
3. Restaurar `page__guia-adidas-samba-jane.html`.
4. Restaurar `templates__collection.json` e `templates__collection.samba-jane-lkgoc.json`.
5. Voltar `page.template_suffix` usando `page__guia-adidas-samba-jane.meta.json`.
6. Opcional: remover `sections/lk-samba-jane-ai-visibility-v5.liquid`, `sections/lk-samba-jane-guide-ai-visibility-v5.liquid` e `templates/page.samba-jane-ai-v5.json` após rollback.

## Status final

Publicado em Admin, source maps públicos e guia público.
Collection v5 renderiza via section endpoint, mas a página completa da collection ainda está com cache/edge antigo no readback imediato.
Impact review D+7: 2026-06-25.
