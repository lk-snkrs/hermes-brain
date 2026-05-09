# LK Paid Attribution Brief — real read-only v0.3

Período: 2026-05-08

Fontes: GA4 Data API read-only, Shopify Admin API read-only, Meta Ads Insights read-only. Sem PII; sem alteração de campanha, orçamento, Shopify, Tiny, Notion, Klaviyo, WhatsApp ou n8n.

## Leitura executiva

- Shopify web: 9 pedidos / R$ 22.401,02 em pedidos web sanitizados.
- GA4: Paid Social gerou 1.814 sessões, 1 compra(s) e R$ 1.599,99 de receita atribuída.
- GA4: Google pago somando Cross-network + Paid Search + Paid Shopping gerou 848 sessões, 3 compra(s) e R$ 6.359,98 de receita atribuída.
- Meta Ads API funcionou read-only: 94 anúncios com gasto no dia; gasto total Meta R$ 1.253,51; compras reportadas Meta 9; valor reportado Meta R$ 18.239,94.
- Primeiro sinal claro: Meta/Instagram traz muito tráfego, mas GA4 atribuiu poucas compras diretas a Paid Social no dia; parte da venda aparece em Direct/Organic Social/referral, então o funil precisa de reconciliação, não de conclusão apressada.
- Atenção: compras/ROAS do Meta são atribuição da própria plataforma. ROAS absurdo com gasto muito baixo, como Mariah, não deve virar decisão automática; precisa cruzar com Shopify/UTM/cupom.

## GA4 — canais e campanhas

- Paid Social: 1.814 sessões / 1 compra(s) / R$ 1.599,99
- Cross-network: 552 sessões / 3 compra(s) / R$ 6.359,98
- Organic Search: 488 sessões / 1 compra(s) / R$ 5.999,99
- Direct: 313 sessões / 2 compra(s) / R$ 4.889,99
- Paid Shopping: 186 sessões / 0 compra(s) / R$ 0,00
- Organic Social: 149 sessões / 2 compra(s) / R$ 4.951,06
- Paid Search: 110 sessões / 0 compra(s) / R$ 0,00
- Unassigned: 92 sessões / 0 compra(s) / R$ 0,00
- Organic Shopping: 67 sessões / 0 compra(s) / R$ 0,00
- Referral: 30 sessões / 0 compra(s) / R$ 0,00
- Email: 8 sessões / 0 compra(s) / R$ 0,00
- Paid Other: 1 sessões / 0 compra(s) / R$ 0,00

### Campanhas/source-medium com maior sinal

- Organic Search | google / organic | (organic): 471 sessões / 1 compra(s) / R$ 5.999,99 / conv. 0,21%
- Organic Social | l.instagram.com / referral | (referral): 119 sessões / 2 compra(s) / R$ 4.951,06 / conv. 1,68%
- Direct | (direct) / (none) | (direct): 313 sessões / 2 compra(s) / R$ 4.889,99 / conv. 0,64%
- Cross-network | google / cpc | Pareto [Pmax - Marcas Luxo Moda]: 80 sessões / 1 compra(s) / R$ 2.799,99 / conv. 1,25%
- Cross-network | google / cpc | [PD][FUNDO] Pmax | Search DSA: 215 sessões / 1 compra(s) / R$ 2.160,00 / conv. 0,47%
- Paid Social | facebook / paid | 120210118442410224: 147 sessões / 1 compra(s) / R$ 1.599,99 / conv. 0,68%
- Cross-network | google / cpc | [PD][FUNDO] | Performance Max | Todos os Tênis: 78 sessões / 1 compra(s) / R$ 1.399,99 / conv. 1,28%
- Paid Social | facebook / paid | 120210400473720224: 658 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | facebook / cpc | Pareto.Vendas-Adv [ Dia das Mães | Helena] Campanha: 188 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Shopping | google / cpc | Pareto.Shopping: 172 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | facebook / paid | 120206303993560224: 157 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | facebook / cpc | [PD] [FUNDO] DABA: 149 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Cross-network | google / cpc | [PD] [MEIO] | Demand Gen | Tráfego: 108 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | facebook / paid | 120241297336180224: 103 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | ig / paid | 120210400473720224: 103 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Search | google / cpc | [PD] Brasil | Search - Marca: 100 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | tiktok / paid | Pareto Vendas Geral: 85 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%
- Paid Social | facebook / cpc | Pareto.Vendas-Adv [ Geral]: 75 sessões / 0 compra(s) / R$ 0,00 / conv. 0,00%

## Meta Ads — gasto e retorno reportado pela plataforma

- [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ): gasto R$ 192,11 / compras 6 / valor R$ 13.439,97 / ROAS plataforma 69,96x / 20 ads
- [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+): gasto R$ 308,48 / compras 3 / valor R$ 4.799,97 / ROAS plataforma 15,56x / 17 ads
- Pareto,lancamento,Jacquemus: gasto R$ 257,24 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 22 ads
- Pareto,Vendas [Masculino]: gasto R$ 161,53 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 3 ads
- [PD][MEIO] TRAF (antiga Simples | Tráfego): gasto R$ 144,06 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 5 ads
- Pareto,Vendas-Adv [ Geral]: gasto R$ 126,21 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 24 ads
- [Pareto] [FUNDO] DABA: gasto R$ 49,38 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 2 ads
- [PD] [TOPO] Alcance Loja Física (antiga Simples | Alcance - Loja e Bairros): gasto R$ 14,50 / compras 0 / valor R$ 0,00 / ROAS plataforma 0,00x / 1 ads

### Ads/criativos com sinal de compra

- Campanha: [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ) | Adset: RMKT (Site + Instagram + Vídeo) | Ad: [influencer Ju Mesquita | start 25-02-26 | Onitsuka] — Cópia | gasto R$ 31,21 / compras 3 / valor R$ 6.840,00 / ROAS 219,16x
- Campanha: [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ) | Adset: RMKT (Site + Instagram + Vídeo) | Ad: [influencer Mariah- Adv geral] — Cópia | gasto R$ 0,14 / compras 3 / valor R$ 6.599,97 / ROAS 47142,64x
- Campanha: [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+) | Adset: Simples | Vendas Advantage+ [clube do sky] | Ad: [influencer Lala noleto] —Simples | gasto R$ 213,40 / compras 3 / valor R$ 4.799,97 / ROAS 22,49x

### Possível bloco de influencer/creator detectado por nome de campanha/ad

- [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ) | RMKT (Site + Instagram + Vídeo) | [influencer Ju Mesquita | start 25-02-26 | Onitsuka] — Cópia: gasto R$ 31,21 / compras 3 / valor R$ 6.840,00 / ROAS 219,16x
- [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ) | RMKT (Site + Instagram + Vídeo) | [influencer Mariah- Adv geral] — Cópia: gasto R$ 0,14 / compras 3 / valor R$ 6.599,97 / ROAS 47142,64x
- [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+) | Simples | Vendas Advantage+ [clube do sky] | [influencer Lala noleto] —Simples: gasto R$ 213,40 / compras 3 / valor R$ 4.799,97 / ROAS 22,49x
- Pareto,Vendas [Masculino] | Masculino Segmentado | [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores — — Cópia: gasto R$ 140,81 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ) | RMKT (Site + Instagram + Vídeo) | [influencer Ju Mesquita | start 25-02-26 | New Balance 204 L] — Cópia: gasto R$ 111,96 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- [PD][MEIO] TRAF (antiga Simples | Tráfego) | Simples | [Regiona l Camboriu - Curitiba] | [influencer Maria Fernanda - Video 2 - Nov 25] — Regional: gasto R$ 108,03 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- Pareto,Vendas-Adv [ Geral] | Stories | [influencer Silvia | start 20-12-25 | Onitsuka Sabot Stories 3]: gasto R$ 49,97 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- Pareto,lancamento,Jacquemus | Lista Zipper | [influencer Silvia 24-03-26] - jacquemus]Lista Compradores —: gasto R$ 38,26 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+) | Simples | Vendas Advantage+ [clube do sky] | [influencer Helena | start 07-12-25 | Stories 5] — — — Cópia: gasto R$ 37,43 / compras 0 / valor R$ 0,00 / ROAS 0,00x
- Pareto,lancamento,Jacquemus | Lista VIP | [influencer Silvia 11-03-26] - jacquemus]Lista Compradores: gasto R$ 26,16 / compras 0 / valor R$ 0,00 / ROAS 0,00x

## Shopify web — evidência pedido a pedido sem PII

- #147334: R$ 2.280,00 | origem: instagram/referral | campanha/utm_id: 97760_v0_s00_e0_tv3 | conteúdo: — | referrer: https://l.instagram.com/ | cupom: IG-EMAIL-C1O3GXTV
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-3 / tam. 36 / 1 un.
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU [sem SKU no Shopify] / tam. 36.5 / 1 un.
- #147331: R$ 1.599,99 | origem: facebook | campanha/utm_id: — | conteúdo: Facebook_UA | referrer: — | cupom: —
  - Tênis Nike Sb Dunk Low Pro Triple White Branco / SKU FJ1674-100-2 / tam. 38 / 1 un.
- #147330: R$ 2.390,00 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://lksneakers.com.br/cart | cupom: INSTA10
  - Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-5 / tam. 38 / 1 un.
- #147328: R$ 2.160,00 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://www.google.com/ | cupom: HELENA10
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-2 / tam. 35 / 1 un.
- #147327: R$ 2.799,99 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://www.google.com/ | cupom: —
  - Tênis New Balance 204L Mushroom Arid Stone Marrom / SKU U204LMMA-5 / tam. 38 / 1 un.
- #147326: R$ 5.999,99 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://www.google.com/ | cupom: —
  - Tênis Nike Air Jordan 1 Low Voodoo Flax and Oil Green Marrom / SKU [sem SKU no Shopify] / tam. 44 / 1 un.
- #147322: R$ 2.671,06 | origem: instagram/referral | campanha/utm_id: 97760_v0_s00_e0_tv3 | conteúdo: — | referrer: https://l.instagram.com/ | cupom: —
  - Tênis New Balance 9060 Sea Salt Moonbeam Branco / SKU U9060WHT-4 / tam. 37 / 1 un.
- #147321: R$ 2.499,99 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://www.google.com/ | cupom: —
  - Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege / SKU 1183C015-202-12 / tam. 36.5 / 1 un.
- #147320: R$ 1.399,99 | origem: sem UTM claro | campanha/utm_id: — | conteúdo: — | referrer: https://www.google.com/ | cupom: —
  - Tênis Nike Air Force 1 '07' "White" Branco / SKU 315115112-41 / tam. 41 / 1 un.

## Diagnóstico de atribuição

- O Shopify mostra evidências úteis por pedido: landing_site, referrer e cupons como `INSTA10`/`IG-*`. Isso já permite uma camada v0.3 de atribuição, mas ainda não amarra 100% influencer → campanha → produto.
- GA4 mostra campanha/source/medium e compra, mas nem sempre preserva o mesmo valor do Shopify. Shopify continua fonte oficial de receita; GA4/Meta entram como leitura de tráfego e atribuição.
- Meta Ads tem dados de spend e compras por anúncio. Próxima reconciliação correta é cruzar: Meta campaign/ad/adset ↔ UTM no Shopify ↔ produtos vendidos.

## Recomendações sem executar nada

- Criar padrão obrigatório de naming/UTM para influencer: `utm_source=instagram`, `utm_medium=influencer` ou `paid_social`, `utm_campaign=<campanha>`, `utm_content=<influencer>_<criativo>`, e cupom único quando fizer sentido.
- No Daily Brief v0.3, incluir bloco “Pago & Influencers”: gasto, sessões, compras, receita Shopify, produtos/marcas vendidos, ROAS plataforma e confiança da atribuição.
- Não otimizar orçamento automaticamente. O output deve virar sugestão: manter, escalar, pausar, trocar criativo ou investigar tracking — sempre com aprovação Lucas.

## Dados faltantes / bloqueios

- Google Ads spend/custo ainda não foi puxado direto da Google Ads API; por enquanto Google pago vem via GA4 (`google / cpc`).
- Influencer real ainda não está garantido em UTM/cupom/campaign naming. Existe sinal em campanha “Helena”, mas não dá para concluir performance de influencer sem padrão consistente.
- Shopify web via Admin retornou 9 pedidos web e 6 POS nessa consulta sanitizada; para o Daily Brief completo, manter o método anterior que consolidou 20 pedidos totais. Aqui o foco foi atribuição web/paga.