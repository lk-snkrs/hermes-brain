# Receipt — Salomon XT-6 LKGOC rebase para Gold Source 204L

Data UTC: 20260615T184630Z

## Motivo
Lucas rejeitou o padrão anterior do final da coleção: visual diferente do LKGOC/Gold Source 204L.

## Correção executada
- Removida ponte improvisada `lk-goc-salomon-final-guide` da section e do footer JS.
- Coleção `salomon-xt-6` restaurada para `template_suffix: ""`, mesmo caminho base da 204L.
- Criado snippet `snippets/lk-goc-salomon-xt6-guide-panel.liquid` copiando o contrato visual do guide panel 204L.
- Render adicionado no ponto canônico pós-grid da `sections/lk-collection.liquid`:
  - `collection.handle == 'salomon-xt-6'`
  - `{% render 'lk-goc-salomon-xt6-guide-panel' %}`
- Patch aplicado em Production/main `155065417950` e DEV/unpublished `155065450718`.

## Validação pública
Link validado estável:
https://lksneakers.com.br/collections/salomon-xt-6?page=1

5/5 requests:
- `id="lk-guia-salomon-xt6"`: 1
- `lk-goc-salomon-final-guide`: 0
- `lk-goc-coll-preview--salomon-xt6`: 1
- link `/pages/guia-salomon-xt-6`: presente
- ordem DOM aproximada: hero < último produto < guide = OK

Link alternativo validado:
https://lksneakers.com.br/collections/salomon-xt-6?sort_by=manual

## Observação
URL limpa ainda pode ter cache antigo em alguns shards Shopify, mas os caminhos públicos com parâmetro já renderizam o padrão correto e sem a ponte rejeitada.
