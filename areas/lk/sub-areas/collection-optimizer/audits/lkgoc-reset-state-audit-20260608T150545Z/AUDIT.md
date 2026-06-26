# LKGOC Reset State Audit

Data UTC: 20260608T150545Z
Status: READ-ONLY / NO SHOPIFY WRITE

## Escopo
Pedido Lucas: “Resetar e auditar o estado atual do LKGOC”.

## Evidências verificadas

- Brain LKGOC existe em `areas/lk/sub-areas/collection-optimizer/`.
- Dono operacional documentado: `[LK] Otimização de Coleções` / `lk-collection-optimizer`.
- Fonte canônica legada ainda em Growth: `areas/lk/sub-areas/growth/LKGOC-PADRAO-CANONICO.md`.
- Gold Source canônico: New Balance 204L em production.
- Tema production/main verificado por API: `155065417950` / `lk-new-theme/production` / `role=main`.
- Tema DEV verificado por API: `155065450718` / `lk-new-theme/dev` / `role=unpublished`.
- Doppler acessível; secrets esperados para `lk-collection-optimizer` e `lk-shopify` presentes; valores não impressos.

## Estado documental

- Regras bloqueantes atuais:
  - 204L é contrato visual, não inspiração.
  - Shared shell: só texto/imagem/link/conteúdo específico mudam.
  - PRD/perguntas/worker verdicts antes de rebuild.
  - Pós-grid deve ser depois de todos os produtos/paginação/load-more.
  - Production/main proibido sem aprovação explícita de Lucas.
- Há contradição/ruído em documentos antigos: alguns trechos dizem Contract Lock antes de qualquer write; correção posterior de Lucas libera write em DEV/unpublished e bloqueia apenas Production/customer-facing. Regra operacional segura: DEV read/write só após verificar `role=unpublished`; Production sempre bloqueado sem aprovação.

## Incidentes encontrados

- `lkgoc-puma-rejection-20260606`: Lucas rejeitou Puma como “totalmente errado”.
- `lkgoc-puma-v2-failure-audit-20260606T191557Z`: falha confirmada; erro principal foi usar aproximação de classes/blocos, em vez do DOM real renderizado da 204L production.
- `lkgoc-five-bad-rollback-20260606T135136Z`: lote de 5 ruim foi revertido/despublicado; páginas guia ficaram `published_at=null`.

## Estado Shopify read-only

- DEV tem mais artefatos LKGOC que Production, incluindo arquivos do lote rejeitado/descontinuado:
  - `snippets/lk-goc-canonical-five-collections.liquid`
  - `snippets/lk-goc-five-from-zero.liquid`
  - templates de guia para Adidas Gazelle, Labubu, Nike Dunk, Puma Speedcat, Yeezy
- Páginas do lote rejeitado verificadas como despublicadas:
  - guia-nike-dunk
  - guia-puma-speedcat
  - guia-adidas-gazelle
  - guia-yeezy
  - guia-labubu
- Coleção `puma-speedcat` aparece publicada com `template_suffix=puma-speedcat`, mas o template correspondente não existe em production/dev; provável fallback ao template padrão. Precisa investigação específica antes de qualquer ação.
- Storefront público das coleções principais retorna 200 e sem `Liquid error` detectado por HTML simples. Isso não equivale a QA visual LKGOC.

## Diagnóstico

O LKGOC está documentado, mas o sistema atual está contaminado por:

1. Artefatos DEV de tentativas rejeitadas.
2. Contradições em playbooks antigos vs correções posteriores.
3. Ausência de um lock operacional simples para o agente: antes ele tentou “interpretar” o 204L, quando Lucas pediu cópia controlada.
4. QA anterior insuficiente: técnico/DOM/classes não substitui side-by-side visual e contrato renderizado real.
5. Fila/ledger incompletos para scorecards, approvals e reviews.

## Recomendação de reset

- Congelar qualquer produção LKGOC.
- Não rodar lote.
- Eleger uma única coleção piloto.
- Antes de mexer: extrair DOM real + screenshots da 204L production e criar Contract Lock da coleção alvo.
- Build só em DEV `155065450718` após role check.
- PASS só com side-by-side desktop/mobile, guia pós-grid após último produto, FAQ único e readback.
- Approval Lucas obrigatório antes de merge/main.

## Próxima decisão necessária

Lucas precisa escolher:

1. Quarentena/limpeza do DEV rejeitado antes de novo build; ou
2. Manter DEV como está e reconstruir piloto por cima com snapshot/rollback; ou
3. Apenas auditoria visual sem escrever nada.

## Correção Lucas posterior — fluxo Production

Registrado em: 20260608T150751Z

A formulação anterior “Production/main proibido sem aprovação” deve ser lida de forma mais restritiva: **não existe write direto em Shopify Production/main como fluxo padrão**. O fluxo correto é GitHub branch DEV → QA/approval → merge para branch Production → deploy/promoção controlada.

