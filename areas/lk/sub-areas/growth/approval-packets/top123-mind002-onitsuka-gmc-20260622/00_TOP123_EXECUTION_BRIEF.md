# LK Top 1-2-3 Execution Brief — 2026-06-22

**Pedido Lucas:** seguir 1, 2 e 3.  
**Interpretação:** preparar execução dos próximos três blocos: Nike Mind 002, Onitsuka Tiger, GMC/Product Data.  
**Writes externos executados agora:** 0.  
**values_printed:** false.  
**Gerado:** 2026-06-22T17:50:07.989491+00:00

## Ordem recomendada

1. **Nike Mind 002:** read-only GSC/GA4 filtered + arquitetura do cluster Mind; não criar collection nova ainda porque `/collections/nike-mind-002` é 404 e os PDPs vivem em `/collections/nike-mind-001`.
2. **Onitsuka Tiger:** QA de duplicidade antes de aplicar packet de title/meta/description; a página já performa e não deve ser retrabalhada no escuro.
3. **GMC/Product Data:** current-state read-only + micro-piloto, separado do SEO; cuidado com Simprosys/overwrite e sem estoque direto.

## Entregáveis criados

- `01_NIKE_MIND_002_PACKET.md`
- `02_ONITSUKA_TIGER_PACKET_REFRESH.md`
- `03_GMC_PRODUCT_DATA_PACKET.md`

## Próxima ação que posso executar sem nova aprovação

- Rodar QA/read-only detalhado de Mind 002 + Onitsuka + GMC current-state.
- Preparar approval packet final para a primeira ação com write.

## O que ainda exige aprovação explícita

- qualquer Shopify production write;
- qualquer theme production write;
- qualquer GMC/feed/Simprosys write/reprocess;
- qualquer mudança em produto, preço, estoque, desconto, campanhas, Klaviyo/WhatsApp ou checkout.
