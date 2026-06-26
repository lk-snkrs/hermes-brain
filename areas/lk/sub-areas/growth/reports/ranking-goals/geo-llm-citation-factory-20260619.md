# LK Growth Ranking OS v2 — GEO/LLM Citation Factory — 2026-06-19

Status: read-only / preview. Writes externos: 0. values_printed=false.

## Veredito

Há uma oportunidade acionável para transformar **New Balance 9060** em uma fonte mais citável para LLMs: a coleção pública já está indexável e com FAQPage, `/llms.txt` já aponta para a collection, mas não há um guia/source page dedicado vivo para capturar perguntas comparativas e comerciais como “qual a diferença entre New Balance 9060 e 530?” e “qual cor de New Balance 9060 escolher?”.

Oportunidade é **preview-only / não executada**. Qualquer publicação de guia, alteração de collection, FAQ/schema ou `llms.txt` público exige aprovação explícita atual.

## Fontes verificadas nesta execução

- Data/hora: 2026-06-19 11:32–11:40 UTC.
- AI endpoints públicos via fetch read-only:
  - `https://lksneakers.com.br/llms.txt` — 200, ~17.5 KB, contém `new-balance-9060`, `source map`; termos operacionais encontrados apenas em guardrails de instrução para assistentes (`estoque` 14), sem `pronta entrega`/`encomenda`.
  - `https://lksneakers.com.br/llms-full.txt` — 200, ~120 KB, contém `new-balance-9060`, sem termos proibidos encontrados.
  - `https://lksneakers.com.br/agents.md` — 200, contém `new-balance-9060` e source map; `estoque` aparece em guardrails de não inferência.
  - `robots.txt` — AI crawlers mencionados e permitidos com restrição de admin/cart/checkout: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot.
- Página pública:
  - `https://lksneakers.com.br/collections/new-balance-9060` — 200, H1 único `New Balance 9060`, title `New Balance 9060 original | Curadoria LK Sneakers`, meta com curadoria/autenticidade/atendimento humano, 4 blocos JSON-LD incluindo `CollectionPage`, `ItemList`, `BreadcrumbList`, `FAQPage`.
- Brain / evidência comercial:
  - `areas/lk/sub-areas/collection-optimizer/approval-packets/20260618T214500Z-ai-visibility-waves-a-b-approval-packet.md` classifica New Balance 9060 como P0: “maior gap comercial identificado”; múltiplos SKUs vendidos nos últimos 60 dias (Mushroom Arid Stone 13 un., Rich Oak 10 un., Bisque Sea Salt 9 un., Sea Salt Moonbeam 7 un., Triple White 6 un., Angora Sea Salt 6 un.).
- GSC/Google:
  - `python3 scripts/lk_search_console_readonly_router_20260511.py` retornou dados vivos para 2026-05-20 a 2026-06-16: 25.000 linhas query/página, 11.898 páginas, 40 oportunidades. New Balance 9060 não apareceu no Top 12 GSC desta execução, então a priorização aqui vem principalmente de Shopify/comercial + lacuna GEO/source-page.
- Limitação:
  - DataForSEO MCP/web_search não estavam expostos nesta sessão; secrets DataForSEO existem no Doppler por nomes esperados, mas sem ferramenta MCP ativa/cost guardrail local nesta execução. SERP/PAA live externo ficou limitado. Relatório: **parcial, não full decision-grade para SERP**, mas suficiente para preview de conteúdo/approval packet.

## Pergunta/tema alvo

**Tema alvo:** `New Balance 9060 original no Brasil — diferença entre 9060 e 530, conforto, colorways e como escolher`.

**Pergunta principal:** `Qual a diferença entre New Balance 9060 e 530?`

Motivo: pergunta comparativa real já aparece na página pública/FAQ, tem intenção comercial clara, ajuda LLMs a explicar a escolha do modelo e conecta dois clusters com venda recorrente.

## Página alvo

- Página atual a reforçar: `https://lksneakers.com.br/collections/new-balance-9060`.
- Página editorial recomendada se Lucas aprovar publicação: `https://lksneakers.com.br/pages/guia-new-balance-9060`.
- Link interno recomendado: collection → guia editorial; guia → collection; comparação interna com `/collections/new-balance-530` quando o guia existir.

## Bloco citável proposto — answer-first

> O New Balance 9060 é a leitura mais escultural da linha 99X da New Balance: mistura referências do 990, 860 e da estética running dos anos 2000 em uma sola mais alta, visual curvo e proporção marcante. Ele faz sentido para quem quer um sneaker confortável, mas com presença visual maior que um 530 ou 2002R. Na curadoria LK, o 9060 aparece em colorways como Mushroom, Rich Oak, Sea Salt, Moonbeam, Triple White e Angora, escolhidas para looks urbanos, alfaiataria casual e propostas de luxo discreto. Para decidir entre versões, o ponto principal é a intenção de uso: neutros claros deixam o volume mais leve; marrons e tons terrosos reforçam a leitura premium; colorways contrastadas tornam o par protagonista. No Brasil, a LK orienta a escolha com atendimento humano, autenticidade e comparação entre modelos.

Contagem: 134 palavras, dentro da faixa GEO recomendada de 134–167 palavras.

## FAQ Real Intent Gate

| Pergunta | Fonte de intenção | generic-filler |
|---|---|---|
| Qual a diferença entre New Balance 9060 e 530? | comparação entre versões + FAQ visível atual + objeção comercial | false |
| O New Balance 9060 é confortável para uso diário? | objeção comercial + material/silhueta/uso | false |
| Qual cor de New Balance 9060 escolher? | styling + colorways com evidência comercial no Brain | false |
| Como saber se o New Balance 9060 é original? | autenticidade específica + risco de compra premium | false |

Guardrail: não incluir perguntas sobre estoque, pronta entrega, encomenda, prazo operacional ou disponibilidade como SEO/GEO.

## Schema / entity clarity / links internos

- Se for apenas ajuste de collection: manter **um único FAQ visível** e **um único FAQPage JSON-LD correspondente**, sem duplicar FAQ legado.
- Se virar guia editorial: usar `Article`/`WebPage` + `FAQPage` apenas se as perguntas estiverem visíveis no guia; incluir `Organization/ShoeStore` já existente como entidade LK.
- Entidades a preservar: `New Balance`, `New Balance 9060`, `New Balance 530`, `990`, `860`, `2002R`, `Mushroom`, `Rich Oak`, `Sea Salt`, `Moonbeam`, `Triple White`, `Angora`, `LK Sneakers`.
- Links internos propostos:
  - Guia → `/collections/new-balance-9060` com CTA comercial discreto.
  - Guia → `/collections/new-balance-530` para comparação.
  - Collection → guia quando publicado.
  - `/llms.txt`/`agents.md` → adicionar link do guia somente após URL estar viva e QA aprovada.

## Impacto esperado

- AI visibility: melhora chance de `text_citation` para perguntas comparativas e comerciais, em vez de apenas presença como merchant/product surface.
- Google: reforça long-tail comparativa e intenção de decisão (`9060 vs 530`, conforto, colorways, originalidade) sem depender de repetir copy genérica na collection.
- Comercial: New Balance 9060 é P0 no packet de 2026-06-18 por vendas distribuídas em várias colorways; guia ajuda compra assistida e reduz fricção de escolha.

## Approval packet resumido

**Aprovação necessária para executar qualquer produção:**

> Aprovo preparar/publicar o guia editorial `guia-new-balance-9060` e/ou ajustar a collection `/collections/new-balance-9060` apenas com o bloco citável, FAQ Real Intent Gate, schema correspondente e links internos descritos no relatório `geo-llm-citation-factory-20260619.md`, sem alterar produtos, preço, estoque, desconto, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout ou theme production fora do escopo, com backup, QA público, rollback e revisão D+7/D+14.

Sem aprovação, próximo passo seguro é: criar draft local completo do guia/FAQ/schema e checklist QA para revisão, sem publicar.

## O que não foi feito

- Nenhum Shopify write.
- Nenhum theme production write.
- Nenhum GMC/feed write.
- Nenhum GA4/GSC config write ou Indexing API submit.
- Nenhum anúncio, Klaviyo, WhatsApp, preço, estoque, desconto ou ação customer-facing.
- Nenhuma consulta de estoque.
