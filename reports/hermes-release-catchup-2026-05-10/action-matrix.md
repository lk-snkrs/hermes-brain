# Hermes release catch-up v0.10–v0.13 — matriz operacional LK/Hermes

Data: 2026-05-10
Fonte: GitHub releases NousResearch/hermes-agent

## Objetivo
Transformar releases recentes do Hermes em melhorias práticas para o dia a dia LK/Hermes, não apenas anotar novidades.

## Releases revisadas
- v0.10.0 — 2026-04-16 — Tool Gateway release
- v0.11.0 — 2026-04-23 — Transport/TUI/gateway/cron/webhook/skills
- v0.12.0 — 2026-04-30 — curator, self-improvement, skills, dashboard, cron workdir/context_from
- v0.13.0 — 2026-05-07 — Tenacity release: Kanban, `/goal`, durability, no_agent cron, security/reliability, optional skills

## Implementar/operacionalizar agora — baixo risco

### 1. Daily release catch-up com janela histórica
- Status: operacionalizado no cron diário `f5a23dd6a1bd`.
- Dia a dia: toda execução precisa revisar latest + janela histórica relevante, hoje v0.10–v0.13.
- Motivo: features antigas podem só fazer sentido depois que a operação LK amadurece.

### 2. Classificação obrigatória por tipo de adoção
- Status: operacionalizado na skill `lucas-hermes-continuous-improvement` e no prompt do cron.
- Categorias:
  - adotar agora;
  - ensinar manual;
  - guardar para depois;
  - ignorar;
  - pedir aprovação por médio/alto risco.

### 3. Aprendizado vira sistema
- Status: operacionalizado na skill.
- Regra: melhoria de baixo risco não termina em nota; precisa virar skill, checklist, relatório, cron, script, dashboard local ou documentação prática.

### 4. Curator/self-improvement como disciplina de skills
- Origem: v0.12.
- Ação atual sem risco: usar como princípio operacional já; ao carregar skill e descobrir lacuna, patch imediato.
- Próximo depois do update: avaliar comandos nativos `hermes curator status`/self-review com configuração segura.

### 5. Cron com toolsets enxutos e workdir/context_from
- Origem: v0.11/v0.12/v0.13.
- Status: já aplicado parcialmente no cron diário com `enabled_toolsets` limitado.
- Próximo baixo risco: revisar crons LK para garantir toolsets mínimos, contexto explícito e outputs encadeáveis sem inflar prompt.

### 6. Webhook/direct-delivery e no_agent como watchdogs baratos
- Origem: v0.11/v0.13.
- Status: operacionalização inicial documentada em `areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md`.
- Uso LK recomendado: checks de saúde de relatório/e-mail/API que só acordam agente quando há anomalia.
- Risco: baixo para scripts read-only; médio se acoplar a produção/envio externo.
- Próximo baixo risco: preparar script local read-only e testar stdout vazio no caso OK antes de pedir aprovação para cron real.

## Ensinar Lucas — manual

### `/goal`
- Origem: v0.13.
- Status: operacionalizado como padrão de uso em `areas/operacoes/rotinas/hermes-v013-operacionalizacao.md`.
- Uso ideal: tarefas longas que hoje exigem vários “seguir”.
- Exemplo de uso agora:
  - `/goal Criar rotina completa de relatório semanal LK com layout LK/Klaviyo, validação visual e aprovação antes de envio real`
- Resultado esperado: Hermes mantém objetivo persistente e retoma etapas sem você reexplicar.
- Sinal de falha: objetivo continuar genérico, sem checklist/estado claro, ou pedir contexto já conhecido.

### Kanban multi-agent
- Origem: v0.13.
- Status: desenho seguro inicial documentado em `areas/operacoes/rotinas/hermes-v013-kanban-lk-growth-ops.md`.
- Uso ideal: transformar LK Growth Ops em board operacional.
- Colunas sugeridas:
  - Backlog
  - Doing
  - Waiting Lucas
  - Waiting External
  - QA
  - Done
- Primeiro board recomendado: `lk-growth-ops`.
- Sinal de falha: tarefas soltas no chat sem dono/status/próximo passo.
- Guardrail: ativar workers reais, dashboard público ou mudança de gateway exige aprovação.

### `/background` ou `/btw`
- Origem/reforço: v0.12.
- Status: operacionalizado como manual de uso no Telegram para pesquisas/auditorias longas que não exigem decisão imediata.
- Uso ideal: pedir pesquisa, auditoria ou revisão que pode rodar enquanto a conversa continua.
- Exemplo: `/background Auditar releases Hermes v0.10-v0.13 e gerar matriz de impacto LK`.
- Guardrail: não usar background para produção, Docker, secrets, envio externo, banco ou campanha; nesses casos pedir plano + aprovação.

## Pedir aprovação — médio/alto risco

### Atualizar runtime Hermes para 0.13
- Benefício: habilita `/goal`, Kanban, no_agent cron, melhorias de gateway, dashboard e segurança.
- Risco: restart/troca de gateway pode interromper agentes e Telegram.
- Estado: clone 0.13 preparado em paralelo com patch de compressão; teste `70 passed`.
- Próximo seguro: build/deploy com rollback e janela de restart aprovada.

### Ativar dashboard
- Benefício: visibilidade de Kanban, status e operação.
- Risco: exposição web se mal configurado.
- Recomendação: apenas local/SSH primeiro; nada público sem hardening.

### Migrar cron semanal LK para Cloudflare Email Sending
- Benefício: envio HTML real e melhor controle de MIME/layout.
- Risco: envio externo executivo; layout precisa ser LK/Klaviyo aprovado.
- Estado: preview aprovado localmente, mas não versionado no script/cron.
- Próximo seguro: integrar em branch/preview, validar screenshot/raw, pedir aprovação antes de envio real/cron.

### Optional skill Shopify
- Benefício: acesso mais nativo a Shopify para relatórios/atendimento.
- Risco: permissões de escrita ou vazamento de dados.
- Recomendação: configurar read-only primeiro; qualquer write exige aprovação.

## Guardrails permanentes
- Produção, Docker, gateway restart, secrets, banco, campanhas, Shopify writes e envios externos exigem plano + rollback + aprovação.
- Nunca expor tokens/secrets.
- Preferir read-only, preview, branch, PR e teste antes de mudar rotina viva.
