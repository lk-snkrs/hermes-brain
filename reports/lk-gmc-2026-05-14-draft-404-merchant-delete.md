# LK GMC — Delete/Suppress 12 Shopify DRAFT 404 items, 2026-05-14

Gerado em: `2026-05-14T15:10:58.492314+00:00`

## Resultado final
- Status final: `closed_verified_absent_by_direct_get`
- Escopo aprovado: opção 2 — remover/suprimir os 12 itens Merchant com landing page 404 porque Shopify está DRAFT.
- Deletes Content API OK: 12 / 12
- Verificação inicial: `productstatuses` já ausente para 12/12; `products.list` ainda tinha consistência eventual em 7/12.
- Verificação atrasada por GET exato: produtos presentes=0, statuses presentes=0.

## Itens removidos/suprimidos
- `online:pt:BR:15031239196158973196` — delete `ok` — Nike Air Force 1 07 White - Tamanho 45
- `online:pt:BR:9250025623243509812` — delete `ok` — Calça Saint Studio Wide Alfaiataria Risca de Giz Preta
- `online:pt:BR:13622509763707629816` — delete `ok` — Calça Saint Studio Wide Alfaiataria Risca de Giz Cinza
- `online:pt:BR:10591784840915585992` — delete `ok` — Boné Saint Studio Art Department Azul - LK
- `online:pt:BR:3876299146406606317` — delete `ok` — Calça Saint Studio Jeans Baggy Preta
- `online:pt:BR:10002025469927148791` — delete `ok` — Calça Nude Project Jeans Soft Velvet Azul Marinho
- `online:pt:BR:1624428988081867066` — delete `ok` — Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo | LK Sneaker
- `online:pt:BR:6562590402534581177` — delete `ok` — Calça Nude Project Illegal Jeans Ash Cinza - LK
- `online:pt:BR:2258634078163248862` — delete `ok` — Calça Chino Saint Studio Supima Preto
- `online:pt:BR:13498809788548851139` — delete `ok` — Moletom Essentials Fear of God Jet black SS24 Preto | LK Sneakers
- `online:pt:BR:4041641007094962608` — delete `ok` — Camisa Saint Studio Trico Palha | LK Sneakers
- `online:pt:BR:11314792792398542744` — delete `ok` — Moletom Oversized Nylon Fear of God Essentials Jet Black Preto

## Rollback
- Snapshot privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-draft-404-merchant-delete-rollback-20260514T150641Z.json`
- Para rollback, reinserir os recursos originais salvos no snapshot privado.

## Arquivos
- `reports/lk-gmc-2026-05-14-draft-404-merchant-delete.json`
- `reports/lk-gmc-2026-05-14-draft-404-merchant-delete.md`
- `reports/lk-gmc-2026-05-14-draft-404-merchant-delete-delayed-verify.json`

## Não executado
- Shopify publish/write
- Shopify redirect creation
- feed upload/fetchNow
- Tiny write
- price/availability/title/category changes
- campaign/message/WhatsApp/supplier contact
