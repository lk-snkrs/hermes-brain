# Decisão — Subagentes com contexto mínimo e Brain sob demanda

**Data:** 2026-06-05
**Status:** aprovado por Lucas
**Escopo:** LC Mordomo OS, subagentes Hermes-native, rotinas de governança e Brain health.

## Decisão

Subagentes do LC Mordomo OS **não devem carregar tudo** por padrão.

A arquitetura aprovada é:

- contexto mínimo de boot;
- memória compacta apenas para preferências/regras estáveis;
- Brain versionado como fonte rica e auditável;
- índices/MAPAs para navegação;
- `session_search` para recuperar histórico sob demanda;
- skills para procedimentos;
- busca/leitura de fontes vivas somente quando material para a tarefa;
- compactação e handoff para preservar continuidade sem despejar histórico inteiro;
- Brain health checks para impedir drift, lacunas de índice e regressões de governança.

## Regra operacional

Cada subagente deve começar com um **Context Budget**:

1. **Boot mínimo:** identidade, escopo, permissões, bloqueios, fontes canônicas e skill principal.
2. **Índice antes de conteúdo:** ler `MAPA.md`, registry, rotina ou PRD antes de carregar arquivos grandes.
3. **Busca sob demanda:** usar `search_files`, `session_search`, SQLite/API/fonte viva ou skill só quando a pergunta exigir.
4. **Recorte por tarefa:** carregar somente trechos/arquivos necessários ao próximo passo verificável.
5. **Handoff compacto:** ao terminar, salvar decisão/receipt/resumo estruturado no Brain, não histórico bruto.
6. **Promoção seletiva:** só promover para memória/skill/rotina fatos duráveis ou procedimentos recorrentes.

## Anti-padrões bloqueados

- “Memória infinita carregada” como estratégia de qualidade.
- Subagente com histórico inteiro no prompt por conveniência.
- Copiar chat longo para Brain sem síntese, fonte, decisão e status.
- Misturar Brain de LK, Zipper, SPITI e pessoal quando a tarefa é de um domínio só.
- Alertar Lucas com dump de contexto, logs, JSON ou múltiplas filas soltas.

## Aplicação imediata

Esta decisão deve aparecer em:

- `areas/operacoes/mordomo/subagent-registry-2026-06-05.md`;
- `areas/operacoes/prds/lcmordomo-os-prd-2026-06-05.md`;
- `areas/operacoes/rotinas/hermes-nightly-governance-cycle.md`;
- `areas/operacoes/rotinas/brain-health-check.md`;
- `areas/operacoes/MAPA.md`.

## Critério de aceite

Antes de promover subagente, cron recorrente ou runtime separado, verificar:

- escopo e fontes do subagente definidos;
- Context Budget explícito;
- índices/rotinas atualizados;
- handoff/receipt definido;
- limites A0-A4 definidos;
- health check e secret scan limpos para os artefatos alterados.
