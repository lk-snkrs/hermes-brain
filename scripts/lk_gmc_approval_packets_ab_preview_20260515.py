#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import pathlib
import sqlite3
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
PRICE_JSON = ROOT / 'reports/lk-gmc-2026-05-14-post-gtin-price-updated-preview.json'
LANDING_JSON = ROOT / 'reports/lk-gmc-2026-05-14-landing-page-current-drilldown.json'
OUT_DIR = ROOT / 'reports/gmc_approval_packets_20260515'
BRAIN_MD = ROOT / 'areas/lk/rotinas/gmc-approval-packets-ab-preview-2026-05-15.md'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
DATA_SOURCE = 'accounts/*/dataSources/10636492695'
MERCHANT_ID = '103444654'


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def micros(price: str | None) -> str | None:
    if price is None:
        return None
    d = Decimal(str(price)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return str(int(d * Decimal(1_000_000)))


def write_csv(path: pathlib.Path, rows: list[dict], fields: list[str]) -> None:
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow(r)


def log_decision(payload: dict) -> None:
    if not LOCAL_DB.exists():
        return
    con = sqlite3.connect(str(LOCAL_DB))
    try:
        cols = [r[1] for r in con.execute('pragma table_info(lk_approval_decision_ledger)')]
        decision_id = 'gmc_approval_packets_ab_preview_20260515'
        learning = json.dumps({'summary': payload['summary'], 'artifacts': payload['artifacts']}, ensure_ascii=False)
        if 'decision_id' in cols:
            con.execute('''
                insert or replace into lk_approval_decision_ledger
                (decision_id,created_at,updated_at,business,domain,source_request,rule_id,status,risk_level,allowed_next_action,blocked_actions,requires_future_approval,external_or_visible_write_done,evidence_artifact,learning,owner)
                values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                decision_id,
                payload['generated_at'],
                payload['generated_at'],
                'LK',
                'GMC',
                'seguir: prepare next explicit approval packages A/B only',
                'LK-APPROVAL-GMC-GATE-20260515',
                'preview_only_needs_explicit_approval_before_write',
                'A3',
                'Lucas may explicitly approve A 10, A 42, or B 20; otherwise continue read-only.',
                'Merchant write; ProductInputs PATCH; Content API delete/upsert; Shopify write; feed fetch/upload; external send',
                1,
                0,
                str(BRAIN_MD),
                learning,
                'Hermes',
            ))
        else:
            con.execute('''
                create table if not exists lk_approval_decision_ledger (
                    id integer primary key autoincrement,
                    created_at text not null,
                    gate_id text,
                    risk_level text,
                    decision text,
                    artifact_path text,
                    payload_json text
                )
            ''')
            con.execute('''
                insert into lk_approval_decision_ledger
                (created_at,gate_id,risk_level,decision,artifact_path,payload_json)
                values (?,?,?,?,?,?)
            ''', (
                payload['generated_at'], 'LK-APPROVAL-GMC-GATE-20260515', 'A3',
                'preview_only_needs_explicit_approval_before_write', str(BRAIN_MD), learning,
            ))
        con.commit()
    finally:
        con.close()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    price = json.loads(PRICE_JSON.read_text())
    landing = json.loads(LANDING_JSON.read_text())

    price_rows = [r for r in price['rows'] if r.get('decision_state') == 'candidate_price_only_patch_to_shopify_current_price']
    # Hard gates: no promo/sale/compare_at, exact price-only issue, active product, suggested write only price.
    price_rows = [r for r in price_rows
                  if r.get('merchant_sale_price') is None
                  and r.get('shopify_compare_at_price') is None
                  and r.get('issue_codes') == ['price_updated']
                  and r.get('shopify_product_status') == 'active'
                  and (r.get('suggested_write') or {}).get('updateMask') == 'productAttributes.price']

    packet_a = []
    rollback_a = []
    for r in price_rows:
        before = {'amountMicros': micros(r.get('merchant_price')), 'currencyCode': 'BRL'} if r.get('merchant_price') else None
        after = {'amountMicros': micros(r.get('shopify_price')), 'currencyCode': 'BRL'}
        packet_a.append({
            'product_id': r['product_id'],
            'offerId': r.get('offerId'),
            'title': r.get('title'),
            'route': 'Merchant API ProductInputs v1 PATCH',
            'data_source': DATA_SOURCE,
            'updateMask': 'productAttributes.price',
            'current_merchant_price_brl': r.get('merchant_price'),
            'target_shopify_price_brl': r.get('shopify_price'),
            'target_amountMicros': after['amountMicros'],
            'currencyCode': 'BRL',
            'shopify_variant_id': r.get('shopify_variant_id'),
            'shopify_variant_sku': r.get('shopify_variant_sku'),
            'merchant_link': r.get('merchant_link'),
            'guardrails': 'price-only; no salePrice; no strikethrough; no Shopify write',
        })
        rollback_a.append({
            'product_id': r['product_id'],
            'rollback_route': 'Merchant API ProductInputs v1 PATCH',
            'rollback_updateMask': 'productAttributes.price',
            'previous_productAttributes.price': before,
            'target_productAttributes.price': after,
            'rollback_note': 'If post-check fails or price is wrong, patch back previous productAttributes.price; if ownership rejects, stop and review source/Google & YouTube sync.',
        })

    landing_rows = [r for r in landing['rows'] if r.get('classification') == 'shopify_not_public_stale_or_suppress_candidate']
    landing_rows = [r for r in landing_rows
                    if (r.get('shopify_admin') or {}).get('status') in {'DRAFT', 'ARCHIVED'}
                    and (r.get('public_get') or {}).get('status_code') == 404
                    and (r.get('public_product_js') or {}).get('status_code') == 404]
    packet_b = []
    rollback_b = []
    for r in landing_rows:
        mp = r.get('merchant_product') or {}
        sh = r.get('shopify_admin') or {}
        packet_b.append({
            'product_id': r['product_id'],
            'offerId': mp.get('offerId'),
            'title': mp.get('title') or r.get('status_title'),
            'route': 'Merchant Center suppress/delete candidate',
            'source': mp.get('source'),
            'shopify_status': sh.get('status'),
            'public_get_status': (r.get('public_get') or {}).get('status_code'),
            'public_js_status': (r.get('public_product_js') or {}).get('status_code'),
            'merchant_link': mp.get('link'),
            'shopify_admin_product_id': sh.get('legacyResourceId'),
            'guardrails': 'only DRAFT/ARCHIVED + public 404 + .js 404; do not publish Shopify; keep public OK rows out',
        })
        rollback_b.append({
            'product_id': r['product_id'],
            'merchant_product_snapshot': mp,
            'shopify_admin_snapshot': sh,
            'rollback_note': 'If deleted/suppressed incorrectly, re-add via original Google & YouTube/feed source or Merchant API using captured product snapshot; verify public Shopify state first.',
        })

    json_a = OUT_DIR / 'packet_a_price_only_42_preview.json'
    csv_a = OUT_DIR / 'packet_a_price_only_42_preview.csv'
    rb_a = OUT_DIR / 'packet_a_price_only_42_rollback_snapshot.json'
    json_b = OUT_DIR / 'packet_b_draft404_20_preview.json'
    csv_b = OUT_DIR / 'packet_b_draft404_20_preview.csv'
    rb_b = OUT_DIR / 'packet_b_draft404_20_rollback_snapshot.json'

    json_a.write_text(json.dumps(packet_a, ensure_ascii=False, indent=2) + '\n')
    rb_a.write_text(json.dumps(rollback_a, ensure_ascii=False, indent=2) + '\n')
    json_b.write_text(json.dumps(packet_b, ensure_ascii=False, indent=2) + '\n')
    rb_b.write_text(json.dumps(rollback_b, ensure_ascii=False, indent=2) + '\n')
    write_csv(csv_a, packet_a, ['product_id','offerId','title','current_merchant_price_brl','target_shopify_price_brl','target_amountMicros','currencyCode','shopify_variant_id','shopify_variant_sku','merchant_link','guardrails'])
    write_csv(csv_b, packet_b, ['product_id','offerId','title','source','shopify_status','public_get_status','public_js_status','merchant_link','shopify_admin_product_id','guardrails'])

    payload = {
        'generated_at': now(),
        'status': 'preview_only_needs_explicit_approval',
        'merchant_id': MERCHANT_ID,
        'data_source': DATA_SOURCE,
        'summary': {
            'packet_a_price_only_rows': len(packet_a),
            'packet_a_guardrails_pass': len(packet_a) == 42,
            'packet_b_draft404_rows': len(packet_b),
            'packet_b_guardrails_pass': len(packet_b) == 20,
            'merchant_writes_executed': 0,
            'shopify_writes_executed': 0,
        },
        'artifacts': {
            'packet_a_json': str(json_a),
            'packet_a_csv': str(csv_a),
            'packet_a_rollback': str(rb_a),
            'packet_b_json': str(json_b),
            'packet_b_csv': str(csv_b),
            'packet_b_rollback': str(rb_b),
            'briefing_md': str(BRAIN_MD),
        },
    }

    lines = [
        '# LK GMC — Approval packets A/B preview',
        '',
        f"Gerado em: `{payload['generated_at']}`",
        f"Status: `{payload['status']}`",
        '',
        '## Resultado',
        '',
        f"- Pacote A price-only: `{len(packet_a)}` IDs exatos.",
        f"- Pacote B DRAFT/404: `{len(packet_b)}` IDs exatos.",
        '- Writes executados: `0`.',
        '- Shopify/Merchant/feed/campanha/envio externo: `0`.',
        '',
        '## Pacote A — price-only micro-pilot',
        '',
        '- Escopo: `productAttributes.price` somente via Merchant API ProductInputs v1.',
        '- Exclui salePrice, strikethrough e qualquer item com `compare_at_price`.',
        '- Fonte alvo: preço atual Shopify no snapshot local/variant ID exato.',
        '- Rollback: patch de volta para preço Merchant capturado antes do write.',
        '- Pós-check exigido: Product API/statuses após delay; se não convergir, parar.',
        '',
        '### Amostra A',
    ]
    for r in packet_a[:10]:
        lines.append(f"- `{r['product_id']}` — R$ {r['current_merchant_price_brl']} → R$ {r['target_shopify_price_brl']} — {r['title']}")
    lines += [
        '',
        '## Pacote B — DRAFT/404 suppress/delete',
        '',
        '- Escopo: produtos `source=crawl`/Merchant com Shopify `DRAFT/ARCHIVED` e URL pública 404 + `.js` 404.',
        '- Exclui os 2 casos public 200/monitor.',
        '- Não publica Shopify automaticamente.',
        '- Rollback: snapshot do Merchant product + Shopify admin para recriar/reprocessar se necessário.',
        '',
        '### Amostra B',
    ]
    for r in packet_b[:10]:
        lines.append(f"- `{r['product_id']}` — Shopify {r['shopify_status']} / public {r['public_get_status']} / js {r['public_js_status']} — {r['title']}")
    lines += [
        '',
        '## Aprovação necessária para executar',
        '',
        'Escolher explicitamente uma destas opções:',
        '',
        '1. `aprovo GMC A 10 IDs price-only` — mais conservador.',
        '2. `aprovo GMC A 42 IDs price-only` — aplica todos os candidatos price-only.',
        '3. `aprovo GMC B 20 DRAFT/404 suppress/delete` — limpa landing errors DRAFT/404.',
        '',
        'Sem uma dessas frases, continuar só em preview/read-only.',
        '',
        '## Artefatos',
    ]
    for k, v in payload['artifacts'].items():
        lines.append(f"- {k}: `{v}`")
    lines += [
        '',
        '## Não executado',
        '',
        '- Merchant write',
        '- ProductInputs PATCH',
        '- Content API delete/upsert',
        '- Shopify write',
        '- feed fetch/upload',
        '- campanha/envio/contato externo',
    ]
    BRAIN_MD.write_text('\n'.join(lines) + '\n')
    log_decision(payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
