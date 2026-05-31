# Critérios de promoção — profiles auxiliares, Zipper e novos agentes

Data: 2026-05-30
Owner: Hermes Geral / Governança Brain
Status: política documental ativa.

## Princípio

Profile com token, pasta ou configuração não é automaticamente agente operacional. Um agente só vira operacional quando existe decisão explícita, escopo, fonte, canal, watchdog, handoff e rollback.

## Profiles auxiliares atuais

### `lc-claude-cli`

- Classificação: agente de brainstorm/editorial interno para Lucas.
- Status: profile criado e validado em CLI; gateway/canal dedicado pendente.
- Pode fazer: ideação, pauta, títulos, ângulos, perguntas de pesquisa, briefs internos e handoff para especialistas.
- Não pode por padrão: publicar, enviar, agendar campanha, criar cron editorial, alterar superfícies de negócio ou operar como especialista de LK/Zipper/SPITI.
- Observação: este profile é uma promoção explícita solicitada por Lucas, não um auxiliar dormente; ainda assim só vira agente Telegram operacional quando houver token/canal/watchdog aprovados.

### `brain-process`

- Classificação: governança/documentação local.
- Status: preparado/read-only; não é agente Telegram operacional.
- Pode fazer: leitura, higiene Brain, relatórios locais, health checks, organização documental.
- Não pode por padrão: enviar Telegram, criar cron, alterar runtime, tocar produção ou atuar como dono de negócio.

### `hermes-ops-readonly`

- Classificação: operações Hermes read-only.
- Status: preparado/read-only; não é agente Telegram operacional.
- Pode fazer: auditoria local, inventário, análise de logs/configs sanitizados, relatórios.
- Não pode por padrão: reiniciar gateway, migrar cron, mexer em Docker/VPS/Traefik, alterar secrets.

### `lk-analyst-readonly`

- Classificação: análise LK read-only/experimental.
- Status: preparado; não é dono de atendimento, Shopify ou Growth enquanto não for promovido.
- Pode fazer: relatórios e análise local/read-only com fontes explícitas.
- Não pode por padrão: contato externo, preço/disponibilidade prometida, Shopify/Tiny/GMC/Klaviyo/Meta writes.

### `lk-content-reviewer`

- Classificação: reviewer de conteúdo LK read-only/experimental.
- Status: preparado; não é substituto do LK Growth.
- Pode fazer: revisão, checklist, quality gate, apontamento de risco.
- Não pode por padrão: publicar, editar Shopify/theme/GMC/Klaviyo, enviar campanha, assumir dono de conteúdo final sem handoff para LK Growth.

## Zipper

- Classificação atual: documental/read-only.
- Runtime dedicado: não criar por simetria.
- Promoção para bot/profile próprio só se existir pelo menos um gatilho objetivo:
  - volume recorrente de pedidos Zipper que congestiona Main/Mordomo;
  - risco de contato externo ou proposta exigindo isolamento forte;
  - canal dedicado aprovado por Lucas;
  - rotina recorrente com fontes estáveis e handoff claro;
  - necessidade de watchdog próprio.

## Checklist para promover qualquer profile a agente operacional

1. Escopo e dono lógico documentados.
2. Fonte de verdade definida.
3. Pacote mínimo: `SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS`, `MEMORY`.
4. Bot/canal esperado definido.
5. Runtime profile com API/webhook off por padrão, salvo exceção aprovada.
6. Watchdog silent-OK definido.
7. Handoff/receipt obrigatório definido.
8. Guardrails de write externo/produção claros.
9. Rollback claro.
10. Aprovação explícita de Lucas quando envolver runtime novo, cron, contato externo ou produção.

## Regra anti-drift

Revisar esta classificação quando houver mudança de canal, volume, risco, fonte de verdade ou rotina recorrente. Não promover por estética do organograma.
