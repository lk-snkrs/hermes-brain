# Receipt — LKGOC NB 204L Guia LK: correção galeria para ON FEET

Data: 2026-06-09
Tema: `155065450718` / `lk-new-theme/dev`
Role verificado por API: `unpublished`
Escopo: preview DEV da página `/pages/new-balance-204l-original-brasil-guia-lk`

## Motivo
Lucas apontou que a maioria das imagens adicionadas eram fotos de produto e não faziam sentido para o bloco editorial. Direção correta: imagens **on feet**.

## Ação executada
- Removi da galeria editorial os cards com imagens estáticas de produto/colorway.
- Mantive fotos de produto apenas nos cards comerciais de compra.
- Reconfigurei a galeria para 10 cards com foco em uso real/campanha/on feet.
- Novo título: `New Balance 204L on feet: como o tênis aparece no uso real`.
- Novo intro explica que fotos estáticas ficam nos cards de compra e a galeria é para proporção, volume, queda da calça e leitura fashion no corpo.

## QA executado
- Preview DEV verificado:
  - `role_unpublished=True`
  - `Liquid error=False`
  - `img_total=24`
  - termos antigos de produto removidos da galeria: `Sea Salt Linen=False`, `Mushroom em outra leitura=False`
- Playwright QA:
  - mobile: `liquid=0`, `image_cards=10`, título visível;
  - desktop: `liquid=0`, `image_cards=10`, título visível.

## Evidências locais
- HTML verificado: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-on-feet-verified.html`
- Screenshot mobile: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-on-feet-mobile-20260609.png`
- Screenshot desktop: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-on-feet-desktop-20260609.png`
- Backup local antes da correção: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/templates__page.nb204l-guide.before-on-feet-fix.json`

## Produção
Nenhuma alteração em Production. Merge/publicação depende de aprovação explícita de Lucas.
