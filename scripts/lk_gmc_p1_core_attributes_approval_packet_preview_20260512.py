#!/usr/bin/env python3
"""LK GMC P1 core attributes approval packet preview, no-write.

Builds an exact-ID approval packet from the P1 core root-cause probe. It prepares
candidate attribute payloads and guardrails for a future Merchant correction, but
performs no Merchant/Shopify/Tiny/feed/DB writes and creates no rollback snapshots
until execution is explicitly approved.
"""
from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREVIEW_JSON = ROOT / 'reports/lk-gmc-2026-05-12-p1-attribute-completion-preview.json'
ROOT_CAUSE_JSON = ROOT / 'reports/lk-gmc-2026-05-12-p1-core-attributes-root-cause-probe.json'
RUN_STAMP = '2026-05-12-p1-core-attributes-approval-packet-preview'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
CORE_MAP = {
    'title': 'title',
    'link': 'link',
    'image link': 'imageLink',
    'price': 'price',
    'availability': 'availability',
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f'missing_file: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def main() -> None:
    preview = load(PREVIEW_JSON)
    root = load(ROOT_CAUSE_JSON)
    preview_by_id = {r.get('product_id'): r for r in preview.get('public_rows') or [] if r.get('product_id')}
    candidates = []
    blocked = []
    for r in root.get('rows') or []:
        pid = r.get('product_id')
        pr = preview_by_id.get(pid) or {}
        if r.get('root_cause_bucket') != 'root_cause_merchant_payload_missing_core_attrs_shopify_has_evidence':
            blocked.append({
                'product_id': pid,
                'offer_id': r.get('offer_id'),
                'reason': r.get('root_cause_bucket'),
                'write_allowed_now': False,
            })
            continue
        missing = r.get('merchant_missing_core_attrs_from_status') or []
        suggestions = pr.get('suggested_attributes') or {}
        proposed = {}
        missing_payload_fields = []
        for attr in missing:
            key = CORE_MAP.get(attr)
            if not key:
                continue
            val = suggestions.get(key)
            if val in (None, '', []):
                missing_payload_fields.append(key)
            else:
                proposed[key] = val
        if missing_payload_fields:
            blocked.append({
                'product_id': pid,
                'offer_id': r.get('offer_id'),
                'reason': 'candidate_missing_suggested_payload_fields',
                'missing_payload_fields': missing_payload_fields,
                'write_allowed_now': False,
            })
            continue
        candidates.append({
            'product_id': pid,
            'offer_id': r.get('offer_id'),
            'missing_core_attrs': missing,
            'proposed_core_attributes': proposed,
            'evidence': pr.get('evidence') or {},
            'shopify_product_title': r.get('shopify_product_title'),
            'merchant_title_before': r.get('merchant_title'),
            'rollback_required_before_write': True,
            'rollback_snapshot_method': 'products.get exact product_id; save full JSON resource under /opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots chmod 600 before update',
            'write_allowed_now': False,
            'future_write_scope_if_approved': 'exact Merchant online product update for proposed_core_attributes only; no local channel/POS rows; no Shopify/Tiny/feed/campaign writes',
        })

    attr_counts = Counter(a for c in candidates for a in c.get('missing_core_attrs') or [])
    field_counts = Counter(k for c in candidates for k in (c.get('proposed_core_attributes') or {}).keys())
    # Availability has a special stock-truth caveat for LK. It is present as a candidate,
    # but should either be explicitly approved from Shopify snapshot evidence or validated
    # against Tiny before execution policy is finalized.
    availability_rows = sum(1 for c in candidates if 'availability' in (c.get('proposed_core_attributes') or {}))
    summary = {
        'candidate_rows_in_packet_preview': len(candidates),
        'blocked_rows_in_packet_preview': len(blocked),
        'candidate_missing_core_attr_counts': dict(attr_counts),
        'candidate_proposed_payload_field_counts': dict(field_counts),
        'availability_candidate_rows_need_stock_truth_policy': availability_rows,
        'write_allowed_now': 0,
        'merchant_writes': 0,
        'shopify_writes': 0,
        'tiny_writes': 0,
        'feed_writes': 0,
        'database_writes': 0,
        'external_sends': 0,
    }
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_core_attributes_approval_packet_preview_ready_no_execution',
        'scope': 'No-write approval packet preview for exact online Merchant product IDs missing core attributes',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': summary,
        'approval_packet': {
            'candidate_count': len(candidates),
            'execution_not_authorized_by_this_file': True,
            'requires_lucas_approval_before_write': True,
            'recommended_execution_strategy': 'Prefer a bounded Content API products.update/custombatch executor only after full rollback snapshots; evaluate supplemental feed only if direct update is rejected/overwritten by source feed.',
            'stock_truth_caveat': 'availability is proposed from Shopify local snapshot evidence for Merchant completeness, but LK stock truth remains Tiny; execution policy should explicitly choose whether to write availability now or split title/link/imageLink/price first and validate availability against Tiny.',
            'hard_guards': [
                'exact product_id only; no wildcard/query updates',
                'abort if candidate product_id no longer exists in fresh products.get',
                'abort if current productstatus no longer has the same missing core attrs and product resource changed materially',
                'snapshot full current products.get resource for every exact product_id before write',
                'chmod 600 rollback snapshot; never commit raw rollback JSON',
                'write only proposed_core_attributes fields; preserve all other fields from current product resource',
                'never touch local channel rows or Shopify/Tiny/feed/campaign surfaces in this package',
                'post-write verify product resource and productstatus after Content API consistency delay',
            ],
        },
        'candidates': candidates,
        'blocked': blocked,
        'not_performed': ['merchant_product_delete','merchant_product_insert','merchant_product_update','content_api_custombatch','supplemental_feed_upload','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','rollback_snapshot_creation','pos_or_local_inventory_setting_change','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','missing_core_attrs','proposed_core_attributes','evidence','rollback_required_before_write','write_allowed_now','future_write_scope_if_approved']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in candidates:
            out = {k: c.get(k) for k in fields}
            out['missing_core_attrs'] = ';'.join(out.get('missing_core_attrs') or [])
            out['proposed_core_attributes'] = json.dumps(out.get('proposed_core_attributes') or {}, ensure_ascii=False)
            out['evidence'] = json.dumps(out.get('evidence') or {}, ensure_ascii=False)
            w.writerow(out)
    lines = [
        '# LK GMC P1 Core Attributes Approval Packet Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Candidatos exatos no packet preview: {summary['candidate_rows_in_packet_preview']}",
        f"- Bloqueados no packet preview: {summary['blocked_rows_in_packet_preview']}",
        f"- Campos propostos: {summary['candidate_proposed_payload_field_counts']}",
        f"- Linhas com availability proposta e caveat Tiny: {summary['availability_candidate_rows_need_stock_truth_policy']}",
        '- Writes executados: 0', '',
        '## Veredito',
        '- Packet preview pronto, mas ainda sem autorização de execução por este artefato. O pacote é tecnicamente estreito: exact online product IDs e core attrs calculados de evidência Shopify/Data Spine por SKU ativo exato.',
        '- Caveat importante: `availability` é atributo obrigatório no Merchant, mas estoque verdadeiro da LK é Tiny. Recomendo escolher explicitamente entre executar todos os core attrs com availability do snapshot Shopify, ou partir em dois pacotes: title/link/imageLink/price primeiro e availability após validação Tiny.', '',
        '## Não executado',
    ]
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1 core attributes approval packet preview'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: {payload['status']}.\n"
                 f"- Packet preview: candidatos={summary['candidate_rows_in_packet_preview']}; bloqueados={summary['blocked_rows_in_packet_preview']}; writes=0.\n"
                 f"- Caveat: availability exige política explícita por Tiny/Shopify antes de execução.\n"
                 f"- Execução futura exige aprovação Lucas, snapshot privado rollback e verificação pós-delay.\n\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Core Attributes Approval Packet Preview 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Packet preview no-write para correção de core attrs Merchant por exact product ID, com guardrails, rollback obrigatório e caveat de availability/Tiny |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
