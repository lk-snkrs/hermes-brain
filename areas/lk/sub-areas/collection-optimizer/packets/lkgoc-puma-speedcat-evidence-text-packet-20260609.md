# LKGOC Packet — Puma Speedcat coleção + Guia LK

Status: DEV PREVIEW / NÃO PRODUCTION  
Owner: `[LK] Otimização de Coleções`  
Data: 2026-06-09

## Escopo
Criar LKGOC para:
- Collection: `/collections/puma-speedcat`
- Guia LK page: `/pages/guia-puma-speedcat`

## Evidence de demanda
DataForSEO Brasil / Google:
- `puma speedcat`: volume 18.100; intenção principal transacional; tendência trimestral +83; meses recentes 27.100 buscas em mar/abr 2026.
- `puma speedcat feminino`: volume 480; intenção transacional.
- `puma speedcat vermelho`: volume 480; intenção transacional.
- `puma speedcat preto`: volume 210; intenção transacional.
- `puma speedcat masculino`: volume 140; intenção transacional.
- `puma speedcat brasil`: volume 10; intenção transacional, mas útil para bloco de compra/original no Brasil.

SERP mobile para `puma speedcat original brasil`:
- AI Overview aparece no topo.
- Popular Products ocupa posição alta com forte presença de PUMA Brasil, Authentic Feet, Netshoes e sellers.
- PAA observadas: original/falso, conforto, modelos de Speedcat, origem do Puma Speedcat.
- Players orgânicos: PUMA Brasil, Loja Virus, Your ID, Authentic Feet, Netshoes.

Sinais editoriais internacionais:
- Highsnobiety: Speedcat como sneaker em alta.
- Vogue: Speedcat como parte do uniforme urbano/cool girl.
- PUMA Newsroom: campanhas com Dua Lipa.
- Teen Vogue: Rosé e Speedcat como it sneaker.

## Diagnóstico da coleção atual
A descrição atual da collection tinha boa intenção, mas usava linguagem não alinhada ao guardrail LK, incluindo:
- entrega rápida;
- estoque disponível;
- tamanhos menores saindo rápido;
- preço/faixa como promessa pública.

No DEV LKGOC, a descrição visível foi substituída pelo shell editorial, mantendo produto-first e escondendo a descrição antiga na experiência renderizada. Não foi alterado conteúdo administrativo da collection em Production.

## Lógica textual aprovada para DEV
- Posicionamento: motorsport baixo, leitura fashion.
- Entidade principal: Puma Speedcat.
- Clusters: original, feminino, masculino, vermelho, preto, conforto, forma, OG, Faded, Archive, Brasil.
- CTA: coleção e Guia LK.
- Tom: premium, humano, sem marketplace, sem pronta entrega/estoque como gatilho.

## Estrutura Collection LKGOC
- Hero editorial no padrão 204L.
- Mobile product-first com teaser curto e botão Ler mais.
- Grid nativo completo.
- Guia pós-grid depois do último produto.
- FAQ/schema curto na collection.

## Estrutura Guia LK Page
- Template DEV criado: `templates/page.guia-puma-speedcat-lkgoc.json`.
- Usa `sections/lk-goc-guide-v1.liquid`.
- 47 blocos: resumo, tabela, styling, sinais editoriais, produtos, comparação, imagens e FAQ.
- Página administrativa existente está unpublished; template_suffix atualizado para `guia-puma-speedcat-lkgoc` sem publicar.

## Bloqueio atual da página
A página `/pages/guia-puma-speedcat` está `published_at=null`. Por isso, o preview público retorna 404 mesmo com o tema DEV. Publicar a página é customer-facing e exige aprovação explícita de Lucas.
