# LK WhatsApp — Resposta de estoque deve mencionar tamanho explicitamente

Data: 2026-05-21
Responsável: Hermes
Escopo: LK Sneakers / WhatsApp estoque

## Correção solicitada

Lucas corrigiu que a resposta de estoque não pode só falar produto/SKU; precisa falar o tamanho explicitamente.

## Causa

A resposta removia o tamanho do nome do produto via `product_base_name(...)` e mostrava apenas:

```text
Produto: Nome do produto (`SKU`).
```

Isso deixava a confirmação ambígua no WhatsApp, mesmo quando a consulta tinha sido feita por tamanho.

## Correção

A linha final de produto agora inclui o tamanho pedido/resolvido:

```text
Produto: Nome do produto — Tamanho: 36 (`SKU`).
```

## Validação

Caso validado ao vivo:

```text
Tem sim: 3 par(es) no LK | CONTROLE ESTOQUE.
Produto: Slide Nike Mind 001 Light Smoke Grey Cinza — Tamanho: 36 (`HQ4307-003-3`).
```

Também validado para item zerado:

```text
Produto: Tênis New Balance 204L Sea Salt Linen Bege — Tamanho: 35 (`U204L2SZ-35`).
```

Testes executados:

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`: OK
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`: OK / silent
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py --live-tiny --verbose`: OK
- `git diff --check` no Brain: OK

## Guardrail

Sem writes em Tiny/Shopify/estoque; apenas alteração de texto do responder e teste de regressão.
