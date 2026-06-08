# Nike Mind — GMC direct identifier QA

Data: 2026-06-07T21:28:14.744252+00:00
Modo: read-only, sem writes.

## Resultado executivo

- Itens Nike Mind encontrados no GMC carregado: `92`.
- Online: `51`.
- Local/LIA: `41`.
- `brand=Nike`: `92/92`.
- `mpn` presente: `91/92`.
- `mpn` coincide com SKU/offerId: `91/92`.
- GTIN presente: `17`.
- GTIN ausente: `75`.

## Conclusão

A frente `brand/mpn` **não é o gargalo principal agora** para os itens Nike Mind encontrados no GMC: brand e MPN já aparecem preenchidos.

O gargalo real continua sendo **GTIN ausente** em parte relevante dos itens, especialmente LIA/local e muitos online.

## Implicação

- Não recomendo aplicar override genérico de `brand/mpn` agora; seria redundante para os itens encontrados.
- Não recomendo `identifier_exists=false` como default.
- Próximo caminho útil: usar os GTINs já observados no próprio GMC para reconciliar Shopify/online/local por SKU quando houver equivalência segura — mas isso precisa cuidado porque alguns GTINs parecem repetidos por style/grade e não podem ser propagados automaticamente para tamanhos diferentes sem validação.

## Arquivos

- `gmc_nike_mind_direct_items.json`
- `gmc_nike_mind_direct_items.csv`
- `gmc_nike_mind_gtin_by_style_observed.json`

## Próxima ação recomendada

Gerar pacote de reconciliação **GMC → Shopify/Tiny** somente para casos em que o GTIN já existe no próprio GMC no mesmo `offerId/SKU` ou variante equivalente inequívoca. Não aplicar nada automaticamente.
