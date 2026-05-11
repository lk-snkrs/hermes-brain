# LK Campaign Attribution Dictionary — v0.2 influencer × produto × estoque

Status: dicionário read-only operacionalizado a partir dos relatórios versionados. Não cria campanha, não altera Meta/Google/Shopify/Tiny, não envia mensagem e não autoriza compra/reposição sem aprovação de Lucas.

Gerado em: `2026-05-11` a partir de artefatos do Brain. Recorte principal Shopify/Tiny: `2026-02-09..2026-05-10`. Recorte Meta/Shopify ROAS: `2025-12-01..2026-05-10`.

## Fontes
- `reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.md`
- `reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.json`
- `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`
- `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`
- `areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-seed-v0.md`

## Regras operacionais v0.2
- Shopify é a verdade de pedidos/receita/produto/SKU/variante; Tiny `LK | CONTROLE ESTOQUE` é a verdade de estoque.
- Meta attributed ROAS é diagnóstico de plataforma, não verdade operacional de venda.
- Influencer vira acionável quando há ponte Shopify forte: cupom, UTM, landing/referrer, note attribute ou ad_id/utm_content compatível.
- Toda linha de produto deve carregar **nome + SKU + tamanho**. Quando o SKU está ausente, a consequência não é compra: é corrigir/mapear SKU.
- Decisão de estoque usa consequência por SKU/tamanho: `ruptura agora`, `baixo estoque`, `ok/monitorar`, `mapear SKU no Tiny`, `sem SKU no Shopify`.
- Lala permanece investigação: Meta mostra spend/compra atribuída, mas Shopify não trouxe ponte direta no recorte.

## silvia_heinz_v02

- status: `validated_stock_actionable`
- influencer_name: Silvia Heinz
- influencer_handle: `[a confirmar]`
- platform: Meta Ads + Shopify evidence + Tiny read-only
- commercial_window: Shopify/Tiny `2026-02-09..2026-05-10`; Meta/ROAS `2025-12-01..2026-05-10`
- Meta platform signal: spend R$ 50.311,49; compras Meta 822; valor Meta R$ 2.560.642,92; ROAS plataforma 50,90x
- Shopify/Tiny matrix: pedidos casados 117; linhas produto/SKU únicas 122
- Receita de linhas ranqueadas na matriz: R$ 429.291,45; unidades: 147
- Consequência estoque agregada: ruptura agora: 86, sem SKU no Shopify: 23, baixo estoque: 6, ok/monitorar: 1, mapear SKU no Tiny: 6

### Naming/ad patterns conhecidos
- campaign: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )` | adset: `RMKT (Site + Instagram + Vídeo)` | ad: `[influencer Silvia start 11.12.25- RMKT]`
- campaign: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)` | adset: `Simples | Vendas Advantage+ [clube do sky]` | ad: `[influencer Silvia start 11.12.25- Adv geral] — — Cópia`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Pareto.Vendas-Adv [ Campanha Nova]` | ad: `[influencer Silvia | start 20-12-25 | Camp Onitsuka] — Cópia`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Stories` | ad: `[influencer Silvia | start 20-12-25 | Onitsuka Sabot Stories 3]`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Stories` | ad: `[influencer Silvia | start 15-12-25 | New Balance 204L Stories 1]`

### Produtos/SKUs/tamanhos acionáveis
- **Tênis Nike Air Jordan 4 Retro Metallic Gold Branco / SKU AQ9129-170-7 / tam. 40** — vendido 4 un.; receita R$ 13.399,96; evidência discount_code:4; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-38 / tam. 38** — vendido 3 un.; receita R$ 14.999,97; evidência discount_code:3; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 37** — vendido 3 un.; receita R$ 14.999,97; evidência discount_code:2, landing_site:2; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **sem SKU no Shopify**
- **Tênis Onitsuka Tiger Mexico 66 White Black Branco / SKU 1183A201-126-3 / tam. 36** — vendido 3 un.; receita R$ 7.199,97; evidência discount_code:3; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom / SKU HV8547-200-38 / tam. 38** — vendido 2 un.; receita R$ 11.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-8 / tam. 41** — vendido 2 un.; receita R$ 11.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-39 / tam. 39** — vendido 2 un.; receita R$ 9.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-38 / tam. 38** — vendido 2 un.; receita R$ 9.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 36** — vendido 2 un.; receita R$ 9.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **sem SKU no Shopify**
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU [sem SKU no Shopify] / tam. 36** — vendido 2 un.; receita R$ 9.999,98; evidência discount_code:2; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **sem SKU no Shopify**

### Decisão v0.2
- Leitura: influencer já acionável para Jacquemus/Nike, Onitsuka e New Balance, mas há rupturas e SKUs sem vínculo suficiente.
- Próxima ação segura: montar lista curta de reposição/sourcing por SKU/tamanho zerado e lista separada de saneamento SKU. Aprovação necessária antes de compra, contato fornecedor ou alteração Tiny/Shopify.

## helena_lunardelli_v02

- status: `validated_stock_actionable`
- influencer_name: Helena Lunardelli
- influencer_handle: `[a confirmar]`
- platform: Meta Ads + Shopify evidence + Tiny read-only
- commercial_window: Shopify/Tiny `2026-02-09..2026-05-10`; Meta/ROAS `2025-12-01..2026-05-10`
- Meta platform signal: spend R$ 24.364,51; compras Meta 627; valor Meta R$ 1.720.526,49; ROAS plataforma 70,62x
- Shopify/Tiny matrix: pedidos casados 14; linhas produto/SKU únicas 16
- Receita de linhas ranqueadas na matriz: R$ 33.786,84; unidades: 16
- Consequência estoque agregada: sem SKU no Shopify: 2, ok/monitorar: 1, ruptura agora: 11, mapear SKU no Tiny: 2

### Naming/ad patterns conhecidos
- campaign: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )` | adset: `RMKT (Site + Instagram + Vídeo)` | ad: `[influencer Helena | start 07-12-25 | Stories 3] — Cópia`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Stories` | ad: `[influencer Helena | start 07-12-25 | Stories 3]`
- campaign: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)` | adset: `Simples | Vendas Advantage+ [clube do sky]` | ad: `[influencer Helena | start 07-12-25 | Stories 3] — Cópia`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Stories` | ad: `[influencer Helena | start 07-12-25 | Stories 1 ] —`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Stories` | ad: `[influencer Helena | start 07-12-25 | Stories 5] — —`

### Produtos/SKUs/tamanhos acionáveis
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU [sem SKU no Shopify] / tam. 38** — vendido 1 un.; receita R$ 4.999,99; evidência note_attributes:1; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **sem SKU no Shopify**
- **Tênis New Balance 204L Arid Timberwolf Bege / SKU U204LMMC-3 / tam. 36** — vendido 1 un.; receita R$ 2.799,99; evidência landing_site:1, note_attributes:1; Tiny `LK | CONTROLE ESTOQUE`: 2; leitura: **ok/monitorar**
- **Tênis Onitsuka Tiger Mexico 66 SD Vin Clay Canyon Cream Marrom / SKU 1183C015.205-3 / tam. 36** — vendido 1 un.; receita R$ 2.499,99; evidência note_attributes:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis New Balance 9060 Sea Salt Concrete Branco / SKU U9060ECA-10 / tam. 40** — vendido 1 un.; receita R$ 2.499,99; evidência landing_site:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege / SKU 1183C015-202-2 / tam. 35** — vendido 1 un.; receita R$ 2.499,99; evidência landing_site:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege / SKU 1183A872.101-4 / tam. 37** — vendido 1 un.; receita R$ 2.499,99; evidência landing_site:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Onitsuka Tiger Mexico 66 SD Birch Metropolis Bege / SKU 1183C015200 / tam. 36** — vendido 1 un.; receita R$ 2.499,99; evidência discount_code:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege / SKU 1183C015101 / tam. 38** — vendido 1 un.; receita R$ 2.499,99; evidência note_attributes:1; Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-2 / tam. 35** — vendido 1 un.; receita R$ 2.399,99; evidência discount_code:1; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **mapear SKU no Tiny**
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-3 / tam. 36** — vendido 1 un.; receita R$ 2.399,99; evidência note_attributes:1; Tiny `LK | CONTROLE ESTOQUE`: sem saldo confiável; leitura: **mapear SKU no Tiny**

### Decisão v0.2
- Leitura: volume menor, mas sinal consistente em Onitsuka/NB feminino premium; várias linhas já zeradas no Tiny.
- Próxima ação segura: usar como briefing de produto e checar sourcing apenas dos SKUs/tamanhos com ruptura. Aprovação necessária antes de compra/campanha.

## lala_noleto_v02

- status: `ambiguous_meta_signal_only`
- influencer_name: Lala Noleto
- influencer_handle: `[a confirmar]`
- platform: Meta Ads; Shopify evidence direta não encontrada
- commercial_window: Shopify/Tiny `2026-02-09..2026-05-10`; Meta/ROAS `2025-12-01..2026-05-10`
- Meta platform signal: spend R$ 25.750,26; compras Meta 519; valor Meta R$ 1.686.413,85; ROAS plataforma 65,49x
- Shopify/Tiny matrix: pedidos casados 0; linhas produto/SKU únicas 0
- Receita Shopify com ponte direta no recorte: R$ 0,00

### Naming/ad patterns conhecidos
- campaign: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)` | adset: `Simples | Vendas Advantage+ [clube do sky]` | ad: `[influencer Lala noleto] —Simples`
- campaign: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )` | adset: `RMKT (Site + Instagram + Vídeo)` | ad: `[influencer Lala noleto] — RMKT`
- campaign: `Pareto.Vendas-Adv [ Geral]` | adset: `Pareto.Vendas-Adv [ Campanha Nova]` | ad: `[influencer Lala noleto] — Adv geral`
- campaign: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )` | adset: `RMKT (Site + Instagram + Vídeo)` | ad: `[influencer Lala-Nolleto- start 30-04-2026  Adv geral] — DIA DAS MÃES — Cópia`
- campaign: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)` | adset: `Simples | Vendas Advantage+ [clube do sky]` | ad: `[influencer Lala-Nolleto- start 30-04-2026  Adv geral] — DIA DAS MÃES`

### Produtos/SKUs/tamanhos acionáveis
- Nenhum produto/SKU/tamanho Shopify casado por cupom/UTM/landing/note no recorte. Não transformar em compra/estoque até achar ponte real.

### Decisão v0.2
- Leitura: plataforma indica demanda, mas a LK ainda não tem ponte Shopify direta no recorte; qualquer ROAS operacional seria chute.
- Próxima ação segura: descobrir cupom/UTM/landing/brief/ad_id real de Lala e só depois cruzar com Shopify/Tiny.

## Campanhas com match Shopify por UTM strict

### campaign_120210118442410224
- campaign_name: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)`
- family: `advantage/broad`
- Meta: spend R$ 36.296,67; valor atribuído R$ 2.542.659,81; ROAS plataforma 70,05x
- Shopify UTM strict: pedidos 3; receita R$ 10.799,98; ROAS vs spend Meta 0,30x
- Produtos/SKU/tamanho vistos:
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege | 1183A872.101-3 | 36 — qtd 1
  - Tênis New Balance 204L Mushroom Arid Stone Marrom | U204LMMA-4 | 37 — qtd 1
  - Tênis New Balance 530 'Silver Metallic Black Cement' Prateado | U530ESA-9 | 42 — qtd 1
  - New Balance 9060 Black Cement "Black Cat" Preto | U9060ZGE | 37 — qtd 1
  - Tênis Adidas Samba OG Crochet Pack Sand Strata Bege | JR9446-3 | 36 — qtd 1
- Decisão: usar como ponte de campanha, não como influencer específico sem ad/ad_id/utm_content/cupom adicional.

### campaign_120206303993560224
- campaign_name: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )`
- family: `remarketing`
- Meta: spend R$ 32.274,10; valor atribuído R$ 2.320.329,06; ROAS plataforma 71,89x
- Shopify UTM strict: pedidos 6; receita R$ 18.489,97; ROAS vs spend Meta 0,57x
- Produtos/SKU/tamanho vistos:
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege | 1183C015101-14 | 42.5 — qtd 1
  - Tênis Onitsuka Tiger Tiger Corsair A55 Midnight Cream Azul | 1183C317-401-10 | 43 — qtd 1
  - Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | 1183B566021-4 | 37 — qtd 1
  - Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | [sem SKU] | 35.5 — qtd 1
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | [sem SKU] | 43 — qtd 1
- Decisão: usar como ponte de campanha, não como influencer específico sem ad/ad_id/utm_content/cupom adicional.

### campaign_120215662888410224
- campaign_name: `[Pareto] [FUNDO] DABA`
- family: `other`
- Meta: spend R$ 16.526,39; valor atribuído R$ 1.037.493,36; ROAS plataforma 62,78x
- Shopify UTM strict: pedidos 15; receita R$ 41.027,24; ROAS vs spend Meta 2,48x
- Produtos/SKU/tamanho vistos:
  - Camisa Aphase Check - Light Yellow Bege | 20054-3 | L/G — qtd 1
  - Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege | 1183C015-202-9 | 42 — qtd 1
  - Tênis Onitsuka Tiger California 78 EX Monument Blue Cream Azul | 1183A355.405-8 | 41 — qtd 1
  - Tênis New Balance 530 White Natural Indigo Branco | MR530SG-3 | 37 — qtd 1
  - Tênis Nike Moon Shoe SP Jacquemus Off White | [sem SKU] | 38 — qtd 1
- Decisão: usar como ponte de campanha, não como influencer específico sem ad/ad_id/utm_content/cupom adicional.

## Backlog seguro gerado por este dicionário
- Criar visão `repor estoque` separando: ruptura confirmada, baixo estoque, sem SKU Shopify, mapear SKU Tiny.
- Completar handles/cupons oficiais de Silvia, Helena, Lala, Ju Mesquita, Mariah, Arlindo e Maria Fernanda.
- Padronizar naming futuro com `influencer_slug`, `product_theme`, `sku_or_model`, `launch_date` e `utm_content/ad_id` em todos os ads.
- Proibir decisão por `campaign_id/adset_id` genérico; produto vendido por criativo só via ponte segura como ad_id/utm_content/cupom/landing/referrer/note/tag.
- Separar `Pareto-compatible` de `Lucas-operational`: Maria, Maria Fernanda e Mariah ficam separados na visão Pareto-compatible.

## Limites
- Nenhuma campanha/orçamento/criativo foi alterado.
- Nenhum cupom foi criado.
- Nenhum SKU/estoque/preço foi alterado.
- Nenhum cliente/fornecedor/time externo foi contatado.
- Qualquer compra/reposição/envio/campanha exige preview e aprovação explícita de Lucas.
