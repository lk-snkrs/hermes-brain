# Skill Quality Triage — 2026-06-25

## Contexto

O preflight diário v4 voltou a apontar `skill_quality_drift`: 80 skills com risco de carga excessiva ou marcador de staleness. Não houve referências faltantes nos principais riscos; o problema atual é principalmente confiança operacional e custo cognitivo de skills muito grandes/stale.

## Classificação

- Risco: A1 local/documental.
- Valores de secret impressos: false.
- Ações externas: nenhuma.
- Runtime/Docker/gateway/cron: nenhuma mutação.

## Evidência resumida

- Skills escaneadas: 226.
- Skills sinalizadas: 80.
- Principais classes de risco: `oversized_skill_load` e `contains_staleness_marker`.
- Top alvos atuais: `bruno-openclaw-hermes-brain-adaptation`, `research-paper-writing`, `hermes-agent`, `lk-operational-intelligence`, `lucas-hermes-continuous-improvement`, `hermes-brain-governance`, `mission-control-development`, `lk-seo-weekly-improvement`, `claude-code`, `lucas-chief-of-staff`, `lk-shopify-readonly`, `multiempresa-routing-lucas`.

## Decisão operacional para próximos ciclos

Não repetir o alerta como ruído genérico. Tratar como fila de higiene por ondas pequenas:

1. Priorizar skills carregadas por crons/rotinas críticas antes de skills raras.
2. Para skills oversized, mover detalhes episódicos para `references/` e deixar o `SKILL.md` como contrato operacional curto.
3. Para marcadores de staleness, verificar a fonte viva/Brain antes de obedecer à instrução antiga.
4. Toda wave deve ter readback, secret scan, e receipt quando editar skill/Brain.
5. Não alterar runtime, gateways, Docker, cron schedule, credenciais ou integrações externas dentro dessa higiene.

## Próxima ação segura recomendada

Próxima wave A1: escolher no máximo 2–3 skills críticas de alto uso diário (`hermes-agent`, `lucas-hermes-continuous-improvement`, `multiempresa-routing-lucas` ou `lucas-chief-of-staff`) e extrair blocos históricos longos para referências curtas, preservando os gatilhos e regras atuais no `SKILL.md`.

## Resultado deste run

A melhoria aplicada hoje foi transformar o achado recorrente em triagem operável e critério de onda, sem mexer em produção. O contador de skills sinalizadas ainda não foi reduzido; por isso continua como dívida controlada, não incidente.

values_printed=false
