# PRD v0.1 — Agente `[LK] Estoque Loja Física` (`lk-stock`)

Criado em: 2026-06-08T15:03:39Z
Status: **Gate B runtime real ativado; Gate C operacional read-only em preview de aprovação desde 2026-06-08T19:39:31Z**

## 1. Problema

A LK precisa transformar dados de venda/demanda em disponibilidade real na loja física. O risco atual é vender bem online, receber procura ou tráfego para produtos fortes, mas não ter os tamanhos/modelos certos à pronta entrega no ponto físico.

## 2. Objetivo

Criar um agente especialista responsável por controlar e priorizar estoque físico da loja, garantindo que best sellers e produtos de maior chance de conversão estejam disponíveis à pronta entrega, com decisões baseadas em fonte viva e sem ações externas automáticas.

## 3. Resultado esperado

O agente deve produzir uma fila acionável do tipo:

- produto/modelo;
- SKU/variante/tamanho;
- estoque Tiny atual por loja/depósito quando disponível;
- vendas recentes e velocidade de giro;
- demanda latente: pedidos, buscas, campanhas, influencers, tendência;
- risco de ruptura;
- recomendação: manter, repor, transferir, comprar, investigar SKU, ou não agir;
- aprovação necessária e próximo dono.

## 4. Escopo v1

Incluído:

1. Score de best seller/pronta entrega por produto-variante-tamanho.
2. Monitoramento read-only de ruptura/baixo estoque de itens com demanda.
3. Fila de ação para Lucas/Júlio/operação: repor, transferir, comprar, sanear SKU.
4. Handoff para `lk-ops`, `lk-shopify`, `lk-growth` e `lk-trends` conforme causa.
5. Receipts no Brain para decisões, bloqueios e pacotes.

Fora do v1:

- compra automática;
- contato automático com fornecedor;
- alteração de Tiny/Shopify;
- reserva/promessa de disponibilidade ao cliente;
- cron Telegram ruidoso;
- campanhas/WhatsApp/Klaviyo automáticos.

## 5. Fontes e hierarquia

1. Tiny `LK | CONTROLE ESTOQUE` — estoque e disponibilidade final.
2. Shopify orders/order_items — venda, produto, variante/SKU, tamanho.
3. Shopify catalog — contexto de handle/título/variant, não estoque final.
4. GA4/GSC/Meta/Klaviyo/Judge.me — sinais de demanda e conversão.
5. LK Trends/Growth — tendência, hype, oportunidades, tráfego/influencer.
6. Evidência humana — Lucas/Júlio/operação, quando fonte viva está incompleta.

## 6. Score v0

Score total 0–100:

- 30 pts: vendas líquidas recentes por SKU/tamanho, janela 7/30/90 dias.
- 20 pts: margem/valor comercial estimado, quando disponível.
- 15 pts: procura/tráfego/sinal de campanha/influencer.
- 15 pts: risco de ruptura na loja física segundo Tiny.
- 10 pts: recorrência histórica do modelo/família.
- 10 pts: confiança de dados SKU↔Tiny↔Shopify.

Faixas:

- P0: 80–100 — precisa decisão rápida; risco alto de venda perdida.
- P1: 60–79 — revisar/repor se viável.
- P2: 40–59 — monitorar ou validar dados.
- P3: <40 — não agir por enquanto.

## 7. Guardrails

- Regra operacional corrigida por Lucas em 2026-06-10T17:32:11Z: confirmar primeiro pela **nossa database Stock OS** (`lk_stock_os_current_pointer.json` / DB apontada), porque ela é a superfície operacional canônica de consulta construída a partir de Tiny/Shopify read-only com identidade, estoque observado e freshness.
- Tiny / `LK | CONTROLE ESTOQUE` continua sendo a fonte primária que alimenta e valida a database. Shopify stock nunca é resposta final.
- Toda disponibilidade deve ser variante/tamanho-level.
- Se a database estiver stale, sem SKU resolvido, sem observação de estoque, com duplicidade/bloqueio ou sem freshness suficiente, resposta deve ser “não confirmado” até consultar Tiny/fonte viva; não chute.
- Writes em Tiny/Shopify/fornecedor/campanha exigem aprovação escopada, snapshot/readback/rollback quando aplicável.
- Telegram para Lucas: só decisão/alerta acionável; OK silencioso.
- IMBOX/Inbox não entra no COO/rotina deste agente salvo pedido explícito.

## 8. Autonomia

Autônomo:

- ler Brain/local docs;
- preparar perfil/local docs;
- gerar score/fila read-only;
- criar approval packet/receipt/handoff;
- apontar dados ausentes.

Bloqueado sem aprovação:

- ativar gateway/bot/cron;
- criar webhooks;
- consultar/escrever APIs externas se envolver credenciais sensíveis sem caminho Doppler aprovado;
- alterar estoque/preço/produto/tema/campanha;
- contato externo/fornecedor/cliente.

## 9. Handoffs

- Para `lk-ops`: executar/validar processo físico, Tiny, loja, Júlio.
- Para `lk-shopify`: resolver SKU/variant/catalog/readback e event-trigger Shopify.
- Para `lk-growth`: demanda, tráfego, GMC, CRO, performance.
- Para `lk-trends`: sourcing e tendência.
- Para Lucas: somente decisão com trade-off claro.

## 10. Modo de trabalho gradual aprovado para desenho

Lucas escolheu o caminho **sistema completo gradual**, com evolução em etapas e gate explícito antes de cada ativação:

1. **Manual read-only** — o agente trabalha quando chamado por Lucas ou por outro especialista. Ele consulta fonte viva autorizada, cruza demanda/venda/estoque, monta fila ou packet, mas não roda sozinho.
2. **Base local read-only + sync live/diário** — após aprovação separada, o agente passa a ter um índice local de estoque/demanda, atualizado por webhook live e reconciliado por cron diário. A base acelera decisão, mas não substitui Tiny como fonte final.
3. **Rotina read-only silent-OK** — após aprovação separada, o agente roda checagem periódica sobre a base local e só alerta Lucas quando houver P0, falha de fonte, divergência SKU crítica ou aprovação necessária. OK benigno fica silencioso.
4. **Bot/perfil dedicado Telegram** — após aprovação separada, o perfil `lk-stock` pode ficar conversável para perguntas e decisões de estoque, ainda sem promessa de disponibilidade sem Tiny e sem writes externos automáticos.
5. **Sistema completo operacional** — somente depois dos gates anteriores estarem estáveis, o agente vira fila contínua de decisão: detecta demanda, atualiza/consulta base local, confirma Tiny/fonte viva, classifica P0/P1/P2/P3, cria approval packets, faz handoff e registra receipts.

Cada etapa deve terminar com evidência real: fonte consultada, output gerado, logs/receipts, writes externos executados `0` salvo aprovação escopada, e próximo gate claro.

## 11. Contrato operacional — como o agente deve trabalhar

### 11.1 Loop padrão

1. Receber sinal: pergunta de Lucas, venda recente, demanda Growth/Trends/CRM, campanha, item buscado ou suspeita de ruptura.
2. Resolver identidade do item: produto, handle, variant, SKU, tamanho e código Tiny.
3. Consultar Tiny ou fonte viva equivalente antes de afirmar disponibilidade.
4. Cruzar com vendas 7/30/90, margem/valor quando disponível, demanda externa e histórico da família.
5. Classificar prioridade P0/P1/P2/P3.
6. Gerar output no formato certo:
   - resposta curta se for pergunta simples;
   - fila priorizada se houver vários itens;
   - packet de ação se precisar aprovação;
   - handoff se o dono for `lk-ops`, `lk-shopify`, `lk-growth` ou `lk-trends`.
7. Registrar receipt quando houver decisão material, bloqueio, lacuna de fonte, aprovação ou write aprovado.

### 11.2 Regras de resposta

- Se não consultou Tiny/fonte viva, não afirma disponibilidade.
- Se SKU↔Tiny não está confiável, a recomendação vira saneamento de SKU antes de compra/reposição.
- Se o caso exige compra, transferência, reserva, campanha, Shopify/Tiny write, fornecedor ou contato com cliente, produzir preview/packet e aguardar aprovação.
- Telegram para Lucas deve ser limpo: apenas decisão acionável, P0, falha de fonte ou aprovação necessária.
- Nada de alerta de “OK” recorrente, fallback benigno ou recuperação automática sem impacto.

### 11.3 Saídas canônicas

1. **Resposta de disponibilidade:** produto/tamanho, fonte consultada, status confirmado ou não confirmado, próximo passo seguro.
2. **Fila P0/P1:** ranking com SKU/tamanho, Tiny, evidência de demanda, risco, recomendação e dono.
3. **Packet de ação:** ação proposta, quantidade/limite, fonte, risco, aprovação textual necessária e verificação/readback.
4. **Receipt/handoff:** o que foi decidido, por quem, fonte, writes externos, próximo dono e pendências.

### 11.4 Base local operacional com sync vivo

Para o agente trabalhar rápido sem depender de varrer APIs inteiras a cada pergunta, o sistema deve evoluir para uma **base local read-only de estoque/demanda**, alimentada por duas vias complementares:

1. **Sync live via webhook** — eventos Shopify/Tiny/fonte autorizada atualizam a base local quando houver venda, alteração de produto/variante, alteração de estoque ou evento relevante de demanda.
2. **Sync diário via cron** — uma rotina diária reconcilia a base local contra as fontes vivas, corrige eventos perdidos, recalcula score e gera evidência local.

Contrato da base local:

- A base local é **cache operacional/índice de decisão**, não fonte final de disponibilidade.
- Tiny / `LK | CONTROLE ESTOQUE` continua sendo a fonte final para afirmar estoque e ruptura.
- Webhook e cron podem atualizar cache e score, mas não executam compra, reserva, contato externo, campanha, Tiny/Shopify write ou promessa ao cliente.
- Se webhook falhar ou ficar atrasado, o cron diário deve reconciliar e registrar lacuna.
- Se cron falhar, o agente deve marcar a base como stale e consultar fonte viva antes de responder.
- Toda resposta material deve declarar freshness: `live`, `cron diário`, `stale` ou `fonte viva consultada agora`.

Campos mínimos da base local:

- produto, handle, variant, SKU, tamanho, código Tiny;
- estoque por fonte/loja/depósito quando disponível;
- timestamp da última atualização por fonte;
- vendas 7/30/90 por SKU/tamanho;
- sinais Growth/Trends/campanha/demanda humana;
- confiança SKU↔Tiny↔Shopify;
- score P0/P1/P2/P3/needs_sku_resolution;
- ledger de eventos, reconciliações, falhas e receipts.

Ativação de webhook/cron/base produtiva exige gate próprio e aprovação escopada. Documentar no PRD não ativa runtime.

### 11.5 Arquitetura mínima da base local — Gate B

O Gate B deve ser implementado como uma base local simples, auditável e reversível, preferencialmente SQLite ou equivalente local, com schema versionado no Brain antes de qualquer runtime.

Entidades mínimas:

1. **products** — produto/handle/título/marca/família/status comercial.
2. **variants** — variant, SKU, tamanho, código Tiny, confiança de mapeamento.
3. **stock_snapshots** — estoque por SKU/tamanho/fonte/loja/depósito/timestamp/freshness.
4. **sales_velocity** — vendas líquidas 7/30/90 por SKU/tamanho, com fonte e janela.
5. **demand_signals** — Growth/Trends/campanha/loja/operação, com peso, validade e origem.
6. **scores** — P0/P1/P2/P3/needs_sku_resolution por SKU/tamanho, com explicação.
7. **event_ledger** — eventos webhook, cron, backfill, erro, reconciliação e idempotência.
8. **receipts** — outputs materiais, decisões, aprovações e handoffs.

Fluxos mínimos:

- **Backfill inicial read-only:** popula catálogo, variantes, vendas recentes e snapshot de estoque autorizado.
- **Webhook live:** recebe evento assinado, valida origem, normaliza payload, grava event ledger, atualiza entidades afetadas e marca freshness `live`.
- **Cron diário:** reconcilia catálogo/vendas/estoque contra fontes vivas, recalcula scores, detecta eventos perdidos, marca freshness `cron diário` ou `stale`.
- **Consulta do agente:** lê base local para formar candidatos e contexto; confirma Tiny/fonte viva quando a resposta afirmar disponibilidade, ruptura ou recomendação P0/P1.

Regras de segurança da arquitetura:

- Webhook público canônico deve usar `hermes-webhooks` no Vercel quando houver provedor externo, com validação HMAC do provedor e resign para Hermes quando aplicável.
- Secrets ficam em Doppler/ambiente autorizado; PRD/Brain registram nomes/contratos, nunca valores.
- Idempotência obrigatória por `provider`, `event_id` ou hash do payload normalizado.
- Toda mutação da base local precisa ser appendável/auditável no ledger.
- Sem write externo a partir da base local.

Template/schema canônico do Gate B:

- `areas/lk/sub-areas/stock/templates/base-local-gate-b-schema.md`

Plano de implementação local/dry-run do Gate B:

- `areas/lk/sub-areas/stock/plans/gate-b-base-local-implementation-plan.md`

Implementação local/offline/dry-run iniciada após aprovação de Lucas:

- Scripts: `areas/lk/sub-areas/stock/scripts/`
- Testes offline: `areas/lk/sub-areas/stock/evaluation/`
- Fixtures: `areas/lk/sub-areas/stock/fixtures/`
- Runbook de verificação: `areas/lk/sub-areas/stock/evaluation/gate-b-local-verification-runbook.md`
- Preview de aprovação runtime futuro: `areas/lk/sub-areas/stock/approval-packets/gate-b-runtime-activation-preview.md`
- Decision packet de runtime real: `areas/lk/sub-areas/stock/approval-packets/gate-b-runtime-decision-20260608T175817Z.md`
- Receipt: `areas/lk/sub-areas/stock/receipts/lk-stock-gate-b-local-implementation-20260608T173403Z.md`

O plano/implementação local não autorizava runtime. Em 2026-06-08T17:58:17Z, o Gate B local foi revalidado com 11 testes offline `OK`. Em 2026-06-08T19:29:25Z, após aprovação do Lucas, o runtime real do Gate B foi ativado em escopo read-only: rotas `lk-stock-shopify-order-paid`, `lk-stock-shopify-product-update` e `lk-stock-tiny-stock-snapshot` via `hermes-webhooks`/Vercel para o Hermes Gateway público; cron diário no profile `lk-stock` (`e8b35e20751b`, 11:15 UTC); base local `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite`; HMAC/resign/idempotência; Telegram silent-OK; writes externos `0`. Receipt: `areas/lk/sub-areas/stock/receipts/lk-stock-gate-b-runtime-activation-20260608T192925Z.md`.

Gate B.2 — crosswalk local Tiny↔Shopify do catálogo ativo: em 2026-06-10T10:48:42Z, os 90 shards SQLite locais foram consolidados em packet de saneamento, sem ativar runtime novo e sem write externo. Evidência: 1.647 prefixos, 12.645 linhas de crosswalk, 11.740 liberadas localmente para decisão interna e 905 bloqueadas para saneamento (`shopify_variant_tiny_missing`, `shopify_duplicate_sku_blocked`, `tiny_duplicate_exact_code_blocked`, `matched_exact_sku_stock_missing_deposit`). Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-consolidado-20260610T104842Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-issues-20260610T104842Z.csv` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-sku-saneamento-decision-packet-20260610T104842Z.md`. Próximo passo continua sendo aprovação escopada para fila P0/P1 de saneamento, não write Tiny/Shopify nem cron/webhook/runtime novo.

Em 2026-06-10T10:59:00Z, após aprovação de Lucas, foi preparada a fila local/read-only P0/P1 de saneamento Gate B2: 905 issues SKU/tamanho, 558 handles com bloqueio, 9 `P0_saneamento`, 141 `P1_saneamento` e 408 `P2_saneamento`. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-fila-p0p1-20260610T105900Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-fila-p0p1-20260610T105900Z.csv` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-sku-saneamento-fila-p0p1-preview-20260610T105900Z.md`. Esta fila é prioridade de saneamento, não autorização para write Tiny/Shopify, compra, transferência, promessa de disponibilidade ou runtime novo.

Em 2026-06-10T11:24:21Z, após Lucas responder `Seguir`, foi preparado o preview do lote P0 completo de saneamento, ainda local/read-only: 9 handles P0, 84 linhas SKU/tamanho bloqueadas (`shopify_duplicate_sku_blocked`: 66, `tiny_duplicate_exact_code_blocked`: 11, `shopify_variant_tiny_missing`: 7). Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-p0-batch-packet-20260610T112421Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-p0-batch-issues-20260610T112421Z.csv` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-sku-saneamento-p0-batch-preview-20260610T112421Z.md`. Próximo gate seguro: aprovação escopada para investigação read-only ao vivo Shopify/Tiny dos 9 handles P0, ou escolha de um único handle piloto; nenhum write externo/runtime foi autorizado.

Em 2026-06-10T11:30:47Z, após Lucas responder novo `Seguir`, foi executada investigação live read-only Shopify/Tiny dos 9 handles P0. Resultado: 74 linhas avaliadas; 58 `shopify_duplicate_sku_blocked`, 6 `shopify_variant_tiny_missing`, 4 `tiny_duplicate_exact_code_blocked` e 6 `matched_exact_sku_stock_resolved` com depósito Tiny oficial confirmado (todos com saldo `0.0`). Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-live-readonly-investigation-decision-20260610T113047Z.md`. Próximo gate: packet de correção por handle ou registro local dos 6 matches resolvidos; Tiny/Shopify write e disponibilidade pública continuam bloqueados sem aprovação escopada.

Em 2026-06-10T11:45:00Z, após pedido de preparar todos os packets de correções de forma automática, foram gerados 9 correction packets por handle P0, índice consolidado e CSV de propostas a partir da investigação live read-only. Resultado: 6 packets lane `SHOPIFY_DUPLICATE_PACKET`, 2 lane `TINY_DUPLICATE_PACKET`, 1 lane `LOCAL_CACHE_RESOLVED_ZERO_STOCK`; 74 linhas propostas. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-p0-correction-packets-index-20260610T114500Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-p0-correction-proposals-20260610T114500Z.csv`, `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-index-20260610T114500Z.md` e diretório `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-20260610T114500Z/`. Execução externa permaneceu bloqueada: `Tiny write 0`, `Shopify write 0`, `runtime novo 0`.

Em 2026-06-10T11:44:37Z, Lucas escolheu opção `A`; foram aplicados localmente/cache os 6 matches exatos resolvidos do P0 em SQLite novo `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.db`, com backup `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.before_apply.bak`. Linhas cacheadas: `FQ8138-600-45`, `FQ8138-600-46`, `CW1588601-4`, `IH2612-12`, `IH2612-1`, `IH2612-13`; todas com saldo Tiny `LK | CONTROLE ESTOQUE` observado como `0`. Gate C manual pós-apply retornou `ok_silent`/0 alertas. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-p0-resolved-local-cache-apply-20260610T114437Z.json` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-resolved-local-cache-apply-20260610T114437Z.md`. Tiny/Shopify write, cliente/fornecedor e runtime novo permaneceram `0`.

Em 2026-06-10T12:09:20Z, após Lucas confirmar a regra operacional “corrigir local/cache e não mexer em Shopify/Tiny por padrão”, foi criada uma camada local consultável P0 Shopify↔Tiny↔estoque para organizar o que é cada SKU/tamanho e permitir consulta futura segura. Resultado: 74 linhas, 9 handles, 6 linhas `CONSULTABLE_LOCAL_RESOLVED`, 58 `BLOCKED_SHOPIFY_DUPLICATE`, 4 `BLOCKED_TINY_DUPLICATE` e 6 `BLOCKED_TINY_MISSING`; `public_availability_safe_rows: 0` e `writes_externos: 0`. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-p0-consultable-crosswalk-20260610T120920Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-p0-consultable-crosswalk-20260610T120920Z.csv`, `areas/lk/sub-areas/stock/data/gate_b2_p0_consultable_crosswalk_20260610T120920Z.db` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-consultable-crosswalk-20260610T120920Z.md`. Tiny e Shopify permaneceram read-only/intactos.

Em 2026-06-10T12:17:16Z, após novo `Seguir`, a camada consultável foi ampliada para todos os bloqueios Gate B2 P0/P1/P2, ainda local/cache: 905 linhas de issues, 558 handles, prioridades `P0_saneamento: 9`, `P1_saneamento: 141`, `P2_saneamento: 408`; lanes `BLOCKED_TINY_MISSING: 459`, `BLOCKED_SHOPIFY_DUPLICATE: 293`, `BLOCKED_TINY_DUPLICATE: 96`, `BLOCKED_TINY_DEPOSIT_MISSING: 57`. `public_availability_safe_rows: 0` e `writes_externos: 0`. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-full-consultable-crosswalk-20260610T121716Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-full-consultable-crosswalk-20260610T121716Z.csv`, `areas/lk/sub-areas/stock/data/gate_b2_full_consultable_crosswalk_20260610T121716Z.db` e `areas/lk/sub-areas/stock/approval-packets/gate-b2-full-consultable-crosswalk-20260610T121716Z.md`. Tiny/Shopify permaneceram intactos; próxima ação padrão é detalhar/localizar correções local/cache por lane e prioridade, sem write externo.

Em 2026-06-10T12:36:35Z, Lucas pediu “Seguir todos em sequência, só pare quando acabar”. Interpretação segura aplicada: processar todas as lanes como fila local/cache consultável, sem write Tiny/Shopify. Foram gerados artefatos sequenciais para as 905 linhas: ordem `BLOCKED_TINY_MISSING` (459), `BLOCKED_SHOPIFY_DUPLICATE` (293), `BLOCKED_TINY_DUPLICATE` (96), `BLOCKED_TINY_DEPOSIT_MISSING` (57). Foram criados JSON/CSV/SQLite e packets por lane em `areas/lk/sub-areas/stock/approval-packets/gate-b2-all-lanes-local-work-queue-20260610T123635Z/`; arquivo índice `areas/lk/sub-areas/stock/approval-packets/gate-b2-all-lanes-local-work-queue-20260610T123635Z.md`; dados `areas/lk/sub-areas/stock/reports/gate-b2-all-lanes-local-work-queue-20260610T123635Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-all-lanes-local-work-queue-20260610T123635Z.csv` e SQLite `areas/lk/sub-areas/stock/data/gate_b2_all_lanes_local_work_queue_20260610T123635Z.db`. `Tiny write: 0`, `Shopify write: 0`, `public_availability_safe_rows: 0`, cron/runtime/webhook/bot/gateway novo: `0`.

Em 2026-06-10T12:45:19Z, após novo `seguir`, foram gerados packets locais individuais para todos os 558 handles bloqueados Gate B2, um `.json` e um `.md` por handle, a partir da fila sequencial local/cache. Resultado: 1.116 arquivos no diretório `areas/lk/sub-areas/stock/approval-packets/gate-b2-handle-local-packets-20260610T124519Z/`; índice JSON `areas/lk/sub-areas/stock/reports/gate-b2-handle-local-packets-index-20260610T124519Z.json`; índice CSV `areas/lk/sub-areas/stock/reports/gate-b2-handle-local-packets-index-20260610T124519Z.csv`; índice MD `areas/lk/sub-areas/stock/approval-packets/gate-b2-handle-local-packets-index-20260610T124519Z.md`. Contagem por lane principal dos handles: `BLOCKED_TINY_MISSING: 332`, `BLOCKED_SHOPIFY_DUPLICATE: 183`, `BLOCKED_TINY_DUPLICATE: 35`, `BLOCKED_TINY_DEPOSIT_MISSING: 8`. Tiny/Shopify permaneceram intactos; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T12:53:35Z, após novo `seguir`, foi criada uma camada de lookup local rápido para consulta futura por SKU, handle, título, código Tiny ou tipo de issue, apontando para o packet local correto. Artefatos: SQLite FTS `areas/lk/sub-areas/stock/data/gate_b2_lookup_index_20260610T125335Z.db`; JSON `areas/lk/sub-areas/stock/reports/gate-b2-lookup-index-20260610T125335Z.json`; CSV `areas/lk/sub-areas/stock/reports/gate-b2-lookup-index-20260610T125335Z.csv`; índice MD `areas/lk/sub-areas/stock/approval-packets/gate-b2-lookup-index-20260610T125335Z.md`; script `areas/lk/sub-areas/stock/scripts/gate_b2_lookup_local_crosswalk.py`. Totais: 911 linhas indexadas (905 bloqueios + 6 resolvidos P0 cache local), 903 SKUs únicos, 558 handles, FTS habilitado. Tiny/Shopify write: `0`; disponibilidade pública: `0`.

Em 2026-06-10T13:06:44Z, após novo `Seguir`, foi criada a visão canônica local atual por SKU+handle para resolver conflito entre histórico bloqueado e match resolvido. Resultado: 903 linhas canônicas a partir de 911 linhas de lookup, com 8 estados antigos marcados como superseded e preservados para auditoria. Status canônico: `CONSULTABLE_LOCAL_RESOLVED: 6`, `BLOCKED_TINY_MISSING: 457`, `BLOCKED_TINY_DUPLICATE: 96`, `BLOCKED_SHOPIFY_DUPLICATE: 287`, `BLOCKED_TINY_DEPOSIT_MISSING: 57`. Artefatos: SQLite `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`; JSON `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json`; CSV `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.csv`; índice MD `areas/lk/sub-areas/stock/approval-packets/gate-b2-canonical-current-index-20260610T130644Z.md`; script `areas/lk/sub-areas/stock/scripts/gate_b2_lookup_canonical_current.py`. Tiny/Shopify write: `0`; disponibilidade pública: `0`.

Em 2026-06-10T13:26:30Z, após novo `seguir`, a visão canônica foi promovida a superfície estável de consulta interna, sem runtime novo e sem depender de timestamp no uso diário. Em 2026-06-10T13:38:14Z, após novo `seguir`, a superfície foi revalidada/atualizada de forma idempotente. Criados/atualizados: pointer `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`; wrapper estável `areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py`; guia operacional `areas/lk/sub-areas/stock/references/gate-b2-current-lookup-operational-guide-20260610.md`; packet inicial `areas/lk/sub-areas/stock/approval-packets/gate-b2-stable-current-lookup-surface-20260610T132630Z.md`; packet refresh `areas/lk/sub-areas/stock/approval-packets/gate-b2-stable-current-lookup-surface-refresh-20260610T133814Z.md`. Uso padrão: `python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py <query> --limit 10`. Pointer aponta para `gate_b2_canonical_current_index_20260610T130644Z.db` com 903 linhas canônicas e 8 superseded. A consulta continua local/cache only; Tiny/Shopify write: `0`; runtime novo: `0`; disponibilidade pública/pronta entrega: `0`; disponibilidade final exige Tiny/fonte viva no momento.

Em 2026-06-10T13:43:07Z, após novo `seguir`, foi criado o QA pack da superfície estável. Novo checker: `areas/lk/sub-areas/stock/scripts/lk_stock_current_surface_check.py`. Ele valida pointer/artefatos, contagens do DB contra pointer, status/prioridades, guardrails zerados e amostra determinística por status/prioridade. Evidências geradas: JSON `areas/lk/sub-areas/stock/reports/gate-b2-current-lookup-surface-qa-20260610T134307Z.json`; CSV amostra `areas/lk/sub-areas/stock/reports/gate-b2-current-lookup-surface-qa-sample-20260610T134307Z.csv`; MD `areas/lk/sub-areas/stock/approval-packets/gate-b2-current-lookup-surface-qa-20260610T134307Z.md`. Resultado do checker: `ok: True`; linhas canônicas `903`; superseded `8`; amostra `20`; guardrails `tiny_write=0`, `shopify_write=0`, `writes_externos=0`, `public_availability_safe=0`.

Em 2026-06-10T13:47:34Z, após novo `seguir`, foi criada a worklist operacional local da consulta atual por handle/lane/prioridade, para transformar a superfície canônica em fila humana/local de próximos passos. Resultado: 694 linhas de worklist, 691 bloqueadas para cleanup e 3 resolvidas como referência; fonte: 903 SKUs canônicos, sendo 897 bloqueados e 6 resolvidos. Ações recomendadas: `READONLY_TINY_CODE_INVESTIGATION: 345`, `SHOPIFY_DUPLICATE_PROPOSAL: 207`, `TINY_DUPLICATE_PROPOSAL: 82`, `TINY_DEPOSIT_MAPPING_CHECK: 57`, `NO_WRITE_RESOLVED_CACHE: 3`. Artefatos: JSON `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.json`; CSV `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.csv`; packet `areas/lk/sub-areas/stock/approval-packets/gate-b2-current-operator-worklist-20260610T134734Z.md`; guia `areas/lk/sub-areas/stock/references/gate-b2-current-operator-worklist-guide-20260610.md`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T13:55:30Z, Lucas pediu “seguir... vamos fazer o P0, usando sub agentes, ate acabar ok? faca tudo e depois me avise”. Interpretação segura aplicada: concluir todo P0 da worklist com workers locais paralelos/subagentes temporários, em live read-only Shopify/Tiny, e depois gerar correction packets locais sem executar writes. Cobertura: 18 linhas P0 da worklist, 9 handles, 13 prefixes, 150 linhas crosswalk live/read-only. Status: `shopify_duplicate_sku_blocked: 99`, `matched_exact_sku_stock_resolved: 27`, `shopify_variant_tiny_missing: 12`, `tiny_duplicate_exact_code_blocked: 11`, `matched_exact_sku_stock_missing_deposit: 1`. Packets de correção gerados para todos os 9 handles P0: `SHOPIFY_DUPLICATE_PACKET: 6`, `TINY_DUPLICATE_PACKET: 3`; 150 linhas de propostas. Artefatos: agregado JSON `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-all-20260610T135530Z.json`; agregado CSV `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-all-20260610T135530Z.csv`; packet live `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-live-readonly-all-20260610T135530Z.md`; índice de correction packets `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-index-20260610T135530Z.md`; propostas CSV `areas/lk/sub-areas/stock/reports/gate-b2-p0-correction-proposals-20260610T135530Z.csv`; packets individuais em `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-20260610T135530Z/`; orquestrador local `areas/lk/sub-areas/stock/scripts/gate_b2_p0_live_worker_orchestrator.py`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T14:07:28Z, Lucas pediu “agora, seguir para os proximos”. Interpretação segura aplicada: concluir a próxima prioridade após P0, isto é P1_saneamento inteiro, usando workers locais paralelos/subagentes temporários em live read-only Shopify/Tiny, sem write Tiny/Shopify e sem promessa pública. Cobertura: 251 linhas P1 da worklist, 141 handles, 146 prefixes, 1690 linhas crosswalk live/read-only. Status: `matched_exact_sku_stock_resolved: 1027`, `shopify_variant_tiny_missing: 474`, `shopify_duplicate_sku_blocked: 76`, `tiny_duplicate_exact_code_blocked: 67`, `matched_exact_sku_stock_missing_deposit: 46`. Packets de correção gerados para todos os 141 handles P1: `TINY_DUPLICATE_PACKET: 44`, `TINY_CODE_INVESTIGATION_PACKET: 42`, `SHOPIFY_DUPLICATE_PACKET: 35`, `TINY_DEPOSIT_PACKET: 14`, `LOCAL_RESOLVED_REFERENCE_PACKET: 6`; 1690 linhas de propostas. Artefatos: agregado JSON `areas/lk/sub-areas/stock/reports/gate-b2-p1-live-readonly-all-20260610T140728Z.json`; agregado CSV `areas/lk/sub-areas/stock/reports/gate-b2-p1-live-readonly-all-20260610T140728Z.csv`; packet live `areas/lk/sub-areas/stock/approval-packets/gate-b2-p1-live-readonly-all-20260610T140728Z.md`; índice de correction packets `areas/lk/sub-areas/stock/approval-packets/gate-b2-p1-correction-packets-index-20260610T140728Z.md`; propostas CSV `areas/lk/sub-areas/stock/reports/gate-b2-p1-correction-proposals-20260610T140728Z.csv`; packets individuais em `areas/lk/sub-areas/stock/approval-packets/gate-b2-p1-correction-packets-20260610T140728Z/`; orquestrador local generalizado `areas/lk/sub-areas/stock/scripts/gate_b2_priority_live_worker_orchestrator.py`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T14:42:45Z, Lucas pediu “FAZER O P2 ATE ACABAR POR FAVOR”. Interpretação segura aplicada: concluir todo `P2_saneamento`, usando workers locais paralelos/subagentes temporários em live read-only Shopify/Tiny, sem write Tiny/Shopify e sem promessa pública. Cobertura: 425 linhas P2 da worklist, 408 handles, 410 prefixes, 6493 linhas crosswalk live/read-only. Status: `matched_exact_sku_stock_resolved: 3412`, `shopify_variant_tiny_missing: 2606`, `shopify_duplicate_sku_blocked: 236`, `matched_exact_sku_stock_missing_deposit: 225`, `tiny_duplicate_exact_code_blocked: 14`. Packets de correção gerados para todos os 408 handles P2: `SHOPIFY_DUPLICATE_PACKET: 184`, `TINY_CODE_INVESTIGATION_PACKET: 123`, `TINY_DEPOSIT_PACKET: 91`, `TINY_DUPLICATE_PACKET: 7`, `LOCAL_RESOLVED_REFERENCE_PACKET: 3`; 6493 linhas de propostas. Artefatos: agregado JSON `areas/lk/sub-areas/stock/reports/gate-b2-p2-live-readonly-all-20260610T144245Z.json`; agregado CSV `areas/lk/sub-areas/stock/reports/gate-b2-p2-live-readonly-all-20260610T144245Z.csv`; packet live `areas/lk/sub-areas/stock/approval-packets/gate-b2-p2-live-readonly-all-20260610T144245Z.md`; índice de correction packets `areas/lk/sub-areas/stock/approval-packets/gate-b2-p2-correction-packets-index-20260610T144245Z.md`; propostas CSV `areas/lk/sub-areas/stock/reports/gate-b2-p2-correction-proposals-20260610T144245Z.csv`; packets individuais em `areas/lk/sub-areas/stock/approval-packets/gate-b2-p2-correction-packets-20260610T144245Z/`; orquestrador local generalizado `areas/lk/sub-areas/stock/scripts/gate_b2_priority_live_worker_orchestrator.py`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T16:10:41Z, Lucas pediu um “Stock OS PRD checkpoint”. Foi criado checkpoint executivo/governança do PRD confirmando que o Stock OS está saudável no estágio atual: Gate B/B2 read-only completo, P0/P1/P2 investigados e packetizados, superfície canônica validada e guardrails sem write externo. Totais consolidados: 694 linhas de worklist concluídas, 558 handles, 8.333 linhas crosswalk live/read-only, 558 packets e 8.333 propostas. Achados consolidados: `matched_exact_sku_stock_resolved: 4466`, `shopify_variant_tiny_missing: 3092`, `shopify_duplicate_sku_blocked: 411`, `matched_exact_sku_stock_missing_deposit: 272`, `tiny_duplicate_exact_code_blocked: 92`. Verification: 20 tests OK, surface checker `ok: True`, lookup smoke `CW1588601-4` OK, cron registry com apenas o cron read-only existente. Artefatos: `areas/lk/sub-areas/stock/approval-packets/stock-os-prd-checkpoint-20260610T161041Z.md` e `areas/lk/sub-areas/stock/reports/stock-os-prd-checkpoint-20260610T161041Z.json`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T16:22:41Z, após Lucas pedir “Seguir o master register”, foi consolidado o Master Register Gate B2 P0+P1+P2 por `priority + lane + handle`, com detalhe por proposta/SKU em CSV e SQLite local. Resultado: 558 linhas master, 558 handles, 8.333 linhas detalhadas de proposta, lanes `SHOPIFY_DUPLICATE_PACKET: 225`, `TINY_CODE_INVESTIGATION_PACKET: 165`, `TINY_DEPOSIT_PACKET: 105`, `TINY_DUPLICATE_PACKET: 54`, `LOCAL_RESOLVED_REFERENCE_PACKET: 9`. Status detalhado preservado: `matched_exact_sku_stock_resolved: 4466`, `shopify_variant_tiny_missing: 3092`, `shopify_duplicate_sku_blocked: 411`, `matched_exact_sku_stock_missing_deposit: 272`, `tiny_duplicate_exact_code_blocked: 92`. Artefatos: `areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.json`, `areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.csv`, `areas/lk/sub-areas/stock/reports/gate-b2-master-register-proposals-20260610T162241Z.csv`, SQLite `areas/lk/sub-areas/stock/data/gate_b2_master_register_20260610T162241Z.db` e packet `areas/lk/sub-areas/stock/approval-packets/gate-b2-master-register-20260610T162241Z.md`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T16:55:23Z, após Lucas pedir para fazer tudo em sequência e avisar só no fim, foi criada a DB unificada local/read-only `LK Stock OS current` (Gate B3), juntando a visão canônica Gate B2, Master Register, observações de estoque lidas nos batches P0/P1/P2 e metadados da DB runtime Gate B. Resultado: tabela `current_local_stock` com 903 linhas por SKU+handle, tabela `stock_observations` com 8.333 observações/propostas, `master_register` com 558 linhas e pointer estável `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`. Estoque observado no current: 316 linhas com alguma observação, 18 com estoque positivo observado, 298 com estoque zero observado; identidade local resolvida segura: 6; bloqueadas/não resolvidas: 897; disponibilidade pública segura: 0. Artefatos: SQLite `areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db`, JSON `areas/lk/sub-areas/stock/reports/lk-stock-os-current-20260610T165523Z.json`, CSV `areas/lk/sub-areas/stock/reports/lk-stock-os-current-20260610T165523Z.csv`, packet `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-current-20260610T165523Z.md`, guia `areas/lk/sub-areas/stock/references/lk-stock-os-current-db-guide-20260610.md` e script `areas/lk/sub-areas/stock/scripts/gate_b3_build_unified_local_stock_db.py`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`.

Em 2026-06-10T17:21:39Z, Lucas pediu para fazer primeiro a resolução dos bloqueios de identidade SKU/Tiny/Shopify usando subagentes. Foi criado um overlay local/read-only com workers por lane (`BLOCKED_TINY_MISSING`, `BLOCKED_TINY_DEPOSIT_MISSING`, `BLOCKED_TINY_DUPLICATE`, `BLOCKED_SHOPIFY_DUPLICATE`) sobre a DB Gate B3. Regra aplicada: resolver localmente apenas SKU+handle com evidência exata `matched_exact_sku_stock_resolved` e sem duplicidade exata Shopify/Tiny; manter bloqueadas as duplicidades e faltas de código/depósito. Resultado: 164 novas linhas resolvidas localmente (`BLOCKED_TINY_MISSING`: 123; `BLOCKED_TINY_DEPOSIT_MISSING`: 41), elevando `identity_resolved_safe` de 6 para 170. Status após overlay: `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH: 164`, `CONSULTABLE_LOCAL_RESOLVED: 6`, `BLOCKED_TINY_MISSING: 334`, `BLOCKED_SHOPIFY_DUPLICATE: 287`, `BLOCKED_TINY_DUPLICATE: 96`, `BLOCKED_TINY_DEPOSIT_MISSING: 16`. Artefatos: SQLite `areas/lk/sub-areas/stock/data/lk_stock_os_current_identity_resolved_20260610T172139Z.db`, JSON `areas/lk/sub-areas/stock/reports/lk-stock-os-identity-resolution-20260610T172139Z.json`, CSV `areas/lk/sub-areas/stock/reports/lk-stock-os-identity-resolution-20260610T172139Z.csv`, packet `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-identity-resolution-20260610T172139Z.md`, guia `areas/lk/sub-areas/stock/references/lk-stock-os-identity-resolution-guide-20260610.md`, script `areas/lk/sub-areas/stock/scripts/gate_b3_resolve_identity_local_overlay.py` e consulta `areas/lk/sub-areas/stock/scripts/lk_stock_os_query.py`. Tiny/Shopify write: `0`; cron/webhook/runtime novo: `0`; disponibilidade pública/pronta entrega: `0`. Regra corrigida por Lucas: confirmar pela Stock OS DB primeiro; Tiny/fonte viva só como fallback quando a DB estiver stale, bloqueada ou insuficiente.

Em 2026-06-10T19:07:41Z, foi executado o próximo passo local/read-only: enriquecer a Stock OS DB com sinais reais locais de vendas/demanda e score operacional. A DB apontada passou para `areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db`, com tabelas novas `demand_signals_stock_os`, `current_stock_scored` e `demand_score_summary`. Fontes usadas: reports locais LK Sales e snapshots locais LK Data Spine, sem chamadas live e sem writes externos. Resultado: 903 linhas Stock OS, 352 SKUs com sinal local agregado, 18 linhas da DB casadas por SKU normalizado, 5 demandas com identidade resolvida, 13 demandas ainda bloqueadas por identidade, 4 candidatos P0 e 13 candidatos P1. Artefatos: JSON `areas/lk/sub-areas/stock/reports/lk-stock-os-demand-score-20260610T190741Z.json`, CSV `areas/lk/sub-areas/stock/reports/lk-stock-os-demand-score-20260610T190741Z.csv`, packet `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-demand-score-20260610T190741Z.md`, guia `areas/lk/sub-areas/stock/references/lk-stock-os-demand-score-guide-20260610.md`, script `areas/lk/sub-areas/stock/scripts/gate_b3_enrich_stock_os_demand_score.py` e consulta atualizada `areas/lk/sub-areas/stock/scripts/lk_stock_os_query.py --scored`. Guardrails preservados: Tiny write `0`, Shopify write `0`, writes externos `0`, runtime novo `0`, `public_availability_safe=0`, `availability_claim_allowed=0`. Próximo gate natural: gerar fila P0/P1 de reposição/transferência/decisão local a partir de `current_stock_scored`, ainda sem compra, fornecedor, Tiny/Shopify write ou promessa pública.

## 12. Gates de ativação

### Gate A — Manual read-only

- Permite: responder sob demanda, ler Brain/local, consultar fontes read-only autorizadas, criar fila/packet/receipt.
- Bloqueia: cron, gateway/bot, webhooks, writes Tiny/Shopify, compra, fornecedor, cliente.
- Aceite: 3 casos reais respondidos com fonte viva e nenhum chute de disponibilidade.

#### Caso real de aceite A1 — Ruptura de best sellers

Pergunta-alvo: **“quais best sellers estão acabando?”**

O agente deve, sob demanda:

1. Listar candidatos best sellers por venda recente, giro, demanda Growth/Trends/CRM ou histórico de família.
2. Resolver cada candidato até SKU/variante/tamanho e código Tiny quando possível.
3. Consultar Tiny/fonte viva para estoque atual por tamanho/loja física.
4. Classificar risco de ruptura por SKU/tamanho:
   - `P0`: best seller com venda/demanda forte e estoque zerado ou crítico em tamanho relevante;
   - `P1`: venda/demanda forte com estoque baixo;
   - `P2`: monitorar, demanda moderada ou dados incompletos;
   - `needs_sku_resolution`: SKU/Tiny sem confiança suficiente.
5. Entregar uma fila curta e acionável, não relatório ruidoso.
6. Para cada P0/P1, indicar ação proposta: repor, transferir, comprar, sanear SKU ou não agir.
7. Se a ação exigir Tiny/Shopify write, compra, fornecedor ou cliente, gerar packet de aprovação em vez de executar.

Saída mínima:

- Produto/modelo.
- SKU/tamanho.
- Fonte viva consultada.
- Estoque Tiny/fonte por tamanho.
- Evidência de best seller/demanda.
- Prioridade P0/P1/P2/needs_sku_resolution.
- Recomendação.
- Dono seguinte.
- Writes externos executados: `0`.

#### Ordem de fontes para candidatos best sellers — Gate A1

Para evitar depender de feeling e para não consultar Tiny para catálogo inteiro sem necessidade, o A1 usa funil em duas fases:

**Fase 1 — formar candidatos de demanda**

1. **Vendas Shopify 7/30/90 dias** — principal entrada para giro real por produto, variante, SKU e tamanho.
2. **Histórico/família forte** — modelos/marcas que costumam girar mesmo quando a janela recente está distorcida por estoque baixo.
3. **Sinais Growth/Trends/campanha** — tráfego, mídia, influencer, busca, tendência ou coleção que pode gerar demanda próxima.
4. **Demanda humana da loja/operação** — pedidos recorrentes, procura em loja física, WhatsApp/atendimento e percepção Danilo/Júlio/Lucas.

**Fase 2 — validar risco real**

5. **Tiny / `LK | CONTROLE ESTOQUE`** — fonte final para confirmar estoque atual por SKU/tamanho/loja física antes de declarar ruptura, baixo estoque ou disponibilidade.

Regra: Shopify, Growth, Trends e percepção humana criam **candidatos**; Tiny confirma ou bloqueia a **decisão de estoque**.

#### Heurística inicial de ruptura — Gate A1

Enquanto não houver modelo estatístico validado, usar esta leitura operacional:

- `P0`: item top de venda/demanda com estoque Tiny zerado ou 1 unidade em tamanho central/mais pedido.
- `P1`: item forte com estoque baixo, disperso ou sem grade suficiente para loja física.
- `P2`: item com sinal moderado ou estoque ainda confortável, mas que merece monitoramento.
- `needs_sku_resolution`: item com venda/demanda aparente, mas SKU/variant/Tiny inconfiável.

A saída do A1 deve priorizar poucos itens: primeiro P0, depois P1, e só incluir P2 se houver contexto útil. O objetivo é decisão, não inventário completo.

Template canônico do output A1:

- `areas/lk/sub-areas/stock/templates/ruptura-best-sellers-a1.md`

### Gate B — Base local read-only + sync live/diário

- Permite: criar/operar base local read-only, receber eventos via webhook autorizado, rodar cron diário de reconciliação, recalcular score local e registrar ledger/receipts.
- Bloqueia: writes Tiny/Shopify, compra, fornecedor, cliente, campanha, promessa de disponibilidade automática e alerta ruidoso.
- Aceite técnico:
  - schema local versionado e documentado;
  - backfill inicial read-only concluído com fonte declarada;
  - webhook live validado com evento assinado/no-op ou evento real autorizado;
  - cron diário validado em dry-run e depois em piloto aprovado;
  - idempotência por evento/chave de fonte;
  - freshness registrada por SKU/tamanho/fonte;
  - falha de webhook recuperada pelo cron diário;
  - falha de cron marca base como `stale`;
  - nenhuma resposta afirma disponibilidade sem Tiny/fonte viva atual ou consulta live no momento.
- Aceite operacional:
  - A1 ruptura de best sellers usa base local para formar candidatos e Tiny/fonte viva para confirmar decisão;
  - Lucas recebe só P0/falha/aprovação, não relatório de OK;
  - writes externos executados: `0`.

### Gate C — Rotina operacional read-only silent-OK

- Permite: checagem periódica read-only sobre a base local + reconfirmação em fonte viva quando necessário, com entrega apenas de exceções acionáveis.
- Bloqueia: writes, contato externo, promessa ao cliente, alertas ruidosos.
- Escopo: transformar sinais Gate B em fila curta A1/P0/P1, divergência SKU/Tiny/Shopify e falha de fonte, mantendo Tiny/fonte viva como confirmação final.
- Gatilhos permitidos para Telegram/stdout:
  - P0 confirmado ou provável;
  - P1 acionável;
  - `needs_sku_resolution` crítico;
  - fonte falhou/base `stale`;
  - aprovação necessária para compra/transferência/write.
- OK benigno: stdout vazio e nenhum Telegram.
- Aceite: rotina roda por período piloto, gera evidência local, alerta só quando gatilho real ocorrer, inclui `writes externos: 0` e nunca afirma disponibilidade sem Tiny/fonte viva.
- Decision packet: `areas/lk/sub-areas/stock/approval-packets/gate-c-operational-decision-20260608T193931Z.md`.
- Gate C0 implementado e testado local/offline em 2026-06-08T19:53:06Z: runner `areas/lk/sub-areas/stock/scripts/lk_stock_gate_c_operational_queue.py`, testes `areas/lk/sub-areas/stock/evaluation/test_lk_stock_gate_c_operational_queue.py`, receipt `areas/lk/sub-areas/stock/receipts/lk-stock-gate-c0-local-offline-implementation-20260608T195306Z.md`.
- Gate C1 piloto manual assistido executado em 2026-06-08T19:56:08Z após aprovação de Lucas: 1 alerta `fonte_stale`/`needs_sku_resolution` para `NK-AMP-BLK-40`, `telegram_sent: false`, `runtime_ativado: Nenhum`, `writes_externos: 0`. Receipt: `areas/lk/sub-areas/stock/receipts/lk-stock-gate-c1-manual-pilot-20260608T195608Z.md`.
- Gate C1+ reconciliação read-only executada em 2026-06-08T20:07:19Z: Gate B reconcile rodou `exit 0`/stdout vazio, mas o bloqueio `NK-AMP-BLK-40` persistiu sem `tiny_codigo` confiável; criado packet `areas/lk/sub-areas/stock/approval-packets/sku-saneamento-nk-amp-blk-40-20260608T200719Z.md` e receipt `areas/lk/sub-areas/stock/receipts/lk-stock-gate-c1-reconcile-sku-packet-20260608T200719Z.md`.
- Correção local Gate B/C aprovada e executada em 2026-06-08T20:42:58Z: placeholder `NK-AMP-BLK-40` substituído por `DM0032005-40` apenas na SQLite/receipt local, sem Tiny/Shopify write; receipt `areas/lk/sub-areas/stock/receipts/lk-stock-local-sku-correction-nk-amp-blk-40-to-dm0032005-40-20260608T204258Z.md`.
- Gate C manual pós-correção/reconfirmação Tiny read-only em 2026-06-08T20:47:15Z classificou `DM0032005-40 / 40` como `P0` por venda/demanda forte com estoque Tiny `LK | CONTROLE ESTOQUE` zerado; criado packet `areas/lk/sub-areas/stock/approval-packets/p0-reposicao-transferencia-dm0032005-40-20260608T204715Z.md`; writes externos `0`, runtime Gate C `Nenhum`.
- Preview de reposição/compra preparado em 2026-06-08T20:53:24Z após aprovação opção A: **SUPERSEDED em 2026-06-08T21:14:59Z** porque a demanda `6` vinha de fixture/teste (`shopify_fixture`) e não de blend/venda real; não usar para execução. Rollback/quarentena registrado em `areas/lk/sub-areas/stock/receipts/lk-stock-rollback-wrong-p0-fixture-blend-dm0032005-40-20260608T211459Z.md`.
- Regra operacional adicionada: fixtures/probes (`shopify_fixture`, `tiny_fixture`, `GATEB-PROBE-*`) nunca entram em blend, P0/P1, quantidade de compra ou recomendação operacional; compra/transferência exige demanda real/read-only ou fonte comercial viva.
- Runtime/cron Gate C ainda não ativado; Gate C2 exige aprovação separada.
- Gate B3/P0-P1 fila operacional gerada em 2026-06-10T19:23:28Z com workers locais paralelos P0/P1: 4 P0 candidatos a decision packet de reposição/transferência e 13 P1 bloqueados por identidade. Artefatos: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.md` e `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.md`. Guardrails: Tiny write `0`, Shopify write `0`, writes externos `0`, pronta entrega pública `0`, runtime novo `0`.
- Sequência aprovada por Lucas “Opção B, depois A” executada em 2026-06-10T19:42:08Z: B resolveu live/read-only 1 dos 13 P1 (`LIPCASE-11`) e manteve 12 bloqueados por duplicidade/missing; A reconfirmou Tiny/fonte viva dos 4 P0 e gerou preview conservador total de 13 unidades sugeridas. Artefatos: `areas/lk/sub-areas/stock/reports/lk-stock-os-sequential-B-then-A-20260610TSEQBA.md` e `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-sequential-B-then-A-20260610TSEQBA.md`. Guardrails: Tiny write `0`, Shopify write `0`, writes externos `0`, pronta entrega pública `0`, runtime novo `0`.
- Execução local/Brain-only do preview P0 aprovada por Lucas e registrada em 2026-06-10T20:06:12Z: 4 SKUs, quantidades `4/3/3/3`, total `13`, canal `Local/Brain apenas`, sem envio externo. Artefatos: `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-approved-preview-local-execution-20260610TP0EXECLOCAL.md`, `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-approved-preview-local-execution-20260610TP0EXECLOCAL.json` e receipt `areas/lk/sub-areas/stock/receipts/lk-stock-os-p0-approved-preview-local-execution-20260610TP0EXECLOCAL.md`. Guardrails: Tiny write `0`, Shopify write `0`, compra/transferência `0`, envio externo `0`, pronta entrega pública `0`, runtime novo `0`.
- Após Lucas dizer `SEGUIR`, preparado em 2026-06-10T20:16:58Z o packet local `DRAFT_ONLY_NOT_SENT` para próxima aprovação de envio/execução P0, com mensagem de cotação/fornecedor, mensagem de operador interno e frases de aprovação escopada. **SUPERSEDED em 2026-06-10T20:35:23Z** por correção do fluxo de compras: compras LK entram no Notion para Júlio, não em cotação de fornecedor pelo agente.
- Correção operacional de compras registrada em 2026-06-10T20:35:23Z: todos os candidatos de compra/reposição aprovados devem ser adicionados ao **Notion de compras da LK** para execução pelo **Júlio**. Criado packet Notion-ready local, sem write Notion ainda: `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-notion-julio-ready-20260610TP0NOTIONJULIO.md`; CSV importável: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-notion-julio-import-20260610TP0NOTIONJULIO.csv`. Guardrails: Notion write `0`, fornecedor/cotação `0`, compra/transferência `0`, Tiny/Shopify write `0`, pronta entrega pública `0`, runtime novo `0`.
- Write Notion aprovado e executado em 2026-06-10T20:51Z: adicionado **1 item** em `[LK] Estoque` / `Compras Pendentes`, com `Origem=À Definir`, responsável `Júlio`: `205759 610-8` / Crocs Lightning McQueen Vermelho / tam. 41 / qtd 4. Link: `https://app.notion.com/p/ESTOQUE-Crocs-Lightning-McQueen-Vermelho-41-205759-610-8-37b27dc9e0338158bd39d1b8c75ef40b`. Guardrails: Tiny/Shopify write `0`, fornecedor/cliente `0`, compra real `0`, transferência `0`, pronta entrega pública `0`.
- Correção Lucas em 2026-06-11T00:12Z, refinada em seguida: a seleção anterior do Crocs foi **erro operacional**, mas Crocs **pode entrar na fila** quando as vendas sustentarem. Regra aplicada na skill/referência: antes de escolher P0/Notion, aplicar `sales-window-fit` para Crocs — D30/D90/D180 (e janela maior disponível) precisam justificar prioridade e quantidade. Se o histórico não sustentar recorrência/velocidade real, não promover para P0 nem sugerir quantidade alta. A qtd 4 anterior ficou marcada como excessiva para o histórico considerado. Receipt da regra inicial: `areas/lk/sub-areas/stock/receipts/lk-stock-os-crocs-priority-correction-20260611T001227Z.md`.
- Correção Notion aprovada e executada em 2026-06-11T00:23Z: Lucas escolheu **arquivar/remover** a página Crocs criada anteriormente. Página `37b27dc9-e033-8158-bd39-d1b8c75ef40b` arquivada via Notion API; readback confirmou `archived=true` e `in_trash=true`. Report: `areas/lk/sub-areas/stock/reports/lk-stock-os-crocs-notion-archive-20260611T001227Z.json`; receipt: `areas/lk/sub-areas/stock/receipts/lk-stock-os-crocs-notion-archive-20260611T001227Z.md`. Guardrails: Tiny/Shopify write `0`, compra real `0`, transferência `0`, fornecedor/cliente `0`, cron novo `0`.

### Gate D — Bot/perfil dedicado Telegram

- Permite: conversa direta com `lk-stock` para triagem e decisão de estoque, usando base local como contexto e Tiny/fonte viva como confirmação final.
- Bloqueia: qualquer ação externa sem aprovação escopada no próprio turno.
- Aceite: smoke test local, token dedicado configurado sem vazamento, gateway validado e fallback seguro.

### Gate E — Sistema completo operacional

- Permite: pipeline contínuo de demanda → base local → Tiny/fonte viva → score → fila → packet → handoff → receipt.
- Bloqueia: automação de compra/reserva/campanha/write externo sem aprovação.
- Aceite: P0/P1 consistentes, baixa taxa de falso alerta, receipts completos e Lucas recebendo só decisões úteis.

## 13. Critérios de aceite atuais

- Brain package completo criado.
- Perfil Hermes `lk-stock` preparado.
- Gate B runtime real ativado com guardrails read-only e receipt de evidência.
- Roteamento LK atualizado: estoque/pronta entrega é dono obrigatório `lk-stock`.
- Gate C documentado como próximo passo seguro, ainda sem runtime operacional ativado.
- Nenhum write Tiny/Shopify/fornecedor/cliente/campanha autorizado ou executado.
- Toda próxima ativação real exige aprovação escopada separada, receipt e rollback/kill switch documentado.
