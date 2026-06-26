# Addendum de validação — next20

Data: 2026-05-28

## Correção de leitura do public_ok

Duas coleções apareceram com `public_ok=False` no receipt bruto porque o storefront público omite produtos não disponíveis/ocultos que ainda aparecem no Admin no final do top 8.

Isso não indica falha comercial de ordenação.

## Casos

- Supreme (`supreme`): prefixo vendável público OK. Os 6 primeiros vendáveis do Admin aparecem iguais no público; divergência começa quando o Admin entra em produtos `not_storefront_available_final`.
- Fear of God Essentials (`fear-of-god`): prefixo vendável público OK. Os 7 primeiros vendáveis do Admin aparecem iguais no público; divergência começa quando o Admin entra em produto `not_storefront_available_final`.

## Conclusão

- Admin reorder: OK.
- Vitrine pública para produtos vendáveis: OK.
- Divergência residual: esperada por filtragem/visibilidade do storefront em produtos não disponíveis.

## Não ações

- Nenhum produto, estoque, preço, tag, tema, GMC, checkout ou cron alterado.
