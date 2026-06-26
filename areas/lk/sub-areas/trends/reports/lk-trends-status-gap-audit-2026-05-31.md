# LK-TRENDS — Status, Gap Audit e Próximo Ciclo

Data: 2026-05-31
Status: relatório local/read-only. Nenhuma ação externa executada.
Origem: continuidade do radar LK-TRENDS e correção de papel validada por Lucas.

## 1. Papel canônico do LK-TRENDS

LK-TRENDS é o especialista da LK Sneakers para detectar novidades e tendências relevantes fora do Brasil e transformar esses sinais em decisão comercial segura.

Ordem correta:

1. Detectar produto/modelo/colorway bombando fora do Brasil.
2. Validar tração internacional com KicksDev/KicksDB, StockX, GOAT e fontes editoriais/culturais.
3. Validar Brasil com busca BR, Droper, retail local e saturação.
4. Cruzar com LK: catálogo, grade, estoque/sell-through read-only, fit de curadoria e margem provável.
5. Classificar em sourcing para Júlio, watchlist, catálogo-preview, conteúdo downstream ou ignorar.

SEO/conteúdo/PDP são consequência, não ponto de partida.

## 2. O que está bom

### 2.1 Estrutura e identidade

- O papel do agente foi documentado no PRD do LK Trend Hermes Bot.
- A correção principal foi registrada: LK-TRENDS não é SEO-first; é radar comercial de produto.
- Skill `lk-trends-product-intelligence` já codifica o workflow e os guardrails.
- O relatório mestre `lk-trends-master-market-radar-cron-base-2026-05-26.md` já tem régua, ranking e fila de decisão.

### 2.2 Fonte internacional

- KicksDev/KicksDB foi definido como fonte primária programática para StockX/GOAT.
- Snippets web ficaram corretamente como fallback/sanity-check.
- Já existe script read-only de probe KicksDev.
- O relatório bruto KicksDev foi salvo como evidência auditável.

### 2.3 Régua comercial

- Há regra clara para sourcing:
  - 150+ vendas/90d; ou
  - 15%+ da líder; ou
  - 50+ vendas/90d com assimetria; ou
  - collab forte + escassez; ou
  - pedido/fit BR comprovado.
- Há downgrade explícito para retail saturado, busca BR vazia de intenção ou histórico ruim LK/BR.
- Produtos são roteados para sourcing, watchlist, catálogo-preview, conteúdo downstream ou ignorar.

### 2.4 Guardrails

- O cron/relatório não compra, não contacta fornecedor, não publica e não altera Shopify/Tiny/Merchant/Klaviyo/ads sem aprovação.
- Saída Telegram exige fonte, confiança, risco, próxima ação segura e aprovação necessária.

## 3. O que falta melhorar

### 3.1 Watchlist persistente

Hoje existe relatório e probe, mas falta uma watchlist estruturada em JSON/YAML com:

- modelo;
- colorway;
- SKU/slug StockX/GOAT/KicksDev;
- categoria de decisão;
- thresholds de alerta;
- status LK;
- motivo de entrada;
- motivo de saída;
- próxima checagem.

Sem isso, cada relatório depende demais de reconstrução manual.

### 3.2 Rotina viva / automação aprovada

O PRD dizia que cron automático estava fora do escopo v1. O relatório mestre desenhou o cron, mas não há comprovação aqui de rotina semanal ativa rodando e entregando relatório.

Próximo nível seguro:

- manter execução manual/read-only agora;
- só ativar cron depois de Lucas aprovar cadência, canal de entrega, critérios de alerta e kill criteria.

### 3.3 Validação Brasil ainda incompleta

O radar já usa DataForSEO/Google Ads BR, mas a camada Brasil precisa ficar mais forte:

- Droper por SKU/colorway, não só snippets;
- retail oficial/local para saturação;
- concorrentes brasileiros relevantes;
- preço BR comparável;
- sinais de venda/velocidade quando disponíveis.

### 3.4 Cruzamento LK interno

O radar ainda dependeu bastante de busca pública LK. Para decisão comercial real, precisa cruzar read-only com:

- Shopify: produto/coleção/variante/tag/preço;
- Tiny: estoque no depósito correto;
- sell-through/pedidos recentes;
- busca interna/atendimento/CRM quando disponível.

Sem isso, a recomendação deve continuar como hipótese, não como autorização de sourcing.

### 3.5 Detecção de novidade fora do Brasil

O sistema está bom para analisar seeds conhecidas, mas ainda precisa de uma camada de descoberta ativa:

- lançamentos/collabs recentes de Hypebeast, Highsnobiety, Sneaker News, Nice Kicks, Vogue etc.;
- top movers KicksDev quando endpoint/lista permitir;
- marcas/linhas fora do radar óbvio;
- sinais de moda internacional antes de aparecer no Brasil.

### 3.6 Liquidez relativa por família

A régua existe, mas precisa virar cálculo fixo no pipeline:

- líder da família/modelo;
- % da líder por colorway;
- exceção documentada quando houver collab/escassez;
- bloqueio automático de colorway marginal.

Isso evita repetir erro de tratar colorway fraca como gap só porque a LK ainda não tem.

## 4. Estado atual dos candidatos do radar anterior

### Jacquemus x Nike Moon Shoe SP

- Status: watchlist alta / sourcing seletivo.
- Bom: collab premium, liquidez internacional forte, sinal fashion.
- Falta: grade interna LK, preço de entrada, Droper/retail BR e margem.
- Próxima ação segura: montar pacote por colorway/tamanho antes de qualquer contato.

### Nike Vomero Premium

- Status: motor de demanda BR + grade/colorway.
- Bom: busca BR forte, liquidez internacional, LK já tem base.
- Falta: cruzar sell-through/estoque LK e preço real por colorway.
- Próxima ação segura: top 5 colorways KicksDev vs LK vs Droper.

### Nike Mind 002

- Status: reposição/grade/watchlist, não descoberta.
- Bom: liquidez internacional forte em algumas CWs.
- Falta: demanda BR sustentada e validação de giro LK.
- Próxima ação segura: só recomendar compra se houver ruptura/velocidade interna.

### Puma Speedcat Ballet

- Status: watchlist média/alta.
- Bom: versão separada do Speedcat genérico, com sinal internacional próprio.
- Falta: prova BR específica, filtro adulto, saturação retail.
- Próxima ação segura: validar Ballet adulto por SKU e preço antes de pacote Júlio.

### New Balance 1906L

- Status: catálogo-preview / watchlist alta.
- Bom: gap público LK aparente e liquidez internacional material.
- Falta: demanda BR específica e fit real com público LK.
- Próxima ação segura: ficha de monitoramento com Metallic Silver, Black, Black Angora e Black Croc.

### Adidas SL 72

- Status: conteúdo/PDP downstream, não sourcing StockX/GOAT.
- Bom: busca BR alta.
- Falta: liquidez internacional forte no recorte e prova de escassez.
- Próxima ação segura: melhorar descoberta/conversão da coleção existente; só sourcing se colorway especial escassa.

### New Balance 204L

- Status: reposição seletiva; modelo já capturado.
- Bom: fit LK validado, Mushroom líder clara.
- Falta: ruptura/grade interna e preço de compra por tamanho.
- Próxima ação segura: monitorar líderes; ignorar CWs pequenas salvo pedido específico.

### On x Loewe Cloudsolo

- Status: ignorar para sourcing recorrente.
- Bom: curadoria luxo.
- Falta: liquidez e giro suficientes.
- Próxima ação segura: reavaliar só com pedido interno ou oportunidade pontual de preço.

## 5. Próximo ciclo recomendado

### Entrega 1 — Watchlist canônica

Criar `lk-trends-watchlist-v1.json` com os candidatos atuais e campos padronizados.

### Entrega 2 — Radar semanal v1 real

Gerar um novo relatório semanal no template `lk-trend-weekly-v1`, separando:

- sourcing;
- watchlist;
- catálogo-preview;
- conteúdo downstream;
- ignorar.

### Entrega 3 — Camada Brasil

Para os P1/P2, validar:

- Droper;
- retail BR;
- busca BR;
- saturação;
- faixa de preço.

### Entrega 4 — Cruzamento LK read-only

Checar presença e gaps reais na LK antes de sugerir pacote Júlio:

- coleção/produto;
- variação/colorway;
- estoque/grade;
- sinais de venda quando disponíveis.

### Entrega 5 — Approval packet, não execução

Quando um candidato passar na régua, preparar pacote para Lucas/Júlio com:

- item exato;
- SKU/colorway/tamanho;
- evidência internacional;
- evidência Brasil;
- preço estimado/custo se validado;
- risco;
- decisão solicitada.

Nenhum contato, compra ou publicação sem aprovação atual.

## 6. Decisão operacional sugerida

Próxima decisão segura: produzir a watchlist canônica v1 e, em seguida, rodar um relatório semanal v1 atualizado.

Aprovação necessária: nenhuma para documentação local/read-only. Necessária apenas para ativar cron automático, contato com Júlio/fornecedor, compra, publicação ou writes em sistemas externos.
