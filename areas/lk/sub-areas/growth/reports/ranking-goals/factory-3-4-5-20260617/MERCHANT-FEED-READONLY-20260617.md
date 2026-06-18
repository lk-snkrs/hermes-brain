# Merchant / Feed read-only audit — 2026-06-17

Status: auditoria pública/read-only. Não houve GMC/feed write. values_printed=false.

## Escopo verificado

- HTML público de PDP Moon Shoe Off White.
- HTML público de collections Moon Shoe, Travis e New Balance 204L.
- SERP mobile Brasil para `nike travis scott` e `new balance 204l`.
- DataForSEO keyword overview para termos comerciais.

## Evidências

### Simprosys / Google Shopping Feed

Detectado app block público:

- `shopify://apps/simprosys-google-shopping-feed/blocks/core_settings_block/...`
- Variável pública `gsf_spd_data` em PDP.

No PDP `/products/tenis-nike-moon-shoe-sp-jacquemus-off-white`, a variante renderizada expõe:

- product_id presente;
- variant_id presente;
- name: `Tênis Nike Moon Shoe SP Jacquemus Off White`;
- price: BRL;
- SKU: `HV8547-002-34`;
- brand: `Jacquemus x Nike`;
- category: `Tênis`.

O script indica que o item ID do feed parece usar SKU (`parseInt('1') === 1`), não `shopify_BR_product_variant`.

### SERP / Shopping pressure

#### `nike travis scott`

- Volume: 8.100/mês; intenção transactional.
- Popular Products aparece acima do orgânico.
- LK aparece orgânico rank_absolute 4 / rank_group 2.
- AI Overview cita LK como referência para a coleção Travis.
- Popular Products da amostra mostra concorrentes como Droper, Bee Fancy e Original São Paulo; LK não observada no bloco Popular Products da amostra.

#### `new balance 204l`

- Volume: 12.100/mês; maio/abril 2026 com 40.500 buscas.
- SERP dominada por New Balance oficial nas primeiras posições.
- Knowledge/shopping compare mostra marketplaces e lojas com snippets de estoque/frete.
- LK não observada nos blocos top da amostra pública.

## Diagnóstico

### Travis

LK já tem força orgânica e citação em AI Overview. O gargalo Merchant é aparecer melhor nos blocos de produto para termos de alta intenção, mas isso depende de GMC/feed e competitividade de produto/preço/sinais — não deve ser mexido sem aprovação específica.

### New Balance 204L

SEO da collection é bom, mas o campo de batalha principal da SERP é produto/listing. Para melhorar 204L, o próximo pacote deve auditar:

- item ID consistency;
- título de produto no feed;
- brand padronizado;
- GTIN/MPN quando aplicável;
- image_link/additional_image_link;
- product_type/google_product_category;
- availability/price mismatch;
- disapprovals/warnings no GMC.

### Moon Shoe

O public data layer do Simprosys parece preencher SKU, brand, category e price. Ponto de atenção: brand `Jacquemus x Nike` pode ser ótimo comercialmente, mas no Merchant às vezes a padronização por marca principal/colaboração precisa ser validada contra reprovações e comparação de performance.

## Limitação

Este relatório não é decision-grade para reprovações GMC porque não abriu o painel Merchant Center nem o feed exportado autenticado. É suficiente para priorização e briefing de auditoria.

## Próximo action sem write

Preparar um pacote GMC read-only autenticado para:

1. exportar warnings/disapprovals por item;
2. filtrar por clusters Travis, New Balance 204L, Moon Shoe e Onitsuka;
3. comparar item title/feed title/SEO title;
4. validar GTIN/MPN/brand por família;
5. gerar patch proposal, não aplicar.

## Approval necessário para qualquer alteração

- GMC/feed writes;
- alteração de brand/MPN/GTIN;
- título/descrição de feed;
- regras Simprosys;
- supplemental feed;
- campanhas Shopping/Performance Max.
