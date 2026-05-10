#!/usr/bin/env python3
"""LK weekly Meta creative asset audit (local preview only).

Read-only workflow:
- Reuses the weekly influencer Meta logic at ad level.
- Ranks top ads by canonical purchases/value/spend.
- Fetches real creative assets from Meta creative fields, video thumbnails and
  asset_feed_spec image hashes via /adimages.
- Downloads the best local image per ad and writes JSON + DesignMD LK HTML.

No e-mail send, no campaign edits, no Shopify/Tiny/Klaviyo/DB writes.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import importlib.util
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import parse_qs, urlparse

import requests

BASE = Path('/opt/data')
OUT_DIR = BASE / 'lk_weekly_creative_audits'
WEEKLY_SCRIPT = BASE / 'hermes_bruno_ingest' / 'scripts' / 'lk_weekly_influencer_sales_report.py'
BLOCKED_QUERY_KEYS = {'access_token', 'appsecret_proof', 'client_secret', 'token', 'key', 'secret', 'password'}
GRAPH = 'https://graph.facebook.com/v20.0/'
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}
CREATIVE_FIELDS = ','.join([
    'id', 'name', 'title', 'body', 'thumbnail_url', 'image_url', 'image_hash',
    'effective_object_story_id', 'object_story_id', 'instagram_permalink_url',
    'object_type', 'object_story_spec', 'asset_feed_spec', 'video_id', 'status',
])


def load_weekly_module():
    spec = importlib.util.spec_from_file_location('lk_weekly', WEEKLY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot import weekly script at {WEEKLY_SCRIPT}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def is_safe_url(raw: Any) -> bool:
    url = str(raw or '').strip()
    if not url.startswith('https://'):
        return False
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
    except Exception:
        return False
    return not any(k.lower() in BLOCKED_QUERY_KEYS or any(b in k.lower() for b in BLOCKED_QUERY_KEYS) for k in params)


def graph_get(token: str, path: str, params: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    p = dict(params)
    p['access_token'] = token
    r = requests.get(GRAPH + path, params=p, timeout=60)
    try:
        data = r.json()
    except Exception:
        data = {'raw': r.text[:400]}
    return r.status_code, data


def walk_urls(obj: Any, prefix: str = '') -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f'{prefix}.{k}' if prefix else k
            if isinstance(v, str) and v.startswith(('http://', 'https://')):
                out.append((p, v))
            else:
                out.extend(walk_urls(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.extend(walk_urls(v, f'{prefix}[{i}]'))
    return out


def jpeg_size(data: bytes) -> tuple[int, int] | None:
    if len(data) < 4 or data[:2] != b'\xff\xd8':
        return None
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        i += 2
        if marker in (0xD8, 0xD9):
            continue
        if i + 2 > len(data):
            return None
        seglen = int.from_bytes(data[i:i + 2], 'big')
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            if i + 7 > len(data):
                return None
            h = int.from_bytes(data[i + 3:i + 5], 'big')
            w = int.from_bytes(data[i + 5:i + 7], 'big')
            return w, h
        i += seglen
    return None


def png_size(data: bytes) -> tuple[int, int] | None:
    if data.startswith(b'\x89PNG\r\n\x1a\n') and len(data) >= 24:
        return int.from_bytes(data[16:20], 'big'), int.from_bytes(data[20:24], 'big')
    return None


def image_size(data: bytes) -> tuple[int, int] | None:
    return png_size(data) or jpeg_size(data)


def ext_for(content_type: str, data: bytes) -> str:
    ct = (content_type or '').lower()
    if 'png' in ct or data.startswith(b'\x89PNG'):
        return '.png'
    if 'webp' in ct or data.startswith(b'RIFF'):
        return '.webp'
    return '.jpg'


def collect_hashes(creative: dict[str, Any]) -> list[str]:
    hashes: list[str] = []
    if creative.get('image_hash'):
        hashes.append(str(creative['image_hash']))
    feed = creative.get('asset_feed_spec') or {}
    for item in feed.get('images') or []:
        if isinstance(item, dict) and item.get('hash'):
            hashes.append(str(item['hash']))
    seen: set[str] = set()
    return [h for h in hashes if not (h in seen or seen.add(h))]


def fetch_adimages(token: str, account_id: str, hashes: list[str]) -> list[dict[str, Any]]:
    if not hashes:
        return []
    status, data = graph_get(
        token,
        f'{account_id}/adimages',
        {'hashes': json.dumps(hashes), 'fields': 'hash,url,url_128,width,height,original_width,original_height,name,permalink_url'},
    )
    if status != 200:
        return []
    out: list[dict[str, Any]] = []
    for img in data.get('data') or []:
        if img.get('url') and is_safe_url(img.get('url')):
            out.append({'source': f'adimages.hash:{img.get("hash")}', 'url': img['url'], 'declared_size': [img.get('width'), img.get('height')]})
        if img.get('permalink_url') and is_safe_url(img.get('permalink_url')):
            out.append({'source': f'adimages.permalink:{img.get("hash")}', 'url': img['permalink_url'], 'declared_size': [img.get('width'), img.get('height')]})
    return out


def fetch_video_assets(token: str, video_id: str) -> list[dict[str, Any]]:
    if not video_id:
        return []
    status, data = graph_get(token, str(video_id), {'fields': 'id,thumbnails{uri,width,height,is_preferred},picture'})
    if status != 200:
        return []
    out: list[dict[str, Any]] = []
    for item in ((data.get('thumbnails') or {}).get('data') or []):
        if item.get('uri') and is_safe_url(item.get('uri')):
            out.append({'source': 'video.thumbnails', 'url': item['uri'], 'declared_size': [item.get('width'), item.get('height')]})
    if data.get('picture') and is_safe_url(data['picture']):
        out.append({'source': 'video.picture', 'url': data['picture'], 'declared_size': None})
    return out


def candidate_urls(token: str, account_id: str, creative: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for path, url in walk_urls(creative):
        if not is_safe_url(url):
            continue
        if 'instagram_permalink' in path or 'call_to_action' in path or 'website_url' in path:
            continue
        if any(marker in path for marker in ['image_url', 'thumbnail_url', 'video_data.image_url']):
            candidates.append({'source': path, 'url': url, 'declared_size': None})
    candidates.extend(fetch_adimages(token, account_id, collect_hashes(creative)))
    video_id = creative.get('video_id') or ((creative.get('object_story_spec') or {}).get('video_data') or {}).get('video_id')
    if video_id:
        candidates.extend(fetch_video_assets(token, str(video_id)))
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for c in candidates:
        u = c.get('url')
        if not u or u in seen:
            continue
        seen.add(u)
        deduped.append(c)
    return deduped


def image_luma_stats(path: Path) -> dict[str, Any]:
    """Decode a tiny RGB sample with ffmpeg to detect all-black frames.

    This avoids adding Pillow/pip to the runtime and keeps the workflow portable
    in the current Hermes container.
    """
    try:
        proc = subprocess.run(
            ['ffmpeg', '-v', 'error', '-i', str(path), '-vf', 'scale=32:32', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=20,
        )
        raw = proc.stdout
        if not raw:
            return {'decoded': False}
        pixels = [sum(raw[i:i + 3]) / 3 for i in range(0, len(raw), 3)]
        mean = sum(pixels) / len(pixels)
        var = sum((p - mean) ** 2 for p in pixels) / len(pixels)
        stdev = var ** 0.5
        # Detect vertical videos where the exported frame has black sidebars.
        width = 32
        rows = [pixels[i:i + width] for i in range(0, len(pixels), width)]
        left = [v for row in rows for v in row[:6]]
        right = [v for row in rows for v in row[-6:]]
        center = [v for row in rows for v in row[12:20]]
        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        center_mean = sum(center) / len(center)
        black = mean < 10 and stdev < 10
        side_black_bars = left_mean < 22 and right_mean < 22 and center_mean > 35
        return {
            'decoded': True,
            'mean_luma': round(mean, 2),
            'stdev_luma': round(stdev, 2),
            'edge_luma': [round(left_mean, 2), round(right_mean, 2)],
            'center_luma': round(center_mean, 2),
            'black_frame': black,
            'side_black_bars': side_black_bars,
        }
    except Exception as exc:
        return {'decoded': False, 'error': type(exc).__name__}


def download_image(url: str, ad_id: str, source: str, index: int, image_dir: Path) -> dict[str, Any]:
    try:
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        content_type = r.headers.get('content-type', '')
        data = r.content or b''
        if r.status_code != 200 or not content_type.lower().startswith('image/') or len(data) < 1000:
            return {'ok': False, 'status': r.status_code, 'content_type': content_type, 'bytes': len(data), 'source': source}
        size = image_size(data)
        sha = hashlib.sha256(data).hexdigest()[:16]
        ext = ext_for(content_type, data)
        safe_source = re.sub(r'[^a-zA-Z0-9_.-]+', '_', source)[:42]
        path = image_dir / f'{ad_id}_{index:02d}_{safe_source}_{sha}{ext}'
        path.write_bytes(data)
        quality = image_luma_stats(path)
        return {'ok': True, 'status': r.status_code, 'content_type': content_type, 'bytes': len(data), 'size': list(size) if size else None, 'path': str(path), 'sha16': sha, 'source': source, 'quality': quality}
    except Exception as exc:
        return {'ok': False, 'error': type(exc).__name__, 'source': source}


def center_crop_sidebars(asset: dict[str, Any]) -> dict[str, Any]:
    quality = asset.get('quality') or {}
    size = asset.get('size') or []
    path = Path(str(asset.get('path') or ''))
    if not quality.get('side_black_bars') or len(size) != 2 or not path.exists():
        return asset
    w, h = int(size[0]), int(size[1])
    if w < 480 or h < 800:
        return asset
    crop_w = max(2, int(w * 0.52) // 2 * 2)
    x = max(0, (w - crop_w) // 2)
    cropped = path.with_name(path.stem + '_center_crop' + path.suffix)
    try:
        subprocess.run(
            ['ffmpeg', '-v', 'error', '-y', '-i', str(path), '-vf', f'crop={crop_w}:{h}:{x}:0,scale={w}:{h}', str(cropped)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
        out = dict(asset)
        out['original_path'] = asset.get('path')
        out['path'] = str(cropped)
        out['source'] = str(asset.get('source') or '') + '.center_crop'
        out['quality'] = image_luma_stats(cropped) | {'cropped_sidebars': True}
        out['bytes'] = cropped.stat().st_size
        return out
    except Exception:
        return asset


def choose_asset(downloads: list[dict[str, Any]]) -> dict[str, Any] | None:
    good = [d for d in downloads if d.get('ok') and d.get('size')]
    # Hard-block unusable 64/128 thumbnails and all-black video frames unless
    # there is truly no alternative.
    non_tiny = [d for d in good if int(d['size'][0]) >= 480 and int(d['size'][1]) >= 480]
    non_black = [d for d in non_tiny if not ((d.get('quality') or {}).get('black_frame'))]
    pool = non_black or non_tiny or good
    if not pool:
        return None
    pool.sort(
        key=lambda d: (
            0 if ((d.get('quality') or {}).get('black_frame')) else 1,
            int(d['size'][0]) * int(d['size'][1]),
            int(d.get('bytes') or 0),
        ),
        reverse=True,
    )
    return center_crop_sidebars(pool[0])


def money(v: Any) -> str:
    return ('R$ {:,.2f}'.format(float(v or 0))).replace(',', 'X').replace('.', ',').replace('X', '.')


def render_html(rep: dict[str, Any], out_dir: Path) -> str:
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=DM+Sans:wght@400;500;700&display=swap');
    :root{--ink:#0A0A0A;--paper:#F0ECE8;--surface:#fff;--bone:#FDF9F5;--line:#E8E6E2;--muted:#827C75;--accent:#C8A98A;--serif:'Cormorant Garamond',Georgia,serif;--sans:'DM Sans',Arial,sans-serif}
    *{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans)}.page{max-width:1180px;margin:0 auto;background:var(--surface)}header{background:var(--ink);color:#fff;text-align:center;padding:32px}.brand{font:400 34px/1 var(--serif);letter-spacing:-.04em}.hero{background:var(--bone);text-align:center;padding:52px 28px;border-bottom:1px solid var(--line)}.eyebrow{font:700 10px/1.3 var(--sans);letter-spacing:.24em;color:var(--muted);text-transform:uppercase}.hero h1{font:400 56px/.95 var(--serif);letter-spacing:-.04em;margin:12px 0}.hero em{color:var(--accent);font-style:italic}.copy{max-width:780px;margin:0 auto;color:var(--muted);font:400 14px/1.7 var(--sans)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:22px;padding:30px}.card{border:1px solid var(--line);background:#fff}.image{background:#111;aspect-ratio:9/16;display:flex;align-items:center;justify-content:center;overflow:hidden}.image img{width:100%;height:100%;object-fit:contain;display:block}.fallback{padding:30px;color:#fff;text-align:center;font:400 13px/1.6 var(--sans)}.body{padding:16px}.inf{font:700 10px/1.2 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}.adname{font:400 25px/1 var(--serif);letter-spacing:-.025em;margin:8px 0}.meta{font:400 12px/1.65 var(--sans);color:var(--muted)}.pill{display:inline-block;margin-top:10px;border:1px solid var(--line);padding:8px 10px;font:700 9px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}.note{padding:0 30px 30px;color:var(--muted);font:400 12px/1.7 var(--sans)}
    """
    parts = [f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{css}</style></head><body><main class="page">']
    parts.append('<header><div class="brand">LK Sneakers</div></header>')
    parts.append('<section class="hero"><div class="eyebrow">CRIATIVOS META · ASSETS BAIXADOS · READ-ONLY</div><h1>Imagens reais dos<em> criativos.</em></h1>')
    parts.append(f'<p class="copy">Janela {html.escape(rep["period"]["start"])} a {html.escape(rep["period"]["end"])}. Assets baixados localmente via Meta creative/video/adimages; sem thumbnail 64×64 quando houver alternativa, sem envio externo e sem URLs com tokens/secrets.</p></section>')
    parts.append('<section class="grid">')
    for i, ad in enumerate(rep.get('ads') or [], 1):
        chosen = ad.get('chosen_asset')
        parts.append('<article class="card"><div class="image">')
        if chosen and chosen.get('path'):
            rel = os.path.relpath(chosen['path'], out_dir)
            parts.append(f'<img src="{html.escape(rel, quote=True)}" alt="Criativo Meta {html.escape(str(ad.get("ad_id") or ""))}">')
        else:
            parts.append('<div class="fallback">Sem asset local baixável com segurança neste ad.</div>')
        parts.append('</div><div class="body">')
        parts.append(f'<div class="inf">#{i:02d} · {html.escape(str(ad.get("influencer") or ""))}</div>')
        parts.append(f'<h2 class="adname">{html.escape(str(ad.get("ad_name") or ""))}</h2>')
        parts.append(f'<div class="meta">ad_id {html.escape(str(ad.get("ad_id") or ""))}<br>{float(ad.get("purchases") or 0):.0f} compras Meta · {money(ad.get("value"))} valor atribuído · {money(ad.get("spend"))} spend</div>')
        if chosen:
            sz = chosen.get('size') or ['', '']
            parts.append(f'<div class="pill">{html.escape(str(chosen.get("source") or ""))} · {sz[0]}×{sz[1]}</div>')
        parts.append('</div></article>')
    parts.append('</section>')
    parts.append('<p class="note">Guardrail: este HTML é uma ferramenta interna de curadoria. Agora ele tenta ativos reais de alta resolução antes de qualquer fallback pequeno. Antes de e-mail externo, manter QA visual e remover duplicados/frames ruins.</p>')
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
    account_id = secrets.get('META_AD_ACCOUNT_ID') or 'act_1242062509867163'
    if not token:
        raise RuntimeError('missing META_ACCESS_TOKEN')

    out_dir = Path(args.out_dir)
    image_dir = out_dir / 'images'
    image_dir.mkdir(parents=True, exist_ok=True)
    ads: List[Dict[str, Any]] = []
    for ad in (meta.get('top_creatives') or [])[:args.limit]:
        ad_id = str(ad.get('ad_id') or '')
        status, data = graph_get(token, ad_id, {'fields': f'id,name,creative{{{CREATIVE_FIELDS}}}'})
        creative = (data.get('creative') or {}) if status == 200 else {}
        candidates = candidate_urls(token, account_id, creative)
        downloads = []
        for idx, cand in enumerate(candidates[:24], 1):
            downloads.append(download_image(cand['url'], ad_id, cand['source'], idx, image_dir))
        chosen = choose_asset(downloads)
        item = dict(ad)
        item.update({
            'creative_id': creative.get('id'),
            'instagram_permalink_url': creative.get('instagram_permalink_url'),
            'creative_fetch_status': status,
            'candidate_count': len(candidates),
            'download_count': len(downloads),
            'download_ok_count': sum(1 for d in downloads if d.get('ok')),
            'chosen_asset': chosen,
            # Keep detailed local paths + dimensions, but never persist source URLs in JSON.
            'downloads': [{k: v for k, v in d.items() if k != 'url'} for d in downloads],
        })
        ads.append(item)

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
            'uses_thumbnail_url_as_primary': False,
            'stores_source_urls': False,
            'blocked_query_keys': sorted(BLOCKED_QUERY_KEYS),
        },
    }
    base = out_dir / f'lk-weekly-meta-creative-assets-{slug}'
    json_path = base.with_suffix('.json')
    html_path = base.with_suffix('.html')
    json_path.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding='utf-8')
    html_path.write_text(render_html(rep, out_dir), encoding='utf-8')
    with_assets = sum(1 for ad in ads if ad.get('chosen_asset'))
    min_sizes = [ad['chosen_asset']['size'] for ad in ads if ad.get('chosen_asset') and ad['chosen_asset'].get('size')]
    print(json.dumps({'ok': True, 'json': str(json_path), 'html': str(html_path), 'ads': len(ads), 'with_assets': with_assets, 'chosen_sizes': min_sizes}, ensure_ascii=False))


if __name__ == '__main__':
    main()
