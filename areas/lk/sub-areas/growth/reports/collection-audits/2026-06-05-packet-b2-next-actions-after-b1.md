# Packet B2 — próximos passos após B1 FAQ/corpo

Data: 2026-06-05

## Estado B1

- B1 aprovado por Lucas e executado em 10 collections.
- Admin readback: 10/10 limpas no `descriptionHtml` para os termos-alvo.
- Public QA após propagação: 8/10 limpas.
- Cache nudge/reaplicação dentro do escopo B1 feito para `nike-todos-os-modelos` e `new-balance-9060`.
- Resultado após nudge: `nike-todos-os-modelos` ficou limpo; `new-balance-9060` ainda renderiza blocos antigos no corpo e meta pública, apesar de Admin SEO/description estar limpo.

## Diagnóstico específico — new-balance-9060

Fatos verificados:

- Shopify Admin `descriptionHtml`: limpo.
- Shopify Admin SEO title/description: limpo.
- Metafields `global.title_tag` e `global.description_tag`: limpos.
- Público ainda mostra:
  - meta antiga: `Pronta entrega`;
  - corpo antigo: `Envio em até 2 dias úteis para produtos em estoque`;
  - FAQ antigo: `roda grande ou pequeno`.
- Busca read-only em assets do tema produção `155065417950` não encontrou os textos antigos exatos.

Interpretação:

- Mais provável: cache/edge/render stale específico da collection NB 9060 ou camada Shopify/theme/app servindo payload antigo.
- Não aplicar novo write amplo antes de nova checagem temporal ou investigação do profile Shopify/theme.

## Packet B2 proposto

Escopo seguro sugerido:

1. Continuar monitoramento público de `new-balance-9060` por janela curta.
2. Se persistir: handoff para LK Shopify/theme investigar origem renderizada.
3. Separado de B1: aprovar B2 para aplicar nas próximas 20–30 collections do lote, **somente descriptionHtml/FAQ**, com a mesma régua de backup/readback/rollback.

## Bloqueios

- Qualquer alteração em theme production para remover frase logística estática exige aprovação separada.
- Qualquer alteração de metafield fora do `descriptionHtml` aprovado exige novo escopo.

## Approval text sugerido — B2 lote seguinte

Aprovo Packet B2 para aplicar a limpeza de linguagem operacional em mais 25 collections priorizadas do lote, alterando somente `descriptionHtml`/FAQ, sem produto, preço, estoque, campanhas, GMC, Klaviyo, checkout ou theme production; com backup, readback público, rollback e revisão D+7.
