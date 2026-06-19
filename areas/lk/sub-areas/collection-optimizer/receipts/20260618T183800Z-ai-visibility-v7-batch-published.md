# Receipt — AI Visibility v7 Batch publicado

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Aprovação Lucas: “Aprovo executar o Batch v7 de 10 melhorias AI Visibility, com templates dedicados e rollback.”

## Escopo executado

1. Hotfix escopo SL72 — executado antes do batch e registrado em receipt próprio.
2. Source maps v7 em `llms.txt` e `agents.md`.
3. Adidas Samba main hub.
4. New Balance 204L.
5. Nike Vomero Premium.
6. Nike Mind 001/002.
7. Crocs Relâmpago McQueen.
8. Onitsuka Tiger / Mexico 66.
9. Nike x Jacquemus Moon Shoe.
10. QA checker anti-inferência criado e executado.

## Princípio técnico usado

- Nenhum bloco de cluster específico foi mantido no `templates/collection.json` global.
- Cada collection com bloco visual recebeu template dedicado `collection.<cluster>-ai-v7.json`.
- Cada guia/page recebeu template dedicado `page.<cluster>-ai-v7.json` quando aplicável.
- CSS isolado por namespace `lk-goc-*`.
- Snapshots antes dos writes salvos em `work/ai-visibility-v7-batch-20260618/snapshots-before/`.

## Admin readback

- `llms_marker`: true em asset/admin.
- `agents_marker`: true em asset/admin.
- Templates/sections criados:
  - `sections/lk-samba-ai-visibility-v7.liquid`
  - `sections/lk-nb204l-ai-visibility-v7.liquid`
  - `sections/lk-vomero-premium-ai-visibility-v7.liquid`
  - `sections/lk-nike-mind-ai-visibility-v7.liquid`
  - `sections/lk-crocs-mcqueen-ai-visibility-v7.liquid`
  - `sections/lk-onitsuka-ai-visibility-v7.liquid`
  - `sections/lk-jacquemus-moon-ai-visibility-v7.liquid`
- Collections com `template_suffix` dedicado:
  - Adidas Samba: `samba-ai-v7`
  - New Balance 204L: `nb204l-ai-v7`
  - Nike Vomero Premium: `vomero-premium-ai-v7`
  - Nike Mind 001: `nike-mind-ai-v7`
  - Onitsuka Tiger todos os modelos: `onitsuka-ai-v7`
  - Nike x Jacquemus Moon Shoe SP: `jacquemus-moon-ai-v7`
- Pages com `template_suffix` dedicado:
  - Guia Adidas Samba: `samba-ai-v7`
  - Guia New Balance 204L: `nb204l-ai-v7`
  - Guia Nike Vomero Premium: `vomero-premium-ai-v7`
  - Guia Nike Mind 001/002: `nike-mind-ai-v7`
  - Guia Crocs Relâmpago McQueen: `crocs-mcqueen-ai-v7`
  - Guia Onitsuka Tiger: `onitsuka-ai-v7`
  - Guia Nike x Jacquemus Moon Shoe: `jacquemus-moon-ai-v7`

## Readback público

### Source maps

- `https://lksneakers.com.br/llms.txt`: contém “LK AI Visibility v7”, Adidas Samba, New Balance 204L e guardrail anti-inferência.
- `https://lksneakers.com.br/agents.md`: contém “LK AI Visibility v7”, Adidas Samba, New Balance 204L e guardrail anti-inferência.

Observação técnica: a primeira tentativa escreveu em assets simples; a correção aplicou também nos templates públicos `templates/llms.txt.liquid` e `templates/agents.md.liquid`, que são as chaves realmente servidas no root público.

### Blocos visuais / templates

Readback imediato por HTML completo:
- Adidas Samba collection: v7 presente; sem `Liquid error`; sem vazamento de outros clusters.
- Nike Vomero Premium collection/page: v7 presente; sem `Liquid error`.
- Nike Mind collection/page: v7 presente; sem `Liquid error`.
- Onitsuka collection/page: v7 presente; sem `Liquid error`.
- New Balance 204L page: v7 presente; collection ainda pode estar em edge/cache parcial.
- Nike x Jacquemus page: v7 presente; collection ainda pode estar em edge/cache parcial.
- Crocs page: template/section publicados; HTML completo ainda pode estar em edge/cache parcial.

Readback por `section_id` confirmou funcionamento das seções que ainda estavam em cache na página completa:
- Guia Adidas Samba section: OK.
- New Balance 204L collection section: OK.
- Crocs McQueen page section: OK.
- Jacquemus Moon collection section: OK.

## QA anti-inferência

Arquivo criado:
`work/ai-visibility-v7-batch-20260618/qa_checker_ai_visibility.py`

Execução pública salva em:
`work/ai-visibility-v7-batch-20260618/logs/qa_checker_public.json`

Resultado:
- Sem `Liquid error` em todos os alvos testados.
- Termo “preço final” aparece em vários alvos porque os próprios blocos v7 dizem que assistentes **não devem inferir preço final**. Isso é guardrail, não promessa comercial.

## Arquivos principais

- Executor: `work/ai-visibility-v7-batch-20260618/publish_v7_batch.py`
- Admin readback: `work/ai-visibility-v7-batch-20260618/logs/admin_readback.json`
- Source map fix readback: `work/ai-visibility-v7-batch-20260618/logs/source_maps_fix_readback.json`
- Snapshots/rollback: `work/ai-visibility-v7-batch-20260618/snapshots-before/`

## Rollback

Rollback possível usando os snapshots salvos antes do batch:
- restaurar templates dedicados/anteriores;
- restaurar `templates/llms.txt.liquid` e `templates/agents.md.liquid`;
- restaurar `template_suffix` de collections/pages pelos JSON snapshots;
- remover/ignorar seções v7 dedicadas se necessário.

## Pendências de monitoramento

- Revalidar em 1–24h as páginas completas que estavam em cache parcial:
  - `/collections/new-balance-204l`
  - `/collections/nike-x-jacquemus-moon-shoe-sp`
  - `/pages/crocs-relampago-mcqueen-guia`
  - `/pages/guia-adidas-samba`
- Fazer Impact Review D+7 em 2026-06-25.
