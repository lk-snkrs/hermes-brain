# Receipt — LK 204L desktop description retune

Data: 2026-05-27
Tema produção: `155065417950` (`lk-new-theme/production`)
Página: `/collections/new-balance-204l`

## Pedido do Lucas
- O título da descrição da coleção ficou pequeno demais.
- Aumentar `CURADORIA LK` em 1pt.
- Ajustar `Perfil baixo, leitura fashion.` para ficar apenas 4pt menor que o padrão anterior.

## Alterações aplicadas
- `CURADORIA LK`: desktop final `10px`.
- `Perfil baixo, leitura fashion.`: desktop final `50px`.
- Mantido `New Balance 204L`: desktop `52px`.
- Mantido espaçamento reduzido entre título da coleção e bloco editorial.

## Assets alterados
- `assets/lk-product-card.css`
- `sections/lk-collection.liquid`
- `layout/theme.liquid`

## Observação técnica
O storefront público estava alternando variantes/cache antigas: a seção ainda servia um bloco antigo com `h2=44px` e `kicker=9px`, e o asset CSS linkado no HTML às vezes vinha com versão antiga. Para garantir aplicação visual imediata, foi adicionado um override final no `layout/theme.liquid` depois de `{{ content_for_layout }}`, com escopo restrito a páginas que possuem `.lk-204l-coll-preview`.

## Backups
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-desktop-description-retune-20260527-152130/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-section-description-retune-20260527-152443/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-layout-final-override-20260527-152644/`

## Verificação final via browser
Viewport: `1280x577`

Computed styles:
- `New Balance 204L`: `52px`, margin-bottom `0px`
- `CURADORIA LK`: `10px`, margin-bottom `10px`
- `Perfil baixo, leitura fashion.`: `50px`, margin-bottom `16px`
- Banner padding-bottom: `18px`
- Preview padding-top: `20px`
- Override final presente no HTML público: sim

## Rollback
Restaurar os arquivos dos backups acima ou remover o bloco `<style id="lk-204l-final-desktop-override">` de `layout/theme.liquid`.
