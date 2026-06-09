# LK Ecommerce — Mapa

Escopo: Shopify, produtos, pedidos, clientes, Judge.me, Tiny/Frenet quando aplicável. Estoque físico/pronta entrega/best sellers agora pertence ao especialista `lk-stock` em `../stock/`.

Regra: consultar fonte viva antes de responder sobre estoque, preço, pedido ou prazo. Para estoque físico, encaminhar ao `lk-stock`: Tiny / `LK | CONTROLE ESTOQUE` é a verdade.

## Skill canônica

- `skills/lk-shopify-readonly/SKILL.md` — consultas Shopify LK em modo read-only, com Doppler, sem mutations, sem envios e sem tratar estoque Shopify como verdade final.

## Guardrails Shopify

- Shopify é fonte para pedidos, clientes, catálogo e contexto de venda.
- Tiny / `LK | CONTROLE ESTOQUE` é a verdade de estoque.
- Qualquer write em Shopify, alteração de produto/preço/estoque/tag/metafield, tema, app, webhook ou envio ao cliente exige aprovação explícita de Lucas.
