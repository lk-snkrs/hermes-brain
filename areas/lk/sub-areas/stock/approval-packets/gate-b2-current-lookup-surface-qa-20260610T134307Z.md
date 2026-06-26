# Gate B2 — current lookup surface QA

- ok: `True`
- pointer: `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`
- canonical_db: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- canonical_rows: `903`
- superseded_rows: `8`
- unique_skus: `903`
- handles: `558`

## Checks
- all_artifacts_exist: `True`
- canonical_rows_match_pointer: `True`
- superseded_rows_match_pointer: `True`
- unique_skus_match_pointer: `True`
- handles_match_pointer: `True`
- status_counts_match_pointer: `True`
- priority_counts_match_pointer: `True`
- guardrails_zero: `True`
- sample_has_all_statuses: `True`

## Guardrail sums
- tiny_write: `0`
- shopify_write: `0`
- writes_externos: `0`
- public_availability_safe: `0`

## Sample
- `CONSULTABLE_LOCAL_RESOLVED` / `P0_saneamento` / `CW1588601-4` / `nike-dunk-low-pink-red-white` / superseded `1`
- `CONSULTABLE_LOCAL_RESOLVED` / `P0_saneamento` / `IH2612-1` / `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` / superseded `0`
- `BLOCKED_TINY_DEPOSIT_MISSING` / `P1_saneamento` / `B75807-6` / `adidas-samba-og-black-gum` / superseded `0`
- `BLOCKED_TINY_DEPOSIT_MISSING` / `P1_saneamento` / `FD1437020-2` / `air-jordan-1-high-gs-palomino` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P0_saneamento` / `a0827u` / `slipper-alo-yoga-recovery-saddle-ivory-bege` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P0_saneamento` / `IH2612` / `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P1_saneamento` / `DD9335641` / `air-jordan-1-high-atmosphere` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P1_saneamento` / `FD1437020` / `air-jordan-1-high-gs-palomino` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P2_saneamento` / `NB-0058078` / `990v6-made-in-usa-triple-black` / superseded `0`
- `BLOCKED_TINY_MISSING` / `P2_saneamento` / `GX4634` / `adi2000-triple-black` / superseded `0`
- `BLOCKED_TINY_DUPLICATE` / `P0_saneamento` / `553560412-2` / `air-jordan-1-low-true-blue` / superseded `0`
- `BLOCKED_TINY_DUPLICATE` / `P0_saneamento` / `553560412-3` / `air-jordan-1-low-true-blue` / superseded `0`
- `BLOCKED_TINY_DUPLICATE` / `P1_saneamento` / `DD9335641-9` / `air-jordan-1-high-atmosphere` / superseded `0`
- `BLOCKED_TINY_DUPLICATE` / `P1_saneamento` / `DB4612300-7` / `air-jordan-1-high-lucky-green` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P0_saneamento` / `a0827u-1` / `slipper-alo-yoga-recovery-saddle-ivory-bege` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P0_saneamento` / `a0827u-10` / `slipper-alo-yoga-recovery-saddle-ivory-bege` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P1_saneamento` / `B75807` / `adidas-samba-og-black-gum` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P1_saneamento` / `JR4790-37` / `adidas-wmns-tokyo-mj-core-black-cream-white-gold-metallic` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P2_saneamento` / `HQ6638` / `adidas-campus-00s-kids-black-white-gum` / superseded `0`
- `BLOCKED_SHOPIFY_DUPLICATE` / `P2_saneamento` / `B75806` / `adidas-samba-og-white-black-gum` / superseded `0`
