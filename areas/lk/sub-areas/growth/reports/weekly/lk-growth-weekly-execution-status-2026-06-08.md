# LK Growth Weekly — Execution Status Bundle — 2026-06-08

Generated: `2026-06-08T19:28:25.377944+00:00`

## Completed after PRD

### 1. GMC LIA linkTemplate repatch

- Approved by Lucas: yes
- GMC write: yes
- Shopify write: no
- Final scan pages: 23
- Final `mhlsf_full_missing_valid_link_template`: 0
- Receipt: `receipts/gmc/lia-link-template-repatch-162-20260608T/FINAL_SUCCESS.md`

### 2. GMC missing color micro-pilot preview

- Status: approval-ready / preview only
- Candidates: 50 high-confidence
- Packet: `approval-packets/gmc-missing-color-micro-pilot-20260608/APPROVAL_PACKET.md`
- Needs approval before write.

### 3. Onitsuka CTR/GEO packet

- Status: approval-ready / preview only
- Packet: `approval-packets/onitsuka-ctr-geo-20260608/APPROVAL_PACKET.md`
- Needs Shopify approval before applying title/meta/FAQ.

### 4. Nike Mind CRO/GEO packet

- Status: approval-ready / preview only
- Packet: `approval-packets/nike-mind-cro-geo-20260608/APPROVAL_PACKET.md`
- Note: `/collections/nike-mind` returned 404; confirm actual handle before collection write.
- Needs Shopify approval before applying PDP/collection changes.

### 5. New Balance 204L LKGOC handoff

- Status: handoff ready
- File: `handoffs/lkgoc-new-balance-204l-refresh-20260608.md`
- Needs LKGOC execution gate and DEV-first approval for any visual/theme work.

### 6. Klaviyo tracking diagnostic

- Status: completed read-only
- Report: `reports/measurement/klaviyo-tracking-diagnostic-20260608.md`
- Result: Klaviyo API accessible; ecommerce events are present and non-zero in last 28 days.
- Key counts approx:
  - Active on Site: 2,822
  - Viewed Product: 6,183
  - Added to Cart: 651
  - Started Checkout: 422
  - Placed Order: 348
  - Opened Email: 59,490
  - Clicked Email: 1,033

Interpretation: Weekly zeros were likely report/query/mapping issue, not missing tracking.

### 7. PageSpeed / CrUX recovery

- Status: completed read-only
- Report: `reports/pagespeed-crux/pagespeed-crux-recovery-20260608.md`
- Tooling: GOOGLE_API_KEY present; PSI/CrUX recovered after retry.

Mobile lab performance scores:
- home: performance `0.41`, field `AVERAGE`
- onitsuka_collection: performance `0.6`, field `FAST`
- new_balance_204l_collection: performance `0.69`, field `FAST`
- nike_mind_black_chrome_pdp: performance `0.47`, field `FAST`

## Open decisions for Lucas

### Decision A — Apply Onitsuka CTR/GEO

Approval wording:
`Aprovo aplicar Onitsuka CTR/GEO Packet 2026-06-08 na coleção alvo.`

### Decision B — Apply Nike Mind CRO/GEO

Approval wording:
`Aprovo aplicar Nike Mind CRO/GEO Packet 2026-06-08 nos PDPs/coleção definidos, com snapshot e rollback.`

### Decision C — Run GMC missing color micro-pilot

Approval wording:
`Aprovo micro-piloto GMC color 2026-06-08 nos candidatos do preview, com snapshot/readback/rollback.`

### Decision D — Start New Balance 204L LKGOC execution

Approval wording:
`Aprovo iniciar LKGOC New Balance 204L Refresh em DEV/preview, sem production publish.`

### Decision E — Open DEV PageSpeed audit

Approval wording:
`Aprovo auditoria DEV PageSpeed para home/PDP Nike Mind, sem production publish.`

## Recommendation

Próximo melhor passo: **GMC missing color micro-pilot** ou **Onitsuka CTR/GEO**.

- Se quiser reduzir reprovação/servibilidade: GMC color.
- Se quiser capturar demanda orgânica rápido: Onitsuka.
- Se quiser efeito estrutural/premium: LKGOC 204L em DEV.
