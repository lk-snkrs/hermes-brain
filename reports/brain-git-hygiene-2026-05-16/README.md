# Brain Git Hygiene Proposal — 2026-05-16

Branch: `consolidation/brain-filesystem-git-hygiene-20260516`

## Summary

- Total changed/untracked entries: 750

## By status code

- `??`: 711
- `M`: 39

## By group

- `reports/artifacts`: 431
- `lk-operational-docs`: 148
- `brain-scripts`: 130
- `ops-hermes-docs-scripts`: 18
- `skills-mirror-updates`: 11
- `company-operating-docs`: 6
- `zipper-operational-docs`: 4
- `brain-root-docs`: 2

## By proposed action

- `candidate-keep-in-brain-consolidation`: 747
- `review-temp-script-before-commit`: 3

## By extension

- `.md`: 348
- `.json`: 204
- `.py`: 133
- `.csv`: 58
- `(none)`: 6
- `.jsonl`: 1

## Recommendation

- Do not push.
- Do not bulk-commit all entries blindly.
- First commit a small consolidation/report commit containing the reports generated in this pass.
- Then split the remaining Brain changes into topic commits: GMC/LK ops docs, scripts, skills, Zipper docs, root changelog/roadmap.
- Review `review-temp-script-before-commit` files before staging.
