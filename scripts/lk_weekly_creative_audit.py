#!/usr/bin/env python3
"""LK weekly Meta creative audit (local preview only).

Read-only workflow:
- Reuses the weekly influencer Meta logic at ad level.
- Ranks top ads by canonical purchases/value/spend.
- Fetches Meta ad preview iframe URLs for local visual QA.
- Writes JSON + DesignMD LK HTML locally.

No e-mail send, no campaign edits, no Shopify/Tiny/Klaviyo/DB writes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import importlib.util
import json
import re
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import parse_qs, urlparse

import requests

BASE = Path('/opt/data')
OUT_DIR = BASE / 'lk_weekly_creative_audits'
WEEKLY_SCRIPT = BASE / 'hermes_bruno_ingest' / 'scripts' / 'lk_weekly_influencer_sales_report.py'
PREVIEW_FORMATS = [
    'MOBILE_FEED_STANDARD',
    'INSTAGRAM_STANDARD',
    'INSTAGRAM_STORY',
    'FACEBOOK_STORY_MOBILE',
]
BLOCKED_QUERY_KEYS = {'access_token', 'appsecret_proof', 'client_secret', 'token', 'key', 'secret', 'password'}


def load_weekly_module():
    spec = importlib.util.spec_from_file_location('lk_weekly', WEEKLY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot import weekly script at {WEEKLY_SCRIPT}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def safe_preview_url(raw: Any) -> str | None:
    url = str(raw or '').strip()
    if not url.startswith('https://'):
        return None
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
    except Exception:
        return None
    if any(k.lower() in BLOCKED_QUERY_KEYS or any(b in k.lower() for b in BLOCKED_QUERY_KEYS) for k in params):
        return None
    if not (parsed.netloc.endswith('facebook.com') or parsed.netloc.endswith('facebook.net') or 'business.facebook.com' in parsed.netloc):
        return None
    return url


def extract_iframe_src(body: str) -> str | None:
    m = re.search(r'<iframe[^>]+src=["\']([^"\']+)["\']', body or '', flags=re.I)
    if not m:
        return None
    return html.unescape(m.group(1))


def fetch_previews(token: str, ad_id: str) -> list[dict[str, Any]]:
    previews = []
    for fmt in PREVIEW_FORMATS:
        try:
            r = requests.get(
                f'https://graph.facebook.com/v20.0/{ad_id}/previews',
                params={'access_token': token, 'ad_format': fmt},
                timeout=60,
            )
            item = {'format': fmt, 'http_status': r.status_code, 'iframe_url': None, 'usable': False}
            if r.status_code == 200:
                data = r.json().get('data') or []
                body = data[0].get('body') if data else ''
                iframe = safe_preview_url(extract_iframe_src(body or ''))
                item['iframe_url'] = iframe
                item['usable'] = bool(iframe)
            else:
                item['error'] = f'http_{r.status_code}'
            previews.append(item)
        except Exception as exc:
            previews.append({'format': fmt, 'http_status': None, 'iframe_url': None, 'usable': False, 'error': type(exc).__name__})
    return previews


def money(v: Any) -> str:
    return ('R$ {:,.2f}'.format(float(v or 0))).replace(',', 'X').replace('.', ',').replace('X', '.')


def render_html(rep: dict[str, Any]) -> str:
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500;700&display=swap');
    :root{--ink:#0A0A0A;--paper:#F0ECE8;--surface:#fff;--bone:#FDF9F5;--line:#E8E6E2;--muted:#827C75;--accent:#C8A98A;--serif:'Cormorant Garamond',Georgia,serif;--sans:'DM Sans',Arial,sans-serif}
    *{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans)}.page{max-width:1180px;margin:0 auto;background:var(--surface)}header{background:var(--ink);color:#fff;text-align:center;padding:32px}.brand{font:400 34px/1 var(--serif);letter-spacing:-.04em}.hero{background:var(--bone);text-align:center;padding:52px 28px;border-bottom:1px solid var(--line)}.eyebrow{font:700 10px/1.3 var(--sans);letter-spacing:.24em;color:var(--muted);text-transform:uppercase}.hero h1{font:400 54px/.95 var(--serif);letter-spacing:-.04em;margin:12px 0}.hero em{color:var(--accent);font-style:italic}.copy{max-width:760px;margin:0 auto;color:var(--muted);font:400 14px/1.7 var(--sans)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px;padding:30px}.card{border:1px solid var(--line);background:#fff;padding:18px}.rank{display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid var(--line);padding-bottom:12px}.num{background:var(--ink);color:#fff;width:38px;height:32px;display:flex;align-items:center;justify-content:center;font:700 10px/1 var(--sans);letter-spacing:.12em}.inf{font:700 10px/1.2 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}.adname{font:400 25px/1 var(--serif);letter-spacing:-.025em;margin:8px 0}.meta{font:400 12px/1.65 var(--sans);color:var(--muted)}.preview{margin-top:14px;background:#111;min-height:520px;display:flex;align-items:center;justify-content:center;overflow:hidden}.preview iframe{width:100%;height:620px;border:0;background:#111}.fallback{padding:24px;color:#fff;text-align:center;font:400 13px/1.6 var(--sans)}.pill{display:inline-block;margin-top:10px;border:1px solid var(--line);padding:8px 10px;font:700 9px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}.note{padding:0 30px 30px;color:var(--muted);font:400 12px/1.7 var(--sans)}
    """
    parts = [f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{css}</style></head><body><main class="page">']
    parts.append('<header><div class="brand">LK Sneakers</div></header>')
    parts.append('<section class="hero"><div class="eyebrow">AUDITORIA LOCAL · CRIATIVOS META · READ-ONLY</div><h1>Criativos em<em>veiculação.</em></h1>')
    parts.append(f'<p class="copy">Janela {html.escape(rep["period"]["start"])} a {html.escape(rep["period"]["end"])}. Esta prévia é local para curadoria: não usa thumbnail 64×64 no e-mail, não envia nada e bloqueia URLs com tokens/secrets.</p></section>')
    parts.append('<section class="grid">')
    for i, ad in enumerate(rep.get('ads') or [], 1):
        usable = [p for p in ad.get('previews') or [] if p.get('usable') and p.get('iframe_url')]
        chosen = usable[0] if usable else None
        parts.append('<article class="card">')
        parts.append('<div class="rank"><div>')
        parts.append(f'<div class="inf">{html.escape(str(ad.get("influencer") or ""))}</div>')
        parts.append(f'<h2 class="adname">{html.escape(str(ad.get("ad_name") or ""))}</h2>')
        parts.append(f'<div class="meta">ad_id {html.escape(str(ad.get("ad_id") or ""))}<br>{ad.get("purchases",0):.0f} compras Meta · {money(ad.get("value"))} valor atribuído · {money(ad.get("spend"))} spend</div>')
        parts.append('</div><div class="num">#%02d</div></div>' % i)
        parts.append('<div class="preview">')
        if chosen:
            parts.append(f'<iframe loading="lazy" src="{html.escape(chosen["iframe_url"], quote=True)}" title="Meta preview {html.escape(str(ad.get("ad_id") or ""))}"></iframe>')
        else:
            parts.append('<div class="fallback">Preview visual não carregou com segurança neste ad.<br>Manter fora do e-mail até asset nítido/validado pela Pareto/Maicon ou Page/IG.</div>')
        parts.append('</div>')
        parts.append(f'<div class="pill">iframe sem token: {len(usable)}/{len(ad.get("previews") or [])} · QA visual manual</div>')
        parts.append('</article>')
    parts.append('</section>')
    parts.append('<p class="note">Guardrail: este HTML é uma ferramenta interna de QA. Só promove criativo para e-mail/relatório executivo se o preview estiver nítido, sem overlay problemático e aprovado visualmente. Caso contrário, manter apenas ranking produto-first.</p>')
    parts.append('</main></body></html>')
    return '\n'.join(parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default=str(OUT_DIR))
    ap.add_argument('--limit', type=int, default=12)
    args = ap.parse_args()

    weekly = load_weekly_module()
    secrets = weekly.load_secrets()
    aliases = weekly.load_aliases()
    windows = weekly.date_windows()
    meta = weekly.fetch_meta(secrets, *windows['current'], aliases, include_creatives=False)
    token = secrets.get('META_ACCESS_TOKEN')
    if not token:
        raise RuntimeError('missing META_ACCESS_TOKEN')

    ads: List[Dict[str, Any]] = []
    for ad in (meta.get('top_creatives') or [])[:args.limit]:
        item = dict(ad)
        item['previews'] = fetch_previews(token, str(ad.get('ad_id') or ''))
        ads.append(item)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = windows['current'][1].date().isoformat()
    rep = {
        'generated_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'period': {'start': windows['current'][0].date().isoformat(), 'end': windows['current'][1].date().isoformat()},
        'meta_rows': meta.get('rows'),
        'match_source_counts': meta.get('match_source_counts'),
        'ads': ads,
        'guardrails': {
            'local_only': True,
            'email_send': False,
            'uses_thumbnail_url': False,
            'blocked_query_keys': sorted(BLOCKED_QUERY_KEYS),
        },
    }
    base = out_dir / f'lk-weekly-meta-creative-audit-{slug}'
    json_path = base.with_suffix('.json')
    html_path = base.with_suffix('.html')
    json_path.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding='utf-8')
    html_path.write_text(render_html(rep), encoding='utf-8')
    safe_previews = sum(1 for ad in ads for p in ad.get('previews', []) if p.get('usable'))
    print(json.dumps({'ok': True, 'json': str(json_path), 'html': str(html_path), 'ads': len(ads), 'safe_previews': safe_previews}, ensure_ascii=False))


if __name__ == '__main__':
    main()
