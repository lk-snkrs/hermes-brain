# LK-TRENDS — Pipeline de fontes v1

Status: referência operacional read-only
Origem: diretriz Lucas / Paperclip-like radar

## Objetivo

Transformar sinais externos em decisões seguras para a LK:

- boost/divulgação quando LK já tem o produto;
- sourcing quando existe lacuna real e evidência forte;
- catálogo-preview quando há tese promissora mas incompleta;
- watchlist quando falta prova;
- ignorar quando o risco/ruído é alto.

## Pipeline semanal

### 1. Seeds e descoberta

Entradas:

- Seeds manuais de Lucas.
- Watchlist LK-TRENDS.
- Lançamentos/collabs recentes.
- Blogs/editoriais de moda/sneakers.
- Social/recent web.
- KicksDev/StockX/GOAT top movers quando disponível.

Saída:

- Lista bruta de candidatos: modelo + colorway + marca + fonte + motivo.

### 2. Liquidez internacional

Fonte primária:

- KicksDev/KicksDB para StockX/GOAT.

Campos mínimos:

- product id / slug / SKU;
- colorway;
- gender/grade;
- weekly_orders;
- orders_7d / 30d / 90d;
- avg price / lowest ask quando disponível;
- família/modelo líder;
- liquidez relativa vs líder.

Regra:

- Snippets Google só fallback/sanity-check.
- Não usar hype editorial como prova de compra sem liquidez ou exceção forte.

### 3. Social e recent web

Fontes desejadas:

- Reddit;
- X/Twitter;
- TikTok/social quando disponível;
- skill/workflow tipo `last30days`;
- busca web recente.

Uso:

- identificar conversa, aceleração e contexto cultural;
- não substituir dados de venda/liquidez;
- detectar early signals antes de virar busca BR.

### 4. Blogs/editoriais

Fontes:

- Hypebeast;
- Highsnobiety;
- Vogue;
- Sneaker News;
- Nice Kicks;
- outros blogs de moda/sneakers.

Uso:

- collabs;
- lançamentos;
- colorways novas;
- narrativa cultural;
- timing para conteúdo/newsletter.

### 5. Validação Brasil

Fontes:

- DataForSEO / Google Ads BR;
- Droper;
- retail oficial/local;
- concorrentes brasileiros;
- notícias/marketplaces BR quando relevantes.

Perguntas:

- existe busca BR?
- existe oferta ou venda no Droper?
- está saturado no retail?
- preço local permite margem?
- o público LK tende a comprar?

### 6. Cruzamento LK

Checar read-only:

- produto/coleção existe?
- colorway existe?
- grade/tamanho existe?
- estoque e sell-through, se disponível;
- histórico comercial informado por Lucas;
- fit com curadoria LK.

Rotas:

- LK tem + fit/estoque bom = boost/newsletter/conteúdo.
- LK tem família, falta CW/grade = gap analysis / sourcing seletivo.
- LK não tem + evidência forte = catálogo-preview ou sourcing packet.
- Evidência fraca = watchlist/ignorar.

### 7. Classificação e saída

Para cada candidato, classificar em uma rota primária:

- boost;
- sourcing;
- catálogo-preview;
- watchlist;
- ignorar.

Saídas:

- relatório semanal;
- newsletter preview;
- watchlist atualizada;
- approval packet quando houver ação externa.

## Frequência sugerida

- Semanal completo: newsletter/relatório LK-TRENDS.
- Diário leve futuro: watchlist KicksDev e alertas, apenas se aprovado.
- Sob demanda: modelo/collab citado por Lucas.

## Aprovação

Ativação de cron/envio automático exige aprovação explícita com:

- cadência;
- canal;
- destinatários;
- kill criteria;
- nível de alerta;
- o que pode e não pode ser feito automaticamente.
