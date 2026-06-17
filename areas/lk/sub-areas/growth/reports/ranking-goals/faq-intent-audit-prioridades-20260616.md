# LK Growth — Auditoria FAQ por intenção real — prioridades 2026-06-16

Status: read-only + melhoria de processo local.  
Writes externos: 0.  
Motivo: Lucas sinalizou que FAQs genéricos não agregam e prejudicam qualidade comercial/SEO/GEO.

## Veredito executivo

Lucas está certo: o problema não é “ter FAQ”; é FAQ que parece preenchimento SEO. A nova regra deve ser: **FAQ só entra se responder uma dúvida real de busca, comparação, objeção de compra ou decisão de styling/tamanho/autenticidade específica daquele modelo.**

Ação recomendada:

1. **Nike Mind 001 — corrigir primeiro.** O bloco novo melhorou a página, mas ainda ficou abaixo do padrão ideal e convive com um FAQ global/genérico do PDP que polui a experiência.
2. **Nike Vomero Premium — corrigir FAQ do topo da coleção.** Existe pergunta errada/desalinhada citando Vomero 5 como “melhor” dentro da coleção Vomero Premium; isso confunde intenção.
3. **Onitsuka Tiger — manter base, enriquecer intenção “Brasil / Mexico 66 / ASICS / diferença de modelos”.** Está melhor que os outros, mas ainda pode ser mais decisivo.
4. **New Balance 204L — está ok, mas falta FAQ de comparação e intenção de cor/tamanho/versão.** O PAA já puxa autenticidade NB com blog LK; aproveitar isso sem repetir genérico.
5. **Puma Speedcat Ballet / sneakerinas — oportunidade editorial/coleção futura.** Não aplicar sem confirmar superfície/produtos; preparar FAQ de tendência e comparação.

## Regra nova — FAQ Real Intent Gate

Antes de escrever/aplicar FAQ em PDP, coleção ou guia LK, cada pergunta deve passar por pelo menos 1 dos critérios:

- aparece em PAA/PAS/SERP live;
- aparece em GSC como query/variação relevante;
- responde objeção real de compra: tamanho, material, diferença entre versões, autenticidade, styling, uso, tecnologia, preço/faixa/raridade sem prometer disponibilidade;
- ajuda AI Search/GEO com resposta citável específica, não genérica;
- reduz atrito comercial sem invadir estoque/prazo operacional.

Bloqueios:

- Não usar “O produto é original?” como pergunta genérica em todas as páginas. Se usar, precisa falar do modelo/risco real daquele modelo.
- Não usar “Qual prazo de entrega?”, “tem pronta entrega?”, “sob encomenda”, “estoque” em FAQ SEO/GEO. Disponibilidade e prazo ficam em atendimento/chat.
- Não duplicar FAQ: se a descrição já tem FAQ, remover/ocultar FAQ global genérico ou não inserir outro bloco semelhante.
- Não escrever “melhor modelo em 2026” se a coleção é de um modelo específico e a resposta muda para outro produto.
- Se a resposta não muda a decisão de compra, a pergunta sai.

## 1) Nike Mind 001 Black Chrome — PDP

URL: `/products/slide-nike-mind-001-black-chrome-preto`

### Evidência

- PAA/PAS SERP para `nike mind 001`:
  - O que o Nike Mind 001 faz?
  - Quanto custa o Nike Mind 001?
  - Qual a função do Nike Mind?
  - Quando o Nike Mind chega ao Brasil?
  - O Nike Mind 001 pode ajudar com ansiedade?
  - Nike Mind 001 original / preço / feminino / Nocta.
- Fetch público atual confirmou FAQ novo, mas também bloco global genérico abaixo:
  - troca/devolução;
  - prazo;
  - tamanho genérico;
  - originalidade genérica;
  - água/limpeza;
  - embalagem;
  - parcelamento.

### Problema

- O FAQ novo ainda tem perguntas comerciais amplas (“onde comprar”) que parecem SEO filler se não forem mais específicas.
- O bloco global do tema/PDP é mais grave: adiciona ruído, repete autenticidade/tamanho e traz linguagem operacional que não combina com o padrão premium.
- A pergunta sobre ansiedade precisa ser tratada com cuidado: responder sem promessa médica.

### FAQ recomendado — substituir o bloco atual do PDP

1. **O que o Nike Mind 001 faz?**  
   O Nike Mind 001 usa nódulos de espuma sob o pé para criar estímulo sensorial durante o uso. A proposta da linha Nike Mind é trazer uma sensação de presença, conforto e foco antes/depois da rotina esportiva ou no uso casual. Não é um produto médico; é uma leitura experimental de conforto e design.

2. **Qual a diferença entre Nike Mind 001 e Nike Mind 002?**  
   O Mind 001 tem construção aberta de slide/mule, mais escultural e fácil de usar em looks casuais. O Mind 002 tem leitura mais fechada, próxima de um sneaker. A escolha depende de calce, styling e quanto você quer que o modelo apareça no look.

3. **Por que o Black Chrome é uma das versões mais procuradas?**  
   O Black Chrome concentra a proposta futurista da linha em uma cor mais versátil: preto com acabamento cromado. Funciona melhor para quem quer impacto visual sem depender de cores muito chamativas.

4. **O Nike Mind 001 Black Chrome veste como?**  
   A melhor referência é partir da numeração Nike que você já usa. Por ser um mule/slide, a sensação muda conforme largura do pé e preferência de sobra no calcanhar; em dúvida, vale confirmar com a equipe LK antes de finalizar.

5. **Quanto custa um Nike Mind 001 no Brasil?**  
   O valor varia por versão, numeração, origem e raridade. Em modelos mais disputados, a diferença de preço costuma refletir curadoria, autenticidade, condição e disponibilidade comercial do par. O preço válido é sempre o exibido no PDP no momento da compra.

6. **O Nike Mind 001 ajuda com ansiedade?**  
   A Nike apresenta a linha Mind como uma experiência sensorial ligada a foco e presença, mas o produto não deve ser tratado como solução médica para ansiedade. Na LK, a leitura é de design, conforto e bem-estar no uso — sem promessa terapêutica.

### Ajuste técnico recomendado

- Remover/ocultar o FAQ global genérico deste PDP quando houver FAQ específico na descrição. Fazer primeiro em dev theme ou via lógica segura de template/metafield, não direto sem packet.

## 2) Nike Vomero Premium — coleção

URL: `/collections/nike-vomero-premium`

### Evidência

- PAA/PAS SERP:
  - O que é o Nike Vomero Premium?
  - O que é a linha Vomero da Nike?
  - Vomero Premium serve para corrida?
  - Qual o melhor: Vomero Plus ou Premium?
  - Nike Vomero Premium Brasil / feminino / masculino / branco / original / quando chega no Brasil.
- Fetch atual: existe FAQ no topo e guia pós-grid; o FAQ do topo diz “O Nike Vomero 5 é o modelo mais buscado em 2026”, o que está desalinhado com uma coleção de Vomero Premium.

### Problema

- FAQ mistura Vomero 5 com Vomero Premium e dilui a intenção principal.
- Duplicação entre FAQ topo e guia pós-grid.
- A coleção precisa responder tecnologia e comparação, não “melhor modelo genérico”.

### FAQ recomendado

1. **O que é o Nike Vomero Premium?**  
   É a versão mais maximalista da família Vomero, com foco em amortecimento alto, espuma ZoomX, unidades Air Zoom aparentes e uma plataforma de visual futurista.

2. **Vomero Premium serve para corrida ou é mais lifestyle?**  
   Nasce do universo running e funciona para conforto, treinos leves/recuperação e rotina, mas na LK o apelo principal é a combinação de tecnologia visível, conforto generoso e presença lifestyle premium.

3. **Qual a diferença entre Vomero Premium, Vomero Plus e Vomero 5?**  
   O Vomero 5 é mais retrô/lifestyle; o Vomero Plus é mais direto para corrida diária macia; o Vomero Premium é o mais alto, tecnológico e visualmente expressivo.

4. **O Vomero Premium é pesado ou muito alto no pé?**  
   Ele tem plataforma alta e presença maior que um running retrô tradicional. Quem busca discrição pode preferir Vomero 5; quem quer volume, amortecimento e sneaker protagonista tende a preferir o Premium.

5. **Qual cor de Nike Vomero Premium escolher?**  
   Black e tons escuros são mais urbanos; White Bright Crimson e versões com contraste deixam o sneaker mais protagonista; colaborações e colorways especiais são melhores para quem quer peça de destaque.

6. **O Nike Vomero Premium da LK é original?**  
   Sim. A LK trabalha com curadoria de pares originais e atendimento humano para orientar versão, cor e numeração antes da compra.

## 3) Onitsuka Tiger — coleção

URL: `/collections/onitsuka-tiger-todos-os-modelos`

### Evidência

- PAA/PAS SERP:
  - Tem Onitsuka Tiger no Brasil?
  - Diferença entre Onitsuka Tiger e ASICS?
  - A Onitsuka Tiger é da ASICS?
  - Onitsuka Tiger Mexico 66 / Brasil onde comprar / ASICS.
- LK já rankeia organicamente na página 1 para `onitsuka tiger`.

### Problema

- FAQ atual é razoável, mas ainda pode capturar melhor intenção Brasil + comparação de modelos.
- Falta pergunta sobre Mexico 66 vs SD vs Sabot como decisão de compra.

### FAQ recomendado

1. **Tem Onitsuka Tiger original no Brasil?**  
   A distribuição e disponibilidade variam por mercado, mas a LK mantém curadoria de pares originais Onitsuka Tiger no Brasil, com atendimento humano para orientar modelo, material, cor e numeração.

2. **Qual Onitsuka Tiger escolher primeiro?**  
   O Mexico 66 é o ponto de entrada mais versátil: baixo, leve e reconhecível pelas listras. Quem busca acabamento mais premium pode olhar Mexico 66 SD; quem quer calce mais leve pode considerar Sabot ou Slip-on.

3. **Qual a diferença entre Onitsuka Tiger e ASICS?**  
   Onitsuka Tiger é a leitura de herança/lifestyle japonesa ligada à origem da ASICS; ASICS é mais associada à performance e tecnologia de corrida.

4. **Mexico 66, Mexico 66 SD e Sabot: qual a diferença?**  
   Mexico 66 é o clássico baixo; Mexico 66 SD eleva materiais e acabamento; Sabot traz o DNA Onitsuka em formato mule, com styling mais casual e menos óbvio.

5. **Onitsuka Tiger tem forma grande ou pequena?**  
   A forma varia por modelo e material. A referência ideal é comparar com sneakers baixos que você já usa e confirmar com a equipe LK antes da compra.

6. **Por que alguns Onitsuka Tiger custam mais?**  
   Preço varia por modelo, material, cor, raridade e origem do par. Colorways muito buscadas, versões SD, colaborações e tamanhos difíceis tendem a ter valor mais alto.

## 4) New Balance 204L — coleção

URL: `/collections/new-balance-204l`

### Evidência

- PAA/PAS SERP:
  - New Balance 204L bege / Brasil / feminino / branco / 36 / 35.
  - Como identificar New Balance original? — PAA já citando blog da LK.
  - Por que New Balance é tão caro?
- Fetch atual: FAQ bom, mas curto e sem comparação com outras silhuetas NB.

### Problema

- Falta capturar intenção de cor/tamanho/versão e comparação com outras linhas.
- “Originalidade” pode linkar melhor para o blog LK já citado no PAA.

### FAQ recomendado

1. **O que é o New Balance 204L?**  
   É uma silhueta baixa e slim que mistura referências de tênis dos anos 1970 com running retrô dos anos 2000, em construção leve com camurça, mesh e proporção fashion.

2. **New Balance 204L é feminino, masculino ou unissex?**  
   A leitura é unissex, mas a procura costuma ser forte em numerações menores e styling feminino por causa do perfil baixo e da estética “sneakerina/slim sneaker”.

3. **Qual cor do New Balance 204L escolher?**  
   Bege, Mushroom e Timberwolf são mais neutros; branco é mais limpo; Silver Metallic aparece mais no look; Black Magnet é mais urbano.

4. **New Balance 204L tem forma grande ou pequena?**  
   Por ser baixo e slim, pode parecer mais ajustado que modelos volumosos. A melhor referência é comparar com outros New Balance ou sneakers baixos que você já usa e validar com atendimento LK.

5. **Qual a diferença entre New Balance 204L, 530 e 2002R?**  
   O 204L é mais baixo e fashion; o 530 tem leitura running retrô mais esportiva; o 2002R é mais robusto e tecnológico. O 204L é a escolha para quem quer proporção discreta e elegante.

6. **Como saber se o New Balance 204L é original?**  
   Verifique etiqueta interna, código do modelo, acabamento do “N”, qualidade do suede/mesh e consistência geral. A LK também tem guia dedicado sobre New Balance original vs falso para aprofundar a checagem.

## 5) Puma Speedcat Ballet / sneakerinas — pauta futura

Superfície atual LK não confirmada nesta auditoria; não aplicar write sem definir coleção/PDP/guia e sem confirmar se existe página alvo.

### Evidência

- SERP dominada por PUMA, Authentic Feet, ELLE, Shop2gether, Guadalupe e Your ID.
- PAS:
  - Puma Speedcat Ballet Brasil
  - Puma Speedcat Ballet lace
  - tênis Puma Speedcat Ballet feminino
  - Puma Speedcat Ballet prata / rosa / suede.

### FAQ recomendado para futura coleção/guia

1. **O que é o Puma Speedcat Ballet?**  
   É uma releitura do Speedcat que mistura DNA de automobilismo com tiras e proporção inspiradas em sapatilha de balé.

2. **Puma Speedcat Ballet é tênis ou sapatilha?**  
   Ele fica entre os dois: tem base sneaker/Speedcat, mas leitura visual de ballet flat, por isso conversa com a tendência das sneakerinas.

3. **Qual a diferença entre Speedcat Ballet, Speedcat tradicional e Speedcat Metallic?**  
   O tradicional tem pegada racing mais direta; o Ballet tem tiras e visual mais delicado; Metallic/Satin/Glossy mudam acabamento e presença no look.

4. **Como usar Puma Speedcat Ballet?**  
   Funciona com denim reto, saia, alfaiataria leve, vestido minimalista e peças esportivas limpas. A força está no contraste entre sapatilha e sneaker.

5. **Puma Speedcat Ballet veste como?**  
   Por ter perfil baixo e construção mais ajustada, a escolha deve considerar largura do pé e preferência de calce; confirmar numeração antes da compra.

6. **Por que o Speedcat Ballet virou tendência?**  
   Ele combina duas demandas fortes: sneakers baixos de corrida retrô e sapatilhas/sneakerinas. Por isso aparece tanto em editoriais de moda quanto em varejo esportivo.

## Próximo passo recomendado

Criar um **Approval Packet FAQ v2** para:

1. Nike Mind 001 PDP — corrigir FAQ específico + planejar remoção/ocultação do FAQ global genérico em dev theme.
2. Nike Vomero Premium collection — substituir FAQ do topo e consolidar com guia pós-grid.
3. New Balance 204L — enriquecer FAQ com comparação + link interno para guia de autenticidade NB.
4. Onitsuka Tiger — ajuste leve, sem urgência.

## Aprovação necessária para executar

Qualquer aplicação em Shopify/tema/produção exige aprovação explícita. Frase sugerida:

`Aprovo preparar e aplicar o FAQ Intent v2 nas páginas Nike Mind 001, Nike Vomero Premium, Onitsuka Tiger e New Balance 204L, somente nos blocos FAQ/descrição/listados, com rollback/readback, sem alterar preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo. Para remoção de FAQ global, primeiro gerar preview/dev theme.`
