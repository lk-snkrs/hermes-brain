# Receipt — Salomon XT-6 remover guia antigo + hero editorial

Data UTC: 20260615T190459Z

## Pedido Lucas
Remover bloco antigo:
- Guia rápido Salomon XT-6 — Guia de Compra
- VEJA TAMBEM / Ver Guia LK Salomon XT-6

Substituir 3 imagens do hero por pessoas usando/referências editoriais Vogue/Hypebeast/etc.

## Execução
- Blocos antigos removidos de `templates/collection.lkgoc.json` e `templates/collection.salomon-xt6-lkgoc.json` em Production e DEV.
- Hero Salomon em `sections/lk-collection.liquid` atualizado em Production e DEV.
- Criado template novo `templates/collection.salomon-xt6-golden.json` para bypass de cache antigo.
- Collection `salomon-xt-6` apontada para `template_suffix: salomon-xt6-golden`.
- Cache guard adicionado em `assets/lk-footer.js` para remover bloco antigo caso Shopify sirva HTML stale.

## Imagens novas
- Hypebeast campanha XT-6 — `solomon-beau-beaus-cafe-teoni-atlantic-interview-1.jpg`
- Hypebeast styling urbano — `solomon-beau-beaus-cafe-teoni-atlantic-interview-7.jpg`
- Vogue street style — `NYFW_FW26_STREETSTYLE_DAY5_PHILOH_013.jpg`

## Validação pública funcional
Link validado:
https://lksneakers.com.br/collections/salomon-xt-6?view=salomon-xt6-golden

Resultado:
- bloco antigo: 0
- hero Salomon: presente
- guide panel correto: presente
- 3 imagens editoriais no hero: presentes

## Observação
URL limpa ainda pode receber shards antigos do cache Shopify por alguns minutos; o view `salomon-xt6-golden` está correto e público.
