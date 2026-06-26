#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,pathlib,urllib.parse
from collections import Counter,defaultdict
from datetime import datetime,timezone
from typing import Any
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
AUDIT=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
OUT=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.md'
TARGET_CODES={'price_updated','strikethrough_price_updated','restricted_gtin','reserved_gtin','missing_item_attribute_for_product_type','landing_page_error','image_single_color','image_link_broken','landing_page_pending_crawl'}

def load_audit():
    spec=importlib.util.spec_from_file_location('audit', AUDIT); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def issue_key(i): return str(i.get('code') or i.get('servability') or i.get('attributeName') or 'unknown_issue')
def main():
    audit=load_audit(); sec=audit.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=audit.google_access_token(audit.parse_service_account(sec))
    def list_all_retry(endpoint):
        import time
        last=None
        for i in range(5):
            try:
                return audit.list_all(endpoint, mid, token)
            except Exception as e:
                last=e
                time.sleep(min(60, 2**(i+1)))
        raise last
    statuses=list_all_retry('productstatuses'); products=list_all_retry('products'); pmap={p.get('id'):p for p in products}
    rows=[]; by=Counter(); by_product=defaultdict(list)
    for st in statuses:
        pid=st.get('productId')
        for issue in st.get('itemLevelIssues') or []:
            k=issue_key(issue)
            if k in TARGET_CODES:
                by[k]+=1; by_product[pid].append(issue)
    for pid,issues in sorted(by_product.items()):
        prod=pmap.get(pid) or {}
        rows.append({
            'product_id':pid,'offerId':prod.get('offerId') or (pid or '').split(':')[-1], 'title':prod.get('title') or next((s.get('title') for s in statuses if s.get('productId')==pid), None),
            'link':prod.get('link'), 'imageLink':prod.get('imageLink'), 'additionalImageLinks':prod.get('additionalImageLinks') or [],
            'price':prod.get('price'), 'salePrice':prod.get('salePrice'), 'availability':prod.get('availability'), 'gtin':prod.get('gtin'), 'brand':prod.get('brand'), 'condition':prod.get('condition'),
            'googleProductCategory':prod.get('googleProductCategory'), 'productTypes':prod.get('productTypes'), 'color':prod.get('color'), 'sizes':prod.get('sizes'), 'ageGroup':prod.get('ageGroup'), 'gender':prod.get('gender'),
            'issues':[{'code':issue_key(i),'attributeName':i.get('attributeName'), 'severity':i.get('severity'), 'resolution':i.get('resolution'), 'destination':i.get('destination'), 'detail':str(i.get('detail') or '')[:500]} for i in issues]
        })
    payload={'generated_at':datetime.now(timezone.utc).isoformat(),'source_labels':['fact_merchant_center'],'summary':{'target_issue_instances':dict(by),'products_with_target_issues':len(rows),'productstatuses_read':len(statuses),'products_read':len(products)},'rows':rows,'not_performed':['merchant_write','shopify_write','tiny_write','feed_fetch','external_send']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC residual triage current — 2026-05-14','',f"Gerado em: `{payload['generated_at']}`",'', '## Summary']
    for k,v in by.most_common(): lines.append(f'- `{k}`: {v}')
    lines += ['', f"Produtos com alvo: {len(rows)}", '', '## Samples']
    for r in rows[:80]: lines.append(f"- `{r['product_id']}` — {', '.join(i['code'] for i in r['issues'])} — {r.get('title')}")
    MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({'summary':payload['summary'],'out':str(OUT),'md':str(MD)},ensure_ascii=False))
if __name__=='__main__': main()
