# Approval packet — Curadoria LK PDP: Samba OG collabs/seasonal II → merge Production

Gerado: 2026-06-08 12:13 BRT

## Pedido limpo

Levar para Production, via GitHub PR para branch `production`, o batch já validado em DEV/unpublished **Adidas Samba OG collabs/seasonal II**.

Este packet **não executa merge**, **não faz write Shopify Production** e **não altera produto/preço/estoque/coleção/app/checkout**.

## Estado read-only atual

- Maintenance read-only: OK.
- Relatório: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260608T121339-0300.md`.
- Semáforo: verde 47 · amarelo 11 · vermelho 0 · cinza 3.
- Handles públicos checados: 260.
- Último source Production confirmado: `origin/production` commit `8d39bf3`.
- Main Production SHA12: `1dd290044fd7`.

## Prova de ausência em Production

Batch ainda **não** está no source Production:

- Render line count no `snippets/lk-variante-top30-visited-v2.liquid`: `0`.
- Split snippet existe em Production: `false`.
- Marker no main/split Production: `false`.
- Marker alvo: `top30-adidas-samba-og-collabs-seasonal-20260608`.

## Evidência DEV já validada

- DEV theme: `155065450718` / `lk-new-theme/dev` / `unpublished`.
- Production theme preservado no apply DEV: `155065417950` / `lk-new-theme/production` / `main`.
- Status DEV: `applied`.
- Receipt DEV: `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-samba-og-collabs-seasonal-20260608T1203BRT.md`.
- Main DEV SHA12 antigo: `5631e577112f`.
- Main DEV SHA12 novo/readback: `5bd5f4143a24`.
- Split DEV SHA12 readback: `50ce9904d609`.
- Production main no apply DEV: `1dd290044fd7` → `1dd290044fd7`.
- Production unchanged no apply DEV: `True`.
- Production split ausente/inalterado no apply DEV: `True`.

## Preflight / static QA DEV

- Product `.js`: 10/10 HTTP 200, `available=true`, `title_ok=true`.
- Image HEAD: 10/10 HTTP 200, `image/jpeg`.
- Static QA: `True`.
- Static errors: `[]`.
- Arrays: `lk_handles=10`, `lk_labels=10`, `lk_images=10`, `lk_titles=10`.
- Simulação: `5` cards; produto atual excluído.
- Preview público DEV: inconclusivo porque `preview_theme_id` foi removido/ignorado em headless; Admin readback + static QA são a evidência primária.

## Escopo exato para Production

Arquivos no repo `lk-snkrs/lk-new-theme`, branch alvo `production`:

1. Criar:
   - `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`
2. Alterar:
   - `snippets/lk-variante-top30-visited-v2.liquid`
3. Inserir uma render line:
   - `{%- render 'lk-variante-samba-og-collabs-seasonal-20260608', product: product -%}`

## Produtos / labels do batch

1. `tenis-adidas-samba-og-x-lionel-messi-triunfo-estelar-pack-branco` — Messi Triunfo
2. `tenis-adidas-samba-og-x-dingyun-zhang-white-vapour-branco` — Dingyun White Vapour
3. `tenis-adidas-samba-og-x-sporty-rich-usa-branco` — Sporty & Rich USA
4. `tenis-adidas-samba-og-dia-de-muertos-pack-black-preto` — Día de Muertos Black
5. `tenis-adidas-samba-og-dia-de-muertos-pack-off-white-branco` — Día de Muertos Off White
6. `tenis-adidas-samba-og-x-naked-consortium-off-white-crystal-white-branco` — Naked Crystal White
7. `tenis-adidas-samba-og-linen-green-metallic-verde` — Linen Green Metallic
8. `tenis-adidas-samba-og-semi-blue-burst-azul` — Semi Blue Burst
9. `tenis-adidas-samba-og-off-white-cyber-metallic-branco` — Cyber Metallic
10. `tenis-adidas-samba-og-cloud-white-rose-tone-branco` — Cloud White Rose

## Por que este é o próximo passo seguro

- O batch já passou por DEV/unpublished com readback e static QA.
- Production ainda não contém esse split/marker.
- É um lote controlado e semântico de Samba OG collabs/seasonal, separado de Samba regular, Wales Bonner, Sambae, Samba Jane e Samba OG especiais/animal print já publicado.
- Evita iniciar outro DEV maior/misto enquanto há um batch DEV pronto e pendente de Production.

## Plano de execução se aprovado

1. Criar branch a partir de `origin/production`.
2. Adicionar o split snippet validado e uma render line no main.
3. Rodar validação estática local: marker, arrays, 5 cards, current excluded, ausência de URLs malformadas.
4. Abrir PR GitHub para `production`.
5. Verificar mergeability/checks.
6. Fazer squash merge se PR estiver clean.
7. Aguardar sync Shopify.
8. Readback Shopify Production do main e split.
9. QA público Production com `view=default`, cache-buster e headers no-cache em amostras/10 handles.
10. Registrar receipt Brain com PR, merge commit, SHAs, QA e rollback.

## Risco

- Risco baixo/médio: adiciona nova Curadoria em PDPs Samba OG selecionados.
- Risco de cache/edge Shopify no QA público inicial; mitigar com retries no-cache.
- Risco de render duplicado baixo, pois o split é guardado por `product.handle` e a saída simula 5 cards.

## Rollback

Preferencial:

- Reverter o merge commit via GitHub PR/revert na branch `production`.

Manual escopado se necessário:

- Remover do main a render line:
  - `{%- render 'lk-variante-samba-og-collabs-seasonal-20260608', product: product -%}`
- Remover/zerar o split snippet:
  - `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`
- Fazer readback Shopify Production + QA público pós-rollback.

## Decisão necessária

Para executar o merge Production via GitHub PR, Lucas deve aprovar explicitamente:

**Aprovo merge Production Samba OG collabs seasonal**
