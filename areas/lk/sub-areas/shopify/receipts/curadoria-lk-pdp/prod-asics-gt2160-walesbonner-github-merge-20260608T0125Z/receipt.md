# Receipt — Production merge Curadoria LK PDP ASICS GT-2160 + Wales Bonner

Data UTC: 2026-06-08T01:25Z

## Escopo
- Aprovação recebida: `Merge`.
- Interpretação: aprovação para o caminho correto de Production via GitHub PR → merge em `production` → sync/deploy Shopify → readback/QA.
- Direct Shopify Asset API write em Production: **não executado**.
- Production theme: `155065417950` (`lk-new-theme/production`, role main observado em baseline anterior).

## GitHub
- Repo: `lk-snkrs/lk-new-theme`.
- Base: `production`.
- Branch: `hermes/curadoria-asics-gt2160-walesbonner-production-20260608`.
- Head commit da branch: `b5c06b4e5e60`.
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/35
- PR mergeable: `true`; mergeable_state: `clean`.
- Merge SHA: `89aad9905885`.
- Branch remota deletada após merge: `true`.

## Mudança mergeada
- Main asset: `snippets/lk-variante-top30-visited-v2.liquid`
  - Adicionado 1 render line para o split snippet.
- Novo split snippet: `snippets/lk-variante-asics-gt2160-walesbonner-20260608.liquid`.
- Grupos:
  - `top30-asics-gt-2160-regular` — ASICS GT-2160.
  - `top30-adidas-wales-bonner-samba` — Adidas Samba Wales Bonner.

## Reconciliation antes do merge
- GitHub `origin/production` main SHA12: `811dbe5bdec7`.
- Shopify Production readback main SHA12: `811dbe5bdec7`.
- Repo igual ao Shopify live antes do patch: `true`.

## Static QA pré-merge
- Main size antes: `259889` bytes.
- Main size depois: `259970` bytes.
- Abaixo do limite Shopify 256 KB: `true`.
- Split size: `6097` bytes.
- Render line count: `1`.
- Marker counts no split:
  - `top30-asics-gt-2160-regular`: `2`.
  - `top30-adidas-wales-bonner-samba`: `2`.
- Malformed URLs: `false`.
- Placeholder images `TenisMoldeLK`: `false`.
- Current-product exclusion guard: `true`.
- Canonical classes (`lk-variante__head`, `lk-variante__rail`, `lk-variante__media`): `true`.

## Shopify Production readback pós-merge/sync
- Sync observado no primeiro polling de readback.
- Main SHA12 Production após sync: `a377c2ca1168`.
- Split SHA12 Production após sync: `be2f6216c380`.
- Main render line count: `1`.
- Split exists: `true`.
- Marker counts no split:
  - `top30-asics-gt-2160-regular`: `2`.
  - `top30-adidas-wales-bonner-samba`: `2`.

## Public QA pós-merge
Primeira amostra teve uma leitura pública parcial/inconsistente para 1 PDP, então rodei retries cache-busted maiores.

Resultado retry 3 rodadas / 4 PDPs:
- `tenis-asics-gt-2160-white-putty-branco`: marker `top30-asics-gt-2160-regular` presente `3/3`.
- `tenis-asics-gt-2160-x-jjjound-white-branco`: marker `top30-asics-gt-2160-regular` presente `3/3`.
- `tenis-adidas-samba-x-wales-bonner-wonder-white-marrom`: marker `top30-adidas-wales-bonner-samba` presente `2/3`; 1ª leitura sem marker, 2ª/3ª OK.
- `tenis-adidas-samba-x-wales-bonner-wonder-clay-royal-bege`: marker `top30-adidas-wales-bonner-samba` presente `3/3`.

Todos os retries retornaram HTTP `200`, sem Cloudflare challenge. Intermitência residual classificada como Shopify edge/cache, não source failure, pois readback/static QA passou.

## Rollback
Caminho correto: reverter o merge/PR no GitHub e deixar o pipeline/sync aplicar de volta no Shopify.

Escopo de rollback:
1. Remover o render line do main asset `snippets/lk-variante-top30-visited-v2.liquid`.
2. Remover o arquivo `snippets/lk-variante-asics-gt2160-walesbonner-20260608.liquid`.
3. Aguardar sync Shopify e validar readback Production.

## Secrets
- GitHub/Shopify credentials carregadas via Doppler em processo curto.
- `values_printed=false`.
- Nenhum token/secret registrado neste receipt.
