# LK CRO — Correção conceitual sobre tamanho/disponibilidade — 2026-05-18

Lucas corrigiu um erro conceitual no CRO Visual Preview Pack v0: atalhos de tamanho na collection não são um bom módulo de conversão para a LK.

## Correção

A LK vende sob encomenda. Na prática, todos os produtos podem ser compráveis em todos os tamanhos. Portanto, se a pessoa filtra tamanho `37`, o site pode continuar mostrando praticamente todos os produtos.

O que realmente muda comercialmente não é “tem ou não tem tamanho”, mas:

- pronta entrega;
- sob encomenda;
- prazo de obtenção/entrega;
- necessidade de atendimento humano para confirmar expectativa.

Hoje o site não expõe claramente, produto a produto, o que é pronta entrega versus sob encomenda. Logo, usar atalhos de tamanho como promessa de disponibilidade induz a uma leitura errada.

## Ajuste feito no dev theme

Removidos os atalhos numéricos de tamanho do bloco CRO.

Substituição segura:

- Onitsuka Mexico 66:
  - `Curadoria LK`
  - `Mais vendidos`
  - `Novidades`
  - `Consultar prazo`
- Onitsuka todos os modelos:
  - `Mexico 66`
  - `Tokuten`
  - `Delegation`
  - `Serrano`
  - `Prazo sob encomenda`
- Lululemon:
  - `Define`
  - `Nulu`
  - `Leggings`
  - `Shorts`
  - `Consultar prazo`

## Regra para próximos CROs

Não usar filtro/tamanho/estoque como proxy de disponibilidade real na LK. Se o objetivo é reduzir dúvida operacional, o caminho honesto é explicar compra sob encomenda, prazo e atendimento humano, sem prometer disponibilidade por tamanho.
