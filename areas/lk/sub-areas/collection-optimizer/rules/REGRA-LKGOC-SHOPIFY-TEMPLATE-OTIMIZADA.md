# REGRA — LKGOC Shopify template padrão de coleção otimizada

Registrado em: 20260609T112130Z
Status: **CANÔNICO / OPERACIONAL**

## Decisão Lucas

LKGOC não deve reconstruir uma coleção Shopify como layout único do zero a cada execução.

A arquitetura correta é criar/manter um **template padrão de coleção otimizada** no Shopify, por exemplo `collection.lkgoc.json` ou `collection.colecao-otimizada.json`, e atribuir esse template às coleções que entram no padrão LKGOC.

## Princípio

O template define o shell visual compartilhado. Cada coleção muda apenas:

- texto;
- imagens/editoriais;
- links;
- FAQ/schema/conteúdo específico;
- referências editoriais;
- handles/metafields/metaobjects da coleção.

Não muda por coleção:

- arquitetura do layout;
- ordem hero → grid completo → pós-grid/guia → FAQ;
- CSS estrutural;
- comportamento visual;
- namespace `lk-goc-*`;
- critérios de QA.

## Arquitetura Shopify recomendada

1. Criar/manter template JSON de coleção LKGOC:
   - `templates/collection.lkgoc.json` ou nome equivalente aprovado.
2. O template deve chamar seções compartilhadas:
   - hero/bloquinho editorial LKGOC;
   - grid nativo da coleção;
   - seção pós-grid `lk-goc-after-grid`;
   - FAQ/schema quando aplicável.
3. Conteúdo deve vir preferencialmente de metafields/metaobjects da coleção, não hardcoded por template.
4. Para ativar uma coleção no padrão, atribuir o template LKGOC à collection e preencher os campos específicos.
5. Qualquer execução deve acontecer primeiro em DEV/unpublished ou branch DEV, com readback e QA visual.

## Vantagem operacional

- Uma melhoria no shell LKGOC melhora todas as coleções otimizadas.
- Reduz drift visual.
- Evita duplicar Liquid/CSS por coleção.
- Facilita QA, rollback e manutenção.
- Mantém o padrão 204L como contrato real, não inspiração solta.

## Bloqueios

- Proibido criar template/layout novo por coleção sem aprovação explícita.
- Proibido hardcodar conteúdo de várias coleções em uma seção única frágil.
- Proibido promover para Production/main sem approval Lucas e fluxo GitHub DEV → merge Production → deploy/promoção controlada.

## QA obrigatório

- Verificar que a coleção usa o template LKGOC correto.
- Verificar que o grid completo renderiza antes do pós-grid.
- Verificar que o conteúdo específico vem da coleção/metafields/metaobjects corretos.
- Screenshot DEV vs Gold Source 204L lado a lado.
- Readback do template atribuído à collection.
