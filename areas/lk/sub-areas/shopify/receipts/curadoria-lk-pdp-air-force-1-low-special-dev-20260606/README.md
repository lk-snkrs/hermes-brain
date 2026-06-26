# Receipt — Curadoria LK PDP: Nike Air Force 1 Low Special/Collabs — DEV

Data: 2026-06-06 13:53–13:56 UTC  
Aprovação Lucas: “Aprovo DEV Air Force 1 Low Special”  
Escopo aprovado: write somente no tema DEV/unpublished para adicionar grupo de Curadoria LK PDP.

## Mudança executada

Tema DEV/unpublished: `155065450718`  
Asset: `snippets/lk-variante-top30-visited-v2.liquid`  
Marker adicionado: `top30-nike-air-force-1-low-special`  
Nome interno: `Nike Air Force 1 Low special/collabs`

Itens adicionados:

- `tenis-nike-air-force-1-low-x-supreme-black-preto` — `Supreme Black`
- `supreme-x-nike-air-force-1-low-box-logo-white` — `Supreme White`
- `ambush-x-nike-air-force-1-low-black` — `Ambush Black`
- `ambush-x-nike-air-force-1-low-phantom` — `Ambush Phantom`
- `ambush-x-nike-air-force-1-low-game-royal-and-vivid-sulphur` — `Ambush Game Royal`
- `tiffany-co-x-nike-air-force-1-low-1837` — `Tiffany 1837`
- `off-white-x-nike-air-force-1-low-green-brooklyn` — `Off-White Brooklyn`

## Backup/readback

Readback DEV antes do write:

- Bytes: `209922`
- SHA256: `4b0835bf2d5b12928aebc9a6a71733d86909bb7971a4cfc00a22ef28fcbb3a3f`
- Marker AF1 Special antes: `0`
- Backup/readback local: `/opt/data/tmp/lk-dev-before-af1-special.liquid`
- Receipt run dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-force-1-low-special-dev-20260606/20260606T135324Z/`

Readback DEV após polling:

- Bytes: `211559`
- SHA256: `5ade88a839deb895d031a90ee96feba1757e8783d4d4a91886e097ecbcc0f78b`
- Equals expected candidate: `true`
- Marker AF1 Special após: `1`

Observação: o primeiro readback imediato do script de PUT veio stale (`ok:false`, SHA antigo), padrão já conhecido do Shopify Asset API. O polling seguinte no Asset API retornou o source esperado na primeira tentativa.

## QA estático

Resultado: passou.

- Arrays `lk_top30_markers`, `lk_top30_names`, `lk_top30_handles_groups`, `lk_top30_labels_groups`, `lk_top30_images_groups`: todos com `29` grupos.
- Grupo AF1 Special: `7` handles, `7` labels, `7` imagens.
- Marker count: `1`.
- Sem handles duplicados.
- Sem URL malformada `https:https://` / `https://https://`.
- Sem placeholder `TenisMoldeLK` no grupo.
- Simulação de exclusão do produto atual: todos os 7 handles renderizam 5 cards e excluem o próprio produto.

Arquivo QA estático: `/opt/data/tmp/lk_af1_special_static_qa.json`

## QA visual DEV via CDP

CDP/preview validado em 3 PDPs do grupo. Em todos:

- bloco presente;
- marker `top30-nike-air-force-1-low-special`;
- `railDisplay: grid`;
- `cardCount: 5`;
- produto atual excluído;
- labels visíveis com `span font-weight:300` e `::after font-weight:300`.

Amostras:

1. `tenis-nike-air-force-1-low-x-supreme-black-preto`
   - labels renderizadas: `Supreme White`, `Ambush Black`, `Ambush Phantom`, `Ambush Game Royal`, `Tiffany 1837`
2. `ambush-x-nike-air-force-1-low-black`
   - labels renderizadas: `Supreme Black`, `Supreme White`, `Ambush Phantom`, `Ambush Game Royal`, `Tiffany 1837`
3. `tiffany-co-x-nike-air-force-1-low-1837`
   - labels renderizadas: `Supreme Black`, `Supreme White`, `Ambush Black`, `Ambush Phantom`, `Ambush Game Royal`

Arquivos QA:

- `/opt/data/tmp/af1-qa/tenis-nike-air-force-1-low-x-supreme-black-preto.navigate.json`
- `/opt/data/tmp/af1-qa/ambush-x-nike-air-force-1-low-black.navigate.json`
- `/opt/data/tmp/af1-qa/tiffany-co-x-nike-air-force-1-low-1837.navigate.json`

Caveat: o URL final no CDP removeu `preview_theme_id`, comportamento comum do preview/canonical redirect, mas o marcador novo apareceu apenas porque a sessão navegada estava em contexto de preview. Para segurança, foi feito readback Production separado.

## Verificação de não-impacto em Production

Readback Production/main (`155065417950`) após DEV write:

- Bytes: `209922`
- SHA256: `4b0835bf2d5b12928aebc9a6a71733d86909bb7971a4cfc00a22ef28fcbb3a3f`
- Marker AF1 Special: `0`

Conclusão: Production não foi alterado por este passo DEV.

## Rollback DEV

Restaurar o source anterior do asset DEV usando o backup/readback antes do write:

- `/opt/data/tmp/lk-dev-before-af1-special.liquid`
- ou `before.value` em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-force-1-low-special-dev-20260606/20260606T135324Z/apply/before.value`

## Próxima decisão

Se Lucas aprovar, próximo passo é preparar **merge para Production** via GitHub/PR para persistir o grupo `top30-nike-air-force-1-low-special` no tema Production, com readback Production e QA live público depois do merge.
