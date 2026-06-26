#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
INPUT = ROOT/'reports/lk-compras-unified-sourcing-payload-2026-05-14.json'
OUT_JSON = ROOT/'reports/lk-compras-unified-sourcing-notion-execution-2026-05-14.json'
OUT_MD = ROOT/'reports/lk-compras-unified-sourcing-notion-execution-2026-05-14.md'
NOTION_DB = '2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION = '2022-06-28'


def now():
    return datetime.now(timezone.utc).isoformat()


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def req_json(url: str, token: str, method='GET', payload: dict[str, Any] | None = None, attempts=5) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    for i in range(attempts):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', 'Bearer ' + token)
        req.add_header('Notion-Version', NOTION_VERSION)
        if data is not None:
            req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors='replace')
            if e.code not in {429, 500, 502, 503, 504} or i == attempts - 1:
                raise RuntimeError(f'notion_http_{e.code}: {body[:1000]}') from e
        time.sleep(min(30, 2 ** (i + 1)))
    raise RuntimeError('request_failed')


def parse_brl(text: str | None) -> float | None:
    if not text:
        return None
    m = re.search(r'R\$\s*([0-9\.]+,[0-9]{2})', text)
    if not m:
        return None
    return float(m.group(1).replace('.', '').replace(',', '.'))


def query_existing(token: str, title: str) -> list[dict[str, Any]]:
    payload = {'page_size': 5, 'filter': {'property': 'Nome', 'title': {'equals': title}}}
    return req_json(f'https://api.notion.com/v1/databases/{NOTION_DB}/query', token, method='POST', payload=payload).get('results', [])


def paragraph(text: str) -> dict[str, Any]:
    return {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': [{'text': {'content': text[:1900]}}]}}


def origin_for(card: dict[str, Any]) -> str:
    route = (card.get('Rota recomendada') or '').lower()
    if 'nacional/droper não recomendado' in route or 'sem opção nacional' in (card.get('Opção nacional/Droper') or '').lower():
        return 'Internacional'
    return 'Nacional'


def fornecedor_for(card: dict[str, Any]) -> str:
    route = card.get('Rota recomendada') or ''
    if 'não recomendado' in route or 'fora/importação' in route:
        return 'Droper benchmark / Importação a comparar'
    return 'Droper / Grupo nacional + comparação importação'


def create_page(token: str, card: dict[str, Any]) -> dict[str, Any]:
    title = card['Nome']
    option = card.get('Opção nacional/Droper') or ''
    link_match = re.search(r'https?://\S+', option)
    droper_cost = parse_brl(option)
    props: dict[str, Any] = {
        'Nome': {'title': [{'text': {'content': title}}]},
        'Status da Compra': {'status': {'name': 'Aguardando Aprovação'}},
        'Modelo': {'rich_text': [{'text': {'content': str(card.get('Modelo') or '')[:1800]}}]},
        'Tamanho': {'rich_text': [{'text': {'content': str(card.get('Tamanho') or '')}}]},
        'Fornecedor': {'rich_text': [{'text': {'content': fornecedor_for(card)[:1800]}}]},
        'Origem': {'select': {'name': origin_for(card)}},
        'Pedido # ID': {'rich_text': [{'text': {'content': str(card.get('Pedido # ID') or 'LK OS / sourcing econômico')[:1800]}}]},
        'Avisar Fornecedor': {'select': {'name': 'Não'}},
        'Programar Pagamento': {'select': {'name': 'Não'}},
    }
    if link_match:
        props['Link'] = {'url': link_match.group(0)}
    if droper_cost is not None:
        props['Custo'] = {'number': droper_cost}
    body = [
        'Fonte: derived_reconciliation LK OS — vendas 120d + Tiny zerado/baixo + sinal Droper/grupo + regra econômica Lucas 2026-05-14.',
        f"Prioridade: {card.get('Prioridade')} | Demanda 120d: {card.get('Demanda 120d unidades')} un | Preço médio vendido: {card.get('Preço médio vendido')}",
        f"SKU: {card.get('SKU')} | Modelo: {card.get('Modelo')} | Tam: {card.get('Tamanho')}",
        f"Opção nacional/Droper: {card.get('Opção nacional/Droper')}",
        f"Margem nacional pré-taxas: {card.get('Margem nacional pré-taxas')}",
        f"Rota recomendada: {card.get('Rota recomendada')}",
        'Lógica importação quando StockX/GOAT entrar: custo landed estimado = (preço_usd + custo_trazer_usd) × (dólar_atual × 1,05). Preço de venda ideal = custo landed × 2 (markup 2). Custo_trazer_usd padrão inicial: US$100 configurável.',
        'Guardrails: Júlio/humano confere preço atual, disponibilidade, tamanho, logística, prazo e decide. Hermes não comprou, não reservou, não contatou fornecedor, não mandou WhatsApp, não programou pagamento e não alterou Shopify/Tiny/Merchant.',
    ]
    payload = {'parent': {'database_id': NOTION_DB}, 'properties': props, 'children': [paragraph(x) for x in body]}
    return req_json('https://api.notion.com/v1/pages', token, method='POST', payload=payload)


def main():
    data = json.loads(INPUT.read_text())
    token = (load_doppler().get('NOTION_TOKEN_LK') or load_doppler().get('NOTION_API_KEY'))
    if not token:
        raise SystemExit('missing NOTION token')
    results = []
    for card in data['cards']:
        title = card['Nome']
        try:
            existing = query_existing(token, title)
            if existing:
                results.append({'title': title, 'status': 'skipped_existing', 'page_id': existing[0].get('id'), 'url': existing[0].get('url')})
            else:
                page = create_page(token, card)
                results.append({'title': title, 'status': 'created', 'page_id': page.get('id'), 'url': page.get('url')})
            time.sleep(0.40)
        except Exception as e:
            results.append({'title': title, 'status': 'error', 'error': str(e)[:1000]})
            break
    summary = {
        'status': 'completed' if len(results) == len(data['cards']) and all(r['status'] in {'created', 'skipped_existing'} for r in results) else 'partial_or_error',
        'generated_at': now(),
        'source': str(INPUT),
        'notion_database': '[LK] Encomenda',
        'notion_database_id': NOTION_DB,
        'cards_expected': len(data['cards']),
        'created': sum(r['status'] == 'created' for r in results),
        'skipped_existing': sum(r['status'] == 'skipped_existing' for r in results),
        'errors': sum(r['status'] == 'error' for r in results),
        'results': results,
        'not_performed': ['purchase', 'reservation', 'supplier_contact', 'whatsapp_send', 'payment_schedule', 'shopify_write', 'tiny_write', 'merchant_write'],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    md = [
        '# LK Compras — execução Notion payload unificado', '',
        f"- Status: `{summary['status']}`",
        f"- Cards esperados: {summary['cards_expected']}",
        f"- Criados: {summary['created']}",
        f"- Já existiam/idempotente: {summary['skipped_existing']}",
        f"- Erros: {summary['errors']}",
        '- Guardrails: cards criados como `Aguardando Aprovação`, `Avisar Fornecedor=Não`, `Programar Pagamento=Não`.',
        '- Não executado: compra, reserva, fornecedor, WhatsApp, pagamento, Shopify, Tiny, Merchant.', '',
        '## Cards',
    ]
    for r in results:
        md.append(f"- {r['status']}: {r['title']} ({r.get('url') or r.get('page_id') or r.get('error')})")
    OUT_MD.write_text('\n'.join(md) + '\n')
    print(json.dumps({k: summary[k] for k in ['status', 'cards_expected', 'created', 'skipped_existing', 'errors']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
