# Targeted follow-up packet — Samba OG Cream White Core Black

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme / PDP Curadoria LK
- **Handle:** `tenis-adidas-samba-og-cream-white-core-black-bege`
- **Status:** monitor atrasado confirmou persistência do problema público; nenhum novo write executado neste packet.

## Histórico

- PR #90 mergeou o split snippet do batch Curadoria Bestsellers 1–3.
- PR #91 aplicou repair inline focado nos 6 handles descobertos.
- Shopify Admin/Asset API readback do PR #91 passou para:
  - `sections/lk-pdp.liquid`
  - `snippets/lk-variante-top30-visited-v2.liquid`
- Public QA pós-repair mostrou 5/6 handles OK/intermitentes e controles 7/7 sem duplicidade.

## Monitor atrasado

Processo: `proc_97d3af806980`

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/followup/20260625T104827Z_cream_white_delayed_monitor.json`

Resultado:

- Delay inicial: 10 minutos.
- Tentativas: 6.
- Intervalo: 60s.
- Resultado: **0/6 com marker** `repair-samba-og-bestsellers-20260625`.

## Interpretação

O problema agora está isolado em 1 PDP. Como o source/readback do tema está correto e outros produtos do mesmo bloco renderizam, há duas hipóteses prováveis:

1. **cache/edge persistente por rota/produto** — o HTML público desse handle está servindo versão antiga da section;
2. **render path específico do produto** não visível via `templateSuffix` Admin, mas que pula ou substitui parte da section.

Não há evidência de falha global do repair. Também não há evidência para rollback: reverter PR #91 quebraria os 5 handles que melhoraram.

## Opções seguras

### Opção A — Monitorar mais, sem write

- Aguardar nova janela e repetir QA focado.
- Menor risco.
- Mantém 5/6 ganhos e evita mexer em produção por um possível cache tardio.

### Opção B — Targeted theme follow-up via GitHub PR

- Preparar um PR ainda mais específico só para o handle `tenis-adidas-samba-og-cream-white-core-black-bege`.
- Objetivo: aumentar a chance de invalidar/cachear a rota e/ou renderizar o bloco em uma posição ainda mais explícita.
- Risco: se o problema for cache antigo agressivo, outro theme merge pode continuar sem efeito imediato.
- Não deve mexer nos 5 handles já OK.

### Opção C — Product-level cache nudge

- Um write mínimo no produto poderia forçar atualização de cache por produto, mas é **Shopify product write**, não theme write.
- Não recomendado sem justificativa forte e aprovação separada, porque não altera conteúdo real e pode tocar metadata/updatedAt.

## Recomendação

Recomendo **Opção A por enquanto**: não fazer novo write imediato. O benefício marginal de outro theme PR é baixo se a causa for cache/edge por rota.

Se Lucas quiser tentar mesmo assim, aprovação necessária:

`Aprovo targeted theme follow-up Cream White Curadoria`

Escopo dessa aprovação: preparar e executar um PR GitHub/Production **somente** para o handle Cream White, sem produto/estoque/preço/metafield/campanha.

## Rollback se Opção B for executada

- Reverter o PR targeted.
- Confirmar Shopify readback.
- Revalidar Cream White + os 5 handles OK + 7 controles sem duplicidade.
