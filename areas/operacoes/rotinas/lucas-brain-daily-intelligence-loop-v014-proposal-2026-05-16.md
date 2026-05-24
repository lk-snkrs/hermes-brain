# Proposta — Lucas Brain Daily Intelligence Loop v0.14

Data: 2026-05-16 07:39 BRT  
Contexto: evolução do cron 02:00 BRT (`f5a23dd6a1bd`) de manutenção Hermes/LK para cérebro operacional proativo.  
Status: proposta operacional; nenhuma alteração no cron executada neste documento.

## 1. Pergunta do Lucas

Lucas apontou que a proposta anterior cuidava bem da estrutura do Brain, mas deixava um eixo faltando:

> O que o Hermes pode melhorar na maneira como ele trabalha?

A resposta: faz sentido incluir um eixo explícito de **melhoria do mecanismo do Hermes**, não só das empresas/Brain. O cron das 02h deve observar e melhorar o próprio modo de trabalho do agente.

## 2. Pesquisa atual — Hermes Agent v0.14.0

Fonte consultada: GitHub Releases API `NousResearch/hermes-agent`, em 2026-05-16.  
Release nova encontrada após o run das 02h: `v2026.5.16` / Hermes Agent v0.14.0, publicada em 2026-05-16 09:59 UTC.

Destaques aplicáveis ao Lucas Brain:

- `/handoff`: transferência viva de sessão entre modelo/persona/profile.
- `/subgoal`: critérios adicionais em objetivos longos.
- `watchers` skill: RSS/HTTP JSON/GitHub polling usando cron `no_agent`.
- Per-turn file-mutation verifier: verificação do que realmente mudou em disco após writes.
- LSP semantic diagnostics em `write_file`/`patch`.
- `clarify` com botões nativos no Telegram/Discord.
- API server expõe eventos de aprovação de runs longos.
- Plugins podem chamar LLM via `ctx.llm`.
- `tool_override` em plugins.
- MCP com `supports_parallel_tool_calls`.
- Browser CDP muito mais rápido.
- Cross-session Claude prompt cache de 1h.
- Local OpenAI-compatible proxy para Codex/Aider/Cline usando provedores OAuth.
- Circuit breaker por plataforma no gateway.

Observação: produção Lucas ainda está em v0.13.0; qualquer runtime swap para v0.14 exige plano, backup, smoke tests e aprovação explícita.

## 3. Novo eixo obrigatório do cron 02h

Adicionar ao cron um bloco chamado:

## Como o Hermes trabalhou ontem — mecanismo e qualidade

Perguntas diárias:

1. Hermes pediu aprovação demais ou de menos?
2. Hermes parou cedo quando deveria continuar?
3. Alguma tarefa exigiu “seguir” repetido e deveria virar `/goal`, cron, Kanban ou checklist?
4. Algum relatório foi técnico demais e pouco acionável?
5. Algum contexto ficou só no chat e não entrou no Brain/skill/memória?
6. Algum prompt/cron/skill está antigo em relação à prioridade ativa?
7. Algum erro se repetiu e precisa virar guardrail?
8. Alguma ferramenta nova do Hermes pode reduzir fricção para Lucas?
9. Alguma automação deveria ser silent-OK em vez de ruído diário?
10. Algum fluxo poderia usar melhor subagentes, Kanban, watchers, webhooks ou MCP?

## 4. Ações autônomas permitidas neste eixo

A0/A1 — permitido sem nova aprovação:

- atualizar Brain docs;
- atualizar skills com pitfall real;
- melhorar prompts de cron sem ampliar risco externo;
- criar scripts read-only locais;
- classificar crons ruidosos/redundantes;
- criar proposta de uso de feature nova;
- registrar aprendizado de estilo/processo;
- criar checklist de verificação.

Bloqueado sem aprovação explícita:

- atualizar runtime Hermes/Docker;
- reiniciar gateway/container;
- mudar compose/Traefik/rede/host;
- alterar secrets;
- habilitar ferramenta com poder externo sensível;
- criar envio externo;
- escrever em banco/Shopify/campanhas.

## 5. Como aproveitar v0.14 sem atualizar produção ainda

Mesmo antes do update:

- Incluir v0.14 no radar diário e preparar decision brief.
- Mapear quais features resolvem dores reais do Lucas:
  - `/subgoal`: melhorar missões longas.
  - Watchers skill: padronizar polling silencioso de GitHub/HTTP/RSS.
  - Clarify buttons: aprovações mais fáceis no Telegram após runtime update.
  - Per-turn verifier/LSP diagnostics: menos “achei que escrevi/funcionou”.
  - API approval events: menos stalls silenciosos em runs longos.
  - `/handoff`: rotear uma missão para modelo/persona melhor sem perder contexto.
- Não fazer runtime swap automático.

## 6. Documentação atual observada

Hoje o cron documenta em múltiplas camadas:

- Relatório diário: `reports/hermes-continuous-improvement/YYYY-MM-DD.md`.
- Observabilidade host/Docker: `reports/hermes-host-docker-observability-YYYY-MM-DD.json`.
- Rotina operacional: `areas/operacoes/rotinas/hermes-v013-operacionalizacao.md`.
- Changelog geral: `CHANGELOG.md`.
- Skills: especialmente `lucas-hermes-continuous-improvement` e `hermes-agent`.
- Scripts read-only em `/opt/data/scripts/` e cópias/descrições no Brain quando aplicável.

Gap encontrado: o run 2026-05-16 estava documentado no relatório diário e na rotina operacional, mas o `CHANGELOG.md` ainda não tinha entrada 2026-05-16 no topo. Esse tipo de lacuna deve virar check automático do cron.

## 7. Proposta de novo formato do relatório 02h

1. Saúde do sistema.
2. Prioridade ativa do Lucas.
3. Oportunidades por empresa/projeto.
4. Como o Hermes trabalhou ontem — mecanismo e qualidade.
5. O que foi documentado no Brain hoje.
6. Melhorias aplicadas com segurança.
7. Melhorias propostas que exigem aprovação.
8. Próximo melhor passo.

## 8. Recomendação

Atualizar o cron `f5a23dd6a1bd` para virar **Lucas Brain Daily Intelligence Loop**, com um bloco obrigatório de melhoria do próprio Hermes. O cron deixa de ser apenas manutenção técnica e passa a ser um ciclo de metacognição operacional: observar, aprender, documentar, reduzir fricção e propor evolução segura.
