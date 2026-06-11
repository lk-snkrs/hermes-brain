# LK GMC/Product Data + Local Inventory Review — 2026-06-11

**Modo:** read-only / preview.  
**Execução:** Content API GET/list + Merchant API dataSources list + Shopify público `.js` GET + checks públicos de HTML/schema + DataForSEO SERP/keyword.  
**Writes executados:** 0. Sem Content API write, sem ProductInput PATCH, sem supplemental feed write/upload, sem `fetchNow`, sem reprocess, sem Shopify write, sem preço/estoque/desconto/campanha.

## Veredito executivo

A conta está **operacional, mas não saudável** para Merchant/Shopping: há cobertura ampla aprovada, porém os gargalos principais continuam em **atributo de produto**, **Local Inventory/LIA** e **contrato Simprosys/local offer**.

- **23.820 produtos/statuses lidos** no Merchant.
- **Shopping aprovado:** 22.156 produtos.
- **Shopping reprovado:** 1.664 produtos.
- **LocalSurfacesAcrossGoogle aprovado:** 10.406 produtos.
- **LocalSurfacesAcrossGoogle reprovado:** 1.186 produtos.
- **Maior gargalo:** `missing_item_attribute_for_product_type` — 5.496 instâncias / 2.577 produtos.
- **Gargalo Local/LIA:** `local_stores_lack_inventory` — 2.372 instâncias / 1.186 produtos.
- **Contrato local `link_template`:** `mhlsf_full_missing_valid_link_template` — 465 ofertas, todas `local`, todas prefixo `LIA_`, todas sem `link_template`/`mobile_link_template` detectado.

**Classificação:** decision-grade para saúde GMC/feed porque usei leitura autenticada do Merchant. Parcial para impacto comercial por SKU porque este run não cruzou GA4/Shopify revenue/order por offer; a priorização comercial fina deve usar o stack Growth semanal antes de qualquer aplicação.

## Fontes verificadas

- Google Merchant Center / Content API `products` e `productstatuses`: 23.820/23.820.
- Merchant API `dataSources`:
  - `lksneakers.com.br` — `AUTOFEED`, primary.
  - `Simprosys Local Feed (Merchant API)` — `API`, primary.
  - `Simprosys Feed (Merchant API)` — `API`, primary.
- Public Shopify `.js` para amostras de PDP/404/preço.
- HTML público em amostra:
  - PDP 204L Mushroom: 4 JSON-LD, 1 Product, 12 Offer, 1 FAQPage.
  - Collection Adidas Samba Jane: 4 JSON-LD, FAQPage presente.
- DataForSEO Brazil/PT:
  - Keyword overview para 10 modelos prioritários.
  - SERP mobile para `new balance 204l`, `adidas samba jane`, `nike dunk low`.

## Snapshot de issues GMC

| Tema | Issue | Produtos | Instâncias | Leitura |
|---|---:|---:|---:|---|
| Product data | `missing_item_attribute_for_product_type` | 2.577 | 5.496 | Provável falta de `color`/atributos por tipo; corrigível via supplemental/ProductInput com cuidado de overwrite Simprosys. |
| LIA/local | `local_stores_lack_inventory` | 1.186 | 2.372 | LocalSurfaces sofre por inventário local; depende de contrato Local Inventory/GBP/store_code. Não é SEO/PDP. |
| LIA/local | `mhlsf_full_missing_valid_link_template` | 465 | 465 | Todas `local`, `LIA_`, source `api`, sem link template. É contrato do feed local, não erro de preço nem 404. |
| Preço automático | `strikethrough_price_updated` | 48 | 144 | Google ajustou preço riscado; monitorar, não corrigir em massa sem confirmação. |
| Preço automático | `price_updated` | 19 | 57 | Google ajustou preço; precisa checagem por amostra antes de ação. |
| Identificadores | `restricted_gtin` | 35 | 70 | Corrigir só com evidência de GTIN/MPN/brand; risco alto de identificador falso. |
| Required attr | `item_missing_required_attribute` | 32 | 64 | Candidatos a preview, mas precisa campo exato por offer. |
| Landing page | `landing_page_error` | 16 | 34 | Amostra pública retornou `.js` 404 para vários handles; aqui há risco real de oferta órfã/crawl/autofeed antigo. |
| Imagem | `image_link_internal_error` | 2 | 5 | Pontual; checar imagens antes de feed write. |
| Imagem | `image_too_small_for_high_resolution` | 1 | 1 | Pontual; oportunidade de imagem/feed. |

## Local Inventory / LIA / store_code

Achado crítico:

- 465 ofertas afetadas por `mhlsf_full_missing_valid_link_template`.
- 465/465 são `channel=local`.
- 465/465 têm `offer_id` com prefixo `LIA_`.
- 465/465 vêm de `source=api`.
- 465/465 estão sem `link_template` e sem `mobile_link_template` no recurso lido.
- Exemplos: `LIA_1183A872254-12`, `LIA_HV8547-001-3`, `LIA_U204LMMA-2`, `LIA_HV8547-002-42`.

Interpretação: é um problema de **contrato Simprosys Local Feed / Local Inventory / store_code**, não de PDP individual. O link público pode existir, mas o Google exige um `link_template` válido com sinal de loja/store code para veiculação local.

**Packet recomendado — preview, sem write:**

- Problema: Local offers `LIA_*` sem `link_template` válido.
- Evidência: 465 ofertas local/API sem `link_template_current` e com detail `A valid [link_template] value with store code is required for the offer to serve`.
- Ação proposta: micro-piloto em 10–20 offers `LIA_*` para definir o menor surface correto: Simprosys Local Feed/configuração de local feed, ou ProductInput local-offer field se Simprosys não sobrescrever.
- Template candidato para validação técnica, **não aplicado**: `<current_product_link>?store_code={store_code}` ou equivalente aceito pelo contrato do feed.
- Risco: Simprosys pode sobrescrever ProductInput; se aplicado no surface errado, volta a reprovar no próximo sync.
- Rollback: snapshot dos 10–20 offers antes da alteração; reverter `link_template` para valor anterior/vazio no mesmo surface; readback de ProductInput/status.
- Validação: Content/Merchant readback + esperar reprocessamento diagnóstico; não usar `fetchNow` sem aprovação.

Artifact preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-link-template-preview-2026-06-11.csv`.

## Product data: cor/atributos/títulos/GTIN/MPN/brand/condition/imagens

### Missing item attribute / color

Foram gerados previews locais para os 2.577 produtos com `missing_item_attribute_for_product_type`:

- Alta confiança por termo de cor no título: 2.135.
- Média confiança: 57.
- Revisão humana necessária: 385.

**Recomendação:** usar apenas alta confiança em micro-piloto, começando por offers com demanda/comercial mais forte. Não aplicar 2.135 de uma vez.

Artifact preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-missing-color-preview-2026-06-11.csv`.

### GTIN / MPN / brand / identifiers

- `restricted_gtin`: 35 produtos.
- `reserved_gtin`: 2 produtos.
- `invalid_mpn` e `missing_required_gtin`: 0 neste snapshot.

**Recomendação:** não inventar GTIN. Corrigir por fonte confiável: embalagem/fabricante/Shopify/Tiny quando houver código canônico; quando não houver, usar estratégia correta de `identifier_exists`/MPN/brand somente com evidência. Packet separado por offer.

### Títulos / variante como título

No grupo `landing_page_error`, alguns produtos aparecem com título apenas de variante, ex.: `35`, `45`, `P/s`. Isso pode ser resíduo de autofeed/crawl/variante e não necessariamente título visível do Shopify.

**Recomendação:** tratar como triagem de feed/autofeed e não como Shopify-title write. Se houver ação, é Merchant/ProductInput title ou exclusão/limpeza do offer, com rollback.

### Imagens

- `image_single_color`: 4 produtos.
- `image_link_internal_error`: 2 produtos.
- `image_link_broken`/fallback: 1 produto.
- `image_too_small_for_high_resolution`: 1 produto.

**Recomendação:** ponto a ponto. Se a imagem pública estiver correta no Shopify mas o feed aponta para URL quebrada, corrigir no surface feed/ProductInput; se a imagem do produto realmente é insuficiente, abrir packet para Shopify/image somente depois de aprovação específica.

### Condition

`condition_updated_from_detected`: 4 produtos. Não há sinal de escala suficiente para ação em massa.

## Landing page / Shopify ↔ GMC divergência

`landing_page_error`: 16 produtos / 34 instâncias. A amostra pública via `.js` retornou 404 em vários links, incluindo:

- `tenis-new-balance-204l-x-atmos-cow-girl-brown-marrom` — 404.
- `calca-saint-studio-wide-alfaiataria-preto` — 404.
- `tenis-adidas-samba-jane-white-red-gum-branco` — 404.
- `nike-air-force-1-07-white` — 404.

Interpretação: aqui há risco real de offers órfãos, handle antigo, produto removido/draft ou crawl/autofeed residual. Não é caso para mexer em preço/estoque.

Artifact de amostra: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-landing-page-sample-2026-06-11.csv`.

**Packet recomendado:**

- Problema: offers online apontando para URLs públicas com 404.
- Ação proposta: resolver cada offer: atualizar link no Merchant/ProductInput se produto existe com novo handle; ou pausar/excluir offer residual se produto foi removido; ou ajustar fonte Simprosys/autofeed.
- Risco: exclusão/pausa errada pode remover produto vendável; link fix no surface errado pode ser sobrescrito.
- Rollback: snapshot completo do offer antes de alteração; reverter link/status; validar por public `.js` + productstatus.
- Aprovação necessária: sim, qualquer update/delete/pausa/fetch.

## Simprosys feed contract

O Merchant API mostrou 3 data sources relevantes:

1. `lksneakers.com.br` — `AUTOFEED` primary.
2. `Simprosys Local Feed (Merchant API)` — `API` primary.
3. `Simprosys Feed (Merchant API)` — `API` primary.

Risco operacional: correções por ProductInput direto podem ser sobrescritas pelo Simprosys/API no próximo sync. Portanto:

- Link template/local inventory deve ser resolvido preferencialmente no contrato/configuração do Local Feed.
- Missing color pode ser supplemental feed se o supplemental tiver precedência e não conflitar com Simprosys.
- Título/GTIN/MPN deve ter micro-piloto e readback depois do próximo sync.

## DataForSEO / oportunidade comercial

Usei DataForSEO para diferenciar problema de feed vs oportunidade comercial. Principais sinais Brazil/PT:

| Keyword | Volume | Intent | Leitura |
|---|---:|---|---|
| `new balance 9060` | 246.000 | transactional | Alta demanda; issues de produto/atributo aqui têm impacto comercial alto. |
| `nike dunk low` | 33.100 | transactional | SERP/Shopping dominado por Nike, Artwalk, Authentic Feet; qualidade feed e preço/imagem importam. |
| `new balance 204l` | 9.900 | transactional | Crescimento anual muito forte; SERP mostra popular products e PAA. LK não apareceu no top orgânico desta coleta; feed/Shopping precisa estar limpo. |
| `nike shox tl` | 9.900 | transactional | Alta demanda estável. |
| `adidas samba og` | 6.600 | transactional | Alta demanda e concorrência. |
| `onitsuka tiger mexico 66` | 6.600 | transactional | Alta demanda; autenticidade/guide + feed limpo. |
| `adidas samba jane` | 2.400 | transactional | Tendência forte; LK apareceu organicamente em posição 6 na SERP mobile. Prioridade de manter feed/Shopping saudável. |
| `adidas gazelle indoor` | 1.900 | transactional | Comercial relevante. |
| `air jordan 1 travis scott` | 480 | transactional | Menor volume, maior ticket/autenticidade. |
| `nike jacquemus moon shoe` | 110 | transactional | Nicho/collab; alta qualidade de página/feed importa para AI/Shopping. |

SERP live:

- `adidas samba jane`: LK apareceu organicamente em `lksneakers.com.br/collections/adidas-samba-jane` na posição orgânica 2/rank absoluto 6; Shopping/Popular Products é dominado por adidas, Droper, Amazon e outros. Isso reforça que o feed precisa estar limpo para capturar demanda já existente.
- `new balance 204l`: SERP dominada por New Balance, Authentic Feet, Droper, Guadalupe; há bloco Popular Products e PAA. O 204L também aparece nos samples de LIA/link_template, então é candidato forte para micro-piloto.
- `nike dunk low`: SERP/Popular Products dominados por Nike, Artwalk, Authentic Feet; se LK tiver offers afetados, priorizar apenas por demanda + margem/receita, não por HTML isolado.

## Schema Product/Offer

Amostra pública:

- PDP `tenis-new-balance-204l-mushroom-arid-stone-marrom`: Product JSON-LD presente, Offers presentes, FAQPage presente.
- Collection `adidas-samba-jane`: FAQPage presente; Product/Offer não esperado como página de coleção.

Conclusão: não há evidência de problema sistêmico de schema para Merchant nesta amostra. Schema deve ser usado como suporte para rich results/consistência, mas os blockers atuais vêm de feed/ProductStatus: atributos, local inventory, link_template e landing URLs.

## Top 5 ações recomendadas — todas approval-only antes de qualquer write

1. **Micro-piloto Local Inventory link_template**
   - Escopo: 10–20 offers `LIA_*`, incluindo 204L/Moon Shoe/Onitsuka com demanda.
   - Impacto: destravar parte do Shopping/local offer que hoje reprova por contrato.
   - Risco: overwrite Simprosys; precisa descobrir surface correto.
   - Validação: readback + productstatus; sem `fetchNow` sem aprovação.

2. **Missing color high-confidence micro-pilot**
   - Escopo: 50–100 offers de alta confiança, priorizados por demanda/Shopify/GSC.
   - Impacto: reduzir 2.577 produtos com missing attribute.
   - Risco: cor errada em variantes; aplicar só onde título sustenta.
   - Rollback: supplemental/ProductInput snapshot por offer.

3. **Landing page error cleanup packet**
   - Escopo: 16 produtos com 404/landing issue.
   - Impacto: remove reprovações reais e evita tráfego para oferta inválida.
   - Risco: excluir/pausar produto ativo por engano; exige Shopify Admin read-only antes.
   - Rollback: restore link/status/offer.

4. **Identifier/GTIN packet pontual**
   - Escopo: 35 `restricted_gtin` + 2 `reserved_gtin`.
   - Impacto: qualidade e elegibilidade Shopping.
   - Risco: alto se inventar GTIN; usar só fonte confiável.

5. **Imagem/policy packet pontual**
   - Escopo: 1–4 produtos por issue de imagem.
   - Impacto: baixo volume, mas fácil de limpar se evidência confirmar.
   - Risco: Shopify/image write é outra superfície e precisa aprovação separada.

## O que não fiz

- Não alterei Merchant Center.
- Não alterei ProductInput.
- Não alterei supplemental feed.
- Não chamei `fetchNow` nem reprocessamento.
- Não alterei Shopify, preço, estoque, imagens, título, descrição, theme ou campanha.
- Não usei estoque/Tiny como critério decisivo de SEO/CRO.
- Não enviei contato externo.

## Artifacts

- JSON completo: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-product-data-local-inventory-review-2026-06-11.json`
- CSV link_template preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-link-template-preview-2026-06-11.csv`
- CSV missing color preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-missing-color-preview-2026-06-11.csv`
- CSV landing sample: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-landing-page-sample-2026-06-11.csv`

## Approval packet sugerido para Lucas

Se quiser avançar, a menor aprovação segura é:

> Aprovo preparar e executar um micro-piloto read/write de GMC Local Inventory `link_template` para até 20 offers `LIA_*` priorizados, com snapshot antes, alteração apenas no surface correto após confirmação, sem Shopify, sem preço/estoque, sem campanhas, sem `fetchNow` salvo se eu aprovar separado, e com readback/rollback.

Sem essa aprovação, o próximo passo continua sendo só refinar preview e cruzar os offers com Shopify/GSC/GA4 para priorização comercial.
