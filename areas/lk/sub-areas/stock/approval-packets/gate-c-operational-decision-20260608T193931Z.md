# Decision packet — Gate C operacional read-only silent-OK (`lk-stock`)

Data UTC: 2026-06-08T19:39:31Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **preview para aprovação — runtime ainda não ativado**

## Contexto

Gate B já está ativo com guardrails read-only:

- webhooks `lk-stock-*` via `hermes-webhooks`/Vercel;
- Hermes Gateway executando ingest determinístico;
- base local `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite` como cache/ledger;
- cron diário de freshness/reconcile read-only `e8b35e20751b`;
- Telegram silent-OK;
- writes externos `0`.

Gate C transforma esse runtime em **fila operacional segura**, sem virar automação de compra, reserva, campanha, Tiny/Shopify write ou promessa de disponibilidade.

## Objetivo do Gate C

Rodar uma rotina read-only que:

1. lê a base local Gate B;
2. gera candidatos A1 de ruptura de best sellers;
3. detecta P0/P1, `needs_sku_resolution`, falha de fonte e base stale;
4. só consulta Tiny/fonte viva quando necessário para confirmar decisão material;
5. cria receipt/handoff local;
6. envia Telegram apenas se houver exceção acionável.

## O que Gate C permite

- Criar um runner operacional read-only para fila A1/P0/P1.
- Reusar `stock_query_a1.py` como saída humana, mas adicionar camada de decisão/alerta.
- Registrar receipts em Brain quando houver:
  - P0 confirmado;
  - P1 relevante com ação proposta;
  - divergência SKU/Tiny/Shopify bloqueando decisão;
  - base `stale` ou falha de fonte;
  - necessidade de aprovação para compra/transferência/write.
- Entregar Telegram apenas em mensagens acionáveis.
- Rodar inicialmente em modo local/manual, depois acoplar ao cron existente ou criar cron separado, somente após aprovação explícita.

## O que continua bloqueado

- Tiny write.
- Shopify inventory/product write.
- Compra automática.
- Transferência executada automaticamente.
- Reserva/promessa ao cliente.
- Contato com fornecedor/cliente.
- Campanha/CRM/WhatsApp/Klaviyo.
- Alertas de OK, relatórios ruidosos ou ping recorrente.
- Afirmar disponibilidade sem Tiny/fonte viva equivalente.

## Gatilhos de alerta permitidos

Gate C só fala com Lucas quando houver uma destas condições:

1. **P0 confirmado ou provável** — item com demanda forte e estoque Tiny/fonte viva zerado/crítico, ou base local apontando P0 mas exigindo confirmação imediata.
2. **P1 acionável** — item forte com estoque baixo e ação clara de reposição/transferência/compra/saneamento.
3. **`needs_sku_resolution` crítico** — venda/demanda existe, mas SKU/variant/Tiny impede decisão de estoque.
4. **Fonte falhou/stale** — base local ficou vencida, webhook/cron perdeu freshness ou Tiny/fonte viva não respondeu.
5. **Aprovação necessária** — existe uma ação proposta que exige Lucas/Júlio/ops antes de qualquer write externo.

Se nada disso ocorrer, stdout/Telegram ficam silenciosos.

## Formato da mensagem Telegram

```text
LK Stock — decisão necessária

Gatilho: [P0/P1/SKU/fonte/aprovação]
Produto: [modelo]
SKU/tamanho: [sku] / [tamanho]
Fonte/freshness: [Tiny/fonte viva agora | live | cron diário | stale]
Evidência: [venda/demanda/estoque]
Risco: [venda perdida | decisão bloqueada]
Ação proposta: [repor | transferir | comprar | sanear SKU | consultar fonte]
Writes externos executados: 0
Aprovação necessária: [sim/não + texto claro]
```

## Aceite técnico

Antes de ativar runtime Gate C, precisa existir:

1. Runner `lk_stock_gate_c_operational_queue.py` ou equivalente.
2. Testes offline cobrindo:
   - OK silencioso quando não há P0/P1/SKU/falha;
   - P0 gera saída acionável;
   - `needs_sku_resolution` gera saída acionável;
   - `stale`/falha de fonte gera saída acionável;
   - nenhuma saída afirma disponibilidade sem fonte viva;
   - `writes_externos: 0` preservado.
3. Receipt local de dry-run com evidência.
4. Comando manual validado contra a base local atual.
5. Se virar cron: job separado ou update explícito do job existente, com `no_agent`, silent-OK e kill switch.

## Aceite operacional

- Lucas recebe no máximo decisões úteis, não inventário.
- A fila prioriza P0, depois P1, depois divergência crítica.
- Todo P0/P1 inclui dono seguinte: `lk-ops`, `lk-shopify`, `lk-growth`, `lk-trends` ou Lucas.
- Toda recomendação de compra/transferência/write vira approval packet, não execução.
- Todo output material registra fonte/freshness e `writes externos: 0`.

## Plano de execução recomendado

### Fase C0 — Documental/offline

- Atualizar PRD com contrato Gate C.
- Criar testes offline do runner Gate C.
- Implementar runner local sem cron novo.
- Rodar testes e gerar receipt de dry-run.

### Fase C1 — Piloto manual

- Executar runner manualmente sobre a base Gate B.
- Validar se output é silencioso quando OK e acionável quando há fixture P0/SKU/fonte.
- Ajustar copy/limiares para evitar ruído.

### Fase C2 — Runtime aprovado

Somente com aprovação explícita de Lucas:

- acoplar runner ao cron existente ou criar cron Gate C separado;
- manter `no_agent` e stdout vazio em OK;
- manter kill switch;
- registrar receipt de ativação.

## Kill switch / rollback

1. Pausar cron Gate C, se criado.
2. Voltar para Gate B freshness/reconcile apenas.
3. Manter base local e receipts como evidência read-only.
4. Marcar Gate C como `paused` no PRD/receipt.
5. Continuar Gate A/manual sob demanda com Tiny/fonte viva.

## Decisão necessária

Para executar a Fase C0 agora, a aprovação segura é:

> **Aprovo Gate C0: implementar e testar runner operacional read-only local/offline, sem cron novo, sem Telegram real exceto stdout de teste, sem writes externos.**

Para ativar runtime/cron real depois dos testes, será necessária outra aprovação separada.
