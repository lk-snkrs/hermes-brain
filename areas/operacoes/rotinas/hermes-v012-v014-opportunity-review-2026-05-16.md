# Hermes v0.12–v0.14 — Opportunity Review Lucas/Cimino

Data: 2026-05-16
Fonte: GitHub Releases API `https://api.github.com/repos/NousResearch/hermes-agent/releases` + estado local `Hermes Agent v0.14.0 (2026.5.16)` + inventário de crons.
Modo: análise/read-only/documentação. Nenhuma alteração em Docker, gateway, host, secrets, bancos, Shopify, Meta/Google, Klaviyo ou envios externos.

## Síntese executiva

A v0.12–v0.14 muda o Hermes de “agente que responde e executa” para “sistema operacional de agentes”: autocuradoria, metas persistentes, Kanban durável, crons script-only, verificadores de escrita, botões de aprovação, handoff, subgoal, integração Teams/Graph, browser mais rápido, busca X, proxy OpenAI-compatible e watchers padronizados.

No ambiente do Lucas, várias bases já foram adotadas: runtime v0.14, watchers silenciosos, Zipper OS cockpit, Mordomo, host observability, curator ativo e ciclo diário. As maiores melhorias agora são de uso operacional e governança, não de upgrade técnico.

## O que veio em cada release e impacto

### v0.12 — Curator / self-improvement / skills / cron chaining

Novidades úteis:
- Curator autônomo para revisar, consolidar e arquivar skills.
- Self-improvement loop melhor: rubricado, favorece atualizar skills recém-usadas, suporta `references/` e `templates/`.
- `context_from` e `workdir` em cron.
- Skills novas/promovidas: Humanizer, claude-design, design-md, Airtable, ComfyUI, TouchDesigner, etc.
- Providers e gateway/plugin surface ampliados.
- Prompt cache configurável e ganhos de performance.

Adoção atual:
- Curator está habilitado; último run há 4 dias.
- Daily improvement já usa skills e documentação.
- Alguns crons usam `workdir`/toolsets; nem todos usam `context_from`.

Melhorias recomendadas:
1. Criar uma rotina mensal “Skills hygiene review” curta para verificar skills com muita atividade e alto risco operacional.
2. Padronizar `context_from` entre jobs encadeados, especialmente Zipper/Mordomo/LK, para reduzir repetição e custo.
3. Usar Humanizer/claude-design/design-md no pipeline de mensagens/artefatos quando houver comunicação Lucas-facing ou LP/email visual, sempre em preview.

### v0.13 — Tenacity / Kanban / goal / no_agent / segurança

Novidades úteis:
- Kanban multi-agent durável com heartbeat, reclaim, zombie detection e retry.
- `/goal` para manter o agente travado em uma meta entre turnos.
- Cron `no_agent` para watchdogs script-only: stdout vazio = silêncio.
- Checkpoints v2 e auto-resume de sessões após restart.
- Post-write delta lint em `write_file`/`patch`.
- Segurança: redaction default ON na release, allowlists, WhatsApp strangers reject, prompt-injection scan em cron.
- Shopify optional skill.
- Dashboard com plugins/profiles e reverse-proxy support.

Adoção atual:
- Watchdogs `no_agent` já estão em produção e silenciosos.
- Zipper/Mordomo/LK já usam cron/watchdog.
- `/goal`/Kanban ainda não parecem incorporados como hábito operacional diário.

Melhorias recomendadas:
1. Transformar tarefas longas aprovadas em `/goal` + `/subgoal` em vez de sessões soltas.
2. Usar Kanban para “Lucas Ops Board” com trilhas Zipper, LK, SPITI, Hermes, mas sem workers automáticos no começo.
3. Fazer auditoria dos jobs com prompt agentic que poderiam virar `no_agent` para reduzir custo/ruído.
4. Avaliar skill Shopify apenas read-only para relatórios LK e validações, sem permissão de write.

### v0.14 — Foundation / handoff / subgoal / buttons / verifier / watchers / performance

Novidades úteis:
- Runtime v0.14 instalado e saudável.
- `/handoff` transfere sessão viva para outro modelo/persona/profile.
- `/subgoal` adiciona critérios a um `/goal` ativo.
- Botões nativos do `clarify` no Telegram/Discord.
- Per-turn file-mutation verifier: confirma o que realmente mudou no disco.
- LSP semantic diagnostics em `write_file`/`patch`.
- Watchers skill para RSS/HTTP JSON/GitHub polling via `no_agent`.
- Browser/CDP 180x mais rápido e cold start muito menor.
- `vision_analyze` entrega pixels a modelos com visão.
- `x_search` first-class.
- API server expõe approval events; útil para UI/ops.
- OpenAI-compatible local proxy para usar provedores OAuth em ferramentas externas.
- Microsoft Graph/Teams foundation.
- `ctx.llm` em plugins.

Adoção atual:
- Runtime já em v0.14.
- Watchers silenciosos e Zipper OS cockpit já foram criados.
- Approvals estruturadas foram incorporadas à skill.
- O uso de `/handoff`, `/subgoal`, botões e browser rápido ainda pode virar hábito/produto.

Melhorias recomendadas:
1. Padronizar mensagens A2/A3/A4 com botões: Aprovar escopo / Ajustar / Preview only / Bloquear, sempre com escopo, payload, risco e rollback inline.
2. Criar watchdogs de mudança real via RSS/HTTP/GitHub para releases Hermes, status APIs e artefatos obrigatórios, evitando crons agentic quando não há raciocínio necessário.
3. Usar `/handoff` como ritual quando uma missão muda de pesquisa para execução, ou quando precisa trocar modelo/perfil.
4. Usar `/subgoal` para acrescentar critérios de qualidade sem reabrir contexto inteiro.
5. Explorar `x_search`/browser rápido para social listening e SERP/ads/research, inicialmente read-only.
6. Avaliar Teams/Graph para pipeline de reuniões somente se Lucas realmente usar Teams como fonte operacional.
7. Manter local proxy e API approval events como “later/infra”: úteis, mas expor endpoint é A3/A4.

## Matriz de oportunidades priorizadas

### P0 — já deveria virar padrão operacional

1. `Goal/subgoal` para missões longas
- Benefício: menos “seguir”, menos perda de foco.
- Risco: baixo, uso manual.
- Próximo passo: sempre que Lucas pedir algo amplo, iniciar com plano de `/goal` ou sugerir uso explícito.

2. Botões de aprovação estruturada
- Benefício: decisões mais rápidas e auditáveis.
- Risco: baixo se o payload estiver inline; alto se botão for genérico.
- Próximo passo: usar em qualquer pedido A2/A3/A4, nunca para expandir escopo.

3. Watchdogs silenciosos v0.14
- Benefício: menos ruído e custo.
- Risco: baixo se read-only e stdout vazio em OK.
- Próximo passo: inventário semanal de crons; converter checks mecânicos para `no_agent`.

### P1 — implementar como workflow Brain/Ops

4. Lucas Ops Board Kanban sem workers automáticos
- Benefício: visão única multiempresa.
- Risco: baixo se board é local/manual; médio com workers/daemon.
- Próximo passo: criar board com colunas Backlog, Doing, Waiting Lucas, Waiting External, QA, Done e cards sem agente autônomo.

5. Context chaining entre crons
- Benefício: menos repetição, relatórios mais coerentes, menos tokens.
- Risco: baixo, mas exige design para não propagar stale context.
- Próximo passo: mapear jobs que consomem outputs de outros.

6. Social/listening read-only com x_search/browser rápido
- Benefício: sinais de marca, influenciadores, artista/feira, mercado sneaker.
- Risco: baixo read-only; externo/campanhas bloqueado.
- Próximo passo: piloto semanal read-only, sem posts ou DMs.

7. Verificação de artefatos e LSP como QA de scripts Brain
- Benefício: menos scripts quebrados e menos “achei que escrevi”.
- Risco: baixo.
- Próximo passo: exigir smoke/lint em scripts operacionais antes de cron.

### P2 — explorar com cuidado

8. Shopify skill read-only
- Benefício: relatórios e diagnóstico LK mais nativos.
- Risco: alto se houver write scope.
- Próximo passo: plano separado de credenciais read-only + testes sem mutação.

9. Teams/Graph meeting pipeline
- Benefício: atas, tarefas, follow-ups.
- Risco: médio por dados pessoais/empresariais.
- Próximo passo: só se Teams for fonte real; caso contrário não priorizar.

10. OpenAI-compatible local proxy
- Benefício: usar assinatura/OAuth com Codex/Aider/Cline.
- Risco: infra/segurança se exposto.
- Próximo passo: local-only via SSH tunnel; nada público sem plano/rollback.

## Recomendação final

A melhoria mais ampla não é instalar mais coisa: é consolidar um “Lucas Operating Layer” em cima da v0.14.

Prioridade prática:
1. transformar tarefas longas em `/goal` + `/subgoal`;
2. usar botões de aprovação estruturada para todo write/external/prod;
3. reduzir ruído/custo com `no_agent` watchers;
4. criar/usar um Kanban executivo multiempresa sem workers automáticos;
5. encadear outputs de crons com `context_from`;
6. ampliar social/research read-only com `x_search` e browser rápido;
7. deixar proxy/API/Teams/Shopify writes para planos separados com rollback.
