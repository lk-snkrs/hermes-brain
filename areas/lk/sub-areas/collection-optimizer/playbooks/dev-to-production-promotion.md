# Playbook — DEV/Branch → Production Promotion

## Regra

Production theme nunca recebe write direto como padrão.

## Caminho aprovado

1. DEV/unpublished verificado por API ou branch técnico.
2. Diff/preview aprovado.
3. QA desktop/mobile/readback.
4. Approval Lucas para escopo exato.
5. GitHub PR/review quando o tema/repo fizer parte do fluxo.
6. Merge/deploy/promotion.
7. Readback production.
8. Receipt com snapshot, rollback, links e revisão D+7/D+14/D+30.

## Exceção

Hotfix direto em production só se Lucas disser explicitamente que autoriza hotfix direto em production e delimitar o escopo.
