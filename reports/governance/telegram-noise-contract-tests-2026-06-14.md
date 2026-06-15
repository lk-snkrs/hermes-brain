# Telegram Noise Contract Tests — 2026-06-14

## Pedido

Lucas disse: "Seguir" após a wave curta de skill-quality. A wave de approval-packet completeness já estava presente no Brain, então avancei para a próxima melhoria recomendada: contrato local para evitar ruído em mensagens Telegram destinadas ao Lucas.

## Escopo

Classificação: A1 local/documental/testes.

Guardrails preservados:

- Sem envio Telegram.
- Sem runtime, Docker, VPS, Traefik, gateway, restart ou container.
- Sem alteração de cron schedule/delivery/enabled/state.
- Sem Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/banco/API externa.
- Sem WhatsApp/e-mail/envio externo.
- Sem secrets impressos; `values_printed=false`.

## Mudanças aplicadas

1. Novo validador local/read-only:
   - `scripts/telegram_noise_contract_validator.py`

2. Novo teste regressivo:
   - `tests/test_telegram_noise_contract_validator_20260614.py`

3. Novas referências de skill:
   - `/opt/data/skills/autonomous-ai-agents/hermes-agent/references/telegram-noise-contract-validator-20260614.md`
   - `/opt/data/skills/productivity/hermes-brain-governance/references/telegram-noise-contract-validator-20260614.md`

4. Pontes nos SKILL.md:
   - `hermes-agent/SKILL.md`
   - `hermes-brain-governance/SKILL.md`

## Contrato do validador

Bloqueia categorias de ruído em mensagens Lucas-facing:

- `inline_button_marker`: vazamento de `HERMES_INLINE_BUTTONS`.
- `job_id_leak`: exposição de `job_id`/cron ID bruto.
- `router_preflight_leak`: vazamento de `HERMES TASK ROUTER PREFLIGHT`, `decision_json`, `routing_policy` ou wrappers similares.
- `raw_log_or_json_dump`: command output, JSON dump ou traceback como mensagem final.
- `management_boilerplate`: instruções/configuração interna de delivery/tooling.
- `missing_actionability`: alerta sem ação, decisão, próximo passo, correção ou recomendação.

## TDD executado

RED:

- `python3 -m unittest tests/test_telegram_noise_contract_validator_20260614.py`
- Resultado esperado: erro por script ainda inexistente.

GREEN:

- Implementado `scripts/telegram_noise_contract_validator.py`.
- Reexecutado teste: 3 testes OK.

## Validação em artefatos representativos

Rodei o validador em 3 arquivos históricos/representativos de Telegram/governança:

- `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.md`
- `reports/governance/task-router-telegram-clean-decision-ux-fase6d-2026-05-24.md`
- `reports/governance/watchdog-telegram-alert-format-review-2026-06-07.md`

Resultado salvo em:

- `reports/telegram-noise-contract-validation-2026-06-14.json`

Status: `attention`, `files_checked=3`, `failures_count=2`, `values_printed=false`.

Interpretação: os achados ocorreram em relatórios históricos/governance, não em uma entrega Telegram atual. O validador está funcionando como detector; a aplicação produtiva deve mirar artefatos de preview/digest/decision-card antes de envio, não varrer toda documentação histórica como bloqueio absoluto.

## Resultado

A partir desta wave, mensagens/digests/cards Telegram podem passar por um gate local antes de serem tratados como Lucas-ready. Isso reduz o risco de repetir vazamento de wrapper, preflight, `job_id`, JSON/log cru ou alerta sem ação.
