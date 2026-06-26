# REGRA — LKGOC standing approval para publish em DEV

Registrado em UTC: 2026-06-06 10:04:50Z
Origem: Lucas via Telegram no profile `lk-collection-optimizer`.

## Autorização

Lucas autorizou que, sempre que pedir para **refazer**, **fazer** ou equivalente em contexto de LKGOC, tema Shopify, guia, página editorial ou collection optimizer, o agente pode **publicar/aplicar no DEV** sem pedir nova aprovação intermediária.

## Escopo permitido sem nova aprovação

- Aplicar candidate em Shopify DEV/preview.
- Usar apenas tema com `role: unpublished` verificado por API/read-only antes do write.
- Fazer readback, QA técnico, QA visual desktop/mobile e gerar approval packet.
- Preparar rollback/receipt local do DEV.

## Fora do escopo / continua bloqueado

- Qualquer write em tema `main`/production.
- Merge/promoção DEV → Production.
- Alterações finais customer-facing em produção.
- Preço, estoque, desconto, checkout.
- Campanhas, Klaviyo, WhatsApp, e-mail, Merchant/feeds ou envios externos.

## Bloqueio automático

Se o tema alvo não tiver `role: unpublished`, abortar o write e avisar Lucas.
