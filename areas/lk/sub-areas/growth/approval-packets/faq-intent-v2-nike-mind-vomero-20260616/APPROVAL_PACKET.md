# Approval Packet — FAQ Intent v2 — Nike Mind 001 + Nike Vomero Premium — 2026-06-16

Status: **pronto para aprovação de produção**  
Modo: proposta local / sem write externo nesta etapa  
Writes externos executados neste packet: **0**  
values_printed: false

## 1. Pedido / origem

Lucas aprovou seguir após feedback: FAQ genérico não agrega e precisa responder intenção real.  
Base: auditoria `faq-intent-audit-prioridades-20260616.md`.

## 2. Escopo proposto

Aplicar somente nos blocos de conteúdo/FAQ listados abaixo:

1. PDP Nike Mind 001 Black Chrome  
   URL: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`  
   Handle: `slide-nike-mind-001-black-chrome-preto`

2. Collection Nike Vomero Premium  
   URL: `https://lksneakers.com.br/collections/nike-vomero-premium`  
   Handle: `nike-vomero-premium`

## 3. Fora do escopo / não alterar

- preço;
- estoque;
- desconto;
- campanhas;
- GMC/feed;
- Klaviyo/WhatsApp;
- checkout;
- tags operacionais;
- menus;
- imagens;
- theme production fora do ajuste aprovado;
- disponibilidade/prazo como promessa comercial.

## 4. Evidência de intenção real

### Nike Mind 001

SERP/PAA/PAS DataForSEO para `nike mind 001`:

- “O que o Nike Mind 001 faz?”
- “Quanto custa o Nike Mind 001?”
- “Qual a função do Nike Mind?”
- “Quando o Nike Mind chega ao Brasil?”
- “O Nike Mind 001 pode ajudar com ansiedade?”
- PAS: `Nike mind 001 original`, `Nike mind 002`, `Nike mind 001 preço`, `Nike mind 001 feminino`, `Nike mind 001 quando chega no brasil`, `Nike mind 001 nocta`.

Problema atual:

- FAQ específico ainda pode ficar mais decisivo.
- FAQ global genérico aparece abaixo e polui o PDP com perguntas repetidas/operacionais.

### Nike Vomero Premium

SERP/PAA/PAS DataForSEO para `nike vomero premium`:

- “O que é o Nike Vomero Premium?”
- “O que é a linha Vomero da Nike?”
- “Vomero Premium serve para corrida?”
- “Qual o melhor vomero, plus ou premium?”
- PAS: `Nike vomero premium brasil`, `feminino`, `masculino`, `branco`, `original`, `quando chega no brasil`, `black`, `comprar`, `cores`.

Problema atual:

- FAQ no topo cita Vomero 5 como “melhor” dentro de uma coleção Vomero Premium; isso confunde intenção e dilui relevância.
- Há risco de duplicação entre FAQ topo e guia pós-grid.

## 5. Payload proposto — Nike Mind 001 Black Chrome

### Ação A — substituir FAQ específico da descrição do PDP

Manter o bloco descritivo atual e substituir apenas a seção `Perguntas Frequentes` por:

```html
<h3>Perguntas Frequentes</h3>
<dl>
  <dt>O que o Nike Mind 001 faz?</dt>
  <dd>O Nike Mind 001 usa nódulos de espuma sob o pé para criar estímulo sensorial durante o uso. A proposta da linha Nike Mind é trazer uma sensação de presença, conforto e foco antes ou depois da rotina esportiva e também no uso casual. Não é um produto médico; é uma leitura experimental de conforto e design.</dd>

  <dt>Qual a diferença entre Nike Mind 001 e Nike Mind 002?</dt>
  <dd>O Mind 001 tem construção aberta de slide/mule, mais escultural e fácil de usar em looks casuais. O Mind 002 tem leitura mais fechada, próxima de um sneaker. A escolha depende de calce, styling e quanto você quer que o modelo apareça no look.</dd>

  <dt>Por que o Black Chrome é uma das versões mais procuradas?</dt>
  <dd>O Black Chrome concentra a proposta futurista da linha em uma cor mais versátil: preto com acabamento cromado. Funciona melhor para quem quer impacto visual sem depender de cores muito chamativas.</dd>

  <dt>O Nike Mind 001 Black Chrome veste como?</dt>
  <dd>A melhor referência é partir da numeração Nike que você já usa. Por ser um mule/slide, a sensação muda conforme largura do pé e preferência de sobra no calcanhar; em dúvida, vale confirmar com a equipe LK antes de finalizar.</dd>

  <dt>Quanto custa um Nike Mind 001 no Brasil?</dt>
  <dd>O valor varia por versão, numeração, origem e raridade. Em modelos mais disputados, a diferença de preço costuma refletir curadoria, autenticidade, condição e disponibilidade comercial do par. O preço válido é sempre o exibido no PDP no momento da compra.</dd>

  <dt>O Nike Mind 001 ajuda com ansiedade?</dt>
  <dd>A Nike apresenta a linha Mind como uma experiência sensorial ligada a foco e presença, mas o produto não deve ser tratado como solução médica para ansiedade. Na LK, a leitura é de design, conforto e bem-estar no uso — sem promessa terapêutica.</dd>
</dl>
```

### Ação B — FAQ global genérico do PDP

Opção segura recomendada:

- **não mexer direto em produção agora**;
- primeiro criar/validar preview em dev theme para ocultar FAQ global quando o PDP já tiver FAQ específico na descrição;
- se aprovado depois, aplicar lógica condicional.

Motivo: esse FAQ parece vir de tema/módulo global, não só da descrição do produto. Alterar sem preview pode afetar outros PDPs.

## 6. Payload proposto — Nike Vomero Premium

Substituir o FAQ de topo/descrição da coleção por perguntas específicas abaixo. Se houver duplicação com guia pós-grid, consolidar para evitar dois FAQs competindo.

```html
<h3>Perguntas Frequentes</h3>
<dl>
  <dt>O que é o Nike Vomero Premium?</dt>
  <dd>O Nike Vomero Premium é a versão mais maximalista da família Vomero, com foco em amortecimento alto, espuma ZoomX, unidades Air Zoom aparentes e uma plataforma de visual futurista.</dd>

  <dt>Vomero Premium serve para corrida ou é mais lifestyle?</dt>
  <dd>Ele nasce do universo running e funciona para conforto, treinos leves, recuperação e rotina. Na curadoria LK, o apelo principal é a combinação de tecnologia visível, conforto generoso e presença lifestyle premium.</dd>

  <dt>Qual a diferença entre Vomero Premium, Vomero Plus e Vomero 5?</dt>
  <dd>O Vomero 5 é mais retrô e lifestyle; o Vomero Plus é mais direto para corrida diária macia; o Vomero Premium é o mais alto, tecnológico e visualmente expressivo da família.</dd>

  <dt>O Vomero Premium é pesado ou muito alto no pé?</dt>
  <dd>Ele tem plataforma alta e presença maior que um running retrô tradicional. Quem busca discrição pode preferir Vomero 5; quem quer volume, amortecimento e sneaker protagonista tende a preferir o Premium.</dd>

  <dt>Qual cor de Nike Vomero Premium escolher?</dt>
  <dd>Black e tons escuros são mais urbanos; White Bright Crimson e versões com contraste deixam o sneaker mais protagonista; colaborações e colorways especiais são melhores para quem quer peça de destaque.</dd>

  <dt>O Nike Vomero Premium da LK é original?</dt>
  <dd>Sim. A LK trabalha com curadoria de pares originais e atendimento humano para orientar versão, cor e numeração antes da compra.</dd>
</dl>
```

## 7. QA obrigatório após aplicação

### Shopify readback

Confirmar:

- PDP Nike Mind 001 contém novas 6 perguntas exatas;
- Collection Nike Vomero Premium contém novas 6 perguntas exatas;
- não existem `userErrors` na mutação;
- title/meta/preço/estoque não foram alterados;
- descrição/collection body preserva blocos não relacionados.

### Fetch público

Confirmar:

- perguntas renderizadas publicamente;
- não há menção nova a estoque/pronta entrega/encomenda como taxonomia SEO;
- FAQ genérico global ainda aparece ou não aparece, conforme escopo aplicado;
- se ainda aparecer, registrar como pendência de tema/dev preview, não como falha do FAQ específico.

## 8. Risco

- **Baixo** para substituir FAQ específico em descrição/collection body.
- **Médio** para mexer no FAQ global do tema, porque pode afetar múltiplos PDPs. Por isso fica fora da aplicação direta e requer dev preview separado.

## 9. Rollback

Antes de qualquer aplicação:

- salvar `rollback-before.json` com produto/collection completo;
- salvar HTML antes/depois;
- se readback falhar, reexecutar update com o snapshot anterior.

## 10. Plano de impacto

D+7/D+14:

- GSC query + URL:
  - `nike mind 001`
  - `chinelo nike mind 001`
  - `nike mind 001 original`
  - `nike vomero premium`
  - `nike vomero premium original`
  - `nike vomero premium brasil`
- Métricas:
  - impressões;
  - cliques;
  - CTR;
  - posição média;
  - sessões orgânicas;
  - add-to-cart/order quando disponível.

## 11. Aprovação necessária para aplicar produção

Para aplicar no Shopify production, preciso da aprovação explícita abaixo:

`Aprovo aplicar o FAQ Intent v2 de 2026-06-16 no PDP Nike Mind 001 Black Chrome e na coleção Nike Vomero Premium, somente nos blocos FAQ/descrição listados, com rollback/readback, sem alterar preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo. FAQ global do tema deve ficar apenas como dev-preview/packet separado.`
