# LK-TRENDS — Paperclip-inspired weekly radar

Data: 2026-05-31
Origem: diretriz de Lucas por áudio.
Status: regra de produto/rotina em construção. Read-only/documental.

## Contexto

Lucas usava anteriormente uma ferramenta chamada Paperclip que gerava um relatório útil sobre o que estava bombando fora do Brasil. O LK-TRENDS deve absorver a lógica desse tipo de relatório e adaptar para o ecossistema LK Sneakers/Hermes.

## Intenção

LK-TRENDS deve produzir, de forma recorrente, um radar semanal sobre:

- o que está bombando fora do Brasil;
- o que está esfriando ou não merece energia;
- quais tendências já existem no site da LK;
- quais tendências são lacuna de catálogo;
- quais merecem divulgação, newsletter, conteúdo, source page ou campanha futura;
- quais merecem sourcing/watchlist/catálogo-preview.

## Fontes esperadas

### Mercado/resale

- KicksDev/KicksDB como fonte programática primária para StockX/GOAT.
- StockX e GOAT para liquidez, preço, vendas, colorways, ranks e SKUs.

### Social/recent web

- Reddit.
- X/Twitter.
- TikTok/social quando disponível.
- Skill/workflow tipo `last30days` para detectar movimento recente.

### Blogs/editoriais de moda e sneakers

- Hypebeast.
- Highsnobiety.
- Vogue.
- Sneaker News.
- Nice Kicks.
- Outros blogs/fontes de moda quando relevantes.

## Cruzamento obrigatório com LK

Depois de detectar o sinal externo, LK-TRENDS deve cruzar com a LK:

1. O modelo/colorway já existe no site?
2. A LK tem estoque/grade ou só página/coleção?
3. Está vendendo bem ou tem potencial de boost?
4. É lacuna de catálogo?
5. É oportunidade de conteúdo/divulgação ou de sourcing?

## Exemplos de decisão

### Caso A — LK já tem o modelo

Exemplo: LK vende bastante Adidas Samba e surge uma nova collab importante de Adidas Samba.

Decisão provável:

- não tratar como descoberta de produto;
- recomendar energia de divulgação;
- criar preview de newsletter/conteúdo/source page/PDP/storytelling;
- sugerir boost se estoque e fit estiverem bons;
- handoff para LK Growth/Shopify apenas com aprovação adequada.

### Caso B — LK não tem o modelo/colorway

Decisão provável:

- classificar como lacuna;
- validar demanda BR e saturação;
- preparar catálogo-preview ou pacote de sourcing;
- acionar Júlio apenas após aprovação explícita.

## Entrega semanal desejada

Formato: newsletter-style semanal, executiva e legível.

Destinatários desejados por Lucas:

- Lucas: heli@lksneakers.com.br
- Renan: renan@lksneakers.com.br
- Daniela: daniela@lksneakers.com.br
- Júlio: julio@lksneakers.com.br

Observação de segurança: preparar a newsletter localmente é permitido; enviar e-mail exige aprovação explícita atual com destinatários e conteúdo final.

## Saída esperada por item

- Produto/modelo/colorway.
- O que está acontecendo fora.
- Fonte.
- Sinal social/editorial.
- Sinal StockX/GOAT/KicksDev.
- Sinal Brasil/Droper.
- Status LK: já temos / não temos / ambíguo.
- Rota: boost/conteúdo, sourcing, watchlist, catálogo-preview ou ignorar.
- Confiança.
- Risco.
- Próxima ação segura.
- Aprovação necessária.

## Guardrails

Sem aprovação explícita atual, LK-TRENDS pode:

- pesquisar;
- cruzar fontes;
- preparar relatório/newsletter preview;
- documentar no Brain;
- gerar handoff interno.

Sem aprovação explícita atual, LK-TRENDS não pode:

- enviar a newsletter;
- publicar no site;
- criar/alterar produto Shopify;
- contactar Júlio/fornecedor;
- comprar/reservar/negociar;
- prometer preço, estoque ou prazo.
