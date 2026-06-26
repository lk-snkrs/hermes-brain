# Approval packet — Curadoria LK PDP Bonés Aimé Leon Dore — DEV

Data: 2026-06-26  
Agente: lk-shopify  
Superfície: Shopify theme DEV/unpublished, PDP `lk-variante`  
Produto âncora: `bone-aime-leon-dore-saint-george-logo-hat-bege-marrom`  
URL: https://lksneakers.com.br/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom

## Pedido

Lucas apontou que o PDP do boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom deve ter bloco **CURADORIA LK / OUTRAS VARIAÇÕES** com outras sugestões de bonés usando a classe/superfície `lk-variante`.

## Status atual read-only

- PDP público HTTP `200`.
- Liquid errors públicos: `0`.
- Não há `data-lk-variante` renderizado para este PDP.
- O HTML público contém classes `lk-variante` apenas por CSS/superfície global, mas não há bloco Curadoria LK ativo para o handle.
- Production theme `155065417950`, `sections/lk-pdp.liquid` SHA12 `68cbf5f7b498`.
- DEV theme `155065450718`, `sections/lk-pdp.liquid` SHA12 `073276393bfe`.
- Ambos renderizam o snippet ativo `lk-variante-top30-visited-v2` e snippets auxiliares.

## Candidatos validados read-only

Todos abaixo deram PDP público `200` e imagem principal CDN `200`. Não foi feita promessa de estoque/disponibilidade.

| Papel | Handle | Label sugerido | Motivo |
|---|---|---|---|
| Âncora | `bone-aime-leon-dore-saint-george-logo-hat-bege-marrom` | Saint George Tanin | produto atual; será excluído dos cards |
| Alternativa 1 | `bone-aime-leon-dore-saint-george-logo-hat-bege-verde` | Saint George Verde | mesma marca + mesmo modelo Saint George |
| Alternativa 2 | `bone-aime-leon-dore-micro-logo-hat-bege-verde` | Micro Logo Verde | mesma marca + boné premium tonal |
| Alternativa 3 | `bone-aime-leon-dore-sun-faded-unisphere-agave-green-verde` | Unisphere Agave | mesma marca + linha Unisphere / lifestyle ALD |
| Alternativa 4 | `bone-5-panel-aime-leon-dore-unisphere-branco` | Unisphere Branco | mesma marca + 5 panel / Unisphere |
| Alternativa 5 | `bone-aime-leon-dore-washed-script-plaza-taupe-bege` | Washed Script Taupe | mesma marca + paleta bege/taupe próxima |

Candidato extra opcional, se Lucas quiser 6 no grupo-fonte para exibir 5 alternativos após exclusão:

- `bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white` — label `Porsche Pristine`; mesma marca/collab ALD, mas um pouco mais cápsula/collab, por isso deixei como extra.

## Design técnico recomendado

DEV/unpublished apenas:

1. Criar snippet novo e isolado:
   - `snippets/lk-variante-bones-ald-20260626.liquid`
2. Adicionar um render line em `sections/lk-pdp.liquid`, próximo aos outros renders Curadoria:
   - `{%- render 'lk-variante-bones-ald-20260626', product: product -%}`
3. Snippet self-contained:
   - carrega `lk-variante.css`;
   - gate por `product.handle` no grupo;
   - exclui o produto atual;
   - usa classes canônicas `.lk-variante`, `.lk-variante__head`, `.lk-variante__rail`, `.lk-variante__media`, `.lk-variante__label`;
   - `data-lk-variante="bones-ald-20260626"`;
   - cap de 5 cards.

## Risco

- Baixo/médio: theme DEV write em Liquid.
- Sem alteração de produto, preço, estoque, checkout, Tiny, GMC, Klaviyo, ads ou campanha.
- Production não entra neste packet.
- Como o DEV já contém o popup Google Reviews ainda não mergeado, o QA desse DEV terá as duas mudanças visíveis; Production merge deve ser tratado separadamente depois.

## Rollback DEV

- Remover render line de `sections/lk-pdp.liquid` no DEV.
- Remover ou ignorar o snippet `snippets/lk-variante-bones-ald-20260626.liquid`.
- Restaurar backup do asset DEV feito antes do upload.

## QA planejado

- Shopify Asset API PUT em DEV somente após aprovação.
- Readback de `sections/lk-pdp.liquid` e do novo snippet.
- Static QA: arrays alinhados, URLs válidas, current product excluído, marker count esperado.
- Public DEV preview:
  - PDP âncora mostra `data-lk-variante="bones-ald-20260626"`;
  - texto `Curadoria LK` e `Outras variações` aparecem;
  - 5 cards renderizam;
  - produto atual não aparece nos cards;
  - sem Liquid errors.

## Aprovação necessária

Para executar em DEV/unpublished, responder:

> Aprovo DEV Curadoria LK bonés ALD no PDP do Saint George Bege/Marrom, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV; se aprovada, aplicar snippet/render em DEV com readback e QA.
- review trigger: resposta do Lucas com aprovação ou ajuste de candidatos.
- evidence: este approval packet + validação pública read-only dos handles/imagens.
