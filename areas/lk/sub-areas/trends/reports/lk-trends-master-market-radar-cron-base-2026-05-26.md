# LK-TRENDS — Master Market Radar / Base do CRON

Data de captura: 2026-05-26 17:35–17:42 UTC
Status: relatório read-only para desenho do cron; nenhuma ação externa executada.

## 1. Veredito executivo

O LK-TRENDS deve operar como radar comercial, não como gerador de recomendações avulsas. A ordem correta é:

1. detectar liquidez internacional por KicksDev/KicksDB;
2. validar demanda brasileira por Google Ads/DataForSEO e sinais de mercado local;
3. cruzar com presença/gap LK;
4. classificar em sourcing, watchlist, catálogo-preview, conteúdo downstream ou ignorar;
5. produzir pacote seguro para decisão humana quando houver ação com risco.

Correção estrutural implementada nesta rodada: KicksDev/KicksDB passa a ser a fonte primária programática para StockX/GOAT. Snippets de Google ficam apenas como fallback/sanity-check.

## 2. Fontes usadas

### Fontes read-only executadas agora

- KicksDev/KicksDB via API:
  - StockX product search;
  - GOAT product search;
  - StockX/GOAT sales daily quando disponível;
  - Unified API para identidade cruzada.
- DataForSEO / Google Ads Brasil:
  - demanda mensal e tendência por termo.
- Web search público:
  - presença de coleções/produtos LK;
  - checagem pública de cobertura de catálogo.
- Brain/Skill LK-TRENDS:
  - regra de liquidez relativa;
  - regra de downgrade por retail saturado ou histórico ruim no Brasil.

### Artefatos criados/atualizados

- Script KicksDev read-only:
  - `scripts/lk_trends_kicksdev_market_probe_20260526.py`
- Relatório bruto KicksDev principal:
  - `areas/lk/sub-areas/trends/reports/kicksdev-probes/lk-trends-kicksdev-probe-20260526T174039Z.md`
- Contrato KicksDev para o cron:
  - `areas/lk/sub-areas/trends/references/kicksdev-market-intelligence-contract-2026-05-26.md`
- Template semanal atualizado:
  - `areas/lk/rotinas/templates/lk-trend-weekly-v1.md`
- Skill LK-TRENDS atualizada:
  - `productivity/lk-trends-product-intelligence`

## 3. Régua comercial do cron

### Candidato de sourcing

Um modelo/colorway só entra em pacote para Júlio se tiver ao menos um destes critérios:

- 150+ vendas em 90 dias em StockX/GOAT; ou
- 15%+ da líder da família/modelo; ou
- 50+ vendas em 90 dias com preço assimétrico forte; ou
- collab forte + escassez real; ou
- pedido/fit BR comprovado.

Mesmo passando na liquidez, ainda precisa:

- não estar sobrando no retail oficial;
- não conflitar com histórico fraco de sell-through LK/BR;
- ter preço de compra plausível para margem LK;
- ser validado por tamanho/colorway, não só pelo nome do modelo.

### Watchlist

- 50–149 vendas em 90 dias;
- 5%–15% da líder;
- busca BR relevante, mas liquidez internacional ou LK-fit incompleto;
- produto já coberto na LK, mas com possível gap de grade/colorway.

### Ignorar

- abaixo de 50 vendas em 90 dias sem collab/escassez/assimetria;
- hype genérico com retail saturado;
- modelo com busca BR alta mas pouca liquidez internacional no recorte analisado;
- colorway sem volume material contra a líder.

## 4. Radar consolidado — ranking de decisão

Score usado apenas como ordenação auxiliar, não como decisão automática.

Fórmula de apoio:

- 35% liquidez internacional normalizada;
- 30% demanda BR normalizada;
- 20% gap LK/actionability;
- 15% fit comercial LK.

### 1) Jacquemus x Nike Moon Shoe SP — score 60,0

Fato:

- KicksDev StockX:
  - Soft Pearl: 49 weekly_orders; 13.803 vendas/90d; avg_90d USD 299,91.
  - Aluminum Pink: 31 weekly_orders; 21.840 vendas/90d; avg_90d USD 283,89.
  - Fauna Brown: 23 weekly_orders; 13.258 vendas/90d; avg_90d USD 316,10.
- KicksDev GOAT:
  - Fauna Brown: 58 vendas/90d; avg_90d USD 295,09.
  - Soft Pearl: 73 vendas/90d; avg_90d USD 294,08.
  - Aluminum Pink: 63 vendas/90d; avg_90d USD 251,10.
- Google Ads BR:
  - `nike jacquemus`: 1.000/mês; pico recente 3.600 em 2026-03 e 2.400 em 2026-04.
  - `jacquemus nike`: 390/mês; pico recente 1.000 em 2026-03.
  - `nike moon shoe`: 390/mês; 720 em 2026-03/04.
- LK pública:
  - coleção Jacquemus e coleção Nike x Jacquemus Moon Shoe SP existem;
  - produtos vistos: Off Noir, University Red, Alabaster, Off White.

Sinal:

- É o melhor candidato para o cron como família de collab/curadoria premium.
- A liquidez internacional é muito forte nas novas colorways femininas.
- A demanda BR é menor que runners massificados, mas qualificada por collab/luxo.

Hipótese:

- Não é necessariamente “comprar tudo”; é checar grade real e lacunas nas colorways que a LK não cobre ou cobre pouco.
- Melhor uso: pacote de sourcing seletivo + reforço de coleção/guia, se margem e disponibilidade permitirem.

Decisão primária:

- Watchlist alta / sourcing seletivo por colorway e tamanho.

Risco:

- Ticket alto, sizing feminino, risco de estoque parado se comprar grade errada.
- LK já tem cobertura pública relevante; o gap pode ser grade/colorway, não coleção.

Próxima ação segura:

- Gerar pacote Júlio somente com colorways fortes e tamanhos priorizados após checar estoque interno/grade.

Aprovação necessária:

- Aprovação atual antes de contactar Júlio, reservar, comprar ou prometer disponibilidade.

### 2) Nike Vomero Premium — score 57,2

Fato:

- Google Ads BR:
  - `nike vomero premium`: 22.200/mês;
  - 2026-04: 49.500;
  - crescimento forte desde 2025-05.
- KicksDev StockX:
  - Realtree Camo Black: 25 weekly_orders; 3.861 vendas/90d; avg_90d USD 262,29.
  - Blue Tint W: 20 weekly_orders; 929 vendas/90d; avg_90d USD 279,28.
  - White Lapis Total Orange: 18 weekly_orders; 5.614 vendas/90d; avg_90d USD 239,97.
- KicksDev GOAT:
  - Alabaster: 97 vendas/90d; avg_90d USD 218,10.
  - White Bright Crimson: 136 vendas/90d; avg_90d USD 206,03.
  - Sail Total Orange: 144 vendas/90d; avg_90d USD 249,42.
- LK pública:
  - guia Nike Vomero Premium existe;
  - coleção Nike Vomero Premium existe;
  - produtos públicos incluem Tangerine Tint e White Bright Crimson.

Sinal:

- É o melhor modelo para volume de demanda BR.
- A família tem liquidez internacional suficiente para justificar monitoramento semanal.
- Como a LK já tem coleção, a oportunidade é de grade, preço, colorway e conteúdo de conversão, não descoberta de novo modelo.

Hipótese:

- Priorizar colorways com liquidez real e que a LK não cobre bem.
- Evitar recomendar compra só porque o termo explodiu; precisa ver custo e sell-through interno.

Decisão primária:

- Catálogo/grade + watchlist de sourcing seletivo.

Risco:

- Alto interesse pode atrair concorrência e retail; risco de pagar caro no pico.
- Algumas colorways já podem estar bem cobertas na LK.

Próxima ação segura:

- Rodar check interno read-only de estoque/sell-through e mapear top 5 colorways KicksDev vs LK.

Aprovação necessária:

- Aprovação antes de compra, contato fornecedor ou alteração de PDP/preço.

### 3) Nike Mind 002 — score 47,5

Fato:

- Google Ads BR:
  - `nike mind`: 4.400/mês;
  - picos: 14.800 em 2026-01 e 2026-02; 8.100 em 2026-03; 5.400 em 2026-04.
- KicksDev StockX:
  - Light Smoke Grey: 106 weekly_orders; 14.844 vendas/90d; avg_90d USD 193,52.
  - Black Hyper Crimson: 92 weekly_orders; 15.009 vendas/90d; avg_90d USD 233,11.
  - Football Grey W: 4 weekly_orders; 479 vendas/90d; avg_90d USD 252,57.
- KicksDev GOAT:
  - Black Hyper Crimson: 112 weekly_orders; 270 vendas/90d; avg_90d USD 162,90.
  - Thunder Blue: 38 weekly_orders; 130 vendas/90d; avg_90d USD 159,48.
  - Light Smoke Grey: 25 weekly_orders; 336 vendas/90d; avg_90d USD 174,49.
- LK pública:
  - produtos Nike Mind 002 existem: Football Grey, Sail, Light Violet Ore, Light Smoke Grey e outros.
  - coleção/cluster Nike Mind 001/002 existe.

Sinal:

- Liquidez internacional extremamente forte em duas colorways.
- Demanda BR é boa, mas já saiu do pico inicial.
- LK já capturou a tendência publicamente.

Hipótese:

- O cron deve monitorar Mind 002 para reposição/grade e preço, não tratar como novidade.
- Black Hyper Crimson e Light Smoke Grey parecem benchmarks de liquidez.

Decisão primária:

- Reposição/grade e watchlist; não “novo sourcing amplo”.

Risco:

- Se LK já estiver com preço alto ou estoque lento, volume StockX não garante venda local.
- Curva BR parece ter pico em jan/fev e desaceleração até abril.

Próxima ação segura:

- Cruzar KicksDev top colorways com estoque/sell-through LK; só recomendar compra se houver ruptura/velocidade.

Aprovação necessária:

- Aprovação antes de compra/reserva ou mudança de preço.

### 4) Puma Speedcat Ballet — score 46,5

Fato:

- Google Ads BR:
  - `puma speedcat`: 18.100/mês;
  - 27.100 em 2026-03 e 2026-04.
  - termo específico `speedcat ballet` sem volume retornado no recorte.
- KicksDev StockX:
  - Dark Chocolate W: 15 weekly_orders; 1.448 vendas/90d; avg_90d USD 121,64.
  - Whisp of Pink W: 16 weekly_orders; 806 vendas/90d; avg_90d USD 83,40.
  - Venus Jasmine Flower W: 16 weekly_orders; 644 vendas/90d; avg_90d USD 132,75.
- KicksDev GOAT:
  - primeiros resultados capturados eram PS/GS com pouca ou nenhuma venda, sinalizando necessidade de filtro adulto correto.
- LK pública:
  - Speedcat OG presente em várias colorways;
  - Speedcat Ballet não apareceu nos resultados públicos capturados.

Sinal:

- A família Speedcat tem alta busca BR, mas Lucas já apontou risco de retail sobrando no Speedcat comum.
- A versão Ballet tem liquidez internacional própria e deve ser tratada separadamente do Speedcat OG.

Hipótese:

- Speedcat Ballet é oportunidade de watchlist/sourcing cauteloso, não compra automática.
- Só avança se houver escassez real, colorway feminina forte e custo favorável.

Decisão primária:

- Watchlist média/alta; sourcing apenas com preço assimétrico e confirmação de não saturação BR.

Risco:

- Confundir busca de Speedcat genérico com demanda por Ballet.
- Puma Speedcat comum pode estar saturado no retail, reduzindo fit LK.

Próxima ação segura:

- Monitorar Ballet adulto por SKU; checar Droper/retail BR e margem antes de pacote Júlio.

Aprovação necessária:

- Aprovação antes de compra ou contato fornecedor.

### 5) New Balance 1906L — score 42,8

Fato:

- Google Ads BR:
  - termo específico `new balance 1906l` não retornou volume no recorte;
  - proxy `new balance 1906`: 9.900/mês.
  - `new balance loafer`: 390/mês.
- KicksDev StockX:
  - Metallic Silver: 11 weekly_orders; 1.826 vendas/90d; avg_90d USD 124,69.
  - Black: 9 weekly_orders; 1.226 vendas/90d; avg_90d USD 141,66.
  - Black Angora: 6 weekly_orders; 1.050 vendas/90d; avg_90d USD 123,44.
- KicksDev GOAT:
  - Blacktop Phantom: 11 weekly_orders; 186 vendas/90d; avg_90d USD 95,90.
  - Black Croc: 7 weekly_orders; 331 vendas/90d; avg_90d USD 132,08.
  - Black Angora: 6 weekly_orders; 81 vendas/90d; avg_90d USD 110,27.
- LK pública:
  - não apareceu resultado público para 1906L.

Sinal:

- Liquidez internacional material e LK gap público aparente.
- Demanda BR específica ainda fraca/indireta; o modelo pode ser early/adopter.

Hipótese:

- Bom candidato para catálogo-preview ou sourcing pequeno, porque combina gap LK + liquidez internacional.
- Precisa de validação BR mais forte antes de compra ampla.

Decisão primária:

- Catálogo-preview / watchlist alta; sourcing piloto se custo muito bom.

Risco:

- Busca BR ainda não comprova intenção específica por loafer.
- Modelo loafer pode ter fit menor para público LK que runners/collabs.

Próxima ação segura:

- Criar ficha de monitoramento com Metallic Silver, Black e Black Angora; checar Droper/retail BR e possível preview de coleção.

Aprovação necessária:

- Aprovação antes de publicar preview, cadastrar produto ou acionar Júlio.

### 6) Adidas SL 72 — score 40,2

Fato:

- Google Ads BR:
  - `adidas sl 72`: 22.200/mês;
  - 40.500 em 2026-04; 49.500 em 2026-03.
- KicksDev StockX:
  - Collegiate Green W: 3 weekly_orders; 110 vendas/90d; avg_90d USD 88,54.
  - outros resultados capturados com 0–17 vendas/90d.
- LK pública:
  - coleção Adidas SL 72 existe;
  - produtos públicos incluem Cow Print, Aurora Ivy, Scarlet Crochet, Liberty London.

Sinal:

- Demanda BR muito alta, mas liquidez internacional capturada é fraca no KicksDev para os resultados principais.
- Como a LK já tem coleção, a oportunidade é mais SEO/conversão e curadoria de colorways especiais do que sourcing baseado em StockX/GOAT.

Hipótese:

- SL 72 deve entrar como conteúdo/coleção e monitoramento de busca, não como pacote de sourcing prioritário.

Decisão primária:

- Conteúdo/PDP downstream + watchlist leve.

Risco:

- Busca alta pode refletir produto massificado e retail amplo, não oportunidade de resale/sourcing.

Próxima ação segura:

- Usar para otimização de coleção e detectar colorways especiais com escassez, não comprar genérico.

Aprovação necessária:

- Aprovação antes de alteração Shopify/publicação.

### 7) New Balance 204L — score 24,5

Fato:

- KicksDev StockX:
  - Mushroom Arid Stone: 31 weekly_orders; 7.310 vendas/90d; avg_90d USD 108,10.
  - Pastel Pink: 6 weekly_orders; 1.644 vendas/90d; avg_90d USD 121,16.
  - Cortado: 11 weekly_orders; 866 vendas/90d; avg_90d USD 84,16.
- KicksDev GOAT:
  - Mushroom Arid Stone: 159 vendas/90d; avg_90d USD 98,63.
  - Pastel Pink: 180 vendas/90d; avg_90d USD 112,27.
  - Black Timberwolf: 388 vendas/90d; avg_90d USD 75,18.
- Google Ads BR:
  - termo específico `new balance 204l`/`nb 204l` não retornou volume no recorte atual;
  - proxy `new balance loafer`: 390/mês.
- LK pública:
  - coleção New Balance 204L existe com 29 opções.

Sinal:

- A liderança do Mushroom é clara; 204L já foi capturado pela LK.
- A oportunidade agora não é sair buscando novas CWs fracas.

Hipótese:

- Reposição seletiva de vencedoras e ajuste de grade, não expansão ampla.

Decisão primária:

- Reposição seletiva / não sourcing de novas CWs por padrão.

Risco:

- Comprar colorways marginais por “gap” de catálogo sem liquidez relativa.

Próxima ação segura:

- Monitorar só líderes e ruptura de grade; ignorar CWs pequenas salvo pedido específico.

Aprovação necessária:

- Aprovação antes de compra ou reserva.

### 8) Nike Vomero 5 — score 19,2

Fato:

- Google Ads BR:
  - `nike vomero 5`: 5.400/mês;
  - demanda estável entre 4.400 e 6.600/mês no recorte de 12 meses.
- KicksDev capturou principalmente GS/TD no top 3:
  - Ghost Summit White GS: 228 vendas/90d;
  - Valentine’s Day 2025 GS: 79 vendas/90d;
  - Total Orange GS: 130 vendas/90d.
- LK pública:
  - coleção Nike Vomero 5 existe.

Sinal:

- Modelo já maduro e coberto.
- A consulta genérica trouxe muitos resultados infantis/grade school, então o cron precisa filtrar por adulto/target antes de decidir.

Hipótese:

- Não é prioridade de sourcing no radar macro; usar como comparação e otimização de catálogo existente.

Decisão primária:

- Conteúdo/PDP downstream ou ajuste de filtros; não sourcing macro.

Risco:

- Dados de GS/TD distorcem leitura se o cron não filtrar gênero/tamanho.

Próxima ação segura:

- Refinar query por SKU/colorway adulta se Lucas quiser análise específica.

Aprovação necessária:

- Aprovação antes de qualquer alteração de catálogo/preço.

### 9) On x Loewe Cloudsolo — score 12,5

Fato:

- Google Ads BR:
  - `on loewe`: 1.600/mês;
  - `loewe on`: 480/mês;
  - tendência caiu de patamares maiores em 2025 para 2026-04.
- KicksDev StockX:
  - Sand Burgundy W: 0 vendas/90d no retorno capturado;
  - Sand Turquoise W: 26 vendas/90d; avg_90d USD 1.198,00;
  - Khaki Green Sand W: 15 vendas/90d; avg_90d USD 585,07.
- KicksDev GOAT:
  - top capturado com 0 vendas/90d.
- LK pública:
  - coleção Loewe x On Running existe;
  - produtos Cloudsolo públicos existem.

Sinal:

- É produto de luxo/curadoria, mas a liquidez de resale capturada é baixa.
- LK já cobre publicamente a categoria.

Hipótese:

- Não é candidato de sourcing pelo cron, salvo pedido específico ou oportunidade de preço muito assimétrica.

Decisão primária:

- Ignorar para sourcing recorrente; manter como curadoria/conteúdo luxo se já existir.

Risco:

- Ticket altíssimo e giro baixo.

Próxima ação segura:

- Só reavaliar com sinal de demanda interna ou oportunidade pontual de compra.

Aprovação necessária:

- Aprovação antes de sourcing/compra.

## 5. Decisões por fila do cron

### Fila A — Sourcing seletivo / Júlio preview

Entram apenas com validação de grade e margem:

- Jacquemus x Nike Moon Shoe SP:
  - foco em Soft Pearl, Aluminum Pink, Fauna Brown e equivalentes fortes;
  - checar se LK já cobre e onde há ruptura.
- Nike Vomero Premium:
  - foco nas colorways com alta liquidez e demanda BR;
  - não comprar só por termo genérico.
- Nike Mind 002:
  - foco em Black Hyper Crimson e Light Smoke Grey se houver gap interno.

### Fila B — Catálogo-preview / gap público

- New Balance 1906L:
  - Metallic Silver, Black, Black Angora e Black Croc;
  - bom para testar sem assumir compra grande.
- Puma Speedcat Ballet:
  - Dark Chocolate, Whisp of Pink, Venus Jasmine Flower;
  - só se retail BR não estiver saturado e preço for bom.

### Fila C — Conteúdo/PDP downstream

- Adidas SL 72:
  - alto volume BR, mas baixa liquidez StockX/GOAT capturada;
  - usar para melhorar descoberta e conversão da coleção existente.
- Nike Vomero 5:
  - modelo maduro; refinar coleção e filtros.
- On x Loewe Cloudsolo:
  - curadoria luxo, não sourcing recorrente.

### Fila D — Ignorar/baixar prioridade

- Colorways fracas do 204L fora das líderes;
- Speedcat genérico sem escassez;
- On x Loewe Cloudsolo como compra recorrente;
- qualquer colorway abaixo de 50 vendas/90d sem collab forte ou assimetria.

## 6. Especificação operacional do CRON LK-TRENDS

### Frequência recomendada

- Diário leve:
  - checar watchlist e top candidates em KicksDev;
  - atualizar vendas 7d/30d/90d;
  - detectar aceleração/deceleração.
- Semanal completo:
  - relatório `lk-trend-weekly-v1`;
  - ranking consolidado;
  - fila de decisões;
  - comparação com semana anterior.
- Sob demanda:
  - quando Lucas citar um modelo;
  - quando houver lançamento/collab forte;
  - quando KicksDev indicar aceleração anormal.

### Inputs

- Seeds manuais de Lucas;
- Watchlist persistente;
- termos BR com aceleração via DataForSEO;
- modelos/categorias LK com tráfego/coleção ativa;
- lançamentos editoriais relevantes;
- KicksDev top movers, quando endpoint/lista permitir.

### Etapas

1. Resolver identidade:
   - KicksDev StockX search;
   - KicksDev GOAT search;
   - Unified API por SKU/slug.
2. Normalizar produto:
   - brand, model, colorway, SKU, gender, slug, source.
3. Calcular liquidez:
   - weekly_orders;
   - orders_7d, orders_30d, orders_90d;
   - avg_amount_90d;
   - rank.
4. Calcular liquidez relativa:
   - comparar colorway contra líder da família/modelo;
   - exigir 15%+ da líder ou exceção justificada.
5. Validar Brasil:
   - Google Ads/DataForSEO volume;
   - tendência mensal;
   - Droper/retail BR;
   - presença de retail saturado.
6. Cruzar LK:
   - presença pública;
   - presença interna read-only quando disponível;
   - ruptura/grade/sell-through quando permitido.
7. Classificar:
   - sourcing para Júlio;
   - watchlist;
   - catálogo-preview;
   - conteúdo/PDP downstream;
   - ignorar.
8. Emitir saídas:
   - relatório markdown/HTML;
   - JSON de oportunidades;
   - pacote de aprovação se houver ação externa.

### Saídas mínimas por produto

- Fonte;
- Confiança;
- Risco;
- Próxima ação segura;
- Aprovação necessária;
- dados KicksDev brutos suficientes para auditoria;
- motivo de não avançar quando for descartado.

## 7. Regras de alerta

### Alerta vermelho — decisão humana

Enviar para Lucas quando:

- produto ausente na LK tiver 150+ vendas/90d e busca BR relevante;
- colorway tiver 15%+ da líder e LK não cobrir;
- variação 7d crescer 2x contra média 30d;
- preço cair abaixo de faixa que permite margem LK;
- collab forte aparecer com escassez real.

### Alerta amarelo — watchlist

- 50–149 vendas/90d;
- busca BR subindo, mas sem liquidez internacional;
- LK cobre a família, mas não a colorway;
- retail BR pouco claro.

### Silencioso/ignorar

- dados fracos;
- retail saturado;
- busca alta mas StockX/GOAT sem tração;
- produto já coberto e sem ruptura aparente.

## 8. Bloqueios e guardrails

Sem aprovação atual, o cron pode:

- pesquisar KicksDev/DataForSEO/Droper/web;
- consultar dados internos read-only quando credenciais permitirem;
- gerar relatório local;
- preparar pacote para Júlio;
- sugerir preview.

Sem aprovação atual, o cron não pode:

- contactar Júlio/fornecedor;
- comprar/reservar/negociar;
- cadastrar ou alterar Shopify/Tiny/Merchant/Klaviyo/ads;
- publicar conteúdo;
- enviar WhatsApp/email/campanha;
- prometer preço, estoque, prazo ou disponibilidade.

## 9. Próxima implementação segura

1. Transformar este relatório em rotina semanal local.
2. Criar watchlist JSON com campos padronizados.
3. Rodar KicksDev diariamente para a watchlist.
4. Adicionar DataForSEO mensal/weekly trend.
5. Adicionar validador Droper/retail BR.
6. Adicionar checagem LK read-only de coleção/estoque/sell-through.
7. Emitir relatório `lk-trend-weekly-v1` e pacote de aprovação separado.

## 10. Conclusão comercial

- Melhor oportunidade premium imediata: Jacquemus x Nike Moon Shoe SP, mas só com grade/margem validadas.
- Melhor motor de demanda BR: Nike Vomero Premium.
- Melhor oportunidade já capturada pela LK para reposição/grade: Nike Mind 002.
- Melhor gap público para testar preview: New Balance 1906L.
- Melhor watchlist cautelosa: Puma Speedcat Ballet.
- Baixar prioridade: On x Loewe Cloudsolo, Speedcat genérico, colorways fracas do 204L, SL 72 como sourcing StockX/GOAT.
