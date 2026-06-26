# Root cause audit — Onitsuka Tiger vs 204L collection pattern

Date: 2026-05-28
Scope: LK collection pattern governance, New Balance 204L parity, Onitsuka Tiger Mexico 66 implementation.

## Question
Why did the Onitsuka Tiger Mexico 66 collection not get implemented exactly like the canonical New Balance 204L collection pattern?

## Finding
The failure was procedural and documentation-driven, not a lack of an existing standard.

The Brain had an anti-invention rule, but the main standards document presented Moon Shoe as the central editorial pattern while mentioning 204L as a collection reference only later. This made the rule too easy to interpret as “use 204L as inspiration for product-first collections” instead of “clone the 204L collection mold and only swap copy/assets/facts.”

## Live production comparison collected
Reference: `/collections/new-balance-204l`

- H1: 52px, inline-block, transparent background.
- Breadcrumb top: 140px.
- Collage top: 140.03px.
- Delta collage vs breadcrumbs: ~0px.
- Collage transform: `translateY(-123px)`.
- 204L preview padding-top: ~20px.
- 204L preview top: ~243px.
- 204L inner grid top: ~263px.
- Guide card: two columns.
- FAQ: grid-column `2 / 3`, grid-row `1 / span 2`, align-self start, margin/padding top 0, delta vs left title 0px.

Target: `/collections/onitsuka-tiger-mexico-66`

- H1: 52px, inline-block, transparent background.
- Breadcrumb top: 140px.
- Collage top: 176.42px.
- Delta collage vs breadcrumbs: +36.42px.
- Collage transform: `translateY(-123px)`.
- Onitsuka preview padding-top: 38.4px.
- Onitsuka preview top: 261.03px.
- Onitsuka inner grid top: 299.42px.
- Guide card/FAQ currently match the 204L two-column/FAQ alignment contract.

## Technical cause
The fix copied/extended the late 204L override for H1 and collage transform, but did not fully normalize the section pre-transform geometry.

Specifically, Onitsuka kept the generic `.lk-next-coll-preview` geometry:

- padding-top from `clamp(28px,3vw,42px)` → 38.4px at the tested viewport;
- block top/inner-grid top lower than 204L;
- same `translateY(-123px)` applied from a lower starting point.

Therefore, even with the same transform, the Onitsuka collage landed ~36px lower than 204L.

## Documentation cause
Before this audit, the standards doc said:

- central canonical visual/editorial pattern = Moon Shoe;
- 204L = visual reference “when applicable” for product-first collections.

That was ambiguous. For collection pages, 204L must be mandatory and exact, not optional/inspirational.

## Corrections applied to documentation/skill
- Updated `PADRAO-GUIAS-EDITORIAIS-LK.md` to declare two separate canonical molds:
  - product-first collection = New Balance 204L;
  - independent guide/source page = Moon Shoe.
- Updated `templates/brief-guia-editorial-colecao-lk.md` with separate checklists for 204L collections vs Moon Shoe guides.
- Updated skill `lk-collection-patterns` reference `collection-hero-204l-pattern-parity.md` with the missing rule: do not copy only `translateY`; validate/render the pre-transform geometry and padding/top offsets too.

## New non-negotiable rule
For every future LK product-first collection using the 204L mold, parity is only accepted after rendered DOM/computed CSS checks show:

- H1 ~52px desktop, inline-block, transparent background;
- collage top aligned to breadcrumb top, delta ~0px;
- target preview padding/top and inner top match 204L, or compensating offset is explicitly documented;
- after-grid guide uses off-white area, central white card, two-column desktop grid;
- FAQ top aligns to left title, delta ~0px;
- no production write without approval, backup, rollback and readback.

## Current status
Documentation corrected. Production visual still needs a scoped CSS adjustment if Lucas wants exact Onitsuka hero parity now; that write requires explicit approval because it changes live Shopify theme output.
