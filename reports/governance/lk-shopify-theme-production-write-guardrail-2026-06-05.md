# Receipt — LK Shopify Theme Production Write Guardrail

Data: 2026-06-05
Status: documented / local-only / no external writes

## Regra registrada

Lucas corrigiu a governança de alterações de tema Shopify:

- Nunca escrever diretamente no tema Shopify de produção/live para Liquid, CSS, JS, section, snippet, asset ou app-embed surface.
- Alterações de tema devem seguir: dev theme/branch → GitHub PR/review → merge/deploy/readback/QA/receipt.
- Produto, coleção e catálogo são outra classe de write: podem fazer sentido via Shopify quando o playbook próprio permitir, mas ainda exigem approval escopada, preview, rollback e readback.

## Onde foi registrado

- Memória boot do Hermes Geral atualizada.
- Memória do profile `lk-shopify` atualizada.
- Memória do profile `lk-growth` atualizada.
- Brain Shopify `areas/lk/sub-areas/shopify/MEMORY.md` atualizado.
- Skill global `shopify` atualizada.
- Skills/refs LK Shopify e LK Growth atualizadas para bloquear write direto no tema live.
- Cópias herdadas da referência `lk-shopify-readonly` em perfis relacionados (`mordomo`, `lk-ops`, `lk-trends`, `spiti`, `lk-collection-optimizer`) corrigidas para não ensinar upload/copy direto no tema live.
- Referência `shopify-theme-dev-cro-preview-20260515.md` corrigida em todas as cópias encontradas para trocar a antiga sequência de promoção por produção via upload direto por: evidência/readback → diff/branch → GitHub PR/review → merge/deploy → readback/QA/receipt.
- Playbook de correção de tema e Worker OS do LK Shopify atualizados.

## Ações externas

Nenhuma. Não houve write em Shopify, GitHub, tema, Tiny, GMC, Docker, VPS ou Gateway.

## Implicação operacional

Se uma demanda envolver tema Shopify, o agente deve preparar preview/diff/PR e não executar Asset API/Admin write direto no tema live. Se a demanda envolver produto/coleção/catálogo, usar o playbook correspondente e approval própria.
