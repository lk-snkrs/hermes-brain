# Política obrigatória — GitHub-first / sem writes diretos Shopify Admin API

Status: ATIVA
Owner: [LK] Otimização de Coleções / LKGOC
Escopo: qualquer execução LKGOC, tema Shopify, collections, templates, assets, snippets, sections, metafields e publicação customer-facing.

## Regra absoluta
Este agente **NUNCA deve fazer write direto na Shopify Admin API**.

## Permitido
- Shopify Admin API somente em modo read-only/readback/validação.
- Consultar temas, roles, assets, collection metadata e status apenas para evidência.
- Usar API para confirmar `role: unpublished` ou `role: main` sem alterar nada.

## Proibido sem exceção operacional do agente
Não executar via Shopify Admin API:
- `PUT /assets` ou qualquer alteração de asset/snippet/section/template.
- `collectionCreate`, `collectionUpdate`, publish/unpublish, template suffix, regras de coleção.
- `metafieldsSet` ou alteração de metafields/metaobjects.
- alterações de navigation, redirects, products, variants, price, stock, publication, theme role.
- qualquer write customer-facing ou operacional.

## Fluxo obrigatório para qualquer mudança LKGOC
1. Trabalhar no repositório GitHub/local do tema.
2. Criar branch escopada.
3. Alterar arquivos no repo, nunca direto no Admin API.
4. Commitar.
5. Abrir PR ou pacote de aprovação.
6. Lucas aprova explicitamente.
7. Deploy/merge/promoção segue o fluxo aprovado e versionado.
8. Readback Shopify pós-deploy é permitido apenas para validação.

## Se houver urgência
Mesmo em urgência, o agente deve parar e pedir handoff/approval de exceção explícita. Por padrão, não existe hotfix direto via Admin API.

## Incidente registrado
Em 2026-06-13, durante a coleção New Balance 2002R, houve write direto via Shopify Admin API. Isso foi reconhecido como erro de fluxo. A regra acima passa a ser guardrail obrigatório permanente deste perfil.
