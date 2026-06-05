# LK Growth OS — GMC/Product Data + Local Inventory Review — 2026-06-04

Gerado em: `2026-06-04T11:52:00Z`  
Modo: `read-only / preview`  
Writes externos: `0`  
Status: `decision-grade para triagem GMC/Product Data`, com correções bloqueadas até aprovação explícita.

## Veredito curto

GMC não está saudável. O problema material da semana é **Local Inventory/LIA**: `10.441` ofertas `local:*`/`LIA_` estão reprovadas em Shopping por `mhlsf_full_missing_valid_link_template` — falta `link_template` válido com `store_code`. Isso é um issue de contrato Local Inventory/Simprosys/Shopify POS, não de preço, PDP 404 ou copy.

O segundo bloco é qualidade de dados: `712` produtos com atributo ausente por tipo de produto, com preview de cor para `393` linhas high-confidence. P0 de preço inválido está limpo (`0` price mismatch/out-of-range), mas ainda existem `1.431` landing errors e `234` price auto-updates que exigem triagem antes de qualquer patch.

## Fontes verificadas

- Readiness LK Growth: `/opt/data/profiles/lk-growth/scripts/lk_growth_tooling_readiness.py`
  - `pagespeed_crux=true`, `gsc_ga4_url_inspection=true`, `klaviyo_analytics=true`, `ahrefs_api=true`, `dataforseo_mcp=available via Hermes MCP tools`.
- Google Merchant Center / Content API read-only:
  - `21.402` products lidos.
  - `21.402` productstatuses lidos.
  - Cobertura IDs: `0` products sem status; `0` statuses sem product resource.
- Merchant API DataSources read-only:
  - `lksneakers.com.br` — `AUTOFEED`, primary.
  - `Simprosys Local Feed (Merchant API)` — `API`, primary.
  - `Simprosys Feed (Merchant API)` — `API`, primary.
- Shopify público read-only:
  - GET público em PDP `.js` para amostras de divergência GMC ↔ PDP.
- DataForSEO keyword volume read-only, Brasil/pt:
  - `new balance 204l`, `adidas samba jane`, `nike dunk low`, `air jordan 1 travis scott`, `adidas gazelle indoor`.

## Artefatos salvos no Brain

- Weekly GMC: `reports/lk-gmc-weekly-review-2026-06-04.md`
- Weekly GMC JSON: `reports/lk-gmc-weekly-review-2026-06-04.json`
- Rotina GMC: `areas/lk/rotinas/gmc-weekly-review-2026-06-04.md`
- Packet Local Inventory/link_template: `reports/lk-gmc-local-link-template-investigation-2026-06-04.md`
- Packet Local Inventory JSON: `reports/lk-gmc-local-link-template-investigation-2026-06-04.json`
- Preview Local Inventory CSV: `reports/lk-gmc-local-link-template-preview-2026-06-04.csv`
- Preview color CSV: `reports/lk-gmc-missing-color-preview-2026-06-04.csv`
- Preview color MD: `reports/lk-gmc-missing-color-preview-2026-06-04.md`

## Health GMC — números principais

| Área | Status | Evidência | Leitura |
|---|---:|---:|---|
| Shopping disapproved | Crítico | `11.835` produtos | Dominado por LIA/link_template. |
| Shopping approved | Parcial | `9.351` produtos | Online/Shopping ainda roda em parte. |
| LocalSurfaces approved | Bom/parcial | `10.414` produtos | LocalSurfaces aparece aprovado, mas Shopping local falha por link_template. |
| LocalSurfaces disapproved | Baixo | `27` produtos | Principalmente inventory/store local pontual. |
| P0 preço mismatch/out-of-range | Limpo | `0` / `0` | Sem packet de preço final agora. |
| Landing errors | Atenção | `1.431` produtos | Alguns PDPs públicos OK; precisa classificar link/PDP/feed lag. |
| Missing product attributes | Atenção | `712` produtos | `393` color high-confidence para approval packet. |
| Price auto-update | Atenção | `234` produtos | Sinal de governança de preço/promo; não é bulk patch. |
| Strikethrough auto-update | Atenção | `223` produtos | Exige lógica salePrice/compare_at antes de qualquer correção. |
| GTIN restrito/reservado | Baixo/médio | `15` + `1` produtos | Não inferir GTIN; precisa fonte oficial. |
| Local stores lack inventory | Baixo | `27` produtos | Contexto Local/LIA; não usar estoque como prioridade SEO/CRO. |

## Packet E — Local Inventory / LIA / store_code

**Problema**  
`mhlsf_full_missing_valid_link_template` em `10.441` ofertas locais.

**Evidência**

- Afetados: `10.441`.
- Canal: `local` em `10.441`.
- Source: `api` em `10.441`.
- Offer prefix: `LIA_` em `10.441`.
- `link_template`/`mobile_link_template`: `missing` em `10.441`.
- Sinal de `store_code` no template atual: `0`.
- Detalhe do Merchant: `A valid [link_template] value with store code is required for the offer to serve`.
- Destino afetado: `Shopping`.
- Data source provável: `Simprosys Local Feed (Merchant API)` / integração que cria `local:*` via API.

**Interpretação**  
A superfície correta parece ser a geração das ofertas locais / Simprosys Local Feed / Shopify POS-local inventory, não a copy de PDP, não o feed online e não SEO. O PDP público das amostras existe (`ok`), então tratar como 404/preço seria erro.

**Ação proposta — preview somente**

- Validar com Simprosys/Google o contrato exato de `store_code` aceito.
- Micro-piloto nominal em `5–20` offers locais, se Lucas aprovar, adicionando apenas `link_template` no surface dono.
- Padrão candidato para revisão técnica: `{current_product_link}{separator}store_code={store_code}`.
- Exemplo: `https://lksneakers.com.br/products/<handle>?store_code={store_code}` ou `...&store_code={store_code}` quando já houver querystring.

**Risco**  
Alto se feito em massa: altera elegibilidade local de milhares de ofertas. Placeholder errado pode trocar uma reprovação por outra.

**Rollback/validação**

- Snapshot do product resource/config/data source antes do piloto.
- Reverter template anterior no mesmo surface.
- Validar readback product resource + productstatuses.
- Sucesso = queda de `mhlsf_full_missing_valid_link_template` e Shopping local sair de disapproved para pending/approved nas ofertas piloto.
- Revisão D+7 antes de escala.

**Bloqueado sem aprovação**  
Bulk nos `10.441`, `fetchNow`, reprocess, ProductInput patch, upload/feed, Shopify/POS config e campanhas.

## Packet B — Product data quality / missing color

**Problema**  
`missing_item_attribute_for_product_type` em `712` produtos.

**Preview gerado**

- `393` linhas high-confidence.
- `0` medium.
- `319` precisam revisão humana.

**Amostras high-confidence**

| offerId | Cor sugerida | Evidência |
|---|---|---|
| `PERI049-1007` | Preto | Título contém `Preto`. |
| `U204L6A6-34` | Bege | New Balance 204L Reflection Bege. |
| `U204L2SZ-36` | Bege | New Balance 204L Sea Salt Linen Bege. |
| `IQ7604-104` | Rosa | Air Jordan 1 Travis Scott Tropical Pink Rosa. |
| `ALD-9318238-G` | Off White | Aimé Leon Dore Pristine Off White. |

**Ação proposta — preview somente**

- Revisar `reports/lk-gmc-missing-color-preview-2026-06-04.csv`.
- Se aprovado, aplicar apenas high-confidence revisado via menor superfície reversível ativa: supplemental feed/ProductInput conforme contrato Simprosys.
- Medium/ambíguos seguem bloqueados até curadoria humana.

**Risco/rollback/validação**

- Risco: cor inferida errada reduz relevância no Shopping.
- Rollback: remover/sobrescrever atributo no mesmo surface, com snapshot anterior.
- Validação: queda do itemLevelIssue após reprocessamento; revisão D+7.

## Price / Shopify ↔ GMC

- `price_mismatch`: `0`.
- `price_out_of_range`: `0`.
- `price_updated`: `234` produtos.
- `strikethrough_price_updated`: `223` produtos.

Leitura: não há P0 de preço final agora. O que existe é governança de preço/promocional: GMC está ajustando preço/sale/strikethrough em alguns itens. Amostras mostram PDP público com `salePrice` menor que `content_price`, então um bulk patch poderia quebrar promoções corretas. Próximo passo seguro é separar: preço final, salePrice, compare_at/strikethrough, lag e falso positivo.

## Landing pages

- `landing_page_error`: `1.431` produtos.
- `item_missing_required_attribute`: `35` produtos.

Amostras incluem PDP público `.js` OK e preço compatível, então parte pode ser lag/crawl/template/link específico. Classificação necessária antes de qualquer ação:

1. PDP público OK + Merchant ainda acusa landing: monitorar/recheck, sem write.
2. PDP 404 real: decidir entre republicar Shopify, corrigir link, suprimir Merchant ou deletar offer.
3. Preço público diverge por salePrice correto: não corrigir preço final sem lógica de promoção.

## GTIN / MPN / brand / condition / imagens / títulos / variantes

- GTIN restrito: `15` produtos.
- GTIN reservado: `1` produto.
- `condition_updated_from_detected`: `4` produtos.
- `image_single_color`: `2` produtos.
- `image_too_small_for_high_resolution`: `1` produto.
- `utf8_encoding_error`: `6` produtos.
- `restricted_nfs_policy_violation`: `7` produtos.
- `availability_updated`: `6` produtos.

Recomendação: montar filas pequenas por tipo. Não inferir GTIN/MPN automaticamente; exige fonte oficial/fornecedor. Não alterar título/imagem/condition em Shopify sem approval packet específico.

## DataForSEO — oportunidade comercial vs health issue

Objetivo aqui foi separar problema técnico GMC de oportunidade comercial. Os volumes confirmam que alguns itens afetados também têm demanda real, então vale priorizar a triagem por impacto comercial quando houver overlap com offers afetados.

| Keyword | Volume BR/pt | Competição | Sinal |
|---|---:|---|---|
| `nike dunk low` | `33.100` | HIGH | Alto volume; landing/price issues em amostras de Dunk devem subir na fila. |
| `new balance 204l` | `9.900` | HIGH | Alta tendência recente; missing color em 204L tem impacto comercial/GEO/Shopping. |
| `adidas samba jane` | `2.400` | HIGH | Demanda forte; price auto-update em Samba Jane merece governança de sale/strikethrough. |
| `adidas gazelle indoor` | `1.900` | HIGH | Relevante para landing/price checks. |
| `air jordan 1 travis scott` | `480` | HIGH | Menor volume, mas ticket alto; atributos/GTIN precisam precisão. |

Custo DataForSEO registrado: `kw_data_google_ads_search_volume`, `US$0.25`, read-only.

## Simprosys feed contract

Leitura atual dos DataSources indica três superfícies principais:

1. `lksneakers.com.br` — `AUTOFEED`.
2. `Simprosys Local Feed (Merchant API)` — `API`.
3. `Simprosys Feed (Merchant API)` — `API`.

Risco de overwrite: alto. Correções feitas diretamente em ProductInput/supplemental podem ser sobrescritas por Simprosys/API se a origem ativa não for a mesma ou se o app republicar dados. Por isso, qualquer packet precisa declarar:

- surface dono;
- offer IDs aprovados;
- snapshot antes;
- readback depois;
- se Simprosys sobrescreve o campo;
- rollback no mesmo surface.

## Schema Product/Offer

Schema não foi o gargalo principal nesta rotina. Deve entrar apenas quando impactar Merchant/rich results:

- garantir Product/Offer com preço/availability coerentes com PDP;
- não expor taxonomia pública de estoque/pronta entrega/encomenda;
- usar disponibilidade/prazo como confirmação via atendimento/chat quando for copy visível;
- validar que salePrice/compare_at não conflita com JSON-LD/Offer quando houver issue de preço.

## O que posso preparar sem aprovação

1. CSV filtrado de `393` high-confidence color por prioridade comercial: 204L, Dunk, Samba Jane, Gazelle, Travis.
2. Lista nominal de `5–20` offers para micro-piloto `link_template`, com store_code contract checklist.
3. Classificação dos `1.431` landing errors em `PDP ok`, `404 real`, `salePrice/lag`, `link específico`.
4. Packet de governança `price_updated/strikethrough` separando salePrice vs preço final.
5. Fila GTIN/MPN/condition/image por fonte oficial necessária.

## O que exige aprovação antes de executar

- Qualquer Content API / Merchant API write.
- ProductInput PATCH.
- Supplemental feed write/upload.
- Datafeed `fetchNow`, reprocess ou alteração de data source.
- Shopify write, POS/app config, preço, estoque, desconto, imagem, SEO field, theme.
- Campanhas Google/Meta/Klaviyo ou qualquer envio externo.

## O que não foi feito

- Nenhum write externo.
- Nenhum fetch/reprocess.
- Nenhuma mudança em Shopify, preço, estoque, feed, Simprosys, Google Ads, Klaviyo ou campanha.
- Nenhuma ação customer-facing.
