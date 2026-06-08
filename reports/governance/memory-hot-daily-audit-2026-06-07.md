# Audit — memories/hot/daily e boot memory

Data: 2026-06-07
Escopo: audit local/read-only + documentação Brain. Sem alteração de runtime, Docker/VPS/Traefik, providers externos, crons, gateways ou sistemas externos.

## Veredito curto

**Parcialmente correto.**

- **Boot memory (`MEMORY.md`/`USER.md`) está sendo usada corretamente agora**: boot mínimo, sem saturação, provider externo off, cobertura diária com templates para todos os profiles que têm memória.
- **`daily/` existe como camada de continuidade**, mas estava incompleta para 2026-06-07 até o watchdog estrutural criar skeleton durante esta auditoria.
- **`hot.md` não está sendo usado corretamente no momento**: está grande, antigo e com itens que já deveriam ter sido rebaixados para reports/receipts/daily ou atualizados. O próprio watchdog estrutural marca `memories/hot.md stale >3 days`.

## Evidência coletada

### 1. Política canônica

Fonte: `memories/politica-memoria-hermes.md`.

Camadas esperadas:

- `MEMORY.md`/`USER.md`: boot mínimo injetado, preferências, guardrails e ponteiros.
- `hot.md`: prioridades atuais, bloqueios atuais, decisões recentes que ainda afetam ação e links quentes.
- `daily/YYYY-MM-DD.md`: decisões, entregas, handoffs, aprendizados, não-ações e bloqueios do dia.
- `reports/receipts/archive`: evidência longa e auditorias.
- skills: procedimentos repetíveis.
- provider externo: decisão atual é não usar; Brain é fonte rica canônica.

### 2. Boot memories por profile

Medição em 2026-06-07:

- Default: MEMORY 68.7%, USER 74.3%.
- `brain-process`: MEMORY 21.9%, USER 19.3%.
- `hermes-ops-readonly`: MEMORY 19.8%, USER 16.4%.
- `lk-analyst-readonly`: MEMORY 19.0%, USER 14.9%.
- `lk-collection-optimizer`: MEMORY 35.6%, USER 18.4%.
- `lk-content-reviewer`: MEMORY 18.2%, USER 14.7%.
- `lk-growth`: MEMORY 35.5%, USER 15.4%.
- `lk-ops`: MEMORY 49.3%, USER 56.6%.
- `lk-shopify`: MEMORY 61.6%, USER 52.6%.
- `lk-trends`: MEMORY 19.1%, USER 14.8%.
- `mordomo`: MEMORY 72.0%, USER 43.7%.
- `spiti`: MEMORY 25.0%, USER 13.7%.

Conclusão: nenhum arquivo acima de 80%; nenhum over-limit; nenhum indício de segredo pelo watchdog. Default ainda está acima da meta ideal de 40–60%, mas abaixo do gatilho de saturação e aceitável como boot mínimo com guardrails globais.

### 3. Watchdog 02h15 de higiene de memória

Fonte: `reports/memory-hygiene/latest.json`.

- `status=ok`.
- `files_checked=24`.
- `near_saturation_count=0`.
- `over_limit_count=0`.
- `possible_secret_locator_count=0`.
- `external_memory_provider_active=false`.
- `coverage_missing_for_existing_memory=[]`.
- `auto_compaction_count=5` na última execução: default MEMORY, default USER, Mordomo USER, LK Ops USER, LK Shopify USER.

Conclusão: o 02h15 está funcionando corretamente como watchdog/silent-OK local. Ele corrige boot memory antes de alertar Lucas.

### 4. `daily/`

Estado encontrado:

- `memories/daily/2026-06-07.md` estava ausente no início da auditoria.
- Rodada manual do watchdog estrutural criou o skeleton local automaticamente.
- O fechamento detalhado já existia em `reports/daily-consolidation/2026-06-07.md` com 13 KB, mas não havia sido promovido para `memories/daily/2026-06-07.md`.

Conclusão: a rotina de fechamento gera report/handoff, mas a camada daily ainda depende do watchdog estrutural para criar skeleton. O daily não está recebendo curadoria suficiente com as decisões reais do fechamento.

### 5. `hot.md`

Estado encontrado:

- `memories/hot.md`: ~7.3 KB, atualizado em 2026-06-01.
- Contém política correta de memória, mas também itens current antigos e marcadores stale, por exemplo versão/runtime antiga e pendências/decisões de maio/início de junho que deveriam estar em receipts/reports/daily.
- O cron `Hermes Brain Operating Layer structural watchdog` marcou último status não-ok por `memories/hot.md stale >3 days`.
- Rodada manual do script confirmou: `memories/hot.md stale >3 days`.

Conclusão: `hot.md` virou mistura de política, prioridades e histórico. Deve ser compactado para uma página current, com links para a política e reports, não manter narrativa longa.

## Falhas reais

1. **Hot stale**: maior problema. O arquivo deveria ser current e está parado desde 2026-06-01.
2. **Daily skeleton, não daily curado**: 2026-06-07 só foi criado por auto-heal; a informação real está no fechamento, não no daily.
3. **Fechamento não fecha a cadeia completa**: 01h/02h/02h15 gera reports/receipts, mas falta etapa consistente de promover resumo curado para daily e refrescar hot.
4. **Telegram report acertou ao alertar `hot.md stale`**, mas o alerta recorrente deveria virar ação local de refresh/compactação, não só ser mencionado.

## O que está correto

1. Arquitetura de camadas está certa: Brain rico; prompt memory mínimo; reports/receipts para evidência; hot/daily para continuidade.
2. Provider externo continua off, alinhado à decisão de Lucas.
3. Watchdog de boot memory está correto e coberto por roster real.
4. Brain Health Check passou: FAIL=0/WARN=0.
5. Focused secret scan nos arquivos de memória current não encontrou tokens/API keys em claro.

## Correção local aplicada após o audit

Pacote local/documental executado na mesma sessão, sem tocar runtime ou sistemas externos:

1. Backups criados em `reports/governance/memory-backups/` para `memories/hot.md` e `memories/daily/2026-06-07.md`.
2. `memories/hot.md` reescrito como camada current compacta:
   - manteve prioridades/guardrails/bloqueios desta semana;
   - passou a linkar `memories/politica-memoria-hermes.md` em vez de repetir política longa;
   - removeu itens históricos e referências stale;
   - registrou v0.16.0 como runtime esperado atual e antigo alerta de versão como superseded.
3. `memories/daily/2026-06-07.md` complementado com resumo curado do fechamento/audit, sem segredo e sem payload sensível.
4. Verificação final:
   - `brain_operating_layer_audit.py`: `rc=0`, stdout vazio;
   - `brain_health_check.py`: FAIL=0/WARN=0;
   - focused secret scan em report, daily e hot: 0 hits.

## Próxima melhoria recomendada

Ajustar o Fechamento 01h ou o supervisor 02h para, quando houver fechamento material, atualizar `daily/` e `hot.md` automaticamente antes do relatório 02h30. Isso evita que o structural watchdog precise auto-healar daily ou acusar `hot.md stale` no dia seguinte.

## Não-ações nesta auditoria

- Não alterei Docker/VPS/Traefik/SSH/containers.
- Não alterei gateways, providers, webhooks, API server ou crons.
- Não fiz writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail.
- Não expus segredos.
- Única mudança operacional local indireta: o watchdog estrutural criou o skeleton `memories/daily/2026-06-07.md` ao ser executado manualmente para verificação.
