# NB550 — Reactivation Intake / LKGOC Lite Candidate

Data: 2026-06-14T15:10:25Z
Status: read-only; sem writes Shopify/produção.
Owner: [LK] Otimização de Coleções.

## Decisão do Lucas

Lucas sinalizou que, mesmo com baixa venda atual de New Balance 550, a demanda externa pode justificar uma ação de reativação. O enquadramento correto não é “coleção forte que já vende”, e sim **experimento de reativação comercial**.

## Tese

NB550 tem demanda transacional grande no Brasil, mas a LK aparentemente não captura/vende proporcionalmente. O trabalho deve descobrir se o gargalo é:

- curadoria/sortimento;
- preço/competição;
- página/SEO/GEO fracos;
- falta de visibilidade interna/interlink;
- desalinhamento com desejo atual do público LK.

## Evidência pública coletada

### Demanda Google Brasil/pt — DataForSEO

- `new balance 550`: 74.000 buscas/mês; intenção transacional; competição HIGH; maio/2026 60.500.
- `nb 550`: 9.900 buscas/mês; intenção transacional/informacional.
- `tenis new balance 550`: 5.400 buscas/mês; intenção transacional.
- `new balance 550 feminino`: 4.400 buscas/mês; intenção transacional; quarterly +50%.
- `new balance 550 masculino`: 2.400 buscas/mês; intenção transacional; quarterly +53%.
- `new balance 550 verde`: 1.300 buscas/mês.
- `new balance 550 preto`: 1.000 buscas/mês.
- `new balance 550 branco`: 880 buscas/mês.
- `new balance 550 rosa`: 210 buscas/mês.
- `new balance 550 original`: 50 buscas/mês, mas AI volume aparece maior que Google long-tail.

### AI Search Volume

- `new balance 550`: 61/mês.
- `tenis new balance 550`: 22/mês.
- `new balance 550 original`: 15/mês.
- `nb 550`: 12/mês.

### SERP mobile — `new balance 550`

- Top orgânico: New Balance oficial, Netshoes, Sunika, Dafiti, Centauro, World Tennis.
- SERP tem bloco de produtos e PAA.
- LK não apareceu no top 20 orgânico capturado.
- PAA relevantes:
  - New Balance 550 para que serve?
  - New Balance 550 confortável?
  - Por que New Balance é caro?
  - Qual o valor do tênis New Balance 550?

### SERP mobile — `new balance 550 feminino`

- Top orgânico: New Balance oficial, Netshoes, Dafiti, Loja Kings, Loja Virus, Renner, Centauro, Paquetá.
- LK não apareceu no top 20 orgânico capturado.
- PAA relevantes:
  - Qual o New Balance feminino mais vendido?
  - New Balance 550 para que serve?
  - Qual o New Balance que as blogueiras usam?
  - Qual é o tênis New Balance mais top?

## Estado público LK — coleção

URL: https://lksneakers.com.br/collections/new-balance-550

Leitura pública anterior da sessão:

- Title: `New Balance 550 - LK`
- Meta: `Confira os New Balance 550 na LK Sneakers. 100% originais · 10x sem juros · Frete grátis · Loja Jardins SP.`
- H1: `New Balance 550`
- Marcadores públicos: `lk-goc` e `lk-204l` aparecem no HTML, FAQ aparece; precisa QA visual/readback antes de considerar pronto.

## Interpretação

- O volume bruto é alto, mas a tendência anual está em queda vs pico anterior; ainda há volume absoluto suficiente.
- A oportunidade principal não é “rankear no termo geral” imediatamente, pois o SERP é muito forte e preço-driven.
- A oportunidade da LK é capturar **intenção premium/autenticidade/curadoria** e long-tail de feminino/masculino/cores, além de usar autoridade New Balance já construída em 204L/530/9060.
- Como Lucas informou baixa venda atual, o projeto deve ser tratado como experimento com kill criteria, não full rebuild cego.

## Recomendação de execução

### Sprint NB550 Reactivation — Lite, 7–14 dias

1. **Read-only comercial antes de write**
   - Shopify/GA4/GSC: sessões, cliques, CTR, posição, add-to-cart, conversão, receita histórica e PDPs NB550 mais vistos.
   - Se a validação envolver disponibilidade/grade, handoff obrigatório para `lk-stock`; este agente não consulta estoque.

2. **Patch editorial leve em DEV/approval**
   - Reescrever title/meta sem linguagem genérica.
   - Criar bloco citável curto: história 1989, basquete/lifestyle, silhueta retrô, como escolher.
   - FAQ alinhado a PAA: conforto, uso, preço/valor, feminino/masculino, autenticidade.
   - Interlink: NB550 ⇄ New Balance 204L/530/9060 ⇄ todos New Balance.

3. **Sinal comercial/merchandising**
   - Se compras/curadoria quiserem apostar, selecionar 2–4 modelos âncora coerentes com demanda: branco/verde, feminino, preto/branco, neutros.
   - Não prometer disponibilidade na copy.

4. **Medição**
   - Revisão D+7 e D+14: GSC impressions/clicks/CTR, GA4 sessions, add-to-cart, orders/revenue, scroll/clicks se disponível.

## Kill criteria

- Se após exposição e melhoria editorial houver tráfego mas zero engajamento/conversão, não escalar para full LKGOC.
- Se GSC mostrar baixa impressão orgânica e a demanda não chega, tratar como problema de ranqueamento/autoridade, não de CRO.
- Se vendas só dependem de sortimento/preço indisponível, travar LKGOC e rotear para compras/curadoria.

## Aprovação necessária

- Qualquer alteração em SEO title/meta/descrição/FAQ em produção exige aprovação explícita de Lucas.
- DEV/unpublished/preview pode ser preparado sem produção, seguindo LKGOC e Shopify dev-first.
- Estoque/disponibilidade deve ser confirmado apenas por `lk-stock`.
