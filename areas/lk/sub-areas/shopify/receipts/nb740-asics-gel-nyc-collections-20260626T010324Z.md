# Receipt — LK Shopify — collections canônicas NB740 + ASICS Gel NYC

Data: 20260626T010324Z
Origem: `lk-shopify` via Kanban `t_5db8be73`.
Status: **ASICS Gel NYC criada/ativada e validada; New Balance 740 bloqueada por ausência de produto ACTIVE correspondente**.

## Pedido aprovado

Validar/criar superfícies canônicas Shopify:
- `/collections/new-balance-740`
- `/collections/asics-gel-nyc`

Escopo aprovado pelo handoff: usar apenas produtos `ACTIVE` já existentes no Shopify que correspondam claramente aos modelos, sem consultar/alterar estoque, Tiny, inventory, preço, produtos, checkout, GMC, campanhas ou Klaviyo; fazer readback público HTTP 200; registrar receipt.

## Evidência live Shopify/Admin

Fonte: Shopify Admin API via Doppler profile `lk-shopify`; `values_printed=false`; smoke `shopify_lk` HTTP 200.

### ASICS Gel NYC

Antes:
- `collectionByHandle(asics-gel-nyc)`: ausente.
- Produto ACTIVE correspondente encontrado: `tenis-asics-gel-nyc-graphite-grey-black-preto`.
- Produto relacionado `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` apareceu como `ARCHIVED`, portanto ficou fora do escopo.

Feito:
- Criada custom collection Shopify:
  - Title: `ASICS Gel NYC`
  - Handle: `asics-gel-nyc`
  - GID: `gid://shopify/Collection/1128952955102`
  - Legacy ID: `1128952955102`
- Vinculado somente 1 produto ACTIVE:
  1. `tenis-asics-gel-nyc-graphite-grey-black-preto`

Readback público:
- URL: `https://lksneakers.com.br/collections/asics-gel-nyc`
- HTTP: `200 OK`
- Title tag: `ASICS Gel NYC: 1 modelos | LK Sneakers`
- H1 presente: sim.
- HTML contém o handle esperado: sim.

### New Balance 740

Antes/readback:
- `collectionByHandle(new-balance-740)`: ausente.
- Busca live por `740`, `New Balance 740`, `vendor:New Balance 740` e `U740GP2` encontrou apenas o produto `tenis-new-balance-740-x-concepts-saignee-verde` como `ARCHIVED`.
- Nenhum produto `ACTIVE` correspondente a New Balance 740 foi encontrado.

Decisão operacional:
- Não foi criada collection vazia em `/collections/new-balance-740`, porque o handoff autorizava usar apenas produtos ACTIVE existentes e o próximo passo de Growth depende de superfície 200 OK com produtos ativos.
- Não houve alteração de status de produto nem consulta/promessa de estoque/disponibilidade.

## Artefatos técnicos

- Script de execução/readback: `/opt/data/kanban/boards/lk-growth-ops/workspaces/t_5db8be73/lk_canonical_collections.py`
- Discovery antes: `/opt/data/kanban/boards/lk-growth-ops/workspaces/t_5db8be73/discovery-before.json`
- Resultado apply: `/opt/data/kanban/boards/lk-growth-ops/workspaces/t_5db8be73/apply-result.json`
- Readback final: `/opt/data/kanban/boards/lk-growth-ops/workspaces/t_5db8be73/final-readback.json`

## Guardrails preservados

Não foi consultado/alterado:
- estoque/Tiny/inventory/variants;
- preço;
- status/cadastro de produto;
- checkout;
- GMC/feed;
- Klaviyo/campanhas;
- SEO title/meta ou descrição editorial;
- tema/liquid.

## Writes externos executados

Shopify Admin, dentro do escopo aprovado:
- criação da custom collection `ASICS Gel NYC` (`asics-gel-nyc`);
- criação de 1 collect para o produto ACTIVE `tenis-asics-gel-nyc-graphite-grey-black-preto`.

Nenhum write foi executado para New Balance 740.

## Risco / bloqueio

- ASICS Gel NYC: risco baixo; readback Admin + público 200 OK confirmou a superfície e o produto esperado.
- New Balance 740: bloqueada. Criar a collection agora geraria superfície vazia/sem produto ACTIVE, fora do objetivo aprovado; reativar produto arquivado, cadastrar novo produto ou validar disponibilidade exigem novo escopo/handoff com o dono correto.

## Rollback

Para ASICS Gel NYC, se necessário:
1. remover o collect do produto `tenis-asics-gel-nyc-graphite-grey-black-preto` da collection legacy `1128952955102`;
2. despublicar ou excluir a custom collection `asics-gel-nyc`;
3. validar Admin e público.

Não há rollback de estoque, preço, produto, tema, GMC, Klaviyo, campanhas ou checkout porque essas superfícies não foram alteradas.

## Próximo passo

- `[LK] Growth` pode preparar guia/FAQ/schema DEV para ASICS Gel NYC.
- Para New Balance 740, é necessária decisão/handoff antes de qualquer Shopify write adicional: validar com `lk-stock`/operação se existe produto NB740 publicável/ativo, ou aprovar cadastro/reativação/listagem conforme política própria. Até lá, `/collections/new-balance-740` permanece não criada.

Source confidence: runtime-verificado.
