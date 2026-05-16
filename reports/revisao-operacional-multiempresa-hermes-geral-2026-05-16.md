# Revisão operacional multiempresa — Hermes Geral

Data: 2026-05-16 20:02 UTC
Modo: sob demanda, read-only/local, sem cron novo, sem envio externo, sem deploy e sem write produtivo.
Identidade aplicada: Hermes Geral / Grande Mente — `agentes/hermes-geral/IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `HEARTBEAT.md`.

## Sumário executivo

A nova identidade Hermes Geral já está consolidada o suficiente para operar como camada de COO: primeiro olha a Grande Mente, depois roteia para LK, Zipper, SPITI, Operações, Tecnologia e Governança.

Prioridade desta rodada:

1. Manter o Hermes/Brain saudável e sem automação nova não aprovada.
2. Continuar LK OS pelos blocos que já têm dados e guardrails: Daily/Weekly, GMC, sourcing manual, influencer dictionary, Loyalty/aniversário em planejamento.
3. Usar Zipper OS como cockpit de inbox/follow-ups/comercial, com rascunho interno e aprovação humana.
4. Manter SPITI conservador: repo/PRD/Paperclip e dados de leilão só com fonte verificada; nenhum lance ou deploy inferido.

## Fontes verificadas nesta revisão

- `memories/pending.md`
- `empresa/gestao/pendencias.md`
- `empresa/contexto/organograma-operacional-hermes-brain.md`
- `areas/operacoes/rotinas/revisao-semanal-multiempresa.md`
- `areas/lk/projetos/lk-os-implementation-control.md`
- `memories/lk.md`
- `areas/zipper/MAPA.md`
- `memories/zipper.md`
- `reports/zipper-os-executive-inbox-followups-2026-05-16.md`
- `areas/spiti/MAPA.md`
- `memories/spiti.md`
- `cronjob list` executado em 2026-05-16
- `git status`, branch e log local executados em 2026-05-16

## Hermes / Infra / Grande Mente

### Status verificado

- Branch atual do Brain: `consolidation/brain-filesystem-git-hygiene-20260516`.
- Últimos commits locais antes desta revisão:
  - `57d38a5 docs: complete hermes brain identity hygiene`
  - `10978fc docs: adapt amora identity model for hermes`
- A estrutura Hermes Geral está documentada:
  - `IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `HEARTBEAT.md`
  - `MAPA.md` raiz
  - organograma operacional com Grande Mente no topo.
- `cronjob list` encontrou 15 jobs. Relevantes para governança:
  - `f5a23dd6a1bd` Lucas Brain Daily Intelligence Loop ativo, próxima execução 2026-05-17 05:00 UTC.
  - `edd06fe19397` Hermes runtime + cron watchdog ativo a cada 30 min.
  - `4bb4e2223fd3` Hermes compression failure self-heal watchdog ativo a cada 10 min.
  - Jobs de LK/Zipper/Mordomo existem e alguns estão ativos; dois itens sensíveis/externos estão pausados.
- Nenhum cron novo foi criado nesta rodada.
- Git já tinha alterações não commitadas em reports Zipper gerados por rotina/watchdog antes deste relatório; foram tratados como evidência local, não como mudança produtiva.

### Pendências

- Resolver se a revisão Hermes Geral vira cron recorrente ou continua sob demanda. Política atual do `HEARTBEAT.md`: documentar, rodar sob demanda, medir utilidade, só então propor agenda/destino/kill criteria.
- Correção ativa de alerta/divergência Gateway Hermes segue bloqueada para qualquer restart/update/Docker/VPS sem aprovação explícita e rollback.
- Mission Control visual/cron próprio ainda exige aprovação de escopo/cadência.

### Riscos

- Risco de confundir rotina documentada com cron ativo; mitigação: sempre verificar `cronjob list` antes de afirmar recorrência.
- Risco de tocar infra por impulso; mitigação: manter Docker/VPS/restart/deploy bloqueados sem autorização explícita.

### Próximas ações recomendadas

1. Fechar esta revisão como baseline sob demanda da nova identidade.
2. Usar este formato por mais 1 a 2 execuções manuais antes de propor cron.
3. Se virar recorrente, começar semanal ou diário útil em janela 08:00–19:00 BRT, com silêncio quando não houver decisão.

## LK Sneakers / LK OS

### Status verificado

- LK OS está avançado e operacionalizado em várias frentes, com guardrails claros.
- Fase 1 Data Spine/Data Quality Layer:
  - Data Quality Layer v0 materializado localmente em SQLite.
  - Snapshot Tiny completo ainda parcial: 842 leituras consolidadas, 14.530 checagens restantes; Tiny bloqueou por excesso de acessos e Hermes pausou sem insistir.
- Fase 3 Paid & Influencer:
  - Dicionário v0.2 criado.
  - Silvia alta confiança, Helena média, Lala em investigação; Meta permanece `platform_signal` até ponte Shopify/Tiny/identidade confirmada.
  - Regra Maicon/Meta em memória: influencer em `ad_name`; somar todos `ad_ids`; separar Marias.
- Fase 4 Briefings:
  - Daily Sales Brief ativo como entrega obrigatória read-only.
  - Weekly CEO Review ativo, aguardando primeira execução programada em 2026-05-18.
- Fase 5 CRM/RFM:
  - Draft Klaviyo P1 existe e permanece sem envio/agendamento/flow; precisa confirmar no painel se template aprovado está selecionado antes de qualquer envio.
- Fase 6 SEO/GMC:
  - GMC passou por correções aprovadas e verificadas; residual geral ainda existe e deve seguir por preview/aprovação.
- Fase 9 Mission Control:
  - Stockout/recompra/sourcing v8–v11 consolidado.
  - Pacote P1 de compra manual: 4 itens, custo estimado R$ 4.465,92, valor site R$ 11.199,96, margem combinada 60,1%; sem compra, contato, pagamento ou marketplace automático.
- Fase 10 Customer Trust & Loyalty:
  - Planejada como futura; Rivo/LK Rewards/Judge.me primeiro em read-only/modelagem.

### Pendências

1. Aprofundar dicionário canônico de influencers/campanhas e auditoria influencer → produto/SKU/tamanho/estoque, começando por Silvia/Helena; Lala segue investigação.
2. Confirmar template HTML aprovado no campaign message Klaviyo antes de qualquer envio P1.
3. Completar Tiny stock snapshot em lotes menores/cooldown, sem insistir contra rate limit.
4. Modelar LK Rewards/Rivo/Judge.me e captura de aniversário sem implementar no checkout/theme/customer profile ainda.
5. Seguir GMC residual com snapshots antes de writes e aprovação por lote.

### Riscos

- Tratar ROAS Meta como ROAS operacional. Regra: Meta = sinal de plataforma até reconciliação Shopify/Tiny.
- Agir em compra/sourcing automático. Regra: Droper/StockX/GOAT/KicksDev on-demand só quando houver compra, reposição ou produto novo, e decisão humana antes de compra.
- Enviar CRM/Klaviyo/WhatsApp sem aprovação. Bloqueado.

### Próximas ações recomendadas

- Próximo bloco seguro imediato: relatório read-only de `influencer → produto/SKU/tamanho → estoque` para Silvia/Helena e investigação Lala, sem campanha/write.
- Alternativa segura: plano UX/técnico de aniversário + LK Rewards, sem implementação.
- Para operação diária: acompanhar Daily/Weekly/GMC existentes; não criar novo cron ainda.

## Zipper Galeria

### Status verificado

- Zipper está separado de SPITI no Brain:
  - Zipper Vendas: Supabase `pcstqxpdzibheuopjkas`, tabela `vendas_tango`.
  - SPITI/CRM: Supabase `rmdugdkantdydivgnimb`.
- Tom Zipper documentado: culto, leve, sofisticado, sem hard-sell.
- Cockpit Zipper 2026-05-16 gerado por rotina/watchdog em modo read-only:
  - Conta Gmail verificada: `lucas@zippergaleria.com.br`.
  - IMAP drafts disponível: `True`.
  - Rascunhos Hermes já registrados: 9.
  - Itens sem resposta direta/atenção: 34.
  - Candidatos ainda não tratados: 1.
  - Followups totais: 19; abertos: 0; vencidos: 0.
  - Vendas últimos 60 dias: 42; valor total R$ 2.317.860,00.
  - Top artistas por valor no relatório: Janaina Mello Landini, Flávia Junqueira, Vik Muniz, Nina Pandolfo, Rizza.

### Pendências

1. Tratar 1 candidato Gmail ainda não tratado como briefing/rascunho interno, sem envio automático.
2. Usar vendas recentes + sinais de ARPA/feira para priorizar follow-up cultural leve quando houver aprovação.
3. Manter logística/retirada de obras via calendário `lucas@zippergaleria.com.br` quando houver movimentação real e aprovação.

### Riscos

- Hard-sell ou tom de liquidação em arte. Bloqueado pelo playbook.
- Confundir vendas reais Zipper com lances/leilão SPITI. Bloqueado pela regra central.
- Enviar email/WhatsApp/proposta/publicação sem Lucas/Osmar/equipe responsável aprovar. Bloqueado.

### Próximas ações recomendadas

- Preparar briefing interno do candidato Gmail pendente e dos rascunhos recentes, mantendo PII minimizada.
- Se Lucas quiser, gerar lista curta de follow-ups culturais por artista/obra baseada em venda recente e feira, como preview interno.

## SPITI Auction

### Status verificado

- Regra crítica mantida: email é fonte de verdade de lances; site mostra destaques; meta tag é preço base, não lance atual.
- `areas/spiti/MAPA.md` separa rotinas de verificação de lances, alertas, relatório de leilão, monitor health e pós-leilão.
- Repo privado documentado: `spiti-auction/spiti-hub`; fluxo seguro: `main` produção, `dev` staging, PR para `dev`, sem push direto em produção.
- Paperclip/PRD SPITI documenta próximos blocos possíveis:
  - mapa Supabase/migrations/RLS;
  - issues da próxima onda do Hub;
  - governança de PRs para agentes;
  - conteúdo/SEO/newsletter com factuality check.
- Evidência do `spiti-hub` antigo não-git foi preservada anteriormente em `reports/spiti-hub-diff-2026-05-16/old-nongit-preservation/` com secret scan limpo.

### Pendências

1. Decidir descarte físico do diretório antigo `/opt/data/hermes_bruno_ingest/spiti-hub` depois do backup/diff, se Lucas quiser.
2. Quando retomar SPITI Hub: trabalhar em branch/PR para `dev`, com lint/build/secret scan antes de PR.
3. Criar mapa Supabase/migrations/RLS antes de deixar agentes mexerem em features com dados.
4. Reavaliar email poller/monitor só quando houver novo leilão ou necessidade operacional.

### Riscos

- Afirmar lance/lote/preço sem fonte correta. Regra: silêncio > dado errado.
- Deploy/merge/migração/email/post sem aprovação. Bloqueado.
- Conteúdo público com dados de artista/obra/proveniência/leilão sem fonte. Bloqueado.

### Próximas ações recomendadas

- Próximo bloco seguro: backlog SPITI Hub/Paperclip apenas documental, sem código produtivo, listando issues P1/P2 e guardrails.
- Se houver novo leilão, primeiro validar fonte de lances por email antes de qualquer relatório operacional.

## Decisões que preciso de Lucas

1. A revisão Hermes Geral deve continuar sob demanda por mais algumas rodadas ou já quer que eu proponha cadência semanal/dia/horário/canal?
2. Para LK: prefere próximo bloco seguro como influencer dictionary/produto/estoque ou LK Rewards/aniversário?
3. Para Zipper: quer que eu transforme o candidato Gmail pendente em briefing/rascunho interno para aprovação?
4. Para SPITI: posso preparar só o backlog documental Paperclip/Spiti Hub ou prefere esperar novo leilão/necessidade?
5. Sobre o diretório antigo do `spiti-hub`: manter preservado por enquanto ou preparar plano de remoção física com rollback?

## Posso executar sem risco agora

- Atualizar documentação local/Brain desta revisão.
- Rodar health check e secret scan local.
- Preparar previews/briefings internos sem envio externo.
- Gerar próximos relatórios read-only por área.

## Não executado nesta rodada

- Nenhum cron novo.
- Nenhum envio externo, email, WhatsApp, campanha ou contato.
- Nenhum deploy, merge remoto, Docker, VPS, restart, banco produtivo, Shopify, Tiny, Klaviyo, Meta, Google, Merchant ou marketplace write.
- Nenhum dado sensível bruto impresso no relatório.
