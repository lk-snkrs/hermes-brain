# Handoff — LKGOC Onitsuka Tiger broad collection — execução item 2 — 2026-06-09

Status: **handoff local / preview-only / sem write externo**  
Criado em: 2026-06-09 14:15 UTC  
Origem: LK Growth  
Destino: **[LK] Otimização de Coleção**

## Por que é LKGOC

A oportunidade envolve coleção, copy, FAQ, source/guide, internal linking e possível ajuste `llms.txt`/`llms-full.txt`. Pela regra LK Growth, Growth entrega evidência e packet; execução visual/textual de coleção fica com **[LK] Otimização de Coleção**.

## URL

`https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`

## Evidência verificada

- GSC: **36.261 impressões / 194 cliques / CTR 0,54% / posição 7,5** em queries posição 4–15.
- Query principal `onitsuka tiger`: **24.395 impressões / 73 cliques / CTR 0,30% / posição 8,3**.
- GA4 orgânico: **879 sessões / 787 usuários / 1.787 pageviews / engagement 77,5%**.
- URL Inspection: indexada, canonical OK, mobile crawl OK.
- Fetch público: collection já tem guia editorial, FAQ e orientação humana.
- DataForSEO `onitsuka tiger`: volume Brasil **33.100**, intenção **transactional**, tendência mensal **+22%**.
- DataForSEO `onitsuka tiger mexico 66`: volume Brasil **6.600**, intenção **transactional**.
- SERP mobile: LK aparece organicamente em **rank absoluto 9** para `onitsuka tiger`; PAA inclui “Tem Onitsuka Tiger no Brasil?”, “Qual a relação entre Onitsuka Tiger e Asics?”, “Quanto custa um Onitsuka Tiger no Japão?”, “Quem é Onitsuka Tiger?”.
- Shopping/Popular Products: LK aparece como seller em produtos Onitsuka, sinal de merchant visibility.
- GEO gap: `agents.md` contém broad collection, mas `llms.txt`/`llms-full.txt` priorizam Mexico 66 e não listam broad `onitsuka-tiger-todos-os-modelos`.

## Hipótese

A página já é tecnicamente boa, mas ainda captura pouco clique na query broad. O ganho provável está em:

- reforçar a resposta direta “Onitsuka Tiger original no Brasil”;
- diferenciar Onitsuka Tiger vs ASICS sem parecer genérico;
- explicar Mexico 66, SD, Sabot e Slip-on em linguagem de compra;
- alinhar `llms.txt`/`llms-full.txt` com a URL broad que recebe maior demanda orgânica.

## Brief para o owner LKGOC

Preparar preview dev-first com:

1. Bloco citável de 134–167 palavras para `Onitsuka Tiger original no Brasil`.
2. FAQ orientado às perguntas da SERP:
   - Tem Onitsuka Tiger no Brasil?
   - Qual a relação entre Onitsuka Tiger e ASICS?
   - Qual Onitsuka Tiger escolher primeiro?
   - Mexico 66, SD, Sabot ou Slip-on: qual a diferença?
   - Como confirmar tamanho/modelo com atendimento humano?
3. Revisão de linkagem interna broad collection ↔ Mexico 66 ↔ guia/source.
4. Proposta de inclusão da broad collection em `llms.txt` e `llms-full.txt`.
5. QA mobile/desktop e schema FAQPage/CollectionPage/ItemList.

## Copy direction — não final

Tom: premium, objetivo, curadoria, autenticidade e orientação humana.  
Evitar linguagem de estoque/pronta entrega/prazo no conteúdo público da coleção.

## Métrica esperada

- CTR `onitsuka tiger`: de **0,30%** para primeiro alvo **>0,60%**.
- Posição média broad: buscar faixa **<7**.
- Sessões orgânicas collection.
- AI visibility separada por `text_citation`, `merchant_card`, `not_visible`.

## Risco e rollback

- Risco: médio, por alteração visível de coleção/FAQ/schema/llms.
- Rollback: snapshot de collection description, SEO fields, snippets/sections, `llms.txt`/`llms-full.txt`, schema e HTML público.
- Produção só com aprovação explícita de Lucas após preview.

## Approval surface

> Lucas, aprova [LK] Otimização de Coleção preparar preview dev-first de Onitsuka broad com bloco citável, FAQ/schema e proposta `llms.txt`, sem produção?
