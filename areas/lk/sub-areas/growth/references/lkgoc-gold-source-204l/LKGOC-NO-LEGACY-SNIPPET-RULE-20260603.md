# Regra LKGOC — não expandir snippets legados por coleção

Data UTC: 2026-06-03T19:22:46.355091+00:00

## Decisão
Para novas execuções LKGOC, não criar nem evoluir arquitetura baseada em snippets específicos legados por coleção, como:
- `lk-samba-204l-hero-v2`
- `lk-samba-204l-guide-v2`
- `lk-sambae-204l-*`
- qualquer `lk-lkgoc-*`

## Nuance técnica
Snippets Shopify não são proibidos por si só. O erro é usar snippets antigos/específicos como padrão de crescimento LKGOC.

## Padrão correto
- Usar o componente canônico LKGOC (`lk-goc-*`) e a Gold Source 204L.
- Para guias: `lk-goc-guide-v1` parametrizado, com FAQ/Schema da mesma fonte.
- Para collections: componente LKGOC novo/canônico, com namespace `lk-goc-*` e aliases legados apenas se necessários para compatibilidade temporária.

## Ponte temporária permitida
Se uma coleção já estiver wired via snippet legado, só é aceitável corrigir em DEV como contenção imediata, mas deve abrir tarefa de migração para o componente novo.

## QA obrigatório
Antes de pedir approval:
- readback Asset API batendo;
- browser real desktop/mobile;
- largura/tipografia medidas;
- comportamento mobile validado por clique real;
- nenhum `lk-lkgoc-*` dentro do bloco novo.
