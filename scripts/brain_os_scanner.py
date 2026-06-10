#!/usr/bin/env python3
"""Brain OS scanner: local/read-only candidate discovery for canonical project hubs.

This script does not mutate the Brain. It scans markdown/json/text-like artifact paths,
computes project-sprawl signals, and writes a sanitized JSON report when requested.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

DEFAULT_ROOT = Path('/opt/data/hermes_bruno_ingest/hermes-brain')
TEXT_EXTS = {'.md', '.json', '.txt', '.yaml', '.yml', '.csv'}
EXCLUDE_PARTS = {'.git', '__pycache__'}

PROJECT_DEFS = [
    {
        'id': 'lk-growth-gmc-shopify-meta',
        'title': 'LK Growth / Shopify / GMC / Meta',
        'owner_area': 'areas/lk/sub-areas/growth',
        'suggested_hubs': [
            'areas/lk/sub-areas/growth/projetos/gmc-merchant-center',
            'areas/lk/sub-areas/growth/projetos/shopify-growth-os',
            'areas/lk/sub-areas/growth/projetos/meta-ads-performance',
        ],
        'terms': ['growth', 'gmc', 'merchant', 'shopify', 'meta', 'ads', 'facebook', 'instagram', 'klaviyo', 'cro'],
        'risk': 'high_external_write_risk',
        'wave': 1,
    },
    {
        'id': 'lk-stock-tiny-pos',
        'title': 'LK Estoque / Tiny / POS / Pronta Entrega',
        'owner_area': 'areas/lk/sub-areas/stock',
        'suggested_hubs': [
            'areas/lk/sub-areas/stock/projetos/tiny-estoque-source-of-truth',
            'areas/lk/sub-areas/stock/projetos/pronta-entrega-pos',
        ],
        'terms': ['tiny', 'estoque', 'stock', 'pos', 'pronta entrega', 'produto', 'shopify-stock'],
        'risk': 'source_of_truth_confusion',
        'wave': 1,
    },
    {
        'id': 'lkgoc-collection-optimizer',
        'title': 'LKGOC Collection Optimizer',
        'owner_area': 'areas/lk/sub-areas/collection-optimizer',
        'suggested_hubs': ['areas/lk/sub-areas/collection-optimizer/projetos/lkgoc-collection-optimizer'],
        'terms': ['collection optimizer', 'lkgoc', 'colecao', 'collection', 'scorecard', 'qa'],
        'risk': 'production_theme_or_shopify_write_risk',
        'wave': 1,
    },
    {
        'id': 'memory-os',
        'title': 'Hermes Memory OS',
        'owner_area': 'areas/operacoes',
        'suggested_hubs': ['areas/operacoes/projetos/memory-os'],
        'terms': ['memory os', 'memory-os', 'memoria', 'memory hygiene', 'auto-heal', 'context intelligence'],
        'risk': 'context_truth_and_runtime_claim_risk',
        'wave': 1,
    },

    {
        'id': 'lk-content-klaviyo-agent',
        'title': 'LK Content / Klaviyo Agent',
        'owner_area': 'areas/lk/sub-areas/content',
        'suggested_hubs': ['areas/lk/sub-areas/content/projetos/lk-content-klaviyo-agent'],
        'terms': ['lk content', 'klaviyo', 'newsletter', 'calendar', 'calendario editorial', 'brand guide', 'content guide', 'dashboard'],
        'risk': 'campaign_send_and_runtime_activation_risk',
        'wave': 2,
    },
    {
        'id': 'mission-control-mesa-coo',
        'title': 'Mission Control / Mesa COO',
        'owner_area': 'areas/operacoes',
        'suggested_hubs': ['areas/operacoes/projetos/mission-control', 'areas/operacoes/projetos/mesa-coo'],
        'terms': ['mission control', 'mesa coo', 'decision inbox', 'decisao', 'telegram ux'],
        'risk': 'approval_sequence_and_decision_state_risk',
        'wave': 2,
    },
    {
        'id': 'mordomo-os',
        'title': 'Mordomo OS',
        'owner_area': 'areas/operacoes',
        'suggested_hubs': ['areas/operacoes/projetos/mordomo-os'],
        'terms': ['mordomo', 'whatsapp', 'wacli', 'calendar', 'follow-up', 'followup'],
        'risk': 'personal_external_action_risk',
        'wave': 2,
    },
    {
        'id': 'zipper-email-crm-intake',
        'title': 'Zipper Email / CRM / Leads Intake',
        'owner_area': 'areas/zipper',
        'suggested_hubs': ['areas/zipper/projetos/email-crm-intake'],
        'terms': ['zipper', 'zpr', 'enquiry', 'crm', 'lead', 'email intake', 'vendas_tango'],
        'risk': 'commercial_reply_and_human_approval_risk',
        'wave': 2,
    },
    {
        'id': 'spiti-bridge-governance',
        'title': 'SPITI Bridge / Governance',
        'owner_area': 'areas/spiti',
        'suggested_hubs': ['areas/spiti/projetos/bridge-governance'],
        'terms': ['spiti', 'lance', 'leilao', 'leilão', 'pregao', 'pregão', 'spiti-hub'],
        'risk': 'auction_bid_source_of_truth_risk',
        'wave': 3,
    },
    {
        'id': 'lk-shopify-product-upload-bot',
        'title': 'LK Shopify Product Upload / Bot',
        'owner_area': 'areas/lk/sub-areas/shopify',
        'suggested_hubs': ['areas/lk/sub-areas/shopify/projetos/product-upload-bot'],
        'terms': ['product upload', 'cadastro produto', 'shopify product', 'variant', 'metafield', 'product-upload'],
        'risk': 'shopify_product_write_risk',
        'wave': 3,
    },
    {
        'id': 'meta-ads-performance',
        'title': 'Meta Ads Performance',
        'owner_area': 'areas/lk/sub-areas/trafego-pago',
        'suggested_hubs': ['areas/lk/sub-areas/trafego-pago/projetos/meta-ads-performance'],
        'terms': ['meta ads', 'facebook ads', 'instagram ads', 'paid attribution', 'trafego pago', 'tráfego pago', 'roas'],
        'risk': 'ads_campaign_write_risk',
        'wave': 3,
    },
    {
        'id': 'theme-cro-performance',
        'title': 'Theme / CRO Performance',
        'owner_area': 'areas/lk/sub-areas/growth',
        'suggested_hubs': ['areas/lk/sub-areas/growth/projetos/theme-cro-performance'],
        'terms': ['theme', 'cro', 'conversion', 'pagespeed', 'core web vitals', 'pdp', 'dev theme'],
        'risk': 'theme_production_write_risk',
        'wave': 3,
    },
    {
        'id': 'executive-dashboards',
        'title': 'Executive Dashboards',
        'owner_area': 'areas/operacoes',
        'suggested_hubs': ['areas/operacoes/projetos/executive-dashboards'],
        'terms': ['dashboard', 'mission control', 'snapshot', 'cockpit', 'executive', 'painel'],
        'risk': 'snapshot_vs_live_state_risk',
        'wave': 3,
    },

    {
        'id': 'lk-crm-recovery-os',
        'title': 'LK CRM Recovery OS',
        'owner_area': 'areas/lk/sub-areas/crm',
        'suggested_hubs': ['areas/lk/sub-areas/crm/projetos/recovery-os'],
        'terms': ['checkout abandonado', 'carrinho abandonado', 'crisp', 'hugo', 'whatsapp', 'meta templates', 'klaviyo', 'rfm', 'cross-sell'],
        'risk': 'external_contact_and_crm_automation_risk',
        'wave': 4,
    },
    {
        'id': 'lk-trends-sourcing-intelligence',
        'title': 'LK Trends / Sourcing Intelligence',
        'owner_area': 'areas/lk/sub-areas/trends',
        'suggested_hubs': ['areas/lk/sub-areas/trends/projetos/sourcing-intelligence'],
        'terms': ['trends', 'tendencia', 'tendência', 'sourcing', 'droper', 'stockx', 'goat', 'fornecedor', 'compras'],
        'risk': 'purchase_negotiation_or_supplier_contact_risk',
        'wave': 4,
    },
    {
        'id': 'lk-ecommerce-orders-checkout',
        'title': 'LK E-commerce Orders / Checkout',
        'owner_area': 'areas/lk/sub-areas/ecommerce',
        'suggested_hubs': ['areas/lk/sub-areas/ecommerce/projetos/orders-checkout'],
        'terms': ['ecommerce', 'e-commerce', 'checkout', 'pedido', 'pedidos', 'frete', 'pagamento', 'catalogo', 'catálogo'],
        'risk': 'order_checkout_customer_promise_risk',
        'wave': 4,
    },
    {
        'id': 'lk-atendimento-chatwoot-elle',
        'title': 'LK Atendimento / Chatwoot / Elle',
        'owner_area': 'areas/lk/sub-areas/atendimento',
        'suggested_hubs': ['areas/lk/sub-areas/atendimento/projetos/chatwoot'],
        'terms': ['atendimento', 'chatwoot', 'elle', 'whatsapp', 'ops', 'loja', 'resposta', 'cliente'],
        'risk': 'customer_support_external_message_risk',
        'wave': 4,
    },

    {
        'id': 'lk-operating-system',
        'title': 'LK Operating System',
        'owner_area': 'areas/lk',
        'suggested_hubs': ['areas/lk/projetos/lk-operating-system'],
        'terms': ['lk operating system', 'lk-os', 'lk os', 'program to finish', 'implementation control', 'future configuration', 'gap audit'],
        'risk': 'cross_specialist_runtime_confusion_risk',
        'wave': 5,
    },
    {
        'id': 'lk-data-quality-layer',
        'title': 'LK Data Quality Layer',
        'owner_area': 'areas/lk',
        'suggested_hubs': ['areas/lk/projetos/data-quality-layer'],
        'terms': ['data quality', 'qualidade de dados', 'materialization', 'materialização', 'status audit', 'reconciliation', 'reconciliação'],
        'risk': 'stale_or_conflicting_source_of_truth_risk',
        'wave': 5,
    },
    {
        'id': 'lk-reporting-briefings',
        'title': 'LK Reporting / Briefings',
        'owner_area': 'areas/lk',
        'suggested_hubs': ['areas/lk/projetos/reporting-briefings'],
        'terms': ['daily sales', 'weekly', 'briefing', 'report', 'relatório', 'morning briefing', 'status surface'],
        'risk': 'telegram_noise_or_stale_report_risk',
        'wave': 5,
    },
    {
        'id': 'lk-approval-learning-ledger',
        'title': 'LK Approval / Learning Ledger',
        'owner_area': 'areas/lk',
        'suggested_hubs': ['areas/lk/projetos/approval-learning-ledger'],
        'terms': ['approval', 'aprovação', 'decision log', 'ledger', 'outcome', 'lesson', 'consequence tracker'],
        'risk': 'approval_history_misuse_or_ledger_manipulation_risk',
        'wave': 5,
    },

    {
        'id': 'lk-sourcing-procurement-os',
        'title': 'LK Sourcing / Procurement OS',
        'owner_area': 'areas/lk/sub-areas/stock',
        'suggested_hubs': ['areas/lk/sub-areas/stock/projetos/sourcing-procurement-os'],
        'terms': ['sourcing', 'compras', 'recompra', 'stockout', 'quote', 'cotação', 'fornecedor', 'supplier', 'mission-control-sourcing'],
        'risk': 'external_purchase_or_supplier_contact_without_approval_risk',
        'wave': 6,
    },
    {
        'id': 'lk-seo-cro-weekly-improvement',
        'title': 'LK SEO / CRO Weekly Improvement',
        'owner_area': 'areas/lk/sub-areas/growth',
        'suggested_hubs': ['areas/lk/sub-areas/growth/projetos/seo-cro-weekly-improvement'],
        'terms': ['seo cro', 'seo-cro', 'search console', 'seo fields', 'cro weekly', 'conversion preview', 'decision-grade'],
        'risk': 'preview_or_readonly_evidence_mistaken_for_production_change_risk',
        'wave': 6,
    },
    {
        'id': 'lk-rewards-loyalty-trust',
        'title': 'LK Rewards / Loyalty / Trust',
        'owner_area': 'areas/lk/sub-areas/growth',
        'suggested_hubs': ['areas/lk/sub-areas/growth/projetos/rewards-loyalty-trust'],
        'terms': ['rewards', 'loyalty', 'trust spine', 'rivo', 'judgeme', 'milestone', 'cashback'],
        'risk': 'customer_benefit_or_commercial_promise_without_policy_risk',
        'wave': 6,
    },
    {
        'id': 'lk-whatsapp-integration-platform',
        'title': 'LK WhatsApp Integration Platform',
        'owner_area': 'areas/lk/sub-areas/atendimento',
        'suggested_hubs': ['areas/lk/sub-areas/atendimento/projetos/whatsapp-integration-platform'],
        'terms': ['whatsapp hermes', 'wacli', 'openclaw', 'agent number', 'whatsapp integration', 'whatsapp notion', 'signal queue'],
        'risk': 'external_customer_or_supplier_message_without_approval_risk',
        'wave': 6,
    },

    {
        'id': 'collection-sort-automation',
        'title': 'LK Collection Sort Automation',
        'owner_area': 'areas/lk/sub-areas/collection-optimizer',
        'suggested_hubs': ['areas/lk/sub-areas/collection-optimizer/projetos/collection-sort-automation'],
        'terms': ['auto-sort', 'autosort', 'ruleb', 'rule b', 'manual collections', 'collection sorting', 'rollback-snapshot-pre-write'],
        'risk': 'shopify_collection_order_write_or_receipt_confusion_risk',
        'wave': 7,
    },
    {
        'id': 'catalog-badges-sync',
        'title': 'LK Catalog Badges Sync',
        'owner_area': 'areas/lk/sub-areas/shopify',
        'suggested_hubs': ['areas/lk/sub-areas/shopify/projetos/catalog-badges-sync'],
        'terms': ['catalog badges', 'badge sync', 'badges sync', 'catalog-badges-sync', 'tag new', 'snapshot-before'],
        'risk': 'shopify_badge_or_tag_write_without_current_source_risk',
        'wave': 7,
    },
    {
        'id': 'editorial-collection-guides',
        'title': 'LK Editorial Collection Guides',
        'owner_area': 'areas/lk/sub-areas/collection-optimizer',
        'suggested_hubs': ['areas/lk/sub-areas/collection-optimizer/projetos/editorial-collection-guides'],
        'terms': ['guia lk', 'collection guides', 'guias editoriais', 'source page', 'moon shoe', 'samba jane', '204l'],
        'risk': 'production_page_or_theme_publish_without_research_qa_approval_risk',
        'wave': 7,
    },
    {
        'id': 'source-pages-geo-experiments',
        'title': 'LK Source Pages / GEO Experiments',
        'owner_area': 'areas/lk/sub-areas/growth',
        'suggested_hubs': ['areas/lk/sub-areas/growth/projetos/source-pages-geo-experiments'],
        'terms': ['seo geo', 'geo source', 'source pages', 'comparison table', 'llms', 'ai search', 'experiment ledger'],
        'risk': 'seo_geo_experiment_mistaken_for_measured_production_gain_risk',
        'wave': 7,
    },

]


def iter_files(root: Path) -> Iterable[Path]:
    for dp, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_PARTS]
        p = Path(dp)
        for name in files:
            f = p / name
            if f.suffix.lower() in TEXT_EXTS:
                yield f


def safe_read(path: Path, max_bytes: int = 200_000) -> str:
    try:
        data = path.read_bytes()[:max_bytes]
        return data.decode('utf-8', errors='ignore').lower()
    except Exception:
        return ''


def count_owner_files(root: Path, rel: str) -> int:
    p = root / rel
    if not p.exists():
        return 0
    return sum(1 for f in p.rglob('*') if f.is_file())


def existing_hubs(root: Path, hubs: list[str]) -> list[str]:
    return [h for h in hubs if (root / h).exists()]


def scan(root: Path) -> dict:
    root = root.resolve()
    text_files = list(iter_files(root))
    rels = [str(p.relative_to(root)) for p in text_files]
    candidates = []
    for spec in PROJECT_DEFS:
        term_hits = 0
        file_hits = []
        term_re = re.compile('|'.join(re.escape(t.lower()) for t in spec['terms']))
        for p, rel in zip(text_files, rels):
            rel_l = rel.lower()
            path_match = any(t.lower().replace(' ', '-') in rel_l or t.lower() in rel_l for t in spec['terms'])
            content_match = False
            if path_match:
                content_match = True
            elif len(file_hits) < 250:
                content_match = bool(term_re.search(safe_read(p, 60_000)))
            if path_match or content_match:
                file_hits.append(rel)
                term_hits += 1
        owner_files = count_owner_files(root, spec['owner_area'])
        hubs_existing = existing_hubs(root, spec['suggested_hubs'])
        score = 0
        score += min(owner_files // 100, 40)
        score += min(term_hits // 25, 30)
        score += 15 if not hubs_existing else 5
        score += 10 if spec['risk'] else 0
        score += 5 if spec['wave'] == 1 else 0
        candidates.append({
            'id': spec['id'],
            'title': spec['title'],
            'owner_area': spec['owner_area'],
            'suggested_hubs': spec['suggested_hubs'],
            'existing_hubs': hubs_existing,
            'wave': spec['wave'],
            'risk': spec['risk'],
            'owner_file_count': owner_files,
            'term_hit_files': term_hits,
            'sample_artifacts': file_hits[:30],
            'score': score,
            'recommendation': 'canonical_hub_needed' if not hubs_existing or score >= 40 else 'monitor_or_refine_existing_hub',
        })
    candidates.sort(key=lambda x: (-x['wave'], -x['score']))
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'root': str(root),
        'mode': 'read_only_scan',
        'scanner_version': 'brain-os-v1',
        'total_text_files_scanned': len(text_files),
        'candidates': sorted(candidates, key=lambda x: (x['wave'], -x['score'])),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=str(DEFAULT_ROOT))
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--output')
    args = ap.parse_args()
    result = scan(Path(args.root))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + '\n', encoding='utf-8')
    if args.json or not args.output:
        print(text)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
