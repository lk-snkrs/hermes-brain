# Bruno/OpenClaw — documentação, organograma de agentes e subida para o Brain

Data: 2026-05-19
Status: síntese operacional para Hermes Brain
Fontes consultadas:
- `bruno_upload_20260508_204305/.../aula-06-workspace/Workspace + mapas.html`
- `bruno_upload_20260508_204305/.../aula-13-multi-agente/material.html`
- `bruno_upload_20260508_204305/.../Referências para seu agente/multi-agente.md`
- `bruno_upload_20260508_204305/.../Referências para seu agente/workspace-do-seu-agente.md`
- `bruno_upload_20260508_204305/.../Referências para seu agente/memoria-do-seu-agente.md`
- `bruno_upload_20260508_204305/.../Exemplos da Amora/AGENTS-amora.md`
- `bruno_upload_20260508_204305/.../Exemplos da Amora/MAPA-amora.md`

## Tese central do Bruno

A lógica do Bruno/OpenClaw é:

> O agente não é o cérebro. O agente opera em cima de um workspace/cérebro persistente.

O agente pode ter sessão, canal e memória local, mas o que importa para continuidade operacional precisa virar arquivo versionado, mapa, rotina, decisão, skill, report ou handoff dentro do Brain/workspace.

## Como Bruno documenta o workspace

Na Aula 06, o padrão é um workspace canônico com arquivos raiz e MAPAs distribuídos:

```text
workspace/
├── SOUL.md
├── IDENTITY.md
├── AGENTS.md
├── USER.md
├── MEMORY.md
├── MAPA.md
├── HEARTBEAT.md
├── content/
│   └── MAPA.md
├── memory/
│   ├── MAPA.md
│   ├── hot.md
│   ├── YYYY-MM-DD.md
│   ├── context/
│   └── projects/
├── skills/
│   └── MAPA.md
└── archive/
    └── MAPA.md
```

Princípios relevantes:

1. `MAPA.md` raiz explica onde cada coisa vive.
2. Cada pasta relevante tem seu próprio `MAPA.md`.
3. `memory/` é território do agente: decisões, pendências, contexto quente, dailies e projetos.
4. Conteúdo criado vai para `content/` ou equivalente.
5. Coisa encerrada não é apagada; vai para `archive/`.
6. A manutenção vem por auditoria periódica de MAPAs, pendências e referências quebradas.

## Como Bruno define o organograma entre agentes

Na Aula 13, Bruno trata `AGENTS.md` como o **organograma vivo** do time digital.

O `AGENTS.md` deve responder:

- quem é cada agente: handle, papel, modelo e escopo;
- quem chama quem: subagentes disponíveis e agentes paralelos com handoff;
- onde cada um vive: workspace, canais e integrações;
- permissões cruzadas: escopo próprio e menor privilégio;
- governança: custo, audit log, limites e monitoramento.

A distinção central:

- **Subagente**: execução pontual/background, sandbox isolado, baixo custo de manutenção.
- **Agente paralelo**: entidade separada com workspace, SOUL/IDENTITY/USER/MEMORY próprios, canal próprio e custo de manutenção muito maior.

Regra de Bruno: a maioria dos PMEs começa melhor com **1 agente bem configurado**. Multi-agente só vale quando há sinais claros: lentidão/context rot, domínios muito distintos, time humano com canais próprios ou necessidade real de delegação 24/7.

## Como agentes “conversam” segundo Bruno

Bruno explicita que não existe, por padrão, uma DM interna mágica entre agentes. A cooperação acontece por mecanismos concretos:

1. subagente invocado pelo agente principal;
2. menção em canal compartilhado com `requireMention`;
3. arquivo compartilhado no workspace;
4. trigger/cron que chama outro agente programaticamente.

Tradução Hermes-native:

1. `delegate_task` / subagentes são execução pontual, não memória organizacional;
2. bots/profiles de Telegram são superfícies de execução;
3. Hermes Brain é o arquivo compartilhado durável;
4. cronjobs/rotinas podem acionar leituras e relatórios, mas precisam estar documentados e auditáveis.

## Como isso “sobe para o cérebro”

No material de memória (A7), Bruno separa três camadas:

1. **Memória de boot**: `MEMORY.md`, `hot.md`, dailies recentes, SOUL/IDENTITY/USER/AGENTS e MAPAs.
2. **Memória de sessão**: conversa atual; útil, mas perecível.
3. **Memória semântica**: busca no workspace inteiro.

A regra prática dos exemplos da Amora é:

> “Mental notes don’t survive session restarts. Files do.”

E também:

> “Text > Brain.”

Portanto, quando algo relevante acontece em um chat/profile/bot, o caminho correto é transformar a execução em artefato:

```text
conversa / execução / especialista
  ↓
handoff mínimo ou receipt
  ↓
arquivo no Brain: decisão, rotina, report, skill, PRD, template, memória ou changelog
  ↓
MAPA/índice atualizado para ser encontrável
  ↓
health/secret check quando houver commit/PR
```

## Adaptação para o Hermes de Lucas

O Hermes já é mais forte que OpenClaw em algumas partes: tem ferramentas nativas, memória persistente, `session_search`, skills, cronjobs, Telegram e integrações reais com LK/Zipper/SPITI. Então a adaptação correta não é copiar pastas literalmente; é manter a lógica:

```text
Lucas / Telegram principal
  ↓
Hermes Geral — COO / Grande Mente operacional
  ↓
Hermes Brain — fonte versionada de contexto, decisões, rotinas e governança
  ├── Lucas pessoal / Mordomo
  ├── LK OS
  │   └── LK Growth / Renan como especialista com autonomia delimitada
  ├── Zipper OS
  ├── SPITI OS
  ├── Operações Hermes
  ├── Tecnologia / Infra
  └── Governança / Segurança / Aprovações
```

No Hermes, a equivalência fica assim:

- `AGENTS.md` global: organograma e guardrails centrais.
- `empresa/contexto/organograma-agentes-hermes.md`: mapa entre negócio, agente documental, runtime profile/bot e rotina.
- `areas/<empresa>/MAPA.md`: como navegar cada OS.
- `agentes/<empresa>/`: identidade/escopo do agente documental.
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`: mecanismo de subida para o Brain.
- `reports/`, `rotinas/`, `projetos/`, `skills/`, `memories/`: destinos duráveis do que foi executado/aprendido.

## Regra operacional aprovada para especialistas

Nenhum especialista pode virar uma mente separada. Cada profile/bot pode executar dentro do escopo dele, mas precisa deixar rastro para o Hermes Central.

Formato mínimo do rastro:

```md
Data/hora:
Agente/profile:
Empresa/área:
Responsável humano:
Pedido original:
O que foi feito:
Fontes usadas:
Output/artefato:
Aprovação:
Envio/publicação:
Writes externos:
Riscos/bloqueios:
Próximos passos:
Onde foi documentado no Brain:
```

## Diagnóstico do estado atual do Hermes Brain

Já estamos alinhados com a lógica do Bruno em três pontos principais:

1. Existe uma Grande Mente central, não agentes soltos.
2. O organograma diferencia negócio, agente documental e runtime profile/bot.
3. Já existe protocolo de handoff para especialistas reportarem ao Hermes Central.

Gaps que continuam importantes:

1. Formalizar pasta documental completa para `Mordomo`, se o volume continuar crescendo.
2. Garantir que cada especialista ativo tenha `MAPA`, escopo, autonomia, rotina de handoff e local de receipts.
3. Criar/usar receipts padronizados para execuções relevantes, principalmente LK Growth/Renan, SPITI e Zipper.
4. Auditar periodicamente se outputs ficaram só no Telegram/profile e não subiram para o Brain.

## Decisão Hermes-native

Aplicar a lógica de Bruno como regra de governança, não como cópia literal:

- `AGENTS.md` = organograma vivo.
- `MAPA.md` = navegação distribuída.
- Handoff/receipt = ponte entre execução em perfil especialista e Brain.
- Brain versionado = fonte durável.
- Subagente = execução pontual.
- Profile/bot paralelo = entidade operacional com custo de governança e obrigação de handoff.

## Próximo passo recomendado

Criar a rotina “auditoria de handoff de especialistas” para verificar diariamente/semanalmente:

1. quais profiles/bots executaram algo relevante;
2. se houve receipt/handoff;
3. se o Brain recebeu decisão/output/artefato;
4. se há gaps de aprovação, fonte, rollback ou próximos passos;
5. se algum especialista está virando ilha de dados.
