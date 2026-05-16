# Pending Tasks — Hermes Brain

Última revisão: 2026-05-16
Fonte executiva detalhada: `empresa/gestao/pendencias.md`

## Ativos agora

- [ ] Rodar primeira revisão sob demanda com a nova identidade Hermes Geral — escopo: Hermes/Infra, LK OS, Zipper e SPITI; gerar relatório interno em `reports/`; sem cron, contato externo, deploy ou write produtivo.
- [ ] Aprofundar dicionário canônico de influencers/campanhas LK e auditar match influencer → produto — usar evidências Shopify/Meta/UTM/cupom; Silvia/Helena têm ROAS operacional provisório, Lala segue ambígua.
- [ ] Completar subdocs de integrações adicionais somente quando virarem fluxo recorrente real.
- [ ] Adicionar Customer Trust & Loyalty ao LK OS — Rivo/LK Rewards/Judge.me primeiro em read-only/modelagem; sem cupons, review changes, campanhas ou writes.
- [ ] Mapear captura de aniversário no Shopify/checkout/customer profile da LK — preparar opções/UX/plano; sem implementação sem aprovação.

## Bloqueados — aprovação Lucas

- [ ] Rotação de senha root da `lc.vps`, se desejado — infra sensível.
- [ ] Decidir se a chave SSH dedicada da VPS permanece ou será removida.
- [ ] Correção ativa do alerta/divergência Gateway Hermes — restart/update/Docker/VPS exigem aprovação.
- [ ] Mission Control visual ou cron recorrente — exige aprovação de escopo/cadência.
- [ ] Campanhas, WhatsApp, email, posts, contatos externos e ações produtivas — sempre com preview/aprovação.

## Aguardando data/evento

- [ ] Revisão mensal/arquivamento de pendências antigas — próximo check recomendado 2026-05-26.
- [ ] SPITI email poller/monitor — reavaliar quando houver novo leilão ou necessidade operacional.

## Concluídos / retirados da fila ativa

- [x] Adaptação Amora → Hermes Geral — DOCX convertidos, `IDENTITY.md` criado, `SOUL/AGENTS/HEARTBEAT` consolidados, `MAPA.md` raiz criado, raiz `AGENTS.md`/`HEARTBEAT.md` higienizada para Hermes-native; sem cron novo. Evidência: `areas/operacoes/rotinas/amora-templates-hermes-geral-adaptacao-2026-05-16.md` e `reports/amora-reference-ingest-2026-05-16/`.
- [x] Preservação do `spiti-hub` antigo não-git — evidências copiadas para `reports/spiti-hub-diff-2026-05-16/old-nongit-preservation/`; secret scan limpo; não mergear fontes antigas no `spiti-hub-git`.
- [x] Limpeza de 43 worktrees do Brain — pacotes exportados em `reports/brain-worktrees-2026-05-16/`; worktrees removidos; branches internas preservadas.
- [x] Hermes v0.13/v0.14 pós-deploy operacionalizado em documentação/read-only; runtime/infra mutável continua approval-gated.
- [x] Script local/read-only de retomada de planos/PRDs — criado em 2026-05-09 com relatório `reports/retomada-planos-prds-2026-05-09.md`; cron recorrente não criado.
- [x] Script executivo local/read-only para `brain-improvement-score.md` — criado em 2026-05-09; sem cron/UI/runtime.
- [x] Rodada G — Health checks do Brain — script expandido, rotina atualizada e relatório JSON gerado em 2026-05-09.
- [x] Mission Control / Bruno — extração/adaptação/PRD documental concluídos; UI/cron seguem fora de escopo.

## Nota de higiene

Não usar este arquivo como log de sessão. Toda pendência precisa ter status, próxima ação e evidência. Detalhes longos ficam em `empresa/gestao/pendencias.md`, `areas/`, `reports/`, `CHANGELOG.md` ou `memories/lessons.md`.
