# Publish dev theme to production

UTC: 2026-06-03T12:24:59.613759+00:00

## Approval
Lucas aprovou no Telegram: “Publique o tema também”.

## Executado
- Tema publicado como main: `lk-new-theme/dev` / `155065450718`.
- Tema main anterior: `lk-new-theme/production` / `155065417950`.

## Verificação
- Novo main confirmado: `True`.
- Role do dev após publish: `main`.
- Role do tema anterior: `unpublished`.

## QA público Sambae
- URL: `https://lksneakers.com.br/pages/guia-adidas-sambae?lkqa=theme-published-20260603`
- Status: `200`
- Seção veículos: `1`
- Cards veículos: `4`

## Rollback
Para restaurar o tema anterior como production/main:
- `PUT /admin/api/2024-10/themes/155065417950.json` com `{"theme":{"id":155065417950,"role":"main"}}`

Backups de assets principais foram salvos neste receipt.
