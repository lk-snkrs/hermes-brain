# Audit LKGOC — 2026-06-03

## Escopo

Auditoria read-only do sistema LKGOC no Brain/profile e checagem pública básica das páginas LKGOC atuais.

Fontes verificadas:

- `LKGOC-PADRAO-CANONICO.md`
- `LKGOC-PRD.md`
- `LKGOC-INPUT-CONTRACT.md`
- `LKGOC-EVIDENCE-PACKET.md`
- `LKGOC-EXECUTION-WORKFLOW.md`
- `LKGOC-SCORECARD-100.md`
- `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`
- `skills/lk-superpowers-collection-optimizer/SKILL.md`
- profile skills: `lk-growth` e `lk-collection-optimizer`
- ledger: `ledgers/lk-optimized-collections-ledger.json`
- páginas públicas: `/collections/new-balance-204l`, `/collections/adidas-samba-jane`, `/collections/adidas-sambae`, `/pages/guia-adidas-samba-jane`, `/pages/guia-adidas-sambae`, `/pages/new-balance-204l-original-brasil-guia-lk`

## Veredito executivo

O LKGOC está conceitualmente certo e o canônico já corrigiu problemas críticos anteriores, mas ainda tem quatro falhas relevantes:

1. **Governança documental poluída:** regras longas continuam duplicadas em muitos arquivos ativos; isso aumenta risco de drift.
2. **Ledger desatualizado:** o registro operacional só lista `adidas-samba-jane` como `dev_implemented_pending_visual_qa`, apesar de já existirem receipts públicos/produção para Samba Jane, Sambae e 204L.
3. **Template citado pela skill está faltando:** `templates/approval-packet-template.md` é requerido pela skill, mas não existe.
4. **Aplicação pública inconsistente:** `adidas-sambae` está com hero curto para a régua LKGOC; `samba-jane` e `204L` estão acima da régua 500–700 no HTML completo; guias dedicados não carregam classe/namespace LKGOC detectável e alguns guias não mostram bloco de referências editoriais reconhecível na leitura textual.

## Achados

### A1 — Fonte única existe, mas o ecossistema ainda duplica regra longa

Evidência:

- O canônico declara que `LKGOC-PADRAO-CANONICO.md` é o documento único de verdade.
- Mesmo assim, há **35 documentos ativos `.md`** com menções/regras LKGOC fora de receipts/reports/work/approval.
- Arquivos com mais duplicação: `prds/lk-otimizacao-colecao-agent-prd-2026-06-03.md`, `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`, `skills/lk-superpowers-collection-optimizer/SKILL.md`, `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`, `PADRAO-LK-COLLECTION-V2.md`, `PADRAO-GUIAS-EDITORIAIS-LK.md`, `MAPA.md`, `IDENTITY.md`.

Risco:

- Agente pode seguir documento auxiliar/antigo e ignorar o canônico.
- Correções novas de Lucas exigem patch em muitos lugares.

Status:

- Não bloqueia execução se a skill abrir o canônico primeiro, mas é risco estrutural.

Recomendação:

- Transformar documentos auxiliares em ponteiros curtos para `LKGOC-PADRAO-CANONICO.md`.
- Manter regras executáveis apenas em: canônico, workflow, scorecard, input/evidence, templates e skill carregável.

### A2 — Skill carregável foi corrigida nos profiles principais

Evidência:

- `/opt/data/profiles/lk-growth/skills/lk-superpowers-collection-optimizer/SKILL.md` existe.
- `/opt/data/profiles/lk-collection-optimizer/skills/lk-superpowers-collection-optimizer/SKILL.md` existe.
- Ambas abrem com fonte única: `LKGOC-PADRAO-CANONICO.md`.
- `lk-seo-weekly-improvement` nos dois profiles tem override explícito: LKGOC vence padrões antigos como off-white/hero claro, 350–450 chars, FAQ duplicado e draft local como output final.

Status:

- Corrigido em relação ao audit anterior.

Risco restante:

- A skill diz “Este profile `lk-growth`” mesmo dentro do profile `lk-collection-optimizer`; pequeno ruído de identidade, não bloqueante.

### A3 — Template de approval packet requerido não existe

Evidência:

- `skills/lk-superpowers-collection-optimizer/SKILL.md` manda usar `templates/approval-packet-template.md`.
- Arquivo não existe em `areas/lk/sub-areas/growth/templates/`.

Risco:

- O agente improvisa approval packet e pode esquecer score, link preview, evidência, limitações, rollback/cache ou decisão pedida.

Recomendação:

- Criar `templates/approval-packet-template.md` alinhado ao LKGOC canônico.

### A4 — Ledger LKGOC está atrasado e não reflete produção

Evidência:

- `ledgers/lk-optimized-collections-ledger.json` contém apenas `adidas-samba-jane`.
- Status ainda: `dev_implemented_pending_visual_qa`.
- Há receipts posteriores de produção/dev para Samba Jane, Sambae e 204L, por exemplo:
  - `receipts/production/samba-jane-lkgoc-v2-apply-20260602T194351Z/`
  - `receipts/shopify-collections/sambae-collection-production-publish-20260603T122556Z/`
  - `receipts/production/lkgoc-204l-compare-20260602T193829Z/`

Risco:

- Refresh mensal, batch update e impact review pegam lista errada.
- Agente pode achar que não há LKGOC ativo além de Samba Jane pendente.

Recomendação:

- Atualizar ledger com `new-balance-204l`, `adidas-samba-jane`, `adidas-sambae`, status real, URLs, guia dedicado, score, data de produção e próxima revisão de impacto.

### A5 — Aplicação pública: hero/copy não está consistente com régua 500–700

Checagem pública HTML:

- `/collections/new-balance-204l`: `coll-banner__desc` com ~882 caracteres no HTML completo.
- `/collections/adidas-samba-jane`: `coll-banner__desc` com ~860 caracteres no HTML completo.
- `/collections/adidas-sambae`: `coll-banner__desc` com ~352 caracteres.

Interpretação:

- O canônico diz 500–700 caracteres, salvo exceção registrada.
- `adidas-sambae` está curto.
- `204L` e `samba-jane` estão acima da faixa no HTML completo; podem estar aceitáveis visualmente se o read-more/altura resolver, mas deveriam ter exceção registrada ou régua clarificada como “500–700 visível/primeiro bloco útil”, não total expandido.

Risco:

- Inconsistência no que o agente entende como “primeiro bloco”: visível, HTML completo, texto antes do readmore ou texto total.

Recomendação:

- Ajustar canônico: definir exatamente se a régua é para texto visível inicial, parágrafo total ou bloco expandido.
- Corrigir Sambae para entrar na régua ou registrar exceção.

### A6 — FAQ schema da Samba Jane coleção parece divergente do FAQ visível

Evidência pública:

- `/collections/adidas-samba-jane` tem 1 script `FAQPage`, mas os nomes detectados no schema são genéricos da família Samba:
  - “Qual Adidas Samba escolher primeiro?”
  - “Qual a diferença entre Samba OG, Samba Jane, Sambae e Samba XLG?”
  - “Como saber se o Adidas Samba é original?”
  - “O Adidas Samba tem forma grande ou pequena?”
- O FAQ visível no fetch textual é específico de Samba Jane:
  - “O que é o Adidas Samba Jane?”
  - “Qual a diferença entre Samba Jane e Samba OG?”
  - “Como usar Adidas Samba Jane?”
  - “Qual cor do Adidas Samba Jane escolher?”

Risco:

- Desalinhamento entre schema e conteúdo visível; ruim para SEO/GEO e QA do LKGOC.

Recomendação:

- Read-only confirmar no Liquid/section e corrigir em DEV: schema `FAQPage` deve refletir somente o FAQ visível canônico daquela coleção.

### A7 — Guias dedicados estão públicos, mas namespace/QA detectável é fraco

Evidência pública:

- Guias retornam HTTP 200 e têm `FAQPage` único.
- Páginas testadas: `/pages/new-balance-204l-original-brasil-guia-lk`, `/pages/guia-adidas-samba-jane`, `/pages/guia-adidas-sambae`.
- Não detectei classe/namespace `lkgoc` nos guias dedicados.
- `guia-adidas-samba-jane` tem referência textual a “Revistas internacionais”; `guia-adidas-sambae` e guia 204L não mostraram bloco de referências/revistas reconhecível na leitura textual básica.

Risco:

- Fica difícil auditar em lote se o guia usa LKGOC/Moon Shoe ou só reaproveita CSS/template.
- GEO perde força se fontes editoriais externas não estiverem visíveis/citáveis.

Recomendação:

- Padronizar namespace/classe nos guias: `lk-lkgoc-guide`, `lk-lkgoc-guide--[handle]`.
- Garantir seção “Referências editoriais e contexto” em todos os guias Full, com fontes internacionais reconhecíveis quando houver.

### A8 — Páginas públicas ainda têm CSS/comentários históricos de hotfix

Evidência:

- HTML público contém comentários/trechos como `LK production fix — Samba Jane collection LKGOC CSS v2` e `LK DEV fix — 204L post-grid spacing before LK guide` dentro do CSS global da seção.

Risco:

- Não quebra conversão, mas viola a higiene de source do canônico: production sem markers/comentários DEV/técnicos.
- Aumenta ruído de manutenção.

Recomendação:

- Limpar comentários técnicos em próximo batch DEV → approval → production.

## Priorização de correção

### P0 — Corrigir antes de novas coleções LKGOC

1. Atualizar ledger LKGOC.
2. Criar `templates/approval-packet-template.md`.
3. Corrigir schema FAQ da coleção Samba Jane se confirmado no readback.
4. Definir no canônico a régua exata de caracteres do hero.

### P1 — Corrigir no próximo batch visual/DEV

1. Ajustar hero da Sambae para régua LKGOC ou registrar exceção.
2. Adicionar namespace LKGOC nos guias dedicados.
3. Padronizar referências editoriais visíveis nos guias Full.
4. Limpar comentários técnicos/DEV do source público.

### P2 — Governança documental

1. Reduzir duplicações: transformar documentos auxiliares em ponteiros.
2. Manter canônico + workflow + scorecard + templates como fonte operacional.
3. Registrar checks automáticos simples para ledger, schema FAQ e presença de guia.

## O que não foi feito

- Nenhum write externo.
- Nenhuma alteração em Shopify/GMC/tema/produção.
- Não usei GA4/GSC/GMC para métrica comercial; este audit é de governança/execução LKGOC, não de impacto comercial.

## Próxima ação segura

Preparar patch local Brain com:

- template de approval packet;
- atualização do ledger;
- checklist automático LKGOC read-only;
- pacote de approval para eventual correção em DEV de Sambae/Samba Jane schema.
