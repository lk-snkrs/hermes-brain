# Pending Tasks — Hermes Brain

Última revisão: 2026-05-09
Fonte executiva detalhada: `empresa/gestao/pendencias.md`

## Ativos

- [x] Primeiro Stock Intelligence real/read-only da LK com sourcing acionado por sinal — relatório `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`; sem WhatsApp, Notion, compra ou alteração produtiva.
- [x] Criar mapa canônico SKU Shopify ↔ Tiny — preview read-only `reports/lk-sku-shopify-tiny-map-preview-2026-05-10.md`; 6/6 campeões antes sem match tiveram candidato Tiny com confiança alta; tabela de aprovação para alias/correção gerada em `reports/lk-sku-tiny-alias-approval-preview-2026-05-10.md`; sem write produtivo.
- [x] Investigar/corrigir leitura dos ROAS Meta 50–70x de influencers — relatório `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`; 50–70x é Meta attributed ROAS, não ROAS operacional LK.
- [x] Calcular ROAS atribuído por título de campanha Meta — relatório `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`; separa Meta attributed ROAS por `campaign_name` de Shopify UTM evidence com matching estrito.
- [ ] Preencher dicionário canônico de influencers/campanhas LK e auditar match influencer → produto, começando por Lala Noleto, Silvia Heinz e Helena Lunardelli; calcular ROAS operacional só com Shopify evidence/cupom/UTM/landing/produto + custo relacionado, checando campaign/adset/ad/título de campanha e janela real.
- [ ] Completar subdocs de integrações adicionais somente quando virarem fluxo recorrente real.

## Bloqueados — aprovação Lucas

- [ ] Rotação de senha root da `lc.vps`, se desejado — infra sensível.
- [ ] Decidir se a chave SSH dedicada da VPS permanece ou será removida.
- [ ] Correção ativa do alerta/divergência Gateway Hermes — exige aprovação antes de restart/update/Docker/VPS.
- [ ] Mission Control visual ou cron recorrente — exige aprovação de escopo/cadência.
- [ ] Campanhas, WhatsApp, email, posts, contatos externos e ações produtivas — sempre com preview/aprovação.

## Aguardando data/evento

- [ ] `Hermes release watch` — próximo run 2026-05-11 09:00 UTC; post-check 09:15 UTC.
- [ ] Revisão mensal/arquivamento de pendências antigas — próximo check recomendado 2026-05-26.
- [ ] SPITI email poller/monitor — reavaliar quando houver novo leilão ou necessidade operacional.

## Concluídos / retirados da fila ativa

- [x] Script local/read-only de retomada de planos/PRDs — criado em 2026-05-09 com relatório `reports/retomada-planos-prds-2026-05-09.md`; cron recorrente não criado.
- [x] Script executivo local/read-only para `brain-improvement-score.md` — criado em 2026-05-09 com relatório `reports/brain-improvement-score-2026-05-09-script.md`; sem cron/UI/runtime.
- [x] Teste `material-ingest-to-prd.md` em PRD antigo — modo leve validado em 2026-05-09 com relatório `reports/material-ingest-to-prd-test-2026-05-09.md`.
- [x] Rodada G — Health checks do Brain — script expandido, rotina atualizada e relatório JSON gerado em 2026-05-09.
- [x] Mission Control / Bruno — extração/adaptação/PRD documental concluídos; UI/cron seguem fora de escopo.
- [x] Hermes Brain Improvement System P0 — PR #2 mergeado no `main`.
- [x] Guardrails P1 — PR #4 mergeado no `main`.
- [x] Meta Ads token — resolvido em 2026-04-25 segundo `memories/consolidation_weekly/2026-04-28.md`; não é urgente atual sem nova evidência.
- [x] Data gap Supabase LK e Shopify missing orders — resolvidos em 2026-04-25 segundo consolidação.

## Nota de higiene

Não usar este arquivo como log de sessão. Toda pendência precisa ter status, próxima ação e evidência. Detalhes longos ficam em `empresa/gestao/pendencias.md`, `areas/`, `reports/`, `CHANGELOG.md` ou `memories/lessons.md`.
