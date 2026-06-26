# Blueprint v1 — Rebuild do Flow QVNtnC

Data: 2026-06-10
Flow: `QVNtnC`
Link: https://www.klaviyo.com/flow/QVNtnC/edit
Nome atual: `Hash - Abandonment Checkout`
Status read-only: `live`
Trigger type: `Metric`
Flow actions detectadas: 7
Writes externos: 0
Ativação/pausa/edição: 0
Values printed: false

## 1. Decisão estratégica

Reconstruir como um **Checkout Concierge Flow**, não como um abandono de checkout varejista.

A LK não deve aparecer como uma loja pressionando a finalização. A LK deve aparecer como uma boutique que acompanha uma decisão de compra rara, com procedência, repertório e atendimento humano.

### Nova tese

**A escolha começou no checkout, mas a decisão continua com curadoria.**

### Promessa emocional

Comprar na LK é comprar com segurança, orientação e filtro — especialmente quando a peça é rara, desejada ou exige confiança.

### Frase-guia do flow

**Sua seleção continua aqui — com tempo, cuidado e orientação da LK.**

## 2. O que melhorar no flow atual

Como o flow atual é legado e live, a reconstrução deve corrigir principalmente:

- tom de abandono genérico;
- eventual excesso de cobrança ou urgência;
- estética de e-commerce comum;
- falta de narrativa LK;
- sequência que provavelmente trata todo lead igual;
- ausência de uma camada clara de concierge/atendimento;
- risco de desconto cedo demais;
- pouco uso de confiança, autenticidade e repertório como argumentos.

## 3. Regras de marca para este flow

### Usar

- curadoria;
- seleção;
- escolha;
- procedência;
- autenticidade;
- atendimento humano;
- orientação;
- repertório;
- revisar a seleção;
- retomar com calma.

### Evitar

- `você esqueceu algo` como headline principal;
- `corre`, `última chance`, `garanta agora`;
- contagem regressiva;
- cupom no primeiro contato;
- promessa de estoque, grade, prazo ou pronta entrega;
- tom marketplace;
- botão gritado;
- trust block com cara técnica/SaaS.

## 4. Estrutura recomendada do novo flow

### Nome interno sugerido

`LK | Checkout Concierge — Abandono de Checkout v1`

### Gatilho

`Started Checkout` / métrica equivalente usada no Klaviyo.

### Exit / flow filters obrigatórios para validar no Klaviyo antes de ativar

- saiu do flow se realizou pedido desde que entrou;
- não enviar para quem não tem consentimento aplicável;
- limite de reentrada: sugerido 14 a 30 dias;
- suprimir quem já recebeu uma sequência de abandono recente;
- suprimir perfis com email inválido/suppressed;
- não usar estoque ou disponibilidade como condição criativa sem validação `lk-stock`.

## 5. Sequência de contatos proposta

### Email 1 — 1h depois

**Papel:** lembrete calmo / continuidade da seleção.

**Subject principal:** Sua seleção continua aqui

**Alternativas:**

- Um olhar final antes da escolha
- A curadoria que você começou
- Sua seleção, com tempo para decidir

**Preview text:**

A LK mantém o caminho aberto para você revisar a escolha com calma.

**Headline:**

Sua seleção continua aqui.

**Subheadline:**

Algumas escolhas merecem mais do que impulso. Se ainda faz sentido, você pode retomar o checkout com calma — ou falar com a LK antes de concluir.

**CTA primário:** Retomar checkout

**CTA secundário:** Falar com a LK

**Blocos visuais:**

1. header preto LK;
2. hero off-white com headline serifada;
3. bloco dinâmico do produto/checkout, se disponível;
4. nota curta de atendimento;
5. footer limpo.

**Tom:** silencioso, direto, sem cobrança.

---

### Email 2 — 20–24h depois

**Papel:** confiança / procedência / autenticidade.

**Subject principal:** Escolher raro exige confiança

**Alternativas:**

- Antes de concluir: procedência e cuidado
- O que sustenta uma escolha LK
- Mais do que encontrar. Escolher bem.

**Preview text:**

Autenticidade, curadoria e atendimento humano fazem parte da experiência LK.

**Headline:**

Escolher raro exige confiança.

**Subheadline:**

Na LK, a compra não termina no checkout. Ela passa por uma leitura de procedência, cuidado com a seleção e suporte humano quando a decisão pede detalhe.

**CTA primário:** Voltar ao checkout

**CTA secundário:** Pedir orientação

**Blocos visuais:**

1. hero editorial sem produto exagerado;
2. três pontos de serviço boutique:
   - Autenticidade e procedência;
   - Curadoria com repertório;
   - Atendimento humano;
3. CTA baixo ruído;
4. nota final: `O que é raro, merece ser encontrado.`

**Tom:** institucional premium, não defensivo.

---

### Email 3 — 48h depois

**Papel:** styling / repertório / desejo racionalizado.

**Subject principal:** Como essa peça entra no seu repertório

**Alternativas:**

- Uma escolha pensada para durar no armário
- Do produto ao styling
- Se ainda faz sentido, vale revisar

**Preview text:**

Uma seleção LK deve fazer sentido no uso, no styling e no tempo.

**Headline:**

Do produto ao repertório.

**Subheadline:**

Uma boa escolha volta para a cabeça porque resolve mais do que uma compra: rotina, presença, styling e identidade. Se a seleção ainda conversa com você, vale revisar.

**CTA primário:** Revisar seleção

**CTA secundário:** Falar sobre tamanho ou styling

**Blocos visuais:**

1. imagem/produto abandonado se o Klaviyo permitir;
2. micro-bloco editorial:
   - para usar agora;
   - para permanecer no armário;
   - para combinar com o seu repertório;
3. atendimento como concierge.

**Tom:** editorial e consultivo.

---

### Email 4 — 72h ou 4 dias depois

**Papel:** encerramento elegante / último lembrete.

**Subject principal:** Último lembrete sobre sua seleção

**Alternativas:**

- Uma última nota antes de encerrar
- Se ainda estiver considerando, estamos por aqui
- Sua seleção, pela última vez neste flow

**Preview text:**

Se a escolha ainda faz sentido, este é o último lembrete para retomar.

**Headline:**

Uma última nota sobre sua seleção.

**Subheadline:**

Este é o último lembrete deste flow. Se ainda estiver considerando, você pode retomar o checkout ou conversar com a LK para decidir com mais segurança.

**CTA primário:** Retomar checkout

**CTA secundário:** Falar com a LK

**Blocos visuais:**

1. layout mais curto;
2. sem grade pesada;
3. sem desconto automático;
4. fechamento elegante.

**Tom:** final, humano, sem pressão.

## 6. Layout base recomendado

Usar uma base LK/Klaviyo visual, com adaptação para flow:

- 640px de largura;
- header preto com LK;
- off-white como base;
- serifada apenas para headline;
- Helvetica/Arial para texto;
- CTA preto limpo;
- produto dinâmico como elemento de apoio, não vitrine agressiva;
- bloco concierge curto;
- footer com slogan atual.

### Wireframe comum

1. Header LK
2. Eyebrow discreto: `Checkout Concierge`
3. Headline editorial
4. Parágrafo curto
5. Bloco do produto/checkout abandonado
6. CTA principal
7. Nota concierge / WhatsApp
8. Footer

## 7. Split/segmentação sugerida para v2

Depois do v1 funcionar, considerar splits:

### Cliente novo vs recorrente

- Novo: mais confiança, autenticidade, atendimento.
- Recorrente: mais curadoria, continuidade, repertório.

### Valor do checkout

- Alto valor: concierge e decisão assistida.
- Médio/baixo: retomar seleção + contexto de produto.

### Categoria

- Sneaker: cultura, autenticidade, raridade.
- Apparel/luxo casual: styling, composição, uso.
- Presentes: cuidado e orientação.

## 8. Métricas para avaliar

- placed order rate do flow;
- revenue per recipient;
- click rate por email;
- drop-off por etapa;
- opt-out/spam por etapa;
- cliques em WhatsApp/atendimento;
- performance por novo vs recorrente;
- tempo médio até conversão.

## 9. Plano de migração seguro

1. Manter QVNtnC live.
2. Criar novo flow em draft/clone com nome LK.
3. Recriar emails com nova estrutura.
4. QA interno:
   - delays;
   - filtros;
   - exit conditions;
   - links;
   - dinâmicos;
   - mobile;
   - compliance;
   - sem promessa de estoque/prazo.
5. Enviar testes Klaviyo se endpoint/rota estiver validado.
6. Lucas aprova visual/copy.
7. Dupla confirmação para troca live:
   - pausar antigo;
   - ativar novo;
   - monitorar 24h.

## 10. Gate de aprovação

Aprovação atual necessária apenas para avançar para pacote criativo detalhado ou build draft.

Ações que ainda NÃO foram feitas:

- criar flow;
- editar flow live;
- pausar QVNtnC;
- ativar novo flow;
- alterar filtros/delays;
- enviar teste.

## 11. Próximo entregável recomendado

Criar **Preview local dos 4 emails** em HTML, usando base visual LK, para Lucas aprovar o layout antes de qualquer Klaviyo write.

Depois do preview aprovado:

- transformar em templates/draft no Klaviyo;
- QA;
- pedir dupla confirmação para migração live.
