# Approval Packet — LKGOC P1 DEV corrections

Data UTC: 2026-06-03T14:13:10Z

## 1. Decisão pedida

Aprovar correções **em Shopify DEV somente** para endurecer o LKGOC antes de novas coleções e antes de qualquer novo production write.

Escopo DEV proposto:

1. `adidas-sambae`: ampliar/ajustar hero/bloco principal para régua LKGOC, mantendo padrão 204L.
2. `adidas-samba-jane`: corrigir schema `FAQPage` da coleção para refletir somente o FAQ visível específico de Samba Jane, se confirmado no readback Liquid.
3. Guias dedicados 204L/Samba Jane/Sambae: adicionar namespace/classe LKGOC auditável, sem mudar visual público pretendido.
4. Guias Full: garantir bloco “Referências editoriais e contexto” quando faltar, priorizando fontes internacionais reconhecíveis.
5. Limpar comentários técnicos/DEV/hotfix em assets candidatos antes de eventual production.

Não inclui:

- production;
- preço, estoque, produtos, checkout;
- GMC, Klaviyo, Meta/Google Ads;
- alteração de title/meta público em production.

## 2. Evidência

- Audit: `reports/lkgoc-audit-20260603.md`
- Ledger atualizado: `ledgers/lk-optimized-collections-ledger.json`
- QA público salvo: `collection-optimizer/qa-runs/lkgoc-public-qa-20260603T141230Z.json`
- Template criado: `templates/approval-packet-template.md`

## 3. QA público atual resumido

- `new-balance-204l`: HTTP 200; hero ~882 chars; FAQPage 1; LKGOC hint true.
- `adidas-samba-jane`: HTTP 200; hero ~860 chars; FAQPage 1; schema aparenta genérico de Samba, não específico do FAQ visível.
- `adidas-sambae`: HTTP 200; hero ~352 chars; FAQPage 1; abaixo da régua LKGOC se métrica for texto expandido.
- `adidas-samba`: HTTP 200; hero ~549 chars; DEV candidate com preview blocker registrado, não production-ready.

## 4. Score/riscos

Este packet não pede publicação. É hardening DEV.

Risco baixo em DEV, mas exige QA visual desktop/mobile antes de qualquer produção.

Riscos a observar:

- cache Shopify alternar variantes;
- schema FAQ duplicar ou ficar divergente;
- ajuste de hero Sambae alterar altura mobile e empurrar grid;
- namespaces novos não podem quebrar CSS existente.

## 5. Rollback DEV

Para cada asset alterado em DEV:

- salvar `.before` em `receipts/dev/lkgoc-p1-dev-corrections-[timestamp]/`;
- readback `.after`;
- rollback = PUT dos arquivos `.before` no mesmo tema DEV.

## 6. Critério de aceite DEV

- Preview Shopify DEV com link direto e `preview_theme_id`.
- Desktop/mobile comparados à 204L/Moon Shoe.
- Sambae com hero dentro da régua ou exceção registrada.
- Samba Jane com `FAQPage` igual ao FAQ visível da coleção.
- Guias com namespace LKGOC auditável.
- Nenhum comentário técnico/DEV em candidato para production.
- Novo QA público/readback salvo.

## 7. Frase de aprovação escopada

`Aprovo aplicar em Shopify DEV o pacote LKGOC P1 DEV corrections para Sambae, Samba Jane e guias LKGOC, sem production e sem alterar preço/estoque/produtos/campanhas/GMC/Klaviyo/checkout.`
