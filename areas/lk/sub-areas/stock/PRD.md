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

- Tiny é a verdade de estoque. Shopify stock nunca é resposta final.
- Toda disponibilidade deve ser variante/tamanho-level.
- Sem fonte viva, resposta deve ser “não confirmado”, não chute.
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
