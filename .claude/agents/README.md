# Claude Code Subagents — Hermes Brain

Subagentes nativos do Claude Code que portam as personas/guardrails dos agentes do Hermes Brain para uso interativo (delegação via Agent tool, fan-out paralelo, roteamento pelo `hermes-geral`).

## Como usar

- **Instalação global:** copiar estes arquivos para `~/.claude/agents/` (ficam disponíveis em qualquer sessão do Claude Code).
- **Invocação:** o `hermes-geral` roteia a tarefa para o subagente dono, ou o usuário pede diretamente ("peça pro `lk-stock`…"). Vários podem rodar em paralelo.
- **Cada arquivo é um *loader* leve:** aponta para a fonte canônica no Brain (`agentes/<slug>/` ou `areas/lk/sub-areas/<x>/`) e instrui `git pull` antes de trabalho operacional. A "alma" continua versionada na fonte; estes arquivos não a duplicam, referenciam.

## Roster

| Subagente | Model | Papel | Fonte canônica no Brain |
|---|---|---|---|
| `hermes-geral` | opus | Chief of Staff / orquestrador central | `agentes/hermes-geral/` |
| `lk-atendimento` | opus | Atendimento + CRM/inteligência comercial LK | `agentes/lk/` + `areas/lk/sub-areas/atendimento/` |
| `lk-growth` | opus | SEO/GEO/CRO/GMC/analytics/conteúdo LK | `agentes/lk/` + `areas/lk/sub-areas/growth/` |
| `lk-otimizacao-colecao` | opus | LKGOC — coleções/páginas de produto | `agentes/lk-otimizacao-colecao/` |
| `lk-shopify` | sonnet | Superfície Shopify (write approval-gated) | `agentes/lk/` |
| `lk-stock` | sonnet | [LK] Estoque Loja Física — dono de estoque | `areas/lk/sub-areas/stock/` |
| `lk-trends` | sonnet | Tendências / sourcing intelligence (read-only) | `agentes/lk/` |
| `zipper` | sonnet | Zipper Galeria — arte/colecionadores | `agentes/zipper/` |
| `spiti` | opus | SPITI Auction — leilões (fonte-first) | `agentes/spiti/` |
| `mordomo` | sonnet | Intake pessoal / agenda / triagem | `agentes/mordomo/` |
| `lc-claude-cli` | sonnet | Brainstorm editorial de pautas | `agentes/lc-claude-cli/` |

## Guardrails (herdados do Brain, embutidos em cada prompt)

- Fonte viva antes de número (preço/estoque/pedido/lance/métrica) — Brain guarda ponteiro/receipt, não substitui dado vivo.
- Sem write externo (Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/publicação) sem aprovação explícita atual de Lucas.
- Sem Docker/VPS/root/SSH/Traefik/deploy sem aprovação escopada + backup.
- Secrets só via Doppler `lc-keys/prd` sob demanda; documentar nomes, nunca valores.
- Não misturar dados/contexto/credenciais entre LK, Zipper e SPITI.
- Estoque LK: todos os agentes delegam ao `lk-stock`.

## Notas

- **Prompt-gated, não tool-gated:** as restrições vivem na instrução (como o HERMES AGENT runtime), não no frontmatter `tools:`.
- **MCPs:** referenciados no corpo de cada agente; nem todos wired (Shopify/Tiny/Meta ainda via CLI+Doppler).
- **Origem:** gerados a partir das personas em `agentes/` e `areas/lk/sub-areas/stock/` — ver histórico de commit.
