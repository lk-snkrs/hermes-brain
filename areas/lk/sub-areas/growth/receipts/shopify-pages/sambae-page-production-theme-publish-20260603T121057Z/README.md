# Sambae — publish visual fix to Production theme

UTC: 2026-06-03T12:13:33.367132+00:00

## Approval
Lucas aprovou no Telegram: “Pode aprovar o que você fez do sambae no Production”.

## Escopo executado
- Tema production/main: `lk-new-theme/production` / `155065417950`.
- Asset alterado: `layout/theme.liquid`.
- Patch escopado somente para `.lk-source-page--sambae` e seção `.lk-press`.
- Conteúdo da página `/pages/guia-adidas-sambae` foi validado/readback; já estava publicado no Page Admin.

## Evidência Admin API
- PUT no production theme: `200`.
- Marker production no readback: `2`.
- Readback SHA256: `5e2ac9b5e394fb766fc6a9235a8019f8ada68a8b2ff38f23ee0ea0a399ce1d81`.
- Seção press no Page Admin: `True`.
- Cards press no Page Admin: `4`.
- Produtos na página: `6`.

## Evidência storefront production
- Status público: `200`.
- Marker production no HTML público: `2`.
- Seção press no HTML público: `1`.
- Cards press no HTML público: `4`.
- Regra mobile 2-colunas no HTML público: `3`.
- Screenshot mobile: `sambae-production-mobile-after.png`.

## Rollback
- Restaurar `production-theme-layout-theme.before.liquid` no asset `layout/theme.liquid` do tema `155065417950`.
- Conteúdo da página não foi alterado nesta publicação; snapshot salvo em `page.readback-admin.json`.
