#!/usr/bin/env python3
"""LK GMC P1-B corrected availability packet: propose `in stock` by policy.

Read-only/no-write. Lucas corrected that GMC availability should remain available
(`in stock`) even when Tiny has zero/no stock. Tiny remains internal stockout and
sourcing evidence, not the driver for GMC out-of-stock visibility.
"""
from __future__ import annotations

import base64
import csv
import importlib.util
import json
import os
import pathlib
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
RUN_STAMP = '2026-05-12-p1-availability-in-stock-policy-packet'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_secrets() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def offer_id(pid: str) -> str:
    parts = (pid or '').split(':', 3)
    return parts[3] if len(parts) == 4 else pid


def norm_attr(attr: str) -> str:
    return (attr or '').strip().lower().replace('_', ' ')


def missing_required_attrs(status: dict[str, Any]) -> set[str]:
    return {
        norm_attr(i.get('attributeName') or '')
        for i in (status.get('itemLevelIssues') or [])
        if i.get('code') in REQ_CODES and norm_attr(i.get('attributeName') or '')
    }


def main() -> None:
    audit = import_audit()
    secrets = load_secrets()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}

    rows: list[dict[str, Any]] = []
    for st in statuses:
        pid = st.get('productId') or ''
        attrs = missing_required_attrs(st)
        if chan(pid) != 'online' or 'availability' not in attrs:
            continue
        prod = product_by_id.get(pid) or {}
        rows.append({
            'product_id': pid,
            'offer_id': offer_id(pid),
            'merchant_title': prod.get('title') or st.get('title') or '',
            'current_availability': prod.get('availability') or '',
            'diagnostic_required_attrs': ';'.join(sorted(attrs)),
            'proposed_availability': 'in stock',
            'decision_state': 'ready_for_in_stock_policy_apply_if_lucas_approves',
            'evidence_label': 'manual_approval_policy_gmc_visibility_not_tiny_stock',
            'policy_caveat': 'Tiny zero/no stock remains internal stockout/sourcing evidence, but does not set GMC out of stock.',
            'write_scope_if_approved': 'update exact Merchant online product availability only, preserving current resource and using products.insert upsert',
            'rollback_required_before_write': True,
            'write_allowed_now': False,
        })
    rows.sort(key=lambda r: r['product_id'])
    counts = Counter(r['decision_state'] for r in rows)

    fields = ['product_id','offer_id','merchant_title','current_availability','diagnostic_required_attrs','proposed_availability','decision_state','evidence_label','policy_caveat','write_scope_if_approved','rollback_required_before_write','write_allowed_now']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_availability_in_stock_policy_packet_ready_no_write',
        'scope': 'Corrected no-write approval packet: set missing GMC availability to in stock by Lucas policy, independent of Tiny stock quantity.',
        'policy_correction': 'GMC availability should show in stock even when Tiny has zero/no stock; Tiny remains internal stockout/sourcing evidence.',
        'source_labels': ['fact_merchant_center', 'manual_approval_policy', 'derived_reconciliation'],
        'summary': {
            'merchant_products_current': len(products),
            'merchant_productstatuses_current': len(statuses),
            'online_rows_missing_availability': len(rows),
            'ready_for_in_stock_policy_apply_if_lucas_approves': len(rows),
            'proposed_in_stock': len(rows),
            'proposed_out_of_stock': 0,
            'decision_state_counts': dict(counts),
            'merchant_writes': 0,
            'tiny_calls': 0,
            'tiny_writes': 0,
            'shopify_writes': 0,
            'feed_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'samples': rows[:25],
        'files': {'public_json': str(OUT_JSON), 'public_csv': str(OUT_CSV), 'public_md': str(OUT_MD)},
        'not_performed': ['merchant_product_update', 'merchant_product_insert_upsert', 'tiny_call', 'tiny_write', 'shopify_write', 'feed_update_or_fetch', 'database_write', 'pos_write', 'campaign_or_external_send', 'sourcing_or_supplier_contact'],
        'approval_wording': f'Aprovo aplicar availability=in stock no Merchant para os {len(rows)} produtos online exatos do packet P1-B corrigido; Tiny zero/no stock não deve derrubar GMC availability; sem alterar Tiny/Shopify/feed/DB/POS/campanhas/sourcing, com rollback privado antes do write e piloto fail-fast primeiro.'
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC P1-B Availability In-Stock Policy Packet, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Correção de política',
        '- Lucas corrigiu: mesmo sem estoque no Tiny, o produto deve aparecer disponível no GMC.',
        '- Portanto, a proposta corrigida é `availability = in stock` para os produtos online exatos com availability ausente.',
        '- Tiny continua valendo para operação/sourcing/stockout, mas não para enviar `out of stock` ao GMC.', '',
        '## Resumo executivo',
        f"- Produtos online com diagnóstico `availability` ausente: {len(rows)}",
        f"- Proposta `in stock`: {len(rows)}",
        '- Proposta `out of stock`: 0',
        '- Tiny calls nesta correção: 0',
        '- Merchant/Tiny/Shopify/feed/DB/POS writes: 0', '',
        '## Amostra inline — primeiros 25 IDs',
    ]
    for r in rows[:25]:
        lines.append(f"- `{r['product_id']}` → `availability: in stock` — {r['merchant_title'][:140]}")
    lines.extend([
        '', '## Approval wording', f"`{payload['approval_wording']}`", '',
        '## Não executado'
    ])
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True)
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
