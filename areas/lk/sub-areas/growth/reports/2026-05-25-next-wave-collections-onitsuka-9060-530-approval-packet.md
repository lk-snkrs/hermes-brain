# Approval packet — próximo bloco editorial/reveal de coleções

Data: 2026-05-25
Escopo: Onitsuka Tiger, New Balance 9060, New Balance 530

## Pedido limpo

Aprimorar as páginas de coleção seguindo a lógica já aplicada em 204L e Moon Shoe:

- texto editorial curto, premium e comercial;
- no mobile: primeiras 3 linhas visíveis;
- imagem logo abaixo;
- clique em "Ler mais" ou na imagem inicial revela texto completo + fotos;
- clique nas fotos abertas revela imagem grande em modal/lightbox, sem sair da loja;
- sem usar taxonomia pública de estoque/pronta entrega/encomenda.

## Páginas-alvo verificadas publicamente

- Onitsuka Tiger: https://lksneakers.com.br/collections/onitsuka-tiger
- New Balance 9060: https://lksneakers.com.br/collections/new-balance-9060
- New Balance 530: https://lksneakers.com.br/collections/new-balance-530

## Diagnóstico público rápido

### Onitsuka Tiger

- Página focada em Mexico 66, Mexico 66 SD, Sabot e colaborações.
- Forte potencial editorial por herança japonesa, linhas baixas e leitura fashion.
- Oportunidade: explicar diferença entre Mexico 66 clássico, SD e Sabot sem virar texto técnico excessivo.

### New Balance 9060

- Página com variedade alta de colorways: cinza, branco, bege, marrom, preto, rosa, verde e colorido.
- Potencial comercial: posicionar como silhueta mais volumosa/sculptural da New Balance, diferente do 530 e 204L.
- Oportunidade: orientar escolha por intenção de uso: neutros, terrosos, statement e contraste.

### New Balance 530

- Página com perfil running retrô, muitas opções metálicas/brancas/cinzas e algumas colaborações.
- Potencial comercial: modelo de entrada premium/versátil dentro de New Balance.
- Oportunidade: simplificar escolha por cor e uso diário.

## Copy sugerida — versão inicial

### Onitsuka Tiger

Kicker: Curadoria LK · Onitsuka Tiger
Título: Herança japonesa, leitura contemporânea.
Texto:
Onitsuka Tiger ocupa um lugar raro entre sneaker clássico e peça de estilo. A linha Mexico 66 carrega proporção baixa, listras marcantes e uma presença que funciona tanto em looks minimalistas quanto em composições mais fashion. Na LK Sneakers, a curadoria reúne pares originais da marca japonesa — do Mexico 66 ao SD e ao Sabot — para quem busca um tênis leve, reconhecível e menos óbvio. A escolha ideal passa por cor, material e intenção de uso: amarelos criam ponto focal, brancos e azuis são mais clássicos, enquanto tons bege, prata e preto aproximam o par de uma estética mais urbana.

### New Balance 9060

Kicker: Curadoria LK · New Balance 9060
Título: Volume escultural, presença imediata.
Texto:
O New Balance 9060 é a leitura mais expressiva da marca para quem quer conforto, proporção ampla e visual contemporâneo. A silhueta combina referências running com uma sola escultural, criando presença sem depender de excesso. Na LK Sneakers, a curadoria prioriza colorways originais que vão dos neutros fáceis — Sea Salt, Raincloud, Moonbeam e Triple White — aos tons terrosos e versões mais marcantes. Para escolher bem, vale pensar no papel do par no look: base neutra, ponto de volume ou contraste fashion.

### New Balance 530

Kicker: Curadoria LK · New Balance 530
Título: Running retrô para uso real.
Texto:
O New Balance 530 é um dos pares mais versáteis da marca: leve, confortável e com estética running retrô que atravessa rotina, viagem e produções casuais. A silhueta funciona especialmente bem em tons brancos, prateados, cinzas e cremes, mas também ganha força em versões coloridas e colaborações pontuais. Na LK Sneakers, a curadoria reúne pares originais para quem quer um New Balance fácil de usar, com presença suficiente para elevar o look sem competir com o restante da composição. A escolha passa por cor, acabamento e frequência de uso.

## Direção visual

- Onitsuka Tiger: editorial urbano/japonês, Mexico 66 em uso, close de listras e styling de rua.
- NB 9060: imagens com volume/sola e styling oversized/neutro.
- NB 530: running retrô, prata/branco, street/casual leve.

## Risco

- Usar imagens externas pode depender de CDN de terceiros. Ideal: subir imagens finais para Shopify Files depois.
- Publicar em produção exige backup do asset `sections/lk-collection.liquid` e verificação pública.
- Não alterar preço, estoque, feed, coleção, produto ou checkout.

## Rollback

Antes de qualquer publish em produção:

1. baixar `sections/lk-collection.liquid` do tema live;
2. salvar em `areas/lk/sub-areas/growth/receipts/theme-production/.../sections__lk-collection.production.before.liquid`;
3. rollback = re-upload do arquivo salvo no mesmo tema live.

## Próximo passo recomendado

1. Criar preview no tema dev para as 3 páginas.
2. Enviar screenshots/links para aprovação visual.
3. Só publicar em produção após aprovação explícita de Lucas.
