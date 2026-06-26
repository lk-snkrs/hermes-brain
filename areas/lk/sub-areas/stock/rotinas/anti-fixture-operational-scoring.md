# Rotina — Anti-fixture no scoring operacional LK Stock

Status: canônica
Criada em: 2026-06-09
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Origem: Mesa COO 2026-06-09 Decisão 2/3 + receipt de rollback `areas/lk/sub-areas/stock/receipts/lk-stock-rollback-wrong-p0-fixture-blend-dm0032005-40-20260608T211459Z.md`

## Regra canônica

Fixtures, probes, testes e qualquer dado marcado como simulação **nunca** podem alimentar:

- blend de demanda;
- score P0/P1/P2/P3;
- fila de reposição/transferência/compra;
- quantidade sugerida;
- promessa de pronta entrega ou disponibilidade;
- recomendação operacional para Lucas, Júlio, fornecedor, cliente ou campanha.

## Fontes proibidas no cálculo operacional

Bloquear no mínimo fontes/padrões:

- `shopify_fixture`;
- `tiny_fixture`;
- `manual_fixture`;
- `GATEB-PROBE-*`;
- qualquer `source` com `fixture`, `probe` ou `test`;
- arquivos em `fixtures/`;
- payloads usados só para teste, dry-run, demo, regressão ou validação técnica.

Essas fontes podem existir como evidência técnica ou teste automatizado, mas não como evidência comercial.

## Fonte mínima aceitável para decisão

Antes de classificar P0/P1 ou gerar action packet, exigir:

1. SKU/variant/Tiny com confiança alta ou item `needs_sku_resolution`.
2. Estoque confirmado em fonte viva Tiny, preferencialmente depósito `LK | CONTROLE ESTOQUE`.
3. Demanda vinda de venda real/read-only Shopify, dado comercial vivo, relatório validado, ou sinal Growth/Trends explicitamente classificado como operacional.
4. Freshness suficiente; se stale, a ação é consultar fonte viva antes de afirmar ruptura ou disponibilidade.

## Procedimento no loop

1. Resolver produto → variant → SKU → tamanho.
2. Separar fonte operacional de fonte técnica/teste.
3. Excluir fixtures/probes/testes antes de somar vendas, demanda ou snapshots de estoque.
4. Se só houver fonte excluída, bloquear a decisão como `needs_sku_resolution`/fonte insuficiente e registrar o motivo.
5. Só então calcular score e classificar P0/P1/P2/P3.
6. Para P0/P1, criar action packet com `writes externos: 0` até aprovação escopada.
7. Registrar receipt/handoff quando houver correção, rollback, recomendação material ou aprendizado.

## Sinais de alerta

- SKU/tamanho aparece com demanda alta mas a origem é `fixture`, `probe`, `test` ou payload em `fixtures/`.
- SQLite local tem linha de demanda sem correspondência com venda real/fonte viva.
- Um score P0/P1 depende de snapshot `tiny_fixture` ou `freshness` não decision-grade.
- Produto placeholder foi resolvido para SKU real sem revalidar a origem da demanda.

## Resposta obrigatória ao detectar contaminação

Se fixture/probe/teste entrou em qualquer fila operacional:

1. Marcar o artefato como `superseded / não usar para execução`.
2. Remover/quarentenar a linha da base operacional local, com backup quando houver DB.
3. Recalcular score/fila.
4. Registrar receipt com causa raiz, rollback, artefatos afetados e writes externos `0`.
5. Não executar Tiny/Shopify/fornecedor/cliente/campanha até nova validação por fonte viva.

## Verificação

- Teste de regressão deve provar que `shopify_fixture`, `tiny_fixture`, `manual_fixture`, `GATEB-PROBE-*`, `probe` e `test` não geram P0/P1.
- `stock_score.recalculate_scores` deve filtrar fontes excluídas antes de consultar `sales_velocity`, `demand_signals` e `stock_snapshots`.
- Secret scan focado nos arquivos alterados deve retornar `0` findings.

## Fora de escopo

Esta rotina não autoriza:

- Tiny write;
- Shopify write;
- compra/fornecedor;
- promessa a cliente;
- campanha/CRM;
- novo cron/runtime/gateway;
- alteração em Docker/VPS/produção.
