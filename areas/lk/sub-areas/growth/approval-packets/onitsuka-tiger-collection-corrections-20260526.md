# Approval packet — Onitsuka Tiger Mexico 66 collection corrections

Destino: LK Shopify dev theme / coleção Onitsuka Tiger Mexico 66

## Pedido limpo

1. Remover o bloco/frase `Sinal editorial` da coleção.
2. Criar um guia editorial completo separado para ser acessado via link na coleção.
3. Ajustar a parte superior da coleção para incluir descrição + fotos/moodboard, pois o topo atual está apenas textual.

## Evidências read-only verificadas

- URL verificada: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718`
- Preview dev renderiza a seção pós-grid com id `lk-guia-onitsuka-tiger-mexico-66`.
- Texto `Sinal editorial` ainda aparece no DOM.
- Topo da coleção tem H1 + parágrafo + `LER MAIS +`, mas não tem imagem/moodboard no bloco superior.
- Captura visual local: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_a6a2e79eaea0450ea508f6c60cdc401b.png`

## Preview proposto

### Coleção

- Manter produtos primeiro.
- Remover o panel `Sinal editorial`.
- Substituir o guia longo pós-grid por um bloco mais curto com link discreto: `Abrir guia completo`.
- Link alvo planejado: `/pages/guia-onitsuka-tiger-mexico-66`.
- Ajustar topo com descrição + fotos/moodboard, sem duplicar H1 e sem empurrar demais o grid no mobile.

### Guia editorial

Rascunho interno criado em:

`areas/lk/sub-areas/growth/drafts/guias-editoriais/guia-onitsuka-tiger-mexico-66-20260526.md`

Inclui:

- H1;
- title/meta sugeridos;
- bloco citável;
- explicação Mexico 66 vs SD vs Sabot vs Slip-on;
- seção material/cor/proporção;
- FAQ visível planejada para FAQPage schema.

## Risco

- Baixo em dev theme se aplicado apenas no tema `lk-new-theme/dev`.
- Médio se criar Page Shopify publicada, porque `/pages/guia-onitsuka-tiger-mexico-66` ficaria publicamente acessível; ideal publicar primeiro como página/preview controlado ou só após aprovação.
- Topo com imagens precisa usar asset LK-owned ou referência com direito claro antes de produção.

## Bloqueios

- Sem write Shopify executado neste turno por boundary de aprovação/roteamento.
- Falta escolher/validar imagens do topo/moodboard.
- Falta aprovação explícita para criar/publicar página Shopify real ou alterar produção.

## Rollback

- Para dev theme: restaurar `sections/lk-collection.liquid` a partir do snapshot anterior em `areas/lk/sub-areas/growth/receipts/theme-dev/dev-phase1-onitsuka-samba-guides-20260526-013141/sections__lk-collection.before.liquid` ou do novo backup a ser gerado antes do patch.
- Para Page Shopify, se aprovada: backup do Page JSON/body/template antes de qualquer alteração e reversão por Admin API.

## Decisão recomendada

Aprovar um patch somente no dev theme para:

1. remover `Sinal editorial`;
2. trocar o guia longo da coleção por CTA/link para guia completo;
3. ajustar o topo com bloco imagem + descrição usando assets LK-owned.

Produção e Page pública ficam para aprovação separada após preview visual.
