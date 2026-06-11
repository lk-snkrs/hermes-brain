# MAPA — LK Content

Subárea da LK Sneakers para o agente especialista **LK Content**: conteúdo premium, CRM, Klaviyo, newsletters, calendário editorial, criativos, social repurpose, Brand/Content Guide vivo e pós-mortems.

## Documentos principais

- `prd/lk-content-prd-20260607.md` — PRD completo do agente LK Content. Status: aprovado por Lucas em 2026-06-07; runtime ainda pendente de aprovação separada.
- `plans/lk-content-implementation-checklist-20260607.md` — checklist técnico-operacional para implementação futura.

## Pacote do agente

- `agentes/lk-content/` — pacote documental de identidade/rotina do perfil especialista.

Arquivos do pacote:

- `agentes/lk-content/IDENTITY.md`
- `agentes/lk-content/SOUL.md`
- `agentes/lk-content/AGENTS.md`
- `agentes/lk-content/USER.md`
- `agentes/lk-content/MEMORY.md`
- `agentes/lk-content/TOOLS.md`
- `agentes/lk-content/HEARTBEAT.md`
- `agentes/lk-content/MAPA.md`

## Estrutura planejada

- `brand-guide/` — Brand/Content Guide vivo da LK.
- `calendario/` — calendário editorial e sazonal.
- `campanhas/` — campanhas/newsletters planejadas e executadas.
- `flows/` — auditorias e propostas de flows Klaviyo.
- `moodboards/` — referências visuais e direção criativa.
- `performance/` — análises e scorecards.
- `postmortems/` — pós-mortems por campanha.
- `receipts/` — receipts operacionais sanitizados.
- `templates/` — templates de campanha, aprovação e checklist.
- `dashboards/` — visão executiva do agente.

## Guardrail

Este diretório é documental até aprovação explícita de ativação runtime. Não salvar tokens, API keys ou secrets no Brain.
## Projetos Brain OS

- `projetos/lk-content-klaviyo-agent/` — hub canônico para LK Content / Klaviyo Agent: PRD, agente documental, Klaviyo/CRM, calendário editorial, dashboard, Brand Guide, receipts e guardrails de envio/runtime.
