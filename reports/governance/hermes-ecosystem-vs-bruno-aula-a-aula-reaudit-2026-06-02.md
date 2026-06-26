# Auditoria — Ecossistema Hermes vs método Bruno/OpenClaw aula a aula

Data: 2026-06-02  
Escopo: reauditoria local/read-only do ecossistema Hermes/Brain contra o material Bruno/OpenClaw já ingerido.  
Pedido de Lucas: “comparar nosso ecossistema Hermes com o ecossistema sugerido pelo Bruno; reler aula por aula e ver se falta alguma coisa.”

## Fontes lidas/revalidadas

### Material Bruno/OpenClaw

- Curso extraído em `/opt/data/hermes_bruno_ingest/bruno_upload_20260508_204305_analysis/texts/`.
- Aulas revalidadas: A0/A00 visão, vitrine 3 agentes, A1 setup, A2 cockpit, A3 starter kit, A4 Telegram, A5 identidade, A6 workspace/MAPAs, A7 memória/contexto, A8 skills, A9 crons/heartbeat, A10 segurança, A11 canais, A12 integrações, A13 multi-agente, A14 Mission Control e A15 fechamento.
- Mapa pedagógico lido: `STARTER_KIT_starter-kit_skills_starter_onboarding-checklist_references_mapa-aulas.md.txt`.
- Auditorias históricas usadas como baseline:
  - `reports/bruno-atual-hermes-adaptation-audit-2026-05-19.md`.
  - `reports/governance/brain-bruno-correctness-audit-2026-05-22.md`.

### Estado Hermes/Brain atual

- Manual canônico: `areas/hermes/operacoes/manual-producao/README.md`.
- Matriz de profiles: `areas/hermes/operacoes/manual-producao/PROFILE_STATUS_MATRIX.md`.
- Matriz de capabilities: `areas/hermes/operacoes/manual-producao/CAPABILITIES_ADOPTION_MATRIX.md`.
- Runbook runtime: `areas/hermes/operacoes/manual-producao/RUNTIME_REPAIR_RUNBOOK.md`.
- Política de memória: `memories/politica-memoria-hermes.md`.
- Hot/current: `memories/hot.md`.
- Inventário crons/profiles: `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- Live cron registry via `cronjob list` em 2026-06-02.
- Brain health check gerado: `reports/brain-health-check-2026-06-02-bruno-ecosystem-reaudit.json`.

## Veredito executivo

O ecossistema Hermes está **mais maduro do que o padrão base sugerido pelo Bruno/OpenClaw** em segurança, multiempresa, profiles, toolsets, crons, receipts, aprovação e memória rica via Brain.

Mas a reauditoria mostra que ainda não está “fechado” no padrão Bruno adaptado para Hermes. O ponto principal não é instalar mais coisa; é **reduzir drift entre documentação, runtime e memória current**.

Nota honesta atual: **8,6/10**.

- Subiu vs auditorias anteriores porque memória, manual canônico, profiles, runtime repair, capabilities matrix e ciclo 01h/02h/02h15/02h30 foram formalizados.
- Não é 10/10 porque ainda há docs com linguagem 23h legada, skills sem inventário formal completo, Kanban/plugins/hooks/goals sem piloto controlado vivo, algumas rotinas externas com erro conhecido e o novo handoff 01h ainda precisa ser observado no próximo ciclo real.

## Aula por aula — comparação Bruno → Hermes

### A0 / Aula 00 — visão, stack e investimento

**Bruno ensina:** agente não é chat; é um funcionário digital com modelo, canal, ferramentas, memória e operação diária.  
**Hermes atual:** alinhado e acima do básico: Telegram, profiles, tools, skills, cron, session_search, Brain, MCP parcial, relatórios e aprovação.  
**Gap:** transformar a visão em cockpit ainda mais simples para Lucas: “o que está vivo, o que está degradado, o que precisa decisão”.  
**Status:** bom, P1 observabilidade/cockpit.

### Vitrine / cases dos 3 agentes

**Bruno ensina:** olhar Amora e outros cases como benchmark de maturidade, não como cópia literal.  
**Hermes atual:** correto: Hermes Geral atua como COO/orquestrador; especialistas por domínio; Brain central; guardrails fortes.  
**Gap:** alguns especialistas ainda dependem de confirmação de round-trip e rotinas próprias para serem considerados operacionalmente maduros.  
**Status:** bom, P1 maturidade de especialistas.

### A1 — setup / dar vida ao agente

**Bruno ensina:** primeiro canal + credenciais + smoke test + entendimento do que está ativo.  
**Hermes atual:** Telegram principal e múltiplos profiles ativos/preparados; STT/voz funcionando no gateway; modelo principal atual documentado.  
**Gap:** profile configurado ainda pode ser confundido com profile realmente operacional; a matriz diz para revalidar, mas o status envelhece.  
**Status:** bom, precisa revalidação antes de qualquer afirmação live.

### A2 — cockpit do terminal / doctor / troubleshoot

**Bruno ensina:** terminal é cockpit operacional; health, status, restore, doctor e verificação antes de agir.  
**Hermes atual:** tem runbook canônico, health check, cron list, scripts watchdog, receipts e política de aprovação.  
**Gap:** cockpit humano ainda está documental; dashboard/API/Mission Control ainda não é um cockpit operacional completo e seguro para Lucas.  
**Status:** parcialmente atendido; P1 dashboard/cockpit local seguro.

### A3 — Starter Kit

**Bruno ensina:** pacote lido pelo agente, checklist viva, templates, prompts, workspace e validações.  
**Hermes atual:** tem manual de produção, policy, profile matrix, capabilities matrix, runbook, Brain MAPAs e skills.  
**Gap:** ainda falta um “Hermes Brain Starter Kit” único para onboarding/reparo de novo especialista: criar profile, identidade, toolsets, memory boot, Brain subárea, watchdog, receipts e smoke tests.  
**Status:** bom, mas falta empacotar como starter kit Hermes-native.

### A4 — Telegram organizado por tema

**Bruno ensina:** Telegram é canal operacional; grupos/tópicos/menções precisam de regra clara.  
**Hermes atual:** Telegram é canal principal; Lucas quer só alertas acionáveis; profiles especialistas existem.  
**Gap:** precisa manter matriz de canal/profile/bot/round-trip sempre fresca; alguns watchdogs específicos de gateway estão pausados enquanto watchdog global existe, o que precisa ficar claro para não parecer cobertura duplicada/ausente.  
**Status:** bom, P0 evitar ruído e confusão live vs pausado.

### A5 — identidade, SOUL, USER, AGENTS

**Bruno ensina:** agente sem identidade vira chat genérico; SOUL/IDENTITY/USER/AGENTS precisam guiar comportamento.  
**Hermes atual:** há organograma, perfil default, especialistas, manual, guardrails e memória compactada.  
**Gap:** manter uniformidade dos pacotes por especialista e evitar que `USER.md`/`MEMORY.md` virem Brain inteiro.  
**Status:** bom após correções; P1 auditoria periódica dos pacotes de identidade.

### A6 — workspace + MAPAs distribuídos

**Bruno ensina:** MAPA local diz onde salvar e buscar; workspace precisa ser navegável.  
**Hermes atual:** Brain tem MAPA, áreas, empresa, agentes, rotinas, reports, manual canônico.  
**Gap:** existem documentos antigos e inventários longos ainda com linguagem do ciclo 23h; isso é histórico útil, mas alguns trechos ativos ainda podem confundir.  
**Status:** bom, P0 limpar ponteiros ativos 23h → 01h sem apagar histórico.

### A7 — memória + higiene de contexto

**Bruno ensina:** separar boot memory, memória rica, hot/current, dailies, compactação e reset.  
**Hermes atual:** muito alinhado agora: `memories/politica-memoria-hermes.md`, `hot.md`, receipts, dailies, Brain como fonte rica, provider externo rejeitado, watchdog 02h15.  
**Gap:** `hot.md` ainda contém algumas referências a 23h e à versão/runtime antiga; precisa acompanhar a mudança para 01h e v0.15.2 quando o fechamento novo rodar.  
**Status:** forte, mas exige manutenção diária real.

### A8 — skills

**Bruno ensina:** prompt resolve uma vez; skill resolve mil vezes. Skill deve ter gatilho, passos, output e verificação.  
**Hermes atual:** usa skills de forma intensa e obrigatória; skills críticas existem para Hermes, Brain, LK, Shopify, SEO, MCP, GitHub, etc.  
**Gap:** ainda falta inventário formal de skills com owner, status, risco, última revisão, última execução e depreciação. Há auditoria de safety, mas não uma matriz operacional completa.  
**Status:** P0/P1 pendência real.

### A9 — crons + heartbeat

**Bruno ensina:** cron é cadência; heartbeat é respiração; sucesso saudável deve ser silencioso.  
**Hermes atual:** muito forte: 29 jobs, padrão `local`/silent-OK, no_agent watchdogs, relatório executivo desejado para Lucas, ciclo 01h/02h/02h15/02h30.  
**Gaps vivos:**

- `last_status=error` em rotinas externas LK/Zipper por WACLI/entrega externa ou timeout conhecido.
- `LK Weekly Collection Sort Rule B` com erro persistente.
- `LK Weekly Catalog Badges BEST SELLER sync` ainda sem primeira execução.
- Validador do novo ciclo ainda acusa ausência de `reports/daily-consolidation/latest-handoff.json` até o primeiro 01h real pós-mudança.

**Status:** arquitetura forte, execução com P0/P1 runtime backlog.

### A10 — segurança operacional

**Bruno ensina:** cofre, escopo mínimo, APIs com cuidado, prompt injection, canal público e rollback.  
**Hermes atual:** acima do padrão: guardrails Docker/VPS/Traefik/secrets/externos, read-only por padrão, approvals, secret scan e receipts.  
**Gap:** default API/webhook bind foi documentado como `0.0.0.0`; qualquer mudança de exposição exige plano/rollback/aprovação.  
**Status:** forte; manter bloqueios.

### A11 — outros canais

**Bruno ensina:** cada canal precisa regra de uso, ruído, escopo e permissão.  
**Hermes atual:** Telegram principal, bots especialistas, WhatsApp/WACLI em rotinas aprovadas, e-mail/relatórios externos em scripts.  
**Gap:** falhas WACLI recentes mostram que canais externos aprovados precisam health próprio e receipt sem spam.  
**Status:** parcialmente bom; P1 canal externo health/reauth packet.

### A12 — integrações via API/CLI

**Bruno ensina:** integração só com auth, dry-run, teste, monitoramento e escopo.  
**Hermes atual:** integrações existem/planejadas com Shopify, Tiny, Metricool, Meta, DataForSEO, Supabase, etc.; MCP policy e pilots read-only criados.  
**Gap:** MCP de negócio ainda está em política/pilotos, não em operação ampla; isso é correto por segurança, mas ainda é lacuna de maturidade operacional.  
**Status:** bom, expansão só por piloto read-only.

### A13 — multi-agente / subagentes

**Bruno ensina:** começar com 1 agente forte; criar agentes paralelos só quando domínio contínuo justificar.  
**Hermes atual:** alinhado: default orquestra; especialistas LK Shopify/Ops/Growth/Trends/Mordomo/SPITI isolados; delegation usada para subtarefas.  
**Gap:** Kanban ainda não é board vivo de trabalho durável; delegation resolve sessão, não governança persistente.  
**Status:** bom; P1 piloto Kanban seguro.

### A14 — Mission Control

**Bruno ensina:** Mission Control é cockpit customizado avançado: estado, aprovações, execução em chunks, receipts e iteração por Telegram.  
**Hermes atual:** manual de produção, capability matrix, receipts, aprovação e relatórios existem; dashboard/API classificado; Mission Control conceitualmente correto.  
**Gap:** ainda falta cockpit operacional único e seguro que Lucas use no dia a dia; hoje a verdade está em docs/relatórios + Telegram, não numa UI madura.  
**Status:** P1/P2, não bloqueia operação, mas é lacuna de maturidade.

### A15 — fechamento

**Bruno ensina:** o produto real é prática diária + memória + automações + aprendizado contínuo.  
**Hermes atual:** muito alinhado: ciclo 01h/02h/02h15/02h30, learning loop semanal, memory watchdog, runtime truth reconciler, Mesa COO.  
**Gap:** primeiro ciclo completo com novo handoff 01h ainda precisa ser observado; docs antigas com 23h precisam ser reconciliadas para não voltar a confundir o agente.  
**Status:** forte, aguardando primeira execução real do novo ciclo.

## Lacunas reais encontradas

### P0 — corrigir drift de documentação ativa 23h → 01h

Evidência: busca direcionada encontrou referências ativas a “Fechamento 23h” em `TOOLS.md`, `areas/operacoes/intelligence-map.md`, `areas/operacoes/inventarios/crons-agentes-profiles.md`, `memories/hot.md` e uma skill de Brain Sync. Parte é histórico aceitável; parte ainda parece instrução viva.

Ação recomendada: patch documental local, sem mexer em runtime:

- atualizar ponteiros vivos para `Fechamento Ágil 01h + Brain Sync`;
- marcar trechos 23h como históricos/superseded;
- manter BRD 23h como evidência histórica.

### P0 — observar/validar o primeiro ciclo real 01h → 02h → 02h15 → 02h30

Evidência: validador novo retornou `missing 01h handoff: reports/daily-consolidation/latest-handoff.json`, esperado antes da primeira execução 01h real.

Ação recomendada:

- não mexer agora por ansiedade;
- após o próximo ciclo, verificar se o handoff nasceu, se o 02h consumiu, se o 02h15 escreveu receipt e se o 02h30 reportou tudo limpo.

### P0/P1 — auditoria formal de skills

Evidência: capability matrix reconhece alto uso de skills; auditorias anteriores apontam falta de owner/status/risco/última revisão/última execução.

Ação recomendada:

- criar `areas/operacoes/inventarios/skills-control-plane.md`;
- classificar skills críticas: Hermes, Brain, LK, Shopify, SEO, MCP, DevOps, crons, runtime;
- marcar skill grande demais/risco de bloat e skills obsoletas.

### P1 — health dos canais externos WACLI/entrega externa

Evidência live cron: rotinas LK/Zipper com `last_status=error` em scripts de entrega externa/read-only, sem delivery error do scheduler.

Ação recomendada:

- abrir frente própria de triagem read-only dos scripts/outputs;
- não reautenticar WhatsApp/WACLI ou mexer em canal externo sem approval packet.

### P1 — Kanban como trabalho durável

Evidência: capability matrix diz que Kanban está parcialmente configurado/subutilizado.

Ação recomendada:

- piloto local/read-only `hermes-lk-improvements` com cards não atribuídos inicialmente;
- sem dispatcher produtivo até lanes/guardrails testados.

### P1/P2 — cockpit/Mission Control operacional

Evidência: há manual e matriz, mas não cockpit único seguro para Lucas.

Ação recomendada:

- priorizar cockpit local/read-only de status, decisões, crons, profiles e receipts;
- não expor API/dashboard publicamente sem aprovação/rollback.

### P2 — plugins/hooks/goals/batch

Evidência: matrix classifica como pouco usados ou subutilizados.

Ação recomendada:

- só depois de P0/P1: plugin local read-only de capability cards, hook local de receipts, goals para tarefas documentais e batch para auditoria de docs/skills.

## O que não falta / não deve ser copiado

- Não falta “mais memória externa”: Lucas rejeitou Mem0/provider externo; Brain é fonte rica.
- Não falta copiar OpenClaw literalmente: Hermes-native é o caminho certo.
- Não falta criar 60+ crons: Bruno/Amora é benchmark; Hermes deve preservar silent-OK e baixa superfície Telegram.
- Não falta relaxar segurança: Hermes está mais seguro que o padrão base e deve continuar assim.
- Não falta mais agentes por padrão: primeiro fechar contratos, handoffs, round-trip e runtime truth dos especialistas existentes.

## Plano seguro recomendado

1. **P0 documental:** reconciliar docs ativos 23h → 01h e deixar 23h apenas como histórico.
2. **P0 pós-ciclo:** amanhã conferir artefatos reais do ciclo 01h/02h/02h15/02h30.
3. **P1 skills:** criar control plane de skills com owner/status/risco/revisão.
4. **P1 canais externos:** gerar approval packet para triagem WACLI/rotinas externas que estão em erro.
5. **P1 Kanban:** piloto local/read-only para backlog de melhorias Hermes/LK.
6. **P2 cockpit:** Mission Control/dashboard local de observabilidade, sem exposição pública.

## Verificações executadas

- `cronjob list`: 29 jobs; 25 ativos; 4 pausados; erros vivos conhecidos em rotinas LK/Zipper e sort rule; relatório Hermes 01h+02h+02h15 ativo; memory watchdog 02h15 ativo.
- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-02-bruno-ecosystem-reaudit.json`: `FAIL=0`, `WARN=0`.
- `python3 /opt/data/scripts/hermes_nightly_governance_artifacts_check.py --mode digest`: acusou apenas ausência esperada do handoff 01h antes da primeira execução real.

## Conclusão

O Hermes está seguindo o método Bruno no que importa: agente com identidade, Brain, memória, skills, crons, canais, integrações, multi-agente, segurança e fechamento contínuo.

O que falta agora é menos “construir do zero” e mais **higiene de maturidade**:

- remover drift 23h dos docs vivos;
- provar o novo ciclo 01h completo com artefatos reais;
- formalizar inventário de skills;
- tratar erros de canais externos em frente própria;
- pilotar Kanban/cockpit/plugins com escopo read-only.

Status final: **correto e maduro, mas ainda com lacunas P0/P1 de governança viva**.
