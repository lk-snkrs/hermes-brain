# PRD — Auto-ordenação semanal de coleções Shopify LK

Status: proposta / aguardando aprovação para implementação
Data: 2026-05-26
Dono: LK Growth / Lucas
Executor proposto: Hermes LK Shopify, com governança Hermes Geral

## 1. Pedido limpo

Criar um sistema de auto-ordenação das coleções Shopify da LK Sneakers para que, ao entrar em uma coleção, o cliente veja primeiro:

1. até 8 produtos mais novos lançados nos últimos 90 dias;
2. se houver menos de 8 produtos novos, completar os primeiros 8 slots com produtos mais vendidos e/ou mais acessados;
3. ordenar o restante da coleção por performance comercial e interesse, preservando filtros, SEO, estoque/preço e layout.

Rodar automaticamente todos os domingos às 04h, gerar relatório de execução e acompanhar se a performance de cada coleção melhorou, piorou ou ficou inconclusiva.

## 2. Veredito estratégico

A ideia é boa para a LK, desde que seja implementada como merchandising controlado e mensurado, não como reorder cego.

Motivo: a LK vende curadoria e novidade. Mostrar lançamentos primeiro reforça percepção de seleção viva/premium e ajuda modelos novos a ganharem tração. O risco é empurrar para baixo best-sellers que sustentam conversão. Por isso, a regra dos 8 primeiros slots precisa misturar novidade com fallback por demanda e ter guardrails por performance.

Recomendação: aprovar um piloto com modo dry-run + preview em 5 a 10 coleções prioritárias antes de aplicar em todas.

## 3. Escopo

### Inclui

- Descobrir coleções elegíveis.
- Ler produtos de cada coleção.
- Calcular ranking por coleção.
- Gerar proposta de nova ordem.
- Backup da ordem atual.
- Aplicar reordenação apenas após aprovação explícita.
- Relatório semanal com antes/depois, mudanças, riscos e performance.
- Revisão de impacto após 7, 14 e 28 dias.

### Não inclui sem aprovação separada

- Alterar preço, estoque, disponibilidade ou desconto.
- Alterar título, descrição, SEO, imagem, tag, metafield ou coleção.
- Publicar tema, alterar layout, filtros ou checkout.
- Enviar mensagem para cliente/time.
- Criar/ativar cron de produção sem aprovação atual.

## 4. Fontes de dados

### Shopify Admin — read/write controlado

Leitura:

- coleções: id, handle, title, sortOrder, productsCount;
- produtos na coleção: product id, handle, title, createdAt, publishedAt, status, vendor, productType, tags;
- ordem atual da coleção;
- pedidos/line items por janela de vendas para calcular best-sellers.

Escrita futura, se aprovada:

- `collectionReorderProducts` via Shopify Admin GraphQL.

Observações técnicas Shopify:

- A mutation oficial é `collectionReorderProducts`.
- Requer escopo `write_products`.
- Só funciona quando `Collection.sortOrder = MANUAL`.
- Usa índice zero-based: posição `0` = primeiro produto.
- É assíncrona e retorna `job`, que deve ser monitorado até `done=true`.
- Aceita até 250 movimentos por chamada; coleções maiores exigem lotes sequenciais.
- Deve enviar apenas produtos que mudaram de posição, não a lista inteira.

### GA4 / site analytics — read-only

- pageviews/sessions por PDP ou item list quando disponível;
- clicks em produto na collection, add-to-cart e purchase por item quando disponível;
- janela recomendada: últimos 30/60/90 dias.

### Shopify sales — read-only

- unidades vendidas por produto;
- receita por produto;
- pedidos por produto;
- janela recomendada: últimos 90/180 dias.

## 5. Definições

### “Produto novo / lançado”

Regra proposta:

- produto é novo se `publishedAt` ou, na ausência dele, `createdAt` estiver dentro dos últimos 90 dias;
- se houver uma tag/metafield futuro tipo `lk_launch_date`, ela deve ter prioridade por representar data editorial real de lançamento.

### “Mais vendidos / mais acessados”

Score recomendado para fallback e restante da coleção:

- 70% vendas: unidades vendidas e receita na janela;
- 30% interesse: pageviews/clicks/add-to-cart na janela;
- desempate: margem/conveniência comercial só se existir fonte confiável e aprovada; caso contrário, usar recência e disponibilidade pública.

Se GA4 não estiver confiável por produto, usar Shopify sales como base e registrar `acessos indisponíveis` no relatório.

## 6. Algoritmo proposto

Para cada coleção elegível:

1. carregar lista atual de produtos e ordem atual;
2. separar produtos ativos/publicados da coleção;
3. identificar `novos_90d`;
4. ordenar `novos_90d` por data de lançamento mais recente, com desempate por performance;
5. preencher os primeiros 8 slots:
   - primeiro: até 8 produtos de `novos_90d`;
   - se houver menos de 8, completar com produtos de maior `performance_score` que ainda não entraram;
6. ordenar o restante por `performance_score`, com um leve bônus de recência para não enterrar produtos recém-lançados que ficaram fora do top 8;
7. gerar `desired_order`;
8. comparar com `current_order` e calcular movimentos mínimos;
9. no modo dry-run, salvar preview e relatório, sem escrever no Shopify;
10. no modo apply aprovado, executar `collectionReorderProducts`, aguardar `job.done`, reconsultar a coleção e validar a nova ordem.

## 7. Guardrails de merchandising

- Não mexer em coleções com `sortOrder` diferente de `MANUAL` sem decisão específica.
- Não reordenar coleção com menos de 4 produtos, salvo se fizer sentido comercial.
- Não mover manualmente produtos fixados/estratégicos se houver futura tag/metafield `lk_pin_top` ou `lk_pin_position`.
- Não promover produto oculto, arquivado, sem URL pública ou removido da coleção.
- Separar análise de estoque: Shopify não é a verdade final de estoque LK; Tiny é a fonte de estoque. Esta automação não altera disponibilidade.
- Limitar a mudança máxima por rodada no piloto: por exemplo, não deslocar mais de 60% dos produtos de uma coleção sem revisão humana.
- Permitir denylist de coleções sensíveis: Sale, lançamentos especiais, campanhas, collabs ou coleções editoriais.

## 8. Execução semanal proposta

Horário:

- todo domingo às 04:00 BRT;
- cron técnico: `0 4 * * 0` com timezone `America/Sao_Paulo`.

Fases:

1. `snapshot`: salvar ordem atual e métricas de baseline;
2. `rank`: calcular nova ordem;
3. `dry_run`: gerar diff por coleção;
4. `apply`: somente se Lucas aprovar modo produção;
5. `verify`: ler Shopify após job concluído;
6. `report`: entregar resumo limpo ao Lucas e arquivar detalhes no Brain;
7. `impact_review`: comparar métricas após 7/14/28 dias.

## 9. Relatório semanal

Campos mínimos por coleção:

- coleção / handle;
- produtos totais;
- quantidade de novos 90d;
- top 8 anterior;
- top 8 proposto/aplicado;
- produtos promovidos;
- produtos rebaixados;
- motivo da mudança: novo, vendido, acessado, fallback;
- status: dry-run, aplicado, pulado, erro;
- riscos/observações;
- link da coleção.

Resumo executivo:

- coleções analisadas;
- coleções alteradas;
- coleções puladas e motivo;
- top oportunidades;
- anomalias;
- rollback disponível.

## 10. Mensuração de impacto

Comparar por coleção antes/depois, preferencialmente em janelas semanais equivalentes:

- sessões na coleção;
- product clicks/list clicks;
- add-to-cart rate;
- conversion rate da coleção/sessões atribuídas;
- pedidos e receita atribuíveis;
- CTR orgânico GSC para páginas de coleção, quando aplicável;
- bounce/engagement onde disponível.

Veredito por coleção:

- `melhorou`: sinais de conversão/receita/ATC sobem sem queda relevante de tráfego;
- `piorou`: conversão, ATC ou receita caem de forma relevante sem explicação externa;
- `neutro`: mudanças pequenas;
- `inconclusivo`: baixo volume, tracking insuficiente ou evento externo.

Importante: não atribuir causalidade forte só pela mudança de ordem. Tratar como sinal CRO/merchandising, com sazonalidade, drops, mídia e estoque como variáveis externas.

## 11. Rollback

Antes de qualquer aplicação:

- salvar JSON com ordem atual por coleção;
- salvar top 8 atual e lista completa de product IDs;
- salvar timestamp, executor, versão do algoritmo e payload planejado.

Rollback:

- executar `collectionReorderProducts` para restaurar a ordem anterior;
- aguardar job assíncrono;
- reconsultar coleção;
- gerar receipt de rollback.

## 12. Modo piloto recomendado

Piloto em 2 fases:

### Fase A — diagnóstico/dry-run

- Rodar sem writes em todas as coleções ou em amostra priorizada.
- Produzir relatório com o que mudaria.
- Lucas aprova ou ajusta pesos/guardrails.

### Fase B — aplicação controlada

- Aplicar em 5 a 10 coleções com maior tráfego/comercialidade.
- Monitorar 7/14/28 dias.
- Só expandir para todas as coleções se o resultado for positivo ou neutro.

Coleções candidatas iniciais devem ser escolhidas por tráfego e receita, não só por gosto editorial.

## 13. Riscos

- Converter pior se best-sellers forem empurrados para baixo por produtos novos fracos.
- Dado de “mais acessado” pode estar incompleto se GA4/item tracking não estiver confiável.
- Coleções com sort não-manual não podem ser reordenadas pela mutation sem alteração de configuração.
- Reorder é write de Shopify e afeta storefront; exige aprovação explícita atual.
- Coleções grandes exigem batching e fila por coleção para evitar conflitos.

## 14. Bloqueios atuais

- Não foi criado cron real.
- Não foi feita mutation em Shopify.
- Falta aprovação explícita para: autenticação read-only inicial, dry-run operacional, criação do cron e aplicação em produção.
- Falta confirmar lista de coleções elegíveis/excluídas.
- Falta confirmar janela e pesos finais de performance.

## 15. Decisão recomendada para Lucas

Aprovar primeiro apenas o diagnóstico/dry-run:

> “Aprovado rodar o dry-run read-only da auto-ordenação das coleções LK, sem aplicar mudanças no Shopify, gerando preview/relatório com top 8 atual vs proposto, coleções puladas e plano de rollback.”

Depois do dry-run, decidir:

1. pesos finais entre novo/vendido/acessado;
2. coleções excluídas;
3. piloto de aplicação;
4. criação do cron de domingo 04h.

## 16. Evidências consultadas

- Shopify Dev Docs: `collectionReorderProducts` é a mutation oficial para reordenar produtos em coleção.
- Shopify Dev Docs: requer `write_products`, coleção com `sortOrder = MANUAL`, job assíncrono e polling.
- Brain LK Shopify: writes em Shopify, inclusive coleção, exigem aprovação explícita atual.
- Brain LK Growth: mudanças aprovadas devem gerar rollback snapshot, receipt, evidência e revisão de impacto.
