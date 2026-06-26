# Handoff urgente — publicar correções 204L em Shopify Production

Data: 2026-05-27
Origem: Telegram Lucas Cimino
Status: Lucas reiterou: “Publique, pois ainda está antigo”

## Escopo aprovado

Publicar em produção, na coleção:

- URL: https://lksneakers.com.br/collections/new-balance-204l
- Tema esperado: `lk-new-theme/production` / role `main` quando executar via Shopify Admin

Correções exatas:

1. H1 `New Balance 204L`: aumentar fonte em +3pt.
   - Baseline público medido antes: `48px`.
   - Alvo aproximado se a implementação for CSS pixel-equivalente: `52px` ou ajuste equivalente a +3pt conforme stack CSS.
2. Kicker/eyebrow:
   - De: `CURADORIA LK · NEW BALANCE 204L`
   - Para: `CURADORIA LK`
3. Paginação do grid:
   - De: 24 produtos por página.
   - Para: 20 produtos por página.

## Evidência de que ainda está antigo

Nova verificação pública com cachebuster `?hermes_publish_check=20260527b`:

- H1: `New Balance 204L`
- Fonte computada H1: `48px`
- Kicker: `Curadoria LK · New Balance 204L`
- Produto links únicos detectados: 25 via DOM público, compatível com a página ainda renderizando acima do alvo de 20 por página

## Guardrails

- Fazer backup do(s) asset(s)/settings antes do write.
- Patch mínimo; não subir arquivos locais amplos sem comparar com live.
- Não tocar produto, preço, estoque, filtros, ordem comercial, checkout, apps, campanhas, Klaviyo, Meta/Google Ads, GMC ou menus.
- Após write, readback por hash/substrings e QA público com cachebuster.

## QA esperado depois da publicação

- Kicker público deve ser exatamente `CURADORIA LK`, sem `NEW BALANCE 204L`.
- H1 deve estar maior que o baseline de `48px` em aproximadamente +3pt.
- Primeira página deve renderizar 20 produtos por página.
- URL pública sem `preview_theme_id` deve refletir a alteração.

## Rollback

Reaplicar backup do(s) asset(s)/settings anteriores e confirmar retorno para:

- H1 baseline anterior;
- kicker anterior;
- paginação anterior de 24.
