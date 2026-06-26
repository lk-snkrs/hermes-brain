# PRD / Approval packet — Rebuild flow QVNtnC

Data: 2026-06-10
Perfil: LK Content
Flow Klaviyo: `QVNtnC`
Link: https://www.klaviyo.com/flow/QVNtnC/edit
Nome atual: `Hash - Abandonment Checkout`
Status read-only: `live`
Trigger type: `Metric`
Ações detectadas via read-only: 7 flow-actions
Writes realizados: 0
Flow activation realizada: false
Values printed: false

## Pedido Lucas

> reconstruir ele do zero; repensar layout, títulos, fluxo de contatos e posicionamento de loja.

## Diagnóstico inicial

Este é um flow de abandono de checkout legado (`Hash - Abandonment Checkout`) e está **live**. Por segurança, a recomendação é não editar o live diretamente.

Direção operacional segura:

1. manter o flow atual live até o novo estar pronto;
2. desenhar um novo flow paralelo/draft com arquitetura, copy, layout e delays aprovados;
3. QA visual + links + regras de exclusão;
4. só então pedir dupla confirmação para pausar/trocar/ativar.

## Tese de reposicionamento LK

O abandono de checkout da LK não deve parecer cobrança, urgência falsa ou varejo promocional. Deve parecer continuação de atendimento premium:

- curadoria humana;
- autenticidade e confiança;
- produto raro sob encomenda;
- orientação para escolher melhor;
- WhatsApp como concierge, não SAC genérico;
- desconto como último recurso, não primeiro argumento.

## Objetivo do flow

Recuperar intenção sem vulgarizar a marca.

Objetivos secundários:

- reduzir fricção de confiança;
- reforçar legitimidade LK;
- levar quem tem dúvida para atendimento humano;
- preservar margem;
- aprender quais argumentos movem melhor: raridade, confiança, styling/curadoria, atendimento.

## Arquitetura recomendada — versão premium

### Entrada

Trigger: Started Checkout / Abandoned Checkout.

Filtros recomendados para validar no Klaviyo antes de qualquer ativação:

- excluir quem realizou pedido desde o início do flow;
- excluir quem recebeu campanha muito recente, se houver risco de saturação;
- limitar frequência de entrada no flow;
- respeitar consentimento email/SMS;
- não fazer promessa de disponibilidade/estoque/prazo.

## Sequência proposta

### Email 1 — 1h após abandono

Função: lembrete editorial leve, sem pressão.

Título recomendado:

**Sua seleção continua aqui**

Alternativas:

- **Um olhar final antes da escolha**
- **A curadoria que você começou**
- **Seu checkout, com tempo para decidir**

Copy direcional:

> Algumas escolhas merecem mais do que impulso. Se você ainda está considerando o par, sua seleção continua disponível para revisão no checkout.
>
> Na LK, cada compra passa por uma curadoria de autenticidade, procedência e atendimento humano — para que a decisão seja segura do começo ao fim.

CTA:

**Retomar checkout**

Bloco secundário:

**Precisa comparar tamanho, cor ou proposta?**
Fale com a LK antes de concluir.

CTA secundário:

**Falar com atendimento**

Layout:

- header preto LK;
- hero limpo, sem excesso de produto;
- card de produto/checkout se o bloco dinâmico estiver disponível;
- CTA preto sobre fundo off-white;
- bloco concierge curto.

### Email 2 — 20–24h após abandono

Função: confiança, autenticidade, operação premium.

Título recomendado:

**Escolher raro exige confiança**

Alternativas:

- **Antes de concluir: procedência, curadoria e cuidado**
- **O que sustenta uma escolha LK**
- **Mais do que encontrar. Escolher bem.**

Copy direcional:

> O que torna uma escolha LK diferente não é apenas encontrar o produto certo. É comprar com procedência, leitura de curadoria e suporte humano quando a decisão pede detalhe.
>
> Se ficou alguma dúvida sobre tamanho, composição ou uso, nossa equipe pode orientar antes da finalização.

CTA primário:

**Voltar ao checkout**

CTA secundário:

**Pedir orientação**

Layout:

- mais institucional/editorial;
- 3 blocos discretos: Autenticidade / Curadoria / Atendimento humano;
- sem trust grid SaaS; usar linguagem boutique.

### Email 3 — 48h após abandono

Função: styling e contexto; recuperar interesse sem desconto.

Título recomendado:

**Como essa peça entra no seu repertório**

Alternativas:

- **Uma escolha pensada para durar no armário**
- **Do produto ao styling**
- **Se ainda faz sentido, vale revisar**

Copy direcional:

> Algumas compras voltam para a cabeça porque resolvem mais de um uso: rotina, viagem, styling e presença. Se a peça ainda faz sentido, vale revisitar a seleção com calma.

CTA:

**Revisar seleção**

Bloco secundário:

Sugestão editorial: combinar com categorias próximas ou atendimento.

Layout:

- mais visual/editorial;
- usar bloco dinâmico do produto abandonado se permitido;
- evitar excesso de grades e promoções.

### Email 4 — 72h ou 4 dias após abandono

Função: último toque elegante, sem agressividade.

Título recomendado:

**Último lembrete sobre sua seleção**

Alternativas:

- **Se ainda estiver considerando, estamos por aqui**
- **Uma última nota antes de encerrar**
- **Sua seleção, pela última vez neste flow**

Copy direcional:

> Este é o último lembrete sobre a seleção iniciada no checkout. Se ainda estiver considerando, você pode retomar a compra ou conversar com a LK para decidir com mais segurança.

CTA primário:

**Retomar checkout**

CTA secundário:

**Falar com a LK**

Layout:

- curto;
- sofisticado;
- sem desconto automático;
- sem tom de urgência falsa.

## O que eu NÃO recomendo

- cupom no primeiro email;
- contagem regressiva;
- “seu carrinho está esperando” em tom varejista;
- excesso de emojis;
- grid de confiança com cara SaaS;
- promessa de estoque, prazo, disponibilidade ou pronta entrega;
- editar o flow live diretamente sem clone/draft e QA.

## Layout base recomendado

Usar a lógica visual LK já aprovada em campanhas:

- container 640px;
- faixa preta com logo LK;
- fundo off-white/editorial;
- serifada para headlines;
- Helvetica/Arial para corpo;
- CTA preto/off-white;
- blocos com respiro;
- serviço/concierge como parte da experiência;
- footer com slogan atual: `O que é raro, merece ser encontrado.`

## Segmentação/controle de contato

Recomendações para validar em Klaviyo:

- sair do flow se `Placed Order` desde o início;
- não enviar se a pessoa comprou depois do checkout abandonado;
- limitar reentrada, ex.: 14–30 dias;
- suprimir perfis sem consentimento;
- considerar divisão por valor do checkout se o Klaviyo permitir:
  - alto valor: mais concierge/confiança;
  - baixo/médio: mais produto/contexto;
- considerar split por cliente novo vs recorrente:
  - novo: prova de confiança;
  - recorrente: curadoria/continuidade.

## Próximo passo seguro

1. Lucas confirmar se este é o primeiro dos 2 flows.
2. Lucas enviar o segundo link/nome do flow.
3. Criar pacote final v1 com:
   - árvore completa;
   - assunto + preview de cada email;
   - copy final PT-BR;
   - wireframe visual por email;
   - checklist de links/dinâmicos;
   - plano de migração sem derrubar o flow live.

## Aprovação necessária depois

Qualquer uma das ações abaixo exige aprovação explícita e, para ativação/troca live, dupla confirmação no Telegram:

- criar/editar flow no Klaviyo;
- pausar flow live;
- ativar novo flow;
- trocar delays/filtros no live;
- enviar teste Klaviyo, se endpoint/rota estiver validado.
