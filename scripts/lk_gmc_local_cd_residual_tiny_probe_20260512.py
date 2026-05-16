#!/usr/bin/env python3
"""Read-only Tiny probe for residual LK GMC local C/D candidates.

Consumes the Shopify-live local C/D preview and checks only the residual rows that
had no Shopify live exact SKU. Uses Tiny v2 read-only endpoints. No Merchant,
Shopify, Tiny, POS, feed, DB, campaign or external writes.
"""
from __future__ import annotations

import base64
import csv
import json
import os
import pathlib
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
INPUT_JSON = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-shopify-live-preview.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
RUN_STAMP = '2026-05-12-local-cd-residual-tiny-probe'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.csv'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_secrets() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
    req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def tiny_search(token: str, sku: str) -> list[dict[str, Any]]:
    body = tiny_call(token, 'produtos.pesquisa', {'pesquisa': sku, 'pagina': 1})
    retorno = (body or {}).get('retorno') or {}
    rows = retorno.get('produtos') or []
    out = []
    for item in rows:
        prod = (item or {}).get('produto') or {}
        out.append(prod)
    return out


def tiny_stock(token: str, tiny_id: str) -> dict[str, Any]:
    body = tiny_call(token, 'produto.obter.estoque', {'id': tiny_id})
    retorno = (body or {}).get('retorno') or {}
    return retorno.get('produto') or {}


def load_residual_rows() -> list[dict[str, Any]]:
    data = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    rows = []
    for sample_bucket in data.get('samples', {}).values():
        # Samples are incomplete, so read the full public CSV instead below.
        pass
    csv_path = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-shopify-live-preview.csv'
    all_rows = list(csv.DictReader(csv_path.open(encoding='utf-8')))
    return [r for r in all_rows if r.get('decision_state') == 'no_shopify_live_exact_sku_no_tiny_local_match_cleanup_candidate_after_pos_validation']


def saldo_from_stock(produto: dict[str, Any]) -> tuple[bool, float | None, int]:
    deposits = produto.get('depositos') or []
    official_seen = False
    saldo_val: float | None = None
    for item in deposits:
        dep = item.get('deposito') or {}
        if dep.get('nome') == OFFICIAL_DEPOSIT:
            official_seen = True
            raw = dep.get('saldo')
            if raw not in (None, ''):
                try:
                    saldo_val = float(str(raw).replace(',', '.'))
                except Exception:
                    saldo_val = None
    return official_seen, saldo_val, len(deposits)


def main() -> None:
    secrets = load_secrets()
    token = secrets.get('TINY_API_TOKEN') or ''
    if not token:
        raise RuntimeError('missing_tiny_api_token')
    residual = load_residual_rows()
    out_rows: list[dict[str, Any]] = []

    for i, row in enumerate(residual, start=1):
        sku = row.get('normalized_sku') or ''
        time.sleep(1.25)
        matches = tiny_search(token, sku)
        exact = [m for m in matches if str(m.get('codigo') or '') == sku]
        if exact:
            tiny_id = str(exact[0].get('id') or '')
            time.sleep(1.25)
            stock = tiny_stock(token, tiny_id) if tiny_id else {}
            official_seen, saldo, deposit_count = saldo_from_stock(stock)
            if official_seen and saldo is not None and saldo > 0:
                state = 'tiny_official_stock_positive_preserve_review_mapping'
                action = 'preserve; investigate Shopify/POS mapping drift before any Merchant local change'
            elif official_seen:
                state = 'tiny_official_stock_seen_zero_or_unknown_review_before_cleanup'
                action = 'review POS/Tiny history; no Merchant local cleanup until stale is confirmed'
            else:
                state = 'tiny_product_exact_code_found_no_official_deposit_review'
                action = 'review Tiny deposit mapping before Merchant action'
        else:
            tiny_id = ''
            stock = {}
            official_seen, saldo, deposit_count = False, None, 0
            state = 'tiny_no_exact_code_match_residual_cleanup_candidate_needs_pos_source_validation'
            action = 'candidate for residual approval packet only after POS/source validation and rollback snapshot'
        out_rows.append({
            'package': row.get('package'),
            'product_id': row.get('product_id'),
            'offer_id': row.get('offer_id'),
            'normalized_sku': sku,
            'merchant_title': row.get('merchant_title'),
            'shopify_state': row.get('decision_state'),
            'tiny_probe_state': state,
            'tiny_exact_match_count': len(exact),
            'tiny_id': tiny_id,
            'tiny_official_deposit_seen': official_seen,
            'tiny_official_deposit_saldo': saldo,
            'tiny_deposit_count': deposit_count,
            'recommended_next_action': action,
        })

    counts = Counter(r['tiny_probe_state'] for r in out_rows)
    by_package: dict[str, Counter] = defaultdict(Counter)
    for r in out_rows:
        by_package[r['package']][r['tiny_probe_state']] += 1
    final_cleanup = [r for r in out_rows if r['tiny_probe_state'] == 'tiny_no_exact_code_match_residual_cleanup_candidate_needs_pos_source_validation']
    preserve = [r for r in out_rows if r['tiny_probe_state'] != 'tiny_no_exact_code_match_residual_cleanup_candidate_needs_pos_source_validation']

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    fields = ['package','product_id','offer_id','normalized_sku','merchant_title','shopify_state','tiny_probe_state','tiny_exact_match_count','tiny_id','tiny_official_deposit_seen','tiny_official_deposit_saldo','tiny_deposit_count','recommended_next_action']
    for path in (PRIVATE_CSV, OUT_CSV):
        with path.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(out_rows)
    os.chmod(PRIVATE_CSV, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_local_cd_residual_tiny_probe_readonly',
        'scope': 'Read-only Tiny probe for 63 residual local C/D rows with no Shopify live exact SKU',
        'source_labels': ['fact_tiny_stock', 'fact_merchant_center', 'fact_shopify', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'input_residual_rows': len(residual),
            'tiny_probe_state_counts': dict(counts),
            'tiny_probe_state_counts_by_package': {pkg: dict(cnt) for pkg, cnt in by_package.items()},
            'preserve_or_review_not_cleanup_count': len(preserve),
            'final_cleanup_candidate_needs_pos_source_validation_count': len(final_cleanup),
            'tiny_writes': 0,
            'merchant_writes': 0,
            'shopify_writes': 0,
            'pos_or_local_inventory_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'samples': {
            'final_cleanup_candidates': final_cleanup[:20],
            'preserve_or_review': preserve[:20],
        },
        'private_csv': str(PRIVATE_CSV),
        'not_performed': ['merchant_product_delete','merchant_product_update','tiny_write','shopify_write','feed_update','database_write','local_inventory_disable','pos_inventory_write','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC Local C/D Residual Tiny Probe, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Residuais C/D de entrada: {len(residual)}",
        f"- Estados Tiny: {dict(counts)}",
        f"- Preservar/revisar antes de cleanup: {len(preserve)}",
        f"- Candidatos finais ainda dependentes de POS/source validation: {len(final_cleanup)}",
        '- Tiny/Merchant/Shopify/POS/DB writes: 0', '',
        '## Veredito',
        '- Este probe reduz a fila local para um pacote residual estrito; continua proibido deletar/alterar local em massa.',
        '- Qualquer candidato final ainda precisa validação POS/source e rollback privado antes de aprovação de execução.', '',
        '## Arquivos',
        f"- JSON público: `{OUT_JSON}`",
        f"- CSV público: `{OUT_CSV}`",
        f"- CSV privado/auditoria chmod 600: `{PRIVATE_CSV}`", '',
        '## Não executado',
    ]
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local C/D residual Tiny probe'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: Tiny probe read-only concluído para {len(residual)} residuais locais C/D.\n"
            f"- Estados: {dict(counts)}.\n"
            f"- Candidatos finais ainda dependentes de POS/source validation: {len(final_cleanup)}.\n"
            f"- Nenhum Tiny/Merchant/Shopify/POS/feed/DB write executado.\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
