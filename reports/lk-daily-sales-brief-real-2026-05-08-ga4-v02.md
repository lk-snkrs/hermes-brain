# Daily Sales Brief LK — real read-only v0.2 com GA4

Status: execução real read-only v0.2 com GA4 validado por Lucas.  

> Relatório real agregado/read-only, sem dados pessoais e sem valores de secrets.
> Gerado após aprovação de Lucas para salvar a service account GA4 no Doppler e testar GA4 Data API.
> O arquivo preserva apenas métricas operacionais e nomes de secrets/IDs não sensíveis.

Período: 2026-05-08 00:00–23:59 BRT.  
Fontes consultadas: Shopify Admin API read-only, Tiny API read-only por SKU no depósito **LK | CONTROLE ESTOQUE**, GA4 Data API read-only.  
Dados pessoais: não exportados. Sem nome, email, telefone ou endereço.  
Padrão LK: toda linha operacional de produto deve trazer **nome + SKU**. Quando SKU estiver ausente, marcar `[sem SKU no Shopify]`.  
Regra nova: usar **somente** `LK | CONTROLE ESTOQUE`; todos os outros depósitos ficam em standby e não entram em decisão/relatório operacional.

## 1. Resumo executivo

A LK vendeu **R$ 68.416,85** em **20 pedidos** no dia.

- Online/web: **R$ 33.410,99 / 9 pedidos**.
- Loja física/POS: **R$ 35.005,86 / 11 pedidos**.
- Ticket médio: **R$ 3.420,84**.
- Vs média diária dos últimos 7 dias: receita **+36,1%**, pedidos **+37,3%**.

## 2. Produtos/modelos/tamanhos vendidos, sempre nome + SKU

- Tênis Nike Mind 002 Light Smoke Grey Cinza / SKU HQ4308-003-5 (Nike): 2 un., R$ 6.079,99. Tamanho: 36. LK | CONTROLE ESTOQUE: 0.
- Tênis Nike Air Jordan 1 Low Voodoo Flax and Oil Green Marrom / SKU [sem SKU no Shopify] (Jordan): 1 un., R$ 5.999,99. Tamanho: 44. LK | CONTROLE ESTOQUE: sem_sku.
- Tênis New Balance 9060 Angora Sea Salt Bege / SKU U9060ERB-3 (New Balance): 2 un., R$ 5.199,98. Tamanho: 36. LK | CONTROLE ESTOQUE: 1.
- Tênis New Balance 9060 Rich Oak Marrom / SKU U9060CCC-4 (New Balance): 2 un., R$ 4.679,98. Tamanho: 37. LK | CONTROLE ESTOQUE: 0.
- Tênis Onitsuka Tiger Moage White/White Branco / SKU 1183B555.102-6 (Onitsuka Tiger): 1 un., R$ 3.999,99. Tamanho: 39. LK | CONTROLE ESTOQUE: 0.
- Tênis New Balance 204L Mushroom Arid Stone Marrom / SKU U204LMMA-5 (New Balance): 1 un., R$ 2.799,99. Tamanho: 38. LK | CONTROLE ESTOQUE: 0.
- Tênis New Balance 9060 Bisque Sea Salt Bege / SKU U9060CCB-2 (New Balance): 1 un., R$ 2.799,99. Tamanho: 35. LK | CONTROLE ESTOQUE: 1.
- Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-4 (New Balance): 1 un., R$ 2.599,99. Tamanho: 37. LK | CONTROLE ESTOQUE: -1.
- Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-5 (New Balance): 1 un., R$ 2.599,99. Tamanho: 38. LK | CONTROLE ESTOQUE: 1.
- Tênis Onitsuka Tiger Mexico 66 TGRS Gunmetal/Metropolis Preto / SKU 1182A708.020-4 (Onitsuka Tiger): 1 un., R$ 2.599,99. Tamanho: 37. LK | CONTROLE ESTOQUE: 0.

## 3. Centro de Inteligência de Stock, somente LK | CONTROLE ESTOQUE

### Zerado ou negativo

- Tênis Nike Mind 002 Light Smoke Grey Cinza / SKU HQ4308-003-5 / tam. 36 / vendido 2 un. / LK | CONTROLE ESTOQUE: 0
- Tênis New Balance 9060 Rich Oak Marrom / SKU U9060CCC-4 / tam. 37 / vendido 2 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Onitsuka Tiger Moage White/White Branco / SKU 1183B555.102-6 / tam. 39 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom / SKU U204LMMA-5 / tam. 38 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-4 / tam. 37 / vendido 1 un. / LK | CONTROLE ESTOQUE: -1
- Tênis Onitsuka Tiger Mexico 66 TGRS Gunmetal/Metropolis Preto / SKU 1182A708.020-4 / tam. 37 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege / SKU 1183C015-202-12 / tam. 36.5 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Onitsuka Tiger México 66 SD Birch Peacoat Bege / SKU 1183A872200-9 / tam. 42 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Onitsuka Tiger Mexico 66 Paraty Birch Cream Bege / SKU 1183B601.200-6 / tam. 39 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Nike Sb Dunk Low Pro Triple White Branco / SKU FJ1674-100-2 / tam. 38 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Tênis Onitsuka Tiger Mexico Mid Runner Kids Birch/India INK Bege / SKU 1184A002.200-8 / tam. 32 / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Boné Kith Script Logo Classic Boné Canvas Bege Branco / SKU khw5052-210 / tam. None / vendido 1 un. / LK | CONTROLE ESTOQUE: 0
- Boné Represent Clo Micro Owners Club Jet Black Preto / SKU Rep22 / tam. None / vendido 1 un. / LK | CONTROLE ESTOQUE: 0

### Baixo, mas ainda com saldo

- Tênis New Balance 9060 Angora Sea Salt Bege / SKU U9060ERB-3 / tam. 36 / vendido 2 un. / LK | CONTROLE ESTOQUE: 1
- Tênis New Balance 9060 Bisque Sea Salt Bege / SKU U9060CCB-2 / tam. 35 / vendido 1 un. / LK | CONTROLE ESTOQUE: 1
- Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-5 / tam. 38 / vendido 1 un. / LK | CONTROLE ESTOQUE: 1
- Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom / SKU 1183C102250-5 / tam. 38 / vendido 1 un. / LK | CONTROLE ESTOQUE: 2

### Saldo confortável

- Tênis Adidas Samba OG Crochet Pack Sand Strata Bege / SKU JR9446-5 / tam. 38 / vendido 1 un. / LK | CONTROLE ESTOQUE: 6

### Sem SKU ou sem match no Tiny

- Tênis Nike Air Jordan 1 Low Voodoo Flax and Oil Green Marrom / SKU [sem SKU no Shopify] / tam. 44 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_sku
- Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata / SKU 1183B566021-4 / tam. 37 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-2 / tam. 35 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU [sem SKU no Shopify] / tam. 44 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_sku
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-3 / tam. 36 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU [sem SKU no Shopify] / tam. 36.5 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_sku
- Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege / SKU ONI-3740254-39 / tam. 39 / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado
- Camiseta Represent Clo Storms In Heaven Black Preto / SKU REP-4645470-M / tam. M/M / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado
- Calça Saint Studio Alfaiataria Leve Prega Dupla Marrom / SKU SST-9064286-XL / tam. XL/GG / vendido 1 un. / LK | CONTROLE ESTOQUE: sem_resultado

## 4. Conferência específica — New Balance 204L Mushroom Arid Stone

Fonte: Tiny API read-only, depósito **LK | CONTROLE ESTOQUE**.

- Tênis New Balance 204L Mushroom Arid Stone Marrom - 34 / SKU U204LMMA-1: LK | CONTROLE ESTOQUE 2
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 35 / SKU U204LMMA-2: LK | CONTROLE ESTOQUE 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 36 / SKU U204LMMA-3: LK | CONTROLE ESTOQUE 4
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 37 / SKU U204LMMA-4: LK | CONTROLE ESTOQUE 4
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 38 / SKU U204LMMA-5: LK | CONTROLE ESTOQUE 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 39 / SKU U204LMMA-6: LK | CONTROLE ESTOQUE 3
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 40 / SKU U204LMMA-7: LK | CONTROLE ESTOQUE 4
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 41 / SKU U204LMMA-8: LK | CONTROLE ESTOQUE 3
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 42 / SKU U204LMMA-9: LK | CONTROLE ESTOQUE 1
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 43 / SKU U204LMMA-10: LK | CONTROLE ESTOQUE 1
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 44 / SKU U204LMMA-11: LK | CONTROLE ESTOQUE 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 37.5 / SKU U204LMMA-12: LK | CONTROLE ESTOQUE 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom - 39.5 / SKU U204LMMA-13: LK | CONTROLE ESTOQUE 0
- Tênis New Balance 204L Mushroom Arid Stone Marrom / SKU U204LMMA: LK | CONTROLE ESTOQUE 0

Leitura: o tamanho vendido no briefing foi **New Balance 204L Mushroom Arid Stone / SKU U204LMMA-5 / tam. 38**, e no Tiny via API ele aparece com **LK | CONTROLE ESTOQUE = 0**. Lucas conferiu e aprovou as quantidades do Tiny para esse depósito; portanto a regra operacional fica mantida: usar somente `LK | CONTROLE ESTOQUE` e manter alerta de reposição quando a variante vendida estiver zerada.

## 5. Conversão, GA4 e CRO

Fonte: GA4 Data API read-only, propriedade `properties/348553567` / `Lk Sneakers`.

- Sessões GA4: **3.858**.
- Usuários ativos GA4: **3.311**.
- Total users GA4: **3.531**.
- Compras/ecommerce purchases GA4: **9**.
- Receita de compra GA4: **R$ 23.801,01**.
- Conversão GA4 calculada por compras/sessões: **0,233%**.
- Baseline estratégico Shopify Analytics: **0,13%**.
- Meta v0.1: **0,20%**.
- Leitura: no GA4, o dia ficou **acima da meta de 0,20%**; ainda assim, a meta oficial continua ancorada no Shopify Analytics até a reconciliação Shopify Analytics x GA4.
- Reconciliação inicial: Shopify web registrou **9 pedidos / R$ 33.410,99**; GA4 registrou **9 compras / R$ 23.801,01**. A contagem bate, mas a receita GA4 ficou **-28,8%** abaixo do Shopify web. Provável diferença de tracking/receita atribuída/impostos/frete/desconto; precisa entrar como checagem fixa do briefing.

Top canais/campanhas GA4 por sessões:

- Paid Social / `facebook / paid` / campanha `120210400473720224`: **658 sessões**, **0 compras**, **R$ 0,00**.
- Organic Search / `google / organic` / `(organic)`: **471 sessões**, **1 compra**, **R$ 5.999,99**.
- Direct / `(direct) / (none)` / `(direct)`: **313 sessões**, **2 compras**, **R$ 4.889,99**.
- Cross-network / `google / cpc` / `[PD][FUNDO] Pmax | Search DSA`: **215 sessões**, **1 compra**, **R$ 2.160,00**.
- Paid Social / `facebook / cpc` / `Pareto.Vendas-Adv [ Dia das Mães | Helena] Campanha`: **188 sessões**, **0 compras**, **R$ 0,00**.
- Paid Shopping / `google / cpc` / `Pareto.Shopping`: **172 sessões**, **0 compras**, **R$ 0,00**.
- Paid Social / `facebook / paid` / campanha `120210118442410224`: **147 sessões**, **1 compra**, **R$ 1.599,99**.
- Organic Social / `l.instagram.com / referral`: **119 sessões**, **2 compras**, **R$ 4.951,06**.

Decisão de CoS:

- GA4 está funcionando e deve entrar no Daily Brief v0.2.
- Próximo bloco analítico: separar pago por campanha/influencer/cupom/UTM e cruzar com produto/marca vendida no Shopify.
- Não mexi em Google Ads, Meta Ads, Shopify, campanhas ou tags; leitura foi read-only.

## 6. Recompra / CRM

- Janela 90 dias Shopify consultada: 1100 pedidos.
- Clientes únicos 90 dias: 934.
- Clientes com 2+ pedidos na janela: 102.
- Taxa de recompra 90 dias estimada por Shopify: **10,92%**.
- Meta v0.1 +50%: alvo indicativo **16,38%**.

## 7. Brand Mix Intelligence

- Onitsuka Tiger: R$ 31.699,87 / 13 un, / 46,3% da receita
- New Balance: R$ 20.679,92 / 8 un, / 30,2% da receita
- Nike: R$ 7.679,98 / 3 un, / 11,2% da receita
- Jordan: R$ 5.999,99 / 1 un, / 8,8% da receita
- Adidas: R$ 2.199,99 / 1 un, / 3,2% da receita
- Represent Clo: R$ 1.649,98 / 2 un, / 2,4% da receita
- KITH: R$ 799,99 / 1 un, / 1,2% da receita
- Saint Studio: R$ 619,99 / 1 un, / 0,9% da receita

## 8. O que não foi feito

- Nenhum WhatsApp enviado.
- Nenhum Klaviyo enviado.
- Nenhum fornecedor/revendedor acionado.
- Nenhum item Notion criado.
- Nenhum produto, preço, estoque, tag, tema ou campanha alterado.
- Nenhum cron criado.
- Nenhum dado pessoal exportado.
