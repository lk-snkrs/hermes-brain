# Handoff — LK Shopify aplicar DEV/branch correction Alo Yoga + Crocs McQueen

Origem: `[LK] Otimização de Coleções` / LKGOC  
Data: 2026-06-25  
Prioridade: P1 cleanup pós-publicação  
Writes já feitos por LKGOC nesta etapa: 0

## Pedido

Aplicar em ambiente DEV/branch/readback, não Production/main, os payloads corrigidos de `collection.descriptionHtml` para:

- `alo-yoga-1`
- `crocs-mcqueen`

## Fonte dos payloads

Workdir:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/20260625T-alo-crocs-lkgoc-lite-correction-dev/`

Arquivos:

- `collection__alo-yoga-1.descriptionHtml.corrected.html`
- `collection__crocs-mcqueen.descriptionHtml.corrected.html`
- `candidate-payload.json`
- `local-qa.json`
- `CORRECTION-PACKET.md`

## Escopo permitido

- DEV/branch/readback apenas.
- Atualizar somente conteúdo editorial LKGOC Lite dos dois handles acima.
- Gerar backup antes do write.
- QA público/preview mobile+desktop.
- Sem Production/main até approval posterior de Lucas.

## Fora do escopo

- Preço.
- Estoque/disponibilidade/grade.
- Produtos/variantes.
- Ordenação.
- GMC/feed.
- Klaviyo/WhatsApp/email.
- Campanhas.
- Checkout.
- Theme production/main.

## QA esperado após aplicação DEV

- HTTP 200.
- H1 único.
- FAQPage único.
- Bloco citável único.
- Sem Liquid error.
- Alo Yoga sem duplicidade de `Como escolher`/FAQ.
- Crocs McQueen com guia visualmente pós-grid.
- Screenshots mobile/desktop.
- Readback sanitizado.

## Observação de governança

LKGOC preparou o candidato, mas não fez Shopify Admin write porque a política ativa é GitHub-first/no direct Admin writes para este agente. LK Shopify deve assumir a superfície técnica ou Lucas precisa aprovar exceção explícita.
