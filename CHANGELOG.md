# Changelog — Hermes Brain

Registro das principais mudanças estruturais do Hermes Brain após a adaptação Bruno/OpenClaw para o universo Hermes.


## 2026-05-09 — Guardrails P1 de memória, segurança e entrega

- Criada rotina `areas/operacoes/rotinas/memory-hygiene-pendencias.md` para separar pendências ativas, bloqueadas, aguardando, concluídas, arquivadas, decisões e lições.
- Criada rotina `areas/operacoes/rotinas/security-checkup.md` para revisão de secrets, scopes, prompt injection, integrações, canais, crons, produção e ações sensíveis.
- Criados templates `areas/operacoes/templates/nova-integracao.md`, `areas/operacoes/templates/novo-canal-agente.md` e `areas/operacoes/templates/delivery-summary.md`.
- Atualizados `areas/operacoes/MAPA.md`, `empresa/rotinas/_index.md`, projeto do Hermes Brain Improvement System e roadmap.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.

## 2026-05-09 — Instrumentos executivos Bruno P0

- Criada matriz `areas/operacoes/rotinas/area-skill-subagent-agent-decision.md` para decidir área, rotina, skill, subagent, cron ou agente/canal permanente.
- Criado PRD `areas/operacoes/projetos/mission-control-prd.md` para Mission Control Hermes read-only, separando o uso criativo/performance do protocolo operacional.
- Criado template `areas/operacoes/templates/report-health-executivo.md` para relatórios executivos de health, riscos, evidências e aprovações.
- Criado primeiro relatório manual `reports/brain-improvement-score-2026-05-09.md`, com score geral 88/100.
- Atualizados índices, roadmap e pendências relacionadas a Mission Control.
- Produção, Docker/VPS, bancos, secrets, campanhas, mensagens externas e runtime não foram alterados.

## 2026-05-08 — Hermes Brain Improvement System

- Adicionada rotina `areas/operacoes/rotinas/material-ingest-to-prd.md` para transformar material externo em extração segura, inventário, documentação, matriz de decisão e PRD.
- Adicionados templates `areas/operacoes/templates/matriz-decisao-bruno-hermes.md` e `areas/operacoes/templates/prd-hermes-brain-improvement.md`.
- Adicionadas rotinas `brain-improvement-score.md` e `retomada-planos-prds.md` para avaliação executiva do Brain e retomada de planos pausados.
- Criado projeto `areas/operacoes/projetos/hermes-brain-improvement-system.md` com backlog P0/P1/P2.
- Atualizados `areas/operacoes/MAPA.md`, `empresa/rotinas/_index.md` e `ROADMAP-30-DIAS-HERMES.md`.
- Produção, Docker/VPS, bancos, campanhas, mensagens externas e merge em `main` não foram alterados.

## 2026-05-05 — Hermes Docker atualizado para v0.12.0 com imagem custom

- Confirmado via GitHub API que a release upstream mais recente conhecida é `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`.
- VPS `lc.vps` agora roda os dois containers Hermes com `hermes-agent-custom:v0.12.0-20260505`.
- Versão verificada nos dois containers via `/opt/hermes/.venv/bin/hermes --version`: `Hermes Agent v0.12.0 (2026.4.30)`, Python `3.13.5`, OpenAI SDK `2.32.0`.
- Corrigido pós-deploy o travamento de tools causado por `terminal.cwd: telegram`; valor correto preservado em `terminal.cwd: /opt/data`.
- Registrados backups/rollback: `docker-compose.yml.bak.20260503_191723`, `docker-compose.yml.pre-v012-20260505T102618Z` e `data/config.yaml.bak-20260505-cwd-telegram`.
- Documentado checklist para próximos updates: preservar Compose/config, validar `terminal.cwd`, permissões de logs/sessions, versão real, gateway Telegram, cron ticker e tool call.
- Segredos não foram documentados; senha root enviada em chat deve ser tratada como exposta e rotacionada depois.

## 2026-05-05 — Hermes Docker: pull/update seguro executado, imagem sem versão nova

- Lucas autorizou reset da senha root da `lc.vps` via Hostinger e backup/update do Hermes Docker.
- Nova senha root foi gerada e salva no Doppler `VPS_ROOT_PASSWORD`, sem documentar valor.
- Backup leve coletado fora do repo: `/opt/data/hermes_bruno_ingest/backups/lc-vps-hermes-20260505T011529Z`.
- Criada rollback tag: `ghcr.io/hostinger/hvps-hermes-agent:preupdate-20260505T011613Z`.
- Executado `docker compose pull` e `docker compose up -d --no-deps` apenas para `hermes-agent` e `hermes-telegram`.
- Digest da imagem Hostinger `latest` permaneceu `sha256:7fc18af3c7a124b00b8853218cf59296861101d65d6af1dc9d7851277829d6b7`; versão segue `Hermes Agent v0.9.0 (2026.4.13)`.
- Confirmado por GitHub API que upstream `NousResearch/hermes-agent` latest segue `v2026.4.30` / `Hermes Agent v0.12.0 (2026.4.30)`; imagem Hostinger não avançou para essa versão no pull.
- Investigação GHCR read-only confirmou tags públicas Hostinger disponíveis (`latest`, `8eb9eb9`, `ba03513` e aliases sha256); `latest` é alias de `8eb9eb9`, digest atual, e `ba03513` é anterior — não há tag pública Hostinger mais nova nesta data.
- Documentado registro completo em `areas/operacoes/rotinas/hermes-runtime-update-attempt-2026-05-05.md`.
- Traefik, n8n, Paperclip, volumes, redes, firewall, Supabase, Vercel, campanhas e mensagens externas não foram alterados.

## 2026-05-05 — Spiti Hub: PR #92 bundle/code splitting mergeado em dev

- Criado e mergeado em `dev` o PR #92: `https://github.com/spiti-auction/spiti-hub/pull/92`.
- Merge commit: `2943614 perf: split route and pdf bundles (#92)`.
- Implementado code splitting de rotas com `React.lazy`/`Suspense` e `manualChunks` para dependências pesadas de PDF/Recharts.
- Warning de chunks Vite acima de 500 kB eliminado sem elevar `chunkSizeWarningLimit`; maiores chunks pós-build ficaram abaixo de 500 kB.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/0 warnings, build OK sem warning de chunk grande.
- Revisão independente pré-commit aprovada; sugestões futuras não bloqueantes: ErrorBoundary para falhas de chunk e monitoramento de requests após split granular.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #91 mergeado em dev

- Criado e mergeado em `dev` o PR #91: `https://github.com/spiti-auction/spiti-hub/pull/91`.
- Merge commit: `e8d4de4 chore: resolve hook and fast refresh lint warnings (#91)`.
- Warnings de lint reduziram de 8 para 0, mantendo 0 errors.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/0 warnings, build OK.
- Registrado aviso Vercel bot: preview/deploy pode falhar porque `@hermes-agent` não é membro do time Vercel da `spiti-auction`; nenhuma alteração em Vercel/team/billing/settings foi feita.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #90 mergeado em dev

- Criado e mergeado em `dev` o PR #90: `https://github.com/spiti-auction/spiti-hub/pull/90`.
- Merge commit: `49b5c84 chore: remove unused lint warnings (#90)`.
- Warnings de lint reduziram de 39 para 8, mantendo 0 errors.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/8 warnings, build OK.
- Os 8 warnings restantes foram preservados para rodada própria porque envolvem hooks/Fast Refresh.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR #89 mergeado em dev

- PR #89 (`chore: redact edge function secret examples`) foi squash-mergeado em `dev` do `spiti-auction/spiti-hub`.
- Merge commit: `ae625a2 chore: redact edge function secret examples (#89)`.
- Branch `hermes/spiti-hub-secrets-lint-hardening` removida após merge.
- Clone local sincronizado em `dev...origin/dev`.
- Produção/`main`, Supabase, Vercel configs, VPS, Docker, campanhas e mensagens externas não foram alterados.

## 2026-05-04 — Spiti Hub: PR de hardening aberto

- Clonado `spiti-auction/spiti-hub` via Git usando `GITHUB_SPITI_HUB_TOKEN` sem embutir token no remote.
- Criada branch `hermes/spiti-hub-secrets-lint-hardening` a partir de `dev`.
- Commit no Spiti Hub: `8c8549b chore: redact edge function secret examples`.
- Aberto PR #89 para `dev`: `https://github.com/spiti-auction/spiti-hub/pull/89`.
- Verificações locais: `git diff --check` OK, secret scan 0, lint 0 errors/39 warnings, build OK.
- Nenhum merge ou alteração em produção foi executado.

## 2026-05-04 — Spiti Hub: token salvo no Doppler

- Salvo no Doppler `lc-keys/prd` o secret `GITHUB_SPITI_HUB_TOKEN` para acesso ao repo privado `spiti-auction/spiti-hub`.
- Verificação segura confirmou acesso ao repo com permissões administrativas/push sem imprimir o token.
- Atualizados docs de integração GitHub e contexto SPITI Hub com o nome do secret, sem valor.
- Como o token foi enviado por chat, segue recomendado rotacionar/revogar depois da sequência de PR e substituir no Doppler.

## 2026-05-04 — Spiti Hub: hardening local sem push

- Redigida localmente a cópia de `docs/deploy-edge-functions.md` do Spiti Hub para substituir assignments secret-like de Google OAuth/refresh token por placeholders.
- Rodado `eslint --fix` localmente, reduzindo warnings de lint de 46 para 39, com 0 errors.
- Build local segue OK; warning de bundle grande permanece.
- Secret scan local pós-redação retornou 0 achados nos padrões verificados.
- Nenhum push/PR no Spiti Hub foi feito: token válido para `spiti-auction/spiti-hub` ainda precisa ser colocado em Doppler; PAT colado em chat deve ser rotacionado/revogado.

## 2026-05-04 — Rodada E: inventário GitHub do Spiti Hub

- Confirmado acesso ao repo privado `spiti-auction/spiti-hub`, projeto operacional novo da SPITI.
- Criado `areas/spiti/contexto/spiti-hub-github.md` com inventário inicial, relação com o Hermes Brain, regras de segurança e próximos passos.
- Atualizados `areas/spiti/MAPA.md`, `empresa/integracoes/github.md` e roadmap.
- Verificações locais do Spiti Hub: install OK, lint OK com warnings, build OK.
- Nenhuma alteração foi feita em GitHub remoto, Supabase, Vercel, VPS, Docker, campanhas ou mensagens externas.
- Token GitHub enviado por chat não foi documentado; recomendada migração para Doppler e rotação/revogação depois.

## 2026-05-04 — Rodada D: templates Zipper por subárea

- Criados templates Zipper para consulta read-only de `vendas_tango`, registro pós-contato com colecionador, checklist de feira por fase e briefing de publicação obra/artista.
- Atualizados mapas das subáreas Zipper, mapa principal, índice de rotinas e roadmap.
- Preservadas regras de separação Zipper Vendas vs SPITI, tom Zipper e aprovação Lucas/Osmar antes de contato, negociação, proposta ou publicação externa.
- Fase documental segura: nenhuma consulta/alteração em produção, Docker, VPS, banco, campanhas ou mensagens externas.

## 2026-05-04 — Rodada C: playbooks operacionais LK/Zipper/SPITI

- Criados playbooks LK para comando diário e campanha CRM aprovada.
- Criados playbooks Zipper para abordagem obra/colecionador e execução de feira.
- Criados playbooks SPITI para pregão ao vivo e divergência de lances.
- Atualizados mapas de áreas, índice de rotinas e roadmap.
- Fase documental segura: nenhuma consulta/alteração em produção, Docker, VPS, campanhas ou mensagens externas.

## 2026-05-04 — Diagnóstico read-only do Hermes Gateway

- Executado diagnóstico read-only do Gateway/Telegram na VPS sem restart, kill, update, alteração de env/compose ou mudança Docker/root.
- Criado `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` com evidências e classificação H1/H2/H3/H4.
- Atualizados observabilidade, plano de remediação, roadmap e índice de rotinas.
- Conclusão operacional: detector de gateway em Docker foreground provavelmente diverge do processo real; conflito Telegram parece histórico/transitório no momento da coleta.

## 2026-05-04 — Planos seguros para Gateway e update Hermes

Commit: `docs: add Hermes gateway and runtime update plans`

Entregas:

- Criado plano de diagnóstico/correção segura do gateway Telegram, separando hipóteses, evidências, escopo read-only, ações bloqueadas e critérios de sucesso.
- Criado plano de update do runtime Hermes `v0.9.0` → `v0.12.0` com pré-condições, backup, rollback e validações pós-update.
- Atualizado índice de rotinas e roadmap para deixar claro que correção/update exigem aprovação Lucas antes de qualquer alteração em Docker/VPS/root.
- Corrigida orientação antiga de troubleshooting rápido que sugeria restart via `systemctl`; no footprint atual Hermes roda em Docker/Hostinger e restart é ação sensível.

## 2026-05-04 — Observabilidade Hermes runtime/gateway

Commit: `docs: add Hermes runtime observability routine`

Entregas:

- Documentada rotina read-only para observar versão, containers, gateway, cron interno e logs do Hermes na VPS.
- Registrado gap entre runtime Hostinger observado (`Hermes Agent v0.9.0`) e release upstream (`Hermes Agent v0.12.0`, `v2026.4.30`).
- Registrada divergência operacional: processo `hermes gateway run` existe no container Telegram, mas `hermes cron status` reporta gateway não running.
- Registrado warning de conflito de polling Telegram sem aplicar restart, update ou alteração em Docker/VPS/root.
- Atualizados `areas/tecnologia/contexto/hermes-docker-footprint.md`, `areas/operacoes/rotinas/hermes-release-watch.md`, `empresa/rotinas/_index.md` e roadmap.

## 2026-05-04 — Integrações por ferramenta e rotinas seguras

Commit: `docs: deepen integration operating routines`

Entregas:

- Corrigido troubleshooting genérico de Supabase em `TOOLS.md` para apontar nomes específicos por base.
- Validado que os nomes reais de secrets das integrações críticas existem no Doppler, sem imprimir valores.
- Criadas rotinas operacionais para validação de secrets, Shopify read-only, Supabase audit, Evolution/WhatsApp approval, Klaviyo approval, Meta Ads reporting e Hostinger/VPS inventory.
- Atualizados `empresa/integracoes/MAPA.md`, `empresa/rotinas/_index.md` e roadmap com o estado da Rodada B.

## 2026-05-04 — Manual operacional do Brain

Commit: `65a3cfa docs: add Hermes Brain operating manual`

Entregas:

- Criado `START-HERE.md` como manual operacional de entrada.
- Atualizado `README.md` para apontar primeiro para `START-HERE.md`.
- Documentada a ordem de navegação: regras globais → memórias → empresa → áreas → agentes → skills/rotinas → segurança.
- Documentados procedimentos por tipo de tarefa: pergunta de negócio, comunicação externa, automação, skill, bug e credenciais.

## 2026-05-04 — Segurança e permissões por área

Commit: `86d9097 docs: align security permissions with Hermes areas`

Entregas:

- Expandido `seguranca/permissoes.md`.
- Expandido `seguranca/acoes-sensiveis.md`.
- Criado modelo de níveis L0-L5 para ações sensíveis.
- Documentados limites por agente e por negócio.
- Reforçado Doppler `lc-keys/prd` como fonte de verdade de credenciais.
- Reforçada aprovação Lucas para ações externas, produção, dados e credenciais.

## 2026-05-04 — Índices executivos globais

Commit: `9fdaa96 docs: add executive Brain navigation indices`

Entregas:

- Corrigido `README.md` para identificar o repo como Hermes Brain real, não draft.
- Expandido `areas/MAPA.md` com índice executivo de áreas e sub-áreas.
- Expandido `empresa/MAPA.md` com mapa cross-área.
- Criado `empresa/rotinas/_index.md`.
- Criado `empresa/skills/_index.md`.

## 2026-05-04 — Zipper e SPITI operacionalizados

Commit: `6753205 docs: map Zipper and SPITI operating routines`

Entregas:

- Expandido `areas/zipper/MAPA.md`.
- Expandido Zipper em sub-áreas: vendas de obras, colecionadores, feiras e comunicação.
- Criadas rotinas Zipper: consulta de vendas, abordagem de colecionadores e planejamento de feiras.
- Expandido `areas/spiti/MAPA.md`.
- Criadas rotinas SPITI: verificação de lances, alerta de lances e relatório de leilão.
- Reforçada separação Zipper Vendas vs SPITI.
- Reforçada regra SPITI: email é fonte de verdade para lances; meta tag não é lance atual.

## 2026-05-04 — LK CRM, skills e rotinas

Commit: `f08d2b9 docs: map LK CRM routines and skills`

Entregas:

- Expandido `areas/lk/MAPA.md`.
- Expandido `areas/lk/sub-areas/crm/MAPA.md`.
- Criada navegação de área para skills LK cross-sell e leads esfriando.
- Documentadas rotinas LK: RFM semanal, outcomes tracker, consequence tracker e sync log.

## 2026-05-04 — Remediação de secrets versionados

Commit: `bcab06f fix: remove hardcoded secrets from Hermes Brain`

Entregas:

- Redigidos token-like values em docs/memórias.
- Scripts passaram a buscar credenciais por ambiente/Doppler.
- Adicionados erros explícitos quando env vars obrigatórias estão ausentes.
- Scan de secrets retornou `possible_secrets 0` antes do push.

Observação de segurança:

- Tokens que apareceram em chat/log/repo devem ser rotacionados/revogados quando a sequência operacional terminar.

## 2026-05-04 — Padronização de agentes

Commit: `eff6287 docs: standardize Hermes Geral LK and Zipper agent docs`

Entregas:

- Padronizados documentos de agentes Hermes Geral, LK e Zipper.
- Preservadas identidades/regras ricas existentes.
- Adicionados docs de ferramentas, usuário, memória e heartbeat.

## 2026-05-04 — Estrutura Bruno/OpenClaw adaptada ao Hermes

Commit: `fb61b2a docs: adapt Bruno OpenClaw structure for Hermes Brain (#1)`

Entregas:

- Estrutura de áreas, empresa, segurança e agentes aplicada ao repo real.
- `memories/` preservado como memória executiva compacta.
- Adicionada arquitetura compatível com Bruno/OpenClaw, mas filtrada pela lógica Hermes.

## Estado atual

A adaptação estrutural base está aplicada em `main`.

O Brain agora tem:

- manual de entrada;
- README correto;
- índices executivos;
- áreas e sub-áreas por negócio;
- rotinas documentadas;
- skills indexadas;
- agentes padronizados;
- permissões e ações sensíveis;
- scan de secrets limpo na última rodada.
