# PRD v0.1 — LK Operating System no Hermes

Status: aprovado conceitualmente por Lucas em 2026-05-09; documento inicial para implementação faseada.
Escopo desta versão: produto/documentação. Não cria cron, não altera Shopify, Tiny, Klaviyo, Evolution, Notion, Google, Meta, n8n, GitHub, VPS, Docker, banco, campanha ou mensagem externa.

## 1. Razão de existir

A LK existe porque os tênis mais desejados esgotam, somem das lojas oficiais ou nem chegam bem ao Brasil. A LK faz curadoria independente dos pares mais legais, compra no mercado certo e conecta esses produtos aos clientes certos.

A LK não é um retailer oficial que precisa vender qualquer grade enviada por Nike, Adidas ou outras marcas. A vantagem da LK é escolher apenas os tênis mais desejados e difíceis de encontrar, comprando via pessoas, mercado secundário, StockX/KicksDev, fontes Brasil ou canais internacionais quando fizer sentido.

Princípio central:

> A LK não vende catálogo. A LK vende curadoria, acesso, escassez, desejo, confiança e conveniência.

O `LK Operating System` deve operar como um CEO/Chief of Staff da LK: transformar dados, estoque, comportamento, tendências, conteúdo e aprovações em ações comerciais melhores.

## 2. Objetivos v0.1

1. Aumentar conversão online de 0,13% para 0,20%.
   - Baseline: Shopify Analytics.
   - Leitura: prioridade estratégica de CRO, não métrica lateral.
2. Aumentar recompra em 50%.
   - Métricas recomendadas: taxa de recompra em janela móvel de 90 dias, clientes que recompram e receita de clientes recorrentes.
3. Criar o `Stock Intelligence Center` por produto, modelo e tamanho.
4. Reduzir decisões baseadas em estoque errado da Shopify.
5. Acelerar curadoria, pricing, subida de produto, conteúdo e campanha.
6. Separar corretamente comunicação online/Klaviyo de loja física/WhatsApp.
7. Medir performance de marca, produto, tamanho, canal, influenciador e campanha ao longo do tempo.
8. Criar um loop de aprendizado/aprovação para que correções de Lucas virem regras futuras.

## 3. North Star operacional

> Fazer a melhor curadoria independente de sneakers desejados no Brasil, conectando produtos difíceis de encontrar aos clientes certos, com inteligência de estoque, dados, conteúdo, preço, relacionamento e aprovação humana.

## 4. Princípios de operação

- Dados antes de afirmação.
- Produto/modelo/tamanho antes de decisão genérica por produto.
- Shopify é fonte de vendas/clientes/source/catálogo; Tiny é fonte oficial de estoque.
- SKU canônico para matching operacional é o SKU da Shopify. O sistema pode sugerir padronizar/corrigir o SKU no Tiny para refletir Shopify, mas não deve alterar SKU Shopify sem aprovação explícita, porque isso pode quebrar histórico, catálogo, integrações e operação.
- Estoque disponível não é igual a estoque físico: encomenda, reserva e produto já vendido precisam ser separados.
- O sistema deve sugerir, preparar e criar previews; humano aprova envio, publicação, compra, alteração de preço, alteração de tema ou ação externa.
- Conteúdo deve nascer de sinal real: venda, tendência, busca, estoque, campanha, influenciador, restock ou oportunidade de curadoria.
- DesignMD da LK é base obrigatória para conteúdo e briefing visual.
- Toda sugestão deve explicar: o que vi, por que importa, o que recomendo, confiança, risco e aprovação necessária.
- O agente pode dizer “não recomendo ação hoje”. Não inventar trabalho para parecer útil.

## 5. Fontes da verdade e integrações

### Fontes principais

- Shopify: vendas, clientes, source/canal, pedidos, catálogo/vitrine, tags de pedido quando disponíveis.
- Tiny / depósito `LK | CONTROLE ESTOQUE`: fonte oficial de estoque operacional.
- Notion LK: `LK Compras`, `LK Encomendas` e estruturas relacionadas de compra/encomenda.
- Klaviyo: comunicação online escalável.
- Evolution API: WhatsApp da LK, loja física e mensagens 1:1/personalizadas.
- Google Analytics / Shopify Analytics: tráfego, funil, conversão e comportamento.
- Google Search Console: busca orgânica e SEO.
- Google Merchant Center: feed, disponibilidade, reprovações e Google Shopping.
- Meta Ads / Google Ads: mídia paga e campanhas.
- KicksDev: dados estruturados de mercado sneaker quando StockX/GOAT/Flight Club bloqueiam scraping direto.
- Droper.app: checagem de disponibilidade/preço Brasil.
- n8n: orquestração de automações aprovadas.
- SQLite local: espelho operacional/analítico inicial.
- GitHub: versionamento, documentação, PRs, tema/código quando aplicável.
- DesignMD LK: regra visual e de produção de conteúdo.

### Integrações a mapear

- Wile ERP: citado como relevante, mas Tiny foi definido como fonte correta de estoque. Wile deve ser tratado como integração a mapear antes de virar fonte oficial.
- `LCWATSAP`: repositório citado como fonte da skill/guia de subida de produto.
- Skill `Cloudcio`: referência futura quando Lucas enviar o link.

## 6. Modelo de dados local

Começar com SQLite local como espelho operacional e analítico. DuckDB pode entrar depois para análise pesada. Postgres local só se houver necessidade real de app/API multiusuário.

O modelo precisa ser no nível de variante/tamanho.

Entidades mínimas:

- produtos;
- variantes/tamanhos;
- estoque Tiny;
- status comercial da variante;
- pedidos Shopify;
- clientes Shopify;
- source/canal;
- campanhas/UTMs;
- influenciadores;
- mapa de SKU Shopify ↔ Tiny, com Shopify como chave canônica e aliases Tiny quando existirem;
- preço atual;
- histórico de preço;
- histórico de estoque;
- histórico de vendas;
- recomendações;
- aprovações;
- eventos.

### Estados comerciais por variante/tamanho

- `disponivel`: estoque livre para venda.
- `reservado`: estoque físico comprometido.
- `sob_encomenda_br`: compra/encomenda via Brasil; classificação humana.
- `sob_encomenda_us`: compra/encomenda via fora; classificação humana.
- `em_transito`: comprado/importado, ainda não chegou.
- `recebido_ja_vendido`: entrou fisicamente mas não deve acionar campanha.
- `recebido_livre`: entrou e pode virar oportunidade.
- `divergente`: Tiny, Shopify, pedido ou Notion não batem.

Regra:

> Nenhuma comunicação externa deve ser sugerida apenas porque o produto entrou no estoque. Primeiro é obrigatório confirmar status livre por variante/tamanho.

Regra de encomenda:

> `encomenda BR` e `encomenda US` são curadoria humana da LK e aparecem no contexto do pedido Shopify quando a equipe marca. O sistema pode sugerir candidatos, mas não deve deduzir automaticamente por tag de produto, nome do produto ou ausência de estoque. A mesma página/produto pode ter tamanho pronta entrega e outro tamanho sob encomenda.

Regra de SKU:

> Para relatórios e matching, Shopify é a chave canônica de SKU porque é onde venda, pedido, produto e variante acontecem. O Tiny continua sendo a fonte oficial de estoque, mas o ideal operacional é o Tiny espelhar o SKU Shopify. Quando houver divergência, o sistema deve primeiro aprender/mapear `SKU Shopify → produto Tiny/alias Tiny`, marcar confiança e só sugerir alteração no Tiny mediante preview; nunca mudar SKU Shopify automaticamente.

## 7. Estrutura de módulos

```text
LK Operating System
├── LK Chief of Staff
├── Daily Sales Brief
├── Pulso Comercial
├── Stock Intelligence Center
├── Brand Mix Intelligence
├── Conversion Rate Optimization
├── Pricing Intelligence
├── Supply & Sourcing
├── Shopify Operations
├── SEO & Google / SEO-CRO Weekly Improvement
├── Google Merchant Center
├── Paid Traffic & Influencer Intelligence
├── CRM & RFM
├── Physical Store Intelligence
├── Content & Campaign Production Engine
├── Data & Integration Layer
├── Approval Manager
└── Hermes Learning Loop
```

## 8. LK Chief of Staff

Papel: CEO operacional da LK no Hermes.

Responsabilidades:

- ler dados e contexto;
- priorizar problemas;
- detectar padrões;
- sugerir ações;
- preparar rascunhos;
- pedir aprovação;
- registrar aprendizado;
- melhorar rotinas.

Submódulos devem começar como skills/rotinas, não agentes permanentes. Essa decisão segue a lógica Amora/Bruno adaptada ao Hermes: um Chief of Staff forte, contextualizado e com skills claras antes de criar muitos agentes especialistas.

## 9. Daily Sales Brief — 07h

Cadência-alvo: todo dia às 07h, analisando o dia anterior fechado.

Escopo v0.1: especificação. Cron real só após aprovação de implementação.

Fontes:

- Vendas/clientes/source: Shopify.
- Estoque: Tiny / depósito `LK | CONTROLE ESTOQUE`.
- Tráfego/conversão: Google Analytics + Shopify Analytics.
- Comunicação online: Klaviyo.
- WhatsApp: Evolution API.
- Pedidos de compra/encomenda: Notion LK.

Estrutura:

1. Resumo executivo.
2. Vendas Shopify.
3. Online vs loja física.
4. Google Analytics / CRO.
5. Produtos vendidos.
6. Tamanhos vendidos.
7. Estoque Tiny e status comercial.
8. Encomendas/importações comprometidas.
9. Alertas de recompra.
10. Pricing signals.
11. Ideias do LK CEO.
12. Aprovações pendentes.

Regra de privacidade: por padrão não expor dados pessoais completos de cliente no Telegram. Usar segmentos, IDs internos ou dados mascarados quando possível.

## 10. Pulso Comercial — 16h

Nome correto: `Pulso Comercial LK`, não “pulso financeiro”.

Objetivo:

> Detectar sinais do dia em andamento e preparar ações comerciais inteligentes, sem fingir que é possível “salvar o dia” com promoção de última hora.

Escopo:

- restocks relevantes;
- vendas que geram recompra;
- estoque crítico;
- produto/tamanho com oportunidade;
- cliente elegível para WhatsApp/Klaviyo;
- alerta para `LK.Sneakers | Compras`;
- ações a preparar.

Regra anti-spam: se não houver sinal acionável, o sistema pode registrar internamente “sem ação relevante” e não deve forçar alerta ruidoso.

## 11. Stock Intelligence Center

Pilar central da LK OS.

Perguntas que responde:

- O que está vendendo?
- O que vai acabar?
- Quantos dias de cobertura existem?
- Quanto tempo demora para repor?
- Vale comprar agora?
- Está caro demais?
- Existe fonte Brasil ou fora?
- Deve acionar WhatsApp de compras?
- Deve virar item em `LK Compras` ou `LK Encomendas`?

Fórmula conceitual:

```text
dias_de_cobertura = estoque_livre / velocidade_de_venda
risco_ruptura = dias_de_cobertura <= lead_time_reposicao
```

Lead times v0.1:

- Brasil: 3–7 dias.
- Fora/US: aproximadamente 30 dias.
- StockX/internacional: aproximadamente 30 dias.
- Pessoa/revendedor Brasil: variável; confirmar manualmente.

### Alerta de recompra/reposição

Fluxo:

```text
Venda detectada no Shopify
→ consultar Tiny por produto/modelo/tamanho
→ avaliar estoque livre, velocidade de venda e lead time
→ se houver sinal, preparar alerta no WhatsApp `LK.Sneakers | Compras`
→ humano aprova/rejeita
→ se aprovado, criar item no Notion LK (`LK Compras` ou `LK Encomendas` conforme caso)
```

Canal: WhatsApp via Evolution API.

Regra: compra automática é bloqueada. O sistema pode sugerir e preparar; humano decide. Compra para estoque deve ser descrita como **repor estoque**, não como “replicar estoque”.

Exemplo de uso correto de busca externa:

```text
Shopify mostra que um New Balance específico/tamanho vendeu bem.
Tiny `LK | CONTROLE ESTOQUE` mostra estoque zerado ou baixo.
O sistema checa apenas fontes plausíveis para aquele item e encontra restock em uma loja/fonte relevante.
Saída: “teve restock deste produto que a LK vende bem e está zerado; vale avaliar compra?”.
```

Esse é o uso legítimo de varejistas e fontes externas na v0.1: busca acionada por sinal interno, não monitoramento amplo contínuo.

## 12. Supply & Sourcing

Uso correto: não monitorar retailers continuamente por curiosidade. Procurar fontes quando houver sinal interno de demanda, ruptura ou oportunidade.

Fontes conhecidas:

- Droper.app;
- StockX/KicksDev;
- GOAT/Flight Club via KicksDev, se aplicável;
- Guadalupe;
- Your ID;
- Artwalk;
- Virus 41;
- New School;
- Adidas direto;
- Monbam, rede/grupo de revendedores citada por Lucas;
- pessoas/revendedores;
- grupo WhatsApp `LK.Sneakers | Compras`.

Score de sourcing recomendado:

- preço final viável, não apenas preço de vitrine;
- prazo;
- confiabilidade;
- risco;
- disponibilidade por tamanho;
- histórico de compra;
- compatibilidade com curadoria LK.

Regra Lucas 2026-05-11 para sourcing futuro/pending:

- Antes de cotação real/contato externo, comparar Droper, StockX e GOAT por produto+tamanho.
- Retornar sempre a fonte mais barata viável.
- StockX/GOAT geralmente usam tamanho americano; identificar se é US Men ou US Women e converter corretamente para o tamanho LK/BR/EU antes de comparar.
- Para StockX/GOAT, custo final estimado deve usar a fórmula LK de importação da seção Pricing Intelligence.

Fluxo Brasil v0.1:

```text
produto/tamanho vendido ou em risco
→ checar Droper e fontes Brasil relevantes
→ se fizer sentido, preparar mensagem para o grupo de compras/revendedores
→ humano aprova antes de postar, negociar ou comprar
```

## 13. Pricing Intelligence

### Fórmula de preço internacional v0.1

```text
preco_base =
(preco_usd + custo_trazer_usd)
× (dolar_atual × 1,05)
× 2
```

Exemplo validado:

```text
(US$100 + US$100) × (R$5,00 × 1,05) × 2 = R$2.100
```

O `custo_trazer_usd` pode começar como US$100 padrão configurável, mas não deve ser hardcoded permanentemente. No futuro, variar por origem, produto, frete, peso e risco.

### Arredondamento LK

Aplicar preço psicológico, evitando preços redondos.

Finais preferidos:

- `49,99`;
- `99,99`.

Regra v0.1:

- arredondar para o final psicológico mais próximo;
- se arredondar para baixo prejudicar margem relevante, sugerir o próximo final para cima;
- preço final é sugestão e exige aprovação antes de aplicação.

### Aumento de preço

Sugerir aumento quando:

- produto vendeu recentemente;
- estoque livre é baixo;
- reposição ficou cara em StockX/KicksDev/fonte;
- demanda interna existe;
- produto é difícil de encontrar;
- conversão do produto não está ruim.

Não sugerir aumento quando:

- produto está parado;
- PDP tem tráfego sem conversão;
- preço já parece travar conversão;
- estoque é alto e velho;
- objetivo é giro de capital.

## 14. Brand Mix Intelligence

Objetivo: medir share e momentum das marcas ao longo do tempo.

Hipótese atual de marcas importantes:

1. Onitsuka;
2. New Balance;
3. Adidas;
4. Nike.

O sistema não deve congelar essa ordem. Deve medir:

- share por receita;
- share por unidades;
- share por pedidos;
- share por canal;
- share por influenciador/campanha;
- mudança mês a mês;
- relação com estoque disponível;
- relação com produtos específicos.

Perguntas:

- Onitsuka caiu por falta de estoque ou queda de demanda?
- Nike subiu por Vomero ou por outro produto?
- New Balance cresce em quais tamanhos?
- Adidas vende por marca ou por modelos específicos?

## 15. CRO — Conversion Rate Optimization

Baseline: conversão online 0,13% segundo Shopify Analytics.
Meta v0.1: 0,20%.

O CRO deve separar causas possíveis:

- tráfego ruim;
- produto errado;
- preço desalinhado;
- estoque/confusão de disponibilidade;
- PDP fraca;
- checkout;
- falta de confiança;
- mobile;
- campanha/influenciador inadequado.

Blocos de análise:

- sessões;
- usuários;
- source/canal;
- conversão por canal;
- product view;
- add to cart;
- checkout;
- purchase;
- produtos com tráfego alto e baixa venda;
- produtos com add-to-cart e baixa compra;
- páginas com queda;
- hipóteses de teste.

## 16. CRM, RFM e recompra

Prioridades iniciais:

- pós-compra;
- recompra;
- clientes dormentes;
- carrinho abandonado;
- segmentação por tamanho/marca/modelo;
- online via Klaviyo;
- loja física via WhatsApp/Evolution.

A recompra da LK não é só vender o mesmo tênis. O objetivo é transformar um comprador pontual em cliente recorrente, vendendo outro tênis certo depois.

Modelo recomendado:

```text
RFM
+ tamanho
+ marca
+ modelo
+ canal
+ compra online/física
+ pronta entrega/encomenda
+ sensibilidade a preço
+ influencer/campanha de origem
```

## 17. Online vs loja física

### Online

Canal principal: Klaviyo.

Uso:

- campanhas segmentadas;
- newsletter;
- carrinho abandonado;
- pós-compra;
- recompra;
- clientes online;
- fluxos automatizados aprovados.

### Loja física

Canal principal: Evolution API / WhatsApp LK.

Uso:

- atendimento personalizado;
- relacionamento 1:1;
- cliente que comprou presencialmente;
- oportunidades por tamanho/marca/modelo;
- mensagens pós-compra existentes a auditar.

Regra:

> Cliente de loja física deve receber relacionamento mais próximo. Nem toda oportunidade deve virar Klaviyo.

## 18. Paid Traffic & Influencer Intelligence

A LK usa Google Ads, Meta Ads e influenciadores. O sistema precisa medir produto/influenciador/campanha e consequência de estoque.

Fontes iniciais:

- UTM;
- campanha Meta;
- campanha Google;
- talvez cupom.

Fonte de custo v0.1 validada:

- Google Ads: Metricool API, brand correta da LK.
- Meta Ads: Meta Marketing API direta enquanto Metricool aponta para conta Meta antiga.
- Shopify: confirmação operacional de pedido, produto, receita e source.
- GA4: sessões, landing pages, source/medium/campaign e contexto de funil.

Perguntas:

- Qual influenciador gerou resultado?
- Qual produto performou com qual influenciador?
- Qual tipo de produto, marca, modelo, faixa de preço e tamanho cada influenciador tende a mover?
- Qual canal trouxe tráfego sem conversão?
- Qual marca/modelo combina com cada público?
- Qual criativo/campanha justifica repetir?
- A campanha vendeu estoque livre ou gerou ruptura/encomenda?

Recomendação de governança:

```text
utm_source
utm_medium
utm_campaign
utm_content
utm_term
influencer_id/opcional
produto_modelo/opcional
```

Sem UTM/cupom consistente, o módulo começa como auditoria e não como julgamento definitivo.

Regra: ROAS de plataforma é sinal, não verdade final. A leitura executiva deve reconciliar custo pago com receita Shopify web e, quando possível, produto/tamanho vendido. O objetivo não é premiar o maior ROAS isolado, mas descobrir qual influenciador/campanha combina com qual curadoria e qual impacto causa no estoque.

### Campaign Attribution Dictionary

O módulo precisa manter um dicionário canônico entre mídia paga, Shopify/GA4 e curadoria:

```text
campaign_name Meta / adset_name / ad_name
→ campaign/ad group Google quando houver
→ utm_campaign Shopify/GA4
→ cupom/landing/referrer quando houver
→ influencer/criativo
→ produto/marca/modelo/SKU/tamanho esperado
→ custo compatível
→ receita Shopify compatível
→ consequência de estoque
```

Sem esse dicionário, `Meta attributed ROAS by campaign title` deve ser tratado apenas como sinal de plataforma. Matching frouxo por texto não deve ser usado para decisão operacional, porque campanhas genéricas podem capturar UTMs de campanhas/influencers diferentes.

O dicionário deve começar por Lala Noleto, Silvia Heinz, Helena Lunardelli e as campanhas broad/Advantage+/RMKT com maior gasto, sempre separando:

- ROAS atribuído pela plataforma;
- receita Shopify com evidência de UTM/cupom/landing/produto;
- ROAS operacional quando custo e receita forem compatíveis;
- impacto em estoque Tiny `LK | CONTROLE ESTOQUE` por SKU/tamanho.

## 19. Content & Campaign Production Engine

Função:

> Transformar sinais de venda, estoque, tendência, SEO, CRM, mídia, influenciador e curadoria em peças de conteúdo e campanhas prontas para aprovação.

Saídas possíveis:

- carrossel Instagram;
- post estático;
- roteiro Reels;
- legenda;
- newsletter;
- WhatsApp;
- Klaviyo;
- blog post Shopify;
- PDP copy;
- HTML de produto / PDP Shopify;
- SEO title/meta;
- briefing visual;
- CTA;
- fluxo de automação.

### DesignMD obrigatório

Todo conteúdo deve consultar o DesignMD da LK antes de gerar estrutura, tom, CTA, hierarquia visual e briefing.

Fluxo:

```text
sinal/oportunidade
→ consultar DesignMD LK
→ escolher formato
→ gerar copy + estrutura + CTA + briefing visual
→ quando for produto/PDP: gerar também HTML pronto para Shopify
→ enviar preview para aprovação
```

### HTML de produto / PDP Shopify

Quando a oportunidade envolve criação ou melhoria de produto, o `Content & Campaign Production Engine` deve gerar não só copy solta, mas também um bloco de HTML pronto para colar/adaptar no Shopify.

O HTML deve seguir DesignMD LK e incluir, quando aplicável:

- bloco de curadoria/por que o produto importa;
- detalhes do produto;
- disponibilidade por tamanho/variante;
- indicação de pronta entrega aparente, encomenda BR, encomenda US ou status a confirmar;
- bloco de atendimento/compra com curadoria LK;
- CTA;
- campos auxiliares: SEO title, meta description, handle, tags, coleções, alt text, FAQ e texto curto para card.

Regra crítica:

> Nenhum HTML de produto deve prometer pronta entrega sem validar Tiny e status comercial por tamanho. O HTML pode ser preparado como draft, mas publicação/alteração Shopify exige aprovação explícita.

### Memória de conteúdo

Registrar:

- o que foi produzido;
- para qual produto/campanha;
- canal;
- aprovação/correção;
- resultado;
- aprendizado.

## 20. Trend-to-Product-to-Blog

Fluxo:

```text
produto bombando lá fora
→ validar fit com curadoria LK
→ checar se LK já tem disponível/sob encomenda
→ se não tiver, checar StockX/KicksDev/Droper/fontes
→ calcular preço LK
→ criar draft de produto Shopify se aprovado
→ criar blog post Shopify
→ blog aponta para link de compra LK
→ preparar distribuição: newsletter, WhatsApp, Instagram, Klaviyo
```

Regra:

> Blog sem produto/link comprável desperdiça tráfego. Quando possível, tendência deve virar produto + blog + distribuição.

Blog Shopify não deve ser notícia genérica. Deve incluir:

- contexto;
- por que importa;
- fit com curadoria LK;
- disponibilidade;
- link de produto;
- CTA;
- SEO;
- interlinking.

## 21. Shopify Operations

Escopo:

- subir produtos;
- criar drafts;
- atualizar produto;
- organizar coleções;
- ordenar coleções;
- revisar tags;
- revisar imagens;
- revisar SEO;
- revisar PDP;
- alterar tema Shopify;
- GitHub/PRs quando aplicável;
- usar skill/guia de subida de produto do repositório `LCWATSAP`.

### Tema Shopify

Alteração de tema é ação sensível. Exige diff/preview/PR/aprovação. Nunca alterar tema publicado sem aprovação explícita.

### Ordenador de coleção v0.1

Regra inicial:

1. primeiros 8 produtos: últimos lançamentos dos últimos 90 dias;
2. depois: best sellers.

Exceções futuras:

- produto sem estoque livre não deve subir ranking;
- produto só encomenda deve ser marcado;
- produto estratégico pode furar regra com aprovação;
- produto com alta conversão pode subir.

## 22. SEO, Google e GMC

### SEO

Começar por auditoria e diagnóstico, não por post aleatório.

Frentes:

- Search Console;
- páginas de produto;
- páginas de coleção;
- blog Shopify;
- páginas de marca/modelo;
- conteúdo evergreen;
- title/meta;
- schema quando fizer sentido;
- links internos.

### GMC / Google Merchant Center

Separar de SEO. GMC cuida de feed e Google Shopping:

- produtos reprovados;
- feed;
- GTIN/MPN quando houver;
- títulos;
- imagens;
- disponibilidade;
- preço;
- divergência Shopify/Tiny;
- performance Shopping/Google Ads.

## 23. Cadência operacional alvo

Escopo desta versão: cadência-alvo. Crons reais exigem implementação e aprovação de escopo.

```text
Diário 07h — Daily Sales Brief
Diário 16h — Pulso Comercial

Segunda 09h — SEO/CRO Audit
Segunda 14h — Stock Intelligence Review

Terça 10h — Newsletter Oportunidades #1
Terça 15h — Content Batch #1

Quarta 09h — Trend-to-Blog / SEO Opportunities
Quarta 15h — CRM/RFM Review

Quinta 09h — GMC Review
Quinta 15h — Paid Traffic & Influencer Review

Sexta 10h — Newsletter Oportunidades #2
Sexta 15h — Shopify Operations Review

Sábado 10h — Weekly CEO Review
```

### Implantação recomendada

Fase 1:

- PRD;
- Daily Sales Brief template;
- Weekly CEO Review template;
- Stock Intelligence template.

Fase 2:

- Daily Sales Brief;
- Newsletter oportunidades terça/sexta;
- Weekly CEO Review.

Fase 3:

- Pulso Comercial;
- Stock Intelligence;
- SEO/GMC;
- Paid/Influencer;
- Content Batch.

Fase 4:

- automações com escrita/aprovação: Notion, WhatsApp, Klaviyo, Shopify draft, GitHub PR, blog Shopify.

## 24. Approval Manager

### Livre sem aprovação externa

- analisar;
- gerar relatório;
- sugerir;
- criar rascunho local;
- preparar copy;
- preparar blog draft;
- preparar produto draft;
- preparar briefing visual;
- gerar preview.

### Exige aprovação

- enviar WhatsApp a cliente;
- disparar Klaviyo;
- publicar blog;
- publicar produto Shopify;
- alterar preço;
- alterar estoque;
- alterar tema;
- criar item operacional no Notion quando virar compra/encomenda real;
- mandar mensagem no grupo de compras;
- contatar fornecedor;
- publicar Instagram;
- alterar campanha Meta/Google;
- qualquer ação externa.

### Bloqueado sem plano explícito

- compra automática;
- deploy/tema publicado;
- envio em massa;
- alteração destrutiva;
- mudança de secrets/infra/banco;
- mutação não aprovada em produção.

## 25. Hermes Learning Loop

Este módulo é global ao Hermes Brain, não exclusivo da LK. A LK OS deve usá-lo para aprender com aprovações, rejeições e correções de Lucas.

Problema que resolve:

```text
Hermes sugere → Lucas corrige → Hermes melhora naquela resposta → próxima semana esquece.
```

Comportamento correto:

```text
Hermes sugere → Lucas aprova/corrige → Hermes registra aprendizado → atualiza PRD/skill/rotina/memória/documento → próxima execução já nasce melhor.
```

Tipos de registro:

- aprovação;
- correção;
- rejeição;
- padrão aprovado;
- anti-padrão;
- decisão permanente;
- melhoria de skill;
- pendência futura.

Campos recomendados:

```text
Feedback ID:
Data:
Área:
Artefato:
Tipo:
Resumo:
Antes:
Depois:
Regra aprendida:
Onde aplicar:
Precisa atualizar skill?
Precisa atualizar PRD?
Status:
```

Regra:

> Se Lucas corrigiu algo que vai se repetir, não basta responder “ok”. É preciso registrar no Brain, skill, PRD ou memória conforme o caso.

## 26. Data Quality Layer

Antes de recomendações comerciais, checar:

- pedido Shopify existe;
- source/canal identificado;
- cliente identificado ou tratado como anônimo;
- variante/tamanho identificado;
- produto mapeado;
- estoque Tiny consultado;
- status comercial conhecido ou marcado como incerto;
- UTM/campanha presente quando usado para atribuição;
- preço atual conhecido;
- dado de margem não confiável marcado como não confiável.

Margem: não usar como base de decisão v0.1 porque preço de compra no Tiny está defasado.

## 27. Learning Loop de recomendações

Cada recomendação importante deve registrar:

```text
recomendação
→ aprovada/rejeitada/ajustada
→ executada/não executada
→ resultado
→ lição
→ próxima recomendação melhor
```

Toda sugestão deve ter:

- confiança: alta/média/baixa;
- motivo;
- dados faltantes;
- risco;
- aprovação necessária.

## 28. O que fica fora do escopo v0.1

- Criar todos os crons automaticamente.
- Enviar mensagens reais.
- Publicar produto/blog/post.
- Alterar preço/estoque/tema.
- Comprar produto automaticamente.
- Criar integrações de escrita sem approval flow.
- Migrar para Postgres local.
- Construir Mission Control visual.
- Fazer scraping proibido de StockX/GOAT/Flight Club.
- Assumir margem confiável antes de saneamento de custo no Tiny.

## 29. Descobertas pendentes

- Confirmar como Shopify marca online vs loja física e se marca importação/encomenda.
- Confirmar em qual estrutura exata do Shopify ficam tags de encomenda no pedido.
- Mapear campos/databases do Notion `LK Compras`, `LK Encomendas` e `LK Stock`.
- Mapear status de Tiny para reservado, em trânsito, comprometido e estoque livre.
- Verificar papel real do Wile ERP.
- Localizar e adaptar a skill/guia de subida de produto no repositório `LCWATSAP`.
- Receber link da skill `Cloudcio`.
- Auditar UTMs/campanhas/cupom de influenciadores.
- Confirmar custo padrão de trazer produto por origem.
- Definir modelo de dados inicial SQLite.

## 30. Alinhamento Bruno/OpenClaw

Este PRD está alinhado com a aula/lógica Bruno/OpenClaw nos pontos relevantes:

- começa com um Chief of Staff forte em vez de criar agentes demais cedo;
- transforma subáreas em skills/rotinas antes de agentes permanentes;
- separa cérebro/documentação de execução;
- define permissões e approval flow antes de automações externas;
- cria rotinas/cadências business-readable;
- preserva aprendizado por feedback;
- adapta o case Amora para Hermes/LK sem copiar arquitetura cegamente.

Adaptação Hermes-native:

- Brain GitHub como fonte durável;
- Doppler para secrets;
- Telegram/WhatsApp como interfaces operacionais;
- ferramentas reais via Hermes;
- PRs pequenos e verificáveis;
- nenhuma ação externa sem preview/aprovação.
