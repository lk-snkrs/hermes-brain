# Pendências executivas — Hermes Brain

Última revisão: 2026-06-14
Rotina aplicada: `areas/operacoes/rotinas/memory-hygiene-pendencias.md`

## Revisão 2026-05-16 — Amora/Hermes identidade

Lucas aprovou aplicar a adaptação dos templates Amora para Hermes, com verificação prévia do que já existia.

Concluído nesta rodada:

- DOCX Amora convertidos para markdown limpo e preservados em `reports/amora-reference-ingest-2026-05-16/`.
- `agentes/hermes-geral/IDENTITY.md` criado.
- `agentes/hermes-geral/SOUL.md`, `AGENTS.md` e `HEARTBEAT.md` consolidados em versão Hermes-native.
- `MAPA.md` raiz criado para navegação rápida da Grande Mente.
- `README.md`, `START-HERE.md` e `empresa/rotinas/_index.md` atualizados para apontar a nova estrutura.
- `AGENTS.md` e `HEARTBEAT.md` da raiz higienizados para remover dependência de comandos/paths OpenClaw e centralizar regras Hermes-native.
- Regra “repetição → skill” formalizada no Brain e na skill `lucas-chief-of-staff`.
- Cron automático de heartbeat/revisão não foi criado; segue como rotina sob demanda até provar valor.

Evidência: commit local `10978fc docs: adapt amora identity model for hermes` e alterações posteriores nesta branch.

## Estado executivo

Esta página substitui a lista antiga de 2026-04-19, que misturava bugs corrigidos, crons históricos, pendências vencidas e registros de auditoria. O histórico útil foi preservado nas seções de concluídos/arquivados e nas fontes citadas.

Critério: manter aqui somente pendências acionáveis ou bloqueios que mudam a operação. Detalhes longos pertencem a `areas/`, `empresa/integracoes/`, `reports/`, `CHANGELOG.md` ou `memories/lessons.md`.

## Ativos

- [x] **Rodar primeira revisão sob demanda com a nova identidade Hermes Geral** — Operações/Multiempresa — concluído em 2026-05-16 em modo read-only/local; escopo Hermes/Infra, LK OS, Zipper e SPITI; sem cron novo, contato externo, deploy ou write produtivo. Evidência: `reports/revisao-operacional-multiempresa-hermes-geral-2026-05-16.md`.
- [x] **Concluir higiene pós-Amora da memória executiva compacta** — Operações/Governança — `memories/pending.md` atualizado em 2026-05-16 com resumo atual e separação entre ativos, bloqueados, aguardando e concluídos; sem apagar histórico útil.
- [x] **Gaps P0 da auditoria BRUNO-ATUAL → Hermes Brain** — Operações/Brain — pacote documental concluído em ondas posteriores: camada `hot/current`, inventário vivo de crons/bots/profiles, auditoria de skills e documentação Mordomo foram promovidos para Brain OS/Memory OS/organograma. Mission Control permanece como pendência dedicada separada, não como P0 geral. Evidência-base: `reports/bruno-atual-hermes-adaptation-audit-2026-05-19.md` + relatórios Brain OS/Memory OS de junho.

- [x] **Gerar primeiro Stock Intelligence real/read-only da LK com sourcing acionado por sinal** — LK/Stock/Sourcing — concluído em 2026-05-10 com `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`. Correção posterior: SKU Shopify é canônico para matching e Tiny deve ser mapeado/normalizado para Shopify; leitura Meta influencer precisa usar janela/período corretos e nomes em campaign/adset/ad antes de claim comercial.
- [x] **Criar mapa canônico SKU Shopify ↔ Tiny** — LK/Stock/Data Quality — preview read-only gerado em 2026-05-10: `reports/lk-sku-shopify-tiny-map-preview-2026-05-10.md`. Resultado: 6/6 campeões antes marcados como `mapear SKU no Tiny` tiveram candidato Tiny encontrado com confiança alta; tabela de aprovação gerada em `reports/lk-sku-tiny-alias-approval-preview-2026-05-10.md`; nenhum write produtivo executado.
- [x] **Investigar/corrigir leitura dos ROAS Meta 50–70x de influencers** — LK/Analytics/Tráfego Pago — relatório read-only gerado em `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`. Correção: 50–70x é `Meta attributed ROAS`, não ROAS operacional; Meta platform value excede receita web Shopify no período, então deve ser tratado como sinal de plataforma/investigação.
- [x] **Calcular ROAS atribuído por título de campanha Meta** — LK/Analytics/Tráfego Pago — relatório read-only gerado em `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`; separa `Meta attributed ROAS` por `campaign_name` de evidência Shopify por `utm_campaign`, com matching estrito para evitar falsos positivos.
- [ ] **Aprofundar dicionário canônico de influencers/campanhas LK e auditar match influencer → produto** — LK/Analytics/Tráfego Pago — dicionário seed v0.1 criado; v0.2 gerou ROAS operacional provisório em `reports/lk-influencer-operational-roas-v02-2026-05-10.md`: Silvia 12,93x e Helena 6,34x com evidência Shopify; Lala segue `ambiguous_meta_signal_only` com spend Meta forte e zero evidência Shopify direta. Próxima ação: confirmar handles/cupons/UTMs oficiais e gerar tabela `influencer → produto/SKU/tamanho → estoque` começando por Silvia/Helena. Prioridade: Lala Noleto permanece investigação de naming/cupom/UTM, não decisão de escala/estoque.
- [x] **Criar matriz inicial de funcionários LK, funções e roteamento de relatórios** — LK/Governança — concluído em 2026-05-10 com `areas/lk/equipe/README.md`. Matriz v0.1 inclui Lucas, Renan, Júlio e Danilo; define roteamento por Daily Sales Brief, Pulso Comercial, Stock Intelligence, Supply & Sourcing, Paid/Influencer, Brand Mix, CRO, SEO, DesignMD, CRM, financeiro/fiscal e loja física. Próxima ação: Lucas validar canais/cópias antes de qualquer cron ou envio recorrente.
- [x] **Aplicar Hermes Learning Loop global** — Operações/Governança — aplicado operacionalmente em 2026-05-11 no Projeto LK OS via `areas/lk/rotinas/approval-learning-ledger-2026-05-11.md`: 24 decisões/aprendizados consolidados, incluindo execução SEO verificada, CRO visível `pending_future` e cotações/sourcing `needs_approval`/`needs_data`. Próxima ação: manter o ledger como fonte de roteamento antes de repetir execução ou pedir aprovação.

- [ ] **Completar subdocs de integrações não recorrentes quando virarem fluxo real** — Operações/Integrações — próxima ação: documentar Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool somente quando houver necessidade operacional concreta. Judge.me foi promovido para etapa futura do LK OS junto com Rivo/LK Rewards. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada B.
- [ ] **Adicionar Customer Trust & Loyalty ao LK OS** — LK/CRM/Fidelidade/Reviews — etapa futura planejada em 2026-05-13: integrar LK Rewards/Rivo e Judge.me ao Data Spine/Mission Control primeiro em modo read-only, sem cupons, reviews, campanhas, envios ou alterações de regras. Correção Lucas: LK Rewards deve ser modelado como benefícios automáticos por marco de gasto/status, não como troca manual de pontos por desconto; 1 ponto = R$1; objetivo recompra/margem + experiência premium/VIP; reviews Judge.me publicam automaticamente mas Lucas deleta ruins e responde negativas pessoalmente; review request deveria sair pelo Klaviyo mas precisa auditoria; página LK Rewards será necessária. Evidência/base: `areas/lk/rotinas/lk-os-future-rivo-rewards-judgeme-reviews-2026-05-13.md` e `areas/lk/rotinas/lk-rewards-automatic-spend-milestone-model-2026-05-13.md`.
- [ ] **Adicionar captura de aniversário ao Shopify/checkout/customer profile da LK** — LK/CRM/Fidelidade — Lucas quer usar aniversário no LK Rewards, mas a data ainda não é captada no checkout. Próxima ação segura: mapear opções Shopify/Rivo/Klaviyo para coleta sem atrito, preparar copy/UX e plano de implementação com rollback; nenhum theme/checkout/customer write sem aprovação.

## Bloqueados — exigem decisão/aprovação Lucas

- [ ] **Rotação de senha root da `lc.vps`, se desejado** — Tecnologia/Segurança — bloqueio: ação sensível em infra; exige aprovação explícita e plano de rollback. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- [ ] **Decidir se a chave SSH dedicada da VPS permanece ou será removida** — Tecnologia/Segurança — bloqueio: decisão de acesso/infra. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- [ ] **Correção ativa do alerta/divergência Gateway Hermes** — Tecnologia — bloqueio: qualquer restart/update/mudança Docker/VPS exige aprovação explícita; diagnóstico read-only já documentado. Evidência/base: `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` e `areas/operacoes/rotinas/hermes-gateway-remediation-plan.md`.
- [ ] **Mission Control visual ou cron recorrente** — Operações — bloqueio: virar UI, cron, automação ou runtime exige aprovação de escopo/cadência. Evidência/base: `areas/operacoes/projetos/mission-control-prd.md`.
- [ ] **Qualquer contato externo/campanha/mensagem em massa** — LK/Zipper/SPITI — bloqueio: segue exigindo preview e aprovação do Lucas/Osmar/equipe responsável conforme o caso. Evidência/base: `seguranca/acoes-sensiveis.md` e playbooks das áreas.

## Aguardando data/evento

- [ ] **Hermes release watch** — Operações — monitoramento recorrente já foi incorporado à rotina de melhoria contínua; manter aqui apenas se um novo release gerar decisão acionável. Evidência: `reports/hermes-release-watch/latest.json`.
- [ ] **Revisão mensal/arquivamento de pendências antigas** — Governança — próximo check recomendado: 2026-06-30; rotina: compactar a fila executiva sem transformar pendências em log de sessão.
- [ ] **SPITI email poller / monitor de leilão** — SPITI — aguardando novo leilão ou necessidade operacional; sem auction previsto até agosto/2026 nos registros antigos. Evidência: `memories/decisions.md` e `ROADMAP-30-DIAS-HERMES.md`.

## Concluídos nesta revisão

- **Primeira revisão sob demanda com a nova identidade Hermes Geral** — concluído: relatório local `reports/revisao-operacional-multiempresa-hermes-geral-2026-05-16.md` gerado após leitura do Brain, cronjob list e git status. Decisão operacional: manter sob demanda até medir utilidade; qualquer cron/agenda recorrente ainda exige decisão de cadência/canal/kill criteria.
- **Rotina de revisão operacional multiempresa** — concluído: `areas/operacoes/rotinas/revisao-operacional-multiempresa.md` criado; primeiro relatório gerado em `reports/revisao-operacional-multiempresa-2026-05-09.md`. Decisão operacional: usar sob demanda para priorização LK/Zipper/SPITI/Operações; não criar cron, não consultar produção e não acionar ações externas por padrão.
- **Script local/read-only de retomada de planos/PRDs** — concluído: `scripts/retomada_planos_prds.py` criado; relatório gerado em `reports/retomada-planos-prds-2026-05-09.md` e JSON em `reports/retomada-planos-prds-2026-05-09.json`. Decisão operacional: não criar cron semanal agora; usar sob demanda quando Lucas disser “seguir”, “retomar” ou “onde paramos”.
- **Script executivo para `brain-improvement-score.md`** — concluído: `scripts/brain_improvement_score.py` criado como ferramenta local/read-only; relatório gerado em `reports/brain-improvement-score-2026-05-09-script.md` e JSON em `reports/brain-improvement-score-2026-05-09-script.json`. Cron/UI/Telegram recorrente continuam bloqueados por aprovação explícita.
- **Teste de `material-ingest-to-prd.md` em PRD antigo** — concluído: rotina validada em modo leve usando `areas/operacoes/projetos/mission-control-prd.md`; artefatos locais gerados fora do repo e relatório versionado em `reports/material-ingest-to-prd-test-2026-05-09.md`. Próxima decisão: script executivo de score antes de qualquer cron/UI.
- **Rodada G — Health checks do Brain** — concluído: `scripts/brain_health_check.py` agora cobre secrets, links/anchors markdown, arquivos estruturais obrigatórios, arquivos de agentes, MAPA por área/subárea, rotinas indexadas e skills canônicas; relatório JSON gerado em `reports/brain-health-check-2026-05-09.json`. Evidência: health check `FAIL=0 WARN=0`.
- **Mission Control / Bruno** — concluído: extração, adaptação Hermes-native e PRD documental foram feitos; UI/cron continuam fora de escopo sem aprovação. Evidência: `areas/operacoes/projetos/mission-control-prd.md`, `CHANGELOG.md` 2026-05-09.
- **Hermes Brain Improvement System P0** — concluído e mergeado no `main`. Evidência: PR #2, merge commit `bb7d16d`, arquivos em `areas/operacoes/rotinas/` e templates.
- **Guardrails P1 de memória, segurança e entrega** — concluído e mergeado no `main`. Evidência: PR #4, merge commit `3ce75f3`, `areas/operacoes/rotinas/memory-hygiene-pendencias.md` e `security-checkup.md`.
- **Meta Ads token** — pendência antiga resolvida em 2026-04-25 segundo consolidação semanal; não manter como urgente atual sem nova evidência de falha. Evidência: `memories/consolidation_weekly/2026-04-28.md`.
- **Data gap Supabase LK e 52 pedidos Shopify em falta** — corrigidos em 2026-04-25 segundo consolidação semanal. Evidência: `memories/consolidation_weekly/2026-04-28.md`.

## Arquivados / históricos preservados

- **Lista “Sistema 100% Auditado” de 2026-04-19** — arquivada como histórico; não é estado atual. Manter como contexto em `memories/lessons.md` e consolidações, não como fila ativa.
- **Tabela antiga de 11 crons ativos e 2 falhas** — arquivada por estar desatualizada e misturar crons externos/antigos. Estado atual de crons Hermes verificado em 2026-05-09: `Hermes release watch` e `Hermes release watch post-check` agendados.
- **`memories/pending_local.md` 2026-04-18** — arquivado como histórico local; duplicava pendências já resolvidas ou reclassificadas.

## Promovidos para decisão/lição

- **Autonomia documental de baixo risco** — decisão: Lucas autoriza merges autônomos em PRs documentais/Brain de baixo risco quando checks passarem; produção, infra, secrets, banco, ações externas ou risco destrutivo continuam exigindo aprovação explícita. Destino: `memories/decisions.md` e `empresa/decisoes/decisoes-permanentes.md`.
- **Pendência não é log de sessão** — lição operacional já formalizada pela rotina `memory-hygiene-pendencias.md`: pendências precisam ter status, próxima ação, bloqueio e evidência.

## Verificação da revisão

- Fontes lidas: `empresa/gestao/pendencias.md`, `memories/pending.md`, `memories/pending_local.md`, `memories/decisions.md`, `memories/lessons.md`, `memories/consolidation_weekly/2026-04-28.md`, `ROADMAP-30-DIAS-HERMES.md`, `CHANGELOG.md`, `empresa/gestao/memory-system.md`.
- Crons Hermes atuais: 2 jobs agendados via `cronjob list` em 2026-05-09.
- Nenhum token/segredo foi escrito; nomes de secrets podem aparecer, valores não.
