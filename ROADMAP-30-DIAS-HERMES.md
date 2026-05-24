# Roadmap — Hermes Brain pós-adaptação Bruno/OpenClaw

Este roadmap substitui o plano genérico de 30 dias por uma visão operacional do que já foi implementado e das próximas rodadas recomendadas.

## Princípio

Hermes não deve virar OpenClaw. O Brain usa a clareza organizacional ensinada pelo Bruno, mas preserva os diferenciais do Hermes:

- execução real com ferramentas;
- verificação antes de afirmação;
- memória persistente e `session_search`;
- Doppler para secrets;
- Telegram como interface;
- dados vivos em Supabase/Shopify/APIs;
- rotinas e crons verificáveis.

## Já implementado

### 1. Estrutura base

Status: concluído.

- `empresa/`
- `areas/`
- `agentes/`
- `seguranca/`
- índices executivos;
- manual operacional `START-HERE.md`.

### 2. Memórias preservadas

Status: concluído.

`memories/` continua como memória executiva compacta e global.

### 3. Agentes padronizados

Status: concluído.

- Hermes Geral.
- LK.
- Zipper.
- SPITI.

Cada agente tem estrutura operacional com identidade, ferramentas, usuário, memória e heartbeat conforme disponível.

### 4. LK operacionalizado

Status: fase base concluída.

- CRM.
- Tráfego pago.
- Ecommerce.
- Atendimento.
- Rotinas RFM, outcomes, consequence tracker, sync log, cross-sell e leads esfriando.

### 5. Zipper operacionalizado

Status: fase base concluída.

- Vendas de obras.
- Colecionadores.
- Feiras.
- Comunicação.
- Rotinas de consulta comercial, abordagem e planejamento.

### 6. SPITI operacionalizado

Status: fase base concluída.

- Verificação de lances.
- Alertas.
- Relatórios.
- Regras críticas de fonte: email > banco/site; meta tag não é lance.

### 7. Segurança e permissões

Status: concluído.

- Modelo de acesso por camada.
- Escopo por agente.
- Níveis de risco L0-L5.
- Regras de aprovação Lucas.
- Regras Doppler/secrets.

### 8. Remediação de secrets

Status: concluído no repo atual.

- Hardcoded secrets removidos dos scripts identificados.
- Whole-repo scan retornou `possible_secrets 0` na última rodada.

### 9. Governança de estrutura e score por risco

Status: concluído como guardrail documental seguro.

- Criada rotina `areas/operacoes/rotinas/brain-structure-governance-preflight.md`.
- `Brain Improvement Score` passou a priorizar risco executivo em vez de nota decorativa: segurança, rollback, integridade, evidência, próxima ação segura e não alterações.
- Regra operacional: antes de mexer em skills, agentes, heartbeats, USER/AGENTS, rotinas ou reorganização, validar estrutura, dono, riscos, índices/MAPAs e aprovação necessária.

### 10. Revisão operacional multiempresa sob demanda

Status: concluído como rotina/report documental segura.

- Criada rotina `areas/operacoes/rotinas/revisao-operacional-multiempresa.md`.
- Gerado primeiro relatório `reports/revisao-operacional-multiempresa-2026-05-09.md`.
- Decisão: usar sob demanda para responder “algo mais?”, “vamos começar?” e priorização multiempresa; não criar cron nem consultar produção por padrão.
- Produção, dados vivos, VPS/Docker, bancos, APIs, campanhas, mensagens externas, UI e cron não foram alterados.

## Próximas rodadas recomendadas

### Rodada BRUNO-ATUAL — adaptação e auditoria 2026-05-19

Status: auditoria/documentação concluída; implementação dos gaps ainda pendente.

Entregas:

1. Relatório `reports/bruno-atual-hermes-adaptation-audit-2026-05-19.md` com leitura do pacote atualizado, decisões aula por aula, takeaways dos cases e matriz de notas.
2. Nota geral do Hermes Brain contra o material: **8,0/10**.
3. Próximos gaps P0 identificados: contexto quente `hot/current`, inventário vivo de crons/bots/profiles, auditoria de skills, reconciliação Mission Control e documentação completa do Mordomo.

Limites preservados: material bruto de terceiro permaneceu fora do Brain; nenhum runtime, Docker/VPS, produção, banco/API, campanha, mensagem externa, cliente, credencial ou cron foi alterado.

### Rodada LK — LK Operating System PRD

Status: PRD v0.1 aprovado conceitualmente por Lucas e documentado como base para implementação faseada.

Entregas:

1. PRD `areas/lk/projetos/lk-operating-system-prd.md` com razão de existir da LK, objetivos, fontes de verdade, módulos, cadência alvo, approval matrix e fases.
2. Módulo global `empresa/gestao/hermes-learning-loop.md` para registrar aprovações/correções e atualizar Brain/skills/PRDs/memória quando um padrão se repetir.
3. Templates/read-only do `Daily Sales Brief`, `Weekly CEO Review` e `Stock Intelligence Center` criados em rodada anterior; próxima fase em execução: Fase 1 Data Spine read-only para padronizar fontes, entidades, reconciliação e lacunas antes de novos briefings/crons.

Limites preservados: nenhum cron, campanha, mensagem externa, alteração Shopify/Tiny/Notion/GitHub/tema, banco, secret, VPS/Docker ou runtime foi criado/alterado nesta fase documental.

Atualização 2026-05-11: Data Spine read-only da LK iniciado com `areas/lk/rotinas/data-spine-readonly-2026-05-11.md` e `areas/lk/contexto/data-spine-v0.1.md`. Primeiro snapshot multi-fonte executado em `reports/lk-os-data-spine-snapshot-2026-05-11.md`, com 6/6 fontes OK e sem writes externos.


### Rodada A — Verificação de crons reais na VPS

Status: inventário base concluído em `lc.vps`; n8n inventariado; tentativa segura de update Hermes Docker executada em 2026-05-05, mas imagem Hostinger `latest` não trouxe versão nova.

Resultado:

- Hostinger API confirmou VPS `lc.vps` (`72.60.150.124`) e `evo.lc` (`187.127.10.158`) rodando.
- Acesso a `lc.vps` restaurado via reset de senha root autorizado pelo Lucas; nova senha salva em Doppler `VPS_ROOT_PASSWORD` sem expor valor.
- Root crontab vazio; `/etc/cron.d` contém apenas Docker prune, sysstat e jobs de sistema.
- Systemd timers encontrados são padrão de sistema; nenhum timer de negócio/Hermes/LK/Zipper/SPITI.
- Docker ativo com Hermes Telegram, Hermes web, n8n, Paperclip e Traefik.
- Hermes cron confirmado: `Hermes release watch` semanal.
- Documento atualizado: `areas/operacoes/rotinas/cron-inventory.md`.

Objetivo final: transformar rotinas documentadas em estado operacional verificado.

Tarefas restantes:

1. Decidir se a chave SSH dedicada permanece ou será removida.
2. Rotacionar senha root enviada em chat, se desejado.
3. Investigar alerta de gateway parado no CLI vs container gateway rodando. — auditoria read-only documentada em `areas/operacoes/rotinas/hermes-runtime-observability.md`; plano de correção segura documentado em `areas/operacoes/rotinas/hermes-gateway-remediation-plan.md`; diagnóstico read-only de Gateway em 2026-05-04 documentado em `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md`; execução corretiva exige aprovação.
4. Fazer inventário específico de workflows n8n via API em rodada própria. — concluído em `areas/operacoes/rotinas/n8n-inventory.md`; workflow_count = 0 em `lc.vps`.
5. Atualizar `empresa/rotinas/_index.md` com coluna de status real se Lucas quiser visual executivo por rotina.
6. Update seguro do runtime Hermes Hostinger executado com backup/rollback e escopo limitado; resultado documentado em `areas/operacoes/rotinas/hermes-runtime-update-attempt-2026-05-05.md`. A imagem `latest` permaneceu em v0.9.0. Investigação GHCR read-only confirmou que `latest`/`8eb9eb9` são o digest atual e `ba03513` é anterior; não há tag pública Hostinger mais nova nesta data. Upgrade real para v0.12.0 exige fonte oficial Hostinger nova ou imagem customizada com nova aprovação.

### Rodada B — Integrações por ferramenta

Status: mapa base e aprofundamento operacional inicial concluídos.

Objetivo: criar mapa operacional por integração e transformar integrações críticas em rotinas seguras.

Entregas:

1. Doppler names por ferramenta mapeados sem valores.
2. Supabase LK, Zipper e SPITI documentados.
3. Shopify, Klaviyo, Evolution, Meta, GA4/GSC, n8n, GitHub, Hostinger e Telegram documentados.
4. Ações separadas em read-only, write, external-send e admin/destructive.
5. Integrações amarradas a áreas/agentes.
6. Rotinas criadas para validação de secrets, Shopify read-only, Supabase audit, Evolution approval, Klaviyo approval, Meta Ads reporting e Hostinger/VPS inventory.

Arquivos principais:

- `empresa/integracoes/MAPA.md`.
- Subdocs por ferramenta em `empresa/integracoes/`.
- Rotinas em `areas/operacoes/rotinas/`.
- `TOOLS.md` corrigido para evitar placeholders genéricos de Supabase.

Pendências futuras:

1. Criar subdocs para Judge.me, Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool quando virarem fluxo recorrente.
2. Transformar rotinas mais usadas em skills executáveis.
3. Rodar testes reais read-only por ferramenta quando houver pergunta operacional concreta.

### Rodada C — Playbooks operacionais LK/Zipper/SPITI

Status: concluída como rodada documental segura, sem tocar produção.

Objetivo: transformar mapas e rotinas base em playbooks business-readable para uso diário, campanhas aprovadas, abordagem de colecionadores, feiras e pregão SPITI.

Entregas:

1. LK Comando Diário: `areas/lk/rotinas/playbook-comando-diario.md`.
2. LK Campanha CRM Aprovada: `areas/lk/sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md`.
3. Zipper Abordagem Obra/Colecionador: `areas/zipper/rotinas/playbook-abordagem-obra-colecionador.md`.
4. Zipper Execução de Feira: `areas/zipper/rotinas/playbook-feira-execucao.md`.
5. SPITI Pregão ao Vivo: `areas/spiti/rotinas/playbook-pregao-ao-vivo.md`.
6. SPITI Divergência de Lances: `areas/spiti/rotinas/playbook-divergencia-lances.md`.

Regras preservadas:

- LK: dados vivos antes de afirmação; preview Lucas antes de campanha/WhatsApp/email/post.
- Zipper: sem hard sell; sem inventar histórico; aprovação Lucas/Osmar antes de contato com colecionador.
- SPITI: email é fonte de verdade; site pode ser parcial; meta tag não é lance; silêncio > dado errado.

### Rodada D — Templates Zipper por subárea

Status: concluída como rodada documental segura, sem tocar produção.

Objetivo: aprofundar Zipper com templates reutilizáveis para vendas reais, colecionadores, feiras e comunicação, preservando fonte verificável e aprovação Lucas/Osmar antes de qualquer ação externa.

Entregas:

1. Template consulta `vendas_tango`: `areas/zipper/sub-areas/vendas-obras/templates/consulta-vendas-tango.md`.
2. Template registro pós-contato com colecionador: `areas/zipper/sub-areas/colecionadores/templates/registro-pos-contato.md`.
3. Template checklist de feira por fase: `areas/zipper/sub-areas/feiras/templates/checklist-feira-por-fase.md`.
4. Template briefing de publicação obra/artista: `areas/zipper/sub-areas/comunicacao/templates/briefing-publicacao-obra-artista.md`.

Regras preservadas:

- Zipper Vendas (`pcstqxpdzibheuopjkas`, `vendas_tango`) continua separado de SPITI/leilão.
- Consultas são read-only e exigem período/ressalva antes de afirmação comercial.
- Contato com colecionador, proposta, negociação ou publicação externa exige aprovação Lucas/Osmar/equipe responsável.
- Tom Zipper: culto, leve, sofisticado, sem hard sell.

Pendências futuras:

1. LK: criar templates de preview de campanha, RFM e cross-sell.
2. SPITI: criar template de relatório interno e matriz de evidência por lote.
3. Validar consultas read-only reais apenas quando houver necessidade operacional concreta.

### Rodada E — Spiti Hub GitHub inventory

Status: concluída como rodada read-only/local, sem alterar GitHub remoto, produção, Supabase, Vercel, VPS ou mensagens externas.

Objetivo: confirmar acesso ao novo projeto `spiti-hub` citado por Lucas e registrar relação com o Hermes Brain.

Entregas:

1. Acesso confirmado ao repo privado `spiti-auction/spiti-hub` com permissões completas pelo token GitHub da Spiti fornecido por Lucas.
2. Cópia local baixada por zipball em `/opt/data/hermes_bruno_ingest/spiti-hub` sem persistir token no remote.
3. Inventário inicial documentado em `areas/spiti/contexto/spiti-hub-github.md`.
4. Verificação local: `npm install` OK, `npm run lint` OK com warnings, `npm run build` OK.
5. Recomendação registrada: mover token GitHub da Spiti para Doppler e rotacionar o token enviado por chat.

Regras preservadas:

- `spiti-hub` é sistema operacional vivo; Hermes Brain documenta regras, processos e guardrails.
- Sem push/PR/settings/secrets/deploy sem tarefa explícita.
- Alterações em migrações, auth, Supabase, CI/CD, Vercel e produção exigem revisão/aprovação.

Hardening local posterior:

- Cópia local teve `docs/deploy-edge-functions.md` redigido para placeholders em linhas secret-like.
- `eslint --fix` reduziu warnings de 46 para 39, mantendo 0 errors.
- Build segue OK; warning de bundle grande permanece.
- Token válido salvo no Doppler como `GITHUB_SPITI_HUB_TOKEN`; PR de hardening aberto para `dev`.

PR aberto:

- Spiti Hub PR #89: `https://github.com/spiti-auction/spiti-hub/pull/89`, branch `hermes/spiti-hub-secrets-lint-hardening` → `dev`.
- Commit `8c8549b` redigiu exemplos secret-like e aplicou lint-fix seguro.
- Verificações locais OK: diff check, secret scan, lint sem erros e build.
- PR #89 squash-mergeado em `dev`; merge commit `ae625a2`.
- `main`/produção não foi alterada.

Lint cleanup pass 1:

- PR #90 aberto e squash-mergeado em `dev`: `https://github.com/spiti-auction/spiti-hub/pull/90`.
- Merge commit `49b5c84`.
- Warnings de lint: 39 → 8, com 0 errors.
- Warnings de lint zerados após pass 2; warning de bundle grande permanece.
- `main`/produção não foi alterada.

Lint cleanup pass 2 e preview Vercel:

- PR #91 aberto e squash-mergeado em `dev`: `https://github.com/spiti-auction/spiti-hub/pull/91`.
- Merge commit `e8d4de4`.
- Warnings de lint: 8 → 0, com 0 errors.
- Build local OK; warning de bundle grande permanece.
- Vercel preview pode ficar bloqueado porque `@hermes-agent` não é membro do time Vercel da `spiti-auction`; resolver isso exigiria ação administrativa/Vercel/billing e não foi feito.
- `main`/produção não foi alterada.

Bundle/code splitting:

- PR #92 aberto e squash-mergeado em `dev`: `https://github.com/spiti-auction/spiti-hub/pull/92`.
- Merge commit `2943614`.
- Implementado code splitting de rotas com `React.lazy`/`Suspense` e `manualChunks` para dependências pesadas de PDF/Recharts.
- Warning de bundle grande do Vite eliminado sem elevar `chunkSizeWarningLimit`; maiores chunks pós-build ficaram abaixo de 500 kB.
- Verificações locais: diff check OK, secret scan 0, lint 0 errors/0 warnings, build OK sem warning de chunk grande.
- Revisão independente aprovada; próximos refinamentos opcionais: ErrorBoundary para falhas de chunk e monitoramento do número de requests.
- `main`/produção não foi alterada.

### Rodada F — Hardening SPITI e observabilidade de monitor

Status: concluída como rodada documental/read-only, sem alterar VPS, Docker, n8n, Supabase, GitHub, Vercel ou mensagens externas.

Objetivo: fechar o ciclo operacional SPITI com saúde do monitor, falhas conhecidas e relatório interno verificável.

Entregas:

1. Rotina `areas/spiti/rotinas/monitor-health.md` criada para health check read-only de `spiti-lances`/porta `19123`/n8n/containers.
2. Template `areas/spiti/templates/relatorio-interno-matriz-evidencia.md` criado para relatório interno com matriz de evidência por lote.
3. Rotina `areas/spiti/rotinas/pos-leilao-lessons.md` criada para fechamento, decisions, lessons e memória executiva.
4. `areas/spiti/rotinas/relatorio-leilao.md`, `areas/spiti/MAPA.md` e `empresa/rotinas/_index.md` atualizados.
5. Validação read-only em `lc.vps` em 2026-05-05: não foram encontrados systemd unit, processo, listener `19123` ou container SPITI/lances ativo nesse host; tratar monitor como não confirmado até nova validação.

Regras preservadas:

- Email segue fonte de verdade para total de lances.
- Site é auxiliar; meta tag nunca é lance atual.
- Monitor histórico documentado não prova execução atual.
- Correções em VPS/Docker/n8n/systemd/cron exigem aprovação explícita e rollback.

### Rodada G — Health checks do Brain

Status: concluída como rodada documental/técnica segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas ou runtime.

Objetivo: validar automaticamente qualidade estrutural do Brain antes de commits, PRs e merges documentais.

Entregas:

1. `scripts/brain_health_check.py` expandido e versionado.
2. Secret scan ampliado para mais famílias de tokens, incluindo GitHub fine-grained e Google OAuth/refresh-token.
3. Check de links relativos e anchors markdown internos.
4. Check de arquivos estruturais obrigatórios do Brain.
5. Check de arquivos obrigatórios por agente.
6. Check de `MAPA.md` por área e subárea.
7. Check de rotinas sem índice em `empresa/rotinas/_index.md`.
8. Check de skills canônicas vs índice/navegação por área.
9. Saída JSON opcional para relatórios em `reports/brain-health-check-*.json`.
10. Rotina `areas/operacoes/rotinas/brain-health-check.md` atualizada com critério `FAIL=0` e alvo `WARN=0`.

Resultado verificado em 2026-05-09:

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-09.json` retornou `FAIL=0 WARN=0` em todos os checks.

Regras preservadas:

- Health check estrutural não prova cron real, VPS/Docker/gateway saudáveis nem dados vivos corretos.
- Checks de produção, runtime e dados vivos continuam em rotinas específicas e/ou exigem aprovação conforme risco.

### Rodada H — Hermes Brain Improvement System

Status: concluída e expandida com instrumentos executivos P0, sem tocar produção, VPS, Docker, bancos, campanhas ou mensagens externas.

Objetivo: transformar o upload Bruno/OpenClaw atualizado e futuros materiais externos em um fluxo repetível de ingestão, documentação, decisão Hermes-native e PRD.

Entregas desta rodada:

1. Rotina `areas/operacoes/rotinas/material-ingest-to-prd.md` para extração segura, inventário, leitura por pasta, comparação com o Brain e geração de PRD.
2. Template `areas/operacoes/templates/matriz-decisao-bruno-hermes.md` para classificar conceitos como aplicar, adaptar, deferir ou rejeitar.
3. Template `areas/operacoes/templates/prd-hermes-brain-improvement.md` para PRDs de melhoria contínua.
4. Rotina `areas/operacoes/rotinas/brain-improvement-score.md` para avaliação executiva de maturidade do Brain.
5. Rotina `areas/operacoes/rotinas/retomada-planos-prds.md` para recuperar planos/PRDs/branches pausados antes de continuar.
6. Projeto `areas/operacoes/projetos/hermes-brain-improvement-system.md` como mapa da iniciativa.
7. Matriz `areas/operacoes/rotinas/area-skill-subagent-agent-decision.md` para evitar agentes/canais permanentes sem volume real.
8. PRD `areas/operacoes/projetos/mission-control-prd.md` para Mission Control read-only.
9. Template `areas/operacoes/templates/report-health-executivo.md` para relatórios executivos.
10. Primeiro score manual `reports/brain-improvement-score-2026-05-09.md` com score geral 88/100.

Regras preservadas:

- Hermes não vira OpenClaw; só adapta o que melhora o Brain.
- Material bruto de terceiros fica fora do repo salvo decisão explícita.
- Rotina documentada não prova cron ativo.
- PR draft pode ser criado; merge em `main`, produção, credenciais, Docker/VPS, banco e ações externas exigem aprovação Lucas.

### Rodada I — Guardrails P1 de operação contínua

Status: concluída como rodada documental segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas ou runtime.

Objetivo: fortalecer o Hermes Brain Improvement System com guardrails para memória, segurança, integrações novas, canais/agentes e fechamento de entregas.

Entregas:

1. Rotina `areas/operacoes/rotinas/memory-hygiene-pendencias.md` para classificar pendências como ativo, bloqueado, aguardando, concluído, arquivado, decisão ou lição.
2. Rotina `areas/operacoes/rotinas/security-checkup.md` para revisar secrets, permissões, prompt injection, integrações, canais, crons e ações sensíveis.
3. Template `areas/operacoes/templates/nova-integracao.md` para documentar ferramentas novas antes de conexão real.
4. Template `areas/operacoes/templates/novo-canal-agente.md` para decidir menor estrutura suficiente antes de criar canal/agente permanente/subagent/cron.
5. Template `areas/operacoes/templates/delivery-summary.md` para encerrar rodadas com entregas, verificações, não alterações, decisões, lições e pendências.

Regras preservadas:

- Documentação e PR podem seguir; produção, secrets, Docker/VPS, banco, campanhas e mensagens externas continuam exigindo aprovação Lucas.
- Novas integrações começam por read-only e escopo mínimo.
- Memória durável não vira log de sessão; Brain segue fonte de verdade.


### Rodada J — Higiene real de memória e pendências

Status: concluída como rodada documental segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas ou runtime.

Objetivo: aplicar a rotina `memory-hygiene-pendencias.md` sobre as pendências reais do Brain e eliminar contradições antigas.

Entregas:

1. `empresa/gestao/pendencias.md` reescrito como fila executiva atual, com itens ativos, bloqueados, aguardando data/evento, concluídos e arquivados.
2. `memories/pending.md` compactado para boot mental, sem log antigo de sessão.
3. `reports/memory-hygiene-2026-05-09.md` criado com fontes, classificação e guardrails.
4. Decisão de autonomia documental de baixo risco registrada em `memories/decisions.md` e `empresa/decisoes/decisoes-permanentes.md`.
5. Meta Ads removido da fila urgente atual, pois `memories/consolidation_weekly/2026-04-28.md` registra correção em 2026-04-25.

Regras preservadas:

- Pendência não vira log de sessão.
- Pendência bloqueada precisa dizer bloqueio e aprovação necessária.
- Estado de cron documentado não prova runtime vivo; usar verificação atual antes de afirmar.
- Produção, infra, secrets, banco e ações externas continuam exigindo aprovação explícita.

### Rodada K — Teste Material Ingest to PRD

Status: concluída como rodada documental segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas ou runtime.

Objetivo: validar a rotina `material-ingest-to-prd.md` em um segundo caso pequeno antes de qualquer automação.

Entregas:

1. Teste em modo leve usando `areas/operacoes/projetos/mission-control-prd.md` como PRD antigo/interno.
2. Artefatos locais fora do repo em `/opt/data/hermes_bruno_ingest/material_ingest_to_prd_test_20260509/`.
3. Relatório `reports/material-ingest-to-prd-test-2026-05-09.md`.
4. Rotina `material-ingest-to-prd.md` atualizada com modo completo vs modo leve.
5. Pendências atualizadas para marcar o teste como concluído e apontar o próximo passo: script executivo local/read-only para `brain_improvement_score`.

Regras preservadas:

- Material bruto externo continua fora do repo.
- Mission Control segue read-only/manual; UI e cron continuam bloqueados por aprovação explícita.
- Nenhuma ação produtiva, runtime ou externa foi executada.

### Rodada L — Script Brain Improvement Score

Status: concluída como rodada documental/tooling local segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas, cron, UI ou runtime.

Objetivo: transformar a rotina manual `brain-improvement-score.md` em um relatório executivo repetível, consumindo o JSON do health check e arquivos versionados do Brain.

Entregas:

1. Script `scripts/brain_improvement_score.py` criado como ferramenta local/read-only.
2. Relatório `reports/brain-improvement-score-2026-05-09-script.md` gerado com score geral 99/100.
3. JSON `reports/brain-improvement-score-2026-05-09-script.json` gerado para evidência estruturada.
4. Rotina `areas/operacoes/rotinas/brain-improvement-score.md` atualizada com comando canônico e limites.
5. Pendências atualizadas para retirar a avaliação do script da fila ativa.

Regras preservadas:

- O script não consulta runtime, VPS, Docker, APIs, bancos, cron real ou dados vivos.
- O score é leitura de saúde estrutural do repo, não prova produção saudável.
- Qualquer cron recorrente, entrega automática por Telegram, UI ou Mission Control visual continua exigindo aprovação explícita.


### Rodada M — Script Retomada de Planos e PRDs

Status: concluída como rodada documental/tooling local segura, sem tocar produção, VPS, Docker, bancos, secrets, campanhas, mensagens externas, cron, UI ou runtime.

Objetivo: transformar a rotina `retomada-planos-prds.md` em relatório manual repetível para quando Lucas disser “seguir”, “retomar” ou “onde paramos”.

Entregas:

1. Script `scripts/retomada_planos_prds.py` criado como ferramenta local/read-only.
2. Relatório `reports/retomada-planos-prds-2026-05-09.md` gerado.
3. JSON `reports/retomada-planos-prds-2026-05-09.json` gerado.
4. Rotina `areas/operacoes/rotinas/retomada-planos-prds.md` atualizada com comando canônico, limites e critérios.
5. Avaliação do cron semanal concluída: não criar cron recorrente agora; usar sob demanda, porque há apenas 1 item ativo e os itens sensíveis estão corretamente bloqueados.

Regras preservadas:

- O script não consulta runtime, VPS, Docker, APIs, bancos, cron real ou dados vivos.
- O relatório ajuda retomada, mas não substitui aprovação para infra, produção, secrets, banco, external send, cron recorrente ou UI.
- Nenhum cron, UI, Mission Control visual ou mensagem automática foi criado.

## Critérios de qualidade para próximas fases

Toda fase deve terminar com:

1. Arquivos no lugar certo.
2. Dados não inventados.
3. Secrets não expostos.
4. Scan de secrets limpo.
5. Commit claro.
6. Push para `main` ou PR, conforme risco.
7. Resumo em português para Lucas.

## Sequência recomendada agora

1. Aprofundar dicionário canônico de influencers/campanhas LK e auditar match influencer → produto — v0.2 concluída em `reports/lk-influencer-operational-roas-v02-2026-05-10.md`; próxima ação: tabela influencer → produto/SKU/tamanho → estoque para Silvia/Helena e investigação de cupom/UTM/landing para Lala.
2. Aplicar `security-checkup.md` no próximo caso de integração/canal/agente/cron antes de executar.
3. Completar subdocs de integrações adicionais somente quando virarem fluxo recorrente real.
4. Usar `scripts/retomada_planos_prds.py` sob demanda antes de retomar planos longos; cron recorrente só se a fila voltar a crescer.
5. Considerar template/skill canônica para relatórios de score se o script for usado em mais rodadas.
6. Mission Control visual, cron recorrente ou entrega automática por Telegram só depois de aprovação de cadência/escopo.

## Atualização contínua obrigatória

A cada rodada de evolução do Hermes Brain:

1. Verificar release atual do Hermes Agent.
2. Avaliar novidades aplicáveis a skills, memória, gateway, crons, ferramentas e segurança.
3. Atualizar skills internas quando o procedimento mudar.
4. Atualizar o Brain, índices e roadmap.
5. Rodar `scripts/brain_health_check.py` e scan de secrets.

## Sistema de memória

Documento canônico: `empresa/gestao/memory-system.md`.

Resumo:

- Memory tool: preferências duráveis do Lucas e regras globais compactas.
- `session_search`: recuperar histórico de conversas e progresso anterior.
- Hermes Brain GitHub: fonte de verdade para negócio, processos, decisões, rotinas, skills e agentes.
- `memories/`: memória executiva compacta por negócio.
- `empresa/` e `areas/`: detalhamento operacional estruturado.
- Dados vivos: Supabase, Shopify, APIs, email e crons.

Motivo: antes de aprofundar operação, vale criar health checks para proteger o Brain e evitar regressão de secrets, links quebrados e estrutura incompleta.
