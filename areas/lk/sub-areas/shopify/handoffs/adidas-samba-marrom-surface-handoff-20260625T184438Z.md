# Handoff — LK Shopify — Adidas Samba Marrom canonical collection

Data: 20260625T184438Z
Owner destino: `[LK] Shopify` / `lk-shopify`
Origem: `[LK] Growth`
Status: aprovado por Lucas para abrir handoff e despachar execução Shopify.

## Aprovação Lucas

> Aprovo abrir handoff para LK Shopify validar/criar/ativar a collection canônica Adidas Samba Marrom, preferencialmente /collections/adidas-samba-marrom, usando apenas produtos Adidas Samba marrom ativos já existentes, sem consultar ou alterar estoque, preço, campanhas, GMC, Klaviyo ou checkout, com preview/readback público; após a superfície 200 OK, Growth prepara guia/FAQ/schema em dev antes de qualquer produção.

## Objetivo

Validar/criar/ativar a collection canônica **Adidas Samba Marrom** para capturar demanda orgânica identificada no alerta SEMrush/DataForSEO.

URL preferida:
- `https://lksneakers.com.br/collections/adidas-samba-marrom`

## Evidência Growth

- Keyword SEMrush: `adidas samba marrom`
- Volume reportado: 3.600
- Alerta: queda forte/sem posição no monitoramento SEMrush
- SERP mobile BR/PT: intenção transacional forte, com Adidas oficial, Authentic Feet, Netshoes, Dafiti, Enjoei, NewSkull e Popular Products.
- Read-only Admin anterior: `collectionByHandle(adidas-samba-marrom)` retornou null.
- URL pública `/collections/adidas-samba-marrom` renderizava conteúdo geral de `adidas-samba`, não uma collection canônica real confirmada no Admin.

Produtos Adidas Samba marrom ativos detectados via Shopify Admin read-only Growth:
- `tenis-adidas-samba-og-shadow-brown-powder-yellow-marrom`
- `tenis-adidas-samba-lt-cow-print-brown-white-marrom`
- `tenis-adidas-samba-62-wild-brown-marrom`

Observação: havia também produtos Samba marrom ARCHIVED; não incluir produtos arquivados/inativos.

## Escopo permitido para LK Shopify

- Validar se já existe collection canônica equivalente com outro handle/título.
- Se não existir, criar/ativar collection canônica `Adidas Samba Marrom`, preferencialmente handle `adidas-samba-marrom`.
- Incluir **apenas produtos Adidas Samba marrom ativos já existentes**.
- Ajustar somente o necessário para a superfície canônica existir e responder 200 OK.
- Devolver evidências:
  - handle;
  - collection id / legacy id;
  - title;
  - URL pública 200 OK;
  - lógica de inclusão;
  - produtos incluídos por handle/título/status;
  - preview/readback público;
  - rollback plan;
  - receipt em `areas/lk/sub-areas/shopify/receipts/`.

## Fora de escopo / proibido

- Não consultar estoque, disponibilidade, grade, Tiny, Shopify inventory ou qualquer fonte de estoque.
- Não alterar estoque.
- Não alterar preço.
- Não alterar produtos fora da associação/validação da collection.
- Não alterar SEO title/meta sem aprovação separada.
- Não alterar descrição editorial sem aprovação separada, salvo mínimo técnico necessário para collection existir.
- Não alterar ordenação comercial sem aprovação separada.
- Não alterar GMC/feed.
- Não alterar campanhas.
- Não alterar Klaviyo/email/WhatsApp.
- Não alterar checkout.
- Não publicar guia/FAQ/schema Growth; Growth fará isso em dev depois que a superfície 200 OK existir.

## Próximo passo Growth após retorno Shopify

Quando LK Shopify retornar a superfície 200 OK com receipt, Growth deve preparar em dev theme `155065450718` o guia/FAQ/schema para `Adidas Samba Marrom`, com QA e novo approval packet antes de qualquer produção.
