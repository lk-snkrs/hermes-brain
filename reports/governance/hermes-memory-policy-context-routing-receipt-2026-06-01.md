# Hermes memory policy context-routing receipt — 2026-06-01

## Objetivo

Dar continuidade à higiene de memória criando uma camada operacional curta para responder: “onde cada tipo de memória deve ser buscado ou salvo?” e garantir que o contexto raiz do Brain aponta para essa política.

## Mudanças aplicadas

### 1. Política canônica ampliada

Arquivo: `memories/politica-memoria-hermes.md`

Adicionado o bloco **“Índice operacional: onde procurar/salvar cada memória”**, cobrindo destinos para:

- preferências/guardrails globais;
- prioridades current;
- daily notes;
- contexto durável por domínio;
- skills/procedimentos;
- reports/receipts/evidência;
- `session_search`;
- dados vivos/API/CLI;
- credenciais;
- provider externo pós-spike.

### 2. Context file raiz atualizado

Arquivo: `AGENTS.md`

O boot mínimo agora manda consultar `memories/politica-memoria-hermes.md` em decisões de memória/contexto e explicita a tese: memória injetada é boot mínimo; memória rica vai para Brain/daily/hot/skills/reports/session_search.

Também substituí a referência específica a fonte/escopo de credenciais por linguagem genérica: “fonte segura autorizada”, sem imprimir valores.

## Auditoria de context files

Foram encontrados 15 `AGENTS.md` no Brain.

Resultado:

- O `AGENTS.md` raiz agora contém a política de memória e será herdado como contexto de topo para operações no repositório.
- Sub-AGENTS de especialistas continuam focados em escopo, risco e writes do domínio; não precisam duplicar a política inteira para evitar ruído.
- Se um especialista voltar a inflar memória local, a correção deve ser feita no `MEMORY.md`/skill/rotina específica, mantendo o root como ponteiro canônico.

## Decisão

Não duplicar a política em todos os `AGENTS.md`. A forma correta é:

1. política canônica em `memories/politica-memoria-hermes.md`;
2. ponteiro no `AGENTS.md` raiz;
3. referências específicas somente quando um domínio tiver regra própria.

## Não-ações

- Não alterei runtime/gateway/profile.
- Não alterei Docker/VPS/Traefik.
- Não habilitei provider externo.
- Não mexi em cron.
- Não movi credenciais.

## Verificação recomendada

- Brain health check.
- Secret scan focado nos arquivos alterados.
- Conferir `git status` escopado antes de qualquer commit futuro, porque há alterações pré-existentes no repo fora deste trabalho.
