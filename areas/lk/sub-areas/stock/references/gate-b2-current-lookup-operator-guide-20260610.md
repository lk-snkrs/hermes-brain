# LK Stock — consulta local atual Gate B2

Gerado em: `20260610T131601Z`

## Uso padrão

Para perguntas internas do tipo “o que é esse SKU/handle?” use a entrada estável:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py <SKU-ou-handle> --limit 5 --history
```

Exemplos:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py CW1588601-4 --history
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py slipper-alo --limit 3
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py --show-pointer
```

## O que a consulta responde

- estado local canônico atual por `sku + handle`;
- `canonical_status` atual;
- tipo de issue atual;
- ação local recomendada;
- packet/artefato operacional relacionado;
- histórico superseded quando `--history` for usado.

## Fonte atual apontada

- Pointer: `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`
- DB canônico: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- CLI canônico timestampado: `areas/lk/sub-areas/stock/scripts/gate_b2_lookup_canonical_current.py`
- CLI estável: `areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py`

## Totais atuais

- Linhas canônicas: `903`
- Estados antigos superseded: `8`
- Linhas resolvidas localmente: `6`
- Disponibilidade pública liberada: `0`

## Guardrails

- Consulta local/cache only.
- Tiny write: `0`.
- Shopify write: `0`.
- Writes externos: `0`.
- Não afirma pronta entrega.
- Qualquer disponibilidade para cliente ou decisão operacional final exige consulta Tiny/fonte viva no momento.
