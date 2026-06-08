# Approval packet — Curadoria LK PDP Production merge: Adidas Samba OG especiais (2026-06-08)

- values_printed: false
- status: aguardando aprovação explícita de Lucas
- operação proposta: **merge para Production via GitHub PR/production branch**
- direct Shopify Asset API em Production: **não proposto / bloqueado por padrão**
- escopo: somente tema/snippets Curadoria PDP; sem produto, preço, estoque, coleção, app, checkout, ads, email, GMC, Tiny ou Klaviyo.

## Contexto

Após merge Production AJ4, Lucas perguntou para continuar o trabalho de thumbnail PDP. O próximo passo seguro já validado em DEV é levar o batch **Adidas Samba OG especiais / animal print / pony / seasonal** para Production via GitHub.

## Baseline read-only pós-AJ4

Manutenção Curadoria LK PDP forçada/read-only:

- gerado: `2026-06-08 11:37 BRT`
- semáforo: verde `47` · amarelo `11` · vermelho `0` · cinza `3`
- handles públicos checados: `260`
- arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260608T113754-0300.md`
- nenhum write Shopify/DEV/Production executado nessa etapa.

Scan read-only do source Production atual:

- source commit: `782b476`
- active snippet count: `55` markers
- covered handles: `744`
- famílias com oportunidade alta:
  - `adidas-samba-og`: sellable adult `52`, covered `22`, uncovered clean `30`, public-valid sample `12`
  - `air-jordan-1-low`: sellable adult `111`, covered `36`, uncovered clean `75`, public-valid sample `9`
  - `nike-dunk-low`: sellable adult `179`, covered `55`, uncovered clean `124`, public-valid sample `12`

Interpretação: Dunk Low e AJ1 Low continuam maiores, mas mais amplos/misturados. Samba OG especiais é o batch mais controlado porque já está segmentado e validado em DEV.

## DEV proof já executado

Receipt DEV:

- `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-samba-og-specials-20260608T1133BRT.md`

Tema:

- DEV theme: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Production theme: `155065417950` / `lk-new-theme/production` / role `main`

Mudança DEV validada:

- split snippet:
  - `snippets/lk-variante-samba-og-specials-20260608.liquid`
- render line no main:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
- marker:
  - `top30-adidas-samba-og-specials-20260608`

Readback DEV:

- status: `applied`
- Main DEV SHA12 antes: `cee33fcd8aa7`
- Main DEV/readback SHA12: `5631e577112f`
- Split DEV readback SHA12: `57e7cfe630ef`
- render line count: `1`
- static QA: `ok: true`, errors `[]`
- arrays alinhados: handles `10`, labels `10`, images `10`, titles `10`
- simulação: max `5` cards; produto atual excluído.

Preflight DEV:

- Product `.js`: `10/10` HTTP 200 e disponíveis
- imagens: `10/10` HTTP 200 e `image/*`

Caveat preview:

- public preview HTML removeu `preview_theme_id`, então HTML público capturado foi live/canonical.
- classificado como inconclusivo, não falha de source, pois Admin readback + static QA DEV passaram.

Production unchanged durante DEV:

- Production main SHA12 before/after DEV: `0c3e18df0bff`
- Production split `snippets/lk-variante-samba-og-specials-20260608.liquid`: ausente antes/depois.

## Production source atual antes do merge

Checagem read-only em `origin/production` após AJ4:

- source commit: `782b476`
- main SHA12: `0c3e18df0bff`
- Samba render line count: `0`
- Samba split exists: `false`
- marker in split: `false`

## Handles / labels aprovados em DEV

- `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco` — Pony Beige Scarlet
- `tenis-adidas-samba-og-liberty-london-better-scarlet-branco` — Liberty London Scarlet
- `tenis-adidas-samba-og-pony-hair-pack-night-indigo-clear-sky-azul-marinho` — Pony Indigo Sky
- `tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado` — Silver Cracked
- `tenis-adidas-samba-og-cow-print-bege` — Cow Print
- `tenis-adidas-samba-og-marron-sand-strata-pony-vinho` — Sand Strata Pony
- `tenis-adidas-samba-og-collegiate-green-leopard-marrom` — Green Leopard
- `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` — Red Leopard
- `tenis-adidas-samba-og-wonder-white-black-pony-bege` — Pony White Black
- `tenis-adidas-samba-og-year-the-snake-2025-branco` — Year Snake 2025

## Por que esse batch é seguro

- Já passou por DEV/unpublished com Admin readback e static QA.
- É segmentado: Samba OG especiais / animal print / pony / seasonal.
- Não mistura Samba regular, Wales Bonner, Samba Jane ou Sambae.
- Não mexe em preço/estoque/produtos/coleções.
- Production será alterado via GitHub source-of-truth, não via Asset API direto.

## Plano de execução se aprovado

1. Criar branch a partir de `origin/production`.
2. Copiar do readback DEV final apenas o split snippet Samba OG especiais.
3. Adicionar uma única render line no `snippets/lk-variante-top30-visited-v2.liquid`.
4. Rodar static QA local:
   - render line count `1`
   - marker presente
   - 10 handles/labels/images/titles alinhados
   - max 5 cards
   - current product excluded
   - `git diff --check`
5. Abrir PR para `production`.
6. Verificar mergeability/estado do PR.
7. Se limpo, squash merge.
8. Aguardar sync Shopify.
9. Readback Production dos dois assets.
10. QA público em amostras Samba OG especiais com cache-buster.
11. Registrar receipt Brain com PR/merge/readback/rollback.

## Rollback

Preferencial:

1. Reverter o merge commit/PR no GitHub.
2. Aguardar sync Shopify.
3. Readback Production para confirmar:
   - render line ausente;
   - marker ausente;
   - split ausente/zerado conforme revert.

Manual escopado:

1. Remover do main:
   - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
2. Remover/zerar:
   - `snippets/lk-variante-samba-og-specials-20260608.liquid`
3. Merge via GitHub/production branch e readback Shopify.

## Aprovação necessária

Para executar o merge Production via GitHub, Lucas precisa aprovar explicitamente este escopo:

`Aprovo merge Production Samba OG especiais`

Essa frase autoriza somente o PR/merge GitHub para o batch acima. Não autoriza Asset API direto em Production nem outros batches.
