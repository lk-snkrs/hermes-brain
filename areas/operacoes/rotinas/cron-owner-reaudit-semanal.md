# Rotina semanal — Reauditoria de donos de crons x organograma

Status: ativa como rotina documental  
Owner: Hermes Geral / COO  
Cadência: semanal ou sob demanda após migração/limpeza de crons  
Entrega padrão: Brain/local; Telegram só se houver decisão, exceção, falha ou aprovação necessária  
Writes externos: não

## Objetivo

Garantir que a execução técnica dos crons continue coerente com o organograma de agentes e com o Task Router:

- Hermes Geral/Main: COO, Mesa, Brain, runtime, watchdogs centrais e supervisão silent-OK.
- LK Growth: SEO, CRO, GEO, GMC, Analytics, conteúdo e reviews de impacto Growth.
- Mordomo: Lucas pessoal, WhatsApp/e-mail pessoal, follow-ups e Zipper documental enquanto não houver profile próprio.
- SPITI: rotinas próprias somente quando existir registry local ou decisão explícita.

A rotina não deve mover crons automaticamente. Ela produz evidência e separa:

1. donos inequívocos;
2. supervisão central intencional;
3. ruído de entrega;
4. candidatos a novo profile;
5. decisões que exigem Lucas.

## Entradas

Ler em modo read-only:

- `/opt/data/cron/jobs.json`
- `/opt/data/profiles/lk-growth/cron/jobs.json`
- `/opt/data/profiles/mordomo/cron/jobs.json`
- `/opt/data/profiles/spiti/cron/jobs.json`, se existir
- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- reports recentes em `reports/governance/cron-*`

## Checklist

### 1. Integridade

- [ ] Contar total/ativos/pausados por profile.
- [ ] Conferir duplicidade de IDs entre registries.
- [ ] Verificar se scripts referenciados existem no contexto correto ou têm dependência absoluta documentada.
- [ ] Registrar `deliver` por profile: `origin`, `telegram`, `local`, vazio.

### 2. Dono lógico

Classificar cada cron como:

- `central_runtime_or_coo`
- `lk_growth`
- `lk_commercial_ops`
- `mordomo`
- `zipper_under_mordomo_or_future_profile`
- `spiti`
- `general_legacy_review`

Regras importantes:

- Watchdogs de gateways especialistas podem permanecer no Main se forem supervisão central do COO e silent-OK/local. Não migrar apenas porque o nome contém LK, Mordomo ou SPITI.
- LK Growth cobre SEO, CRO, GEO, GMC, analytics, conteúdo e impact reviews de crescimento.
- LK Comercial/Ops cobre vendas, pulso comercial, fechamento de loja e reports comerciais obrigatórios; enquanto não existir profile operacional LK próprio, esses crons podem permanecer no Main/COO.
- Não misturar `lk_growth` com `lk_commercial_ops` para justificar migração automática.

### 3. Ruído e UX

- [ ] `origin`/Telegram deve ser decisão, exceção, falha, aprovação ou relatório explicitamente obrigatório.
- [ ] Sucesso normal deve ser `local`/silent-OK.
- [ ] Nenhuma entrega deve vazar metadata técnica, job_id, JSON, wrapper ou marker interno.

### 4. Lacunas de governança

Identificar, sem executar mudança:

- LK Growth com muitos D+7 separados que poderiam virar digest/ledger.
- Zipper com volume suficiente para profile próprio.
- SPITI sem registry local.
- Main concentrando relatórios de operação comercial que talvez pertençam a outro profile futuro.

## Saída

Salvar relatório em:

`reports/governance/cron-owner-reaudit-YYYY-MM-DD.md`

O relatório deve conter:

- matriz por profile;
- duplicidades;
- classificação por domínio;
- crons inequívocos para migração, se houver;
- crons ambíguos que exigem decisão;
- ruído de entrega;
- recomendações 1/N para Lucas, se necessário;
- seção “Não realizado”.

## Verificação

Antes de reportar como concluído:

- [ ] Readback do relatório criado.
- [ ] Brain health/guard se arquivos do Brain foram editados.
- [ ] Secret scan focado nos arquivos criados/editados.
- [ ] Confirmar explicitamente: nenhum cron/gateway/Docker/VPS/integração externa alterado.

## Critério de promoção para automação

Não criar cron automático de reauditoria na primeira semana. Só propor automação depois de pelo menos duas execuções manuais úteis, com baixo ruído e formato estável. Cron novo exige aprovação explícita de Lucas.
