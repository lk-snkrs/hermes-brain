# Correction packet — DEV/branch candidate Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Pedido: Lucas aprovou seguir após QA pós-publicação.  
Escopo executado: preparação local de payload/candidato DEV/branch.  
Writes externos: 0  
Production/main: intocado.

## Status

**Candidato preparado e validado localmente.**

Não apliquei em Shopify porque a política ativa do LKGOC é **GitHub-first / sem writes diretos Shopify Admin API**. Como a correção final toca `collection.descriptionHtml`, ela exige execução por fluxo aprovado/handoff técnico `lk-shopify` ou aprovação de exceção específica.

## Arquivos preparados

| Handle | Arquivo candidato | Objetivo |
|---|---|---|
| `alo-yoga-1` | `collection__alo-yoga-1.descriptionHtml.corrected.html` | Consolidar o LKGOC Lite em um único bloco, sem duplicidade de FAQ/Como escolher. |
| `crocs-mcqueen` | `collection__crocs-mcqueen.descriptionHtml.corrected.html` | Manter guia enxuto pós-grid e remover ruído visual/operacional. |

## QA local do candidato

| Arquivo | H2 | FAQ heading | Perguntas FAQ | Bloco citável | Guia editorial | Termos sensíveis de estoque/prazo |
|---|---:|---:|---:|---:|---:|---:|
| Alo Yoga | 1 | 1 | 4 | 1 | 1 | 0 |
| Crocs McQueen | 1 | 1 | 4 | 1 | 1 | 0 |

## Preview local

- `preview-alo-yoga-1.html`
- `preview-crocs-mcqueen.html`
- `preview-alo-yoga-1-mobile.png`
- `preview-crocs-mcqueen-mobile.png`

Observação: preview local simula o bloco depois de um grid fake. O QA real em Shopify DEV/branch ainda precisa ser feito antes de qualquer production.

## Mudanças de conteúdo

### Alo Yoga

Antes: havia duas camadas editoriais parecidas no público, gerando repetição:

- `Como escolher Alo Yoga`
- `Perguntas frequentes`
- `Como escolher peças Alo Yoga`
- `Perguntas frequentes sobre Alo Yoga`

Candidato: um único bloco com:

- H2 editorial;
- 3 cards de escolha;
- 4 FAQs;
- 1 bloco citável LK.

### Crocs McQueen

Candidato: bloco único e enxuto com:

- H2 editorial;
- 3 cards de escolha;
- 4 FAQs;
- 1 bloco citável LK;
- sem promessa pública de dado operacional.

## Próxima decisão necessária

Para aplicar em ambiente Shopify DEV/branch/readback, existem duas opções seguras:

1. **Handoff para `lk-shopify`** aplicar o payload em DEV/branch/readback seguindo política Shopify; ou
2. Lucas aprovar explicitamente uma **exceção de write Shopify Admin DEV** para `collection.descriptionHtml` desses dois handles, com backup, rollback e readback.

Sem uma dessas aprovações, este agente deve parar no candidato local.

## Frase de aprovação para próxima etapa

> Aprovo acionar `lk-shopify` para aplicar em DEV/branch o payload LKGOC Lite corrigido de `alo-yoga-1` e `crocs-mcqueen`, usando os arquivos do correction packet de 2026-06-25, sem production/main, sem preço, estoque, produtos, ordem, GMC, Klaviyo ou campanhas, com backup, QA mobile/desktop, readback e rollback antes de qualquer promoção.

## Rollback

- Não há rollback externo porque não houve write externo.
- Para descartar o candidato local, arquivar/remover esta pasta de trabalho.
- Para production futura, usar backups do receipt de 2026-06-23 antes de qualquer promoção.
