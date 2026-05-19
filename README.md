# Hermes Brain

Hermes Brain é a fonte de verdade versionada para contexto, decisões, áreas, agentes, rotinas e skills de negócio de Lucas Cimino.

Este repositório não guarda secrets. Credenciais vivem no Doppler `lc-keys/prd` e devem ser buscadas sob demanda.

## Princípio central

Hermes não é OpenClaw. A estrutura Bruno/OpenClaw foi adaptada para o Hermes preservar seus diferenciais:

- execução real com ferramentas;
- memória persistente e `session_search`;
- GitHub Brain como fonte durável;
- Doppler como fonte de credenciais;
- Telegram como interface operacional;
- cronjobs e rotinas documentadas;
- integração com LK Sneakers, Zipper Galeria e SPITI Auction.

## Como navegar

Comece por `START-HERE.md`.

Depois use:

- `AGENTS.md` — regras operacionais globais.
- `STARTUP.md` — boot protocol.
- `PROTOCOLS.md` — protocolos operacionais.
- `TOOLS.md` — ferramentas e integrações.
- `CHANGELOG.md` — histórico da adaptação Bruno/OpenClaw → Hermes.
- `ROADMAP-30-DIAS-HERMES.md` — roadmap pós-adaptação e próximas rodadas.
- `memories/` — memória executiva compacta e global.
- `memories/current.md` — camada quente/current para boot rápido, prioridades, bloqueios e riscos.
- `empresa/` — contexto cross-área, decisões, gestão, rotinas e skills.
- `areas/` — mapas operacionais por negócio/área.
- `agentes/` — agentes especializados e suas regras.
- `agentes/mordomo/` — documentação inicial do profile Mordomo/concierge; não cria runtime.
- `seguranca/` — permissões e ações sensíveis.
- `skills/` — skills canônicas versionadas.
- `scripts/` — scripts operacionais versionados.

## Regra de segurança

- Nunca versionar tokens, API keys, senhas ou refresh tokens.
- Usar nomes de secrets, não valores.
- Rodar scripts com Doppler quando precisarem de credenciais.
- Ações externas com clientes, campanhas, WhatsApp, posts, propostas ou publicações exigem aprovação de Lucas.

## Fonte de dados por negócio

- LK Sneakers: Supabase LK `cnjimxglpktznenpbail`, Shopify, Klaviyo, GA4/GSC e integrações comerciais.
- Zipper Galeria: Supabase Zipper Vendas `pcstqxpdzibheuopjkas`, tabela `vendas_tango` para vendas reais.
- SPITI Auction / CRM: Supabase `rmdugdkantdydivgnimb`, tabela `spiti_lotes` e fontes de lance documentadas.

## Regra de verdade

Dados vivos vêm de bancos/APIs. O Brain organiza contexto, decisões e processos. Se houver divergência, consultar a fonte operacional antes de afirmar.
