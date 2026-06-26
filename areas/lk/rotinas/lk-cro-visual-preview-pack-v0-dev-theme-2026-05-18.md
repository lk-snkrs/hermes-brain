# LK CRO Visual Preview Pack v0 — Dev Theme — 2026-05-18

Preparado após aprovação explícita de Lucas para branch/dev theme, sem produção.

## Entrega

- Repo: `lk-snkrs/lk-new-theme`
- Base: `dev`
- Branch: `cro/visual-preview-pack-v0-20260518`
- Commit: `92d6227 feat: add CRO visual preview pack v0`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/14
- Theme dev: `lk-new-theme/dev`, ID `155065450718`, role `unpublished`
- Asset: `sections/lk-collection.liquid`
- Backup/rollback: `/opt/data/hermes_bruno_ingest/shopify-theme-backups/lk-new-theme-dev-cro-visual-v0-20260518-152957/`

## Preview URLs

- https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718&cro=v0
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718&cro=v0
- https://lksneakers.com.br/collections/lululemon?preview_theme_id=155065450718&cro=v0

## Guardrails cumpridos

- 0 publish produção.
- 0 mudança de produto/preço/estoque/SEO/campanha/envio.
- 1 asset de dev theme alterado, após snapshot e readback.
- Theme validado antes do upload: nome `lk-new-theme/dev`, role `unpublished`.
- Readback Admin API confirmou SHA local = SHA remoto.

## Validação

- `git diff --check`: passou.
- Secret scan do diff: passou.
- `npx impeccable detect --fast --json sections/lk-collection.liquid`: `[]`.
- Browser preview nas 3 collections confirmou bloco CRO, shortcuts e sort comercial.
- Caveat: barra preta de preview Shopify pode cobrir parte do bloco; clicar em **Hide bar** na revisão.

## Próximo gate

Lucas revisa os links de preview. Merge/publish/produção continuam bloqueados até nova aprovação explícita.
