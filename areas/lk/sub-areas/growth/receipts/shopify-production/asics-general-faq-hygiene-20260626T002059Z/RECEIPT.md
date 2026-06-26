# Receipt — Shopify production — Asics geral FAQ hygiene

Data: 20260626T002059Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu `Aprovo` ao packet `approval-packets/semrush-alo-yoga-and-asics-general-hygiene-20260625/APPROVAL-PACKET.md`.
Collection: `/collections/asics-todos-os-modelos`
Collection legacy id: `458593435870`
values_printed=false

## Escopo aprovado/executado

Aplicada higiene editorial na FAQ de prazo da collection geral Asics, removendo linguagem operacional antiga:
- `sob encomenda`
- `4 a 6 semanas`
- `Frete grátis acima de R$ 499`

Texto antigo:
> O prazo varia conforme a disponibilidade confirmada e a região de entrega. Itens sob encomenda seguem prazo estimado de 4 a 6 semanas. Frete grátis acima de R$ 499.

Texto novo:
> O prazo varia conforme a região e os detalhes do pedido. Quando necessário, o atendimento humano da LK confirma as informações antes da finalização da compra.

## Artefatos

- Admin backup antes: `areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/admin-before.json`
- Description backup antes: `areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/description-before.html`
- Target aplicado: `areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/description-target.html`
- Resposta mutation: `areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/update-response.json`
- Admin readback: `areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/description-readback-admin.html`

## Readback Admin

- `collectionUpdate`: OK.
- `has_sob_encomenda=false`
- `has_4_6=false`
- `has_frete_499=false`
- SEO title/meta preservados:
  - title: `Asics | Todos os Modelos | LK Sneakers`
  - description: `Compre Asics - Todos Os Modelos na LK Sneakers. 100% originais · 10x sem juros · Frete grátis · Loja Jardins SP.`
- productsCount preservado: 17.

## QA público

URL validada:
`https://lksneakers.com.br/collections/asics-todos-os-modelos?cache=false&qa=asics-hygiene-readback`

Resultado:
- HTTP 200.
- Texto novo presente.
- `sob encomenda`: ausente.
- `4 a 6 semanas`: ausente.
- `Frete grátis acima de R$ 499`: ausente.
- `Liquid error=false`.
- Tema production `155065417950`.

## Non-actions confirmadas

Não alterado:
- SEO title/meta;
- handle/canonical;
- produtos;
- preço;
- estoque/Tiny/inventory;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout;
- theme/assets.

Alo Yoga: apenas read-only/diagnóstico; nenhum write novo.

## Rollback

Restaurar o HTML em:
`areas/lk/sub-areas/growth/work/asics-general-hygiene-20260625/description-before.html`

Na collection `gid://shopify/Collection/458593435870`, campo `descriptionHtml`.
