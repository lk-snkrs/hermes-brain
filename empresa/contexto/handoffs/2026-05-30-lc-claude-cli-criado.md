# Handoff — criação do agente [LC] Claude Cli

Data: 2026-05-30
Owner: Hermes Geral
Status: profile CLI criado e validado; gateway/canal dedicado pendente.

## Pedido de Lucas

Criar um novo agente chamado **[LC] Claude Cli**, para servir como canal de brainstorm de pautas usando Claude.

## O que foi criado

- Runtime profile: `/opt/data/profiles/lc-claude-cli`.
- Wrapper local: `/opt/data/home/.local/bin/lc-claude-cli`.
- Agente documental: `agentes/lc-claude-cli/`.
- Configuração do modelo: Claude via proxy local `claude-max-api`/Claude CLI em `http://127.0.0.1:3456/v1`.
- Modelo configurado: `claude-opus-4`.
- API Server/Webhook/Telegram token: desativados/vazios por padrão.

## Arquivos documentais criados

- `agentes/lc-claude-cli/IDENTITY.md`
- `agentes/lc-claude-cli/AGENTS.md`
- `agentes/lc-claude-cli/MAPA.md`
- `agentes/lc-claude-cli/SOUL.md`
- `agentes/lc-claude-cli/USER.md`
- `agentes/lc-claude-cli/HEARTBEAT.md`
- `agentes/lc-claude-cli/TOOLS.md`
- `agentes/lc-claude-cli/MEMORY.md`

## Documentos atualizados

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`
- `empresa/contexto/criterios-promocao-agentes-auxiliares.md`
- `AGENTS.md`

## Guardrails

[LC] Claude Cli pode:

- gerar pautas, títulos, ângulos, perguntas e briefs internos;
- criticar ideias e separar hipótese criativa de fato verificado;
- fazer handoff para especialista quando a pauta virar execução.

[LC] Claude Cli não pode por padrão:

- publicar ou enviar conteúdo;
- criar campanha, cron ou automação editorial;
- alterar Shopify/site/CRM/Klaviyo/Meta/GMC/Tiny/n8n;
- mexer em Docker/VPS/Traefik/runtime de outros perfis;
- assumir execução final de LK/Zipper/SPITI.

## Verificação feita

- Proxy Claude respondeu `/health` com status OK.
- `hermes profile list` mostra `lc-claude-cli` com modelo `claude-opus-4` e gateway `stopped`.
- Teste CLI executado com sucesso:
  - comando: `lc-claude-cli chat -q 'Teste curto: responda apenas OK LC Claude Cli.' --toolsets '' -Q`
  - resposta: `OK LC Claude Cli`

## Pendências para virar canal Telegram operacional

1. Lucas definir se quer BotFather bot próprio, grupo/canal Telegram ou apenas CLI/local.
2. Se for Telegram: fornecer token dedicado e destino/canal.
3. Ativar somente o gateway do profile `lc-claude-cli`, mantendo API/webhook off.
4. Adicionar watchdog silent-OK somente após o canal ser considerado operacional.
5. Fazer teste round-trip Telegram antes de chamar de ativo.
