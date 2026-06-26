# QVNtnC Checkout Concierge — Email 2 expanded branch copy v1

Data: 2026-06-11
Direção aprovada por Lucas: seguir com ordem provisória de branches:

1. 9060
2. 530
3. Mexico 66
4. Mexico 66 Sabot
5. Vomero / Vomero Premium
6. Nike Mind 001/002
7. Adidas terrace / low-profile
8. fallback

## Guardrails

- Arquitetura segue com 3 emails, sem quarto email.
- Email 2 é o único branchado nesta v1.
- Cada Email 2 deve mostrar produto/carrinho e CTA cedo.
- Não prometer estoque, tamanho, pronta entrega ou últimas unidades.
- Ativação Klaviyo continua bloqueada até readback + dupla confirmação.
- Flow filter obrigatório antes de ativar: `Placed Order since starting this flow = 0`.

## Estrutura padrão de cada Email 2

1. Hero editorial do modelo/família.
2. Bloco dinâmico do produto abandonado.
3. CTA primário imediato.
4. Bloco de repertório/styling.
5. CTA secundário ou WhatsApp, se fizer sentido.

---

## Branch 1 — New Balance 9060

**Condição sugerida**

- item/title/SKU contém `9060`

**Subject**

Por que o 9060 continua tão forte

**Preview**

Volume, conforto e uma leitura runner que funciona além do óbvio.

**Headline**

O 9060 não é só presença. É proporção.

**Copy hero**

O New Balance 9060 funciona porque combina herança runner com uma leitura mais ampla, quase retro-futurista. É o tipo de silhueta que aparece no look sem precisar de excesso: segura denim amplo, alfaiataria relaxada e uniformes urbanos com a mesma naturalidade.

**Produto/checkout block intro**

A seleção que você começou ainda pode ser retomada no checkout.

**CTA primário**

Fechar carrinho

**Editorial support**

Use com calça wide, jeans reto, peças técnicas ou uma base mais limpa para deixar o volume trabalhar. Na curadoria LK, o 9060 entra como escolha de repertório: confortável, visual e menos óbvio que um runner tradicional.

**CTA secundário**

Falar com a LK sobre tamanho ou styling

---

## Branch 2 — New Balance 530

**Condição sugerida**

- item/title/SKU contém `530`

**Subject**

O 530 e a força do sneaker fácil

**Preview**

Leve, versátil e com leitura running sem pesar no look.

**Headline**

Um runner limpo para usar muito.

**Copy hero**

O New Balance 530 tem uma força mais silenciosa: ele entrega a leitura running, mas com uma silhueta fácil de combinar. É uma escolha para quem quer conforto, rotina e estética sem transformar o tênis no único assunto do look.

**Produto/checkout block intro**

Sua seleção continua disponível para revisão.

**CTA primário**

Fechar carrinho

**Editorial support**

Funciona com jeans claro, alfaiataria casual, activewear premium e peças de viagem. A graça está justamente no equilíbrio: esportivo, mas polido; casual, mas com repertório.

**CTA secundário**

Pedir orientação da LK

---

## Branch 3 — Onitsuka Tiger Mexico 66

**Condição sugerida**

- item/title/SKU contém `Mexico 66`
- excluir quando também contiver `Sabot`, para não capturar a mule/sabot indevidamente

**Subject**

Mexico 66: o low-profile que muda o look

**Preview**

Uma silhueta fina, clássica e fácil de levar para diferentes repertórios.

**Headline**

Menos volume. Mais intenção.

**Copy hero**

O Mexico 66 tem a força dos tênis baixos que não precisam disputar atenção. A silhueta fina deixa o look mais leve e conversa bem com denim reto, calças amplas, alfaiataria casual, saias e peças mais limpas.

**Produto/checkout block intro**

Se essa foi a escolha, ela ainda pode ser concluída no checkout.

**CTA primário**

Concluir com o Mexico 66

**Editorial support**

A leitura é vintage, mas o uso é atual: um sneaker para quando a intenção é tirar peso da produção sem perder identidade. O resultado é mais fashion do que esportivo puro.

**CTA secundário**

Falar com a LK antes de concluir

---

## Branch 4 — Onitsuka Tiger Mexico 66 Sabot

**Condição sugerida**

- item/title/SKU contém `Mexico 66 Sabot`
- aliases possíveis: `Sabot`, `Mule`, `Slip-On` somente se confirmados no payload

**Subject**

Mexico 66 Sabot: facilidade com leitura fashion

**Preview**

A versão mais solta da silhueta, pensada para rotina, viagem e styling.

**Headline**

A escolha mais fácil de calçar — e difícil de ignorar.

**Copy hero**

O Mexico 66 Sabot leva a silhueta clássica para um território mais relaxado. A construção mule traz praticidade, mas o efeito no look continua intencional: casual, leve e com leitura fashion sem esforço.

**Produto/checkout block intro**

Sua seleção ainda pode ser retomada no checkout.

**CTA primário**

Fechar carrinho

**Editorial support**

Use com calças amplas, bermudas, vestidos casuais ou peças de viagem. É um produto de transição: menos formal que o sneaker fechado, mais interessante que um slide comum.

**CTA secundário**

Pedir ajuda da LK

---

## Branch 5 — Nike Vomero / Vomero Premium

**Condição sugerida**

- item/title/SKU contém `Vomero`
- se possível separar `Vomero Premium` apenas quando volume justificar

**Subject**

Vomero: conforto com presença

**Preview**

Um runner de volume, textura e uso real.

**Headline**

Quando conforto também constrói o look.

**Copy hero**

O Vomero ocupa o espaço dos runners que entregam conforto, mas não desaparecem visualmente. A silhueta tem volume, linhas técnicas e uma leitura urbana que funciona tanto em rotina quanto em viagem.

**Produto/checkout block intro**

A seleção iniciada no checkout continua disponível.

**CTA primário**

Concluir seleção

**Editorial support**

Combine com activewear premium, cargos, jeans solto ou alfaiataria relaxada. A ideia não é parecer esportivo demais — é usar o runner como contraponto técnico dentro de um look bem resolvido.

**CTA secundário**

Falar com a LK sobre a escolha

---

## Branch 6 — Nike Mind 001 / Mind 002

**Condição sugerida**

- item/title/SKU contém `Mind 001`
- item/title/SKU contém `Mind 002`
- agrupar como `Nike Mind` nesta v1, salvo volume para separar depois

**Subject**

Nike Mind: uma escolha de design

**Preview**

Uma silhueta para quem procura forma, novidade e repertório.

**Headline**

Nem todo sneaker precisa parecer familiar.

**Copy hero**

Nike Mind entra em um território mais conceitual: forma, construção e presença visual. É uma escolha para quem procura algo menos esperado, mas ainda usável dentro de um guarda-roupa urbano.

**Produto/checkout block intro**

Se essa leitura ainda faz sentido, o checkout pode ser retomado.

**CTA primário**

Fechar carrinho

**Editorial support**

Funciona melhor quando o resto do look dá espaço para a silhueta: peças limpas, calças com boa queda, tons neutros ou combinações que deixam o design aparecer sem excesso.

**CTA secundário**

Pedir orientação de styling

---

## Branch 7 — Adidas terrace / low-profile

**Condição sugerida**

- item/title/SKU contém `Samba`
- item/title/SKU contém `Gazelle`
- item/title/SKU contém `Campus`
- item/title/SKU contém `Taekwondo`
- item/title/SKU contém `SL 72`
- aliases terrace/low-profile só se existirem como tags/categorias no payload

**Subject**

Low-profile: o sneaker que limpa o look

**Preview**

Samba, Gazelle, Campus e outras silhuetas baixas seguem fortes pela versatilidade.

**Headline**

A força está na linha baixa.

**Copy hero**

Os Adidas de leitura terrace e low-profile funcionam porque afinam a proporção do look. São tênis que entram fácil: denim, alfaiataria casual, saias, vestidos, peças esportivas e bases minimalistas.

**Produto/checkout block intro**

A seleção que você iniciou continua pronta para revisão.

**CTA primário**

Concluir seleção

**Editorial support**

Quando o sneaker tem menos volume, o styling ganha leveza. É uma escolha para quem quer presença sem peso — e um caminho seguro para deixar o visual mais atual sem depender de exagero.

**CTA secundário**

Falar com a LK

---

## Branch 8 — Fallback curadoria LK

**Condição sugerida**

- caminho default quando nenhum modelo/família prioritária for detectado

**Subject**

Uma curadoria para decidir com calma

**Preview**

Sua seleção continua disponível, com a LK por perto se precisar.

**Headline**

A escolha certa não precisa ser apressada.

**Copy hero**

Se você chegou até essa seleção, provavelmente existe um motivo: forma, desejo, uso ou repertório. A LK mantém o caminho aberto para você revisar o produto com calma e concluir quando fizer sentido.

**Produto/checkout block intro**

Seu checkout pode ser retomado aqui.

**CTA primário**

Retomar checkout

**Editorial support**

Nossa curadoria existe para reduzir ruído: procedência, autenticidade e leitura de produto fazem parte da experiência. Se restar qualquer dúvida antes da compra, a equipe pode ajudar.

**CTA secundário**

Falar com a LK

## Fontes vivas consultadas para repertório macro

- Who What Wear — cobertura/tag Onitsuka Tiger 2026 e menções a Mexico 66/Sabot no contexto de moda.
- Highsnobiety / Hypebeast — sinais de Vomero Premium e agenda sneaker 2026.
- InStyle — sinal de Adidas slim/low-profile/Samba em tendências de primavera 2026.

Usar como repertório editorial, não como promessa de disponibilidade, estoque ou ranking de venda.
