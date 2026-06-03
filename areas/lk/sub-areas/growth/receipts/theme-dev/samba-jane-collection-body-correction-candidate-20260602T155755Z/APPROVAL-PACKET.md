# Approval packet — corrigir body_html da coleção Adidas Samba Jane

Data: 2026-06-02T15:57:55.599352+00:00

## Escopo
Coleção: `/collections/adidas-samba-jane`
Collection ID: `448218071262`
Campo Shopify: `body_html`

## Problema encontrado
O body_html atual ainda contém:
- FAQ legado em `<dl>` dentro da descrição da coleção;
- bloco operacional de loja misturado ao SEO;
- termo operacional proibido para taxonomia pública (`estoque`);
- copy longa antiga que conflita com o padrão LKGOC atual.

Isso explica por que a URL limpa/cache pode voltar a mostrar a coleção errada mesmo com o section render novo já correto.

## Mudança proposta
Substituir o body_html por 3 parágrafos LKGOC:
- definição clara do Adidas Samba Jane;
- leitura de material/cor/styling;
- curadoria LK + CTA textual para Guia LK dedicado.

## Não mexe em
- produtos da coleção;
- regras/sort order;
- template_suffix `samba-jane-lkgoc`;
- theme asset;
- preço/estoque/campanhas.

## QA local
- FAQ legado removido: `True` → `False`
- Termos proibidos no candidato: `{'pronta entrega': 0, 'encomenda': 0, 'estoque': 0, 'envio em até': 0, 'prazo de entrega': 0}`
- Guia LK citado: `True`

## Arquivos
- Antes: `receipts/theme-dev/samba-jane-collection-body-correction-candidate-20260602T155755Z/collection.body_html.before.html`
- Candidato: `receipts/theme-dev/samba-jane-collection-body-correction-candidate-20260602T155755Z/collection.body_html.candidate.html`
- Estado: `receipts/theme-dev/samba-jane-collection-body-correction-candidate-20260602T155755Z/STATE.json`

## Rollback
Reaplicar `receipts/theme-dev/samba-jane-collection-body-correction-candidate-20260602T155755Z/collection.body_html.before.html` no `body_html` da coleção.

## Aprovação necessária
Write em Shopify production/collection visível. Frase sugerida:
“aprovado corrigir body_html da coleção Samba Jane em production”
