# Mission Control — 12 improvements package — 2026-05-16

## User approval
Lucas asked: "Agora fazer os 12".

## Implemented safely now
1. P0 Git/PR local package — patch bundle generated; no push.
2. P0 Live ops-state data feed — JSON Brain mirror + generated TS module.
3. P0 Cron context_from — daily intelligence loop already chained to watchdog context.
4. P0 Approval buttons padrão — Mission Control shows inline A1-A4 button contract.
5. P1 Approval Ledger operacional — generated ledger by gate.
6. P1 Waiting Lucas real — generated decision queue.
7. P1 Skill drift watchdog — Mission Control watchdog validates Shopify skill runtime/Brain mirrors.
8. P1 Mordomo signal pruning — Mission Control marks Mordomo as actionable-only / silent OK.
9. P1 Shopify read-only intelligence — skill verified; findings remain read-only and become approval packets.
10. P2 Clickable approval backend — preview contract only; backend real remains locked.
11. P2 Public API/proxy — preview contract only; no new public proxy/API created.
12. P2 Kanban workers — executive lane/contract only; no worker daemon activated.

## Guardrail interpretation
The 12 are now represented and operationalized in Mission Control. P2 items were not turned into live backend/proxy/workers because that would be A3/security-sensitive; they are implemented as visible, locked command contracts requiring a separate plan + rollback before activation.

## QA
- `npm run lint` passed.
- `npm run build` passed.
- `mission_control_ops_watchdog.py` passed with silent OK.
- Public production URL returned HTTP 200.
- Browser rendered the new `12 melhorias` and `Command System` sections.
- Browser console: 0 messages/errors.
- Secret scan returned guardrail labels only, no credential values.
- Vercel env file removed after deploy.

## Deployment
- Published to `https://mission.lucascimino.com/?debug=12-improvements-20260516`.
- Vercel production alias confirmed: `https://mission.lucascimino.com`.

## Package
- Patch: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-12-improvements-20260516.patch`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-12-improvements-20260516-summary.md`

## Explicitly not executed
- No Git push/PR creation.
- No Docker/host/restart/gateway mutation.
- No Shopify/Tiny/Merchant write.
- No external WhatsApp/email/client send.
- No public API/proxy/backend action endpoint.
- No Kanban worker/daemon activation.
