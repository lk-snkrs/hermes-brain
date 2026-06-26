# LK WhatsApp Hermes — stock match correction receipt

Generated at: `2026-05-21T00:04:13Z`

## Trigger

Lucas reported a false negative in the LK WhatsApp Hermes group responder:

```text
@Hermes tem o U204L2SZ tamanho 35?
Hermes: Não encontrei candidato no Tiny para U204L2SZ tamanho 35.
```

## Root cause

The responder searched Tiny using the base SKU token `U204L2SZ` first. Tiny returned zero results for the base token, while the actual child variation exists under the composed SKU `U204L2SZ-35`.

Observed read-only Tiny evidence:

- `produtos.pesquisa` for `U204L2SZ`: 0 candidates / Tiny status `Erro`.
- `produtos.pesquisa` for `U204L2SZ-35`: candidate found.
- Candidate: `1069547306`, `U204L2SZ-35`, `Tênis New Balance 204L Sea Salt Linen Bege - 35`.
- `produto.obter.estoque`: `LK | CONTROLE ESTOQUE = 0`, `saldo_total = 0`.

## Correction applied

File patched:

```text
/opt/data/scripts/lk_hermes_whatsapp_responder.py
```

Initial fix generated `<base-sku>-<size>`, but Lucas correctly challenged that this is only a heuristic: the final child SKU is not necessarily the size. Follow-up correction at `2026-05-21T00:14:14Z` changed the process to:

1. Parse SKU/model token + requested size.
2. Resolve actual size-aware child SKU through local catalog intelligence (`lk_product_variants`, matching `option1`/variant title/size), read-only.
3. Search Tiny using the resolved child SKU first.
4. Use `<base-sku>-<size>` only as a later fallback heuristic.
5. Then try the bare SKU/model token and natural-language fallback.

Examples verified:

- `U204L2SZ tamanho 35` → actual child SKU `U204L2SZ-35`.
- `DD1503118 tamanho 35` → actual child SKU `DD1503118-2`; this proves size 35 is **not** assumed to be suffix `-35`.

## Correct answer after fix

```text
Está zerado para esse item/tamanho.
Quer que anote para o Júlio comprar?
Produto: Tênis New Balance 204L Sea Salt Linen Bege (`U204L2SZ-35`).
```

## Verification

Commands/results:

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py`: OK.
- Direct parser regression: `U204L2SZ tamanho 35` includes actual resolved child SKU `U204L2SZ-35`: OK.
- Direct parser regression: `DD1503118 tamanho 35` includes actual resolved child SKU `DD1503118-2` before naive fallback `DD1503118-35`: OK.
- Live read-only Tiny regression via `answer_stock()`: no longer returns "Não encontrei candidato": OK.
- Live read-only Tiny regression for opaque suffix case: `DD1503118 tamanho 35` returns `Tênis Nike Dunk Low Rose Whisper Rosa` with SKU `DD1503118-2`, not wrong SKU `DD1503118-35`: OK.
- Live responder restarted via `/opt/data/scripts/lk_hermes_whatsapp_watchdog.sh`: new PID `793912`.

## Preventive guardrail

Created regression self-test:

```text
/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py
/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.sh
/opt/data/.hermes/scripts/lk_hermes_whatsapp_responder_selftest.sh
```

Created cron watchdog:

```text
job_id: a5d7a392eed9
name: LK WhatsApp Hermes responder regression watchdog
schedule: */30 * * * *
mode: no_agent / silent-OK
latest verification: 2026-05-21_00-16-06.md = silent empty output
```

The watchdog is silent when parser regression passes and alerts if this class of SKU+size matching breaks again.

## Boundaries

- No WhatsApp message was sent during this correction.
- No Tiny, Shopify, Notion, supplier, purchase, price, stock or customer-facing write was made.
- Only read-only Tiny checks plus local script/cron/receipt changes were performed.
