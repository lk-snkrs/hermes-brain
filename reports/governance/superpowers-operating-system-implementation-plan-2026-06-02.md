# Implementation Plan — Superpowers Operating System para Hermes

**Data:** 2026-06-02  
**Origem:** `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/superpowers-operating-system-prd-2026-06-02.md`  
**Repo alvo:** `/opt/data/hermes_bruno_ingest/hermes-agent-upstream`  
**Plano executor:** `/opt/data/hermes_bruno_ingest/hermes-agent-upstream/.hermes/plans/superpowers-operating-system-implementation-plan-2026-06-02.md`  
**Status:** plano escrito; execução de código ainda não iniciada

Este arquivo é o espelho Brain do plano executor. A versão canônica para execução fica em:

`/opt/data/hermes_bruno_ingest/hermes-agent-upstream/.hermes/plans/superpowers-operating-system-implementation-plan-2026-06-02.md`

## Resumo

Implementar o Superpowers Operating System em blocos:

1. Núcleo offline `agent/superpowers_os.py` + regras YAML + testes.
2. Integração observe-only em `run_agent.py`.
3. Telemetry local profile-aware sem secrets.
4. Score/digest local sem Telegram inicialmente.
5. Config de rollout por perfil.
6. Warn/soft gates em fases posteriores.
7. Integração com relatório Hermes 02h30 só depois de aprovação/triagem do cron vivo.

## Guardrails

- Sem Docker/VPS/Traefik/secrets/externos.
- Sem restart de gateway nesta etapa.
- Sem novo cron Telegram nesta etapa.
- Falha do Superpowers OS degrada para no-op/observe.
- Telegram continua sem ruído técnico.

## Pontos de hook confirmados

- `run_agent.py` → `AIAgent.run_conversation()` inicia em torno da linha `10151`.
- `agent/prompt_builder.py` → `build_skills_system_prompt()` já lista skills obrigatórias.
- `agent/skill_commands.py` → `build_preloaded_skills_prompt()` já suporta preload session-wide.
- `hermes_cli/plugins.py` → hooks existentes: `pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `on_session_start`, `on_session_finalize`, `pre_gateway_dispatch`, approval hooks.

## Testes principais planejados

```bash
cd /opt/data/hermes_bruno_ingest/hermes-agent-upstream
python -m pytest tests/agent/test_superpowers_os.py -q
python -m pytest tests/test_superpowers_os_run_agent.py -q
python -m pytest tests/test_superpowers_os_report.py -q
python -m pytest tests/agent/test_skill_commands.py tests/tools/test_skills_tool.py tests/tools/test_skill_usage.py -q
```

## Próximo bloco recomendado

Executar o **Bloco A — Núcleo offline** do plano canônico:

- criar `agent/superpowers_os.py`;
- criar `agent/superpowers_rules.yaml`;
- criar `tests/agent/test_superpowers_os.py`;
- criar `scripts/superpowers_os_report.py`;
- rodar testes unitários.

Nada de runtime vivo deve ser alterado antes desse bloco passar.
