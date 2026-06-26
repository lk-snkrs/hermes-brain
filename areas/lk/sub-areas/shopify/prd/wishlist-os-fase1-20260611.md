# Wishlist OS — Fase 1

Data: 2026-06-11
Owner operacional: LK Shopify para superfície Shopify/SWYM e QA; LK Growth/Content para CRM/Klaviyo quando houver campanha; LK Stock para qualquer promessa de estoque/pronta entrega.
Status: plano/packet interno. Sem write externo executado.

## 1. Objetivo

Transformar o Wishlist Plus / SWYM da LK em um sinal diário de intenção de compra, inicialmente sem disparos automáticos para clientes.

A Fase 1 é apenas leitura, inteligência e preparação:

- entender quais produtos/modelos estão sendo favoritados;
- identificar valor potencial parado em wishlist;
- detectar produtos com alta intenção e baixa conversão;
- preparar oportunidades para merchandising, PDP/CRO, CRM e compras/reposição;
- não enviar email, WhatsApp, SMS ou campanha;
- não alterar Shopify, tema, estoque, preço, Klaviyo ou SWYM live além da configuração já feita manualmente por Lucas.

## 2. Estado atual observado

- SWYM/Wishlist Plus foi ativado no Theme Editor por Lucas.
- Página pública configurada: `/pages/my-wishlist`.
- Storefront funcionou em teste manual com produtos renderizados em “Meus Favoritos”.
- Dashboard SWYM indicou `Live On` e eventos recentes de wishlist.
- Secrets SWYM foram armazenados no Doppler `lc-keys/prd` com status verificado e `values_printed=false`:
  - `SWYM_API_KEY` presente;
  - `SWYM_API_ENDPOINT` presente;
  - `SWYM_PID` presente.

## 3. Escopo permitido da Fase 1

Permitido sem nova aprovação:

- leituras SWYM quando a API permitir;
- leitura Shopify Admin/Storefront para enriquecer produto, handle, preço, status e imagens;
- cruzamento read-only com vendas/visitas quando fontes locais ou APIs read-only estiverem disponíveis;
- geração de relatórios internos em Brain/Telegram;
- proposta de segmentos e copies em draft textual.

Bloqueado sem aprovação explícita atual:

- ativar fluxo SWYM/Klaviyo;
- enviar email/SMS/WhatsApp;
- criar/editar campanha, segmento, flow ou template;
- alterar tema, app embed, página Shopify, produto, preço, estoque, tag, metafield ou coleção;
- prometer disponibilidade/pronta entrega sem validação do LK Stock/Tiny.

## 4. Entrega principal — Wishlist Pulse

Relatório interno recorrente, inicialmente manual ou sob demanda, depois passível de rotina aprovada.

### 4.1. Resumo executivo

Campos:

- total de itens favoritados no período;
- valor total estimado em wishlist;
- número de shoppers/visitantes identificados;
- produtos mais favoritados;
- modelos/famílias mais favoritados;
- maiores oportunidades de receita;
- alertas de risco: alto desejo + baixa disponibilidade, alto desejo + baixa conversão, alto desejo + produto indisponível.

### 4.2. Top produtos por intenção

Para cada produto:

- título;
- handle/URL;
- preço atual Shopify;
- imagem principal;
- número de favoritos;
- valor potencial estimado;
- status Shopify de disponibilidade pública, rotulado como sinal de storefront, não verdade final de estoque;
- sinal de vendas/visitas quando disponível;
- classificação: vitrine, PDP/CRO, CRM, estoque/compras ou monitorar.

### 4.3. Top modelos/famílias

Agrupar por família comercial:

- New Balance 530 / 9060 / 204L;
- Adidas Samba / Gazelle / Spezial / Campus;
- Onitsuka Mexico 66;
- Nike Dunk / Cortez / Vomero / Jordan;
- collabs/cápsulas quando fizer sentido.

Uso:

- decidir blocos de home/coleções;
- priorizar Curadoria LK/PDP;
- orientar compra/reposição via handoff para LK Stock/Compras;
- identificar campanha editorial/CRM.

### 4.4. Oportunidades acionáveis

Buckets:

1. `crm_favoritou_nao_comprou`
   - Produto favoritado, shopper ainda sem compra associada.
   - Próxima ação: preparar fluxo/copy em draft; não ativar.

2. `sale_opportunity`
   - Produto favoritado que entrou em sale/condição especial.
   - Próxima ação: campanha controlada depois de aprovação.

3. `stock_attention`
   - Produto muito favoritado com baixa disponibilidade, indisponível ou potencial volta.
   - Próxima ação: handoff para `lk-stock`; não prometer disponibilidade por Shopify.

4. `pdp_conversion_gap`
   - Muitos favoritos/visitas, baixa compra/add-to-cart.
   - Próxima ação: revisão PDP/CRO: imagens, prova social, variações, preço percebido, descrição, frete/parcelamento.

5. `merchandising_boost`
   - Produto/modelo com intenção forte que merece vitrine, coleção, home ou ordenação.
   - Próxima ação: packet Shopify/coleção separado antes de qualquer write.

## 5. Primeira versão do relatório

Arquivo sugerido:

`areas/lk/sub-areas/shopify/reports/wishlist/wishlist-pulse-YYYYMMDD.md`

Formato Telegram resumido:

```text
Wishlist Pulse LK — DD/MM

Veredito: [ex.: intenção concentrada em NB 204L + Nike Vomero]

Top sinais:
- Produto A: X favoritos / R$Y potencial / ação: PDP ou CRM
- Produto B: X favoritos / R$Y potencial / ação: estoque
- Produto C: X favoritos / R$Y potencial / ação: vitrine

Alertas:
- Estoque: N itens precisam validação lk-stock
- CRO: N produtos com desejo alto e compra baixa
- CRM: N shoppers elegíveis para draft “favoritou e não comprou”

Não executado: sem envios, sem Klaviyo, sem WhatsApp, sem Shopify write.
Próxima decisão: aprovar ou não criação de draft Klaviyo Fase 2.
```

## 6. Regras comerciais e de segurança

- Shopify `available` é apenas sinal de storefront; Tiny/LK Stock é fonte final para estoque/pronta entrega.
- Não usar urgência falsa.
- Não usar desconto por padrão.
- Não criar campanhas para produto indisponível sem validação.
- Frequência futura recomendada para CRM: no máximo 1 toque por shopper por janela definida.
- Clientes recorrentes/premium podem entrar em fila de atendimento humano, mas WhatsApp/contato externo exige aprovação separada.

## 7. Drafts de copy para Fase 2 futura

### Favoritou e não comprou

Assunto:
`Seu favorito ainda está por aqui`

Texto:
`Você salvou este produto na sua lista de favoritos. Se ainda estiver pensando nele, ele continua por aqui na LK.`

CTA:
`Ver meu favorito`

### Favorito entrou em condição especial

Assunto:
`Um favorito seu entrou em condição especial`

Texto:
`Um produto que você salvou está com nova condição na LK. Veja antes que acabe.`

CTA:
`Ver produto`

### Favorito voltou

Assunto:
`Seu favorito voltou`

Texto:
`Um produto que você salvou voltou a aparecer disponível na LK. Confira os tamanhos antes que acabe.`

Observação: só usar após validação de estoque com `lk-stock`/Tiny.

## 8. Critérios de aceite da Fase 1

A Fase 1 estará pronta quando houver:

- leitura SWYM funcionando sem imprimir secrets;
- relatório `Wishlist Pulse` gerado com dados reais;
- enriquecimento mínimo com Shopify público/Admin read-only;
- classificação por buckets acionáveis;
- nenhuma ação externa disparada;
- indicação clara do que exige aprovação para Fase 2.

## 9. Próxima execução proposta

1. Descobrir endpoints/exports SWYM disponíveis usando `SWYM_API_ENDPOINT`, `SWYM_API_KEY` e `SWYM_PID` em runtime, sem imprimir valores.
2. Fazer uma chamada read-only mínima de teste e registrar apenas status/campos/counts.
3. Gerar o primeiro `Wishlist Pulse` com dados reais.
4. Se a API SWYM não permitir extração suficiente, usar export/dashboard manual como fallback temporário.
5. Só depois preparar Fase 2: draft Klaviyo “favoritou e não comprou”, sem ativar.

## 10. Não-ações desta etapa

- Sem Shopify write.
- Sem theme upload.
- Sem Klaviyo write/send/flow activation.
- Sem WhatsApp/email/SMS.
- Sem alteração de preço, estoque, coleção, produto ou tags.
- Sem secrets impressos.
