# START HERE — Manual Operacional do Hermes Brain

Este é o ponto de entrada para Lucas e para o Hermes entenderem como navegar e operar o Hermes Brain.

## Ideia central

Hermes Brain é a fonte de verdade versionada para contexto, decisões, áreas, agentes, rotinas e skills de negócio.

O organograma correto é uma **grande mente central** que cuida de tudo e roteia para as camadas abaixo:

```text
Lucas / Telegram
  ↓
Hermes Agent
  ↓
Grande Mente — Hermes Brain / Hermes COO
  ├── Lucas pessoal
  ├── Empresas: LK Sneakers, Zipper Galeria, SPITI Auction
  ├── Operações Hermes
  ├── Tecnologia / Infraestrutura
  └── Governança / Segurança / Aprovações
  ↓
Dados vivos — Supabase, Shopify, APIs, email, crons e integrações
```

Referência: `empresa/contexto/organograma-operacional-hermes-brain.md`.

O agente não é o cérebro. O agente lê e escreve no cérebro.

## Regra Hermes vs OpenClaw

A estrutura Bruno/OpenClaw foi adaptada, não copiada.

Antes de aplicar qualquer ideia OpenClaw, responder mentalmente:

1. Que lógica o Bruno está ensinando?
2. O que o Hermes já faz melhor ou diferente?
3. Isso melhora o Hermes ou só cria burocracia?
4. Qual é a versão Hermes-native?
5. Decisão: aplicar, adaptar, adiar ou rejeitar.

## Ordem recomendada de navegação

### 1. Comece por regras globais

- `AGENTS.md` — regras operacionais globais.
- `MAPA.md` — navegação rápida da Grande Mente.
- `STARTUP.md` — protocolo de início de sessão.
- `PROTOCOLS.md` — protocolos e lições estruturais.
- `TOOLS.md` — ferramentas e integrações.
- `ARCHITECTURE.md` — visão da arquitetura multicamada.

Use isso quando:

- uma sessão começa;
- a tarefa é ambígua;
- há risco operacional;
- precisa entender como o Hermes deve se comportar.

### 2. Consulte a memória executiva

- `memories/lk.md`
- `memories/zipper.md`
- `memories/spiti.md`
- `memories/decisions.md`
- `memories/lessons.md`
- `memories/pending.md`
- `memories/current.md` — camada quente/current para prioridades, bloqueios e riscos atuais documentais.

Use `memories/` para contexto compacto, decisões permanentes e lições. Não use `memories/` como substituto para dados vivos de banco/API.

### 3. Use a camada empresa para contexto cross-área

- `empresa/MAPA.md`
- `empresa/contexto/geral.md`
- `empresa/contexto/metricas.md`
- `empresa/decisoes/decisoes-permanentes.md`
- `empresa/gestao/pendencias.md`
- `empresa/gestao/licoes.md`
- `empresa/gestao/memory-system.md`
- `empresa/rotinas/_index.md`
- `empresa/skills/_index.md`

Use `empresa/` quando a informação atravessa LK, Zipper, SPITI, Operações, Governança ou Tecnologia.

### 4. Vá para a área do negócio

- `areas/MAPA.md` — índice executivo de áreas.
- `areas/lk/MAPA.md` — LK Sneakers.
- `areas/zipper/MAPA.md` — Zipper Galeria.
- `areas/spiti/MAPA.md` — SPITI Auction.
- `areas/operacoes/MAPA.md` — rotinas operacionais.
- `areas/governanca/MAPA.md` — regras e governança.
- `areas/tecnologia/MAPA.md` — arquitetura técnica.

Use `areas/` para operação real por negócio.

### 5. Consulte o agente especialista

- `agentes/hermes-geral/`
- `agentes/lk/`
- `agentes/zipper/`
- `agentes/spiti/`
- `agentes/mordomo/` — profile concierge/intake documental; não implica bot/runtime ativo.

Cada agente deve ter, quando possível:

- `SOUL.md` — identidade e tom.
- `AGENTS.md` — escopo e regras.
- `TOOLS.md` — ferramentas permitidas.
- `USER.md` — quem atende.
- `MEMORY.md` — índice local.
- `HEARTBEAT.md` — checagens periódicas.

Use `agentes/` para saber como responder, qual tom usar, quais limites respeitar e quais fontes consultar.

### 6. Use skills e rotinas

- `skills/` contém skills canônicas.
- `empresa/skills/_index.md` lista skills e atalhos por área.
- `empresa/rotinas/_index.md` lista rotinas documentadas.

Diferença:

- Skill = processo repetível com input, passos, output e verificação.
- Rotina = atividade recorrente/documentada, muitas vezes ligada a cron/script/relatório.

Regra: rotina documentada não prova cron ativo. Verificar cron real na VPS/ambiente antes de afirmar execução.

### 7. Verifique segurança antes de agir

- `seguranca/permissoes.md`
- `seguranca/acoes-sensiveis.md`

Use sempre que a ação envolver:

- cliente, colecionador, parceiro ou público;
- WhatsApp, email, campanha, post ou relatório externo;
- produção, deploy, banco, workflow ou credencial;
- alteração destrutiva ou irreversível.

## Como responder por tipo de tarefa

### Pergunta de negócio

1. Consultar memória executiva do negócio.
2. Consultar área correspondente.
3. Se envolver métrica/dado vivo, consultar banco/API/fonte real.
4. Responder com fonte e ressalva se necessário.

### Pedido de campanha, WhatsApp ou contato externo

1. Consultar área e agente.
2. Criar rascunho/preview.
3. Explicar fonte e público.
4. Pedir aprovação Lucas antes de envio.

### Pedido de automação ou rotina

1. Verificar `empresa/rotinas/_index.md`.
2. Consultar rotina específica.
3. Verificar se cron/script real existe antes de afirmar execução.
4. Documentar rotina se virar recorrente.

### Pedido de skill/processo repetível

1. Verificar `empresa/skills/_index.md`.
2. Usar skill canônica se existir.
3. Se não existir e virar recorrente, criar skill.
4. Não duplicar lógica divergente em área e skill canônica.

### Bug ou erro

Aplicar Lei COO #7:

1. Corrigir.
2. Prevenir repetição.
3. Documentar lição se for insight não óbvio.

### Credenciais

1. Usar Doppler `lc-keys/prd`.
2. Buscar valor sob demanda.
3. Não imprimir valor.
4. Não salvar localmente.
5. Se token apareceu em chat/log/repo, recomendar rotação.

## Regras por negócio

### LK Sneakers

Fonte principal: `areas/lk/` e `memories/lk.md`.

Dados vivos:

- Supabase LK `cnjimxglpktznenpbail`.
- Shopify.
- Klaviyo.
- GA4/GSC.
- Meta Ads.

Regras:

- Dados antes de afirmação.
- Não sugerir produto fora de estoque.
- Copy sem travessão, sem “compre agora”, sem “melhor do Brasil”.
- Campanha, WhatsApp e contato com cliente exigem aprovação Lucas.

### Zipper Galeria

Fonte principal: `areas/zipper/` e `memories/zipper.md`.

Dados vivos:

- Supabase Zipper Vendas `pcstqxpdzibheuopjkas`.
- Tabela `vendas_tango` para vendas reais.

Regras:

- Não confundir Zipper Vendas com SPITI.
- Não afirmar que obra/artista vende bem sem consultar dados.
- Tom culto, leve, sofisticado e sem hard sell.
- Contato com colecionador/proposta/curadoria exige aprovação Lucas/Osmar.

### SPITI Auction

Fonte principal: `areas/spiti/` e `memories/spiti.md`.

Dados vivos:

- Supabase/SPITI CRM `rmdugdkantdydivgnimb`.
- Tabela `spiti_lotes`.
- Email como fonte de verdade para total de lances.

Regras:

- Site pode mostrar só destaques.
- Meta tag é preço base, não lance atual.
- Silêncio é melhor que dado errado.
- Mensagens para grupo/cliente exigem aprovação Lucas.

## Checklist antes de finalizar uma fase

1. O resultado foi escrito no lugar certo do Brain?
2. Dados ou claims foram verificados em fonte real?
3. Secrets foram evitados?
4. Ações externas foram apenas rascunhadas ou aprovadas?
5. Scan de secrets retornou `possible_secrets 0`?
6. Commit foi criado e push feito?
7. Próxima fase recomendada ficou clara?

## Próximo lugar para olhar

Se você não sabe por onde começar:

1. `README.md`
2. `areas/MAPA.md`
3. `empresa/MAPA.md`
4. `empresa/rotinas/_index.md`
5. `empresa/skills/_index.md`
6. `seguranca/acoes-sensiveis.md`
