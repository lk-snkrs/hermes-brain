# Exemplo preenchido — Weekly CEO Review LK

Status: exemplo fictício/read-only v0.1.
Semana simulada: 2026-05-02 a 2026-05-08.
Uso: validar formato executivo antes de dados reais, cron, envio recorrente ou integração de escrita.
Não faz: mensagem, campanha, publicação, compra, Notion, preço, estoque, Shopify/Tiny/Klaviyo/Meta/Google/n8n.

## 1. Resumo CEO

```text
Semana: 2026-05-02 a 2026-05-08
Receita: R$ 91.420,00
Pedidos: 41
Ticket médio: R$ 2.229,75
Conversão online: 0,15% vs baseline 0,13% e meta 0,20%
Recompra: 7 clientes recorrentes no exemplo; taxa 90 dias ainda precisa baseline real
Melhor sinal: New Balance e Onitsuka venderam bem com tráfego de Google/influencer
Maior problema: risco de ruptura em tamanhos vendidos e PDPs com tráfego sem clareza de disponibilidade
Decisão nº 1 para Lucas: aprovar primeira rodada read-only com dados reais mascarados antes de cron
```

Leitura CEO: a semana simulada mostra que a LK pode ganhar mais com três alavancas simples: não romper tamanhos bons, melhorar PDP/disponibilidade para subir conversão e aprender qual influencer funciona para qual produto.

## 2. Vendas e canais

- Receita total: R$ 91.420,00.
- Pedidos: 41.
- Ticket médio: R$ 2.229,75.
- Online vs loja física: online R$ 63.300,00 / 28 pedidos; loja física R$ 28.120,00 / 13 pedidos.
- Source/canal: Google Ads 12 pedidos; Meta Ads 7; influencer/UTM 4; orgânico 5; loja física 13.
- Produtos/modelos líderes: New Balance 860, Onitsuka `[modelo]`, Adidas `[modelo]`.
- Tamanhos líderes: 37, 38, 39.
- Variação vs semana anterior: +11% receita no exemplo.
- Anomalias: Meta trouxe tráfego alto, mas pedido baixo; Google gerou pedidos mais consistentes.

## 3. Conversão online / CRO

Meta: sair de **0,13% para 0,20%**.

- Conversão Shopify Analytics: 0,15%.
- Sessões: 18.600.
- Produtos/PDPs com tráfego e baixa conversão: `[PDP A]` com 1.340 sessões e 1 pedido; `[PDP B]` com 980 sessões e 0 pedido.
- Canais que trouxeram tráfego ruim: Meta Ads no exemplo, especialmente criativo amplo sem produto claro.
- Gargalo provável: mistura de PDP sem clareza de tamanho disponível + tráfego amplo demais.
- Teste recomendado: bloco visual de disponibilidade por tamanho + campanha Meta mais amarrada a produto/grade.
- Aprovação necessária: HTML visual do bloco PDP e briefing de campanha antes de qualquer publicação.

## 4. Recompra / CRM / RFM

Meta: **+50% em recompra**.

- Taxa recompra 90 dias: `[baseline real pendente]`; exemplo usa 7 clientes recorrentes na semana.
- Clientes que recompraram: 7 no exemplo, sem dados pessoais.
- Receita recorrente: R$ 17.900,00 simulados.
- Segmentos com oportunidade: compradores New Balance 37–39; compradores Onitsuka 36–38; clientes loja física com compra nos últimos 60–90 dias.
- Pós-compra que deveria existir: curadoria por marca/tamanho e lembrete de novos modelos relacionados.
- Klaviyo sugerido: draft para segmento “New Balance/running lifestyle”, sem envio.
- WhatsApp sugerido: abordagem manual para clientes VIP de loja física, com aprovação.
- Aprovações necessárias: segmentação, copy, canal e timing antes de qualquer envio.

## 5. Stock Intelligence Center

- Produtos com risco de ruptura: New Balance 860 37/38; Onitsuka 36.
- Produtos zerados relevantes: New Balance 860 38; Onitsuka 36.
- Compra antes de acabar: New Balance 860 37, porque estoque ainda existe mas cobertura está perto do lead time Brasil.
- Estoque alto/lento: Nike `[modelo/cor]` 44; Adidas `[modelo/cor]` 35, se confirmado no Tiny.
- Divergências Tiny/Shopify/pedido: conferir pedidos com tag de encomenda BR/US antes de chamar estoque de livre.
- Itens para `LK.Sneakers | Compras`: New Balance 860 38 como prioridade após aprovação.
- Itens para Notion `LK Compras`/`LK Encomendas`: nenhum real neste exemplo; só criar depois de aprovação humana.

## 6. Brand Mix Intelligence

- Share por marca em receita: New Balance 34%; Onitsuka 26%; Adidas 18%; Nike 12%; outras 10% no exemplo.
- Share por marca em unidades: New Balance 31%; Onitsuka 29%; Adidas 17%; Nike 14%; outras 9%.
- Marca crescendo: New Balance, puxada por 860 e modelos running.
- Marca caindo: Nike no exemplo, mas pode ser efeito de estoque/tamanho e não de desejo.
- Marca com queda por falta de estoque: Onitsuka tamanho 36/37 precisa validação.
- Marca com hype externo mas baixa venda LK: `[a confirmar com KicksDev/StockX/Google Trends]`.
- Produto/modelo que explica mudança: New Balance 860 é o principal driver simulado.

Leitura: o ranking deve sair do histórico, não de preferência fixa. A ação não é “comprar Nike porque Nike é grande”; é entender qual marca/modelo/tamanho está girando com a curadoria LK.

## 7. Paid Traffic & Influencer Intelligence

- Google Ads: melhor intenção de compra no exemplo, com 12 pedidos.
- Meta Ads: tráfego alto, conversão baixa; precisa revisar criativo/produto/landing.
- Influenciadores ativos: `influencer_exemplo_maio`.
- Produto divulgado: Onitsuka `[modelo]` e New Balance `[modelo]`.
- UTM/campanha/cupom: UTM presente; cupom não confirmado.
- Receita/pedidos/conversão atribuída: 4 pedidos e R$ 8.700,00 simulados.
- Melhor fit influencer × produto: influencer parece performar melhor com Onitsuka do que Adidas no exemplo.
- Próximo produto recomendado por influencer: Onitsuka similar ou New Balance running clean, se estoque permitir.
- Problema de tracking/UTM: padronizar UTM por influencer/produto/campanha antes de escalar.

## 8. SEO / Trend-to-Product-to-Blog

- Tendências lá fora relevantes: running/lifestyle e silhuetas retro-tech no exemplo.
- Produto já disponível na LK: New Balance 860 e produtos relacionados.
- Produto disponível em StockX/KicksDev/Droper: consultar só se houver sinal interno e aprovação de pesquisa.
- Preço sugerido LK, se aplicável: usar fórmula v0.1 apenas após preço de fonte validado.
- Blog post Shopify recomendado: “Por que o New Balance 860 voltou para a conversa” com links para produtos LK disponíveis.
- Link de produto necessário: `[link Shopify a preencher]`.
- Conteúdo aprovado/pendente: pendente de HTML/brief visual e aprovação.

## 9. Content & Campaign Production Engine

Tudo deve seguir DesignMD LK.

- Pautas Instagram: “running que não parece uniforme”, “3 formas de usar New Balance 860”, “Onitsuka além do óbvio”.
- Newsletter: curadoria de running/lifestyle com disponibilidade real por tamanho.
- Blog: tendência + curadoria + produto LK linkável.
- Klaviyo: segmento New Balance/Onitsuka com estoque seguro.
- WhatsApp: só 1:1 para clientes loja física/VIP após aprovação.
- PDP/produto: bloco visual de disponibilidade por tamanho e encomenda humana.
- HTML/layout precisa ser visual antes de aprovação: sim.
- Peças prontas para Lucas aprovar: ainda não; próximo passo é gerar rascunhos visuais.

## 10. Shopify Operations

- Produtos para subir como draft: nenhum sem confirmação de fonte/preço.
- PDPs para melhorar: New Balance 860 e Onitsuka `[modelo]`.
- Coleções para ajustar: running/lifestyle e lançamentos recentes, se estoque real suportar.
- Produtos sem SEO/imagem/copy: `[a auditar com Shopify read-only]`.
- Tema/PR necessário: não nesta etapa.
- Atenção: tema publicado exige PR/preview/aprovação.

## 11. Aprendizados e Hermes Learning Loop

```text
Aprovado por Lucas: Brand Mix Intelligence, Stock Intelligence Center, Influencer Intelligence e exemplos por tamanho/variante.
Correção de Lucas: encomenda BR/US é curadoria humana no pedido, não automação cega.
Padrão aprendido: fonte externa deve ser acionada por demanda interna, não monitoramento contínuo de retailers.
Anti-padrão: sugerir compra com base em “marca importante” sem estoque, venda, tamanho, preço e lead time.
Documento/skill/PRD atualizado: templates read-only e exemplos v0.1.
Resultado observado: formato pronto para validação antes de dados reais.
```

## 12. Decisões para Lucas

1. Decisão: aprovar formato dos exemplos para primeira execução com dados reais read-only.
   Recomendação Hermes: aprovar.
   Por quê: o formato separa fato, leitura, ação, risco e aprovação.
   Risco: se o dado real vier incompleto, o relatório pode ter muitos `[a confirmar]`.
   Próximo passo se aprovado: rodar primeiro Daily Sales Brief real mascarado.

2. Decisão: priorizar qual output real vem primeiro.
   Recomendação Hermes: Daily Sales Brief real antes do Weekly CEO Review.
   Por quê: ele testa Shopify/Tiny/Analytics/estoque em ciclo curto.
   Risco: exige acesso read-only consistente.
   Próximo passo se aprovado: mapear fontes e permissões read-only.

3. Decisão: criar cron agora ou não.
   Recomendação Hermes: não criar cron ainda.
   Por quê: falta aprovar formato com dados reais e mapear roteamento da equipe.
   Risco: automatizar cedo gera ruído e relatório para pessoa errada.
   Próximo passo se aprovado: manter sob demanda até primeiro relatório real aprovado.

## 13. O que não foi feito

- Nenhum Klaviyo/WhatsApp enviado.
- Nenhum Shopify/blog/tema publicado.
- Nenhum preço/estoque alterado.
- Nenhuma compra/fornecedor/revendedor acionado.
- Nenhum item Notion real criado.
- Nenhuma campanha Google/Meta criada ou alterada.
