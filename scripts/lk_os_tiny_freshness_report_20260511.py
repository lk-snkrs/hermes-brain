#!/usr/bin/env python3
"""LK OS Tiny ERP freshness report, read-only.

Scope: monitor Tiny API availability, latency, and official stock-deposit visibility for
LK Operating System Data Spine. This script does not write to Tiny, Shopify, Supabase,
or any production system. Secrets are fetched in-process from Doppler and never printed.
"""
from __future__ import annotations

import base64
import json
import os
import pathlib
import statistics
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots')
PUBLIC_JSON = ROOT / 'reports/lk-os-tiny-freshness-report-2026-05-11.json'
PUBLIC_MD = ROOT / 'reports/lk-os-tiny-freshness-report-2026-05-11.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'
BRAND_QUERIES = ['Nike', 'Adidas', 'New Balance', 'Asics', 'Onitsuka', 'Jordan']


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request(
        'https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'
    )
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
    req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.load(resp)
            latency_ms = int((time.perf_counter() - started) * 1000)
            retorno = (body or {}).get('retorno') or {}
            return {
                'ok': True,
                'http_status': resp.status,
                'tiny_status': retorno.get('status'),
                'latency_ms': latency_ms,
                'body': body,
            }
    except urllib.error.HTTPError as exc:
        latency_ms = int((time.perf_counter() - started) * 1000)
        raw = exc.read().decode(errors='replace')
        return {
            'ok': False,
            'http_status': exc.code,
            'tiny_status': None,
            'latency_ms': latency_ms,
            'error': 'HTTPError',
            'message': raw[:300],
        }
    except Exception as exc:
        latency_ms = int((time.perf_counter() - started) * 1000)
        return {
            'ok': False,
            'http_status': None,
            'tiny_status': None,
            'latency_ms': latency_ms,
            'error': type(exc).__name__,
            'message': str(exc)[:300],
        }


def percentile(values: list[int], p: float) -> int | None:
    if not values:
        return None
    values_sorted = sorted(values)
    if len(values_sorted) == 1:
        return values_sorted[0]
    pos = (len(values_sorted) - 1) * p
    lower = int(pos)
    upper = min(lower + 1, len(values_sorted) - 1)
    weight = pos - lower
    return int(values_sorted[lower] * (1 - weight) + values_sorted[upper] * weight)


def collect_tiny_freshness(secrets: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('TINY_API_TOKEN') or ''
    if not token:
        return {
            'source': 'Tiny',
            'fact_label': 'fact_tiny_stock',
            'ok': False,
            'status': 'missing_credentials',
            'generated_at': now_utc(),
        }

    searches: list[dict[str, Any]] = []
    product_ids: list[str] = []
    raw_search_details: list[dict[str, Any]] = []

    for query in BRAND_QUERIES:
        time.sleep(1.25)  # Tiny v2 is sensitive to burst requests.
        res = tiny_call(token, 'produtos.pesquisa', {'pesquisa': query, 'pagina': 1})
        retorno = ((res.get('body') or {}).get('retorno') or {}) if res.get('body') else {}
        rows = retorno.get('produtos') or []
        search_row = {
            'query': query,
            'http_status': res.get('http_status'),
            'tiny_status': res.get('tiny_status'),
            'latency_ms': res.get('latency_ms'),
            'sample_count': len(rows),
            'ok': bool(res.get('ok') and res.get('tiny_status') == 'OK'),
        }
        searches.append(search_row)
        raw_search_details.append({'query': query, 'sample_count': len(rows)})
        for item in rows[:2]:
            pid = str(((item or {}).get('produto') or {}).get('id') or '')
            if pid and pid not in product_ids:
                product_ids.append(pid)

    stock_checks: list[dict[str, Any]] = []
    for pid in product_ids[:8]:
        time.sleep(1.25)
        st = tiny_call(token, 'produto.obter.estoque', {'id': pid})
        retorno = ((st.get('body') or {}).get('retorno') or {}) if st.get('body') else {}
        produto = retorno.get('produto') or {}
        deposits = []
        official_seen = False
        official_has_saldo = False
        for item in produto.get('depositos') or []:
            deposito = item.get('deposito') or {}
            name = deposito.get('nome')
            has_saldo = deposito.get('saldo') is not None
            if name == OFFICIAL_DEPOSIT:
                official_seen = True
                official_has_saldo = has_saldo
            deposits.append({
                'nome': name,
                'has_saldo': has_saldo,
                'desconsiderar': deposito.get('desconsiderar'),
            })
        stock_checks.append({
            'tiny_id': str(produto.get('id') or pid),
            'http_status': st.get('http_status'),
            'tiny_status': st.get('tiny_status'),
            'latency_ms': st.get('latency_ms'),
            'codigo_present': bool(produto.get('codigo')),
            'official_deposit_seen': official_seen,
            'official_deposit_has_saldo': official_has_saldo,
            'deposit_count': len(deposits),
            'depositos': deposits,
            'ok': bool(st.get('ok') and st.get('tiny_status') == 'OK' and official_seen),
        })

    latencies = [int(x['latency_ms']) for x in searches + stock_checks if x.get('latency_ms') is not None]
    search_ok = sum(1 for x in searches if x.get('ok'))
    stock_ok = sum(1 for x in stock_checks if x.get('ok'))
    official_seen = sum(1 for x in stock_checks if x.get('official_deposit_seen'))
    official_with_saldo = sum(1 for x in stock_checks if x.get('official_deposit_has_saldo'))
    error_count = len(searches) + len(stock_checks) - search_ok - stock_ok
    p95 = percentile(latencies, 0.95)
    median_ms = int(statistics.median(latencies)) if latencies else None

    status = 'green'
    reasons: list[str] = []
    if search_ok < len(searches):
        status = 'red'
        reasons.append('uma ou mais buscas Tiny falharam')
    if stock_checks and stock_ok < max(1, int(len(stock_checks) * 0.8)):
        status = 'red'
        reasons.append('menos de 80% dos checks de estoque viram o depósito oficial')
    if p95 is not None and p95 > 10000 and status != 'red':
        status = 'yellow'
        reasons.append('p95 de latência acima de 10s')
    if median_ms is not None and median_ms > 5000 and status == 'green':
        status = 'yellow'
        reasons.append('mediana de latência acima de 5s')
    if not reasons:
        reasons.append('API Tiny respondeu com depósito oficial visível na amostra')

    return {
        'source': 'Tiny',
        'fact_label': 'fact_tiny_stock',
        'generated_at': now_utc(),
        'ok': status in {'green', 'yellow'},
        'freshness_status': status,
        'status_reasons': reasons,
        'scope_note': 'Relatório read-only de saúde/latência da API Tiny v2; não prova estoque completo por catálogo.',
        'thresholds': {
            'green': 'todas as buscas OK, >=80% checks de estoque com depósito oficial, p95 <= 10s, mediana <= 5s',
            'yellow': 'API responde, mas latência elevada ou cobertura parcial não crítica',
            'red': 'falha de busca ou cobertura crítica do depósito oficial',
        },
        'latency': {
            'sample_count': len(latencies),
            'median_ms': median_ms,
            'p95_ms': p95,
            'max_ms': max(latencies) if latencies else None,
        },
        'coverage': {
            'searches_ok': search_ok,
            'searches_total': len(searches),
            'stock_checks_ok': stock_ok,
            'stock_checks_total': len(stock_checks),
            'official_deposit_seen': official_seen,
            'official_deposit_with_saldo': official_with_saldo,
            'error_count': error_count,
        },
        'searches': searches,
        'stock_checks': stock_checks,
        'private_debug_summary': raw_search_details,
    }


def sanitize_for_public(report: dict[str, Any]) -> dict[str, Any]:
    # Tiny product IDs and deposit names are operational, not PII; keep them. Strip any future risky fields defensively.
    blocked = {'token', 'api_key', 'authorization', 'email', 'phone', 'cpf', 'cnpj', 'address', 'customer'}

    def scrub(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: ('[REDACTED]' if any(b in key.lower() for b in blocked) else scrub(val)) for key, val in value.items()}
        if isinstance(value, list):
            return [scrub(item) for item in value]
        return value

    public = scrub(report)
    public.pop('private_debug_summary', None)
    return public


def write_outputs(report: dict[str, Any]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f"lk_os_tiny_freshness_report_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    private_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    os.chmod(private_path, 0o600)

    public = sanitize_for_public(report)
    PUBLIC_JSON.write_text(json.dumps(public, ensure_ascii=False, indent=2))

    cov = public.get('coverage') or {}
    lat = public.get('latency') or {}
    lines = [
        '# LK OS Tiny Freshness Report — 2026-05-11',
        '',
        f"Gerado em: `{public.get('generated_at')}`.",
        '',
        'Escopo: monitoramento read-only da disponibilidade, latência e cobertura do depósito oficial no Tiny ERP.',
        '',
        f"Arquivo privado auditável, fora do Git: `{private_path}`.",
        '',
        '## Veredito',
        '',
        f"- Fonte: `{public.get('source')}`",
        f"- Rótulo: `{public.get('fact_label')}`",
        f"- Status: `{public.get('freshness_status')}`",
        f"- OK operacional: `{'sim' if public.get('ok') else 'não'}`",
        '',
        '## Métricas',
        '',
        f"- Buscas OK: `{cov.get('searches_ok')}/{cov.get('searches_total')}`",
        f"- Checks de estoque OK: `{cov.get('stock_checks_ok')}/{cov.get('stock_checks_total')}`",
        f"- Depósito oficial visto: `{cov.get('official_deposit_seen')}/{cov.get('stock_checks_total')}`",
        f"- Depósito oficial com saldo retornado: `{cov.get('official_deposit_with_saldo')}/{cov.get('stock_checks_total')}`",
        f"- Erros: `{cov.get('error_count')}`",
        f"- Latência mediana: `{lat.get('median_ms')} ms`",
        f"- Latência p95: `{lat.get('p95_ms')} ms`",
        f"- Latência máxima: `{lat.get('max_ms')} ms`",
        '',
        '## Interpretação',
        '',
    ]
    for reason in public.get('status_reasons') or []:
        lines.append(f'- {reason}.')
    lines += [
        '',
        '## Amostra de buscas',
        '',
    ]
    for row in public.get('searches') or []:
        lines.append(f"- `{row.get('query')}`: status Tiny `{row.get('tiny_status')}`, amostra `{row.get('sample_count')}`, latência `{row.get('latency_ms')} ms`.")
    lines += [
        '',
        '## Limites da leitura',
        '',
        '- Este relatório mede saúde e latência da API Tiny, não auditoria completa de estoque por SKU.',
        '- A fonte da verdade de estoque continua sendo Tiny, depósito `LK | CONTROLE ESTOQUE`.',
        '- Qualquer correção de SKU, estoque, preço ou cadastro continua exigindo preview, backup/rollback e aprovação Lucas.',
        '',
        '## O que este script não fez',
        '',
        '- Não alterou Tiny, Shopify, Supabase, Klaviyo, Meta, Google, Metricool, Notion, n8n ou banco de produção.',
        '- Não enviou e-mail, WhatsApp, campanha ou mensagem externa.',
        '- Não exportou PII para o repositório.',
    ]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    secrets = load_secrets()
    report = collect_tiny_freshness(secrets)
    write_outputs(report)
    print(json.dumps({
        'status': report.get('freshness_status'),
        'ok': report.get('ok'),
        'latency': report.get('latency'),
        'coverage': report.get('coverage'),
        'public_json': str(PUBLIC_JSON),
        'public_md': str(PUBLIC_MD),
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
