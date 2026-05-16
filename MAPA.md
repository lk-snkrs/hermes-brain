# MAPA — Hermes Brain

Este é o mapa rápido da Grande Mente do Lucas: Hermes Brain / Hermes COO.

## Arquivos raiz

| Arquivo | Função | Quando ler |
|---|---|---|
| `START-HERE.md` | Manual operacional de navegação | Boot e tarefas ambíguas |
| `README.md` | Visão geral do repositório | Primeiro contato |
| `AGENTS.md` | Regras operacionais globais | Antes de trabalho operacional |
| `STARTUP.md` | Protocolo de início | Sessões novas/retomadas |
| `PROTOCOLS.md` | Protocolos e lições estruturais | Risco, processo ou governança |
| `TOOLS.md` | Ferramentas e integrações | Quando precisar de dados/ferramentas |
| `ARCHITECTURE.md` | Arquitetura multicamada | Planejamento estrutural |
| `HEARTBEAT.md` | Configuração global de heartbeat | Proatividade/crons |
| `MAPA.md` | Este arquivo | Navegação rápida |

## Modelo mental

```text
Lucas / Telegram
  ↓
Hermes Agent
  ↓
Grande Mente — Hermes Brain / Hermes COO
  ├── Lucas pessoal
  ├── Empresas
  │   ├── LK Sneakers
  │   ├── Zipper Galeria
  │   └── SPITI Auction
  ├── Operações Hermes
  ├── Tecnologia / Infraestrutura
  └── Governança / Segurança / Aprovações
```

Referência canônica: `empresa/contexto/organograma-operacional-hermes-brain.md`.

## Pastas principais

```text
hermes-brain/
├── agentes/       → identidade, regras, tools e memória por agente
├── areas/         → operação por área/negócio
├── empresa/       → camada cross-área: contexto, gestão, decisões, rotinas, skills
├── memories/      → memória executiva compacta
├── reports/       → auditorias, evidências e entregáveis gerados
├── scripts/       → scripts operacionais versionados
├── seguranca/     → permissões, ações sensíveis e guardrails
├── skills/        → skills versionadas do Brain
└── templates/     → modelos reutilizáveis
```

## Navegação rápida

| Estou buscando... | Onde ir |
|---|---|
| Identidade do Hermes Geral | `agentes/hermes-geral/IDENTITY.md` |
| Voz e princípios do Hermes Geral | `agentes/hermes-geral/SOUL.md` |
| Regras operacionais do Hermes Geral | `agentes/hermes-geral/AGENTS.md` |
| Perfil de Lucas para o Hermes Geral | `agentes/hermes-geral/USER.md` |
| Proatividade do Hermes Geral | `agentes/hermes-geral/HEARTBEAT.md` |
| Organograma da Grande Mente | `empresa/contexto/organograma-operacional-hermes-brain.md` |
| Rotinas documentadas | `empresa/rotinas/_index.md` |
| Skills do Brain | `empresa/skills/_index.md` |
| Pendências gerais | `empresa/gestao/pendencias.md` |
| Decisões permanentes | `empresa/decisoes/decisoes-permanentes.md` |
| LK Sneakers | `areas/lk/MAPA.md` |
| Zipper Galeria | `areas/zipper/MAPA.md` |
| SPITI Auction | `areas/spiti/MAPA.md` |
| Operações Hermes | `areas/operacoes/MAPA.md` |
| Segurança/governança | `seguranca/` e `areas/governanca/MAPA.md` |
| Evidências da ingestão Amora | `reports/amora-reference-ingest-2026-05-16/` |

## Regra de evolução

A estrutura cresce quando resolve problema real. Não criar pasta, agente, cron ou skill por estética.

- Processo único: executar e registrar se necessário.
- Processo repetido: documentar padrão.
- Processo recorrente/alto impacto: skill, rotina ou script.
- Processo com cadência comprovada: cron com destino, silêncio, erro e kill criteria.
