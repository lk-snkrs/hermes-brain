# LK Stock OS API Adapter — site do Júlio

Status: implementação local/read-only criada em 2026-06-12.

## Objetivo

Permitir que o site interno feito pelo Júlio consulte a **Stock OS DB canônica** em vez de usar uma database própria ou consultar Tiny direto.

## Arquivo canônico

- Script/API: `areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py`
- Pointer usado por padrão: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- DB usada: `artifacts.sqlite_db` dentro do pointer atual

## Rodar localmente

```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain
python3 areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py --serve --host 127.0.0.1 --port 8765
```

Opcional com token interno:

```bash
LK_STOCK_API_TOKEN='[REDACTED]' \
python3 areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py --serve --host 127.0.0.1 --port 8765
```

Quando `LK_STOCK_API_TOKEN` estiver definido, o site deve enviar:

```http
Authorization: Bearer [REDACTED]
```

## Endpoints

### Health

```http
GET /health
```

Retorna status do adapter, pointer, existência da DB e guardrails.

### Lookup

```http
GET /lookup?q=<SKU-ou-handle-ou-termo>&limit=10
GET /api/lk-stock/lookup?q=<SKU-ou-handle-ou-termo>&limit=10
```

## Contrato de resposta

Resposta confirmada:

```json
{
  "status": "confirmado",
  "source": "Stock OS DB",
  "freshness": "tiny_full_sync_nightly",
  "source_observed_at": "2026-06-12T06:20:21Z",
  "guardrails": {
    "tiny_write": 0,
    "shopify_write": 0,
    "writes_externos": 0,
    "public_availability_safe": 0,
    "availability_claim_allowed": 0
  },
  "results": [
    {
      "status": "confirmado",
      "sku": "ABC-40",
      "produto": "Tênis ABC",
      "tamanho": "40",
      "quantity_lk_controle_estoque": 2.0,
      "stock_source": "tiny_full_sync",
      "stock_freshness": "tiny_full_sync_nightly",
      "source_observed_at": "2026-06-12T06:20:21Z"
    }
  ]
}
```

Resposta não confirmada:

```json
{
  "status": "nao_confirmado",
  "source": "Stock OS DB",
  "motivo": "no_local_match",
  "results": [],
  "guardrails": {
    "tiny_write": 0,
    "shopify_write": 0,
    "writes_externos": 0,
    "public_availability_safe": 0,
    "availability_claim_allowed": 0
  }
}
```

## Regras obrigatórias para o site do Júlio

1. Não usar database própria para estoque.
2. Não consultar Tiny direto.
3. Não guardar token Tiny/Shopify no projeto do site.
4. Não transformar `nao_confirmado` em `sem estoque`.
5. Não mostrar promessa pública de pronta entrega.
6. Mostrar fonte/freshness quando exibir saldo interno.
7. Se `availability_claim_allowed=0`, o site não pode usar a resposta para promessa pública/cliente.

## Guardrails preservados

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Public availability: `0`
- Availability claim allowed: `0`

## Verificação

Comando unitário:

```bash
python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py -v
```

Comando de suíte stock:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Smoke CLI:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py CW1588601-4 --limit 1
```

Smoke HTTP:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py --serve --host 127.0.0.1 --port 8765
curl 'http://127.0.0.1:8765/health'
curl 'http://127.0.0.1:8765/lookup?q=CW1588601-4&limit=1'
```
