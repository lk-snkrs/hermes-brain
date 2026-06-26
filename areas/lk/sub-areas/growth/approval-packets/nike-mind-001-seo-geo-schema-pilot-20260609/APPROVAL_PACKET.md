# Approval Packet — Nike Mind 001 SEO/GEO/schema pilot — 2026-06-09

Status: **preview / approval packet / sem write externo**  
Criado em: 2026-06-09 14:15 UTC  
Owner: LK Growth  
Escopo pedido por Lucas: executar item 1 do cron Growth de hoje.

## Decisão solicitada

Aprovar a preparação/executar em ambiente seguro de preview/dev, antes de qualquer produção, de um piloto para melhorar CTR e AI answerability de Nike Mind 001.

**Não aprovado neste packet sem nova confirmação:** publicar title/meta/copy/schema em produção, alterar theme production, alterar preço/estoque/disponibilidade, alterar campanha, alterar GMC.

## URLs alvo

- Collection/hub: `https://lksneakers.com.br/collections/nike-mind-001`
- PDP Black Chrome: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`
- PDP Pearl Pink: `https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa`

## Evidência verificada

Fontes:

- Cron LK SEO/GSC + GEO 2026-06-09.
- GSC e GA4 read-only do cron.
- Fetch público das páginas LK.
- DataForSEO keyword overview Brazil/PT.
- DataForSEO SERP live mobile Brazil/PT para `nike mind 001`.

Fatos:

- GSC PDP Black Chrome: **53.614 impressões / 29 cliques / CTR 0,05% / posição 8,1**.
- GSC PDP Pearl Pink: **28.749 impressões / 12 cliques / CTR 0,04% / posição 8,9**.
- Collection Nike Mind 001: **5.165 impressões / 66 cliques / CTR 1,28% / posição 8,4**.
- GA4 PDP Black Chrome: **208 sessões orgânicas**.
- URL Inspection Black Chrome: indexada, canonical OK, mobile crawl OK.
- CrUX PDP: LCP **1.362ms good**, CLS **0,0 good**, TTFB **613ms good**.
- DataForSEO `nike mind 001`: volume Brasil **18.100**, intenção **transactional**, competição paid **high**.
- SERP mobile: Nike domina orgânico #1/#2; LK aparece em popular products como seller para variação White Speed Red; PAA inclui “O que o Nike Mind 001 faz?”, “Quanto custa?”, “Qual a função?”, “Quando chega no Brasil?”.

## Diagnóstico

O gargalo não parece ser indexação ou velocidade. O problema é captura de clique e consolidação de intenção:

- PDPs têm volume muito alto e CTR quase nulo.
- Collection/hub performa melhor em CTR, mas recebe muito menos impressões que PDPs.
- SERP mistura PDP oficial Nike, social/video, shopping cards e perguntas informacionais.
- A LK precisa separar papel de URL:
  - collection: intenção genérica e comparação Nike Mind 001/002;
  - PDPs: colorway, autenticidade, tamanho e decisão final.

## Proposta de trabalho em preview

### 1) Collection/hub — bloco citável

Adicionar/revisar bloco direto, self-contained, sem linguagem operacional de estoque/prazo:

> O Nike Mind 001 é a versão aberta da linha Nike Mind, criada para uma leitura de conforto sensorial, descanso e presença visual. Ele funciona como um slide escultural: mais relaxado que um sneaker fechado, mas com design forte o suficiente para entrar em looks casuais e fashion. A diferença para o Mind 002 está no uso: o 001 é aberto, mais voltado a recuperação, casa, viagem e styling de impacto; o 002 é fechado e se aproxima mais de um tênis urbano. Na LK Sneakers, a escolha passa por cor, proporção, intenção de uso e orientação humana para comparar tamanho e acabamento antes da decisão.

### 2) FAQ preview

Perguntas propostas:

- O que o Nike Mind 001 faz?
- Qual a diferença entre Nike Mind 001 e Nike Mind 002?
- Nike Mind 001 é tênis de corrida?
- Nike Mind 001 é confortável para usar na rua?
- O Nike Mind 001 da LK é original?

### 3) Title/meta — hipótese de teste

Manter tom premium e evitar promessas de disponibilidade.

- Collection title candidato: `Nike Mind 001 Original | Guia, 001 vs 002 e Curadoria LK`
- Collection meta candidata: `Compare Nike Mind 001 e 002 na curadoria LK: design sensorial, cores, proporção, autenticidade e orientação humana para escolher o par ideal.`

PDPs devem manter colorway no title e reforçar papel de produto específico, sem competir com a collection pelo termo broad.

### 4) Schema/QA

- Verificar FAQPage parity com o conteúdo visível.
- Investigar warning de Merchant/rich result `shippingRate` sem alterar GMC neste pacote.
- Validar canonical e evitar URLs parametrizadas como destino interno.

## Impacto esperado

- CTR de `nike mind 001` e `chinelo nike mind 001`.
- Maior captura pela collection/hub para query broad.
- Menor dispersão entre PDPs e URLs com parâmetros.
- Melhor resposta em AI Search para “o que é”, “função”, “diferença 001/002” e “original no Brasil”.

## Esforço / risco

- Esforço: médio.
- Risco: médio, porque mexe em copy/schema/title/meta visíveis se aprovado para produção.
- Risco específico: conteúdo de PDP atual contém linguagem operacional de prazo/disponibilidade; qualquer ajuste nessa parte precisa validação de atendimento/stock owner antes de virar promessa pública.

## Rollback

Antes de qualquer write:

- Snapshot de SEO fields da collection e PDPs.
- Snapshot de descrição/conteúdo visível.
- Snapshot de schema/theme asset se houver alteração de schema.
- Readback Admin + HTML público pós-write.
- Rollback por reaplicação dos snapshots.

## Aprovação necessária

Para seguir além deste packet:

> “Aprovo o preview/dev do Nike Mind SEO/GEO/schema pilot, sem produção.”

Para publicar em produção depois do preview:

> “Aprovo publicar Nike Mind SEO/GEO/schema em produção conforme preview X.”
