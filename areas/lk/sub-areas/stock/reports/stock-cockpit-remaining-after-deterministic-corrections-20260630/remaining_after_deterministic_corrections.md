# Stock Cockpit — estado após correções determinísticas — 2026-06-30

- generated_at_utc: `2026-06-30T15:50:29.963016+00:00`
- values_printed: false

## Corrigido de verdade
- Shopify SKU-only writes verificados: **12**
  - primeiro lote: 3
  - lotes seguintes: 9

## Recomputado agora
- Missing116 Shopify gate atual:
  - `shopify_exact_sku_unique_preflight_needed`: 106
  - `shopify_exact_sku_duplicate`: 10
- Shopify duplicate deterministic write_ready após recompute: `0`
- Tiny preflight dos 8 recém-destravados:
  - `no_tiny_size_match_found`: 1
  - `ambiguous_or_no_safe_write_candidate`: 7
- Tiny write candidates current: `0`

## Restante bloqueado por decisão/identidade
- Tiny exact missing: 116 linhas ainda sem write determinístico de Tiny `codigo`.
- Tiny exact duplicate: 70 linhas ainda exigem deduplicação/mapeamento Tiny.

## Por que não fiz Tiny write
O wrapper governado existe, mas nenhum item tem target seguro `1 variação de tamanho + codigo vazio`. Escrever agora seria escolher cadastro/ID/código no escuro.

## Arquivos de decisão
- `remaining_missing116_after_deterministic_corrections.csv`
- `remaining_tiny_exact_duplicate70.csv`

## Não alterado
Tiny, Supabase, estoque/quantidade, preço, título, imagem, coleção e texto de produto não foram alterados nesta etapa.
