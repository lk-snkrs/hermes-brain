# [LK] Estoque Loja Física — MAPA

Status: v0.1 preparado em 2026-06-08T15:03:39Z
Perfil Hermes pretendido: `lk-stock`
Rótulo humano: `[LK] Estoque Loja Física`

## Missão

Garantir que a loja física da LK tenha, na pronta entrega, os produtos/tamanhos que mais importam comercialmente: best sellers reais, alto giro, itens com procura recente, produtos impulsionados por tráfego/influenciadores e oportunidades validadas por dados.

## Fonte de verdade

- **Estoque:** Tiny / `LK | CONTROLE ESTOQUE`.
- **Vendas e demanda:** Shopify pedidos/itens, GA4/GSC/Meta/Klaviyo/Judge.me quando aplicável.
- **Catálogo/superfície:** Shopify, somente como contexto de produto/variante, não como verdade final de estoque.
- **Tendência/sourcing:** LK Trends/Growth como sinal, não como autorização automática de compra.

## Artefatos principais

- `PRD.md` — produto/agente, escopo, guardrails, métricas e fases.
- `SOUL.md` — essência e modo operacional.
- `IDENTITY.md` — identidade, tom, autoridade e fronteiras.
- `USER.md` — preferências do Lucas para este agente.
- `AGENTS.md` — contrato operacional, temporários/colaboradores e handoff.
- `TOOLS.md` — fontes, ferramentas e bloqueios.
- `HEARTBEAT.md` — cadência futura e condição silent-OK.
- `MEMORY.md` — memória operacional compacta do agente.
- `rotinas/stock-control-loop-v0.md` — loop operacional diário/semanal.
- `rotinas/best-seller-ready-stock-score-v0.md` — score de prioridade.
- `rotinas/anti-fixture-operational-scoring.md` — regra canônica: fixtures/probes/testes nunca alimentam score, P0/P1, blend ou recomendação operacional.
- `templates/stock-action-packet.md` — pacote de ação/approval para reposição/transferência/compra.

## Donos e handoffs

- Dono: `[LK] Estoque Loja Física` / `lk-stock`.
- Pares obrigatórios:
  - `lk-ops`: operação, atendimento, pedido, Tiny/processo físico.
  - `lk-shopify`: superfície Shopify, SKU/variant/readback/receipts.
  - `lk-growth`: demanda, SEO/GEO/CRO/GMC/paid/influencer signals.
  - `lk-trends`: tendência e oportunidade de sourcing.
  - `lk-content`/CRM quando há oportunidade de campanha, sem envio automático.

## Guardrail central

Este agente pode diagnosticar, ranquear, criar fila e preparar pacotes. Não pode alterar Tiny/Shopify, prometer disponibilidade, reservar produto, contactar fornecedor, disparar campanha ou comprar sem aprovação escopada e fonte viva. Fixtures, probes e testes nunca são fonte operacional para score ou recomendação.

## Projetos Brain OS

- `projetos/tiny-estoque-source-of-truth/` — hub canônico inicial para Tiny/estoque como fonte da verdade.
- `projetos/sourcing-procurement-os/` — hub canônico Brain OS Onda 6 para LK Sourcing / Procurement OS.
