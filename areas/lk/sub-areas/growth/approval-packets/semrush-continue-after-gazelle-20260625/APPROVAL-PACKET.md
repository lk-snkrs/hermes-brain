# Approval Packet — Continuação SEMrush após Adidas Gazelle — 2026-06-25

Status: **read-only concluído; nenhum write externo executado nesta etapa**.

Contexto já verificado:
- Gazelle publicado em produção e validado no receipt `receipts/theme-production/adidas-gazelle-condition-hardening-production-20260625T175732Z/RECEIPT.md`.
- Packet anterior indicava próximos candidatos: ASICS Gel-1130, Nike Shox TL, New Balance 2002R.
- Histórico checado para evitar retrabalho: não há receipt/packet específico de `gel-1130`; há trabalhos antigos de ASICS Gel-NYC/NB740 e Nike Shox variante/PDP.

## Readback atual

### P1 agora — ASICS Gel-1130

Evidência pública:
- `/collections/asics-gel-1130` retorna 404.
- `/collections/asics-todos-os-modelos` retorna 200, com 13 itens públicos.
- A coleção geral Asics tem FAQ público, mas ainda contém termos operacionais antigos: `sob encomenda`, prazo `4 a 6 semanas`, `Frete grátis acima de R$ 499`.

Evidência Shopify Admin read-only:
- Coleção existente: `asics-todos-os-modelos` / title `Asics` / productsCount 17.
- Coleção existente: `asics-gt-2160` / productsCount 6.
- **Não há coleção específica detectada para `asics-gel-1130`.**
- Produtos Gel-1130 ativos detectados: 6 produtos ativos.

Diagnóstico:
- Demanda forte (`asics gel 1130`, cauda feminino/preto/branco/prata/bege), mas falta landing page específica.
- Não é seguro publicar guia SEO/GEO em Growth na coleção geral `asics-todos-os-modelos`, porque dilui intenção e mistura modelos.
- Antes do guia, precisa resolver superfície/canonical com LK Shopify.

Recomendação:
1. Handoff para `[LK] Shopify` validar/criar/ativar collection/hub `asics-gel-1130` com regras/tags corretas, sem mexer em estoque.
2. Em paralelo, preparar pacote de higiene para a coleção geral Asics removendo linguagem operacional antiga da FAQ pública, mas isso é write visível em produção e exige aprovação separada.
3. Depois da superfície canônica 200 OK, Growth prepara dev/preview do guia/FAQ/schema Gel-1130.

### P2 — Nike Shox TL

Evidência pública:
- `/collections/nike-shox-tl` retorna 404.

Evidência Shopify Admin read-only:
- Coleção específica não detectada.
- Produtos Shox TL ativos detectados: 7 produtos ativos + 2 drafts.

Diagnóstico:
- Também tem demanda, mas sem collection/hub. Deve entrar depois de ASICS ou junto no mesmo handoff Shopify de superfície/canonical.

### P3 — New Balance 2002R

Estado anterior:
- `/collections/new-balance-2002r` já tem superfície e guia/FAQPage.
- Não mexer agora; próximo passo é impacto review/GSC, não novo write.

## Decisão recomendada

**Continuar com ASICS Gel-1130, mas como handoff de superfície primeiro, não como write de conteúdo Growth.**

Motivo: há produtos ativos e demanda, porém a collection específica está 404. Publicar conteúdo no hub geral Asics agora seria menos preciso e mais arriscado.

## Aprovação/handoff sugerido

`Aprovo abrir handoff para LK Shopify validar/criar/ativar a collection canônica ASICS Gel-1130, preferencialmente /collections/asics-gel-1130, usando apenas produtos ASICS Gel-1130 ativos já existentes, sem consultar ou alterar estoque, preço, campanhas, GMC, Klaviyo ou checkout, com preview/readback público; após a superfície 200 OK, Growth prepara guia/FAQ/schema em dev antes de qualquer produção.`

## Evidências locais

- `work/semrush-continue-after-gazelle-20260625/shopify-readonly-surfaces.json`
- Public readback executado em 2026-06-25 via fetch: ASICS Gel-1130 404, Asics geral 200, Nike Shox TL 404.
