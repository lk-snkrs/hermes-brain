# LK OS — Plano Mestre de Implementação

Status: plano de execução vivo. Este documento existe para não deixar a implementação da LK parar no meio.
Última atualização: 2026-05-11.
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

Exige aprovação Lucas: campanha, envio, compra, reposição real, alteração Shopify/Tiny/Klaviyo/Meta/Google/Notion/n8n/banco, contato com cliente/fornecedor/time externo, deploy ou infraestrutura.

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

### Fase 1 — Data spine read-only

Status: iniciado em 2026-05-11 com Data Spine v0.1 documental/read-only; primeiro snapshot read-only multi-fonte executado e auditado.

Objetivo: consolidar um esqueleto de dados confiável, sem writes, que permita relatórios consistentes.

Entregáveis:

- [x] Inventário de fontes v0.1: Shopify, Tiny, GA4, Search Console, Meta, Google Ads/Metricool, Klaviyo, Judge.me, Frenet, Notion.
- [x] Matriz de credenciais esperadas no Doppler, sem valores, com status OK/MISSING por nome.
- [x] Scripts read-only com outputs auditáveis e contagem/freshness: v0.1 consolidado para Shopify, Tiny, GA4, Meta, Metricool/Google Ads e Klaviyo.
- [x] Freshness report específico do Tiny ERP: latência, saúde da API e visibilidade do depósito `LK | CONTROLE ESTOQUE`, sem write.
- [x] Dicionário de entidades canônicas v0.1: pedido, cliente, produto, variante, SKU, tamanho, campanha, influencer, cupom, UTM, aprovação/ação.
- [x] Regras de reconciliação Shopify vs GA4 vs Meta/Google v0.1.
- [x] Relatório de lacunas v0.1: Tiny freshness, Merchant Center, Judge.me/Frenet, Notion writes, Klaviyo UI link, PII e rótulos de fonte.

Artefato atual: `areas/lk/rotinas/data-spine-readonly-2026-05-11.md` + `areas/lk/contexto/data-spine-v0.1.md` + `reports/lk-os-data-spine-snapshot-2026-05-11.md` + `reports/lk-os-tiny-freshness-report-2026-05-11.md` + `scripts/lk_os_data_spine_snapshots_20260511.py` + `scripts/lk_os_tiny_freshness_report_20260511.py`.

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

Critério de saída:

- Automação roda silenciosa quando OK e alerta só quando precisa.
- Primeira ativação recorrente: `LK-AUTO-001` Daily 08:00 BRT e `LK-AUTO-002` Weekly segunda 09:00 BRT, ambos `no_agent`/entrega obrigatória; stdout com report = entrega ao Telegram/origin, rc não-zero = falha de watchdog. Correção Lucas: P0/P1 são rótulos de prioridade dentro do report, não condição para envio.

## Próxima sequência recomendada

1. Fechar Fase 0 com este plano mestre indexado.
2. Criar uma visão curta de Mission Control do Projeto LK OS.
3. Manter a campanha Klaviyo P1 em Draft até Lucas aprovar envio, ajuste ou pausa.
4. Avançar o próximo bloco seguro: consolidar Fase 5 no PRD e preparar decisão P2/WhatsApp concierge ou Fase 1 data spine.
5. Depois transformar os outputs em briefing semanal real.

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
