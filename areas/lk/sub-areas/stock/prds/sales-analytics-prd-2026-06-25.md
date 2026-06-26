# PRD — LK Sales Analytics OS

- **Data:** 2026-06-25
- **Dono operacional:** LK Stock / Sales OS
- **Pedido original:** Lucas pediu um analytics de venda: vendas por dia, semana e mês; projeção do mês; distribuição por produto, marca, lugar/canal e afins; usando Superpowers e adaptado ao mundo LK.
- **Status:** PRD v1 documental, sem ativação de write externo.
- **Guardrails:** Shopify write 0; Tiny write 0; Notion write 0; compra automática 0; contato externo 0.

## 1. Problema

A página `/vendas` hoje já mostra alguns sinais comerciais, mas ainda não é um **sistema analítico de decisão**. Ela mistura blocos operacionais, listas pesadas e painéis parciais sem uma narrativa clara para Lucas responder rápido:

1. Quanto vendemos hoje?
2. Como está a semana?
3. Como está o mês contra projeção?
4. O que está puxando venda por produto/modelo/marca?
5. Onde vendeu: loja física, site, canais/origens?
6. Que venda deveria virar ação de estoque/reposição?
7. Quais dados estão frescos e confiáveis?

## 2. Objetivo

Criar o **LK Sales Analytics OS**, uma camada read-only dentro de `/vendas` para transformar vendas em decisão operacional, sem poluir o Stock OS e sem executar ações externas automaticamente.

A tela precisa ser minimalista, executiva e navegável por sidebar própria:

- **Hoje:** venda do dia, pedidos, ticket médio, itens, canal dominante e alertas.
- **Semana:** acumulado semanal, comparação com semana anterior e ritmo.
- **Mês:** acumulado mensal, projeção até fechamento e meta/farol quando houver meta configurada.
- **Mix:** distribuição por produto, família/modelo, marca, categoria e canal/lugar.
- **Reposição:** itens com venda real + cobertura curta no estoque.
- **Qualidade:** freshness, cobertura do índice e lacunas de dados.

## 3. Usuários

| Usuário | Necessidade |
|---|---|
| Lucas | Entender performance e decidir compra/estoque sem mergulhar em planilha. |
| LK Operações | Saber quais produtos/canais estão gerando ação hoje. |
| Júlio / compras | Receber lista já filtrada por venda real e cobertura de estoque, após aprovação. |
| Hermes Stock/Sales | Cruzar venda com estoque e produzir recomendações com fonte/freshness. |

## 4. Princípios UX

1. **Executivo primeiro:** primeira dobra responde “como está vendendo?” e “tem ação?”.
2. **Sidebar própria de Vendas:** `/vendas` não usa a sidebar de filtro de estoque; usa navegação por analytics.
3. **Progressivo:** carregar resumo e health primeiro; analytics pesadas sob demanda ou em segundo plano.
4. **Read-only explícito:** toda ação externa vira preview/approval, nunca execução automática.
5. **Sem métricas vazias:** qualquer KPI sem fonte/freshness suficiente fica oculto ou marcado como “não confirmado”.
6. **Produto → decisão:** qualquer item de venda relevante deve conseguir abrir Produto 360 e cruzar com Stock OS.

## 5. Métricas v1

### 5.1 Resumo executivo

- Receita bruta / líquida quando disponível.
- Pedidos pagos.
- Itens vendidos.
- Ticket médio.
- Unidades por pedido.
- Canal principal do período.
- Freshness da última ingestão.

### 5.2 Janelas temporais

| Janela | Pergunta | Métricas |
|---|---|---|
| Hoje | O que vendeu hoje? | pedidos, itens, receita, ticket, top produtos, canal. |
| Semana | Estamos acelerando ou desacelerando? | acumulado semana, comparação semana anterior, variação %. |
| Mês | Quanto vamos fechar? | MTD, run-rate, projeção mês, dias restantes. |
| 30/90/180 dias | O que sustenta compra? | unidades, recência ponderada, recorrência e sazonalidade. |

### 5.3 Distribuições

- Por produto/modelo/família.
- Por SKU/tamanho quando existir granularidade.
- Por marca.
- Por categoria/tipo.
- Por canal: loja física, site, POS, online, marketplace se houver.
- Por local/lugar quando a fonte trouxer location/store.
- Por forma de pagamento se a fonte confiável existir.

### 5.4 Projeção mensal

Fórmula v1 conservadora:

```text
projecao_mes = vendas_mtd / dias_decorridos_validos * dias_no_mes
```

Regras:

- Excluir dia atual incompleto da projeção se a hora de corte ainda não passou.
- Mostrar intervalo conservador quando houver volatilidade alta.
- Não comparar com meta se meta não estiver configurada em fonte canônica.

## 6. Produto 360 comercial

Ao buscar/clicar produto em `/vendas`, abrir visão com:

- vendas hoje / 7d / 30d / 90d / 180d;
- canais onde vendeu;
- grade/tamanhos vendidos;
- estoque atual Stock OS por tamanho;
- buracos de grade e recomendação de compra;
- status de identidade/freshness;
- CTA seguro: “Acionar Hermes” / “Preparar reposição” como preview, não write.

## 7. Integração com Stock OS

A decisão de reposição precisa cruzar:

1. Vendas reais ponderadas: `30d*5 + 90d*2 + 180d*1`.
2. Estoque atual Stock OS, preferindo DB local fresca.
3. Grade por tamanho.
4. Fit comercial LK.
5. Compra pendente/inbound quando houver.

Saída esperada:

- “Comprar/repor” quando produto tem demanda real e estoque/grade justificam.
- “Completar grade” quando faltam tamanhos úteis.
- “Corrigir cadastro” quando identidade bloqueia a decisão.
- “Monitorar” quando a venda existe mas não sustenta compra.

## 8. Dados e fontes

| Fonte | Uso | Observação |
|---|---|---|
| Shopify Sales OS DB local | pedidos pagos, line items, canais, produtos | read-only; fonte quente de vendas. |
| Stock OS DB local | estoque, grade, freshness, identidade | caminho quente para estoque interno. |
| Reports locais LK | fallback/agregados históricos | explicitar cobertura parcial. |
| Tiny/Olist | reconciliação de estoque quando DB stale/ambígua | read-only sob exceção; não hot path de analytics. |

## 9. Rotas/API v1 propostas

- `GET /api/vendas/summary?period=today|week|month|30d|90d|180d`
- `GET /api/vendas/timeseries?grain=day|week|month&from=&to=`
- `GET /api/vendas/distribution?by=product|brand|category|channel|location&period=`
- `GET /api/vendas/projection?month=YYYY-MM`
- `GET /api/vendas/product-360?q=...`
- `GET /api/vendas/replenishment-signals?period=30d|90d|180d`
- `GET /api/vendas/health`

## 10. UI v1 proposta

Sidebar `/vendas`:

1. Hoje — ação executiva.
2. Resumo — dia/semana/mês.
3. Produtos — mais vendidos e Produto 360.
4. Canais — loja × site × origem.
5. Marcas — distribuição e concentração.
6. Reposição — venda × estoque.

Primeira dobra:

- Header simples: Controle de Vendas.
- Cards compactos: Hoje, Semana, Mês, Projeção.
- Bloco “Ação hoje” com no máximo 5 itens.
- Health/freshness discreto.

## 11. Critérios de aceite

- `/vendas` abre por link direto e possui sidebar própria.
- Resumo carrega sem esperar analytics pesadas.
- Métricas mostram período e freshness.
- Projeção mensal explicita fórmula e limitação.
- Distribuições por produto/marca/canal funcionam com dados reais ou informam “não confirmado”.
- Produto 360 cruza venda + estoque por tamanho.
- CTA “Acionar Hermes” não executa write; apenas prepara pedido estruturado.
- Testes cobrem HTML/rotas/API e ausência de chamadas pesadas no primeiro load.
- `npm test` e Impeccable passam antes de deploy.

## 12. Fora de escopo v1

- Compra automática.
- Criação direta no Notion sem approval.
- Escrita em Shopify/Tiny.
- Promessa pública de disponibilidade.
- Forecast estatístico avançado com sazonalidade/ML.
- Metas financeiras se não houver fonte canônica de meta.

## 13. Plano de implementação em fases

### Fase 1 — UX e navegação

- Sidebar própria `/vendas`.
- Alinhamento visual e CTA seguro.
- Garantir link direto e scroll por seção.

### Fase 2 — Summary temporal

- Expandir `/api/vendas/summary` para `today/week/month`.
- Cards “Hoje / Semana / Mês / Projeção”.
- Testes de contrato e fallback honesto.

### Fase 3 — Distribuições

- Endpoint de distribuição por produto/marca/categoria/canal/local.
- Blocos visuais compactos e tabelas sob demanda.

### Fase 4 — Projeção mensal

- Endpoint de projeção.
- Regra de dia incompleto.
- Comparação com meta só se configurada.

### Fase 5 — Produto 360 + reposição

- Consolidar vendas por tamanho.
- Cruzar com Stock OS grade atual.
- CTA de reposição preview-first.

## 14. Riscos

| Risco | Mitigação |
|---|---|
| Canal/local incompleto | Mostrar coverage/freshness e não inferir como verdade total. |
| Histórico parcial | Expor período coberto; exigir backfill para “história toda”. |
| Load pesado | Summary-first + analytics progressiva/sob demanda. |
| Confundir venda com disponibilidade | Separar Sales OS de Stock OS; disponibilidade só com fonte viva/local fresca. |
| CTA virar write | Botão apenas copia/prepara payload; qualquer write exige aprovação escopada. |

## 15. Decisão pendente

Definir se a Fase 2 deve incluir meta mensal configurável no Brain ou se, por enquanto, a projeção aparece sem meta.
