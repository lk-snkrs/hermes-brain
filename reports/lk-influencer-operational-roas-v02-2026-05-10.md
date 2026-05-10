# LK Influencer Operational ROAS — v0.2 read-only

Data: 2026-05-10  
Escopo: Lala Noleto, Silvia Heinz e Helena Lunardelli  
Status: relatório read-only/documental; não altera Meta, Shopify, Tiny, Notion, Klaviyo, WhatsApp, n8n ou campanhas.

## Objetivo

Aprofundar o dicionário canônico de influencers/campanhas da LK e separar:

1. **Meta attributed ROAS** — valor atribuído pela plataforma Meta.
2. **Shopify evidence revenue** — receita encontrada na Shopify por evidência textual/cupom/UTM/landing/note/referrer.
3. **Operational ROAS provisório** — Shopify evidence revenue / spend Meta relacionado ao mesmo influencer no recorte analisado.

Este relatório ainda não é autorização de verba, campanha, compra ou reposição. Ele só reduz ambiguidade para a próxima rodada de decisão.

## Fontes versionadas usadas

- `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`
- `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`
- `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`
- `areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-seed-v0.md`

## Janela

- Período comercial usado nos relatórios-base: `2025-12-01` a `2026-05-10`.
- O recorte é agregado/read-only e depende dos padrões de naming/cupom/UTM já encontrados nos relatórios-base.

## Resumo executivo

### Silvia Heinz

- Status: **melhor caso para ROAS operacional provisório**.
- Spend Meta relacionado: **R$ 50.311,49**.
- Valor atribuído Meta: **R$ 2.560.642,92**.
- Meta attributed ROAS: **50,90x**.
- Shopify evidence revenue: **R$ 650.658,20**.
- Pedidos Shopify com evidência textual: **209**.
- Evidências encontradas: `discount_code`, `landing_site`, `note_attributes`.
- Operational ROAS provisório: **12,93x**.
- Leitura: performance operacional parece forte mesmo depois de trocar valor atribuído Meta por evidência Shopify, mas ainda precisa separar campanhas Jacquemus vs Onitsuka antes de decisão de produto/estoque.

### Helena Lunardelli

- Status: **mapeada com evidência, mas mais sensível a mistura com tráfego genérico ADV+**.
- Spend Meta relacionado: **R$ 24.364,51**.
- Valor atribuído Meta: **R$ 1.720.526,49**.
- Meta attributed ROAS: **70,62x**.
- Shopify evidence revenue: **R$ 154.482,04**.
- Pedidos Shopify com evidência textual: **37**.
- Evidências encontradas: `note_attributes`, `discount_code`, `landing_site`.
- Cupom observado: `HELENA10`.
- Operational ROAS provisório: **6,34x**.
- Leitura: há evidência real, mas o custo precisa ser separado entre `Dia das Mães | Helena`, ADV+ e possíveis anúncios genéricos antes de recomendar escala.

### Lala Noleto

- Status: **ambígua; não usar para decisão operacional ainda**.
- Spend Meta relacionado: **R$ 25.750,26**.
- Valor atribuído Meta: **R$ 1.686.413,85**.
- Meta attributed ROAS: **65,49x**.
- Shopify evidence revenue encontrada: **R$ 0,00**.
- Pedidos Shopify com evidência textual: **0**.
- Operational ROAS provisório: **0,00x / não conclusivo**.
- Leitura: Lala tem sinal forte de plataforma, mas zero evidência Shopify direta no recorte. O correto é tratar como prioridade de investigação de naming/cupom/UTM, não como campanha vencedora nem perdedora.

## Comparativo rápido

- Silvia + Helena juntas:
  - Shopify evidence revenue: **R$ 805.140,24**.
  - Spend Meta relacionado: **R$ 74.676,00**.
  - Operational ROAS provisório combinado: **10,78x**.
- Lala:
  - Forte no Meta, sem evidência direta Shopify encontrada.

## Produtos e estoque — implicação operacional

### Silvia

Produtos citados nos relatórios-base:

- Tênis Nike Moon Shoe SP Jacquemus Off White.
- Tênis Nike Moon Shoe SP Jacquemus Medium Brown.
- Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto.
- Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege.
- Tênis Onitsuka Tiger Mexico 66 White Black Branco.
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo.
- Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege.
- Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege.

Ação operacional segura: usar Silvia como primeira candidata para `influencer → produto/SKU/tamanho → estoque Tiny LK | CONTROLE ESTOQUE`, mas sem compra/reposição antes de checar SKU+tamanho e lead time.

### Helena

Produtos citados nos relatórios-base:

- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo.
- Tênis adidas Samba Og Supplier Colour Off White Gum Prata.
- Tênis Onitsuka Tiger Mexico 66 SD Vin Clay Canyon Cream Marrom.
- Tênis New Balance 9060 Sea Salt Concrete Branco.
- Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege.
- Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege.
- Tênis Onitsuka Tiger Mexico 66 SD Birch Metropolis Bege.
- Onitsuka Tiger Mexico 66 Paraty Natural Navy Bege.

Ação operacional segura: tratar Helena como campanha com evidência real, mas separar Dia das Mães/ADV+/produto antes de qualquer recomendação de mídia ou estoque.

### Lala

Produto associado: **a confirmar**.  
Ação operacional segura: não atribuir produto, SKU, estoque ou compra à Lala até encontrar cupom/UTM/landing/brief real.

## Atualização recomendada para o dicionário

1. Marcar `Silvia Heinz` como `mapped_operational_roas_provisional`.
2. Marcar `Helena Lunardelli` como `mapped_operational_roas_provisional`.
3. Manter `Lala Noleto` como `ambiguous_meta_signal_only`.
4. Adicionar campos explícitos por influencer:
   - `shopify_evidence_revenue`;
   - `meta_related_spend`;
   - `operational_roas_provisional`;
   - `evidence_gap`;
   - `next_data_question`.

## Perguntas ainda abertas

- Quais são os handles oficiais de Silvia, Helena e Lala usados pela LK?
- Quais cupons oficiais ativos/legados pertencem a cada influencer?
- O naming dos anúncios usa sempre o nome da influencer no `ad_name`, ou às vezes só no `adset_name`/brief interno?
- Existe landing/UTM oficial para Lala que não apareceu no recorte de Shopify?
- Quais criativos/produtos foram efetivamente publicados por Lala?

## Próxima ação segura

Gerar um relatório `Influencer → produto/SKU/tamanho → estoque` começando por **Silvia** e **Helena**, porque já têm evidência Shopify. Lala deve ficar em investigação de dados até aparecer evidência direta.

## O que não foi feito

- Nenhuma campanha foi criada, pausada, escalada ou alterada.
- Nenhum orçamento Meta/Google foi mexido.
- Nenhum WhatsApp, Klaviyo, email, post ou contato externo foi enviado.
- Nenhum estoque, preço, produto, SKU, pedido, Tiny, Shopify, Notion ou n8n foi alterado.
- Nenhuma ação em VPS/Docker/runtime foi executada.
