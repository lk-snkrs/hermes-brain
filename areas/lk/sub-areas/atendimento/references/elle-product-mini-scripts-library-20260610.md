# Elle — Biblioteca inicial de mini scripts por modelo/linha v2

Data: 2026-06-10
Status: rascunho operacional para validação Lucas/Larissa.
Uso: resposta inicial quando cliente chega de página/link ou cita interesse em modelo específico.

## Fontes usadas nesta revisão

- Pesquisa web/Google solicitada por Lucas para levantar contexto e linguagem dos modelos.
- Google Search foi consultado via ambiente local, mas a página retornou sem snippets estruturados aproveitáveis; complementei com pesquisa web em páginas públicas/oficiais quando acessíveis.
- Fonte rica complementar: busca pública do site LK (`/search/suggest.json`) para descrições dos produtos realmente presentes no catálogo.
- Arquivos locais de apoio:
  - `/opt/data/profiles/lk-ops/reports/crisp-elle-learning/elle_product_google_research_20260610.json`
  - `/opt/data/profiles/lk-ops/reports/crisp-elle-learning/lk_site_product_suggest_20260610.json`

## Regras gerais

- Usar apenas como **contexto/estilo/produto**, não como promessa comercial.
- Não afirmar disponibilidade, pronta entrega, estoque em loja, preço atual, reserva ou prazo.
- Se o cliente perguntar “tem no tamanho X?”, “tem na loja?”, “está disponível?” → transbordar para Larissa/lk-stock.
- Se perguntar status de pedido/rastreio/prazo de pedido → transbordar para Larissa.
- Se for dúvida de forma, conforto, estilo ou características gerais, Elle pode responder conforme base aprovada.
- Quando houver link/página de produto, reconhecer o produto antes de perguntar genericamente.

Abertura padrão na primeira resposta real:

```text
Boa tarde, {nome}. Como vai?
Aqui é a Elle da LK.
```

Sem nome:

```text
Boa tarde, como vai?
Aqui é a Elle da LK.
```

## Modelos priorizados pelo export Crisp

- Onitsuka Tiger: 134 conversas
- Onitsuka Tiger Mexico 66: 53 conversas
- New Balance 9060: 35 conversas
- New Balance 204L: 18 conversas
- Adidas Samba: 14 conversas
- Nike Dunk: 12 conversas
- New Balance 530: 11 conversas
- Adidas SL 72: 9 conversas
- Nike Vomero: 8 conversas
- Air Jordan 1: 6 conversas

---

# Scripts por modelo/linha

## Adidas by Stella McCartney Sportswear X Trainers

```text
Vai ser um prazer te ajudar.
Esse Adidas by Stella McCartney tem uma pegada bem fashion e esportiva ao mesmo tempo, com uma proposta mais ousada e diferente dos Adidas clássicos.
É aquele tipo de modelo que chama atenção pelo design e pela colaboração com a Stella McCartney.
Como posso te ajudar com ele?
```

Se for o Bold Gold amarelo:

```text
Esse colorway Bold Gold é bem marcante, com um amarelo forte e visual de bastante presença.
É uma escolha para quem quer um sneaker mais fashion, diferente e com personalidade.
Como posso te ajudar com ele?
```

Bloqueio: não confirmar preço/estoque/tamanho disponível sem fonte viva.

## New Balance 9060

```text
O New Balance 9060 é um dos modelos mais fortes da New Balance hoje.
Ele mistura conforto de running com uma estética mais robusta, chunky e moderna.
Como posso te ajudar com ele?
```

Variação mais consultiva:

```text
O 9060 é bem confortável e tem bastante presença no pé, com aquele visual mais robusto que funciona muito bem em looks casuais e streetwear.
Como posso te ajudar com ele?
```

Fit seguro:

```text
O 9060 costuma ter forma regular e confortável.
Na maioria dos casos, pode seguir seu número habitual.
```

## New Balance 204L

```text
O New Balance 204L tem uma proposta mais baixa, casual e versátil, com inspiração no running retrô.
É uma opção bem fácil de usar no dia a dia e menos robusta que modelos como o 9060.
Como posso te ajudar com ele?
```

Fit aprovado por Lucas:

```text
O 204L tem forma mais regular.
Na maioria dos casos, pode seguir seu número habitual.
Se você fica entre dois tamanhos ou gosta de usar mais folgado, eu iria no maior.
```

Regra: não pedir link/modelo só para falar de forma do 204L; a forma é tratada como a mesma entre variações.

## New Balance 1906 / 1906R

```text
O New Balance 1906 tem uma estética running retrô bem forte, com visual técnico e bastante conforto.
É um modelo que conversa muito com essa tendência de tênis esportivo usado no dia a dia.
Como posso te ajudar com ele?
```

## New Balance 530

```text
O New Balance 530 é um clássico de visual running dos anos 90, leve e confortável.
Ele tem uma estética mais esportiva e funciona muito bem para uso diário.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
O 530 costuma ter forma confortável.
Na maioria dos casos, dá para seguir seu número habitual.
```

## New Balance 550

```text
O New Balance 550 tem uma estética basketball retrô, com visual mais estruturado e casual.
É um modelo bem versátil para quem gosta de sneaker mais clássico e com presença.
Como posso te ajudar com ele?
```

## Adidas Samba

```text
O Adidas Samba é um dos grandes clássicos da Adidas.
Ele tem uma silhueta baixa, casual e muito versátil, com aquela pegada retrô que funciona bem em vários estilos.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
O Samba costuma ter forma mais ajustada, principalmente por ser um modelo baixo e mais fino.
Se você fica entre dois tamanhos, vale considerar o maior.
```

## Adidas Gazelle

```text
O Adidas Gazelle é um clássico casual da Adidas, com visual baixo e retrô.
Ele é uma opção bem versátil para quem quer um tênis fácil de combinar, mas com mais personalidade que um básico comum.
Como posso te ajudar com ele?
```

## Adidas Handball Spezial / Spezial

```text
O Adidas Spezial tem uma pegada retrô bem forte e virou um dos modelos mais desejados da Adidas.
Ele tem perfil baixo, visual casual e combina muito bem com looks do dia a dia.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
O Spezial costuma vestir de forma mais regular, mas por ser um modelo baixo, quem gosta de mais folga pode considerar o tamanho maior se estiver entre dois números.
```

## Adidas Campus

```text
O Adidas Campus tem uma estética casual clássica, com construção mais encorpada que Samba e Gazelle.
É um modelo versátil e com visual bem street.
Como posso te ajudar com ele?
```

## Adidas SL 72

```text
O Adidas SL 72 tem uma proposta running retrô, mais leve e vintage.
É uma opção ótima para quem gosta de tênis baixo, com visual esportivo clássico e fácil de usar no dia a dia.
Como posso te ajudar com ele?
```

## Adidas Yeezy

```text
O Yeezy tem uma proposta bem marcante, com design mais futurista e bastante presença no look.
Qual modelo de Yeezy você tem interesse?
```

Regra: há muitos Yeezys com formas diferentes; perguntar o modelo antes de orientar tamanho.

## Onitsuka Tiger — genérico

```text
Qual modelo você tem interesse?
A forma pode variar um pouco dependendo do modelo.
```

Com gênero masculino conhecido:

```text
Qual modelo você está mais interessado?
A forma pode variar um pouco dependendo do modelo.
```

Regra Lucas: não dar orientação genérica de tamanho para Onitsuka sem saber o modelo.

## Onitsuka Tiger Mexico 66

```text
O Onitsuka Tiger Mexico 66 é um clássico da marca, com silhueta baixa, visual retrô e as listras laterais bem características.
É um modelo leve, mais fino e muito versátil para uso casual.
Como posso te ajudar com ele?
```

Se o cliente citar Kill Bill/amarelo:

```text
Esse Mexico 66 amarelo é um dos colorways mais icônicos do modelo, muito associado ao visual do Kill Bill.
É um tênis de bastante personalidade, mas com a mesma silhueta baixa e clássica do Mexico 66.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
O Mexico 66 costuma ter uma forma mais ajustada e bico mais fino.
Se você tem o pé mais largo ou fica entre dois tamanhos, eu consideraria o maior.
```

## Onitsuka Tiger Mexico 66 Sabot

```text
O Mexico 66 Sabot é diferente do Mexico 66 tradicional: ele mantém a identidade do modelo, mas vem em formato mule, com o calcanhar aberto.
É uma versão mais prática, leve e muito boa para quem quer o visual da Onitsuka com uma pegada mais casual.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
Por ser aberto no calcanhar, o Sabot costuma ter um ajuste mais tolerante.
Mesmo assim, como vem da base do Mexico 66, o bico tende a ser mais fino; se seu pé for mais largo, vale considerar o maior.
```

Regra: tratar Sabot como modelo próprio, não como Mexico 66 comum.

## Nike Dunk

```text
O Nike Dunk é um clássico de visual urbano, com silhueta baixa e bastante presença.
Ele funciona muito bem em looks casuais e streetwear.
Como posso te ajudar com ele?
```

Se for SB Dunk:

```text
O Nike SB Dunk tem uma construção mais ligada ao skate, normalmente com mais estrutura e amortecimento que o Dunk tradicional.
É um modelo muito procurado também por colecionadores.
Como posso te ajudar com ele?
```

## Air Jordan 1

```text
O Air Jordan 1 é uma das silhuetas mais icônicas da Jordan, com visual basketball retrô e muita personalidade.
É um modelo para quem quer um sneaker clássico, mas com bastante presença.
Como posso te ajudar com ele?
```

## Air Force 1

```text
O Air Force 1 é um clássico da Nike, com visual casual, estrutura mais robusta e muita versatilidade.
É aquele modelo fácil de usar no dia a dia e que combina com praticamente tudo.
Como posso te ajudar com ele?
```

## Nike Vomero — genérico

```text
O Nike Vomero tem uma proposta running, com foco em conforto e amortecimento.
Hoje ele também aparece muito no uso casual por esse visual esportivo mais moderno.
Qual Vomero você está olhando?
```

Regra: perguntar qual Vomero quando a pergunta for genérica, porque Vomero 5, Vomero Plus/Premium e outros podem ter propostas diferentes.

## Nike Vomero Premium

```text
O Nike Vomero Premium é uma versão bem especial da linha Vomero, com foco em amortecimento máximo e visual bem futurista.
Ele tem uma presença forte no pé e mistura performance running com uma estética bem fashion.
Como posso te ajudar com ele?
```

Variação mais técnica, se o cliente perguntar detalhes:

```text
O Vomero Premium trabalha uma proposta de amortecimento bem alto, com tecnologias de corrida da Nike e uma sensação mais macia/impactante.
É bem diferente de um sneaker casual básico.
```

Bloqueio: não prometer uso técnico/running ideal para o cliente sem entender necessidade; para treino sério, sugerir avaliar conforto/uso pretendido.

## Nike V2K

```text
O Nike V2K tem uma estética running moderna, com visual robusto e esportivo.
Ele é uma boa opção para quem quer conforto no dia a dia com uma aparência mais atual.
Como posso te ajudar com ele?
```

## Nike Shox

```text
O Nike Shox tem um visual muito marcante por causa da estrutura característica no solado.
É um modelo com bastante personalidade e uma pegada retrô esportiva forte.
Como posso te ajudar com ele?
```

## Asics GEL-Kayano

```text
O Asics GEL-Kayano tem origem em corrida e é conhecido pelo conforto e suporte.
Hoje ele também funciona muito bem no uso casual, principalmente para quem gosta de visual esportivo mais técnico.
Como posso te ajudar com ele?
```

## Asics GEL-NYC

```text
O Asics GEL-NYC mistura estética running retrô com conforto para o dia a dia.
É um modelo bem versátil para quem gosta de tênis esportivo com visual mais atual.
Como posso te ajudar com ele?
```

## Puma Speedcat

```text
O Puma Speedcat tem uma silhueta mais baixa e fina, inspirada no universo automobilístico.
É um modelo bem estiloso para quem gosta de tênis mais discreto, diferente e com visual vintage.
Como posso te ajudar com ele?
```

Fit cauteloso:

```text
Por ser um modelo mais baixo e fino, pode vestir mais justo.
Se você fica entre dois tamanhos, vale considerar o maior.
```

## Mizuno Wave / Wave Prophecy

```text
Os modelos Mizuno Wave têm um visual bem técnico e marcante, principalmente pelo solado característico.
São opções para quem busca conforto e um sneaker com bastante presença.
Como posso te ajudar com ele?
```

## Salomon XT-6

```text
O Salomon XT-6 tem uma pegada outdoor/técnica, mas ficou muito forte também no uso urbano.
É um modelo com visual utilitário, confortável e cheio de personalidade.
Como posso te ajudar com ele?
```

## UGG — genérico

```text
Os modelos UGG têm uma proposta mais confortável e casual, geralmente com visual mais aconchegante.
Qual modelo você está olhando?
```

## UGG Tasman

```text
O UGG Tasman é um modelo bem confortável e casual, com visual de slipper premium.
Ele é muito procurado por quem quer praticidade e conforto para o dia a dia.
Como posso te ajudar com ele?
```

## Birkenstock — genérico

```text
A Birkenstock é conhecida pelo conforto e pelo visual casual, com modelos que funcionam muito bem no dia a dia.
Qual modelo você tem interesse?
```

## Birkenstock Boston

```text
A Birkenstock Boston é um clássico em formato clog, com visual casual e muito conforto.
É uma opção prática, fácil de usar e que combina bem com looks mais relaxados.
Como posso te ajudar com ela?
```

---

# Regras de uso por tipo de pergunta

## Cliente veio de link/produto e disse “gostaria de saber mais”

1. Abrir com saudação + Elle da LK.
2. Reconhecer o modelo com mini script.
3. Perguntar como ajudar com ele.

## Cliente perguntou forma/tamanho

- Se modelo tem orientação aprovada: responder.
- Se marca/linha tem muitas formas: perguntar modelo.
- Se pergunta é “tem meu tamanho?”: transbordar para Larissa/lk-stock.

## Cliente perguntou estoque/disponibilidade/loja

Não responder disponibilidade. Usar:

```text
Vou pedir para a Larissa conferir certinho para você.
```

ou, se precisar coletar dado antes:

```text
Qual tamanho você está procurando?
Vou encaminhar para a Larissa conferir certinho.
```

## Cliente perguntou status/pedido/rastreio

Não responder status. Usar:

```text
Me manda o número do pedido, por favor?
Vou encaminhar para a Larissa conferir certinho para você.
```

## Próximos passos

1. Lucas/Larissa revisar linguagem e corrigir frases que não soem LK.
2. Expandir para os 50 modelos mais acessados/perguntados.
3. Vincular scripts por handle/SKU/família de produto no contexto da Elle.
4. Criar avaliação: cliente vem de link → Elle reconhece modelo → usa script correto → não promete estoque/preço.
