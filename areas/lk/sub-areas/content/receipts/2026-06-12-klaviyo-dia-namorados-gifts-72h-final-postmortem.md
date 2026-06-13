# Receipt — Pós-mortem final 72h — Klaviyo Dia dos Namorados Gifts by LK

- Data/hora: 2026-06-12T18:06:50.780354+00:00
- Agente/profile/cron: lk-content cron
- Empresa/área: LK Sneakers / Content / CRM / Klaviyo
- Responsável humano: LK Content
- Pedido original: Pós-mortem final 72h da campanha Klaviyo 01KTPR0M219KB1ZPR89JNP5YGH, somente leitura.
- Classificação: read-only
- Fontes usadas:
- Klaviyo API read-only via Doppler lc-keys/prd; campaign-values report 72h com Placed Order Shopify; eventos Clicked Email; receipt 24h anterior; playbook de métricas duplicadas Klaviyo.
- O que foi feito:
- Consultadas métricas finais 72h, corrigido conversion_metric_id para Placed Order/Shopify, lidos top clicked links e comparado com 24h; nenhum write externo no Klaviyo.
- Output/artefato:
- Campaign Sent; delivered 5467/5492; open rate 54,05%; click rate 1,39%; 1 pedido atribuído/R$ 2.280; unsub 0,26%; spam 0; cliques concentrados em giftable/tamanho.
- Aprovação: Não exigida: leitura e documentação local. Nenhum envio, agendamento, edição, pausa ou deleção executado.
- Envio/publicação: Sem envio/publicação externa pelo agente; resposta final do cron será entregue pelo sistema.
- Writes externos: nenhum
- Riscos/bloqueios: Klaviyo é sinal auxiliar de atribuição; Shopify/GA4 seguem como fonte de verdade comercial. Pronta entrega/disponibilidade não foi validada por LK Content e não deve ser prometida sem lk-stock.
- Rollback/mitigação: N/A para Klaviyo; documentação local pode ser corrigida por novo receipt ou edição versionada.
- Próximos passos: Repetir compra por tamanho em campanhas giftable, mas testar landing/curadoria mais fechada e segmentação clicked/no purchase; checar atribuição em Shopify/GA4 antes de decisão comercial.
- Onde foi documentado no Brain: Receipt final 72h em content/receipts e atualização do playbook CRM com aprendizado durável.
- Source confidence: runtime-verificado

## Contexto da campanha

- Campaign ID: `01KTPR0M219KB1ZPR89JNP5YGH`
- Nome: `2026-06-09 | Dia dos Namorados | Gifts by LK | 15% off pronta entrega`
- Link UI correto: https://www.klaviyo.com/campaign/01KTPR0M219KB1ZPR89JNP5YGH/wizard/1
- Status API: `Sent`
- Send time: `2026-06-09T18:03:42.016874+00:00` UTC / `2026-06-09 15:03:42` BRT
- Segurança: Doppler `lc-keys/prd`; `values_printed=false`; leitura Klaviyo apenas. Nenhum envio, agendamento, pausa, edição ou deleção.

## Nota de medição importante

A conta LK possui métricas duplicadas de `Placed Order`. A primeira leitura automática usou `Placed Order` / API (`TNNPCi`) e retornou conversão zerada. Para o pós-mortem final foi aplicada a regra do playbook de métricas duplicadas: usar `Placed Order` / Shopify (`VAbhT5`) para conversão atribuída de ecommerce. Com a métrica correta, a campanha mostra 1 pedido atribuído e R$ 2.280,00 de receita.

## Métricas finais 72h disponíveis

| Métrica | 24h | 72h final | Leitura |
|---|---:|---:|---|
| Recipients / sent | 5.485 | 5.492 | Base praticamente estável; Klaviyo report ajustou recipients/bounces após assentamento |
| Delivered | 5.467 | 5.467 | Entrega final forte |
| Delivery rate | 99,67% | 99,55% | Sem problema relevante de entregabilidade |
| Opens totais | 2.980 | 3.585 | Abertura seguiu crescendo após 24h |
| Opens únicos | 2.563 | 2.955 | 54,05% open rate final |
| Open rate | 46,88% | 54,05% | Tema/assunto geraram alta atenção |
| Clicks totais | 98 | 103 | Pouco crescimento pós-24h |
| Clicks únicos | 72 | 76 | 1,39% click rate |
| Click rate | 1,32% | 1,39% | Interesse clicável baixo diante da abertura |
| Click-to-open rate | 2,81% | 2,57% | Gargalo principal: abriram, mas poucos avançaram |
| Placed Order / Shopify | 0* | 1 | *24h foi lido antes da correção de métrica duplicada; 72h usa Shopify |
| Conversion value / revenue | R$ 0,00* | R$ 2.280,00 | Receita atribuída existe, mas concentrada em 1 pedido |
| Conversion rate | — | 0,018% | Muito baixo para conversão direta |
| Revenue per recipient | — | R$ 0,42 | Sinal comercial positivo, porém pequeno |
| AOV atribuído | — | R$ 2.280,00 | Ticket alto; não extrapolar sem Shopify/GA4 |
| Unsubscribes | 14 | 14 | Não piorou após 24h |
| Unsubscribe rate | 0,26% | 0,26% | Atenção para campanhas promocionais amplas |
| Spam complaints | 0 | 0 | Sem sinal crítico |
| Bounced | 18 | 25 | Bounce final 0,46%; ainda administrável |
| Failed | 0 | 0 | OK |

## Top clicked links/produtos — 72h

Leitura de eventos `Clicked Email`: 103 eventos candidatos da campanha, batendo com clicks totais do report. Top links:

1. Giftable tamanho 37: 13 cliques
2. Coleção giftable: 12
3. Giftable tamanho 36: 10
4. Produto Adidas SL72 OG Maroon Almost Yellow: 8
5. Giftable tamanho 33.5: 7
6. Produto New Balance 530 White Natural Indigo: 6
7. Home LK: 6
8. Giftable tamanho 39: 5
9. Giftable tamanho 40: 5
10. Giftable tamanho 38: 4
11. Giftable tamanho 43: 4
12. Giftable tamanho 41: 3
13. Giftable tamanho 34: 3
14. Produto Adidas Samba OG Crochet Pack Sand Strata: 3
15. Produto Adidas Samba OG Cream White Core Black: 3
16. Giftable tamanho 35: 3
17. Produto Nike Dunk Low Cacao Wow: 2
18. TikTok LK: 1
19. Giftable tamanho 39.5: 1
20. Produto New Balance 9060 Sea Salt Concrete: 1

Leitura por intenção: coleção + filtros de tamanho dominaram os cliques. Produtos individuais mais fortes: Adidas SL72 Maroon, NB 530 White/Natural Indigo, Sambas bege/cream e Nike Dunk Cacao Wow.

## Avaliação executiva

### Tema

- `Dia dos Namorados + Gifts by LK` funcionou muito bem para atenção: 54,05% de open rate final.
- O tema é repetível para datas de presente, desde que a campanha seja menos dependente de desconto e mais guiada por curadoria/tamanho.

### Subject / preheader

- Subject usado: `Dia dos Namorados: Gifts by LK`.
- Preview text usado: `15% off em uma seleção pronta para presentear — com envio no mesmo dia para São Paulo capital.`
- Leitura: subject curto, claro e editorial teve boa abertura. O preheader provavelmente ajudou pelo benefício comercial, mas contém claim operacional de envio/pronta entrega; em próximas campanhas, só usar esse tipo de promessa com validação/handoff de `lk-stock` e contexto logístico aprovado.

### Hero / UX

- A decisão de colocar `Compre por tamanho` cedo foi validada pelos cliques: tamanho 37, coleção, tamanho 36 e tamanho 33.5 aparecem no topo.
- O problema não foi descoberta; foi conversão pós-clique. A landing ampla de coleção pode ter gerado dispersão.

### Compra por tamanho

- Repetir como estrutura para campanhas giftable e pronta-entrega-like.
- Melhorar: criar blocos por faixa/numeração com 3–5 escolhas editoriais, em vez de depender só de botões para a coleção filtrada.

### Oferta 15% off

- A oferta ajudou a clareza comercial, mas não foi motor suficiente: 1 pedido em 5.492 recipients e 76 cliques únicos.
- Desconto não deve virar centro da narrativa; usar como suporte quando houver prazo/condição aprovados. Para base premium, a curadoria precisa carregar a intenção.

### Produto / CTA

- CTA de coleção/tamanho superou produto individual. Produtos que puxaram clique têm leitura de presente com cor/forma forte: SL72 Maroon, NB 530 White/Natural Indigo, Sambas neutros.
- Próxima peça deve testar produto-âncora + variações próximas por tamanho, para reduzir a distância entre clique e decisão.

### Segmento

- Envio para `LK News` gerou reach e abertura, mas click rate e unsub sugerem que a segmentação ampla tem custo.
- Próximo follow-up/comparável deve separar: engajados recentes, clicked/no purchase, compradores high-intent e talvez excluir perfis pouco engajados em campanha promocional de data.

## Aprendizado final

### O que repetir

- Ângulo giftable editorial, especialmente para datas de presente.
- Subject direto com nome da ocasião e curadoria LK.
- Compra por tamanho como UX principal logo no hero.
- Links rastreáveis por intenção: coleção, tamanho, produto, social/footer.
- Produtos com leitura de presente clara: cores/ícones fáceis de explicar e modelos reconhecíveis.

### O que evitar

- Depender de desconto como argumento principal.
- Prometer pronta entrega, envio no mesmo dia, tamanho disponível ou disponibilidade sem validação `lk-stock`.
- Landing muito ampla sem curadoria guiada depois do clique.
- Diagnosticar ecommerce como zerado sem checar duplicidade de métricas `Placed Order` por integração.
- Enviar campanhas promocionais amplas para toda a lista sem controle de engajamento quando o objetivo for conversão.

### O que testar na próxima newsletter

1. A/B de subject:
   - editorial: `Presentes que parecem escolha certa`;
   - utilitário: `Escolha o presente pelo tamanho`.
2. Hero com 1 produto-âncora + grade por tamanho, em vez de coleção ampla como primeiro destino.
3. Follow-up para `clicked/no purchase` com curadoria por tamanho clicado, sem claim de disponibilidade sem validação.
4. CTA duplo: `Comprar por tamanho` + `Falar com a LK para escolher`.
5. Segmento mais qualificado: engajados 30/60 dias e exclusão de pouco engajados para reduzir unsub.

## Evidências

- Métricas 72h com leitura automática inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-12T180411Z-klaviyo-campaign-metrics-01KTPR0M219KB1ZPR89JNP5YGH-72h-final.json`
- Métricas 72h corrigidas com `Placed Order` / Shopify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-12T180441Z-klaviyo-campaign-metrics-01KTPR0M219KB1ZPR89JNP5YGH-72h-final-shopify-placed-order.json`
- Click links 72h: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-12T180500Z-klaviyo-click-links-01KTPR0M219KB1ZPR89JNP5YGH-72h-final.json`
- Pós-mortem 24h: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-10-klaviyo-dia-namorados-gifts-24h-postmortem.md`

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
