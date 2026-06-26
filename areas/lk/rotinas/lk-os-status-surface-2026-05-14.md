# LK OS — Superfície padrão de status

Status: `active_status_surface_v1`
Data: 2026-05-14
Escopo: resposta curta para `Status Projeto LK OS`, `Seguir Projeto LK OS` e continuação operacional.
Modo: documentação/local/read-only. Nenhum write externo, marketplace, WhatsApp, Notion, Shopify, Tiny, Klaviyo, Meta, Google, cron ou infra foi executado.

## Objetivo

Padronizar a resposta executiva do Hermes quando Lucas pedir status ou continuidade do LK OS. A resposta deve mostrar estado, bloqueios, próximos passos e aprovações pendentes sem exigir que Lucas abra arquivos locais.

## Contrato de resposta curta

```text
Contexto: LK OS
Modo: [read-only/local | execução aprovada em andamento | approval-needed]
Status geral: [verde/amarelo/vermelho]

1. Agora
- [frente ativa principal]
- [progresso verificável]

2. Em paralelo seguro
- [artefatos/filas/PRD/Mission Control]

3. Bloqueado até aprovação ou condição
- [ação externa/write/marketplace/envio]

4. Próximo passo recomendado
- [uma ação clara]

Não executado
- [lista curta de não-ações relevantes]
```

## Estado atual para 2026-05-14

### Agora

- GMC P2A principal terminou e foi consolidado: 9.826 patches aplicados/verificados via Merchant `products.get`, 0 falhas de verificação.
- Readback final teve mismatch textual/semântico, não falha de PATCH: relatório `lk-gmc-2026-05-14-p2a-128-mismatch-readonly-review`/revisão posterior identificou principalmente localização de taxonomia (`Shoes` → `Vestuário e acessórios > Sapatos`), código numérico de Hats (`3515`) e bucket Bags.
- O residual verdadeiro de Bags foi tratado em point repair aprovado: 44 produtos patchados para `Apparel & Accessories > Handbags, Wallets & Cases`; 43 bateram exatamente e 1 ficou só com variação de `productTypes` (`Bolsa` vs `Bolsa/Carteira`).
- Execução A/B/C aprovada em 2026-05-14 fechou o escopo alvo: 15 cards Notion/Júlio criados, 12 IDs DRAFT/404 removidos do Merchant e 64 produtos corrigidos em atributos não críticos.
- Monitor pós-A/B/C read-only: 12/12 IDs removidos seguem ausentes por `products.get` + `productstatuses.get`; 64/64 IDs de atributos não têm mais diagnóstico alvo de `color/ageGroup/gender`.
- Residual GMC avançou após execução aprovada de preço/landing/imagem/GTIN online: triage lia 23.277 productstatuses; online GTIN estava fechado e os 34 GTINs restantes eram todos `local:LIA_*`.
- Execução local/LIA GTIN aprovada por Lucas (`segue o 2`) concluída: piloto 5 → escala 29 via Content API preservando recurso local e alterando só `gtin`; 34/34 IDs terminaram sem `reserved_gtin`/`restricted_gtin` no `productstatuses` final.
- Houve point repair em 4 IDs porque os primeiros GTINs candidatos ainda eram tratados como reservados; delayed reverify confirmou 4/4 readbacks corretos e 0 issue alvo nos 34.
- Estado prático: alvo GMC P2A + A/B/C + GTIN online + GTIN local/LIA está verde no escopo aplicado; próximos residuais relevantes viram gates separados (`price_updated`, `strikethrough_price_updated`, atributos/tipo de produto/imagens/landing pages).
- Triage read-only pós-GTIN executado em 23.277 `productstatuses`: residuais-alvo atuais são `price_updated` 924 instâncias, `strikethrough_price_updated` 240, `missing_item_attribute_for_product_type` 34, `image_single_color` 8, `image_link_broken` 3 e `landing_page_error` 3; GTIN alvo não reapareceu no triage.
- Preview de preço pós-GTIN gerou gate separado: 313 produtos online com issue de preço/strikethrough; 42 candidatos seguros para piloto `price`-only via Merchant API ProductInputs v1; 271 ficam em revisão separada por `salePrice`/compare-at/strikethrough para não mexer em preço riscado junto.
- Execução aprovada residual aplicou 182 ações iniciais: 17 atributos e 5 imagens online verificaram, 2 imagens local/LIA foram reparadas via Content API local, e 160 linhas de preço entraram em verificação.
- Recheck fresco dos 152 mismatches de preço separou: 43 já batiam com Shopify live e eram falso mismatch do executor anterior; 62 precisavam `price`, 42 precisavam `salePrice`, 5 precisavam limpar `salePrice` antigo.
- Foram tentados dois reparos seguros com rollback privado para preço (`ProductInputs v1` e depois `Content API` restrito a `source=api`), mas readback direto continuou sem persistir em 109 produtos. Diagnóstico read-only posterior em 152 produtos mostrou 108 `merchant_stale_vs_shopify_and_public` (Merchant/Content diverge tanto do Shopify Admin quanto do `/products/{handle}.js`) e 44 que já batiam com Shopify. Novo mapa read-only de fontes confirmou: Autofeed/crawl `10525577766`, API principal `10636492695`, API local `10636384718`, e file feed `10646853947`; o file feed tem header `id,color,age_group,gender,size`, sem preço. Portanto preço fica amarelo/bloqueado por fonte/ownership/auto-update/crawl; não reexecutar em massa.
- Monitor LK OS atualizado em 2026-05-14T21:05Z sobre 23.277 `productstatuses`: `price_updated` 921 instâncias/307 produtos, `strikethrough_price_updated` 228/76 e `landing_page_error` 3/1. Os alvos não-preço pequenos corrigidos continuam fora do diagnóstico: `missing_item_attribute_for_product_type` 0, `image_single_color` 0, `image_link_broken` 0, `restricted_gtin` 0 e `reserved_gtin` 0.
- Point repair não-preço executado com rollback privado: 27 ações planejadas/aplicadas (22 cores online via Merchant ProductInputs v1; 5 limpezas de `additionalImageLinks`, sendo 2 local/LIA via Content API e 3 online via ProductInputs). Productstatuses final nos IDs atuados: 0 issues alvo. Ficou pending 1 landing page ativa (`online:pt:BR:GW3773-39`); probe público retornou HTTP 200, produto ativo, então não é caso seguro de delete/supressão — tratar como crawl/diagnóstico Merchant.

### Em paralelo seguro

- PRD LK OS v0.2 atualizado com Mission Control, sourcing por stockout e fluxo LK Compras/Júlio/Notion.
- Mission Control v2 contém ranking stockout/recompra de 120 dias.
- Ranking atual: 872 grupos com SKU, 647 candidatos, 18 Tiny zero/tamanho exato, 20 ambíguos, 609 pendentes de confirmação Tiny.
- Programa de fechamento criado em `areas/lk/projetos/lk-os-program-to-finish-2026-05-14.md`.
- Novo monitor documentado em `areas/lk/rotinas/gmc-post-abc-monitor-2026-05-14.md` e relatório `reports/lk-gmc-2026-05-14-post-abc-monitor.md`.

### Bloqueado até condição/aprovação

- Novos patches Merchant para preço ficam bloqueados até diagnóstico de fonte/sobrescrita: `ProductInputs v1` e `Content API source=api` retornaram sucesso, mas 109 readbacks não persistiram.
- Residuais menores de atributo/imagem foram tratados; o único não-preço pending agora é `landing_page_error` em `online:pt:BR:GW3773-39`, mas Shopify/live público está ativo e HTTP 200, então não deletar/suprimir sem diagnóstico Merchant/crawl.
- StockX/GOAT: fallback posterior apenas para os 3 sem match forte ou outros casos; exige novo escopo e normalização de tamanho.
- WhatsApp/fornecedor/compra: bloqueados.
- Shopify/Tiny/Klaviyo/Rivo/Judge.me/Meta/Google: sem novos writes.

### Próximo passo recomendado

1. Preço: manter bloqueado para writes. Próximo seguro é investigar fonte/canal de sobrescrita (Google/Shopify app/feed/API data source) e auto-update/crawl, porque o Merchant continua stale vs Shopify Admin e PDP público em 108 casos.
2. Para o único landing residual (`online:pt:BR:GW3773-39`), não deletar: PDP público retornou HTTP 200 e Shopify está ativo; acompanhar/diagnosticar como crawl/Merchant landing-page issue.
3. Não reexecutar preço em massa enquanto o readback não persistir; manter rollback/progresso privado preservados.

## Resposta padrão para Telegram — estado atual pós-GMC P2A

```text
LK OS está amarelo/verde: a frente pesada GMC P2A saiu de execução e entrou em monitor pós-write.

Agora: P2A aplicou/verificou 9.826 patches em Merchant, com 0 falhas de products.get. O bucket Bags residual foi tratado em point repair de 44 produtos. Monitor pós-status encontrou todos os 9.826 IDs e mostra residuais separados: preço/promotional price, 136 missing attrs remanescentes e alguns landing page errors. Não vou reexecutar P2A em massa.

Paralelo seguro: PRD v0.2, Mission Control v2 e ranking de recompra/stockout de 120 dias estão consolidados. Droper read-only já foi executado para os 18 candidatos: 15 têm match forte/útil no tamanho; 3 ficam para fallback posterior se aprovado.

Próximo passo recomendado: revisar os 15 cards Júlio/Notion e decidir se viram write real; em paralelo, aprovar ou não pacote de limpeza para 12 URLs 404 e, depois, executor Merchant v1 para 68 atributos com rollback.

Não executado: StockX/GOAT, WhatsApp, Notion write, compra, fornecedor, Shopify/Tiny/Klaviyo/Meta/Google write, cron ou infra. Droper foi somente read-only público nos 18 aprovados.
```

## Resposta padrão para Telegram — depois do monitor pós-GMC

```text
LK OS: GMC P2A finalizado e consolidado.

Agora: relatório final GMC salvo, rollback/progresso preservados e Mission Control atualizado.

Próximo gate: aprovar ou não consulta Droper read-only nos candidatos `stockout_exact_ready` do ranking de 120 dias.

Isso autoriza somente consulta/preview. Não autoriza compra, fornecedor, WhatsApp, Notion write, StockX/GOAT ou mudança em Shopify/Tiny/Merchant.
```

## Critério de qualidade

- Não responder status com lista longa de caminhos locais.
- Sempre trazer o payload/decisão relevante inline no Telegram.
- Diferenciar execução em andamento, paralelo seguro e bloqueios.
- Não chamar `pending_future` de próximo passo ativo.
- Não tratar progresso JSONL como finalização sem readback/consolidação.
