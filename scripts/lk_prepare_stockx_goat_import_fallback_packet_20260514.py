#!/usr/bin/env python3
from __future__ import annotations
import json, math, pathlib
from datetime import datetime, timezone

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
INPUT = ROOT/'reports/lk-compras-unified-sourcing-payload-2026-05-14.json'
OUT_JSON = ROOT/'reports/lk-compras-stockx-goat-import-fallback-packet-2026-05-14.json'
OUT_MD = ROOT/'reports/lk-compras-stockx-goat-import-fallback-packet-2026-05-14.md'
FX_USD_BRL = 4.911381
FX_SOURCE = 'open.er-api.com latest/USD, time_last_update_utc=Thu, 14 May 2026 00:02:31 +0000'
FX_BUFFER = 1.05
MULTIPLIER = 2.0
CUSTO_TRAZER_USD_DEFAULT = 100.0
FACTOR = FX_USD_BRL * FX_BUFFER * MULTIPLIER


def brl(v):
    if v is None:
        return None
    s = f'R$ {v:,.2f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


def usd(v):
    if v is None:
        return None
    return f'US$ {v:,.2f}'


def parse_brl(s):
    if not s:
        return None
    import re
    m = re.search(r'R\$\s*([0-9\.]+,[0-9]{2})', str(s))
    if not m:
        return None
    return float(m.group(1).replace('.', '').replace(',', '.'))


def max_usd_for_sale(avg_sale, target_margin):
    # landed_cost <= avg_sale * (1-target_margin)
    max_landed = avg_sale * (1 - target_margin)
    return max_landed / FACTOR - CUSTO_TRAZER_USD_DEFAULT


def lookup_priority(card):
    route = (card.get('Rota recomendada') or '').lower()
    if 'não recomendado' in route or 'sem opção nacional' in (card.get('Opção nacional/Droper') or '').lower():
        return 'obrigatório antes de qualquer compra nacional'
    if 'borderline' in route:
        return 'comparar antes de comprar nacional'
    return 'opcional/sanity check; nacional parece viável'


def main():
    data = json.loads(INPUT.read_text())
    rows = []
    for c in data['cards']:
        sale = parse_brl(c.get('Preço médio vendido'))
        droper = parse_brl(c.get('Opção nacional/Droper'))
        max_30 = max_usd_for_sale(sale, 0.30) if sale else None
        max_20 = max_usd_for_sale(sale, 0.20) if sale else None
        max_0 = max_usd_for_sale(sale, 0.00) if sale else None
        route = lookup_priority(c)
        if max_30 is not None and max_30 < 0:
            verdict = 'importação inviável pela fórmula mesmo se sticker US$0 para meta 30%; precisa preço de venda maior ou pular'
        elif max_30 is not None and max_30 < 80:
            verdict = 'só comprar fora se aparecer preço excepcionalmente baixo'
        else:
            verdict = 'buscar StockX/GOAT e comparar landed cost'
        rows.append({
            'produto_lk': c.get('Modelo'),
            'sku': c.get('SKU'),
            'tamanho_lk': c.get('Tamanho'),
            'prioridade': c.get('Prioridade'),
            'demanda_120d': c.get('Demanda 120d unidades'),
            'avg_sale_price_brl': sale,
            'droper_benchmark_brl': droper,
            'national_route': c.get('Rota recomendada'),
            'lookup_priority': route,
            'import_formula': '(preco_usd + 100) × (4.911381 × 1.05) × 2',
            'factor_brl_per_usd_after_buffer_multiplier': FACTOR,
            'max_stockx_goat_sticker_usd_for_30pct_gross': max_30,
            'max_stockx_goat_sticker_usd_for_20pct_gross': max_20,
            'max_stockx_goat_sticker_usd_for_breakeven': max_0,
            'stockx_live_price': None,
            'goat_live_price': None,
            'live_lookup_status': 'not_completed_public_access_blocked_or_no_reliable_connector',
            'operator_instruction': 'Normalizar tamanho StockX/GOAT (US Men vs US Women/EU/BR) antes de preencher preço. Calcular custo final estimado e escolher menor fonte viável; se delta pequeno, preferir origem/logística mais segura/perto de SP.',
            'pre_lookup_verdict': verdict,
        })
    out = {
        'status': 'approval_packet_ready_import_lookup_not_executed_to_purchase',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source': str(INPUT),
        'fx': {'usd_brl': FX_USD_BRL, 'source': FX_SOURCE, 'buffer': FX_BUFFER, 'multiplier': MULTIPLIER, 'custo_trazer_usd_default': CUSTO_TRAZER_USD_DEFAULT},
        'formula': 'custo_final_estimado_brl = (preco_usd + custo_trazer_usd) × (dolar_atual × 1.05) × 2',
        'live_lookup_attempt_notes': [
            'StockX public search returned login gate in browser session.',
            'GOAT public search returned access denied/Cloudflare in browser session.',
            'Bing result snippets did not provide reliable exact-size marketplace prices for this packet.',
        ],
        'rows_count': len(rows),
        'rows': rows,
        'not_performed': ['marketplace_purchase', 'reservation', 'supplier_contact', 'whatsapp_send', 'notion_update_after_lookup', 'shopify_write', 'tiny_write'],
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    md = []
    md.append('# LK Compras — StockX/GOAT fallback/importação')
    md.append('')
    md.append(f"Status: `{out['status']}`")
    md.append('')
    md.append('## Fórmula LK usada')
    md.append('')
    md.append('`custo_final_estimado_brl = (preco_usd + custo_trazer_usd) × (dolar_atual × 1,05) × 2`')
    md.append('')
    md.append(f'- Dólar usado: {FX_USD_BRL} ({FX_SOURCE})')
    md.append(f'- Custo trazer padrão: {usd(CUSTO_TRAZER_USD_DEFAULT)} configurável')
    md.append(f'- Fator por US$ de sticker depois de buffer/multiplicador: {FACTOR:.4f} BRL')
    md.append('')
    md.append('## Observação de lookup')
    md.append('')
    md.append('- StockX/GOAT não entregaram preço público confiável nesta sessão sem login/bloqueio; portanto o pacote deixa os tetos de preço prontos para Júlio/Hermes preencher com fonte autenticada ou manual.')
    md.append('- Sem compra, reserva, contato, WhatsApp ou atualização de card após lookup.')
    md.append('')
    md.append('## Fila por produto/tamanho')
    for r in rows:
        md.append('')
        md.append(f"### {r['prioridade']} — {r['produto_lk']} — Tam {r['tamanho_lk']} — {r['sku']}")
        md.append(f"- Demanda 120d: {r['demanda_120d']} un")
        md.append(f"- Preço médio vendido: {brl(r['avg_sale_price_brl'])}")
        md.append(f"- Benchmark nacional/Droper: {brl(r['droper_benchmark_brl']) if r['droper_benchmark_brl'] is not None else 'sem match'}")
        md.append(f"- Rota nacional: {r['national_route']}")
        md.append(f"- Prioridade do lookup StockX/GOAT: {r['lookup_priority']}")
        md.append(f"- Teto sticker StockX/GOAT para 30% margem: {usd(r['max_stockx_goat_sticker_usd_for_30pct_gross'])}")
        md.append(f"- Teto sticker para 20% margem: {usd(r['max_stockx_goat_sticker_usd_for_20pct_gross'])}")
        md.append(f"- Breakeven sticker máximo: {usd(r['max_stockx_goat_sticker_usd_for_breakeven'])}")
        md.append(f"- Pré-veredito: {r['pre_lookup_verdict']}")
    OUT_MD.write_text('\n'.join(md) + '\n')
    print(json.dumps({'status': out['status'], 'rows_count': len(rows), 'fx_usd_brl': FX_USD_BRL}, ensure_ascii=False))

if __name__ == '__main__':
    main()
