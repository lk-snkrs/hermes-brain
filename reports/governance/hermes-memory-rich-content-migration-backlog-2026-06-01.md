# Hermes memory rich-content migration backlog — 2026-06-01

## Objetivo

Continuação da compactação de `MEMORY.md`/`USER.md`: verificar o conteúdo rico removido dos profiles especialistas e decidir o destino correto sem voltar a inflar a memória injetada.

Tese canônica: memória curta/injetada é boot mínimo; memória rica vive em Brain, daily notes, `hot.md`, context files, skills, `session_search`, reports/archive e, se aprovado, provider externo.

## Fonte auditada

Backups criados antes da compactação:

`reports/governance/memory-backups/20260601-memory-boot-compact/`

Profiles revisados:

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`
- `lk-growth`
- `lk-ops`
- `lk-shopify`
- `lk-trends`
- `mordomo`
- `spiti`

## Achado principal

A maior parte do que saiu dos arquivos injetados já pertence a camadas ricas existentes no Brain. O risco maior não era perda de conhecimento, e sim duplicação/saturação: muitos profiles carregavam o mesmo bloco operacional, com detalhes de infra, integrações, relatórios e estado histórico.

## Classificação dos conteúdos removidos

### 1. Guardrails globais e fonte de verdade de credenciais

Destino correto:

- Memória default mínima: somente a regra abstrata.
- Brain/governança: política de segurança e fonte de verdade.
- Skills específicas: runbooks de Doppler/secrets.

Não deve voltar para `MEMORY.md`/`USER.md` dos especialistas:

- caminhos detalhados de tokens;
- usuário/host/IP/chave;
- nomes de variáveis sensíveis;
- histórico de falhas de SSH/autenticação.

Status: preservar como política/skill; não reinjetar.

### 2. LK OS: Shopify, Tiny, GMC, estoque, Growth, Trends, atendimento

Destino correto:

- `areas/lk/MAPA.md` para visão macro;
- `areas/lk/sub-areas/shopify/` para Shopify/GMC/e-commerce;
- `areas/lk/sub-areas/atendimento/` para atendimento/estoque;
- `areas/lk/sub-areas/growth/` para Growth/SEO/CRO/GEO;
- `areas/lk/sub-areas/trends/` para tendências;
- skills `lk-*` para procedimentos repetíveis.

Status: manter como Brain/skills por domínio. Os profiles já apontam para essas áreas em vez de carregar o conteúdo inteiro no prompt.

### 3. Zipper / SPITI / Mordomo

Destino correto:

- `areas/zipper/` e `agentes/zipper/` para regras Zipper;
- `areas/spiti/` e `agentes/spiti/` para SPITI;
- `areas/operacoes/mordomo/` e `agentes/mordomo/` para Mordomo.

Status: conteúdo rico não deve ficar duplicado em todos os profiles LK. Manter no Brain e carregar sob demanda pelo perfil certo.

### 4. Histórico, receipts, job IDs, status operacional

Destino correto:

- daily notes;
- reports/archive;
- receipts;
- `session_search`.

Não deve ficar em memória injetada:

- cron/job IDs;
- status atual online/offline;
- PIDs;
- entregas concluídas;
- datas e receipts extensos.

Status: regra já capturada em `memories/politica-memoria-hermes.md`.

### 5. Procedimentos repetíveis

Destino correto:

- skills ou references dentro de skills.

Exemplos:

- Shopify/GMC repair/readback;
- LK stock lookup;
- Telegram specialist runtime activation;
- memory compaction;
- governance/Brain health checks.

Status: não reinjetar; quando um procedimento faltar, criar/patchar skill específica.

## Backlog recomendado

### P0 — já resolvido

- Compactar profiles especialistas com backup.
- Registrar receipt e daily/hot.
- Confirmar que todos ficam abaixo dos limites.
- Rodar secret scan e Brain health check.

### P1 — manter como rotina de higiene

- Quando um profile volta a >80% do limite, rodar auditoria e migrar conteúdo rico para Brain/skills.
- Antes de adicionar memória injetada, perguntar: “isso precisa estar no prompt de toda sessão ou pode ser ponteiro?”
- Preferir ponteiros canônicos sobre duplicar fatos de domínio.

### P2 — melhoria documental opcional

- Revisar `areas/lk/sub-areas/*/MEMORY.md` para garantir que cada domínio contém apenas fatos duráveis e não estado atual.
- Criar context files por projeto/diretório somente se houver runtime real que os leia progressivamente.
- Criar um índice curto “onde fica cada memória rica” em `memories/politica-memoria-hermes.md` se Lucas quiser uma versão ainda mais operacional.

### P3 — provider externo

- Avaliar Honcho/Mem0/Hindsight/Supermemory em spike separado.
- Não ativar por padrão: risco de privacidade, custo, ruído e duplicação.

## Não-ações desta etapa

- Não habilitei provider externo.
- Não reiniciei profiles/gateway.
- Não mudei Docker/VPS/Traefik.
- Não movi credenciais.
- Não apaguei backups.

## Conclusão

A análise original está correta e agora está operacionalizada: o Hermes deve inicializar com memória curta como índice/boot mínimo, e recuperar memória rica nas camadas certas conforme a tarefa exige.
