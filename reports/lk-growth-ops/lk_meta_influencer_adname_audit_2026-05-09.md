# LK Meta Ads — auditoria influencer por `ad_name`/`ad_id`

Escopo: read-only via Meta Graph API, conta `act_1242062509867163`, nível `ad`, janela de atribuição `7d_click` + `1d_view`. Regra Maicon aplicada: identificar influencer primariamente e somente em `ad_name` nesta auditoria; somar todos os `ad_id` do mesmo nome normalizado; manter Maria, Maria Fernanda e Mariah separados. Não há inferência de produto por campaign/adset.

## Janela principal — maio MTD fechado: 2026-05-01..2026-05-09

- Meta global: 171 linhas/ad rows; 171 ads ativos; spend R$ 11.559,62; compras atribuídas 109; valor atribuído R$ 295.340,95; ROAS 25.55x.
- Influencers detectados por `ad_name`: 14 nomes; 111 ad_ids somados; spend R$ 9.154,57; compras 84; valor R$ 217.512,20.
- Match source counts: {'ad_name_pattern': 101, 'ad_name_influencer_marker': 10}.
- Ranking Pareto-compatible por compras/valor:
  - Lala Noleto: 15 ad_ids; spend R$ 2.208,59; compras 25; valor R$ 63.539,75; ROAS 28.77x; CPA R$ 88,34.
  - Silvia Henz: 30 ad_ids; spend R$ 2.433,80; compras 16; valor R$ 55.955,97; ROAS 22.99x; CPA R$ 152,11.
  - Arlindo: 3 ad_ids; spend R$ 1.185,55; compras 11; valor R$ 29.517,95; ROAS 24.90x; CPA R$ 107,78.
  - Helena Lunardelli: 22 ad_ids; spend R$ 924,01; compras 10; valor R$ 22.648,60; ROAS 24.51x; CPA R$ 92,40.
  - Ju Mesquita: 8 ad_ids; spend R$ 1.037,37; compras 10; valor R$ 17.169,96; ROAS 16.55x; CPA R$ 103,74.
  - Fiorela: 9 ad_ids; spend R$ 263,84; compras 6; valor R$ 19.999,98; ROAS 75.80x; CPA R$ 43,97.
  - Maria: 2 ad_ids; spend R$ 585,06; compras 5; valor R$ 6.480,00; ROAS 11.08x; CPA R$ 117,01.
  - Mariah: 4 ad_ids; spend R$ 9,28; compras 1; valor R$ 2.199,99; ROAS 237.07x; CPA R$ 9,28.
  - Maria Fernanda: 4 ad_ids; spend R$ 502,18; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Taby: 3 ad_ids; spend R$ 2,20; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Malu Borges: 3 ad_ids; spend R$ 1,34; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Renata: 5 ad_ids; spend R$ 0,67; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Hariana: 2 ad_ids; spend R$ 0,50; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Gio Pagano: 1 ad_ids; spend R$ 0,18; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
- Check Marias separadas: Maria=2 ad_ids/5 compras/R$ 6.480,00 valor; Mariah=4 ad_ids/1 compras/R$ 2.199,99 valor; Maria Fernanda=4 ad_ids/0 compras/R$ 0,00 valor.
- Exemplos de ad_name por influencer (não exaustivo):
  - Lala Noleto: 120231766207010224: [influencer Lala noleto] — Adv geral; 120231767068900224: [influencer Lala noleto] — RMKT
  - Silvia Henz: 120237633068340224: [influencer Silvia start 11.12.25- Adv geral] —; 120237637374840224: [influencer Silvia start 11.12.25- RMKT]
  - Arlindo: 120242637471080224: [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores —; 120242637576320224: [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores — — Cópia
  - Helena Lunardelli: 120237392928140224: [influencer Helena | start 07-12-25 | Stories 1 ] —; 120237392979920224: [influencer Helena | start 07-12-25 | Stories 2] —
  - Ju Mesquita: 120240942507490224: [influencer Ju Mesquita | start 25-02-26 | New Balance 204 L]; 120240942618020224: [influencer Ju Mesquita | start 25-02-26 | Onitsuka]
  - Fiorela: 120242989696250224: [influencer Fiorela- start 09-04-2026  Adv geral] — Jacquemus; 120242989833200224: [influencer Fiorela- start 09-04-2026  Adv geral] — Jacquemus — Video 2
  - Maria: 120229142869820224: [influencer Maria- Adv geral]; 120229680292090224: [influencer Maria- Adv geral] — Regional
  - Mariah: 120235959757460224: [influencer Mariah- Adv geral]; 120236024257710224: [influencer Mariah- Adv geral] — RMKT
  - Maria Fernanda: 120235354422280224: [influencer Maria Fernanda - Video 2 - Nov 25] — ADV; 120235354695890224: [influencer Maria Fernanda - Video 2 - Nov 25] — RMKT
  - Taby: 120238351511710224: [influencer Taby |start 23-12-25 | Video BMW]; 120238352175720224: [influencer Taby |start 23-12-25 | Video BMW] — RMKT
  - Malu Borges: 120243342186850224: [influencer Malu Borges 16-04-26] - jacquemus video ]; 120243343108580224: [influencer Malu Borges 16-04-26] - jacquemus video ] — Clube do sky
  - Renata: 120237393662670224: [influencer Renata | start 15-12-25 | Video 01] — Stories; 120237938182780224: [influencer Renata start 15.12.25- Adv geral] —

## Controle — última semana fechada: 2026-05-03..2026-05-09

- Meta global: 168 linhas/ad rows; 168 ads ativos; spend R$ 9.479,13; compras atribuídas 76; valor atribuído R$ 176.707,25; ROAS 18.64x.
- Influencers detectados por `ad_name`: 14 nomes; 109 ad_ids somados; spend R$ 7.456,37; compras 62; valor R$ 129.818,45.
- Match source counts: {'ad_name_pattern': 100, 'ad_name_influencer_marker': 9}.
- Ranking Pareto-compatible por compras/valor:
  - Lala Noleto: 15 ad_ids; spend R$ 1.726,18; compras 15; valor R$ 22.959,96; ROAS 13.30x; CPA R$ 115,08.
  - Silvia Henz: 29 ad_ids; spend R$ 2.005,17; compras 12; valor R$ 32.399,95; ROAS 16.16x; CPA R$ 167,10.
  - Helena Lunardelli: 22 ad_ids; spend R$ 737,78; compras 8; valor R$ 17.848,62; ROAS 24.19x; CPA R$ 92,22.
  - Ju Mesquita: 8 ad_ids; spend R$ 902,33; compras 8; valor R$ 12.269,98; ROAS 13.60x; CPA R$ 112,79.
  - Arlindo: 3 ad_ids; spend R$ 920,18; compras 7; valor R$ 15.659,97; ROAS 17.02x; CPA R$ 131,45.
  - Fiorela: 9 ad_ids; spend R$ 220,80; compras 6; valor R$ 19.999,98; ROAS 90.58x; CPA R$ 36,80.
  - Maria: 2 ad_ids; spend R$ 445,96; compras 5; valor R$ 6.480,00; ROAS 14.53x; CPA R$ 89,19.
  - Mariah: 4 ad_ids; spend R$ 6,45; compras 1; valor R$ 2.199,99; ROAS 341.08x; CPA R$ 6,45.
  - Maria Fernanda: 4 ad_ids; spend R$ 488,54; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Malu Borges: 3 ad_ids; spend R$ 1,32; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Renata: 4 ad_ids; spend R$ 0,59; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Hariana: 2 ad_ids; spend R$ 0,46; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Taby: 3 ad_ids; spend R$ 0,43; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
  - Gio Pagano: 1 ad_ids; spend R$ 0,18; compras 0; valor R$ 0,00; ROAS 0.00x; CPA R$ 0,00.
- Check Marias separadas: Maria=2 ad_ids/5 compras/R$ 6.480,00 valor; Mariah=4 ad_ids/1 compras/R$ 2.199,99 valor; Maria Fernanda=4 ad_ids/0 compras/R$ 0,00 valor.
- Exemplos de ad_name por influencer (não exaustivo):
  - Lala Noleto: 120231766207010224: [influencer Lala noleto] — Adv geral; 120231767068900224: [influencer Lala noleto] — RMKT
  - Silvia Henz: 120237633068340224: [influencer Silvia start 11.12.25- Adv geral] —; 120237637374840224: [influencer Silvia start 11.12.25- RMKT]
  - Helena Lunardelli: 120237392928140224: [influencer Helena | start 07-12-25 | Stories 1 ] —; 120237392979920224: [influencer Helena | start 07-12-25 | Stories 2] —
  - Ju Mesquita: 120240942507490224: [influencer Ju Mesquita | start 25-02-26 | New Balance 204 L]; 120240942618020224: [influencer Ju Mesquita | start 25-02-26 | Onitsuka]
  - Arlindo: 120242637471080224: [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores —; 120242637576320224: [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores — — Cópia
  - Fiorela: 120242989696250224: [influencer Fiorela- start 09-04-2026  Adv geral] — Jacquemus; 120242989833200224: [influencer Fiorela- start 09-04-2026  Adv geral] — Jacquemus — Video 2
  - Maria: 120229142869820224: [influencer Maria- Adv geral]; 120229680292090224: [influencer Maria- Adv geral] — Regional
  - Mariah: 120235959757460224: [influencer Mariah- Adv geral]; 120236024257710224: [influencer Mariah- Adv geral] — RMKT
  - Maria Fernanda: 120235354422280224: [influencer Maria Fernanda - Video 2 - Nov 25] — ADV; 120235354695890224: [influencer Maria Fernanda - Video 2 - Nov 25] — RMKT
  - Malu Borges: 120243342186850224: [influencer Malu Borges 16-04-26] - jacquemus video ]; 120243343108580224: [influencer Malu Borges 16-04-26] - jacquemus video ] — Clube do sky
  - Renata: 120237393662670224: [influencer Renata | start 15-12-25 | Video 01] — Stories; 120237938182780224: [influencer Renata start 15.12.25- Adv geral] —
  - Hariana: 120240345372740224: [influencer Hariana | start 12-02-26 | Reels 01 Conforto e Estilo] —; 120240346291270224: [influencer Hariana | start 12-02-26 | Reels 01 Conforto e Estilo] — — Cópia

## Lacunas/guardrails

- Este relatório não atribui produto/SKU: não há bridge Shopify/produto confiável neste card; produto por criativo/ad exige ponte segura por `ad_id`/SKU em tarefa separada.
- Valores são atribuição do Meta Ads Manager, não receita operacional final da LK.
- Nenhum write externo executado.
