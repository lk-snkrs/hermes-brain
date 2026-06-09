# Receipt — lk-stock preparado

Data UTC: 2026-06-08T15:08:30Z

## Resultado

Novo agente/perfil preparado: `[LK] Estoque Loja Física` / `lk-stock`.

## Escopo aprovado por Lucas

Preparar **Agente Hermes completo**, incluindo perfil dedicado, mas deixar **gateway/bot/cron pendentes de aprovação**.

## Artefatos criados

Brain:

- `areas/lk/sub-areas/stock/PRD.md`
- `areas/lk/sub-areas/stock/SOUL.md`
- `areas/lk/sub-areas/stock/IDENTITY.md`
- `areas/lk/sub-areas/stock/USER.md`
- `areas/lk/sub-areas/stock/AGENTS.md`
- `areas/lk/sub-areas/stock/MAPA.md`
- `areas/lk/sub-areas/stock/TOOLS.md`
- `areas/lk/sub-areas/stock/HEARTBEAT.md`
- `areas/lk/sub-areas/stock/MEMORY.md`
- `areas/lk/sub-areas/stock/rotinas/stock-control-loop-v0.md`
- `areas/lk/sub-areas/stock/rotinas/best-seller-ready-stock-score-v0.md`
- `areas/lk/sub-areas/stock/templates/stock-action-packet.md`

Perfil local:

- `/opt/data/profiles/lk-stock`
- `/opt/data/profiles/lk-stock/SOUL.md`
- `/opt/data/profiles/lk-stock/IDENTITY.md`
- `/opt/data/profiles/lk-stock/USER.md`
- `/opt/data/profiles/lk-stock/AGENTS.md`
- `/opt/data/profiles/lk-stock/TOOLS.md`
- `/opt/data/profiles/lk-stock/HEARTBEAT.md`
- `/opt/data/profiles/lk-stock/MEMORY.md`
- `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md`

Roteamento atualizado:

- `areas/lk/MAPA.md`
- `areas/lk/sub-areas/ecommerce/AGENTS.md`
- `areas/lk/sub-areas/ecommerce/MAPA.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`

## Segurança

- Gateway: não iniciado.
- Bot Telegram: não ativado; token do perfil sanitizado/vazio.
- API Server/Webhook: forçados off/vazios no `.env` do perfil.
- Cron: nenhum cron criado.
- Writes externos Tiny/Shopify/Klaviyo/Meta/fornecedor/WhatsApp/email: `0`.
- Secrets impressos: `0`; somente status sanitizado.

## Próximo gate

Para ativar runtime, Lucas precisa aprovar separadamente uma destas opções:

1. iniciar CLI/profile apenas para smoke test local;
2. configurar token dedicado BotFather e iniciar gateway `lk-stock`;
3. criar rotina/cron read-only silent-OK de fila P0/P1;
4. conectar consultas Tiny/Shopify read-only via Doppler helper.

Sem essa aprovação, o agente permanece preparado/parado.
