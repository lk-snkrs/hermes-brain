# Fluxo operacional — Growth → Shopify → Approval → Receipt

Data: 2026-06-05
Status: fluxo local/documental; não cria runtime, cron ou write externo.

## Objetivo

Definir o primeiro fluxo prático entre LK Growth OS e LK Shopify OS para que uma demanda real vire ação segura sem confundir agente permanente com subagente.

## Regra LKGOC

Se a entrada for LKGOC, otimização de coleção, guia de coleção ou página/guia de produto-modelo, o dono é sempre `[LK] Otimização de Coleções` (`lk-collection-optimizer`). Growth pode fornecer sinais e Shopify pode fornecer preview/readback, mas o fluxo mestre e o scorecard ficam no Collection Optimizer.

## Fluxo padrão

```text
1. Entrada
   → Inbox Growth ou Inbox Shopify

2. Triagem
   → contexto, objeto, fonte, risco A0-A4, output esperado

3. Evidência
   → fonte viva/read-only/Brain/SERP/GA4/GSC/GMC/Shopify/Tiny conforme caso

4. Score
   → Growth score de oportunidade ou Shopify score técnico/risco

5. Decisão local
   → descartar, backlog, brief, preview, handoff, packet ou bloqueio

6. Colaboração pontual
   → Growth aciona Shopify quando a hipótese precisa virar superfície Shopify
   → Shopify devolve preview, QA, risco, rollback e readback esperado

7. Approval packet
   → só quando houver write externo/produção/publicação/risco A3-A4

8. Execução escopada
   → somente se Lucas aprovar alvo + payload + limite + rollback

9. Readback/receipt
   → fonte viva depois + receipt no Brain

10. Impact/feedback
   → Growth mede impacto quando aplicável; Shopify registra aprendizado técnico
```

## Roteiro mínimo de uma demanda Growth que precisa Shopify

1. Registrar item em `growth/agentic-os/inbox-growth.md`.
2. Criar oportunidade em `growth/agentic-os/opportunity-ledger.md`.
3. Se o próximo output for Shopify, criar handoff para `shopify/agentic-os/inbox-shopify.md`.
4. Criar item na `shopify/agentic-os/preview-queue.md`.
5. Shopify prepara preview/diff/QA/rollback/readback.
6. Se envolver write, gerar approval packet consolidado.
7. Com aprovação escopada, o agente executor aplica exatamente o escopo aprovado.
8. Shopify salva receipt/readback/rollback.
9. Growth agenda impact review quando o impacto for mensurável.
10. Ambos registram feedback se houver aprendizado.

## Roteiro mínimo de uma demanda que começa no Shopify

1. Registrar item em `shopify/agentic-os/inbox-shopify.md`.
2. Se for apenas superfície técnica, seguir preview queue.
3. Se houver dúvida de impacto comercial/SEO/GEO/CRO, criar handoff para LK Growth.
4. Growth devolve hipótese/score ou bloqueia por falta de evidência.
5. Shopify só pede aprovação quando preview/diff/rollback/readback estiverem claros.

## Critérios de bloqueio

Bloquear e devolver como gap report quando:

- objeto Shopify exato não existe;
- fonte viva necessária está ausente;
- Tiny/estoque/preço/disponibilidade não foi verificado quando relevante;
- preview/diff não é claro;
- rollback não está definido;
- readback não é verificável;
- Lucas disse apenas `seguir` e a próxima etapa é write externo/produção.

## Saída curta para Telegram

Quando precisar Lucas, enviar só decisão acionável:

```text
[LK Growth/Shopify] Pedido de aprovação
Alvo: [objeto exato]
Mudança: [1-2 linhas]
Risco: [baixo/médio/alto]
Rollback: [sim/não + onde]
Readback: [como verifico]
Não aprovado ainda: [limites]
Responder: aprovo [escopo] / ajustar / bloquear
```

## Critério de aceite do fluxo

- Toda demanda tem inbox.
- Toda oportunidade tem score ou motivo de não-score.
- Todo write potencial passa por preview queue.
- Toda aprovação declara escopo exato.
- Toda execução aprovada gera readback e receipt.
- Todo aprendizado relevante volta para feedback ledger ou skill/rotina.
