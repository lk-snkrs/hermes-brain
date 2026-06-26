# Nike Mind — GMC identifiers packet

Data: 2026-06-07T21:10:33.213476+00:00
Escopo aprovado por Lucas: avançar na frente de identificadores/GMC após KicksDev não retornar GTIN.

## Resultado executivo

- GTIN/EAN/UPC real via KicksDev: **0 encontrados**.
- Variantes Shopify Nike Mind sem barcode: `123`.
- Candidatas a enrichment conservador com `brand=Nike` + `mpn=<style_sku>`: `104` variantes.
- Bloqueadas para correção prévia/manual review: `19` variantes.

## Guardrail aplicado

- Não inventar GTIN.
- Não preencher `identifier_exists=false` para Nike Mind como default, porque Nike normalmente possui identificador de fabricante. Usar `identifier_exists=false` nesse caso pode ser incorreto perante política Google.
- Caminho conservador: se o GTIN não é conhecido, manter GTIN vazio e garantir `brand=Nike` + `mpn=style_sku` quando o style SKU for confiável.

## O que pode ser aplicado em próxima etapa, se aprovado com escopo de write

Para variantes candidatas:

- `brand`: Nike
- `mpn`: style SKU Nike, exemplo `HQ4307-100`
- `gtin`: vazio, até fonte real
- `identifier_exists`: não alterar / não forçar falso sem revisão de política por item

## Bloqueios

- Variantes com SKU vazio ou style não confiável não devem receber MPN automático.
- GTIN só volta para pauta com fonte primária/verificável: etiqueta, embalagem, invoice, fornecedor, Nike/GS1/Tiny confiável.

## Arquivos

- CSV aplicável/revisão: `gmc_identifier_candidate_rows.csv`
- JSON detalhado: `gmc_identifier_candidate_rows.json`

## Aprovação necessária para write

Para eu aplicar, preciso de aprovação explícita de um destes caminhos:

1. **Shopify-only**: atualizar/garantir MPN/metafields se o fluxo local/GMC usa dados Shopify para feed.
2. **GMC supplemental/feed**: criar ou atualizar override de `brand/mpn` para os itens candidatos.
3. **Read-only QA primeiro**: checar no GMC quais desses itens já têm brand/mpn antes de aplicar qualquer coisa.

Recomendação: fazer **Read-only QA GMC primeiro**, depois aplicar somente os gaps reais.
