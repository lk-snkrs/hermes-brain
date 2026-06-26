# Consolidação operacional — crons e automações ativas (2026-05-16)

## Fonte e escopo

Inventário read-only dos crons ativos do Hermes, scripts em `/opt/data/scripts`, VPS/containers e superfícies recentes. Objetivo: reduzir redundância operacional sem quebrar rotinas úteis.

Ações executadas nesta etapa após confirmação de redundância:

- Removido cron `e7a61e275c37` — `Hermes artifacts freshness watchdog no_agent` — porque validava artefatos v0.13/Mission Control/Kanban que já não são fonte central.
- Arquivados scripts redundantes/órfãos em `/opt/data/scripts/_archived_redundant_20260516/`:
  - `hermes_artifacts_freshness_watchdog.py`
  - `hermes_daily_ci_recheck_after_first_run.py`
- Renomeado cron `f00c68f5967a` de `Zipper OS daily executive cockpit` para `Zipper daily executive inbox/followups report` para reduzir confusão com cockpits/dashboards.

## Estado canônico atual

- Superfície principal: Telegram Hermes.
- Hermes produção: Docker project `hermes-agent-5ajw`, imagem `hermes-agent-custom:v0.14.0-20260516`, versão Hermes `v0.14.0 (2026.5.16)`.
- Workspace terceiro: removido. `hermes.lucascimino.com` retorna 404 intencionalmente.
- Mission Control local: arquivado em `_archived_projects/mission-control-cimino-hermes.20260516-173247`; não tratar como produto ativo por padrão.
- Mission Control domínio: `mission.lucascimino.com` ainda responde 200; precisa ser classificado separadamente como superfície publicada legada/ativa.
- Brain canônico: `/opt/data/hermes_bruno_ingest/hermes-brain`.

## Crons ativos classificados

### Manter — infraestrutura Hermes

- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop — diário 02:00 BRT.
  - Função: inteligência diária + melhoria contínua.
  - Status: manter, mas ajustar prompt para evitar propor novos cockpits sem auditoria prévia.
- `edd06fe19397` — Hermes runtime + cron watchdog no_agent — a cada 30 min.
  - Função: saúde runtime/cron, silent OK.
  - Status: manter.
- `4bb4e2223fd3` — Hermes compression failure self-heal watchdog — a cada 10 min.
  - Função: detectar/corrigir classe específica de falha de compressão, silent OK.
  - Status: manter enquanto a falha ainda for possível.

### Manter, mas renomear/classificar melhor

- `e7a61e275c37` — Hermes artifacts freshness watchdog no_agent — diário 09:00 BRT.
  - Decisão executada em 2026-05-16: removido.
  - Motivo: script validava docs v0.13/Mission Control/Kanban que não são mais fonte central e criava redundância operacional.
  - Script arquivado em `/opt/data/scripts/_archived_redundant_20260516/`.
- `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery — diário 08:00 BRT.
  - Função: relatório obrigatório, não watchdog silencioso.
  - Ação recomendada: renomear mentalmente/docs para “LK Daily Sales Brief delivery”.
- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — quinta 09:00 BRT.
  - Função: relatório obrigatório, não watchdog silencioso.
  - Ação recomendada: manter se Lucas realmente usa; caso contrário consolidar no Weekly CEO Review.
- `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery — segunda 09:00 BRT.
  - Função: review executivo semanal. Ainda sem primeira execução.
  - Ação recomendada: manter até primeira execução; avaliar valor depois.

### Manter — LK crescimento/SEO

- `c214051f7780` — LK weekly influencer sales email — quarta 10:00 BRT.
  - Função: relatório/email semanal aprovado.
  - Status: manter se ainda é canal usado por Lucas.
- `15777e3416dc` — LK SEO/CRO weekly Claude SEO improvement loop — segunda 10:00 BRT.
  - Função: rotina semanal SEO/CRO.
  - Risco de redundância: sobreposição com Daily/Weekly CEO Review se ambos falarem de CRO/SEO.
  - Ação recomendada: manter, mas fazer o Weekly CEO Review referenciar/absorver achados em vez de duplicar.

### Manter — Mordomo pessoal

- `051f05ce17c1` — Mordomo WhatsApp pessoal realtime scan — a cada 15 min.
  - Função: alertas acionáveis de WhatsApp, sem envio externo.
  - Status: manter se a relação sinal/ruído estiver boa.
- `b2492892b18f` — Mordomo WhatsApp pessoal resumo 09h BRT.
  - Função: digest pessoal manhã.
  - Status: manter.
- `4ced266825f0` — Mordomo WhatsApp pessoal resumo 17h BRT.
  - Função: digest pessoal tarde.
  - Status: manter.
- `527ee57b3a6b` — Mordomo: confirmar entrega com Seda Embalagens — one-shot 2026-05-19.
  - Função: lembrete pontual.
  - Status: manter até executar; depois deve desaparecer/ficar histórico.

### Manter, mas consolidar nomenclatura — Zipper

- `a2efea956036` — Zipper Gmail auto-draft reply-all — a cada 15 min, deliver local.
  - Função: criar rascunhos, não enviar externamente.
  - Status: manter se Lucas aprova o fluxo de rascunhos.
- `71b147362ec1` — Zipper Gmail style learning refresh — diário 03:20 BRT, deliver local.
  - Função: aprendizagem de estilo, read-only/local docs.
  - Status: manter, baixa exposição.
- `f00c68f5967a` — Zipper OS daily executive cockpit — diário 08:15 BRT.
  - Problema de nomenclatura: “cockpit” pode confundir com Workspace/Mission Control.
  - Ação recomendada: renomear para “Zipper daily executive inbox/followups report”.
- `af07bbc077b8` — Zipper OS inbox/followups watchdog silent — a cada 30 min.
  - Função: watchdog silencioso real.
  - Status: manter.

## Candidatos a revisão imediata

1. `e7a61e275c37` — Hermes artifacts freshness watchdog.
   - Status: resolvido em 2026-05-16.
   - Ação: cron removido e script arquivado.
   - Motivo: dependia de artefatos v0.13/Mission Control/Kanban já não centrais.

2. `f00c68f5967a` — Zipper daily executive inbox/followups report.
   - Status: resolvido parcialmente em 2026-05-16.
   - Ação: cron renomeado para remover “cockpit” do nome.
   - Próximo passo opcional: renomear script/documentação se quisermos limpeza semântica completa.

3. `7c688553e293`, `953b9055458e`, `d4c26da4cd48`.
   - Motivo: todos são “mandatory delivery” LK; podem competir por atenção.
   - Próximo passo: manter por enquanto, mas fazer Weekly CEO Review resumir/absorver daily/GMC/SEO e não repetir.

4. `15777e3416dc` com workdir `/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510`.
   - Motivo: usa workdir antigo, não o Brain canônico.
   - Próximo passo: revisar se ainda precisa desse worktree; preferir Brain canônico ou repo limpo.

## Scripts órfãos/candidatos a arquivar

- `hermes_daily_ci_recheck_after_first_run.py`
  - Status: arquivado em `/opt/data/scripts/_archived_redundant_20260516/`.
  - Motivo: one-shot antigo sem cron ativo associado.
- `kanban_dispatch_lk_growth_ops_once.sh`
  - Wrapper de dispatcher one-pass, sem cron ativo.
  - Recomendação: manter como ferramenta manual só se Kanban LK continuar; senão arquivar em etapa separada.

## Recomendações de próxima ação

### Ação A — sem risco, agora

Criar/atualizar um mapa operacional único no Brain com três listas:

- Ativo e saudável.
- Ativo mas precisa renomear/revisar.
- Aposentado / não retomar sem aprovação.

### Ação B — baixa mutação, mas exige decisão do Lucas

Pausar/remover somente depois de mostrar escopo:

- `e7a61e275c37` se confirmar dependência de artefatos aposentados.
- scripts órfãos `hermes_daily_ci_recheck_after_first_run.py` e possivelmente `kanban_dispatch_lk_growth_ops_once.sh`.

### Ação C — limpeza posterior

Inventariar worktrees antigos em `/opt/data/hermes_bruno_ingest/hermes-brain-*`, identificar mudanças não commitadas, e só então arquivar/remover.

## Decisão operacional sugerida

Não criar nenhum novo cockpit/dashboard. Consolidar ao redor de:

1. Telegram Hermes;
2. Brain canônico;
3. crons read-only/draft-only com nomes claros;
4. status/report único de operações.
