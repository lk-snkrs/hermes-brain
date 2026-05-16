# LK OS — Plano Mestre de Implementação

Status: atualizado em 2026-05-15 com Data Quality Layer v0 local/reversível materializado. Este documento existe para não deixar a implementação da LK parar no meio.
Última atualização: 2026-05-15.
Escopo: LK Sneakers / Hermes Brain / LK Operating System.

## Como Lucas deve pedir continuidade

Use uma destas frases, sem precisar explicar tudo de novo:

```text
Seguir Projeto LK OS
```

ou, quando quiser ser mais específico:

```text
Seguir LK OS — próximo bloco seguro
```

```text
Status Projeto LK OS
```

```text
Priorizar Projeto LK OS até fechar
```

```text
Executar fase [nome da fase] do Projeto LK OS
```

Regra para Hermes: quando Lucas disser `Projeto LK OS`, carregar este plano, o PRD `lk-operating-system-prd.md`, os mapas LK, as skills `lucas-chief-of-staff`, `multiempresa-routing-lucas`, `lk-shopify-readonly` e as rotinas/relatórios relevantes. Não depender da memória solta do chat.

## Definição de pronto

O Projeto LK OS só é considerado implementado quando estes blocos estiverem operacionais, documentados, verificados e com rotina de continuidade:

1. Dados e fontes de verdade mapeados e acessíveis em modo seguro.
2. Shopify read-only funcionando como fonte de pedidos, clientes, catálogo, source e receita.
3. Tiny `LK | CONTROLE ESTOQUE` funcionando como verdade de estoque por SKU/tamanho.
4. GA4/Search Console/Google/Meta/Metricool reconciliados com Shopify sem inventar ROAS.
5. Centro de Inteligência de Stock gerando lista de ruptura, baixo estoque, mapear SKU e repor estoque.
6. Paid/Influencer Intelligence ligando campanha/influencer/criativo a produto + SKU + tamanho + consequência de estoque.
7. CRM/RFM/Recompra com oportunidades reais e preview antes de Klaviyo/WhatsApp.
8. SEO/Google/Merchant Center com rotina de diagnóstico e tarefas acionáveis.
9. Approval Manager: toda ação externa/destrutiva passa por preview e aprovação Lucas.
10. Learning Loop: correções/aprovações do Lucas viram regra em Brain/skill/rotina.
11. Mission Control/Kanban com próximos passos visíveis, mas cards executáveis só quando guardrails estiverem claros.
12. Crons/briefings necessários rodando com contrato de silêncio quando OK.
13. wacli/OpenClaw WhatsApp incorporado como camada multi-conta com sync/leitura/preview seguros, guardrails de PII e envio externo sempre approval-gated.

## Modelo de gestão

### Camada 1 — PRD estratégico

Arquivo principal: `areas/lk/projetos/lk-operating-system-prd.md`.

Função: dizer o que o LK OS é, por que existe, quais módulos compõem o sistema e quais limites não podem ser quebrados.

### Camada 2 — Plano mestre de implementação

Arquivo atual: `areas/lk/projetos/lk-os-implementation-control.md`.

Função: manter fases, todo-list, status, riscos e próximos passos. Este é o arquivo que Hermes deve abrir quando Lucas disser `seguir Projeto LK OS`.

### Camada 3 — Rotinas e skills

Função: transformar cada pedaço recorrente em procedimento reutilizável.

Exemplos já existentes:

- `skills/lk-shopify-readonly/SKILL.md`
- `areas/lk/sub-areas/trafego-pago/rotinas/campaign-attribution-dictionary.md`
- `areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-v0.2.md`
- `areas/lk/rotinas/templates/daily-sales-brief-07h.md`
- `areas/lk/rotinas/templates/stock-intelligence-center.md`

### Camada 4 — Kanban/Mission Control

Função: tarefas persistentes, responsáveis, dependências e execução por worker quando seguro.

Regra: criar cards unassigned por padrão. Atribuir/rodar worker só depois de escopo, fontes, permissões e guardrails estarem claros.

### Camada 5 — Aprovações

Função: separar análise e preview de execução real.

Livre sem aprovação: documentação, análise read-only, relatório, plano, preview, skill, rotina, secret scan, health check.

Exige aprovação Lucas: campanha, envio, compra, reposição real, alteração Shopify/Tiny/Klaviyo/Meta/Google/Notion/n8n/banco, contato com cliente/fornecedor/time externo, deploy ou infraestrutura. WhatsApp via wacli/OpenClaw: conexão/sync e desenho de preview são permitidos quando no escopo; leitura recorrente, extração operacional sensível, envio, resposta, contato em grupo, mensagem a cliente/fornecedor ou automação externa exigem aprovação explícita atual.

## Fases de implementação

### Fase 0 — Fundação e guardrails

Status: em andamento, quase fechada.

Objetivo: deixar Hermes capaz de continuar sem se perder, sem expor segredo e sem confundir fonte de verdade.

Entregáveis:

- [x] PRD conceitual LK OS.
- [x] Skill Shopify read-only.
- [x] Regra Shopify vendas/catálogo; Tiny estoque.
- [x] Regra nome + SKU + tamanho.
- [x] Guardrails de aprovação.
- [x] Watchdogs básicos Hermes/v0.13.
- [x] Dicionário influencer/campanha v0.2.
- [x] Este plano mestre versionado e indexado.
- [x] Card/linha de Mission Control para o Projeto LK OS.

Critério de saída:

- Brain health check limpo.
- Plano mestre indexado.
- Lucas sabe qual frase usar para retomar.

### Fase 1 — Data spine read-only + Data Quality Layer

Status: Data Spine v0.1 iniciado em 2026-05-11; em 2026-05-15 o Data Quality Layer v0 foi auditado e materializado localmente em SQLite com backup/rollback, sem API externa/write produtivo.

Objetivo: consolidar um esqueleto de dados confiável, sem writes, que permita relatórios consistentes.

Entregáveis:

- [x] Inventário de fontes v0.1: Shopify, Tiny, GA4, Search Console, Meta, Google Ads/Metricool, Klaviyo, Judge.me, Frenet, Notion.
- [x] Matriz de credenciais esperadas no Doppler, sem valores, com status OK/MISSING por nome.
- [x] Scripts read-only com outputs auditáveis e contagem/freshness: v0.1 consolidado para Shopify, Tiny, GA4, Meta, Metricool/Google Ads e Klaviyo.
- [x] Freshness report específico do Tiny ERP: latência, saúde da API e visibilidade do depósito `LK | CONTROLE ESTOQUE`, sem write.
- [x] Dicionário de entidades canônicas v0.1: pedido, cliente, produto, variante, SKU, tamanho, campanha, influencer, cupom, UTM, aprovação/ação.
- [x] Regras de reconciliação Shopify vs GA4 vs Meta/Google v0.1.
- [x] Relatório de lacunas v0.1: Tiny freshness, Merchant Center, Judge.me/Frenet, Notion writes, Klaviyo UI link, PII e rótulos de fonte.
- [x] Auditoria P1 do Data Quality Layer contra o PRD inicial: modelo canônico por produto/variante/tamanho, lacunas de Tiny, estado comercial, preço/histórico e Approval/Learning Ledger.
- [x] Materialização local/reversível v0 em SQLite: `lk_variant_quality_status` e `lk_sku_alias_map`, 14.466 variants por tabela, com backup privado antes do write local.
- [>] Snapshot Tiny completo read-only por SKU/tamanho/depósito iniciado e retomado em 2026-05-15: catálogo Tiny listado completo (17.605 produtos; 15.372 com código), 842 leituras de estoque/deposito consolidadas, 14.530 checagens restantes; Tiny voltou a bloquear por excesso de acessos após +28 leituras na retomada, então Hermes pausou sem insistir. Camada `lk_variant_commercial_state` recalculada em baseline parcial e Mission Control v2 gerado; estado comercial final só deve ser declarado após cooldown/lotes menores.

Artefato atual: `areas/lk/rotinas/data-spine-readonly-2026-05-11.md` + `areas/lk/contexto/data-spine-v0.1.md` + `areas/lk/rotinas/lk-os-data-quality-layer-audit-2026-05-15.md` + `areas/lk/rotinas/lk-os-data-quality-layer-materialization-v0-2026-05-15.md` + `areas/lk/rotinas/lk-os-tiny-stock-snapshot-full-readonly-2026-05-15.md` + `reports/lk-os-data-spine-snapshot-2026-05-11.md` + `reports/lk-os-data-quality-layer-audit-2026-05-15.json` + `reports/lk-os-data-quality-layer-materialization-v0-2026-05-15.json` + `reports/lk-os-tiny-stock-snapshot-full-readonly-2026-05-15.json` + `scripts/lk_os_data_spine_snapshots_20260511.py` + `scripts/lk_os_data_quality_layer_audit_20260515.py` + `scripts/lk_os_data_quality_layer_materialize_v0_20260515.py` + `scripts/lk_os_tiny_stock_snapshot_full_readonly_20260515.py`.

Critério de saída:

- Hermes consegue dizer de onde vem cada número.
- Nenhum relatório chama ROAS de plataforma de venda real.
- Todo dado sensível é minimizado/mascarado.

### Fase 2 — Stock Intelligence Center

Status: em andamento; primeira fila operacional criada, bloco B saneado, catálogo Shopify padronizado em SKU-only para o `codigo` Tiny quando houve match seguro após aprovação explícita do Lucas, Fila B residual classificada e revisão manual priorizada sem writes.

Objetivo: transformar venda + estoque + lead time em ação de estoque, sem compra automática.

Entregáveis:

- [x] Lista `ruptura agora` por produto + SKU + tamanho.
- [x] Lista `baixo estoque` por produto + SKU + tamanho.
- [x] Lista `mapear SKU Tiny`.
- [x] Lista `sem SKU no Shopify`.
- [x] Execução aprovada de padronização SKU Shopify→Tiny para 8 variants com código Tiny não-vazio, backup/rollback e verificação live.
- [x] Execução aprovada no catálogo completo: 505 variants Shopify divergentes seguras alinhadas ao `codigo` Tiny, 505/505 verificadas live, 1.282 puladas por segurança.
- [x] Classificação da Fila B residual pós-saneamento: 857 com SKU Shopify sem match Tiny seguro, 374 sem SKU Shopify sem match Tiny seguro, 51 ambíguos por título+tamanho.
- [x] Priorização read-only da revisão manual residual: 15 variants residuais cruzam com fila de venda/ruptura existente; sequência P0/P1/P2/P3 definida antes de nova Fila A.
- [x] Leitura de velocidade de venda vs lead time.
- [x] Sugestão `repor estoque`, `checar sourcing`, `não agir`.
- [x] Template de preview para Lucas aprovar reposição/sourcing.
- [x] Correção de arquitetura: SQL local deve priorizar LK operacional — pessoas/clientes, produtos/catálogo/SKU/tamanho, pedidos/RFM, estoque Tiny, aprovações e histórico de ação.
- [x] SQL local operacional materializado em modo read-only: clientes, pedidos, itens, produtos, variantes e RFM vindos do Supabase LK, com PII apenas no SQLite privado chmod 600.
- [x] Automação on-demand de sourcing/subida: consultar GOAT/Droper/StockX/KicksDev somente quando houver compra, reposição ou produto novo; não manter full sync permanente de preços externos voláteis.
- [x] Router read-only de sourcing on-demand materializado a partir do Approval Decision Log: 4 P0 prontos apenas depois de aprovação manual, 1 opcional e 3 bloqueados por dados; sem chamadas externas.

Artefato atual: `areas/lk/rotinas/shopify-sku-padronizacao-tiny-catalogo-2026-05-11.md` + `areas/lk/rotinas/shopify-tiny-fila-b-residual-pos-saneamento-2026-05-11.md` + `areas/lk/rotinas/shopify-tiny-fila-b-residual-priorizada-2026-05-11.md` + `areas/lk/rotinas/stock-sku-saneamento-b-e-preview-a-2026-05-11.md` + `areas/lk/rotinas/on-demand-sourcing-router-readonly-2026-05-11.md` + `reports/lk-os-sourcing-sql-architecture-correction-2026-05-11.md` + `reports/lk-os-local-sql-operational-spine-2026-05-11.md` + `reports/lk-os-on-demand-sourcing-router-2026-05-04_2026-05-10.md`.

Critério de saída:

- Toda recomendação de estoque mostra produto + SKU + tamanho + fonte + confiança.
- Nenhuma compra/contato fornecedor é feita sem aprovação.

### Fase 3 — Paid & Influencer Intelligence

Status: iniciado com dicionário v0.2.

Objetivo: saber qual influencer/campanha/criativo move quais produtos e quais consequências gera.

Entregáveis:

- [x] Dicionário campaign/influencer seed.
- [x] Dicionário v0.2 com produto/SKU/tamanho/estoque.
- [x] Handles/cupons oficiais por influencer, primeira fila de identidade criada para Silvia, Helena e Lala; valores oficiais seguem pendentes de Lucas/Pareto/LK, sem criar cupom/campanha.
- [x] Ponte segura ad_id/utm_content/cupom/landing/referrer/note/tag iniciada como Identity Bridge read-only: Silvia alta confiança, Helena média, Lala investigação; Meta permanece `platform_signal`.
- [x] Separação `Pareto-compatible` vs `Lucas-operational`, fronteira materializada: Pareto usa linguagem Meta/ad_name/ad_id e Marias separadas; Lucas-operational só vira decisão com ponte Shopify/Tiny ou identidade confirmada.
- [x] Rotina semanal de e-mail interno LK/Klaviyo-real, sem dashboard/tool jargon, preview interno criado e validado sem envio/cron.
- [x] Regra de criativos: só incluir imagem se visual claro e aprovado; gate criado com 12 criativos em `candidate_needs_human_approval`, 0 elegíveis para e-mail sem aprovação humana.

Artefato atual: `areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-v0.2.md` + `areas/lk/sub-areas/trafego-pago/rotinas/influencer-identity-bridge-readonly-2026-05-11.md` + `areas/lk/sub-areas/trafego-pago/rotinas/pareto-operational-split-readonly-2026-05-11.md` + `areas/lk/sub-areas/trafego-pago/rotinas/weekly-internal-influencer-email-preview-2026-05-11.md` + `areas/lk/sub-areas/trafego-pago/rotinas/creative-visual-approval-gate-readonly-2026-05-11.md` + `reports/lk-os-creative-visual-approval-gate-2026-05-11.md`.

Critério de saída:

- Silvia/Helena/Lala/Maicon e demais nomes têm status claro: validated, mapped, ambiguous ou investigation.
- Produto vendido por criativo nunca é inferido por campaign/adset genérico.

### Fase 4 — Daily/Weekly CEO Briefings

Status: iniciado em 2026-05-11 com primeiro Daily Sales Brief real read-only, usando Shopify + GA4 + Tiny, e preview Telegram com contrato de silêncio.

Objetivo: transformar dados em gestão diária/semanal.

Entregáveis:

- [x] Daily Sales Brief real com Shopify + GA4 + estoque crítico, v0.1 local/read-only para 2026-05-10.
- [x] Weekly CEO Review v0.1 com vendas, canais, estoque e mídia como `platform_signal`, em `reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.md`; recompra/SEO seguem como módulos de profundidade separados.
- [x] Weekly Stock/SKU Action Plan read-only derivado do Weekly CEO Review, com 14 P0/P1 e separação entre cotação preview, validar antes de cotar e resolver SKU/Tiny primeiro.
- [x] Weekly Quote Validation Preview read-only derivado da fila Stock/SKU, com 8 grupos de cotação, tetos de custo 45/50/55%, gate de lead time e quantidade referência não-compra.
- [x] Supplier Quote Approval Packet read-only com 8 decisões por família, status `approve_quote_only`/`needs_data`/`hold_or_bundle_with_p0`, e briefs preview não enviados.
- [x] Approval Decision Log + Router read-only com 8 decisões registradas, 5 `needs_approval`, 3 `needs_data`, e bloqueio explícito de execução externa até aprovação.
- [x] Versão Telegram curta, preview-only, em `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.md`.
- [x] Versão Brain/report detalhada em `reports/lk-os-daily-sales-brief-2026-05-10.md` e `.json`.
- [x] Critério de silêncio: `would_notify=true` só para P0/P1, falha de API ou pedido explícito; sem envio/criação de cron.
- [x] Correção 2026-05-15: contrato Daily/Weekly real é entrega obrigatória, não silent-OK; crons reais verificados (`7c688553e293` Daily ativo OK; `953b9055458e` Weekly ativo aguardando primeira execução programada em 2026-05-18).
- [x] Pulso Comercial 16h template/dry-run criado em 2026-05-15: contrato Telegram curto, fontes esperadas, gatilhos verde/amarelo/vermelho e dry-run local; sem cron/envio/write. Observação: snapshot Shopify local usado no dry-run está defasado (último pedido 2026-04-16), então serve para validar formato, não para operação real do dia.

Critério de saída:

- Lucas recebe ou pede status e Hermes responde com prioridades, não dump de dados.

### Fase 5 — CRM/RFM/Recompra

Status: operacionalizado até rascunho Klaviyo P1 pendente; envio final bloqueado até aprovação explícita.

Objetivo: aumentar recompra com oportunidades aprováveis, sem disparo automático.

Entregáveis:

- [x] Segmentos RFM reais.
- [x] Clientes em risco de esfriar.
- [x] Oportunidades de cross-sell por compra anterior.
- [x] Preview de Klaviyo/WhatsApp por segmento.
- [x] Bloqueio de envio sem aprovação.
- [x] Listas finais P1 por canal geradas em privado: Klaviyo preview e WhatsApp concierge, sem envio externo.
- [x] E-mail customer-facing aprovado visualmente para Klaviyo, sem jargão interno e em padrão premium LK.
- [x] Objetos Klaviyo seguros criados/reutilizados: lista `U8YCCE`, template `XUSEtu` e campanha `01KRC1DPTY615GF5FNBPXMPKY6` em `Draft`, sem envio ou agendamento.
- [x] Rotina documental da execução P1 criada em `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md`.
- [ ] Confirmar no painel Klaviyo se o template HTML aprovado está selecionado no campaign message antes de qualquer envio.
- [x] Decisão Lucas 2026-05-11: manter Draft, sem envio/agendamento/flow.
- [x] Correção Lucas 2026-05-11: não usar deep link Klaviyo não verificado; localizar campanha pelo painel, nome ou ID.
- [x] Decidir próximo bloco: P2, WhatsApp concierge ou Fase 1 data spine, router criado com P1 Klaviyo Draft pendente, WhatsApp sem repetição automática, P2 preview bloqueado até nova fila read-only e Data Spine/RFM como única opção imediata segura.

Artefato atual: `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` + `areas/lk/sub-areas/crm/rotinas/phase5-next-decision-router-readonly-2026-05-11.md` + `reports/lk-crm-phase5-next-decision-router-2026-05-11.md` + `reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.md`.

Critério de saída:

- Cada sugestão de campanha mostra público, motivo, produto, copy, risco e aprovação necessária.

### Fase 6 — SEO, Search Console e Merchant Center

Status: operacionalizado como módulo semanal read-only inicial; cron semanal criado para nota Claude SEO e fila de melhoria, writes seguem bloqueados até aprovação.

Objetivo: trazer Google/Search para dentro do LK OS como fonte de demanda e problemas de feed/PDP.

Entregáveis:

- [x] Rotina Search Console: queries, páginas, CTR, oportunidades, operacionalizada via `search-console-readonly-router`: 25.000 linhas query/página, 15.709 páginas agregadas e 40 oportunidades P1/P2 roteadas como preview sem writes.
- [x] Módulo semanal SEO/CRO com nota Claude SEO, meta próxima e fila priorizada de melhorias de PDP/páginas.
- [x] Diagnóstico Merchant Center/feed, operacionalizado via `merchant-center-feed-readonly-router`: 5.000 status de produto lidos, 959 itens P1, 18 grupos de problema e 0 writes liberados.
- [x] Priorização de PDPs com tráfego alto e conversão baixa, operacionalizada via `pdp-low-conversion-priority-router`: 4.999 linhas GA4, 62 páginas candidatas, 40 itens priorizados, 12 P1, 22 PDPs e 0 writes liberados; follow-up `p1-seo-cro-approval-packets` criado com 8 pacotes top P1, title/meta exatos e CRO visível separado; após aprovação, 8 SEO title/meta aplicados e verificados live com rollback; CRO visível marcado como `pending_future` por decisão Lucas.
- [x] Checklist SEO/PDP para produtos importantes via `lk-seo-weekly-improvement` e rotina `seo-cro-weekly-improvement-loop`.

Critério de saída:

- SEO vira fila de melhoria de PDP/conteúdo/produto, não relatório solto.

### Fase 7 — Approval Manager e Learning Loop

Status: operacionalizado como ledger de decisões/aprendizados; aprovações, pendências futuras, needs_data e execução verificada agora ficam roteáveis por artefato canônico.

Objetivo: cada aprovação/correção do Lucas muda o sistema.

Entregáveis:

- [x] Template de approval preview por tipo de ação.
- [x] Log de decisões do Projeto LK OS iniciado via pacote `supplier-quote-approval-packet`: status `approve_quote_only`, `reject`, `needs_data`, `hold_or_bundle_with_p0`; execução externa bloqueada até aprovação.
- [x] Rotina de patch em skills quando Lucas corrige regra.
- [x] Regra de status: approved, rejected, needs_data, needs_preview, executed.
- [x] Ledger operacional `approval-learning-ledger`: 24 registros consolidados de SEO executado, CRO `pending_future`, cotações `needs_approval`/`needs_data`, regras de roteamento e 0 writes liberados.

Critério de saída:

- Hermes não repete erro já corrigido por Lucas.

### Fase 8 — Automação segura / n8n / crons

Status: aberto em modo planejamento/dry-run; catálogo de automações candidatas criado, sem cron/n8n/envio/write ativado.

Objetivo: automatizar o que já foi validado manualmente.

Entregáveis:

- [x] Lista de automações candidatas: 6 automações em `safe-automation-readiness-registry`.
- [x] Risco por automação: 4 low e 2 medium documentados.
- [x] Plano rollback por automação: pause/remove cron, supersede report, revert PR ou cancelar execução antes de envio conforme caso.
- [x] Teste em modo dry-run: contrato definido por automação; nenhuma ativação feita. `LK-AUTO-001` Daily Sales Brief e `LK-AUTO-002` Weekly CEO Review passaram no primeiro dry-run manual, com 0 cron/n8n/envio/write.
- [x] Aprovação Lucas antes de ativar produção: Lucas disse `Seguir` após o gate de cadência/destino; ativados apenas os dois cronjobs low-risk/read-only `LK-AUTO-001` e `LK-AUTO-002`, ambos `no_agent`, com entrega obrigatória do report e 0 n8n/write produtivo.
- [x] Registry operacional reconciliado: `LK-AUTO-001/002/003` ativos como crons read-only/preview; `LK-AUTO-004` manual pós-ação; `LK-AUTO-005/006` medium risk manual-only/bloqueados.
- [x] `LK-AUTO-004` guard manual pós-ação: `scripts/lk_approval_ledger_refresh_guard_20260511.py` regenera ledger, valida duplicidade/contradições e confirma 24 registros com 0 fails/warnings, sem criar cron/n8n/write.
- [x] `LK-AUTO-005` Klaviyo CRM draft watcher manual/read-only: `scripts/lk_klaviyo_crm_draft_readiness_watcher_20260511.py` confirma draft por ID/nome, 10 checks, 0 fails/warnings, sem send/schedule/customer contact/PII/deep link chutado.
- [x] `LK-AUTO-006` on-demand sourcing router guard manual/read-only: `scripts/lk_on_demand_sourcing_router_readiness_guard_20260511.py` valida 15 checks, 4 famílias prontas só após aprovação manual e 0 marketplace/fornecedor/compra/write/cron.
- [x] Fase 8 completion audit: `scripts/lk_phase8_completion_audit_20260511.py` consolida os 6 `LK-AUTO`, confirma 3 crons ativos, 2 reports obrigatórios, 3 guards manuais e 0 n8n/writes/envios externos/compra/marketplace.
- [x] Correção Lucas/PRD GMC Review: ativado `LK-AUTO-007` como cron `no_agent` read-only obrigatório quinta 09h BRT (`d4c26da4cd48`), elevando o completion audit para 7 `LK-AUTO`, 4 crons ativos e 3 reports obrigatórios, mantendo 0 n8n/writes/envios externos/compra/marketplace.

Critério de saída:

- Automação roda silenciosa quando OK e alerta só quando precisa.
- Primeira ativação recorrente: `LK-AUTO-001` Daily 08:00 BRT e `LK-AUTO-002` Weekly segunda 09:00 BRT, ambos `no_agent`/entrega obrigatória; stdout com report = entrega ao Telegram/origin, rc não-zero = falha de watchdog. Correção Lucas: P0/P1 são rótulos de prioridade dentro do report, não condição para envio.

### Fase 9 — Mission Control operacional

Status: ativo; iniciado em 2026-05-12 como snapshot executivo read-only v1 e evoluído em 2026-05-14 para cockpit com ranking stockout/recompra de 4 meses e gate serial GMC → sourcing.

Objetivo: consolidar crons, reports obrigatórios, aprovações, bloqueios e próximos passos em uma visão curta sem caçar reports.

Entregáveis:

- [x] Snapshot v1 read-only com 4 crons ativos, 3 reports obrigatórios e 7 checks verdes.
- [x] Ledger resumido: 24 registros, 8 executados verificados, 5 aguardando aprovação, 3 bloqueados por dados originalmente, 0 bloqueados restantes após autofix read-only, 8 futuros.
- [x] `needs_data` autofix autônomo: `scripts/lk_needs_data_autofix_readonly_20260512.py` reconciliou os 3 bloqueios com Shopify/Tiny read-only; Onitsuka e Saint Studio foram movidos para monitor/estoque OK, Bearbrick para higiene interna de código; 0 writes/envios/contatos/compras/marketplace.
- [x] Gates especiais visíveis: Klaviyo Draft sem envio, sourcing por aprovação manual e GMC queue P1.
- [x] GMC correction preview: `scripts/lk_gmc_correction_preview_20260512.py` converteu 963 itens P1/P2 em 6 pacotes preview-only, incluindo 1 P0 URL/checkout/landing e 3 P1 atributos/GTIN/inventory local; 0 Merchant/feed/Shopify/GSC writes.
- [x] GMC P0 URL/checkout review: `scripts/lk_gmc_p0_url_checkout_review_20260512.py` abriu o P0 em 32 offer_ids únicos; 32 matches Shopify e 32 PDPs HTTP 200 indicam que a próxima frente é Merchant checkout/account diagnostics + required attributes, não Shopify URL write imediato.
- [x] GMC required attributes preview: `scripts/lk_gmc_required_attrs_preview_20260512.py` preparou CSV local para 80 offer_ids P1; 80/80 matches Shopify, `age_group`/`gender`/`size` sugeridos, 80 linhas prontas para supplemental feed/feed rule mediante aprovação; 0 writes.
- [x] GMC required attributes apply: após aprovação explícita de Lucas, `scripts/lk_gmc_required_attrs_apply_supplemental_feed_20260512.py` atualizou o supplemental feed existente no Gist com 80 linhas; `scripts/lk_gmc_required_attrs_refresh_datafeed_url_20260512.py` apontou o datafeed para raw revisionado e acionou fetchNow; `scripts/lk_gmc_required_attrs_verify_20260512.py` confirmou 80/80 produtos com `ageGroup`/`gender`/`sizes` aplicados no Content API.
- [x] GMC pós-apply read-only: reprocessamento parcial observado; fila caiu de 963 para 957 itens P1/P2 e destinos reprovados de 708 para 586. Novo preview required attributes preparado com 80 offer_ids: 72 prontos para supplemental feed mediante aprovação e 8 em revisão manual; 0 writes.
- [x] GMC required attributes segundo lote: após aprovação explícita de Lucas (`Corrigir e aprovar`), `scripts/lk_gmc_required_attrs_apply_second_batch_20260512.py` atualizou 72 linhas no supplemental feed, apontou o datafeed para raw revisionado, acionou fetchNow e `scripts/lk_gmc_required_attrs_verify_second_batch_20260512.py` confirmou 72/72 produtos com `ageGroup`/`gender`/`sizes` aplicados no Content API; 0 Shopify/GSC/checkout/theme/envio/compra/marketplace/n8n.
- [x] GMC catalog duplication audit: `scripts/lk_gmc_catalog_duplication_audit_20260512.py` confirmou que o total de 25.578 produtos no Merchant não representa catálogo único real da LK; são 13.940 `online:pt:BR` + 11.638 `local:pt:BR`, contra snapshot local Shopify de 2.241 produtos e 14.466 variantes. Há 1.652 offer_ids presentes em mais de uma dimensão (`online` e `local`), e a limpeza/exclusão deve ser tratada como próxima ação separada com rollback.
- [x] GMC router full-catalog fix: `scripts/lk_merchant_center_feed_readonly_router_20260511.py` deixou de usar teto de 5.000 produtos e passou a ler até 30.000 status, evitando análises incompletas; nova leitura retornou 25.578 status, 4.968 itens P1/P2 e 3.656 com destino reprovado.
- [x] GMC cleanup preview: `scripts/lk_gmc_catalog_cleanup_preview_20260512.py` gerou pacote read-only de limpeza potencial: 11.638 linhas `local` P1 (9.986 órfãs locais + 1.652 duplicadas local/online) e 3.369 `online` P2 órfãs contra SKU/variant Shopify; 0 delete/supressão/write.
- [x] Guardrails consolidados: writes aprovados e reversíveis no GMC; nenhum Shopify, GSC, checkout/theme, envio/contato externo, compra/PO, marketplace ou n8n executado.
- [x] Snapshot 2026-05-14 com ranking stockout/recompra de 4 meses integrado ao Mission Control: 872 grupos com SKU, 647 candidatos, 18 Tiny zero no tamanho exato, 20 ambíguos e 609 exigindo confirmação Tiny.
- [x] Padrão LK Compras/Júlio/Notion incorporado: demanda concreta + stockout → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → compra humana → Notion como log.
- [x] PRD v0.2 continuado em paralelo: `areas/lk/projetos/lk-os-prd-continuation-2026-05-14.md`, sem marketplace/WhatsApp/Notion/write.
- [x] Consolidar relatório final do GMC P2A quando o executor autorizado terminar.
- [x] Após GMC final, gerar e executar sequência A/B/C aprovada: Droper/Notion-Júlio, diagnóstico Shopify DRAFT/404, Merchant atributos não críticos, e supressão exata dos 12 IDs DRAFT/404 no Merchant conforme opção 2 escolhida por Lucas.
- [x] Monitor pós-A/B/C read-only: `scripts/lk_gmc_post_abc_monitor_20260514.py` confirmou 12/12 deletes ausentes por GET direto e 64/64 atributos sem diagnóstico alvo; baseline geral atual tem 23.267 productstatuses e 524 linhas com issues residuais gerais.
- [x] Superfície padrão de status criada/atualizada para `Status Projeto LK OS`: `areas/lk/rotinas/lk-os-status-surface-2026-05-14.md`, com resposta Telegram pós-A/B/C.
- [x] Sourcing v8/v9/v10/v11 concluído em 2026-05-15: 14 cards com campos decisivos corretos (`Preço Droper`, menor `StockX/GOAT`, `Custo produto`, `Preço site LK`), ranking Júlio, fila pendente e pacote P1 de compra manual. P1: 4 itens, custo estimado R$ 4.465,92, valor site R$ 11.199,96, margem combinada 60,1%; sem compra/contato/pagamento automático.

Artefato atual: `areas/lk/rotinas/mission-control-snapshot-2026-05-14.md` + `reports/lk-mission-control-snapshot-2026-05-14.md` + `reports/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.md` + `areas/lk/projetos/lk-os-prd-continuation-2026-05-14.md` + `areas/lk/projetos/lk-os-program-to-finish-2026-05-14.md` + `areas/lk/projetos/lk-os-prd-pending-backlog-2026-05-15.md` + `scripts/lk_mission_control_snapshot_20260512.py` + `scripts/lk_os_stockout_recompra_rank_and_notion_preflight_20260514.py`.

Critério de saída:

- Lucas consegue pedir `status Projeto LK OS` e receber uma visão curta com crons, decisões e bloqueios, sem depender de leitura manual de múltiplos reports.
- Qualquer evolução para UI, cron recorrente próprio do Mission Control ou worker Kanban exige escopo/cadência aprovados.

### Fase 10 — Customer Trust & Loyalty Spine

Status: `pending_future`; Lucas pediu em 2026-05-13 para deixar Loyalty para depois e voltar aos próximos passos do PRD LK OS. O que já foi documentado fica como base, mas não é a frente ativa agora. Nenhum acesso/API/write/envio executado.

Objetivo: integrar LK Rewards/Rivo e Judge.me ao LK OS como camada de fidelidade premium, prova social e relacionamento.

Entregáveis:

- [x] Subdocs de integração criados: `empresa/integracoes/rivo.md` e `empresa/integracoes/judgeme.md`.
- [x] PRD atualizado com módulo `Customer Trust & Loyalty / LK Rewards & Reviews`.
- [x] Fonte e rótulos adicionados: `fact_rivo_loyalty`, `fact_judgeme_review`, `derived_loyalty_crm`, `derived_review_cro`.
- [x] Regra Lucas registrada: LK Rewards = 1pt/R$1, tiers por gasto acumulado, benefícios automáticos/status, não troca manual clássica por desconto.
- [x] Regra Judge.me registrada: reviews auto-publicadas; Lucas deleta ruins e responde negativas pessoalmente; review request via Klaviyo precisa auditoria.
- [x] Wireframe/copy v0 da página LK Rewards criado localmente, sem Shopify/theme write.
- [ ] Verificar capacidade Rivo/API/admin para tiers/marcos automáticos por gasto acumulado.
- [ ] Auditar review request Klaviyo/Judge.me sem disparo.
- [ ] Mapear captura de aniversário no Shopify/customer profile/Klaviyo/Rivo, sem implementação antes de aprovação.
- [ ] Definir tabela final de tiers/marcos/benefícios, expiração e regra de devolução/cancelamento.

Artefatos atuais:

- `areas/lk/rotinas/lk-customer-trust-loyalty-spine-v0-2026-05-13.md`.
- `areas/lk/rotinas/lk-rewards-automatic-spend-milestone-model-2026-05-13.md`.
- `areas/lk/rotinas/lk-rewards-page-wireframe-copy-v0-2026-05-13.md`.
- `empresa/integracoes/rivo.md`.
- `empresa/integracoes/judgeme.md`.

Critério de saída:

- O LK OS consegue listar clientes elegíveis/próximos de benefícios e produtos com oportunidades de reviews, sempre com fonte clara e sem PII no Telegram.
- Nenhum benefício, cupom, review response, campanha, página Shopify ou write em plataforma é executado sem preview e aprovação explícita.

## Próxima sequência recomendada

1. Reabrir o PRD completo a partir da auditoria `lk-os-prd-full-gap-audit-2026-05-15.md`, porque Lucas corrigiu que o backlog anterior estava estreito demais.
2. Atualizar/publicar Mission Control com status A/B/C verificado, baseline residual atual e lacunas do PRD completo.
3. Começar pelo primeiro bloco P1 faltante do PRD completo: Data Quality Layer/modelo operacional por variante/tamanho.
4. Finalizar a camada operacional de sourcing pós-correções Lucas: instrução curta Júlio permanece pendente; pacote P1 já pronto para decisão manual, sem compra automática.
5. Gerar preview residual deduplicado do baseline Merchant atual (`price_updated`, `strikethrough_price_updated`, landing/crawl), sem write.
6. Retomar Pulso Comercial, CRO, Brand Mix, Paid/Influencer, Content Engine e Trend-to-Product-to-Blog como frentes P1/P2 do PRD, em modo read-only/preview primeiro. Pulso Comercial 16h e CRO baseline 0,13%→0,20% já têm artefatos P1 read-only em 2026-05-15; próximo CRO seguro é preview visual v0 antes de qualquer Shopify/theme write.
7. Tratar a frente LK + Check / Dia dos Namorados + gift card + CRO/protótipo + Rarity como pendência P1 de melhoria operacional do LK OS, usando `areas/lk/rotinas/alinhamento-semanal-lk-check-2026-05-15.md` como fonte; próximos passos só em checklist/preview/read-only até aprovação de campanha/envio/write.
8. Manter campanha Klaviyo P1 em Draft até Lucas aprovar envio, ajuste ou pausa.
9. Evoluir Mission Control só com aprovação de escopo/cadência se virar UI, cron próprio ou worker Kanban.
10. Substituir lead time padrão por lead time real por fonte/canal quando Lucas confirmar parâmetros Monbam/Droper/interno.
11. Manter Customer Trust & Loyalty como `pending_future` até Lucas retomar Loyalty/Rivo/Judge.me.

## Todo-list imediata

- [x] Criar artefato `stock-action-queue` a partir do dicionário v0.2.
- [x] Separar filas: `ruptura`, `baixo estoque`, `mapear SKU Tiny`, `sem SKU Shopify`.
- [x] Marcar cada item com ação recomendada: `repor estoque`, `checar sourcing`, `corrigir mapa`, `não agir`.
- [x] Criar preview para Lucas aprovar apenas as ações de reposição/sourcing.
- [x] Não contatar Monbam, fornecedores, time ou cliente sem aprovação.
- [x] Criar/atualizar cards unassigned no Mission Control.
- [x] Executar Fila B antes da Fila A: saneamento SKU Shopify↔Tiny read-only.
- [x] Preparar Fila A P0/P1 com velocidade estimada e lead time padrão, ainda sem compra/contato externo.
- [ ] Substituir lead time padrão por lead time real por fonte/canal quando Lucas confirmar parâmetros Monbam/Droper/interno.

## Como Hermes deve responder quando Lucas disser “seguir Projeto LK OS”

1. Abrir este arquivo.
2. Identificar a fase em andamento e o próximo checkbox não concluído.
3. Se for read-only/documentação/análise, executar.
4. Se envolver write, envio, campanha, compra, fornecedor, cliente, banco, infra ou produção, preparar preview e pedir aprovação.
5. Atualizar este plano quando um bloco for fechado.
6. Rodar health check/secret scan quando houver mudança no Brain.
7. Reportar: o que mudou, evidência, próximo passo.

## Frase canônica

A frase oficial do projeto é:

```text
Projeto LK OS
```

Sinônimos aceitos:

- `LK Operating System`
- `implementação LK OS`
- `sistema operacional da LK`
- `COO da LK no Hermes`

Se Lucas falar qualquer uma dessas frases, Hermes deve tratar como o mesmo projeto.
### 2026-05-12 — GMC local inventory source probe

- Status: read-only concluído.
- Fonte provável do inventário local: Shopify POS / Shopify app via Content API.
- Evidência: LIA settings ativo no BR com posExternalAccountId=shopify.com; produtos locais `source=api`; feed listado é apenas supplemental.
- Decisão operacional: não limpar `local` como ruído; regenerar preview com normalização `LIA_` antes de qualquer ação.
### 2026-05-12 — GMC orphan ranking

- Status: read-only concluído.
- Fila P0/P1 total: 4671; P0=2383; P1=2288.
- Preservados como válidos/monitorados: 10336 locais e 10571 online.
- Próximo passo seguro: pacote por bucket para correção/limpeza com rollback; nenhuma execução externa/write realizada.
### 2026-05-12 — GMC action package preview

- Status: preview-only concluído.
- Pacote completo gerado para 4671 itens P0/P1: {'A_online_stale_triage': 2415, 'C_local_identifier_fix': 847, 'D_local_stale_triage': 455, 'B_online_identifier_fix': 954}.
- Ordem recomendada: online stale, online identifier fix, local stale, local identifier fix.
- Nenhum Merchant/feed/Shopify/local inventory write executado; execução exige aprovação atual por pacote.
### 2026-05-12 — GMC executable previews A/B/C/D

- Status: preview-only concluído.
- Previews executáveis A/B/C/D gerados para 4671 itens P0/P1, com CSV de product IDs e snapshot privado de rollback (4671 registros).
- Nenhum Merchant/feed/Shopify/local inventory write executado; execução exige aprovação atual por pacote.
### 2026-05-12 — GMC Package B identifier fix execution

- Status: gmc_package_b_identifier_fix_dry_run_ready.
- Escopo aprovado por Lucas: `B_online_identifier_fix` online.
- Aplicados: insert_ok=0, delete_ok=0, falhas=0; candidatos unambíguos=93.
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b-identifier-fix-rollback.json`.
- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.
### 2026-05-12 — GMC Package A online stale triage execution

- Status: gmc_package_a_online_stale_triage_applied_with_anomalies.
- Escopo aprovado por Lucas: `A_online_stale_triage` online.
- Product IDs processados=2415, deletes OK nesta rodada=1511, já ausentes=898, verificados ausentes=2291, falhas=6.
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-a-online-stale-triage-rollback.json`.
- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.
### 2026-05-12 — GMC A then B execution final verification

- Status: A+B executados em ordem final aprovada por Lucas.
- A: 2415/2415 product IDs online stale verificados ausentes.
- B: 93 correções verificadas; segunda passada após A não encontrou novos B seguros; 854 preservados sem alvo unambíguo.
- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.
### 2026-05-12 — GMC Package B3 delete-old duplicates execution

- Status: superseded_rolled_back.
- Escopo aprovado por Lucas: B3 delete-old-only dos IDs antigos duplicados.
- Resultado: preview B3 estava inseguro porque `old_product_id` e `correct_existing_product_id` eram iguais nos 854 casos; a execução foi revertida.
- Snapshot privado de rollback usado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-execution-rollback.json`.
- Estado final pós-rollback: 854/854 IDs presentes novamente; Merchant products voltou a 23147; falhas finais=0.
- Lição registrada: previews/executores B/B3 devem bloquear hard `old_product_id == target_product_id`; `target already exists` só é delete-old se os IDs forem diferentes.
- Não tocado: Shopify, feed, banco, local/POS, campanhas, Google Business Profile.
### 2026-05-12 — GMC Package B3 emergency rollback restore

- Status: gmc_package_b3_emergency_rollback_restored_verified.
- Restore: reinserção dos recursos originais ausentes via rollback privado; linhas já presentes não foram alteradas.
- Verificação final: 854/854 presentes, still_missing=0, Merchant products=23147.
- Relatório: `reports/lk-gmc-2026-05-12-package-b3-emergency-rollback-restore.md`.
### 2026-05-12 — GMC local C/D Shopify live preview

- Status: preview read-only/local concluído.
- Local C/D avaliados: 1302; pacotes {'C_local_identifier_fix': 847, 'D_local_stale_triage': 455}.
- Shopify live validou como no-op/valid: 1239.
- Candidatos residuais após POS/Tiny: 63; nenhum write executado.
- Próximo: atualizar classificador/approval packet residual, mantendo local inventory preservado por padrão.
### 2026-05-12 — GMC local C/D residual Tiny probe

- Status: Tiny probe read-only concluído para 63 residuais locais C/D.
- Estados: {'tiny_no_exact_code_match_residual_cleanup_candidate_needs_pos_source_validation': 63}.
- Candidatos finais ainda dependentes de POS/source validation: 63.
- Nenhum Tiny/Merchant/Shopify/POS/feed/DB write executado.
### 2026-05-12 — GMC local C/D POS/source validation

- Status: POS/source validation read-only concluída para 63 residuais locais.
- Estados: {'old_lia_sku_replaced_by_active_shopify_product_with_replacement_local_present': 63}.
- Approval candidates residuais: 63; bloqueados revisão: 0.
- Snapshot privado rollback/source salvo; nenhum write executado.
### 2026-05-12 — GMC local C/D final approval packet

- Status: approval packet final gerado sem execução.
- Escopo: 63 old local LIA IDs; guard_failures=0.
- Snapshot privado rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-pos-source-validation-rollback-snapshot.json`.
- Execução continua bloqueada até aprovação explícita Lucas para estes 63 IDs.
### 2026-05-12 — GMC local C/D 63 old LIA cleanup execution

- Status: gmc_local_cd_63_old_lia_cleanup_applied_verified.
- Escopo aprovado por Lucas: delete exato de 63 IDs locais antigos `LIA_`, mantendo replacement rows locais.
- Deletes OK/idempotentes: 63; falhas=0; old_absent=63; old_still_present=0; replacements_present=14/14.
- Snapshot privado rollback+execução: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution-rollback-and-execution.json`.
- Não tocado: online products, replacement local rows, Shopify, Tiny, feed, banco, POS/local channel, campanhas/clientes.
### 2026-05-12 — GMC Phase 7 post-cleanup monitor

- Status: gmc_phase7_post_cleanup_monitor_readonly_ready.
- Merchant products/statuses atuais: 23147 / 23147.
- Local C/D verificado: old_absent=63/63; replacements_present=14/14.
- Item issues atuais: rows=2628; instances=34271; destination_problem_rows=1628.
- Nenhum write executado; próximo bloco recomendado: diagnostics delta/read-only e novo pacote apenas se houver candidato exato.
### 2026-05-12 — GMC Phase 7 diagnostics triage

- Status: gmc_phase7_diagnostics_triage_readonly_ready.
- Item issues atuais: rows=2628; instances=34270; delta_vs_phase7=-1.
- Buckets P1: attribute_completion_preview e checkout_url_readonly_probe.
- Nenhum write executado; próximo seguro: approval packet no-write de atributos obrigatórios por exact IDs.
### 2026-05-12 — GMC P1 attribute completion preview

- Status: gmc_p1_attribute_completion_preview_ready_no_execution.
- Produtos/instâncias required-attribute revisados: 2188 / 32574.
- Candidatos approval packet futuro: 1704; bloqueados=436.
- Nenhum write executado; aplicação exige aprovação separada por exact IDs.
### 2026-05-12 — GMC P1 core attributes root-cause probe

- Status: gmc_p1_core_attributes_root_cause_probe_readonly_ready.
- Linhas core-attr rechecadas: 1627; approval candidates futuros=1627; recheck/no-write=0; fonte incompleta/manual=0.
- Nenhum write executado; qualquer aplicação exige pacote exato, snapshot privado de rollback e aprovação Lucas.
### 2026-05-12 — GMC P1 core attributes approval packet preview

- Status: gmc_p1_core_attributes_approval_packet_preview_ready_no_execution.
- Packet preview: candidatos=1627; bloqueados=0; writes=0.
- Caveat: availability exige política explícita por Tiny/Shopify antes de execução.
- Execução futura exige aprovação Lucas, snapshot privado rollback e verificação pós-delay.
### 2026-05-12 — GMC P1 core attrs 4-field executor dry-run

- Status: gmc_p1_core_attrs_4field_executor_dry_run_ready.
- Scope: exact online IDs; campos title/link/imageLink/price; availability excluída.
- Dry-run prontos para apply futuro: 1627; bloqueados/skipped=0.
- Nenhum write executado no dry-run; apply exige aprovação explícita e snapshot privado chmod 600.
### 2026-05-12 — GMC P1 core attrs 4-field apply final

- Status: gmc_p1_core_attrs_4field_apply_verified.
- Lucas aprovou opção 2; aplicados 1.627 exact online product IDs para `title`, `link`, `imageLink`, `price`; `availability` excluída.
- Verificação pós-delay: 1.627/1.627 com os 4 campos presentes no product resource; 0 ainda faltando os 4 campos no productstatus.
- Restante: `availability` ainda faltante em 1.616 linhas; tratar em pacote separado com Tiny como fonte de verdade.
- Rollbacks privados chmod 600 salvos em `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/`.
### 2026-05-12 — GMC P1-B availability Tiny packet

- Status: `gmc_p1_availability_tiny_packet_ready_no_write`.
- Read-only packet: 5 online rows com `availability` ausente; 0 ready via Tiny depósito oficial (0 in stock / 0 out of stock); 5 bloqueados/revisão.
- Nenhum Merchant/Tiny/Shopify/feed/DB/POS/campaign write executado.
- Próximo gate: aprovação explícita para apply de `availability` somente nos ready IDs, com snapshot rollback privado.
### 2026-05-12 — GMC P1-B availability Tiny packet interim

- Status: `gmc_p1_availability_tiny_packet_queued_after_tiny_rate_limit`.
- Criado executor/packet read-only para `availability` usando Tiny como fonte de estoque.
- Primeiro teste encontrou rate-limit Tiny (`codigo_erro=6`); script corrigido para bloquear erro API e não converter em `out of stock`.
- Reexecução completa enfileirada em background (`proc_3ebe93b6e640`) após cooldown de 30 minutos com pacing conservador.
- Nenhum Merchant/Tiny/Shopify/feed/DB/POS/campaign write executado.
### 2026-05-12 — LK OS handoff antes de restart gateway

- Status: handoff salvo para retomar após restart.
- Arquivo: `reports/lk-os-handoff-after-gateway-restart-2026-05-12.md`.
- Retomada recomendada: GMC P1-B availability read-only packet; verificar Tiny rate-limit; não aplicar Merchant sem nova aprovação explícita.
### 2026-05-12 — GMC P1-B availability retomado após restart

- Status: `gmc_p1_availability_tiny_packet_running_with_tiny_backpressure_handling`.
- Tiny teste simples OK, mas paginação completa encontrou `codigo_erro=6`; executor corrigido para cooldown/retry e para nunca converter Tiny não-OK em `out of stock`.
- Processo atual: `proc_b97e693ef36f`, read-only/no-write, `notify_on_complete=true`.
- Nenhum Merchant/Tiny/Shopify/feed/DB/POS/campaign write executado.
### 2026-05-12 — LK OS next decision queue

- Status: `lk_os_next_decision_queue_ready_no_write`.
- Fila local/read-only consolidada: 10 itens; 7 exigem aprovação atual antes de execução. Observação posterior: os 4 itens de sourcing/cotação P1 genérica foram supercedidos pela correção Lucas de 2026-05-12; não devem virar envio a fornecedor sem gatilho de venda/stockout.
- Arquivos: `reports/lk-os-next-decision-queue-2026-05-12.md` e `areas/lk/rotinas/lk-os-next-decision-queue-2026-05-12.md`.
- Nenhum Merchant/Tiny/Shopify/Klaviyo/fornecedor/compra/marketplace/DB/POS/n8n write ou envio executado.
### 2026-05-12 — LK OS supplier quote send preview

- Status: `superseded_do_not_send_lucas_sourcing_correction_2026_05_12`.
- Preview local de 4 mensagens P1 para cotação foi invalidado pela correção operacional de Lucas: reposição só começa por venda/pedido com SKU/tamanho e estoque zerado confirmado.
- Novo fluxo: confirmar stockout → consultar Droper → se Droper não tiver, comparar StockX vs GOAT → preparar tarefa Notion/Júlio com link/custo/contexto; Hermes nunca compra/reserva/escolhe endereço/importador/aciona fornecedor sozinho.
- Arquivos marcados como supercedidos: `reports/lk-os-supplier-quote-send-preview-2026-05-12.md` e `areas/lk/rotinas/lk-os-supplier-quote-send-preview-2026-05-12.md`; correção registrada em `reports/lk-os-sourcing-logic-correction-2026-05-12.md`.
- Nenhum envio/contato/compra/PO/reserva/write/marketplace/n8n executado.
### 2026-05-12 — LK OS stockout sourcing router template

- Status: `lk_os_stockout_sourcing_router_template_ready_no_write`.
- Correção Lucas operacionalizada: sourcing/reposição só por venda/pedido + stockout confirmado; Droper primeiro; StockX/GOAT fallback; tarefa Júlio/Notion; aprovação inline no Telegram.
- Nenhum marketplace/Notion/n8n/fornecedor/compra/reserva/Shopify/Tiny/Merchant write executado.
### 2026-05-12 — LK OS Telegram approval surface audit

- Status: `lk_os_telegram_approval_surface_audit_ready_no_write`.
- Escaneados 178 artefatos; 50 P1 precisam de reescrita inline antes de aprovação; 8 já parecem OK.
- Regra Lucas aplicada: caminhos JSON/CSV/MD são auditoria; Telegram precisa carregar o conteúdo de aprovação no próprio texto.
- Nenhum Tiny/Shopify/Merchant/Notion/fornecedor/write executado.
### 2026-05-12 — GMC P1-B availability in-stock policy pilot apply

- Status: `gmc_p1_availability_in_stock_policy_pilot_apply_verified`.
- Aprovação: Lucas `Aprovo`; interpretado como piloto recomendado de 25.
- Escopo: exact online Merchant IDs; `availability=in stock` apenas; Tiny/Shopify/feed/DB/POS/campanha/sourcing não tocados.
- Resultado: 25 updates; 4 verificados `in stock`; rollback privado salvo.
### 2026-05-12 — GMC P1-B availability in-stock policy resumable scale

- Status: `partial_running`.
- Aprovação: opção 1, escala em lotes controlados.
- Resultado atual: processed=100; success_or_already=100; failed=0; remaining=1516.
### 2026-05-12 — GMC P1-B availability in-stock policy fast scale

- Status: `complete_verified`.
- Aprovação: opção 1, escala em lotes controlados.
- Resultado: processed=1616; success_or_already=1616; updated_verified=1354; already=262; failed=0; remaining=0.
- Rollbacks privados por lote salvos em `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/`.

### 2026-05-13 — LK OS next execution queue after Loyalty pause

- Status: `lk_os_next_execution_queue_ready_no_write`.
- Decisão Lucas: deixar Customer Trust & Loyalty / Loyalty / Rivo / Judge.me como `pending_future` e voltar aos próximos blocos não-Loyalty do PRD.
- Refresh GMC read-only executado: products/statuses 23.194/23.194; local C/D antigos ausentes 63/63; replacements preservados 14/14; issue instances 11.791; top bucket P1 `attribute_completion_preview` com 2.100 product IDs e 10.162 issue instances.
- Preview P1 attribute completion atualizado: 1.583 candidates para approval packet futuro, 469 bloqueados, 60 high-confidence, 1.523 medium/review; 0 writes.
- Próximo recomendado: `GMC attribute completion packet v2` no-write, com separação por confiança/campo e aprovação inline antes de qualquer Merchant/feed apply.
- Packet v2 gerado: 1.583 candidates, com Onda 1 high-confidence 60 e Onda 2 medium/review 1.523; 469 bloqueados e 48 ambíguos não aplicáveis.
- Relatórios: `reports/lk-os-next-execution-queue-2026-05-13.md` e `reports/lk-gmc-p1-attribute-completion-packet-v2-2026-05-13.md`.
- Nenhum Merchant/Tiny/Shopify/Klaviyo/WhatsApp/Rivo/Judge.me/Notion/n8n/infra write ou envio executado.

### 2026-05-13 — LK OS wacli/OpenClaw WhatsApp integration pending

- Status: `contract_ready_for_review_no_external_action`.
- Pedido Lucas: incorporar `wacli` ao universo operacional construído para a LK.
- Estado técnico: `pessoal` e `lk-compras` conectados como contas separadas no wacli; `lk-compras` em sync inicial. `lk-loja` planejado para etapa futura.
- Contrato criado: `areas/lk/rotinas/lk-os-wacli-openclaw-whatsapp-contract-2026-05-13.md`.
- Próximo bloco seguro: classificador LK Compras v1 local/read-only, usando a regra corrigida de compras: pedido → respostas → escolher menor preço ou opção mais perto de São Paulo se diferença pequena → compra humana → lançamento no Notion. Calibragem inicial criada em `areas/lk/rotinas/lk-compras-whatsapp-notion-flow-calibration-2026-05-13.md`.
- Próxima pendência WhatsApp: conectar amanhã a conta wacli `hermes` (`+55 11 98555-5245`) como agente Hermes para grupos/suporte/reportes. Exemplos futuros: report diário de vendas e responder perguntas operacionais do Júlio, como “quem ofereceu o 9060wht mais barato?”, buscando evidência em `lk-compras`/Shopify/Tiny/Notion. Conexão é permitida no escopo; envios, suporte automático, entrada/alteração de grupos, crons e Notion writes exigem aprovação separada.
- Guardrail: nenhum envio WhatsApp, contato com grupo/cliente/fornecedor, compra, automação recorrente ou integração externa sem aprovação explícita atual.
- Rotina pendente: `areas/lk/rotinas/lk-os-wacli-openclaw-whatsapp-integration-pending-2026-05-13.md`.
### 2026-05-13 — GMC P1 attribute completion Onda 1 dry-run executor

- Status: `gmc_p1_attribute_completion_onda1_executor_dry_run_ready`.
- Escopo: Onda 1 high-confidence do packet v2; exact online Merchant IDs; `sizes` apenas.
- Resultado dry-run: 60 ready; 60 selecionados pelo limite atual; nenhum Merchant/Shopify/Tiny/feed/write executado.
- Apply futuro exige aprovação inline: `Lucas approved GMC P1 Attribute Onda 1 apply`.
### 2026-05-13 — GMC P1 attribute post-apply Onda 1 + Onda 2 review

- Status: `gmc_p1_attribute_post_apply_onda1_verified_wave2_review_ready_no_write`.
- Onda 1 pós-apply: 60/60 com `sizes` esperado; size issues fresh remanescentes=0.
- Onda 2: 1523 rows revisadas read-only; amostra de 80 preparada; nenhum apply/write.
### 2026-05-13 — GMC P1 attribute completion Onda 2 pilot executor dry-run

- Status: `gmc_p1_attribute_wave2_pilot_executor_dry_run_ready`.
- Escopo: Onda 2 piloto conservador; `sizes` + `ageGroup=adult` + `gender=unisex`; exact online Merchant IDs.
- Resultado dry-run: 1285 ready; 50 selecionados no piloto; nenhum write executado.
- Apply futuro exige aprovação inline: `Lucas approved GMC P1 Attribute Wave2 pilot apply`.
### 2026-05-13 — GMC P1 attribute Wave2 post-status recheck

- Status: `gmc_p1_attribute_wave2_post_status_recheck_read_only_complete`.
- Onda 2 aplicada: 969 IDs; productstatuses fresh avaliados.
- Estados Onda 2 aplicada: {'ok_attrs_and_no_target_required_diagnostic': 969}.
- Required attrs atuais no GMC: {'color': 1082, 'size': 464, 'age group': 437, 'gender': 437, 'price': 35}.
- Nenhum write/delete adicional executado.
### 2026-05-13 — GMC P1 remaining attribute Wave3 preview

- Status: `gmc_p1_attribute_remaining_wave3_preview_read_only`.
- Required attr rows: 800; instances: 1368.
- Buckets: {'blocked_no_safe_suggestion': 165, 'candidate_wave3_color_tag_high_confidence': 5, 'candidate_wave3_color_title_review': 377, 'candidate_wave3_mixed_review': 7, 'candidate_wave3_price_review_do_not_apply_without_price_policy': 31, 'candidate_wave3_size_age_gender_review': 215}.
- Nenhum write/delete adicional executado.

### 2026-05-14 — GMC residual corrections pós-A/B/C

- Status: `executado_com_rollback_e_monitoramento`.
- Autorização Lucas: seguir/corrigir residuais 1/3/4/5 e usar Kicks.dev para GTIN quando seguro.
- Resultado monitorado final imediato: `landing_page_error` 27→0, `landing_page_pending_crawl` 5→0, `price_updated` 1089→915, `strikethrough_price_updated` 516→231, `missing_item_attribute_for_product_type` 44→34, `image_link_broken` 6→3.
- GTIN mantido sem write: Kicks.dev consultado, mas sem correspondência segura de tamanho para patch automático.
- Guardrail aprendido: não usar Content API insert/upsert em itens `source=crawl`/multi-feed para missing attrs; a tentativa criou overlay `source=api`, foi revertida/deletada.
- Relatório: `areas/lk/rotinas/gmc-residual-corrections-2026-05-14.md`.

- [>] Atualização incremental Tiny 2026-05-15: 872 leituras consolidadas; lote 250/delay 3s pausado em rate limit após +30; Mission Control v2 atualizado, sem promoção para final.
- [x] Approval Manager + Learning Loop v0 implementado localmente em 2026-05-15: correção crítica `/background` não autoriza envio externo registrada em memória, Brain e skills; contatos externos agora default `draft_only` até aprovação atual com payload/destinatário exatos. Artefato: `areas/lk/rotinas/lk-os-approval-manager-learning-loop-v0-2026-05-15.md`.
- [x] Approval Manager Rules v0 materializado em SQLite local em 2026-05-15: tabela `lk_approval_manager_rules` com gates para envio externo, COMPRE JÁ/tema-CRO, campanhas, sourcing, GMC e data quality local. Artefato: `areas/lk/rotinas/lk-os-approval-manager-rules-v0-2026-05-15.md`.

### 2026-05-15 — Approval Manager v1 finalizado

- Status: `active_local_router_layer`.
- SQLite local: `lk_approval_manager_rules`, `lk_approval_decision_ledger`, `lk_approval_router_tests`.
- Router regression: 8/8 PASS para background/WhatsApp, Klaviyo, GMC price, sourcing/fornecedor, Data Quality, theme/CRO, GMC preview e Tiny/SKU local.
- Mission Control v2 atualizado com filas `draft_only`, `needs_approval/preview` e `autonomous_readonly/local`.
- Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`.
- Nenhum envio externo, campanha, compra, Shopify/Tiny/Merchant/Meta/Klaviyo/WhatsApp, cron, deploy ou infra executado.
