# Receipt — LK Shopify — collection canônica Lululemon Define Jacket

Data: 20260625T200548Z
Origem: `lk-shopify` via Kanban `t_2443c1f6`; receipt consolidado por `[LK] Growth` após worker travar no receipt-writer.
Status: **collection criada/ativada e validada**.

## Pedido aprovado

Criar/validar/ativar a collection canônica Lululemon Define Jacket em `/collections/lululemon-define-jacket`, usando apenas produtos Lululemon Define ACTIVE já existentes, sem consultar/alterar estoque, preço, campanhas, GMC, Klaviyo ou checkout, com readback público.

## Resultado Shopify

- URL: `https://lksneakers.com.br/collections/lululemon-define-jacket`
- Handle: `lululemon-define-jacket`
- Title: `Lululemon Define Jacket`
- GID: `gid://shopify/Collection/1128948367582`
- Legacy ID: `1128948367582`
- Produtos vinculados: 6

Produtos ACTIVE vinculados:

1. `jaqueta-lululemon-define-nulu`
2. `define-cropped-jacket-nulu`
3. `jaqueta-lululemon-define-luon-white-branco`
4. `jaqueta-lululemon-define-nulu-black-plum-gold-roxo`
5. `jaqueta-lululemon-define-nulu-black-gold-preto`
6. `define-jacket-nulu-rose-gold`

## Readback

- Admin `collectionByHandle(lululemon-define-jacket)`: OK.
- Público `/collections/lululemon-define-jacket`: HTTP 200 OK.

## Guardrails preservados

Não foi consultado/alterado:
- estoque/Tiny/inventory/variants;
- preço;
- campanhas;
- GMC;
- Klaviyo;
- checkout;
- SEO title/meta da collection;
- descrição editorial;
- tema.

## Observação sobre Kanban

A task `t_2443c1f6` concluiu o write Shopify e o readback, mas ficou presa ao tentar gerar receipt via `hermes_memory_os_receipt_writer.py` com exit 1. Este receipt consolida a evidência operacional para destravar Growth.

## Rollback

Rollback recomendado:
1. remover os 6 collects da collection `1128948367582`;
2. despublicar ou excluir a custom collection `lululemon-define-jacket`;
3. validar URL pública e Admin.

Como não houve alteração de estoque, preço, SEO, description, tema, GMC, Klaviyo, campanhas ou checkout, não há rollback nessas superfícies.

## Próximo passo

`[LK] Growth` pode preparar guia/FAQ/schema em DEV antes de qualquer produção.
