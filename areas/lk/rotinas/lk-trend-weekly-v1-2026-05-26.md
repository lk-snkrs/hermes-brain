# LK Trend Weekly v1 — relatório semanal + fila de oportunidades

Status: aprovado por Lucas para preparar v1 read-only, sem writes.
Data: 2026-05-26.
Escopo: LK Sneakers / inteligência operacional.

## Objetivo

Criar uma rotina semanal que transforme sinais de mercado, demanda interna e estado de estoque/catálogo em uma fila priorizada de oportunidades para a LK, sem executar compras, contatos, campanhas ou alterações em Shopify/Tiny.

A v1 serve para responder:

- quais tendências parecem relevantes para a LK nesta semana;
- quais oportunidades são de **conteúdo**;
- quais oportunidades são de **compra/reposição**;
- quais oportunidades precisam de validação adicional;
- quais podem virar, numa etapa posterior, previews de Shopify/catálogo/campanha.

## Regra central

A v1 é relatório e fila. Não é executor.

Permitido:

- leitura read-only de fontes;
- resolução local de produto/SKU/tamanho;
- score e priorização;
- rascunho interno de próximos passos;
- preview de decisão para Lucas/Júlio/Renan.

Bloqueado sem nova aprovação explícita:

- criar/editar produto no Shopify;
- alterar preço, estoque, SKU, tag, collection, theme ou Merchant Center;
- comprar produto, reservar, negociar ou contatar fornecedor;
- enviar campanha, WhatsApp, email ou Klaviyo;
- prometer disponibilidade/preço ao cliente.

## Separação obrigatória: conteúdo vs compra

Cada oportunidade deve entrar em uma única categoria primária:

1. **Oportunidade de conteúdo**
   - Objetivo: gerar tráfego, desejo, prova social, SEO/GEO, CRM ou campanha futura.
   - Pode nascer de hype, procura orgânica, tendência social, produto com estoque saudável, produto parado com storytelling forte, ou gap de conteúdo.
   - Não implica compra.

2. **Oportunidade de compra/reposição**
   - Objetivo: avaliar reposição/sourcing de um produto/tamanho específico.
   - Só deve avançar quando houver demanda interna ou ruptura/baixo estoque validado em Tiny no depósito `LK | CONTROLE ESTOQUE`.
   - Não implica contato com fornecedor nem compra automática.

3. **Oportunidade de catálogo/Shopify preview futuro**
   - Objetivo: depois que o formato do relatório estiver bom, transformar melhores oportunidades em previews de produto/SEO/copy/collection.
   - Só nasce da fila v1 aprovada; não cria produto duplicado.

Se uma tendência tiver potencial de conteúdo e compra, registrar uma como primária e a outra como ação secundária, com justificativa.

## Fontes e hierarquia

### Fontes internas

- Shopify: catálogo, pedidos, produtos, variantes, tags, imagens e preço atual.
- Tiny: estoque oficial, sempre no depósito `LK | CONTROLE ESTOQUE`.
- GA4/GSC/Metricool/Meta/Klaviyo: sinais de interesse, tráfego, busca e engajamento.
- WhatsApp/Telegram/atendimento: pedidos e sinais qualitativos, sem prometer nada ao cliente.

### Fontes externas

- Droper: primeira checagem BR quando a oportunidade for compra/reposição.
- StockX/GOAT/KicksDev: referência internacional quando Droper não resolve ou quando for sinal de mercado.
- Web/social/influenciadores: evidência de tendência, sempre rotulada como sinal e não como fato de venda LK.

## Filtros anti-erro

Antes de qualquer item virar oportunidade acionável:

1. Checar se já existe no Shopify, por SKU, handle, título/modelo e variações.
2. Checar Tiny para estoque e SKU/tamanho, usando resolver local e dedupe quando aplicável.
3. Confirmar tamanho/variante; não tratar produto genérico como compra específica.
4. Separar sinal externo de demanda interna.
5. Evitar duplicidade de produto no Shopify.
6. Evitar confundir “tem hype” com “vale comprar”.

## Score v1

Pontuação total: 100.

- Demanda interna LK: 0–25
  - vendas recentes, pedidos, atendimento, CRM, busca interna, recorrência.
- Sinal externo/tendência: 0–20
  - hype, social, influenciador, mercado, lançamento, movimento de preço.
- Fit com LK: 0–20
  - curadoria, marca/modelo compatível, margem provável, público, histórico.
- Estado comercial: 0–20
  - estoque Tiny, cobertura, ruptura, catálogo existente, preço atual.
- Evidência e confiança: 0–15
  - fontes verificadas, SKU/tamanho resolvido, baixa ambiguidade.

Classificação:

- 80–100: P1 — forte, preparar próximo preview/decisão.
- 60–79: P2 — observar ou validar fonte antes de execução.
- 40–59: P3 — manter na watchlist.
- <40: descartar ou arquivar como sinal fraco.

## Campos da fila de oportunidades

Cada linha deve conter:

```text
ID:
Categoria primária: conteúdo / compra-reposição / catálogo-preview-futuro / watchlist
Produto/modelo:
Marca:
Cor/colorway:
Tamanho/variante, se aplicável:
SKU Shopify, se existir:
Tiny código/depósito/estoque, se aplicável:
Shopify status: existe / não existe / ambíguo / duplicidade possível
Sinal principal:
Fontes consultadas:
Score total:
Prioridade: P1/P2/P3/descartar
Confiança: alta/média/baixa
Risco:
Próxima ação segura:
Aprovação necessária:
Dono sugerido: Lucas / Júlio / Renan / Hermes
```

## Formato do relatório semanal

1. **Resumo executivo**
   - 3 a 5 bullets: o que mudou, onde há oportunidade, onde não agir.

2. **Top oportunidades P1**
   - máximo 5 itens;
   - cada item com categoria, score, evidência, risco e próxima ação segura.

3. **Fila de conteúdo**
   - oportunidades para SEO, blog, Reels, newsletter, PDP/storytelling, CRM.
   - não misturar com compra.

4. **Fila de compra/reposição**
   - somente produtos/tamanhos com demanda/ruptura/baixo estoque verificados.
   - incluir Droper primeiro quando for etapa de sourcing.

5. **Watchlist**
   - sinais promissores, mas ainda fracos.

6. **Bloqueios/dados faltantes**
   - SKU/tamanho ambíguo;
   - Tiny sem código;
   - Shopify duplicidade possível;
   - fonte externa fraca;
   - margem/lead time desconhecido.

7. **Próxima decisão**
   - uma decisão por vez para Telegram.
   - exemplo: “Aprovar transformar os 3 P1 de conteúdo em previews de pauta/copy?”

## Evolução para v2

Só depois que Lucas aprovar que o formato semanal ficou bom:

- converter P1 conteúdo em preview de blog/source page/newsletter/CRM;
- converter P1 catálogo em preview Shopify, com checagem anti-duplicidade;
- converter P1 compra em pacote Júlio/Notion, após validação de Droper/StockX/GOAT;
- criar automação recorrente se a v1 tiver baixa taxa de ruído.

## Rollback / contenção

Como a v1 não faz writes:

- se o relatório vier ruim, ajustar score/template;
- se a fila vier ampla demais, limitar top 5;
- se a evidência vier fraca, exigir fonte por oportunidade;
- se misturar execução com análise, separar em duas saídas:
  1. relatório sem execução;
  2. pacote de aprovação para a próxima ação.

## Critério de pronto da v1

- Template criado.
- Fila com campos padronizados.
- Guardrails de aprovação explícitos.
- Conteúdo e compra separados.
- Anti-duplicidade Shopify/Tiny obrigatório.
- Próxima etapa definida como preview, não write.
