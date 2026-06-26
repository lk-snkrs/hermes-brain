# QVNtnC / U5C43z — Blueprint v2 com filtros por modelo/marca

Data: 2026-06-10
Contexto: Lucas sinalizou que a sequência não pode repetir o mesmo sentido. Pediu uma lógica no meio do flow com conteúdo sobre modelo/marca do tênis no carrinho, exemplo New Balance 9060, e email 3 com 10% de desconto + urgência.

## Resposta estratégica

Sim: o flow pode usar condicionais dentro do Klaviyo para trocar o conteúdo do meio conforme o produto do checkout.

Caminho recomendado: manter o Email 1 universal, inserir Conditional Split depois do Email 1 e ramificar o Email 2 por modelo/marca.

## Arquitetura v2

### Email 1 — Universal / continuidade

Função: lembrar que a seleção continua disponível, com tom calmo.

- Não fala ainda de modelo específico.
- Não fala de desconto.
- CTA principal: Retomar checkout.
- CTA secundário: Falar com a LK.

### Conditional Split — Produto/modelo no checkout

Exemplos de condições possíveis, dependendo do payload do evento Shopify/Klaviyo:

- Checkout/cart item name contains `9060`.
- Checkout/cart item name contains `New Balance`.
- Checkout/cart item SKU contains padrão de família 9060, se existir.
- Checkout/cart item collection/category/tag contains `New Balance` ou `9060`, se sincronizado.
- Fallback: item title/variant title contains.

Observação: antes de ativar, precisa confirmar o campo exato disponível no evento de checkout abandonado no Klaviyo. Não assumir nome do campo sem readback/test profile.

### Email 2A — Branch New Balance 9060 / modelo específico

Função: editorial de produto, não lembrete de checkout.

Título proposto: `Por que o 9060 continua tão forte`

Tese: o 9060 funciona porque mistura herança runner New Balance com proporção chunky/retro-futurista, criando um tênis que segura looks casuais, alfaiataria relaxada e repertório street/editorial.

Fontes de inspiração / sinais externos consultados:

- Hypebeast mantém tag ativa de New Balance 9060 com cobertura recorrente de colorways como Dark Olivine, Cortado, Silver Metallic, Vintage Indigo, Grey, Sea Salt/Dream State, Angora, Mushroom/Arid Stone e variações retro/futuristas.
- GQ cita o New Balance 9060 no território de dad shoes e como sneaker que funciona para quebrar alfaiataria/suits de forma mais atual.
- Vogue traz New Balance/9060 em contexto de street style e também aponta a força de sneakers com calças/trousers como combinação de elegância e facilidade.

Blocos de conteúdo:

1. `A silhueta`
   - chunky sem parecer exagero gratuito;
   - leitura Y2K/runner com acabamento atual;
   - volume que aparece no look.
2. `Como usar`
   - calça ampla/alfaiataria relaxada;
   - denim reto ou wide;
   - activewear premium / travel uniform;
   - contraste com peças mais limpas.
3. `Por que faz sentido na LK`
   - curadoria de modelo com presença;
   - escolha para repertório, não apenas tendência.

CTA: `Revisar o 9060`
CTA secundário: `Pedir orientação de tamanho/styling`

### Email 2B — Branch New Balance genérico

Função: editorial de marca/família quando o carrinho é New Balance mas não 9060.

Título: `New Balance, quando o tênis vira repertório`

Conteúdo: heritage running, conforto, silhuetas que conversam com moda, equilíbrio entre urbano e clássico.

### Email 2C — Branch sneaker genérico / fallback

Função: repertório de styling para o produto escolhido sem inventar dados do modelo.

Título: `Como essa escolha entra no seu repertório`

### Email 3 — Incentivo comercial aprovado

Função: conversão.

Proposta de Lucas: desconto de 10% com urgência.

Versão LK recomendada: usar urgência temporal real, não escassez falsa.

Título proposto: `Uma condição para decidir hoje`

Copy-base:

`Se a escolha ainda faz sentido, liberamos uma condição especial para concluir hoje: 10% off no checkout.`

`É um incentivo pontual — não uma pressão. A seleção continua sendo sua.`

CTA: `Usar 10% e concluir`

Cuidados:

- Precisa aprovar cupom/código/regra no Klaviyo/Shopify antes de subir live.
- Não prometer estoque, pronta entrega, tamanhos ou disponibilidade.
- Não usar “últimas unidades” sem validação do lk-stock.
- Urgência permitida: prazo do incentivo/cupom, se tecnicamente configurado.

### Email 4 — Fechamento / último contato

Função: encerrar com limpeza.

Título: `Última nota sobre sua seleção`

Sem novo argumento. Só fechamento elegante e suporte humano.

## Estrutura resumida

1. Email 1 universal — continuidade.
2. Conditional split por modelo/marca.
3. Email 2 editorial específico:
   - 9060;
   - New Balance genérico;
   - fallback styling.
4. Email 3 comercial — 10% com urgência real.
5. Email 4 fechamento — último contato.

## Próximos passos seguros

1. Auditar payload do evento de checkout no Klaviyo para confirmar o campo exato para filtro de `9060`/`New Balance`.
2. Refazer HTML local do Email 2 como branch 9060 editorial.
3. Refazer Email 3 como 10% com urgência temporal real.
4. Só depois atualizar templates/flow draft.
5. Ativação live continua bloqueada por dupla confirmação.
