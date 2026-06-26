MAPA.md — Workspace da Amora

Este é o MAPA.md real do workspace da Amora. Use como referência de profundidade — adapte ao SEU contexto.

Arquivos Raiz



| Arquivo | Funcao | Quando ler |

| --- | --- | --- |

| SOUL.md | Identidade, personalidade, regras | Boot (passo 1) |

| USER.md | Perfil do Bruno | Boot (passo 2) |

| IDENTITY.md | Nome, modelo, territories | Boot |

| MEMORY.md | Memoria de longo prazo (indice) | Boot em main session |

| TOOLS.md | Integracoes, credenciais, skills | Quando precisar de ferramentas |

| AGENTS.md | Boot sequence, regras de sessao | Boot |

| HEARTBEAT.md | Configuração do mecanismo de proatividade | Quando muda comportamento |

| MAPA.md | Este arquivo, navegacao geral | Boot (passo 3) |

| PROPAGATION.md | Protocolo de propagacao de dados | Quando qualquer dado mudar |



Pastas Principais

```markdown
workspace-amora-cos/

├── agents/             → Raio-X dos agentes do ecossistema

├── archive/            → Arquivos antigos e temporarios

├── areas/              → Contexto editorial e areas de trabalho

├── content/            → Producao ativa de conteudo

├── docs/               → Documentacao tecnica

├── memory/             → Cerebro: contexto, projetos, sessoes, hot.md

├── projects/           → Projetos ativos (subpasta por projeto)

├── reports/            → Reports e analises gerados

├── scripts/            → Scripts operacionais

├── skills/             → Skills categorizadas

├── workshops/          → Material de execucao de workshops

└── wiki/               → Base de conhecimento


```Navegacao Rapida



| Estou buscando... | Onde ir |

| --- | --- |

| Onde salvar um rascunho | content/{plataforma}/drafts/ |

| Tom de voz do Bruno | areas/conteudo/contexto/voz/ |

| Estrategia e microprogramas | areas/conteudo/contexto/estrategia/ |

| Status de projetos | memory/projects/_index.md |

| Decisoes estrategicas | memory/context/decisoes/ |

| Pendencias ativas | memory/context/pendencias.md |

| Prazos/Deadlines | memory/context/deadlines.md |

| Equipe/Pessoas | memory/context/people/{pessoa}.md |

| Detalhes de um negocio | memory/context/business/{negocio}.md |

| Skills disponiveis | skills/_registry.md |

| O que aconteceu hoje | memory/YYYY-MM-DD.md |

| Cases reais de OpenClaw | memory/cases/openclaw/ |



Sub-MAPAs

Cada pasta principal tem seu proprio MAPA.md com detalhes internos:

memory/MAPA.md

memory/cases/MAPA.md

skills/MAPA.md

projects/MAPA.md

content/MAPA.md

reports/MAPA.md

Como adaptar pro seu contexto

A Amora tem workspace complexo (12+ pastas principais, dezenas de sub-pastas). Construído ao longo de meses.

Pro seu agente novo: estrutura mínima é mais simples (~20 linhas iniciais):

```markdown
# MAPA.md — Workspace do Atlas

## Arquivos Raiz

| Arquivo | Função |

|---|---|

| `SOUL.md` | Personalidade do Atlas |

| `USER.md` | Sobre o Carlos (dono da padaria) |

| `AGENTS.md` | Regras entre Carlos e Atlas |

| `MAPA.md` | Este arquivo |

| `MEMORY.md` | Memória de longo prazo |

| `HEARTBEAT.md` | Configuração da proatividade |

## Pastas Principais

workspace/

├── content/            → Posts, briefings, planos que Atlas cria

├── memory/             → Decisões, pendências, pessoas

├── archive/            → Material arquivado

└── skills/             → Skills instaladas

## Navegação Rápida

| Buscando... | Onde ir |

|---|---|

| Posts criados | content/drafts/ |

| Decisões | memory/decisoes/ |

| Pendências | memory/pendencias/ |

| Skills | skills/_registry.md |


```

20 linhas. Cresce conforme aluno expande workspace.

Padrão de evolução do MAPA:

Inicial (passo 4 do starter-kit): ~20 linhas. Estrutura básica.

Após primeiros meses: ~50 linhas. Adiciona "Navegação Rápida" expandida.

Maduro (~6 meses): 100+ linhas. Estabiliza.

A regra: MAPA cresce conforme workspace cresce. Não tente prever o futuro — mapeia o que existe.

Versão de referência — workspace original da Amora.
