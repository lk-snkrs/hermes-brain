# LK Growth Agentic OS v1 — Tool & Integration Matrix

Data: 2026-06-04
Status: rascunho para simulação local/read-only
Escopo: definir quais ferramentas cada subagente pode usar e em qual status operacional.

## Status de integração

- `unavailable`: não existe ou não está acessível.
- `documented_only`: há documentação, mas não está provado no runtime.
- `configured`: aparece em config/env, sem prova de descoberta.
- `discovered`: o runtime descobriu a ferramenta.
- `read_only_verified`: pelo menos uma chamada read-only foi validada.
- `write_capable_but_blocked`: ferramenta consegue escrever, mas writes estão bloqueados por política.
- `approved_for_scope`: write aprovado para escopo específico, com rollback/verificação.

Regra: decisão `decision-grade` só pode se apoiar em fonte `read_only_verified` ou em fonte cuja ausência esteja explicitamente declarada como gap.

## Matriz por subagente

### Growth Planner

- Brain/file: obrigatório; read-only.
- Cron output read-only: desejável.
- Session/search histórico: útil quando precisar reconstruir contexto.
- Writes/runtime: bloqueado.

### Growth Data Scout

- Brain/file: obrigatório.
- Shopify read-only: desejável para produto/collection/comercial.
- GA4/GSC: obrigatório para decisão comercial SEO/CRO.
- GMC/Merchant read-only: obrigatório para product data/feed/local inventory.
- DataForSEO: obrigatório para SERP/GEO quando a decisão for orgânica/AI Search.
- PageSpeed/CrUX: obrigatório quando performance/CWV é parte da hipótese.
- Klaviyo/Metricool/Meta: auxiliar; não sustenta causalidade isolada.
- Writes: bloqueado.

### SEO/GEO Analyst

- GSC: fonte superior para demanda real LK.
- DataForSEO: SERP, keyword, competitor, AI/LLM mentions.
- Web/browser: validação pública e SERP/public HTML.
- Brain: experiment history e padrões canônicos.
- Claude SEO skill family: diagnóstico/refinamento, não substitui ranking comercial.
- Shopify writes/theme/content publish: bloqueado.

### CRO/PDP Analyst

- GA4: fonte superior para sessões/conversão/funil.
- Shopify read-only: produto, collection, pedidos/revenue quando disponível.
- Browser/vision: QA público/mobile.
- PageSpeed/CrUX: performance/CWV.
- Brain experiment ledger: evitar repetição.
- Theme/dev upload/production publish: bloqueado sem aprovação A3/A4.

### GMC/Product Data Analyst

- GMC/Merchant read-only: fonte superior para issues/status.
- Shopify read-only: cruzamento de produto/variant/page.
- Product feed/readback: validação.
- Brain packets/receipts: rollback/history.
- DataForSEO Shopping/SERP: auxiliar para impacto.
- Merchant/Product API writes/feed patches: bloqueado sem aprovação A3/A4.

### Content/SEO Analyst — não-LKGOC / Collection Optimizer handoff

- GSC/DataForSEO: demanda e SERP.
- Shopify read-only: estado atual quando houver superfície relacionada.
- Templates Brain: conteúdo/source page não-LKGOC.
- LKGOC/otimização de coleção/guia de coleção: não executar no Growth; rotear para `[LK] Otimização de Coleções`.
- Templates Brain: guia editorial, source page, LKGOC.
- Publishing/Shopify write: bloqueado.

### Experiment Reviewer

- Original receipt: obrigatório.
- Hypothesis ledger: obrigatório.
- GA4/GSC/Shopify read-only: fonte de impacto.
- Brain reports: comparação antes/depois.
- Writes: bloqueado; pode propor atualização de skill/contexto.

### Growth Governor / Critic

- Brain approval matrix/source hierarchy: obrigatório.
- Specialist outputs: obrigatório.
- Receipts/ledgers: obrigatório.
- Verification read-only tools: permitido.
- External writes: bloqueado.

## Safe default

Se uma integração estiver ausente ou não verificada:

1. marcar `source_status` corretamente;
2. rebaixar confiança;
3. bloquear recomendação decision-grade quando a fonte for essencial;
4. produzir checklist de gap em vez de inventar conclusão.

## Write surfaces bloqueadas por padrão

- Shopify Admin mutations.
- Shopify theme upload/publish.
- GMC/Merchant API mutations.
- Supplemental feed update.
- Klaviyo send/update público.
- Meta/Google Ads campaign changes.
- WhatsApp/comunicação externa.
- Docker/VPS/Traefik/API/gateway/secrets.

## Approval mapping

- Read-only diagnostics: A0 livre.
- Local preview/packet: A1 livre.
- Recomendação evidence-based: A2 livre.
- Pequeno write externo: A3 approval escopado.
- Bulk/produção/campanha/infra: A4 approval forte + rollback + verificação.
