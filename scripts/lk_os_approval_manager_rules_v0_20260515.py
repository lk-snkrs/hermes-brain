#!/usr/bin/env python3
"""Materialize LK OS Approval Manager + Learning Loop rules v0.

Local/reversible only. Writes a deterministic rules ledger to local SQLite and Brain reports.
No external sends, no Shopify/Tiny/Merchant/Meta/Klaviyo/WhatsApp/Gmail writes.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
BACKUP_DIR = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups')
REPORT_JSON = ROOT / 'reports/lk-os-approval-manager-rules-v0-2026-05-15.json'
REPORT_MD = ROOT / 'areas/lk/rotinas/lk-os-approval-manager-rules-v0-2026-05-15.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def rules(generated_at: str) -> list[dict]:
    base = {
        'business': 'LK Sneakers',
        'owner': 'Lucas/Hermes',
        'status': 'active',
        'last_updated_at': generated_at,
    }
    rows = [
        {
            'rule_id': 'LK-APPROVAL-EXTERNAL-SEND-DRAFT-ONLY-20260515',
            'domain': 'external_contact',
            'trigger': '/background, seguir, broad approval, client email, WhatsApp, supplier/customer/collector contact',
            'default_state': 'draft_only',
            'requires_approval': 1,
            'approval_contract': 'Current-turn explicit approval with named recipient + exact payload. Background/seguir never authorizes send.',
            'allowed_without_approval': json.dumps(['read_context', 'prepare_draft', 'prepare_disregard_draft', 'save_local_preview'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['gmail_send', 'whatsapp_send', 'newsletter_send', 'supplier_contact', 'customer_contact', 'disregard_or_correction_send'], ensure_ascii=False),
            'learning_action': 'Patch Google Workspace/Mordomo/email skills and record correction in global learning loop.',
            'example': 'Paulo/Zipper correction: should have generated draft, not sent email.',
        },
        {
            'rule_id': 'LK-APPROVAL-COMPRE-JA-VISUAL-BASELINE-20260515',
            'domain': 'theme_cro_visual',
            'trigger': 'Theme/CRO visual correction, PDP CTA, COMPRE JÁ button, visual parity complaint',
            'default_state': 'visual_preview_or_reversible_fix',
            'requires_approval': 1,
            'approval_contract': 'Visual/theme changes require preview or exact scoped approval; if correcting a regression to original, keep parity and verify live/readback.',
            'allowed_without_approval': json.dumps(['local_diff', 'screenshot/readback', 'reversible_low_risk_fix_if_already_approved_scope', 'document_baseline'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['new_redesign', 'broad_theme_refactor', 'checkout_change', 'publish_experiment', 'campaign_using_unapproved_visual'], ensure_ascii=False),
            'learning_action': 'When Lucas corrects visual details, record exact visual baseline and do not reinterpret correction as redesign.',
            'example': 'COMPRE JÁ returned to white background, light-gray border, no shadow/double stroke; preserve original visual parity.',
        },
        {
            'rule_id': 'LK-APPROVAL-CAMPAIGN-GATE-20260515',
            'domain': 'campaign_crm_paid',
            'trigger': 'Klaviyo, WhatsApp, Meta/Google campaign, creative, audience, budget, scheduling, flow activation',
            'default_state': 'preview_only',
            'requires_approval': 1,
            'approval_contract': 'Inline packet with audience, copy/creative, timing, budget/flow, expected action, rollback/stop plan; Lucas approval before send/activate/schedule.',
            'allowed_without_approval': json.dumps(['read_only_analysis', 'segment_preview_masked', 'draft_copy', 'dry_run', 'local_html_preview'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['send', 'schedule', 'activate_flow', 'change_budget', 'publish_creative', 'upload_customer_audience'], ensure_ascii=False),
            'learning_action': 'Campaign approvals must be payload-specific; approval of analysis does not approve delivery.',
            'example': 'Klaviyo/LK CRM can be draft/readiness only until Lucas approves send/schedule.',
        },
        {
            'rule_id': 'LK-APPROVAL-SOURCING-GATE-20260515',
            'domain': 'sourcing_purchase_supplier',
            'trigger': 'Sourcing opportunity, stockout/rebuy, Droper/StockX/GOAT/Kicks, supplier quote, purchase/repor estoque',
            'default_state': 'decision_preview_only',
            'requires_approval': 1,
            'approval_contract': 'Exact product/SKU/size, cost logic, price/margin, source, lead time, risk, and whether action is quote/contact/purchase. Lucas approval before external contact or purchase.',
            'allowed_without_approval': json.dumps(['read_only_market_lookup_on_demand', 'cost_model', 'ranking_preview', 'notion_card_preview', 'data_gap_resolution'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['supplier_contact', 'quote_request_send', 'purchase', 'reserve_stock', 'PO', 'price_promise_to_customer'], ensure_ascii=False),
            'learning_action': 'Use Júlio/LK routing and exact SKU/size economics; do not contact or buy from preview alone.',
            'example': 'Sourcing uses Droper, exact StockX/GOAT, import cost FX*1.05, ideal cost*2; action remains preview until approved.',
        },
        {
            'rule_id': 'LK-APPROVAL-GMC-GATE-20260515',
            'domain': 'gmc_merchant_feed',
            'trigger': 'Merchant Center/GMC attributes, price, availability, GTIN, crawl/API/source ownership',
            'default_state': 'read_only_or_preview',
            'requires_approval': 1,
            'approval_contract': 'Exact offer/product IDs, fields, source ownership, before snapshot/rollback, no bulk wildcard, post-apply verification. Price/source writes require special caution.',
            'allowed_without_approval': json.dumps(['diagnostic_read', 'dedup_preview', 'status_monitor', 'rollback_plan', 'local_report'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['Content API write', 'supplemental_feed_upload', 'fetchNow', 'price_patch', 'availability_patch', 'Shopify source mutation'], ensure_ascii=False),
            'learning_action': 'Separate GMC price/source governance from noncritical attrs; do not upsert crawl-sourced products or bulk retry price blindly.',
            'example': 'GMC residual/preço remains blocked until UI/manual Google & YouTube/Shopify/Merchant checklist and exact preview.',
        },
        {
            'rule_id': 'LK-APPROVAL-DATA-QUALITY-AUTONOMY-20260515',
            'domain': 'data_quality_local_readonly',
            'trigger': 'needs_data, SKU/Tiny mapping, local SQLite reconciliation, Mission Control state refresh',
            'default_state': 'autonomous_readonly_local',
            'requires_approval': 0,
            'approval_contract': 'Read-only/local/reversible data quality fixes may proceed; source-of-truth writes remain gated.',
            'allowed_without_approval': json.dumps(['read_shopify_snapshot', 'read_tiny_throttled', 'update_local_sqlite_derived_tables', 'write_brain_report', 'secret_scan'], ensure_ascii=False),
            'blocked_without_approval': json.dumps(['Shopify SKU change', 'Tiny write', 'inventory_change', 'price_change', 'external_send', 'cron_without_cadence_approval'], ensure_ascii=False),
            'learning_action': 'Do not pause on local/read-only needs_data; resolve and reclassify, but stop before external/source-of-truth write.',
            'example': 'Tiny stock snapshot and lk_variant_commercial_state can update locally; final commercial action waits for coverage/approval.',
        },
    ]
    return [{**base, **r} for r in rows]


def main() -> None:
    generated_at = now_iso()
    if not DB_PATH.exists():
        raise SystemExit(f'DB not found: {DB_PATH}')
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(BACKUP_DIR, 0o700)
    backup = BACKUP_DIR / f'lk_os_phase5_before_approval_manager_rules_v0_{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.sqlite'
    shutil.copy2(DB_PATH, backup)
    os.chmod(backup, 0o600)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.executescript('''
        create table if not exists lk_approval_manager_rules (
          rule_id text primary key,
          business text,
          domain text,
          trigger text,
          default_state text,
          requires_approval integer,
          approval_contract text,
          allowed_without_approval text,
          blocked_without_approval text,
          learning_action text,
          example text,
          owner text,
          status text,
          last_updated_at text
        );
    ''')
    rows = rules(generated_at)
    for r in rows:
        cur.execute('''insert or replace into lk_approval_manager_rules
            (rule_id,business,domain,trigger,default_state,requires_approval,approval_contract,allowed_without_approval,blocked_without_approval,learning_action,example,owner,status,last_updated_at)
            values (:rule_id,:business,:domain,:trigger,:default_state,:requires_approval,:approval_contract,:allowed_without_approval,:blocked_without_approval,:learning_action,:example,:owner,:status,:last_updated_at)''', r)
    con.commit()

    counts = {
        'rules_active': cur.execute("select count(*) from lk_approval_manager_rules where status='active'").fetchone()[0],
        'rules_requiring_approval': cur.execute("select count(*) from lk_approval_manager_rules where status='active' and requires_approval=1").fetchone()[0],
        'autonomous_readonly_rules': cur.execute("select count(*) from lk_approval_manager_rules where status='active' and requires_approval=0").fetchone()[0],
    }
    domains = dict(cur.execute("select domain, count(*) from lk_approval_manager_rules where status='active' group by domain order by domain").fetchall())
    payload = {
        'generated_at': generated_at,
        'status': 'active_local_rule_layer',
        'mode': 'local_sqlite_and_brain_rules_no_external_actions',
        'database': str(DB_PATH),
        'backup_before_local_write': str(backup),
        'summary': counts,
        'domains': domains,
        'rules': rows,
        'not_performed': ['email_send','whatsapp_send','campaign_send','shopify_write','tiny_write','merchant_write','meta_write','klaviyo_send_or_schedule','purchase','supplier_contact','cron_creation'],
    }
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK OS — Approval Manager Rules v0', '',
        f'Gerado em: `{generated_at}`',
        'Status: `active_local_rule_layer`', '',
        '## Veredito', '',
        'Materializei o Approval Manager em SQLite local e Brain: agora os gates principais do LK OS são regras consultáveis, não apenas texto solto.', '',
        '## Snapshot', '',
        f"- Regras ativas: `{counts['rules_active']}`",
        f"- Regras que exigem aprovação: `{counts['rules_requiring_approval']}`",
        f"- Regras autônomas read-only/local: `{counts['autonomous_readonly_rules']}`",
        f"- Backup local antes do write SQLite: `{backup}`", '',
        '## Regras vivas', '',
    ]
    for r in rows:
        lines += [
            f"### {r['rule_id']}", '',
            f"- Domínio: `{r['domain']}`",
            f"- Estado default: `{r['default_state']}`",
            f"- Exige aprovação: `{bool(r['requires_approval'])}`",
            f"- Contrato de aprovação: {r['approval_contract']}",
            f"- Exemplo: {r['example']}", '',
        ]
    lines += ['## O que não foi feito', '']
    for x in payload['not_performed']:
        lines.append(f'- {x}')
    REPORT_MD.write_text('\n'.join(lines) + '\n')

    marker = 'Approval Manager Rules v0 materializado em SQLite local'
    if CONTROL.exists():
        txt = CONTROL.read_text()
        if marker not in txt:
            CONTROL.write_text(txt.rstrip() + f"\n- [x] {marker} em 2026-05-15: tabela `lk_approval_manager_rules` com gates para envio externo, COMPRE JÁ/tema-CRO, campanhas, sourcing, GMC e data quality local. Artefato: `areas/lk/rotinas/lk-os-approval-manager-rules-v0-2026-05-15.md`.\n")

    print(json.dumps({'ok': True, 'summary': counts, 'domains': domains, 'report': str(REPORT_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
