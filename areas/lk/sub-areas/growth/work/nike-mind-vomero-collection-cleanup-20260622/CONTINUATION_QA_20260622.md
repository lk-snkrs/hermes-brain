# Continuação 2026-06-19 → QA pós-cleanup Nike Mind / Vomero

- Criado UTC: 2026-06-22T15:28:45.883041+00:00
- Escopo: read-only public QA após cleanup aplicado em `apply-result.json`.
- Writes externos nesta etapa: 0.
- values_printed=false.

## Veredito

Cleanup de descrição das collections foi aplicado e está público, mas o problema técnico de schema/duplicidade ainda não está totalmente resolvido no render público.

## Evidência pública

| URL | HTTP | H1 | FAQPage público | Conteúdo novo | Liquid error |
|---|---:|---:|---:|---|---|
| `/collections/nike-mind-001` | 200 | 1 | 2 blocos, 4+5 perguntas | presente | false |
| `/pages/guia-nike-mind-001-002` | 200 | 1 | 1 bloco, 8 perguntas | n/a | false |
| `/collections/nike-vomero-premium` | 200 | 1 | 3 strings / 2 blocos parseados, 2+5 perguntas | presente | false |

## Interpretação

- A limpeza aprovada removeu FAQ/copy duplicada do `descriptionHtml` das collections.
- A duplicidade remanescente parece vir de camada de tema/snippet/runtime, não do body admin da página/collection.
- Próximo passo seguro: investigação read-only de assets/snippets que injetam FAQPage nas collections Nike Mind e Vomero; qualquer correção em tema deve seguir DEV/unpublished primeiro e Production só com aprovação explícita.

## Arquivos

- Apply result: `apply-result.json`
- QA JSON: `public-qa-after-continue-20260622T1528Z.json`
