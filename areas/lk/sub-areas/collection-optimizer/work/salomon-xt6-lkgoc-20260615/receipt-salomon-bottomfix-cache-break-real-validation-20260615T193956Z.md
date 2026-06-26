# Receipt — Salomon XT-6 bottom fix real validation

Data UTC: 20260615T193956Z

## Correção após feedback Lucas
Lucas reportou que não estava validado visualmente e as imagens não estavam bottom.

## Causa real
- A primeira validação checou HTML, não computed style visual.
- `assets/lk-footer.js` cache-guard ainda reescrevia a terceira imagem para Vogue e não forçava bottom nas imagens 1/2.
- O view `salomon-xt6-golden` podia servir shard/cache antigo.

## Execução
- `sections/lk-collection.liquid`: classes específicas e CSS com `object-position: 50% 100% !important` para img1/img2.
- `assets/lk-footer.js`: removida Vogue do guard, inserido Hypebeast `interview-5.jpg`, e JS setter `img.style.setProperty('object-position','50% 100%','important')` para img1/img2.
- Criado novo template cache-break: `templates/collection.salomon-xt6-bottomfix.json` em Production e DEV.
- Collection `salomon-xt-6` atualizada de `template_suffix=salomon-xt6-golden` para `template_suffix=salomon-xt6-bottomfix`.

## Validação real via Chromium DevTools Protocol
URL validada:
https://lksneakers.com.br/collections/salomon-xt-6?view=salomon-xt6-bottomfix

Desktop computed style:
- img1 Hypebeast interview-1: `object-position = 50% 100%`, `object-fit = cover`, rect `366x450`
- img2 Hypebeast interview-7: `object-position = 50% 100%`, `object-fit = cover`, rect `325x219`
- img3 Hypebeast interview-5: presente
- Vogue antiga: ausente

Screenshot:
`/opt/data/tmp/salomon-xt6-bottomfix-validated.jpg`

## Observação
Clean URL ainda pode ter cache Shopify temporário; o view `salomon-xt6-bottomfix` está validado por browser/render real.
