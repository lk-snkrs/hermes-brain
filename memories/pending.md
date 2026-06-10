# Pending Tasks — Hermes Brain

Última revisão: 2026-05-16
Última revisão: 2026-05-19
Última revisão: 2026-06-09
Fonte executiva detalhada: `empresa/gestao/pendencias.md`

## Ativos agora

- [ ] Aprofundar dicionário canônico de influencers/campanhas LK e auditar match influencer → produto — usar evidências Shopify/Meta/UTM/cupom; Silvia/Helena têm ROAS operacional provisório, Lala segue ambígua.
- [ ] Reconciliar Mission Control em rodada dedicada — ponte documental criada em `areas/operacoes/projetos/mission-control-reconciliation-pointer-2026-05-19.md`; detalhar ativo/legado/benchmark/próximos módulos sem repo/UI/runtime nesta rodada.
- [x] Primeiro Stock Intelligence real/read-only da LK com sourcing acionado por sinal — relatório `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`; sem WhatsApp, Notion, compra ou alteração produtiva.
- [x] Criar mapa canônico SKU Shopify ↔ Tiny — preview read-only `reports/lk-sku-shopify-tiny-map-preview-2026-05-10.md`; 6/6 campeões antes sem match tiveram candidato Tiny com confiança alta; tabela de aprovação para alias/correção gerada em `reports/lk-sku-tiny-alias-approval-preview-2026-05-10.md`; sem write produtivo.
- [x] Investigar/corrigir leitura dos ROAS Meta 50–70x de influencers — relatório `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`; 50–70x é Meta attributed ROAS, não ROAS operacional LK.
- [x] Calcular ROAS atribuído por título de campanha Meta — relatório `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`; separa Meta attributed ROAS por `campaign_name` de Shopify UTM evidence com matching estrito.
- [ ] Aprofundar dicionário canônico de influencers/campanhas LK e auditar match influencer → produto: v0.2 gerou `reports/lk-influencer-operational-roas-v02-2026-05-10.md`; Silvia 12,93x e Helena 6,34x como ROAS operacional provisório com evidência Shopify; Lala segue ambígua sem evidência Shopify direta. Próxima ação: confirmar handles/cupons/UTMs oficiais e gerar tabela influencer → produto/SKU/tamanho → estoque para Silvia/Helena.
- [ ] Completar subdocs de integrações adicionais somente quando virarem fluxo recorrente real.
- [ ] Adicionar Customer Trust & Loyalty ao LK OS — Rivo/LK Rewards/Judge.me primeiro em read-only/modelagem; sem cupons, review changes, campanhas ou writes.
- [ ] Mapear captura de aniversário no Shopify/checkout/customer profile da LK — preparar opções/UX/plano; sem implementação sem aprovação.

## Bloqueados — aprovação Lucas

- [ ] Rotação de senha root da `lc.vps`, se desejado — infra sensível.
- [ ] Decidir se a chave SSH dedicada da VPS permanece ou será removida.
- [ ] Correção ativa do alerta/divergência Gateway Hermes — restart/update/Docker/VPS exigem aprovação.
- [ ] Mission Control visual ou cron recorrente — exige aprovação de escopo/cadência. Memory OS card/fonte `mission-memory-os` fica pendente por decisão de Lucas em 2026-06-09.
- [ ] Campanhas, WhatsApp, email, posts, contatos externos e ações produtivas — sempre com preview/aprovação.

## Aguardando data/evento

- [ ] Revisão mensal/arquivamento de pendências antigas — próximo check recomendado 2026-05-26.
- [ ] SPITI email poller/monitor — reavaliar quando houver novo leilão ou necessidade operacional.

## Concluídos / retirados da fila ativa

- [x] Agente LC Hermes: rotina canônica `areas/operacoes/rotinas/brain-fonte-viva-e-dados-grandes.md` criada em 2026-06-09 a partir do handoff `areas/operacoes/handoffs/handoff-lc-hermes-brain-fonte-viva-governance-20260609T000522Z.md`; MAPA indexado; matriz Brain vs fonte viva e checklist para PRDs/ingests/subagentes/Mission Control incluídos. Receipt: `areas/operacoes/receipts/brain-fonte-viva-e-dados-grandes-20260609.md`.
- [x] Primeira revisão sob demanda com a nova identidade Hermes Geral — relatório gerado em `reports/revisao-operacional-multiempresa-hermes-geral-2026-05-16.md`; escopo Hermes/Infra, LK OS, Zipper e SPITI; sem cron novo, contato externo, deploy ou write produtivo.
- [x] Adaptação Amora → Hermes Geral — DOCX convertidos, `IDENTITY.md` criado, `SOUL/AGENTS/HEARTBEAT` consolidados, `MAPA.md` raiz criado, raiz `AGENTS.md`/`HEARTBEAT.md` higienizada para Hermes-native; sem cron novo. Evidência: `areas/operacoes/rotinas/amora-templates-hermes-geral-adaptacao-2026-05-16.md` e `reports/amora-reference-ingest-2026-05-16/`.
- [x] Preservação do `spiti-hub` antigo não-git — evidências copiadas para `reports/spiti-hub-diff-2026-05-16/old-nongit-preservation/`; secret scan limpo; não mergear fontes antigas no `spiti-hub-git`.
- [x] Limpeza de 43 worktrees do Brain — pacotes exportados em `reports/brain-worktrees-2026-05-16/`; worktrees removidos; branches internas preservadas.
- [x] Hermes v0.13/v0.14 pós-deploy operacionalizado em documentação/read-only; runtime/infra mutável continua approval-gated.
- [x] Gaps P0 documentais BRUNO-ATUAL — criados `memories/current.md`, `areas/operacoes/rotinas/runtime-profile-channel-inventory-2026-05-19.md`, `empresa/skills/skill-audit-2026-05-19.md` e `agentes/mordomo/`; sem Docker/VPS/runtime/API/envio externo/credenciais. Mission Control detalhado ficou como pendência dedicada.

- [x] Hermes v0.13 pós-deploy operacionalizado — release watch atualizado, `/goal`/Kanban/`no_agent` documentados, board LK Growth Ops criado em modo seguro, watchdogs `edd06fe19397` e `e7a61e275c37` ativos, e learning loop de aprovações documentado; workers amplos/dashboard público continuam bloqueados por aprovação.
- [x] Script local/read-only de retomada de planos/PRDs — criado em 2026-05-09 com relatório `reports/retomada-planos-prds-2026-05-09.md`; cron recorrente não criado.
- [x] Script executivo local/read-only para `brain-improvement-score.md` — criado em 2026-05-09; sem cron/UI/runtime.
- [x] Rodada G — Health checks do Brain — script expandido, rotina atualizada e relatório JSON gerado em 2026-05-09.
- [x] Mission Control / Bruno — extração/adaptação/PRD documental concluídos; UI/cron seguem fora de escopo.

## Nota de higiene

Não usar este arquivo como log de sessão. Toda pendência precisa ter status, próxima ação e evidência. Detalhes longos ficam em `empresa/gestao/pendencias.md`, `areas/`, `reports/`, `CHANGELOG.md` ou `memories/lessons.md`.
