# LK GMC — Checklist pendente UI Google & YouTube / Shopify

**Data:** 2026-05-14  
**Empresa:** LK Sneakers  
**Status:** `pending_ui_diagnostic`  
**Modo:** read-only/manual UI evidence  
**Autorizado por Lucas:** opção 1 — preparar checklist e deixar pendente; enviar por e-mail para lembrar.

## Objetivo

Coletar evidência visual/manual no Shopify Admin e Merchant Center sobre o sync do app **Google & YouTube** para entender por que preços corretos no Shopify continuam stale no Merchant, mesmo com produtos publicados no canal.

Este checklist **não autoriza resync, alteração de configuração, feed fetch, desligar automatic updates, editar preço, publicar/despublicar produto, alterar Merchant, Shopify, Tiny, campanhas ou data sources**.

## Estado atual resumido

- Canal Shopify **Google & YouTube** está ativo.
- Catálogo Google & YouTube está `ACTIVE`.
- 6/6 SKUs da amostra aparecem publicados no canal Google & YouTube.
- 5/6 SKUs ainda têm preço stale no Merchant vs Shopify Admin/PDP público.
- Merchant mostra `price_updated` / automatic price update como safety net.
- Feedback item-level do canal não está acessível pela API/token atual (`read_resource_feedbacks`/sales-channel scope ausente), então a próxima evidência precisa vir da UI.

## SKUs para checar primeiro

1. `01424-002-2`
   - Shopify esperado: `8999.99`
   - Merchant observado: `5999.90`
   - Issue: `price_updated`

2. `553558140-7`
   - Shopify esperado: `1799.99`
   - Merchant observado: `1499.99`
   - Issue: `price_updated`

3. `AQ9129-170-5`
   - Shopify esperado: `2749.99`
   - Merchant observado: `2599.99`
   - Issue: `price_updated`

4. `AQ9129-170-7`
   - Shopify esperado: `3349.99`
   - Merchant observado: `2599.99`
   - Issue: `price_updated`

5. `AQ9129-170-9`
   - Shopify esperado: `3349.99`
   - Merchant observado: `2599.99`
   - Issue: `price_updated`

6. `GW3773-39`
   - Shopify esperado: `3799.99`
   - Merchant observado: `3799.99`
   - Issue: `landing_page_error` / controle, não preço

## Checklist UI — Shopify Admin

### A. Canal Google & YouTube

Abrir Shopify Admin → Sales channels → **Google & YouTube**.

Coletar evidência:

- Print/status geral do canal.
- Última sincronização mostrada, se aparecer.
- Alertas, pendências, produtos rejeitados ou erros de feed.
- Qualquer fila tipo “pending”, “needs attention”, “not approved”, “processing”, “syncing”, “limited”, “disapproved”.
- Se houver contagem de produtos aprovados/rejeitados/pendentes, anotar.

Não clicar:

- Resync/reprocess/sync now.
- Reconnect account.
- Change settings.
- Edit shipping/tax/product settings.
- Update feed/fetch.

### B. Produto individual no Shopify

Para cada SKU da amostra, abrir o produto/variant no Shopify Admin e verificar:

- Produto está `Active`?
- Variant/SKU correto existe?
- Price atual confere com Shopify esperado?
- Compare-at-price existe? Se sim, qual valor?
- Produto está publicado no canal **Google & YouTube**?
- Há banner/alerta do Google no produto?
- Há item-level status, “view on Google”, “manage availability”, “not synced”, “not approved”, “needs attention”?
- Há timestamp de última atualização/sync do Google para o item?

Coletar:

- 1 print da tela de produto mostrando preço/SKU/status.
- 1 print/trecho da publicação no canal Google & YouTube.
- Texto exato de qualquer erro.

Não alterar:

- preço;
- compare-at price;
- publicação em canais;
- status active/draft;
- estoque;
- tags;
- metacampos;
- imagens;
- SEO;
- Google category/custom labels.

## Checklist UI — Google Merchant Center

Para cada item da amostra, buscar pelo SKU/offer ID.

Coletar:

- Item ID/offerId exato.
- Data source exibido na UI.
- Preço enviado vs preço automático/corrigido, se a UI mostrar ambos.
- Diagnóstico `price_updated` / automatic item updates.
- Aba/área de histórico, source, feed, processing ou “final attributes”, se disponível.
- Timestamp de última atualização/processamento.
- Qualquer conflito entre API principal, Autofeed/crawl e supplemental feed.

Não alterar:

- Automatic item updates.
- Data sources.
- Feed settings/fetch now.
- Item suppression/deletion.
- Price, sale_price ou attributes.
- Destinations/free listings/ads.

## Perguntas que a UI precisa responder

1. O Google & YouTube mostra erro/pending/review para estes produtos?
2. Existe timestamp indicando que o canal não sincroniza desde antes da mudança de preço?
3. O Merchant atribui o preço stale à fonte API principal ou ao Autofeed/crawl?
4. `compare_at_price`/promoção no Shopify está gerando `sale_price` ou strikethrough inesperado?
5. Existe botão ou ação de resync específica por produto? Se sim, **não clicar**; apenas documentar.
6. Há discrepância entre preço final, preço enviado e preço auto-atualizado?

## Resultado esperado do diagnóstico

Classificar cada SKU em um destes buckets:

- `ui_channel_error_visible`: Shopify Google & YouTube mostra erro claro.
- `ui_channel_pending_or_lag`: produto publicado, mas pendente/processando/sem sync recente.
- `merchant_source_conflict_visible`: Merchant mostra conflito entre API/Autofeed/crawl.
- `compare_at_or_sale_price_conflict`: compare-at/sale price explica divergência.
- `no_ui_evidence_found`: UI não mostra causa; requer escopo/API adicional ou suporte Google/Shopify.

## Próximo gate após checklist

Depois de coletar as evidências, preparar um pacote separado com uma das opções:

1. **Resync piloto de 1 SKU** no Google & YouTube, se a UI mostrar ação segura e reversível.
2. **Ajuste de source ownership/data source** se a UI mostrar conflito claro.
3. **Solicitar escopo/API adicional** (`read_resource_feedbacks`) se o diagnóstico ficar bloqueado sem UI suficiente.
4. **Suporte Shopify/Google** com evidências anexas se for bug/lag de canal.

Qualquer uma dessas opções é nova ação e exige aprovação explícita de Lucas antes de clicar/escrever.

## Não tocado

- Shopify write.
- Google & YouTube settings.
- Botões de resync/reprocess.
- Merchant write.
- Data source update/delete.
- Automatic item updates.
- Feed fetch/upload.
- Tiny.
- Campanhas, ads, clientes ou envios.

## Referências internas

- `areas/lk/rotinas/gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.md`
- `reports/lk-gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.md`
