# Fase 4A — Classificação de profiles dormentes

Data: 2026-05-24  
Status: concluído em modo read-only  
Escopo: classificar profiles existentes sem gateway/cron ativo para orientar governança futura. Nenhum profile foi removido, editado, iniciado ou reiniciado.

## Resumo executivo

Foram encontrados 4 profiles dormentes em `/opt/data/profiles`:

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`

Todos têm estrutura completa de profile Hermes, incluindo `config.yaml`, `.env`, `SOUL.md`, `sessions`, `skills`, `logs` e `state.db`. Nenhum possui `cron/jobs.json` ativo. Nenhum gateway vivo foi detectado para esses `HERMES_HOME` no inventário anterior.

Classificação geral:

- Não parecem “bots de produção” ativos.
- Parecem workers/specialists usados por tarefas Kanban/subprocessos antigos.
- Devem ser mantidos em quarentena documental até decisão, não apagados automaticamente.
- Risco principal: possuem `.env` com credenciais/chaves presentes; mesmo dormentes, devem ser tratados como profiles sensíveis.

## Evidência coletada sem secrets

### `brain-process`

- Caminho: `/opt/data/profiles/brain-process`
- Gateway ativo: não detectado
- Cron registry: não encontrado
- `SOUL.md`: worker Hermes para manter Hermes Brain, PRDs, rotinas e skills atualizados.
- Última sessão: 2026-05-19
- Sinais de uso: autenticação/check e tarefas Kanban antigas.
- Env keys presentes, sem valores expostos: provider keys + Telegram keys.

Classificação:

- Tipo: worker documental/governança Brain.
- Status: dormente, mas conceitualmente útil.
- Dono lógico: Operações Hermes / Brain governance.
- Recomendação: manter como profile arquivado-documentado por enquanto; se voltar a ser usado, formalizar no organograma como worker interno sem Telegram público ativo.
- Risco: `.env` sensível e skills/sessions próprios; não remover sem backup/export.

Decisão sugerida futura:

- Manter como `archived_worker_brain_process` ou reativar como worker controlado via Kanban, sem gateway Telegram.

### `hermes-ops-readonly`

- Caminho: `/opt/data/profiles/hermes-ops-readonly`
- Gateway ativo: não detectado
- Cron registry: não encontrado
- `SOUL.md`: observabilidade operacional em modo somente leitura.
- Última sessão: 2026-05-16
- Sinais de uso: tarefas Kanban de auditoria/observabilidade.
- Env keys presentes, sem valores expostos: provider keys + Telegram keys.

Classificação:

- Tipo: worker read-only de infra/observabilidade.
- Status: dormente, potencialmente útil.
- Dono lógico: Operações Hermes / Infra read-only.
- Recomendação: manter documentado como worker interno, mas não gateway. Se houver uso futuro, garantir que continua sem Docker/restart/host mutation.
- Risco: possui credenciais e pode ler ambiente; deve permanecer sem automação externa até aprovação.

Decisão sugerida futura:

- Manter como worker read-only canônico para auditorias, ou absorver sua função no Hermes Geral + skill `hermes-agent` e arquivar o profile.

### `lk-analyst-readonly`

- Caminho: `/opt/data/profiles/lk-analyst-readonly`
- Gateway ativo: não detectado
- Cron registry: não encontrado
- `SOUL.md`: análise comercial LK em modo somente leitura.
- Última sessão: 2026-05-11
- Sinais de uso: tarefas Kanban antigas.
- Env keys presentes, sem valores expostos: provider keys + Telegram keys.

Classificação:

- Tipo: worker analítico LK read-only.
- Status: dormente e parcialmente sobreposto ao atual `lk-growth`.
- Dono lógico: LK Growth / analytics, se mantido.
- Recomendação: não reativar como gateway separado agora. Consolidar função dentro de `lk-growth` ou documentar como worker interno opcional de análise.
- Risco: duplicação de contexto LK; pode gerar confusão com `lk-growth` se tratado como especialista ativo.

Decisão sugerida futura:

- Preferência: absorver no `lk-growth` e marcar como legado/arquivado, salvo se Lucas quiser uma separação clara entre Growth editorial e Analyst read-only.

### `lk-content-reviewer`

- Caminho: `/opt/data/profiles/lk-content-reviewer`
- Gateway ativo: não detectado
- Cron registry: não encontrado
- `SOUL.md`: QA de conteúdo, e-mail e marca LK.
- Última sessão: 2026-05-11
- Sinais de uso: tarefa Kanban antiga e skill específica `email/lk-email-qa-product-first`.
- Env keys presentes, sem valores expostos: provider keys + Telegram keys.

Classificação:

- Tipo: worker QA de conteúdo LK.
- Status: dormente e sobreposto ao escopo atual `lk-growth`.
- Dono lógico: LK Growth / content QA, se mantido.
- Recomendação: não reativar como gateway separado. Melhor absorver como skill/rotina dentro de `lk-growth`, preservando checklist de QA.
- Risco: duplicação de especialista de conteúdo LK; pode contradizer a regra atual “conteúdo LK → lk-growth”.

Decisão sugerida futura:

- Consolidar em `lk-growth` como checklist de revisão, depois arquivar profile com backup se aprovado.

## Matriz de decisão sugerida

- `brain-process`
  - Ação sugerida: manter documentado ou reativar apenas como worker interno Kanban.
  - Não virar bot Telegram público agora.
  - Prioridade: baixa/média.

- `hermes-ops-readonly`
  - Ação sugerida: manter como worker read-only potencial, sem gateway.
  - Prioridade: média para auditorias de runtime.

- `lk-analyst-readonly`
  - Ação sugerida: absorver em `lk-growth` ou marcar legado.
  - Prioridade: média, pois toca domínio LK Growth.

- `lk-content-reviewer`
  - Ação sugerida: absorver em `lk-growth` como skill/checklist de QA; depois arquivar se aprovado.
  - Prioridade: alta/média, pois pode confundir a regra de roteamento de conteúdo LK.

## Recomendações práticas sem execução automática

### Próxima fase 4B — Cron ownership

Antes de limpar profiles, classificar ownership dos crons. Isso evita apagar/arquivar algo que algum job ainda espera usar indiretamente.

### Próxima fase 4C — Consolidação LK Growth

Criar um plano documental para consolidar `lk-analyst-readonly` e `lk-content-reviewer` dentro de `lk-growth`, preservando:

- checklist de QA de conteúdo;
- análise comercial read-only;
- limites de não envio externo;
- outputs em `areas/lk/sub-areas/growth/`.

### Próxima fase 4D — Arquivamento seguro de profiles

Somente com aprovação explícita:

1. exportar backup de cada profile;
2. registrar hash/tamanho do backup;
3. remover/neutralizar tokens se necessário;
4. arquivar diretório ou mover para área de backup;
5. verificar que nenhum processo/cron referencia o profile.

Não executar 4D sem aprovação explícita, porque envolve arquivos sensíveis e possível rollback.

## Guardrails preservados

- Nenhum `.env` foi impresso em valor.
- Nenhum secret foi copiado para o relatório.
- Nenhum profile foi alterado, removido, iniciado ou reiniciado.
- Nenhum cron foi alterado.
- Nenhum Docker/gateway/VPS foi alterado.
- Nenhum Telegram bot foi mexido.

## Conclusão

Os quatro profiles dormentes são explicáveis como workers antigos/especializados, não como runtime divergente crítico. A decisão mais segura é documentar e consolidar, não apagar. A prioridade operacional é evitar que `lk-analyst-readonly` e `lk-content-reviewer` concorram conceitualmente com `lk-growth`; eles devem virar checklist/rotina/skill dentro de LK Growth ou serem arquivados com backup em etapa aprovada.
