# AGENTS — [LK] Otimização de Coleção

## Boot obrigatório

1. Ler `agentes/lk-otimizacao-colecao/IDENTITY.md`.
2. Ler este `AGENTS.md`.
3. Ler `agentes/lk-otimizacao-colecao/MAPA.md`.
4. Ler `areas/lk/sub-areas/growth/LKGOC-PADRAO-CANONICO.md` antes de qualquer regra auxiliar.
5. Ler `areas/lk/sub-areas/growth/LKGOC-PRD.md`, `LKGOC-INPUT-CONTRACT.md`, `LKGOC-EVIDENCE-PACKET.md`, `LKGOC-EXECUTION-WORKFLOW.md`, `LKGOC-SCORECARD-100.md` e `LKGOC-IMPACT-REVIEW.md` conforme a etapa.
6. Consultar `areas/lk/sub-areas/growth/AGENTS.md` e `MAPA.md`.
7. Se houver Shopify preview/write, consultar LK Shopify e o template de aprovação Shopify.
8. Separar read-only/draft/preview de qualquer write externo.

## Regra absoluta LKGOC

Quando Lucas pedir “otimizar coleção com LKGOC”, tratar material existente como inventário/evidência e reconstruir a experiência completa. Não fazer remendo incremental salvo se o canônico e o scorecard aprovarem explicitamente.

## Fluxo

Pedido → classificar Full/Lite/Correção/Não-LKGOC → input contract → auditoria do estado atual → pesquisa/SERP/dados → evidence packet → copy coleção + guia pós-grid + FAQ/schema + guia dedicado → Claude SEO/GEO review → scorecard → DEV preview/approval packet → QA visual → aprovação → write escopado → readback/rollback/receipt → impact review → handoff.

## Autonomia permitida

Pode fazer sem aprovação: leitura pública/autenticada read-only, pesquisa, drafts, PRDs, scorecards, evidence packets, approval packets, documentação Brain, comparação antes/depois e previews que não publicam produção.

## Bloqueios

Exige aprovação explícita atual: Shopify/Tiny/GMC/Klaviyo/Ads/WhatsApp/email writes, publicação, produção, theme, page, collection, metafields, SEO fields, cron novo, gateway/runtime além deste profile, Docker/VPS/Traefik/secrets.

## Handoff obrigatório

Registrar no Brain quando houver draft material, decisão, aprovação, write, receipt, rollback, risco, bloqueio ou aprendizado. Nenhuma execução relevante pode ficar só no chat do bot.

## Definition of Done

- nível LKGOC declarado;
- input contract/evidence packet completos ou lacunas declaradas;
- pesquisa registrada;
- coleção no padrão 204L ou justificativa aprovada;
- guia dedicado no padrão Moon Shoe ou justificativa aprovada;
- FAQ/schema coerente;
- score LKGOC calculado com meta >=85;
- preview/QA visual desktop + mobile;
- approval packet antes de write;
- rollback/readback/receipt pós-write aprovado;
- impact review agendado/documentado quando houver produção.
