# PRD — LK Growth Action System

Data: 2026-05-19
Status: `proposed_for_execution`
Escopo: Growth/SEO/CRO/GMC/GA4/GSC/GEO/Paid signals/Content para LK Sneakers

## 1. Tese

O LK Growth OS deve sair da fase de documentação/conectores e entrar em uma cadência prática de melhorias semanais. A premissa principal é comercial:

> O objetivo central é vender mais, converter mais e gerar mais receita para LK, preservando posicionamento premium e atendimento humano.

SEO, GEO, Merchant, PageSpeed, CRO, conteúdo e paid signals não são fins em si. Eles só entram como alavancas quando aumentam:

- tráfego qualificado;
- CTR e captura de demanda;
- conversão de PDP/collection;
- receita por sessão;
- recuperação de demanda gerada por influencer/pago;
- redução de perda por feed/GMC/schema/performance;
- autoridade e visibilidade orgânica/AI no longo prazo.

## 2. Resultado esperado

Criar um sistema semanal de execução Growth com:

1. **uma prioridade comercial por dia**, evitando dispersão;
2. **fila P0/P1/P2** orientada por receita/conversão;
3. **approval packets** para qualquer write;
4. **mudanças pequenas, reversíveis e mensuráveis**;
5. **impact review em aproximadamente 7 dias** para dizer se a melhoria funcionou, foi neutra ou falhou;
6. **aprendizado acumulado** no Brain para melhorar LK, Hermes e o próprio Growth OS.

## 3. Métricas norte

### North Star

- Receita incremental atribuível a melhorias Growth, quando mensurável.

### Métricas primárias

- Taxa de conversão e-commerce.
- Receita por sessão.
- Pedidos por sessão.
- Conversão PDP → carrinho → checkout.
- CTR orgânico GSC em páginas priorizadas.
- Cliques/impressões orgânicas em páginas priorizadas.
- Receita/pedidos de produtos expostos por campanha/influencer.
- Redução de issues GMC que bloqueiam produtos com potencial comercial.

### Métricas secundárias

- PageSpeed/CrUX: LCP, INP, CLS, TTFB.
- Rich results/schema coverage.
- FAQ/blocos citáveis/GEO readiness.
- Reviews/prova social visível.
- Cobertura de conteúdo/cluster para demandas recorrentes.

## 4. Princípios de priorização

### Regra 1 — Receita primeiro

A fila começa por oportunidades com potencial de receita, não por nota técnica isolada.

Priorizar:

1. páginas/produtos com tráfego e baixa conversão;
2. páginas/produtos com receita histórica e queda ou vazamento;
3. campanhas/influencers que geraram demanda mas encontraram gargalo em PDP/collection;
4. GMC issues em produtos com demanda, receita ou exposição;
5. GSC queries com impressões/cliques e CTR/posição melhoráveis;
6. coleções estratégicas com oportunidade de navegação/filtragem/conversão;
7. conteúdos/FAQs que desbloqueiam intenção recorrente ou AI visibility.

### Regra 2 — Diagnóstico público é secundário

HTML, title/meta, schema, PageSpeed e Claude SEO entram depois da priorização comercial. Se faltarem dados de venda, sessão, conversão, GSC ou demanda, o output deve ser `não decision-grade`.

### Regra 3 — Estoque não decide SEO/CRO

Tiny/estoque é contexto operacional, mas não critério decisivo de SEO/CRO. A loja trabalha com curadoria e atendimento humano; não criar taxonomia pública de pronta entrega/encomenda/estoque.

### Regra 4 — Pequeno, reversível, mensurável

Toda melhoria aprovada deve ter:

- snapshot antes;
- mudança exata;
- rollback;
- owner;
- data/hora;
- métrica alvo;
- review D+7.

## 5. Sistema de scoring da fila

Cada oportunidade recebe 0–5 em cada critério:

- **Impacto em receita/conversão:** peso 4.
- **Demanda comprovada:** peso 3.
- **Facilidade de execução:** peso 2.
- **Confiança dos dados:** peso 3.
- **Risco baixo/reversibilidade:** peso 2.
- **Valor estratégico de longo prazo:** peso 2.

Prioridade sugerida:

- P0: score alto, impacto direto em receita/conversão ou bloqueio crítico.
- P1: impacto provável e execução controlada.
- P2: bom para compor longo prazo, mas menor urgência.
- Monitorar: sem dado suficiente ou impacto incerto.

## 6. Cadência semanal por dia

### Segunda — Revenue & Conversion Triage

Objetivo: escolher a fila da semana a partir de dados comerciais.

Fontes:
- Shopify: pedidos, receita, produtos, coleções.
- GA4: sessões, conversão, landing pages, funil.
- GSC: queries/páginas com demanda.
- GMC: issues com impacto comercial.
- Meta/Klaviyo/Paid signals quando houver campanha ativa.

Output:
- top 5 oportunidades P0/P1;
- uma hipótese principal da semana;
- páginas/produtos/campanhas a investigar;
- itens não decision-grade por falta de dado.

Ações permitidas sem aprovação:
- relatório;
- scorecard;
- preview;
- approval packet.

### Terça — PDP/Collection CRO Sprint

Objetivo: transformar oportunidades comerciais em melhoria de conversão.

Foco:
- PDP mobile;
- collection page;
- filtros/ordenação;
- CTA;
- trust blocks;
- reviews/prova social;
- copy de atendimento humano/chat;
- dev-theme previews.

Output:
- 1–3 hipóteses CRO;
- preview visual/dev theme quando aplicável;
- pacote de aprovação separado para qualquer mudança visível.

Guardrail:
- tudo em dev theme/preview antes de produção;
- sem falar publicamente em pronta entrega/encomenda/estoque;
- sem mudança de preço/estoque/desconto.

### Quarta — SEO/GEO/Content Demand Capture

Objetivo: capturar demanda orgânica e AI visibility com base em GSC/SERP.

Foco:
- title/meta de páginas com demanda;
- FAQ e blocos citáveis;
- schema Product/FAQ/Breadcrumb/Article;
- clusters de conteúdo;
- guias/briefs Claude Blog;
- llms.txt e AI Search readiness.

Output:
- approval packets de SEO fields quando houver mudança;
- brief/outline de conteúdo quando a oportunidade for editorial;
- FAQ/schema proposal;
- backlog de conteúdo por impacto comercial.

Guardrail:
- publicar conteúdo ou alterar Shopify/CMS só com aprovação explícita.

### Quinta — GMC/Product Data Quality

Objetivo: reduzir perda de visibilidade e reprovações no Merchant Center.

Foco:
- item issues;
- atributos faltantes;
- GTIN/MPN/brand;
- preço/disponibilidade como consistência de feed;
- ProductInput/supplemental feed apenas com approval packet;
- impacto por produto com demanda.

Output:
- fila de issues agrupada por impacto;
- preview de correção;
- rollback plan;
- review pós-reprocessamento quando aprovado.

Guardrail:
- qualquer feed/ProductInput/fetch que altere estado precisa aprovação atual.

### Sexta — Impact Review & Experiment Ledger

Objetivo: fechar o loop de aprendizado.

Foco:
- revisar mudanças feitas há aproximadamente 7 dias;
- comparar antes/depois;
- classificar impacto;
- decidir manter, iterar, reverter ou escalar;
- atualizar Brain/skills/rotinas.

Output:
- impact review D+7;
- learning ledger;
- próxima hipótese;
- ações que viram padrão.

Classificação:
- `positive`: melhorou métrica alvo;
- `neutral`: sem diferença material;
- `negative`: piorou ou criou risco;
- `inconclusive`: dado insuficiente;
- `needs_more_time`: janela ainda curta.

## 7. Roadmap de 90 dias

### Fase 1 — Primeiras 2 semanas: provar cadência e baseline

Objetivo: executar o sistema manual/read-only + approval packets antes de automatizar mais.

Entregas:
- primeira fila semanal P0/P1 decision-grade;
- primeiro sprint CRO em dev preview;
- primeiro pacote SEO/GEO por demanda GSC;
- primeira revisão GMC por impacto comercial;
- primeiro impact review D+7;
- dashboard simples de oportunidades e decisões no Brain.

Critério de sucesso:
- Lucas consegue decidir toda semana o que aprovar/rejeitar/adiar;
- nenhuma recomendação importante fica sem fonte comercial;
- nenhuma mudança aprovada fica sem review D+7.

### Fase 2 — Semanas 3–6: transformar em máquina de melhoria

Objetivo: repetir, medir e melhorar a precisão.

Entregas:
- cadência semanal estável;
- templates preenchidos sempre no mesmo formato;
- backlog P0/P1/P2 vivo;
- primeiros conteúdos/FAQs/clusters com demanda real;
- primeiros experimentos CRO medidos;
- first-pass de AI/GEO em páginas prioritárias;
- Merchant review com issue categories e impacto estimado.

Critério de sucesso:
- aumento de CTR/conversão em pelo menos parte das páginas testadas;
- queda de issues GMC acionáveis;
- backlog menor e mais qualificado;
- hipóteses ruins descartadas rapidamente.

### Fase 3 — Semanas 7–12: escala controlada

Objetivo: escalar apenas o que provou efeito.

Entregas:
- automações read-only onde fizer sentido;
- filas automáticas de oportunidades com revisão humana;
- playbook de CRO/PDP/collection aprovado;
- playbook de SEO/GEO aprovado;
- playbook de GMC aprovado;
- conteúdo/cluster editorial com cadência comercial;
- integração futura com Mission Control/approval inbox quando pronto.

Critério de sucesso:
- decisões mais rápidas;
- menos retrabalho;
- melhoria acumulada em receita/conversão/CTR;
- Lucas aprova ou rejeita pacotes com clareza.

## 8. Backlog inicial priorizado

### P0 — Começar agora

1. **Weekly Revenue Opportunity Queue**
   - Segunda-feira: ranking de oportunidades por receita/conversão/demanda.
   - Motivo: sem isso, todo SEO/CRO vira opinião.

2. **CRO Preview em páginas com tráfego e baixa conversão**
   - Terça-feira: 1–3 hipóteses visuais em dev preview.
   - Motivo: conversão é alavanca direta de receita.

3. **Impact Review D+7 obrigatório**
   - Sexta-feira: toda mudança aprovada entra na fila de revisão.
   - Motivo: fechar loop e parar de acumular mudança sem saber efeito.

4. **GMC issues por impacto comercial**
   - Quinta-feira: agrupar warnings/reprovações por produto com potencial.
   - Motivo: evitar perda de tráfego Shopping/Free Listings.

### P1 — Próximo bloco

5. **GSC CTR/title/meta queue**
   - Quarta-feira: melhorar páginas com impressão/posição/CTR melhorável.

6. **GEO/FAQ/AI visibility para páginas prioritárias**
   - Quarta-feira: blocos citáveis, FAQ/schema, llms.txt quando aplicável.

7. **Paid/Influencer → PDP/Collection Fit**
   - Segunda ou terça: cruzar campanha/produto com gargalo de conversão.

8. **Review/prova social snippets**
   - Terça: checar impacto de reviews/schema/trust em PDPs priorizadas.

### P2 — Longo prazo

9. **Content clusters comerciais**
   - Guias e artigos só quando houver demanda GSC/SERP/social clara.

10. **PageSpeed/CrUX improvement queue**
   - Priorizar métricas com impacto em páginas comerciais.

11. **Concorrência/SERP/DataForSEO deep dives**
   - Após reload/restart aprovado para DataForSEO MCP ativo.

12. **Google Business/local SEO**
   - Aplicar quando houver hipótese clara para loja/local.

## 9. Ritmo de decisão para Lucas

Toda semana Lucas recebe:

- segunda: fila da semana;
- terça/quarta/quinta: approval packets quando houver ação produtiva;
- sexta: o que funcionou/não funcionou e próxima hipótese.

Formato executivo:

- O que fazer agora.
- Por que isso vende/converte mais.
- Evidência.
- Risco.
- Esforço.
- Aprovação necessária.
- Como desfazer.
- Quando medir.

## 10. O que exige aprovação

Mesmo com PRD aprovado, continuam exigindo aprovação explícita atual:

- Shopify writes: produto, coleção, page, theme, SEO field, descrição, imagem, alt, metafield.
- GMC/feed writes: supplemental feed, Content API, datafeed config, fetch/reprocess quando altera estado.
- GA4/GSC/admin config changes.
- Google/Meta Ads changes.
- Klaviyo, WhatsApp, email, social ou qualquer envio externo.
- preço, estoque, desconto ou checkout.
- produção, deploy ou theme publish.
- runtime/VPS/Docker/restart quando necessário para MCP/DataForSEO.

## 11. O que pode rodar sem aprovação

- leitura/auditoria pública;
- leitura autenticada read-only já autorizada;
- relatórios internos;
- scorecards;
- previews;
- approval packets;
- rollback plans;
- PRD/backlog/rotinas no Brain;
- comparison before/after read-only;
- smoke tests pequenos sem custo relevante e sem mutation, respeitando guardrail DataForSEO.

## 12. Primeira execução recomendada

### Semana 1

- **Segunda:** gerar primeira `Weekly Revenue Opportunity Queue` com Shopify + GA4 + GSC + GMC + paid signals.
- **Terça:** escolher 1 collection/PDP prioritária e preparar CRO preview/dev theme, se necessário.
- **Quarta:** criar pacote SEO/GEO para 3–5 páginas com demanda GSC/CTR.
- **Quinta:** gerar GMC issue queue por impacto comercial e approval packet se houver correção segura.
- **Sexta:** revisar qualquer mudança aprovada anteriormente e registrar D+7; se não houver mudança elegível, revisar baseline e definir próxima hipótese.

### Primeiro output esperado

Um relatório único chamado:

`lk-growth-weekly-revenue-opportunity-YYYY-MM-DD.md`

Ele deve conter:

- top 5 oportunidades;
- fonte de dados;
- score P0/P1/P2;
- ação recomendada;
- approval necessário;
- métrica alvo;
- data de review D+7.

## 13. Riscos

- Otimizar página sem demanda real.
- Executar mudança visível sem aprovação.
- Confundir estoque operacional com prioridade SEO/CRO.
- Rodar DataForSEO/exports pagos sem controle de custo.
- Criar conteúdo sem vínculo com demanda comercial.
- Medir cedo demais ou sem baseline.
- Depender de uma métrica isolada; sempre triangular Shopify/GA4/GSC/GMC quando possível.

## 14. Critério de conclusão deste PRD

Este PRD estará operacional quando:

- a cadência por dia estiver documentada e aceita;
- a primeira fila semanal for gerada;
- pelo menos uma melhoria passar por: hipótese → aprovação → execução → review D+7;
- os aprendizados forem registrados no Brain;
- a próxima semana começar com a fila anterior revisada.
