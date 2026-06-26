# Profile Status Matrix — Hermes/LK produção

Gerado em: 2026-05-30T21:41:19+00:00  
Status: **canônico v0.1**, derivado do inventário read-only de 2026-05-30.  
Aviso: status de runtime envelhece. Antes de ação, revalidar read-only.

## Legenda

- **Telegram:** estado observado no inventário.
- **API/webhook:** externo ligado/desligado conforme sinais do inventário; não imprimir chaves.
- **Round-trip:** só considerar provado se houver mensagem/resposta recente no bot correto.
- **Max turns:** configuração observada; runtime live deve ser confirmado por log/process env antes de diagnosticar performance.

## Perfis canônicos

### default — Hermes Geral

- HERMES_HOME: `/opt/data`
- Missão: orquestrador geral, auditoria, coordenação, aprovação, trabalhos profundos.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: ativo/live no inventário.
- Webhook: ativo/live no inventário.
- Bind observado: `0.0.0.0:8642` e `0.0.0.0:8644`.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `90`.
- Observação: P0 de classificação de exposição real. Não mexer em Docker/firewall/Traefik sem aprovação escopada.

### lk-shopify — LK Shopify

- HERMES_HOME: `/opt/data/profiles/lk-shopify`
- Missão: Shopify/produtos/coleções/páginas/previews/readback/receipts.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `50`.
- Toolsets Telegram observados: clarify, file, memory, session_search, skills, todo, web, terminal, code_execution.
- Observação: inventário recente mostrou conflitos de polling Telegram em alguns momentos. Para “offline”, provar round-trip antes de declarar resolvido.

### lk-ops — LK Ops / Atendimento

- HERMES_HOME: `/opt/data/profiles/lk-ops`
- Missão: atendimento operacional, Tiny, estoque, pedidos e dúvidas práticas.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `40`.
- Toolsets Telegram observados: clarify, file, memory, session_search, skills, todo, terminal, code_execution.
- Observação: conectado mas lento ainda é problema. Atendimento precisa fast lane.

### lk-growth — LK Growth

- HERMES_HOME: `/opt/data/profiles/lk-growth`
- Missão: SEO/GEO/CRO/GMC/analytics/content.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `60`.
- Observação: trabalhos pesados devem ir para background/local quando possível.

### lk-trends — LK Trends

- HERMES_HOME: `/opt/data/profiles/lk-trends`
- Missão: tendências, relatórios read-only, fila de oportunidades.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `45`.
- Toolsets Telegram observados: browser, clarify, file, memory, session_search, skills, todo, web.
- Observação: oportunidade de trend não autoriza compra/reposição/write Shopify.

### mordomo — LC Mordomo

- HERMES_HOME: `/opt/data/profiles/mordomo`
- Missão: pessoal/follow-ups/WhatsApp/e-mail simples verificável.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `45`.
- Toolsets Telegram observados: browser, clarify, code_execution, file, memory, messaging, session_search, skills, terminal, todo, vision, web.
- Observação: terminal/code são necessários para WACLI; ações sensíveis continuam bloqueadas sem fonte/aprovação.

### spiti — SPITI

- HERMES_HOME: `/opt/data/profiles/spiti`
- Missão: CRM/admin obras/leilões/clientes/IA, Growth e financeiro conforme docs.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `openai-codex` / `gpt-5.5`.
- Max turns: `55`.
- Toolsets Telegram observados: browser, clarify, file, memory, session_search, skills, terminal, todo, vision, web.
- Observação: silêncio é melhor que dado errado; usar fontes SPITI/Hub/Supabase doc.

### lc-claude-cli

- HERMES_HOME: `/opt/data/profiles/lc-claude-cli`
- Missão: perfil auxiliar Claude CLI/proxy.
- Gateway live no inventário: sim.
- Telegram: ativo/live.
- API server: não detectado.
- Webhook: não detectado.
- Modelo: `lc-claude-cli-proxy` / `claude-opus-4`.
- Max turns: `50`.
- Observação: proxy Claude local é legado/auxiliar; Hermes principal atual é `openai-codex/gpt-5.5`.

## Perfis preparados/não-live no inventário

Não prometer operação até provar gateway live e round-trip.

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`

## Checklist rápido para atualizar esta matriz

1. Revalidar processos `hermes gateway run` por `HERMES_HOME` exato.
2. Revalidar Telegram connected e logs recentes.
3. Revalidar API/webhook live ou disabled.
4. Não copiar tokens/chaves.
5. Atualizar apenas estado operacional curto; detalhes ficam em receipt.
