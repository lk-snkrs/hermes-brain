# Curadoria LK — Batch 5 Dev preview / approval packet Production

## Status

Batch 5 aplicado apenas no Dev theme.

- Dev theme ID: `155065450718`
- Production theme ID: `155065417950`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Production unchanged: true
- Dev readback: match

## Grupos no Batch 5

1. Reparo/ativação Adidas Gazelle Indoor regular — novos handles
   - Marker: `top30-adidas-gazelle-active-regular`
   - Produtos no grupo: 8
   - Motivo: Gazelle antigo já renderiza para handles cobertos; o handle comercial `tenis-adidas-gazelle-indor-active-marron-vermelho` estava sem bloco live.

2. Air Jordan 1 High regular
   - Marker: `top30-air-jordan-1-high-regular`
   - Produtos no grupo: 8

3. Nike Shox TL regular
   - Marker: `top30-nike-shox-tl-regular`
   - Produtos no grupo: 7

4. ASICS Gel-1130 regular
   - Marker: `top30-asics-gel-1130-regular`
   - Produtos no grupo: 6

5. Yeezy Foam Runner regular
   - Marker: `top30-yeezy-foam-runner-regular`
   - Produtos no grupo: 6

## Bloqueado / não incluído

Yeezy Slide não foi incluído porque só há 5 produtos ativos/disponíveis encontrados no catálogo. Com o produto atual excluído, o bloco renderizaria apenas 4 alternativas, violando a regra de 5 cards.

## QA Dev

Arquivos de evidência:

- `dev-upload-readback-report.json`
- `dev-sanitize-readback-report.json`
- `dev-static-qa-batch5.json`
- `dev-preview-qa-batch5.json`

Resultado:

- API readback Dev bate com upload: pass
- Production unchanged: pass
- Markers Batch 5 presentes no Dev: 5/5
- Sanitização de aspas em string Liquid: pass
- Balanceamento básico Liquid `for/if`: pass
- Simulação por grupo: 5 cards, current product excluído, URLs de imagem Shopify válidas: pass

Observação: preview público com `preview_theme_id` foi derrubado/servido como live em parte dos testes, comportamento já conhecido em Dev theme; por isso a evidência principal do Dev é Asset API readback + QA estático do Liquid.

## Risco

- Baixo/médio: mudança de tema PDP, visual/CRO. Não altera produto, preço, estoque ou checkout.
- ASICS Gel-1130 tem handles duplicados por cor/título com sufixo `-1`; mantidos porque são PDPs ativos separados, mas pode gerar labels parecidos.
- Gazelle usa grupo separado para novos handles para evitar duplicar o bloco nos handles antigos já cobertos pelo legado.

## Rollback

Para rollback de Dev: re-upar `dev_before_batch5.liquid` para o mesmo asset no Dev theme.

Para Production, antes de promover, criar backup do Production asset atual e promover Dev→Production com readback.

## Próxima decisão

Se aprovado, executar promoção Dev→Production do mesmo asset Dev do Batch 5:

`Aprovado subir Batch 5 Curadoria LK para Production`.

Escopo da aprovação: somente `snippets/lk-variante-top30-visited.liquid` no Production theme. Sem produto, preço, estoque, checkout, apps, GMC/feed, Klaviyo/Meta/Tiny ou campanha.
