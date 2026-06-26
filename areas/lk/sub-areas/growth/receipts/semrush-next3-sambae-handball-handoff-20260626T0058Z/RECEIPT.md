# Receipt — SEMrush next 3 — Sambae + Handball + Handoff NB740/Gel NYC

Data: 20260626T010009Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu `Aprovo` ao packet `semrush-continue-after-three-collections-20260626`.
values_printed=false

## 1) Adidas Sambae — produção

URL: `/collections/adidas-sambae`
Collection id: `430079344862`

Executado:
- criado/restaurado snippet production ausente: `snippets/lk-sambae-204l-guide.liquid` a partir do DEV validado;
- corrigido Liquid error público `Could not find asset snippets/lk-sambae-204l-guide.liquid`;
- SEO title atualizado para `Adidas Sambae Original Feminino | Curadoria LK`;
- meta description atualizada para `Adidas Sambae original na curadoria LK: plataforma gum, leitura fashion do Samba e atendimento humano para escolher modelo, cor e tamanho.`;
- higienizada description Admin removendo `sob encomenda` e `4 a 6 semanas`;
- FAQPage schema passou a renderizar via guia Sambae.

QA público:
- HTTP 200;
- title/meta novos presentes;
- FAQPage count = 1;
- guia Sambae renderizado;
- sem Liquid error;
- sem `sob encomenda`, `4 a 6 semanas` ou `pronta entrega`.

## 2) Adidas Handball Spezial — produção schema-only

URL: `/collections/adidas-handball-spezial`
Collection id: `445699653854`

Executado:
- adicionado schema-only condicional em `snippets/lk-goc-schema-extra.liquid`;
- sem alteração visual;
- sem alteração de SEO title/meta;
- sem alteração de description visual.

QA público:
- HTTP 200;
- FAQPage count = 1;
- schema `lk-prod-adidas-handball-spezial-faq-schema-20260626` presente;
- sem Liquid error;
- sem termos operacionais antigos.

## 3) Handoff LK Shopify — NB740 + ASICS Gel NYC

Criado card Kanban:
- Board: `lk-growth-ops`
- Task: `t_5db8be73`
- Assignee: `lk-shopify`
- Status: `ready`

Escopo do handoff:
- validar/criar `/collections/new-balance-740` e `/collections/asics-gel-nyc`;
- usar apenas produtos ACTIVE já existentes;
- não consultar/alterar estoque, preço, produtos, checkout, GMC, campanhas ou Klaviyo;
- gerar readback público/receipt Shopify.

## Artefatos

Workdir:
`areas/lk/sub-areas/growth/work/semrush-next3-sambae-handball-handoff-20260626/`

Backups principais:
- `adidas-sambae-admin-before.json`
- `adidas-sambae-description-before.html`
- `adidas-handball-spezial-admin-before.json`
- `prod__snippets__lk-goc-schema-extra-before-handball.liquid`
- `prod__sections__lk-collection.liquid`
- `dev__snippets__lk-sambae-204l-guide.liquid`

Readbacks:
- `adidas-sambae-admin-readback.json`
- `adidas-handball-spezial-admin-readback.json`
- `prod__snippets__lk-sambae-204l-guide.liquid-readback.liquid`
- `prod__snippets__lk-goc-schema-extra.liquid-readback.liquid`

## Non-actions

Não alterado:
- preço;
- estoque/Tiny/inventory;
- produtos;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout.

## Próximo passo

- Aguardar LK Shopify concluir task `t_5db8be73`.
- Após collections NB740/Gel NYC ficarem 200 OK com produtos ativos, Growth prepara guia/FAQ/schema em DEV antes de qualquer produção.
- Medir Sambae/Handball em D+7/D+14 no GSC/SEMrush.
