# PRD — LK Growth Weekly Execution Plan — Semana 2026-06-08

Data: `2026-06-08T14:37:44.486472+00:00`  
Owner: LK Growth OS  
Fonte-base: `reports/weekly/lk-growth-weekly-command-center-2026-06-08.md`  
Modo: Superpowers Full — PRD/execução, com guardrails LK e 18 tópicos Growth  
Status: pronto para aprovação de execução por packets; writes externos continuam approval-gated

---

## 1. Resumo executivo

Esta semana deve transformar o **LK Growth Weekly Command Center** em uma fila executável de crescimento, sem dispersar em auditorias soltas.

O relatório semanal trouxe três verdades operacionais:

1. **SEO/CRO orgânico tem alavancas claras** em Onitsuka, New Balance 204L, Nike Mind, Lululemon e Samba Jane.
2. **GMC era gargalo material**, principalmente Local/LIA `link_template`, `landing_page_error`, atributos e preço/governança.
3. **Dados ainda têm pontos parciais**: PageSpeed/CrUX, Klaviyo onsite events e reconciliação completa de conversão por URL.

Atualização pós-relatório: o gargalo Local/LIA `mhlsf_full_missing_valid_link_template` já foi executado e validado em produção GMC:

- scan inicial: `10.987` itens com issue;
- scan final: `0` itens restantes;
- receipt: `receipts/gmc/lia-link-template-all-20260608T/FINAL_SUCCESS.md`.

Portanto, este PRD já considera `link_template` como **execução concluída**, e reposiciona GMC para as próximas frentes: `landing_page_error`, atributos high-confidence e governança de preço/GTIN.

---

## 2. Objetivo da semana

Aumentar captura de demanda e servibilidade comercial da LK sem criar risco operacional, entregando:

- 2 packets SEO/GEO/CRO prontos para aprovação/aplicação;
- 1 handoff LKGOC canônico para coleção estratégica;
- 1 pacote GMC pós-link-template com triagem e micro-piloto seguro;
- 1 diagnóstico de mensuração/Klaviyo/PageSpeed para tirar a próxima rotina de “decision-grade parcial”.

### North Star da semana

**Mover o Weekly de relatório para execução com evidência, preview, approval packet, rollback e revisão D+7.**

---

## 3. Não objetivos

Nesta semana, não fazer:

- bulk update de Shopify SEO/copy/coleção sem approval packet;
- publish direto em production theme;
- mudanças de preço, estoque, desconto ou disponibilidade;
- campanhas Meta/Google ou Klaviyo sends;
- `fetchNow`/feed massivo/GMC write sem escopo e rollback;
- alterar taxonomia pública com “pronta entrega/encomenda/estoque”.

---

## 4. Escopo e priorização

### P0 — Já concluído / monitorar

#### P0.1 GMC Local/LIA `link_template`

- Status: concluído.
- Evidência: `10.987 → 0` itens com `mhlsf_full_missing_valid_link_template`.
- Ação restante: monitorar em 24–72h e D+7 para overwrite por feed/Simprosys.
- Owner: LK Growth / GMC runner.
- Aprovação adicional: não necessária para monitoramento read-only.

### P1 — Execução principal da semana

#### P1.1 Onitsuka Tiger CTR/GEO Packet

**Problema:** alta demanda e receita, mas CTR baixo no head term.

Fatos:

- `onitsuka tiger`: 24.448 impressões, CTR 0,29%, posição 8,3.
- Coleção todos os modelos: 865 sessões orgânicas.
- Receita histórica combinada Onitsuka: R$ 1,9M+ no refresh usado pelo Weekly.

Entregáveis:

1. SERP/GSC read-only por query e página.
2. Diagnóstico de snippet atual: title/meta/H1/FAQ/schema.
3. 2–3 variações de title/meta por intenção:
   - head term “Onitsuka Tiger”;
   - “Mexico 66 original”;
   - comprador premium/autenticidade.
4. FAQ buyer-intent sem linguagem operacional proibida.
5. Source-page/guia brief: “Onitsuka Tiger original no Brasil / Mexico 66 original”.
6. Approval packet com impacto, risco, rollback e campos exatos.

Critério de aceite:

- Packet salvo no Brain.
- Inclui antes/depois proposto por URL/campo.
- Nenhum write Shopify.
- Tem rollback textual: restaurar SEO fields/body/schema anteriores.

Approval gate:

- Aplicação em Shopify/coleção/PDP só com “Aprovo aplicar Packet Onitsuka [data/versão]”.

#### P1.2 New Balance 204L — LKGOC refresh/handoff canônico

**Problema:** demanda explosiva maior que tráfego capturado; coleção já forte mas deve virar execução LKGOC disciplinada.

Fatos:

- `new balance 204l`: 9.900/mês; pico 40.500.
- GA4 orgânico: 230 sessões, engagement 71,3%.
- Receita histórica: R$ 1,0M+ no refresh usado pelo Weekly.

Entregáveis:

1. Evidence packet LKGOC: GA4, GSC/DataForSEO, Shopify, SERP, Ahrefs quando disponível.
2. Contract Lock LKGOC antes de qualquer write.
3. Definição se é Full, Lite ou Correção — recomendação: **Correção/Refresh Full**, porque 204L é gold source mas precisa auditoria e impacto review.
4. Handoff para Collection Optimizer com escopo:
   - coleção produto-first;
   - guia dedicado;
   - FAQ/schema único;
   - QA visual desktop/mobile;
   - approval packet.

Critério de aceite:

- Handoff salvo no Brain.
- Sem production write.
- Se houver dev preview, role do tema deve ser verificado como não-main.

Approval gate:

- Qualquer alteração visual/textual pública exige approval explícito no turno.

#### P1.3 Nike Mind 001 — CRO/GEO PDP + coleção

**Problema:** demanda alta, tráfego existe, mas PDP principal tem bounce/engagement pior; intenção exige explicação clara.

Fatos:

- `nike mind 001`: 18.100/mês.
- PDP Black Chrome: 202 sessões, bounce 43,6%.
- Collection: 197 sessões.
- GMC GTIN + link_template já corrigidos para itens Nike Mind/LIA afetados.

Entregáveis:

1. QA público/mobile read-only de PDP e coleção.
2. Diagnóstico de clareza: o que é Nike Mind, tamanho, conforto, autenticidade, CTA, parcelamento, confiança.
3. Blocos GEO citáveis e FAQ propostos.
4. Packet de melhoria PDP/collection com separação:
   - copy/FAQ/schema;
   - visual/theme;
   - Merchant/product data.

Critério de aceite:

- Packet mostra exatamente o que muda e onde.
- Classifica cada mudança como read-only, Shopify content, theme/dev, GMC ou mensuração.
- Sem write público.

#### P1.4 GMC Product Data Quality — pós-link-template

**Problema:** depois de resolver Local/LIA link_template, restam issues com impacto em Shopping/Surfaces.

Frentes:

1. `landing_page_error` — 1.431 produtos no Weekly.
2. `missing_item_attribute_for_product_type` / color — 712 produtos; preview high-confidence citado de 393.
3. `price_updated` / `strikethrough_price_updated` — tratar como governança, não bulk fix.
4. GTIN/restricted/identifier residual — só high-confidence, sem inventar identificador.

Entregáveis:

- Novo scan GMC read-only pós-correção link_template.
- Priorização por issue remanescente e destino reprovado.
- Micro-piloto `missing color` com 25–50 offerIds high-confidence, preview only.
- Checker `landing_page_error` para 50 URLs:
  - HTTP status;
  - redirect chain;
  - canonical;
  - variant válida;
  - noindex/robots;
  - comparação URL limpa vs feed URL.
- Approval packet para qualquer ProductInput/feed write futuro.

Critério de aceite:

- Nenhum preço/promo alterado.
- Nenhum feed write sem aprovação.
- Cada offerId proposto tem snapshot/readback/rollback planejado.

### P2 — Instrumentação e confiança dos dados

#### P2.1 Klaviyo tracking diagnostic

**Problema:** opens/clicks existem, mas eventos comerciais onsite aparecem zerados.

Entregáveis:

- Diagnóstico read-only de eventos Klaviyo:
  - Active on Site;
  - Added to Cart;
  - Started Checkout;
  - Placed Order;
  - identificação de perfis/event mapping;
  - janela e filtros da API.
- Conclusão: problema de tracking, integração, mapeamento, janela ou leitura.

Critério de aceite:

- Explica por que clicked/opened aparece e ecommerce não.
- Não cria campanha, flow, lista, segmento ou envio.

#### P2.2 PageSpeed/CrUX tooling normalization

**Problema:** Weekly ficou parcial por timeout/CrUX 404/API key context.

Entregáveis:

- Doppler-first presence check sanitizado para `GOOGLE_API_KEY` e conectores necessários.
- Teste de 3 URLs P1:
  - home;
  - collection Onitsuka/204L;
  - PDP Nike Mind.
- Resultado salvo como decision-grade ou blocker técnico.

Critério de aceite:

- Sem imprimir secret.
- Se API falhar, status claro: secret ausente, runtime não injetado, API/endpoint falhando ou URL sem CrUX.

---

## 5. Backlog executável

### Ticket A — Recheck GMC pós-link-template

- Tipo: GMC / read-only.
- Ação: rodar scan completo e comparar com Weekly + receipt link_template.
- Output: `reports/gmc/gmc-post-link-template-health-20260608.md`.
- Aceite: top issues atualizados, counts, P0/P1/P2, próximos packets.
- Aprovação: não necessária.

### Ticket B — Onitsuka CTR/GEO Packet

- Tipo: SEO/GSC/GEO/SERP/Shopify SEO preview.
- Output: `approval-packets/onitsuka-ctr-geo-20260608/`.
- Aceite: preview title/meta/FAQ/source page, rollback, approval wording.
- Aprovação para execução pública: necessária.

### Ticket C — Nike Mind CRO/GEO Packet

- Tipo: CRO/PDP/GEO/GMC context.
- Output: `approval-packets/nike-mind-cro-geo-20260608/`.
- Aceite: diagnóstico PDP mobile, copy/FAQ/schema preview, dev-theme handoff se visual.
- Aprovação para execução pública: necessária.

### Ticket D — LKGOC New Balance 204L Handoff

- Tipo: LKGOC/collection optimizer.
- Output: `handoffs/lkgoc-new-balance-204l-refresh-20260608.md`.
- Aceite: evidence packet + contract lock requirements + owner + gate DEV-first.
- Aprovação para Shopify/dev/production: necessária conforme etapa.

### Ticket E — GMC Missing Color Micro-pilot Preview

- Tipo: GMC product data.
- Output: `approval-packets/gmc-missing-color-micro-pilot-20260608/`.
- Aceite: 25–50 exact offerIds, confidence reason, snapshot plan, rollback, no price/stock.
- Aprovação para ProductInput/feed write: necessária.

### Ticket F — GMC Landing Page Error Triage

- Tipo: GMC/SEO technical.
- Output: `reports/gmc/landing-page-error-triage-20260608.md`.
- Aceite: 50 URLs classificadas por causa raiz; plano por causa.
- Aprovação: read-only não; writes futuros sim.

### Ticket G — Klaviyo Tracking Diagnostic

- Tipo: CRM/mensuração.
- Output: `reports/measurement/klaviyo-tracking-diagnostic-20260608.md`.
- Aceite: causa provável + próximos passos; nenhum envio.
- Aprovação para correção/envio: necessária.

### Ticket H — PageSpeed/CrUX Recovery

- Tipo: PageSpeed/CWV/tooling.
- Output: `reports/pagespeed-crux/pagespeed-crux-recovery-20260608.md`.
- Aceite: 3 URLs testadas ou blocker sanitizado.
- Aprovação: não para leitura; sim se precisar alterar env/runtime global.

---

## 6. Sequência recomendada

### Hoje — Bloco 1

1. Recheck GMC pós-link-template.
2. Gerar `landing_page_error` triage e color micro-pilot preview.
3. Abrir Onitsuka packet.

### Hoje — Bloco 2

4. Nike Mind CRO/GEO packet.
5. LKGOC 204L handoff.

### Amanhã

6. Klaviyo tracking diagnostic.
7. PageSpeed/CrUX recovery.
8. Preparar approval bundle único para Lucas decidir o que aplicar.

### D+7

9. Impact review:
   - GMC issues remanescentes;
   - GSC CTR para páginas alteradas, se houver write aprovado;
   - GA4 organic landing pages;
   - Shopify conversion/revenue quando disponível;
   - Klaviyo tracking se corrigido.

---

## 7. Critérios de sucesso

### Até o fim da semana

- `link_template`: continua 0 issue após recheck.
- GMC: top issues remanescentes atualizados pós-correção, com pelo menos 1 micro-pilot approval-ready.
- SEO/GEO: Onitsuka packet pronto para aprovação.
- CRO/GEO: Nike Mind packet pronto para aprovação.
- LKGOC: 204L handoff canônico pronto, sem drift.
- Mensuração: Klaviyo ou PageSpeed deixam de ser “parcial” ou têm blocker documentado.

### Métricas a observar após writes aprovados

- GSC CTR por query/página em 7–14 dias.
- GA4 organic sessions e engagement por landing page.
- Shopify pedidos/receita por produto/coleção quando reconciliado.
- GMC item statuses e destinationStatuses.
- Merchant Diagnostics por issue.
- Klaviyo ecommerce event counts, se tracking corrigido.

---

## 8. Riscos e mitigação

### Risco 1 — Corrigir Shopify sem decision-grade por URL

- Mitigação: packets primeiro; writes só com aprovação e rollback.

### Risco 2 — GMC overwrite por Simprosys/feed

- Mitigação: recheck 24–72h e D+7; registrar dataSource; evitar bulk cego.

### Risco 3 — LKGOC drift visual

- Mitigação: usar `LKGOC-PADRAO-CANONICO.md`; DEV-first; Contract Lock; QA visual desktop/mobile.

### Risco 4 — Copy SEO genérica prejudicar premium LK

- Mitigação: Claude SEO/GEO + tom LK; foco em curadoria, autenticidade e atendimento humano.

### Risco 5 — PageSpeed/Klaviyo virarem buraco infinito

- Mitigação: timebox diagnóstico; se blocker, documentar causa e approval necessário.

---

## 9. Approval matrix

Pode executar sem nova aprovação:

- scans read-only;
- relatórios;
- PRD/packets;
- previews locais;
- QA público;
- handoff interno;
- rollback plans.

Precisa aprovação explícita atual:

- Shopify SEO fields/body/metafields/pages/theme;
- GMC ProductInput/feed/supplemental/fetchNow;
- Klaviyo flow/campaign/list/send/config write;
- Google/Meta Ads;
- preço/estoque/desconto;
- theme production ou publish.

---

## 10. Definition of Done do PRD

Este PRD está pronto quando:

- transforma o Weekly em backlog com owners/gates;
- marca `link_template` como concluído e monitorável;
- preserva guardrails de writes;
- cobre os 18 tópicos como input do plano;
- define critérios de aceite e verificação por ticket;
- é salvo no Brain.

Status deste PRD: **pronto para execução read-only/packets**.
