# Brain OS — Executive Status

**Atualizado em:** 2026-06-11T15:54:29.783872+00:00
**Audiência:** Lucas / Hermes default / especialistas
**Modo:** status documental automático, local/read-only.
**Fonte principal:** scanner v2 + health audit + manifests locais.
**Runtime:** não tocado.
**External APIs:** não usadas.
**Secrets:** não impressos.

## TL;DR

Brain OS está operacional e versionado; o foco passou de criar hubs para maturidade semântica. O status atual é **verde**: pacote estrutural saudável, com melhoria pendente em qualidade/metadata dos hubs e classificação fina de lacunas.

## Snapshot executivo

- **Hubs vivos auditados:** 56
- **Hubs por área:** lk=34, operacoes=17, spiti=2, zipper=3
- **Qualidade:** A=56 / B=0 / C=0 / D=0
- **Scanner:** 53 candidatos, 0 sem hub vivo, 0 com score >= 80
- **Health:** critical=0 / needs_attention=0 / watch=0 / healthy=56
- **Stale:** 0 hubs acima do limite de atualização documental
- **Risco:** 0 hubs com guardrails/fonte viva/write/runtime relevantes a revisar
- **Veredito:** verde

## Status por eixo

- **Hubs canônicos:** verde — pacote mínimo auditado localmente.
- **Scanner:** verde — v2 classifica hub/receipt/backup/artifact e não conta diretório como hub vivo sem manifest canônico.
- **Health local:** verde — auditoria local gerada em `reports/governance/brain-os/brain-os-health-latest.json`.
- **Qualidade documental:** amarelo — ainda há hubs B/C por metadata, fonte viva ou NEXT_STEPS fracos.
- **Fonte viva / stale risk:** verde — docs não substituem fonte viva externa.
- **Risco externo / runtime:** verde — este processo não tocou runtime, Docker, VPS, cron, secrets ou APIs externas.

## Hubs vivos por área

- `lk`: 34
- `operacoes`: 17
- `spiti`: 2
- `zipper`: 3

## Qualidade dos hubs

### Critério de grade

- **A:** score >= 90.
- **B:** score 75–89.
- **C:** score 60–74.
- **D:** score < 60.

### Distribuição

- **A:** 56
- **B:** 0
- **C:** 0
- **D:** 0

### Hubs que exigem atenção

- Nenhuma lacuna crítica.

## Scanner — cobertura e lacunas

- **Relatório:** `reports/governance/brain-os/brain-os-candidates-latest.json`
- **Gerado em:** 2026-06-11T15:54:27.445876+00:00
- **Versão:** brain-os-v2
- **Política de classificação:** brain-os-artifact-classification-v1
- **Arquivos texto escaneados:** 1047
- **Candidatos:** 53
- **Candidatos sem hub vivo:** 0
- **Manifest class counts:** `{'hub_manifest': 56}`

### Maiores scores do scanner

- `lk-growth-gmc-shopify-meta` — score 37 / wave 1 / maturity `live_hub_present`
- `lk-reporting-briefings` — score 33 / wave 5 / maturity `live_hub_present`
- `lk-stock-tiny-pos` — score 32 / wave 1 / maturity `live_hub_present`
- `lk-approval-learning-ledger` — score 31 / wave 5 / maturity `live_hub_present`
- `mordomo-os` — score 26 / wave 2 / maturity `live_hub_present`
- `zipper-email-crm-intake` — score 26 / wave 2 / maturity `live_hub_present`
- `theme-cro-performance` — score 26 / wave 3 / maturity `live_hub_present`
- `executive-dashboards` — score 26 / wave 3 / maturity `live_hub_present`

### Próximas lacunas sugeridas pelo scanner

- Nenhuma lacuna crítica.

## Health local

- **Script:** `scripts/brain_os_health.py`
- **Modo:** local/read-only.
- **Average score:** 95.7/100
- **Top issues:** `{'artifact_index_missing_sample_paths_3': 11, 'artifact_index_missing_sample_paths_8': 8, 'artifact_index_missing_sample_paths_7': 7, 'artifact_index_missing_sample_paths_5': 7, 'artifact_index_missing_sample_paths_4': 4, 'artifact_index_missing_sample_paths_6': 4, 'artifact_index_missing_sample_paths_12': 2, 'artifact_index_missing_sample_paths_2': 1, 'artifact_index_missing_sample_paths_13': 1, 'artifact_index_missing_sample_paths_15': 1, 'artifact_index_missing_sample_paths_18': 1, 'artifact_index_missing_sample_paths_1': 1, 'artifact_index_missing_sample_paths_11': 1, 'artifact_index_missing_sample_paths_16': 1, 'artifact_index_missing_sample_paths_9': 1}`

## Stale / risco de fonte viva

Nenhum arquivo do Brain autoriza afirmar estado vivo externo sem consultar a fonte autorizada quando a pergunta depende de estado atual.

### Hubs stale ou próximos de stale

- Nenhum hub stale pelo limite atual.

## Risco externo / sensível

### Guardrails ativos

- Nenhum scanner score autoriza ação externa.
- Nenhum receipt/report/backup substitui `CURRENT_STATE.md` sem reconciliação.
- Fonte viva externa vence snapshot/documento quando a pergunta exige estado atual.
- Sem writes em Shopify/Tiny/GMC/Meta/Klaviyo/Chatwoot/Supabase sem aprovação escopada.
- Sem runtime/Docker/VPS/gateway/cron neste processo.
- Sem secrets em markdown, JSON, logs ou diffs.

## Próximas ações recomendadas

### P0 — Segurança / confiança

- Nenhuma lacuna crítica.

### P1 — Maturidade Brain OS

- Normalizar metadados dos hubs C/D.
- Fortalecer `source_of_truth`, `guardrails` e `NEXT_STEPS.md` decision-grade.
- Corrigir `ARTIFACT_INDEX.md` com paths quebrados/absolutos onde houver.

### P2 — Evolução do scanner

- Manter scanner v2 como fonte local para separar hub/receipt/backup/artifact.
- Considerar JSON sidecar do status executivo se Mission Control precisar consumir.
- Transformar check silent-OK em cron apenas com aprovação escopada futura.

## Como usar este status

1. Para estado executivo: ler este arquivo primeiro.
2. Para estado de projeto: abrir o hub canônico em `areas/**/projetos/<slug>/`.
3. Para decisão atual: ler `CURRENT_STATE.md` e `DECISIONS_AND_GUARDRAILS.md`.
4. Para evidência histórica: consultar `ARTIFACT_INDEX.md`, `TIMELINE.md`, reports e receipts.
5. Para qualquer estado vivo externo: consultar a fonte viva autorizada antes de afirmar ou agir.

## Data sources

- `reports/governance/brain-os/brain-os-candidates-latest.json`
- `reports/governance/brain-os/brain-os-health-latest.json`
- `areas/**/projetos/*/manifest.json`
- `scripts/brain_os_scanner_v2.py`
- `scripts/brain_os_health.py`

## Notas de geração

- Geração local/read-only.
- Não chama APIs externas.
- Não lê binários.
- Não imprime secrets.
- Não altera runtime, Docker, cron, gateway ou VPS.
