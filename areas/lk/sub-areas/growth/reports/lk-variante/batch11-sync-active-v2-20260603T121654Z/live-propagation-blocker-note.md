# Batch 11 Curadoria LK — live propagation blocker note

- Timestamp UTC: 20260603T121926Z follow-up QA.
- Approval context: Lucas said `Seguir aprovado` after being told the 7 new handles needed a Production anti-cache correction.
- Writes executed under that scope:
  - touched `snippets/lk-variante-top30-visited.liquid` with no logic change;
  - touched `sections/lk-pdp.liquid` with no logic change;
  - root-cause found: `sections/lk-pdp.liquid` renders `snippets/lk-variante-top30-visited-v2.liquid`, so synced active v2 snippet from the canonical Batch 11 snippet.
- Readback:
  - active v2 before SHA12: `1fdaff0ba3db`;
  - active v2 after SHA12: `eda8d824a952`;
  - active v2 readback matched expected;
  - all 7 new handles are present in active v2 source.
- Live QA after sync remains intermittent/not stable:
  - some first-round hits rendered correctly, e.g. Birch Rust, Sea Salt Concrete, Black White;
  - later rounds mostly returned status 200 with no Curadoria section for the 7 new handles;
  - no Liquid errors were observed.
- Interpretation: Admin source/readback is correct, but public PDP HTML for the new handles is still stale/intermittent. Do not call all new Onitsuka/NB9060 fixed yet.
- Boundary: do not do product/metafield nudges or cloned-theme publish without separate explicit approval.
- Next safe options:
  1. passive monitor/retry later;
  2. ask Lucas for explicit product-level cache nudge approval for the 7 handles;
  3. if still blocked, prepare clone/force-fix approval packet per `lk-variante-force-fix-theme-clone-20260603.md`.
