# Painel Semanal do Brain — 2026-05-19

Janela: primeira semana de ativação do Brain Sync seguro, com foco em consolidação do Brain, higiene estrutural e bloqueios corretos.

## 1. Resumo executivo

- O Brain Sync seguro está ativo e fazendo a separação correta entre documentação versionável e artefato bruto/local.
- Health check estrutural após correções: **FAIL=0 / WARN=0**.
- O índice de rotinas agora cobre os documentos que estavam gerando WARN.
- A sub-área Zipper Programação agora tem `MAPA.md` e está navegável.
- A política de relatórios ficou explícita: relatório bruto não entra por padrão; síntese curada entra no Brain.

## 2. Entrou no Brain nesta rodada

- `areas/zipper/sub-areas/programacao/MAPA.md` — MAPA da sub-área de programação/exposições da Zipper.
- `areas/zipper/MAPA.md` — navegação atualizada para incluir Programação.
- `empresa/rotinas/_index.md` — indexação das rotinas que faltavam.
- `areas/operacoes/rotinas/brain-sync.md` — política de promoção/bloqueio de relatórios.
- `areas/operacoes/rotinas/painel-semanal-brain.md` — rotina do painel semanal.
- `areas/operacoes/MAPA.md` — link para o painel semanal.
- `reports/brain-health-check-2026-05-19-final-three-fixes.json` — evidência final do health check sem FAIL/WARN.

## 3. Bloqueado pelo Brain Sync

O dry-run do Brain Sync mostrou **164 arquivos bloqueados**. Isso é esperado e majoritariamente saudável: são artefatos brutos, HTMLs, JSONs, scripts/configs ou reports ainda não promovidos para documentação executiva.

### Motivos capturados

- deny_part: 21
- deny_suffix: 21
- not_in_allowlist: 96
- suffix_not_allowed: 26

### Exemplos representativos

  - `areas/lk/operacoes/lk-os-status-audit-latest.json [not_in_allowlist]`
  - `areas/operacoes/reports/mordomo-email-intake-readonly-audit-2026-05-18.json [not_in_allowlist]`
  - `areas/operacoes/scripts/__pycache__/hermes_runtime_cron_watchdog.cpython-313.pyc [deny_part]`
  - `areas/operacoes/scripts/hermes_runtime_cron_watchdog.py [deny_part]`
  - `config/lk-report-delivery-targets.json [deny_part]`
  - `reports/hermes-compression-self-heal/compression-self-heal-20260516T201012Z.json [not_in_allowlist]`
  - `reports/hermes-host-docker-observability-2026-05-17.json [not_in_allowlist]`
  - `reports/hermes-host-docker-observability-2026-05-18.json [not_in_allowlist]`
  - `reports/hermes-host-docker-observability-2026-05-19.json [not_in_allowlist]`
  - `reports/hermes-stt-runtime-fix-2026-05-16.md [not_in_allowlist]`
  - `reports/lk-16h-cron-failure-fix-2026-05-18.md [not_in_allowlist]`
  - `reports/lk-cro-chat-availability-copy-fix-2026-05-18.md [not_in_allowlist]`

## 4. Política refinada de relatórios

Agora a rotina `brain-sync.md` registra explicitamente:

- **Entra automaticamente**: fechamento diário curado, health checks, continuous improvement e sínteses `.md` promovidas para `areas/**`.
- **Fica local/bloqueado**: HTML, CSV, JSON bruto, dumps, receipts operacionais, logs, snapshots privados, payloads, PII e relatórios ainda não curados.
- Quando algo bruto for importante, o caminho correto é criar uma **síntese executiva `.md`** na área correspondente, mantendo o bruto fora do GitHub automático.

## 5. Saúde do Brain

Resultado da validação:

- secrets: FAIL=0 WARN=0
- links: FAIL=0 WARN=0
- required_files: FAIL=0 WARN=0
- agent_files: FAIL=0 WARN=0
- area_maps: FAIL=0 WARN=0
- routines_index: FAIL=0 WARN=0
- skill_references: FAIL=0 WARN=0

Evidência: `reports/brain-health-check-2026-05-19-final-three-fixes.json`.

## 6. Rotinas/MAPAs promovidos ou limpos

Promovidos/indexados nesta rodada:

- `areas/lk/rotinas/lk-cro-size-filter-concept-correction-2026-05-18.md`
- `areas/lk/sub-areas/crm/rotinas/playbook-newsletter-klaviyo-lk.md`
- `areas/lk/sub-areas/crm/rotinas/playbook-whatsapp-meta-templates-carrinho-checkout-abandonado-2026-05-19.md`
- `areas/lk/sub-areas/growth/rotinas/weekly-growth-review.md`
- `areas/operacoes/rotinas/mordomo-email-whatsapp-intake-correction-2026-05-18.md`
- `areas/operacoes/rotinas/mordomo-global-followup-engine-2026-05-18.md`
- `areas/operacoes/rotinas/mordomo-prd-implementation-1-3-5-6-2026-05-18.md`
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `areas/zipper/sub-areas/programacao/MAPA.md`

## 7. Guardrails e não-ações

Não foi feito:

- nenhum envio Telegram/WhatsApp/e-mail de sucesso normal;
- nenhum write em Shopify, GMC, Klaviyo, Meta, Supabase, banco, Docker, VPS, gateway ou n8n;
- nenhum commit de `config/`, `scripts/`, `tests/`, HTML, CSV, dumps ou JSON bruto não permitido;
- nenhuma exposição de segredo.

## 8. Próxima semana

1. Promover apenas os relatórios brutos que tiverem valor executivo real, criando sínteses `.md` nas áreas corretas.
2. Revisar os 164 bloqueios por categoria, não arquivo a arquivo, para evitar burocracia.
3. Avaliar se o painel semanal deve virar cron local recorrente; por enquanto fica manual/on-demand para evitar ruído.
