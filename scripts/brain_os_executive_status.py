#!/usr/bin/env python3
"""Generate Brain OS executive status from local scanner + health reports."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def area_of(path: str) -> str:
    parts = Path(path).parts
    return parts[1] if len(parts) > 1 and parts[0] == 'areas' else 'unknown'


def grade(score: int) -> str:
    return 'A' if score >= 90 else 'B' if score >= 75 else 'C' if score >= 60 else 'D'


def bullets(items: list[str], empty: str = '- Nenhuma lacuna crítica.') -> str:
    return '\n'.join(f'- {x}' for x in items) if items else empty


def render(root: Path, scanner: dict, health: dict) -> str:
    now = datetime.now(timezone.utc).isoformat()
    hubs = health.get('hubs', [])
    grades = Counter(grade(h['score']) for h in hubs)
    by_area = Counter(area_of(h['hub_path']) for h in hubs)
    stale = [h for h in hubs if h.get('age_days') is not None and h.get('age_days', 0) > 60]
    attention = [h for h in sorted(hubs, key=lambda x: (x['score'], x['hub_path'])) if h['score'] < 75][:10]
    top_candidates = sorted(scanner.get('candidates', []), key=lambda c: (-c.get('score', 0), c.get('wave', 99)))[:8]
    gaps = [c for c in scanner.get('candidates', []) if c.get('live_hub_count', len(c.get('existing_hubs', []))) == 0]
    high = sum(1 for c in scanner.get('candidates', []) if c.get('score', 0) >= 80)
    risk = sum(1 for h in hubs if any(x in ' '.join(h.get('issues', [])).lower() for x in ['fonte','external','runtime','write','source']))
    overall = 'verde' if health.get('status_counts', {}).get('critical', 0) == 0 and not gaps else 'amarelo'
    return f"""# Brain OS — Executive Status

**Atualizado em:** {now}
**Audiência:** Lucas / Hermes default / especialistas
**Modo:** status documental automático, local/read-only.
**Fonte principal:** scanner v2 + health audit + manifests locais.
**Runtime:** não tocado.
**External APIs:** não usadas.
**Secrets:** não impressos.

## TL;DR

Brain OS está operacional e versionado; o foco passou de criar hubs para maturidade semântica. O status atual é **{overall}**: pacote estrutural saudável, com melhoria pendente em qualidade/metadata dos hubs e classificação fina de lacunas.

## Snapshot executivo

- **Hubs vivos auditados:** {health.get('total_hubs', 0)}
- **Hubs por área:** {', '.join(f'{k}={v}' for k, v in sorted(by_area.items()))}
- **Qualidade:** A={grades['A']} / B={grades['B']} / C={grades['C']} / D={grades['D']}
- **Scanner:** {scanner.get('candidate_count', len(scanner.get('candidates', [])))} candidatos, {scanner.get('candidates_without_live_hub', len(gaps))} sem hub vivo, {high} com score >= 80
- **Health:** critical={health.get('status_counts', {}).get('critical', 0)} / needs_attention={health.get('status_counts', {}).get('needs_attention', 0)} / watch={health.get('status_counts', {}).get('watch', 0)} / healthy={health.get('status_counts', {}).get('healthy', 0)}
- **Stale:** {len(stale)} hubs acima do limite de atualização documental
- **Risco:** {risk} hubs com guardrails/fonte viva/write/runtime relevantes a revisar
- **Veredito:** {overall}

## Status por eixo

- **Hubs canônicos:** verde — pacote mínimo auditado localmente.
- **Scanner:** verde — v2 classifica hub/receipt/backup/artifact e não conta diretório como hub vivo sem manifest canônico.
- **Health local:** {'verde' if health.get('status_counts', {}).get('critical', 0) == 0 else 'amarelo'} — auditoria local gerada em `reports/governance/brain-os/brain-os-health-latest.json`.
- **Qualidade documental:** amarelo — ainda há hubs B/C por metadata, fonte viva ou NEXT_STEPS fracos.
- **Fonte viva / stale risk:** {'verde' if not stale else 'amarelo'} — docs não substituem fonte viva externa.
- **Risco externo / runtime:** verde — este processo não tocou runtime, Docker, VPS, cron, secrets ou APIs externas.

## Hubs vivos por área

{bullets([f'`{k}`: {v}' for k, v in sorted(by_area.items())])}

## Qualidade dos hubs

### Critério de grade

- **A:** score >= 90.
- **B:** score 75–89.
- **C:** score 60–74.
- **D:** score < 60.

### Distribuição

- **A:** {grades['A']}
- **B:** {grades['B']}
- **C:** {grades['C']}
- **D:** {grades['D']}

### Hubs que exigem atenção

{bullets([f"`{h['hub_path']}` — {h['score']}/100 ({h['status']}); {', '.join(h.get('issues', [])[:3]) or 'sem issue listada'}" for h in attention])}

## Scanner — cobertura e lacunas

- **Relatório:** `reports/governance/brain-os/brain-os-candidates-latest.json`
- **Gerado em:** {scanner.get('generated_at')}
- **Versão:** {scanner.get('scanner_version')}
- **Política de classificação:** {scanner.get('classification_policy_version')}
- **Arquivos texto escaneados:** {scanner.get('total_text_files_scanned')}
- **Candidatos:** {scanner.get('candidate_count', len(scanner.get('candidates', [])))}
- **Candidatos sem hub vivo:** {scanner.get('candidates_without_live_hub', len(gaps))}
- **Manifest class counts:** `{scanner.get('manifest_class_counts', {})}`

### Maiores scores do scanner

{bullets([f"`{c['id']}` — score {c.get('score')} / wave {c.get('wave')} / maturity `{c.get('maturity', 'n/a')}`" for c in top_candidates])}

### Próximas lacunas sugeridas pelo scanner

{bullets([f"`{c['id']}` — {c.get('recommendation')}" for c in gaps])}

## Health local

- **Script:** `scripts/brain_os_health.py`
- **Modo:** local/read-only.
- **Average score:** {health.get('average_score')}/100
- **Top issues:** `{health.get('top_issues', {})}`

## Stale / risco de fonte viva

Nenhum arquivo do Brain autoriza afirmar estado vivo externo sem consultar a fonte autorizada quando a pergunta depende de estado atual.

### Hubs stale ou próximos de stale

{bullets([f"`{h['hub_path']}` — age_days={h.get('age_days')}" for h in stale[:10]], '- Nenhum hub stale pelo limite atual.')}

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

{bullets(['Corrigir qualquer hub D/critical antes de declarar Brain OS verde total.'] if grades['D'] else [])}

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
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--scanner', default='reports/governance/brain-os/brain-os-candidates-latest.json')
    ap.add_argument('--health', default='reports/governance/brain-os/brain-os-health-latest.json')
    ap.add_argument('--output')
    ap.add_argument('--latest')
    ap.add_argument('--stdout', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    md = render(root, load_json(root / args.scanner), load_json(root / args.health))
    for out in [args.output, args.latest]:
        if out:
            p = root / out
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(md, encoding='utf-8')
    if args.stdout or not (args.output or args.latest):
        print(md)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
