# Decision brief — Hermes Agent v0.14.0 para Lucas Brain

Data: 2026-05-16 07:49 BRT  
Fonte: GitHub Releases API `https://api.github.com/repos/NousResearch/hermes-agent/releases?per_page=10`  
Release: `v2026.5.16` / Hermes Agent v0.14.0, publicada em 2026-05-16 09:59 UTC  
Status original: análise e preparação; **nenhum update/runtime swap executado por este brief**.  
Status atual em 2026-05-16 08:42 BRT: **histórico/superseded**. A produção já foi atualizada com aprovação de Lucas para `Hermes Agent v0.14.0 (2026.5.16)` / imagem `hermes-agent-custom:v0.14.0-20260516`; estado vivo está em `reports/hermes-continuous-improvement/2026-05-16.md` e `areas/operacoes/rotinas/hermes-v014-post-upgrade-monitoring-reconciliation-2026-05-16.md`.

## Resumo executivo

Este brief foi criado antes do upgrade v0.14 aprovado. Ele permanece útil como matriz de decisão e classificação de features, mas não representa mais o estado atual de produção.

Estado atual confirmado depois: produção Lucas saudável em `Hermes Agent v0.14.0 (2026.5.16)` com imagem `hermes-agent-custom:v0.14.0-20260516` nos containers esperados.

A lição operacional continua válida: o ganho principal não é “ter versão nova”, mas reduzir fricção operacional do Hermes Brain — menos stalls de aprovação, mais verificação após writes, melhor uso de `/goal`/`/subgoal`, polling silencioso padronizado e gateway mais resiliente.

Recomendação atual: **não há upgrade pendente; aplicar as novidades v0.14 ao processo e manter novas mudanças de runtime/infra bloqueadas até aprovação explícita**.

## Classificação por feature

| Feature v0.14 | Aplicação Lucas Brain | Classificação | Motivo |
|---|---|---:|---|
| `/handoff` | Transferir uma sessão viva para modelo/profile/persona mais adequado sem perder contexto | Útil depois / ensinar pós-update | Bom para separar execução técnica, CoS e revisão, mas depende do runtime novo. |
| `/subgoal` | Adicionar critérios a uma missão longa já em `/goal` | Adotar como processo pós-update | Resolve “seguir” repetido e melhora missões longas sem reabrir todo o objetivo. |
| Watchers skill | RSS/HTTP JSON/GitHub polling via cron `no_agent` | Adotar como processo após avaliação | Pode padronizar release watcher, Zipper/GitHub/HTTP monitors e reduzir scripts soltos. Não criar novos crons recursivamente sem aprovação de escopo/cadência. |
| Clarify buttons no Telegram | Aprovações/decisões com botões inline | Ensinar Lucas pós-update | Reduz atrito de aprovação, mas não muda a regra: externo/produção precisa payload e destinatário/rollback explícitos. |
| Per-turn file-mutation verifier | Conferir o que realmente mudou em disco após `write_file`/`patch` | Must-adopt | Ataca diretamente o risco “achei que documentei/escrevi”. Forte para Brain/docs/scripts. |
| LSP semantic diagnostics | Diagnóstico semântico em `write_file`/`patch` | Must-adopt | Bom para scripts Python/TS e reduz erro de sintaxe/semântica antes de reportar pronto. |
| API approval events | Approval requests aparecem no stream da API em runs longos | Útil para reduzir stalls | Ajuda dashboard/API/Mordomo a não ficar silencioso esperando aprovação. |
| Plugin `ctx.llm` | Plugins fazem chamadas LLM com provider/credenciais ativos | Útil depois | Pode melhorar plugins internos, mas exige design e testes; não é prioridade imediata. |
| MCP parallel tool calls | Servidores MCP indicam suporte a chamadas paralelas | Útil depois | Interessante para pesquisa/integrações; avaliar só quando houver MCP real no fluxo. |
| Browser/CDP 180x faster | Browser tool mais rápido via CDP persistente | Útil para SEO/CRO/auditorias | Ganho claro para auditorias web, mas não justifica sozinho o upgrade. |
| Prompt cache Claude 1h cross-session | Retomadas e `/new` mais baratos/rápidos em Claude | Útil se Claude estiver no roteamento | Reduz custo/latência em trabalhos repetidos. |
| Local OpenAI-compatible proxy | Codex/Aider/Cline usando provedores OAuth | Útil depois | Pode ajudar dev local; não é core do Telegram/VPS agora. |
| Gateway circuit breakers por plataforma | Uma plataforma com falha não derruba o gateway todo | Must-adopt para produção | Relevante diante de warnings transitórios do Telegram; melhora resiliência sem mudar operação de negócios. |

## Plano seguro proposto antes de aprovar upgrade

1. Preparar clone/build paralelo da v0.14 sem substituir containers atuais.
2. Inventariar config, `.env`, skills, sessions, crons e scripts, sem imprimir secrets.
3. Preservar patches locais conhecidos, especialmente retry de compressão/transientes, se ainda não estiver upstream.
4. Rodar testes/smoke tests com o interpretador correto dentro do container: `/opt/hermes/.venv/bin/python` ou `python3`; nunca `python` puro.
5. Smoke mínimo em staging: `hermes --version`, `hermes config check`, `hermes cron status/list`, API `/health`, gateway startup, Telegram ready, watchdogs silenciosos.
6. Plano de rollback: manter imagem/tag atual `hermes-agent-custom:v0.13.0-20260510`, compose e volumes intactos; swap reversível.
7. Só depois pedir aprovação de Lucas com payload exato: imagem/tag/digest, janela de restart, comandos, evidências e rollback.

## Bloqueios

Sem aprovação explícita atual, continuam bloqueados:

- update/swap Docker;
- restart de gateway/container;
- alteração de compose/Traefik/rede/host/root/SSH;
- mudança de secrets;
- ativação de novos crons/watchers produtivos;
- qualquer external send ou write em Shopify/Tiny/Merchant/Meta/Google/Klaviyo/WhatsApp/email.

## Recomendação

A v0.14 vale um upgrade planejado, principalmente por verificação pós-write, LSP diagnostics, circuit breakers, `/subgoal`, watchers e clarify buttons. O próximo passo correto é um **pacote de staging/upgrade com rollback**, não mexer no runtime agora.
