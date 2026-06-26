# LK OS — Telegram Approval Surface Audit, 2026-05-12

Generated at: `2026-05-12T22:47:23.150744+00:00`

## Veredito

Auditoria local concluída para evitar o erro de pedir aprovação apenas por caminho de arquivo. Nada externo foi executado.

## Resumo inline

- Artefatos markdown escaneados: 178
- Já parecem OK para Telegram inline: 8
- P1 precisam de texto inline antes de qualquer aprovação: 50
- P2 revisar clareza inline: 54
- Supercedidos/não usar: 9

## P1 — não pedir aprovação sem reescrever inline no Telegram

- `reports/lk-daily-weekly-dry-run-validation-2026-05-11.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-daily-weekly-mandatory-report-delivery-2026-05-11.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-local-cd-pos-source-validation.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-local-cd-residual-tiny-probe.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-p1-attribute-completion-preview.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet-resume-status.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-p1-core-attributes-approval-packet-preview.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-p1-core-attributes-root-cause-probe.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-apply-final.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.
- `reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.md` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.

## Regra operacional aplicada

Sempre que houver aprovação: mandar no Telegram o texto exato, escopo, riscos, o que autoriza e o que não autoriza. Caminho de JSON/CSV/MD é só trilha de auditoria.

## Não executado

- external_send
- business_system_write
- tiny_call
- shopify_call
- merchant_call
- notion_or_n8n_change
- supplier_contact
