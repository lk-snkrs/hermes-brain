# Receipt — LKGOC Puma Speedcat como clone/adaptação 204L

Data: 2026-06-09
Tema: `lk-new-theme/dev`
Theme ID: `155065450718`
Role: `unpublished`

## Correção solicitada por Lucas
Lucas apontou que a execução correta não era criar arquitetura/template novo, mas aplicar na coleção Puma Speedcat o padrão Shopify/LKGOC já feito para New Balance 204L e depois trocar texto/imagens.

## O que foi corrigido
- A coleção existente `puma-speedcat` foi mantida como alvo.
- `templates/collection.puma-speedcat.json` no DEV foi corrigido para ser cópia exata do template base usado pela 204L (`templates/collection.json`).
- A diferença `lkgoc_template_mode: true` foi removida do template específico.
- O bloco Speedcat no snippet foi reestilizado para herdar o comportamento visual escuro do padrão 204L:
  - fundo `#101010`;
  - texto claro;
  - banner alinhado ao shell escuro;
  - collage/altura/spacing compatíveis com 204L;
  - classe de compatibilidade `lk-204l-coll-preview` adicionada ao bloco Speedcat.
- Conteúdo/imagens foram mantidos como adaptação da Puma Speedcat.

## O que NÃO foi feito
- Nenhuma alteração em Production.
- Nenhuma publicação de página Guia LK.
- Nenhum write em tema main.
- Nenhuma alteração administrativa global da coleção sem aprovação.

## Estado Shopify verificado
- Production theme `lk-new-theme/production` role `main`: não alterado.
- DEV theme `lk-new-theme/dev` role `unpublished`: alterado.
- Coleção real `puma-speedcat` já tinha `template_suffix: puma-speedcat`.
- Production não possui asset `templates/collection.puma-speedcat.json`; live continua 200 e sem Liquid error.

## QA pós-correção
- Speedcat DEV mobile: `roleUnpublished:true`, `liquid:false`, `hero:true`, `guide:true`, `productLinks:13`, `visibleBad:false`.
- Speedcat DEV desktop: `roleUnpublished:true`, `liquid:false`, `hero:true`, `guide:true`, `productLinks:13`, `visibleBad:false`.
- Readback DEV: `Liquid error 0`; `lk-204l-coll-preview lk-goc-coll-preview--speedcat` presente; `lk-guia-puma-speedcat` presente.

## Evidências
- Preview: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`
- Screenshot mobile: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-mobile-20260609.png`
- Screenshot desktop: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-desktop-20260609.png`

## Regra consolidada
LKGOC para próxima coleção: usar a coleção existente, aplicar/clonar o padrão Shopify aprovado da 204L e adaptar apenas conteúdo, imagens, links, FAQ e nuances comerciais. Não criar arquitetura paralela sem aprovação explícita.
