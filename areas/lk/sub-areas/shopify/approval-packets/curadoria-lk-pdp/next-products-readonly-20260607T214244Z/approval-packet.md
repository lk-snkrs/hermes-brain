# Approval packet — Curadoria LK PDP próximos produtos

Data UTC: 20260607T214244Z

## Escopo read-only
- Fonte: Shopify Admin read-only + GitHub `origin/production` + storefront público `.js`.
- Nenhum Shopify/theme write executado.
- Próximo passo sugerido: DEV/unpublished theme somente após aprovação explícita.

## Baseline
- Produtos totais no Admin: 2331
- Produtos sellable/publicados considerados: 1681
- Production/GitHub snippets renderizados: lk-variante-cortez-speedcat-20260607, lk-variante-onitsuka-versace-gazelle-collabs-20260607, lk-variante-top30-visited-v2
- Production/GitHub grupos parseados: 70
- Production/GitHub handles já cobertos pela Curadoria: 555
- DEV target: `lk-new-theme/dev` / `155065450718` / role `unpublished`
- DEV snippets renderizados: lk-variante-cortez-speedcat-20260607, lk-variante-onitsuka-versace-gazelle-collabs-20260607, lk-variante-top30-visited-v2
- DEV SHA12 atual `lk-variante-top30-visited-v2`: `aba2ed49b088`
- Marcadores selecionados já existem no DEV: ASICS GT-2160 = `false`; Wales Bonner Samba = `false`

## Recomendação de batch DEV
1. `top30-asics-gt-2160-regular` — ASICS GT-2160
   - Grupo novo: True
   - Família sellable: 6; já cobertos: 0; uncovered: 6; públicos/available validados: 6
   - Handles recomendados:
     - `tenis-asics-gt-2160-x-above-the-clouds-white-pure-silver-branco` — Asics GT-2160 x Above the Clouds White Pur
     - `tenis-asics-gt-2160-white-putty-branco` — Asics GT-2160 White Putty Branco
     - `tenis-asics-gt-2160-x-kith-marvel-villains-spider-man-venom-colorido` — Asics GT-2160 x Kith Marvel Villains Spide
     - `tenis-asics-gt-2160-x-gallery-dept-complexcon-cinza` — Asics GT-2160 x Gallery Dept. ComplexCon C
     - `tenis-asics-gt-2160-x-papergirl-beams-white-silver-branco` — Asics GT-2160 x PaperGirl Beams White Silv
     - `tenis-asics-gt-2160-x-jjjound-white-branco` — Asics GT-2160 x JJJJound White Branco
2. `top30-adidas-wales-bonner-samba` — Adidas Samba Wales Bonner
   - Grupo novo: True
   - Família sellable: 3; já cobertos: 0; uncovered: 3; públicos/available validados: 3
   - Handles recomendados:
     - `tenis-adidas-samba-x-wales-bonner-wonder-clay-royal-bege` — adidas Samba x Wales Bonner Wonder Clay Ro
     - `tenis-adidas-samba-x-wales-bonner-collegiate-navy-wonder-white-azul-marinho` — Adidas Samba x Wales Bonner Collegiate Nav
     - `tenis-adidas-samba-x-wales-bonner-wonder-white-marrom` — adidas Samba x Wales Bonner Wonder White M

## Risco
- Baixo em DEV se aplicado como snippet/marker novo e validado com readback/static QA.
- Não misturar collabs/cápsulas com linhas regulares se houver ambiguidade.
- Production continua bloqueado: caminho correto é GitHub PR/branch `production` depois do DEV validado.

## Rollback DEV
- Backup do snippet antes do PUT; rollback restaurando backup no theme DEV.

## Aprovação necessária
Para aplicar somente no DEV/unpublished theme, responder:

`Aprovo DEV Curadoria próximos produtos`

Isso não aprova Production/merge/deploy.
