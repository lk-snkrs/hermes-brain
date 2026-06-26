# LK OS — PRD Continuation v0.2, Mission Control + Sourcing Serial

Status: `active_parallel_prd_continuation`
Data: 2026-05-14
Contexto: LK Sneakers / Projeto LK OS / Hermes Brain
Modo: documentação + análise local/read-only. Nenhum marketplace, WhatsApp, Notion, Shopify, Tiny, Merchant, banco produtivo, campanha, compra ou fornecedor foi acionado por este artefato.

## Veredito

O PRD do LK OS agora deve tratar **Mission Control** como cockpit operacional central e **Stockout/Recompra de 4 meses** como a primeira fila executiva de sourcing. O GMC P2A continua como Step 1 serial em execução; em paralelo, o PRD evolui apenas em documentação, ranking local, gates e estrutura de decisão.

## Decisão operacional ativa

Lucas aprovou continuar em paralelo, mas a serialização de risco permanece:

1. **Step 1 — GMC P2A:** concluir e consolidar a aplicação já autorizada, sem iniciar outro write concorrente no Merchant Center.
2. **Paralelo seguro — PRD/Mission Control:** avançar PRD, cockpit, filas e pacote de aprovação local/read-only.
3. **Step 2 — Sourcing:** só depois do GMC final, preparar aprovação inline para consulta Droper read-only nos candidatos `stockout_exact_ready`; StockX/GOAT apenas como fallback aprovado; sem compra/contato/Notion write.

## Atualização do módulo Mission Control

Mission Control deixa de ser só uma foto de crons/ledger e passa a ser o painel de operação curta do LK OS.

### Entradas mínimas

- `fact_shopify`: pedidos/vendas/SKU/tamanho/receita por janela.
- `fact_tiny_stock`: estoque oficial por SKU/tamanho no depósito `LK | CONTROLE ESTOQUE`.
- `manual_approval`: decisões Lucas/Júlio e status de aprovação.
- `derived_reconciliation`: score, deduplicação SKU, sanity Tiny/Shopify e estado de fila.
- `platform_signal`: GA4/Meta/Google/Metricool quando afetarem demanda, sempre sem virar receita operacional sozinhos.
- `gmc_state`: baseline e progresso de Merchant Center quando houver execução aprovada em andamento.

### Cards obrigatórios

Cada card executivo deve trazer:

- prioridade: P1/P2/P3;
- estado: `ready`, `needs_sanity`, `blocked`, `monitor`;
- produto + tamanho + SKU;
- demanda 120 dias: unidades, receita, última venda;
- estoque Shopify como sinal, Tiny como verdade operacional;
- próximo passo seguro;
- bloqueios explícitos;
- aprovação necessária para qualquer ação externa/write.

### Estados padrão

```text
stockout_exact_ready
→ Tiny zero no tamanho exato; elegível para pacote Droper read-only após GMC final.

stockout_sanity_needed
→ Tiny zero existe, mas tamanho/SKU está ambíguo; exige sanity manual/live antes de marketplace.

shopify_zero_needs_tiny_confirmation
→ Shopify sinaliza zero/negativo, mas Tiny ainda não confirmou; não pode virar sourcing.

monitor_or_no_action
→ demanda insuficiente, estoque não crítico ou dados conflitantes.
```

## Atualização do módulo Supply & Sourcing

O PRD v0.1 falava genericamente em checar fontes. A versão operacional v0.2 fixa o fluxo real da LK Compras:

```text
demanda concreta / venda / pedido
→ confirmar produto + SKU + tamanho
→ confirmar stockout/zero no Tiny
→ Droper primeiro
→ se Droper não resolver: StockX/GOAT fallback com normalização de tamanho
→ decisão humana: menor preço viável ou fonte mais perto de SP se delta pequeno
→ compra/logística humanas
→ Notion/Júlio como registro/log, não automação autônoma
```

Guardrail: Hermes pode preparar ranking, sanity, payload de aprovação e preview de Notion/Júlio. Hermes não compra, reserva, escolhe entregador/importador, escreve Notion, manda WhatsApp, contata fornecedor ou decide financeiramente.

## Ranking stockout/recompra de 4 meses

Janela aprovada: **120 dias**.

Correção metodológica obrigatória:

- Agregar vendas por SKU/modelo antes de cruzar com variants/Tiny.
- Evitar duplicar receita quando SKU aparece em múltiplos tamanhos/variants.
- Separar `Tiny exact size zero` de `Tiny ambiguous/mismatch`.
- Usar Shopify zero como sinal, não como verdade final de estoque.

Snapshot gerado em 2026-05-14:

- 872 grupos de venda com SKU.
- 647 candidatos de recompra/stockout.
- 18 candidatos fortes com Tiny zero no tamanho exato.
- 20 candidatos com Tiny zero ambíguo/mismatch.
- 609 candidatos que precisam confirmação Tiny.

Top candidato atual:

- Produto: Tênis New Balance 204L Arid Timberwolf Bege — 37.
- SKU: `U204LMMC-4`.
- Demanda 4 meses: 8 un · R$ 22.399,92.
- Tiny: 0 no tamanho 37.
- Próximo seguro: pacote de aprovação Droper read-only após GMC P2A final.

## Gate GMC P2A

Enquanto o executor P2A estiver rodando:

- não iniciar novo Merchant write concorrente;
- não reexecutar o mesmo patch sem consolidar progresso JSONL e rollback;
- Mission Control pode ler progresso e preparar fila;
- Step 2 sourcing fica bloqueado para marketplace até relatório final do GMC.

Estado observado nesta continuação:

- processo vivo: `scripts/lk_gmc_p2a_finalize_remaining_online_20260513.py --apply`;
- progresso JSONL observado: 6.250 linhas de patch registradas de 9.826 candidatos esperados no contexto anterior;
- tipos mais aplicados até o checkpoint: Tênis, Calça, Moletom/Jaqueta, Boné, Shorts, Bolsa/Carteira.

## Definition of Done v0.2 para este bloco

- [x] Mission Control contém ranking de 4 meses em cards executivos.
- [x] PRD registra o padrão real LK Compras → Júlio/Notion.
- [x] PRD fixa janela 120 dias e deduplicação antes do join Tiny.
- [x] Sourcing externo permanece approval-gated.
- [x] GMC P2A segue serial, sem executor concorrente.
- [ ] Consolidar relatório final GMC P2A quando o processo terminar.
- [ ] Gerar pacote Droper read-only inline para os `stockout_exact_ready`, após GMC final.
- [ ] Só depois, se aprovado, consultar Droper; StockX/GOAT fallback exige escopo inline.

## Não executado

- Sem Droper/StockX/GOAT/KicksDev lookup.
- Sem WhatsApp leitura/envio.
- Sem fornecedor/compra/reserva.
- Sem Notion write.
- Sem Shopify/Tiny/Supabase/Klaviyo/Meta/Google write.
- Sem novo Merchant write além do executor P2A já autorizado e em andamento.
- Sem cron/UI/worker novo.

## Artefatos relacionados

- `reports/lk-mission-control-snapshot-2026-05-14.md`.
- `reports/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.md`.
- `scripts/lk_os_stockout_recompra_rank_and_notion_preflight_20260514.py`.
- `reports/lk-mission-control-snapshot-2026-05-14.json`.
