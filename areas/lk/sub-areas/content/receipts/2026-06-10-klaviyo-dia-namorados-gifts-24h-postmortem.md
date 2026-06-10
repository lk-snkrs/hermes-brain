# Receipt — Pós-mortem 24h — Klaviyo Dia dos Namorados Gifts by LK

- Data/hora: 2026-06-10T18:06:23.857724+00:00
- Agente/profile/cron: lk-content cron
- Empresa/área: LK Sneakers / Content / CRM / Klaviyo
- Responsável humano: LK Content
- Pedido original: Pós-mortem inicial 24h da campanha Klaviyo 01KTPR0M219KB1ZPR89JNP5YGH, somente leitura.
- Classificação: read-only
- Fontes usadas:
- Klaviyo API read-only via Doppler lc-keys/prd; receipts JSON 2026-06-10T180329Z métricas e 2026-06-10T180503Z click links; check 2h 2026-06-09T200458Z.
- O que foi feito:
- Consultadas métricas 24h de campanha e eventos Clicked Email; comparado contra hipótese Gifts by LK / 15% off até 12/06 / pronta entrega / compra por tamanho / CTA giftable + WhatsApp; sem write externo no Klaviyo.
- Output/artefato:
- Campaign Sent; delivered 5467/5485; open rate 46.88%; click rate 1.32%; 0 placed orders/revenue; unsub 0.26%; spam 0; top cliques concentrados em giftable e filtros de tamanho.
- Aprovação: Não exigida: leitura e documentação local. Nenhum envio/agendamento/edição/pausa/deleção executado.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: nenhum
- Riscos/bloqueios: Receita/conversões podem depender de janela de atribuição e integração Shopify/Klaviyo; pronta entrega é tema criativo, sem validação própria de disponibilidade/estoque por LK Content.
- Rollback/mitigação: N/A para Klaviyo; documentação local pode ser corrigida por novo receipt ou edição versionada.
- Próximos passos: Reavaliar em 72h; se receita continuar zerada, checar atribuição/UTM e considerar campanha de follow-up segmentada por clicked/no purchase.
- Onde foi documentado no Brain: Receipt detalhado 24h em content/receipts e JSONs sanitizados anexos.
- Source confidence: runtime-verificado

## Contexto da campanha

- Campaign ID: `01KTPR0M219KB1ZPR89JNP5YGH`
- Nome: `2026-06-09 | Dia dos Namorados | Gifts by LK | 15% off pronta entrega`
- Link UI: https://www.klaviyo.com/campaign/01KTPR0M219KB1ZPR89JNP5YGH/wizard/1
- Status API: `Sent`
- Send time: `2026-06-09T18:03:42.016874+00:00` UTC / `2026-06-09 15:03:42` BRT
- Segurança: Doppler `lc-keys/prd`; `values_printed=false`; nenhum secret impresso; Klaviyo somente leitura.

## Métricas 24h disponíveis

| Métrica | 2h | 24h | Leitura |
|---|---:|---:|---|
| Recipients / sent | 5.485 | 5.485 | Base estável |
| Delivered | 5.467 | 5.467 | Entrega forte |
| Delivery rate | 99,67% | 99,67% | Sem problema de entregabilidade |
| Opens totais | 1.010 | 2.980 | Abertura continuou crescendo |
| Opens únicos | 925 | 2.563 | 46,88% open rate |
| Open rate | 16,92% | 46,88% | Assunto/ocasião puxaram atenção |
| Clicks totais | 52 | 98 | Cliques quase dobraram vs 2h |
| Clicks únicos | 36 | 72 | 1,32% click rate |
| Click rate | 0,66% | 1,32% | Interesse existe, mas baixo vs abertura |
| Click-to-open rate | 3,89% | 2,81% | Queda relativa: abertura ampliou mais que clique |
| Placed Order / conversions | 0 | 0 | Sem compra atribuída até 24h |
| Conversion value / revenue | R$ 0,00 | R$ 0,00 | Receita atribuída zerada |
| Unsubscribes | 7 | 14 | Dobrou com base de abertura maior |
| Unsubscribe rate | 0,13% | 0,26% | Atenção: acima do ideal para campanha de ocasião |
| Spam complaints | 0 | 0 | Sem sinal crítico |
| Bounced | 18 | 18 | 0,33% bounce |
| Failed | 0 | 0 | OK |

## Top clicked links/produtos — eventos `Clicked Email`

A leitura de eventos encontrou 98 eventos candidatos da campanha; o total bate com `clicks` da campanha. Top links:

1. Coleção giftable: 11 cliques
2. Giftable tamanho 37: 10
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

Leitura por intenção: coleção + filtros de tamanho somam a maior concentração de cliques. Produtos individuais mais fortes: Adidas SL72 Maroon, NB 530 White/Natural Indigo e Sambas bege/cream.

## Fato

- A campanha foi enviada e confirmada como `Sent` via API.
- Entrega: 5.467 de 5.485 recipients, 99,67%.
- Abertura em 24h: 2.563 únicos / 46,88%.
- Clique em 24h: 72 únicos / 1,32%; 98 cliques totais.
- Conversão Klaviyo/Placed Order: 0 pedidos, R$ 0,00 atribuído.
- Descadastro: 14 / 0,26%; spam complaint: 0.
- Top cliques validam interesse em navegação giftable por tamanho.

## Interpretação

- A hipótese de ocasião/assunto funcionou para abrir: Dia dos Namorados + Gifts by LK gerou atenção alta.
- O gargalo está entre abertura e clique/compra: click-to-open de 2,81% e receita zerada indicam que o interesse editorial/promocional não virou intenção de compra suficiente em 24h.
- A navegação por tamanho parece ser o elemento mais útil da experiência: o usuário clicou bastante em filtros de tamanho, sugerindo comportamento de presente prático (“preciso acertar numeração”).
- A oferta `15% off` e `pronta entrega` não foi suficiente, sozinha, para gerar pedido atribuído no Klaviyo até agora. Como `pronta entrega` envolve disponibilidade/estoque, LK Content não valida disponibilidade final nem deve prometer sem handoff ao lk-stock.
- Descadastro de 0,26% merece cuidado: pode haver sensibilidade da base a campanhas muito promocionais/de ocasião ou a amplitude de segmentação.

## Aprendizado

- Para campanhas giftable, manter `compra por tamanho` como UX/CTA relevante, mas combinar com curadoria mais fechada ou produto-âncora para reduzir dispersão pós-clique.
- Em follow-up, priorizar segmento `clicked/no purchase` e personalizar por intenção: quem clicou em tamanho recebe curadoria por tamanho; quem clicou em produto recebe variação de produto/alternativas próximas.
- Para aprender melhor, todo próximo envio giftable deveria ter UTMs e links nomeados por bloco/intenção: coleção, tamanho, produto, WhatsApp, social/footer.
- Aprendizado durável registrado no playbook CRM: `areas/lk/sub-areas/crm/rotinas/playbook-newsletter-klaviyo-lk.md`.

## Próxima recomendação

1. Fazer leitura 72h antes de declarar performance final.
2. Se 72h continuar com receita zerada, abrir checagem de atribuição/UTM e qualidade de landing da coleção giftable.
3. Considerar follow-up curto, somente se aprovado, para `clicked/no purchase` com ângulo consultivo: “Escolha pelo tamanho, finalize com atendimento humano”, sem prometer disponibilidade final.
4. Para qualquer claim real de pronta entrega/tamanho disponível, acionar `lk-stock` antes de usar como fato operacional.

## Evidências

- Métricas 24h JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-10T180329Z-klaviyo-campaign-metrics-01KTPR0M219KB1ZPR89JNP5YGH-24h.json`
- Click links 24h JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-10T180503Z-klaviyo-click-links-01KTPR0M219KB1ZPR89JNP5YGH-24h.json`
- Check 2h JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/2026-06-09T200458Z-klaviyo-campaign-metrics-01KTPR0M219KB1ZPR89JNP5YGH-2h-initial.json`

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
