# LK — P0 restantes: preview de correção Tiny `codigo` — 2026-05-11

## Veredito

Após lookup read-only dos 13 P0 restantes, há **7 candidatos** para preencher `codigo` no Tiny usando SKU Shopify já existente. **6 continuam bloqueados** por falta de SKU Shopify, duplicidade ou ausência de match canônico seguro.

## Guardrails

- Preview only nesta etapa.
- Sem write Tiny ainda.
- Sem write Shopify.
- Sem alteração de preço, estoque, produto, campanha ou sourcing.

## Candidatos a aprovação de write Tiny `codigo`

### 1. Tênis Nike Mind 002 Light Khaki Bege — 41
- Shopify variant ID: `47893735932126`
- SKU Shopify atual: `NKE-9054174-41`
- Tiny ID alvo: `1069545385`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `NKE-9054174-41`
- Confiança: `media_alta`
- Motivo: Shopify SKU preenchido + match Tiny único de tamanho/grade com codigo vazio; siblings Shopify seguem padrão.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 2. Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — 42.5
- Shopify variant ID: `48066691465438`
- SKU Shopify atual: `ONI-0995678-425`
- Tiny ID alvo: `1070120736`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `ONI-0995678-425`
- Confiança: `media_alta`
- Motivo: Shopify SKU preenchido + match Tiny único de tamanho/grade com codigo vazio; siblings Shopify seguem padrão.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 3. Tênis New Balance 204L Cortado Marrom — 37
- Shopify variant ID: `47856402530526`
- SKU Shopify atual: `NB-0254942-37`
- Tiny ID alvo: `1069544047`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `NB-0254942-37`
- Confiança: `media_alta`
- Motivo: Shopify SKU preenchido + match Tiny único de tamanho/grade com codigo vazio; siblings Shopify seguem padrão.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 4. Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — 38
- Shopify variant ID: `48054217933022`
- SKU Shopify atual: `ONI-6772830-38`
- Tiny ID alvo: `1070119554`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `ONI-6772830-38`
- Confiança: `media_alta`
- Motivo: Shopify SKU preenchido + match Tiny único de tamanho/grade com codigo vazio; siblings Shopify seguem padrão.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 5. Moletom Alo Yoga Cropped Serenity Coverup Black Preto — S/P
- Shopify variant ID: `47706484539614`
- SKU Shopify atual: `ALO-8506462-S`
- Tiny ID alvo: `1069542767`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `ALO-8506462-S`
- Confiança: `media`
- Motivo: Busca Tiny pelo título exato/cor do produto tem match de grade único; ambiguidade surgiu apenas na busca ampla por família/cor irmã.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 6. Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza — L/G
- Shopify variant ID: `47860151976158`
- SKU Shopify atual: `SST-4542302-L`
- Tiny ID alvo: `1069544315`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `SST-4542302-L`
- Confiança: `media`
- Motivo: Busca Tiny pelo título exato/cor do produto tem match de grade único; ambiguidade surgiu apenas na busca ampla por família/cor irmã.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

### 7. Camiseta Pace Buero Washed Black Preto — S/P
- Shopify variant ID: `47967340331230`
- SKU Shopify atual: `PAC-1197278-S`
- Tiny ID alvo: `1069930823`
- Tiny `codigo` atual: `[vazio]`
- Tiny `codigo` proposto: `PAC-1197278-S`
- Confiança: `media_alta`
- Motivo: Shopify SKU preenchido + match Tiny único de tamanho/grade com codigo vazio; siblings Shopify seguem padrão.
- Rollback: restaurar `codigo` Tiny para vazio/anterior e revalidar.

## Bloqueados / decisão humana ou cadastro manual

- **Camiseta Pace Cotton Code Branca — G/L**
  - Shopify variant ID: `47512247599326`
  - SKU Shopify: `[sem SKU]`
  - Estado: `needs_manual_tiny_mapping_or_cadastro`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.
- **Camiseta Aimé Leon Dore Musician Graphic Off White — S/P**
  - Shopify variant ID: `47579297939678`
  - SKU Shopify: `[sem SKU]`
  - Estado: `needs_manual_tiny_mapping_or_cadastro`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.
- **Rhode Pocket Blush — Sleepy Girl - Soft Mauve**
  - Shopify variant ID: `46838740648158`
  - SKU Shopify: `[sem SKU]`
  - Estado: `needs_manual_tiny_mapping_or_cadastro`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.
- **Camiseta Pace Cotton Code Preta — G/L**
  - Shopify variant ID: `47512247730398`
  - SKU Shopify: `[sem SKU]`
  - Estado: `needs_manual_tiny_mapping_or_cadastro`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.
- **Camiseta Pace Sketch Yourself Off White — P/S**
  - Shopify variant ID: `47019131568350`
  - SKU Shopify: `[sem SKU]`
  - Estado: `needs_manual_tiny_mapping_or_cadastro`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.
- **Camiseta Pace Patavision Off White — P/S**
  - Shopify variant ID: `47019093295326`
  - SKU Shopify: `PAC-5857246-S`
  - Estado: `ambiguous_tiny_matches_with_shopify_sku`
  - Motivo: Sem SKU Shopify, match Tiny duplicado/ambíguo, ou ausência de match canônico seguro.

## Aprovação necessária para executar os 7 writes Tiny

`aprovo preencher codigo Tiny dos 7 itens candidatos com os SKUs Shopify propostos, sem alterar Shopify, preço, estoque ou produto`

Sem essa aprovação, estes 7 ficam como preview e os 6 bloqueados seguem para decisão humana/cadastro manual.
