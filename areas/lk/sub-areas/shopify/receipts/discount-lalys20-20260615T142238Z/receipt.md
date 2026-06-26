# Receipt — Shopify discount LALYS20

- Data UTC: 2026-06-15T14:22:38Z
- Agente: lk-shopify
- Pedido/aprovação: Lucas pediu criar cupom `LALYS20` para `lalys_andrade@hotmail.com`: 20%, uso único, apenas para essa cliente.
- Classificação: external-write / Shopify discount create.

## Feito

- Criado cupom Shopify `LALYS20`.
- Desconto: 20% (`value_type=percentage`, `value=-20.0`).
- Uso único global: `usage_limit=1`.
- Uma vez por cliente: `once_per_customer=true`.
- Restrição de cliente: `customer_selection=prerequisite` com apenas o customer ID resolvido para `lalys_andrade@hotmail.com`.
- Escopo de itens: todos os line items.
- Sem data final: `ends_at=null`.

## Readback / verificação

- `code_matches=true`
- `price_rule_id_matches=true`
- `percentage_20=true`
- `usage_limit_1=true`
- `once_per_customer_true=true`
- `customer_selection_prerequisite=true`
- `only_target_customer=true`
- `target_all_line_items=true`
- `values_printed=false`

## IDs operacionais

- Price rule ID: `1680377184478`
- Discount code ID: `19984397140190`
- Customer GID: `gid://shopify/Customer/9606447038686`

## Non-actions

- Nenhum envio por Klaviyo, WhatsApp, e-mail ou campanha.
- Nenhuma alteração de produto, preço, estoque, tema, checkout ou coleção.
- Nenhum token/secret impresso.

## Rollback

Se Lucas pedir rollback, excluir/desativar o desconto/price rule `1680377184478` ou o discount code `19984397140190` no Shopify Discounts.

## Artefatos

- `receipt.json` no mesmo diretório contém o readback estruturado.
