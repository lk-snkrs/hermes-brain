# Audit — n8n checkout abandonado 30min/24h/72h

Data: 2026-05-20  
Área: LK CRM / WhatsApp / Crisp / n8n / Shopify  
Workflow: `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`

## Escopo

Auditoria read-only do fluxo ativo após implementação dos 3 touchpoints e cupom Shopify no T3.

## Estado verificado

- Workflow ativo: sim.
- `activeVersionId == versionId`: sim.
- `triggerCount`: 1.
- Nodes: 7.
- Últimas execuções recentes: sucesso.
- Callback workflow ativo: `LK - Crisp WhatsApp Callback Capture (ATIVO)`.
- Templates Meta verificados e aprovados:
  - `lk_checkout_abandonado_30min_v4`
  - `lk_checkout_abandonado_24h_v1`
  - `lk_checkout_abandonado_72h_cupom10_v1`
- Code node syntax check: OK nos 3 code nodes.

## Pontos fortes

- Arquitetura consolidada em um único workflow.
- Dedup por touchpoint.
- Lock `pending` antes do envio.
- Mark sent exige `request_accepted` + `request_id`.
- `createdAt` é obrigatório; não usa fallback `updatedAt` para idade.
- Sem `Math.random` no dedup principal.
- Header image presente nos payloads.
- Shape Crisp híbrido preservado: `as:text`, `type:text`, `new_session:false`.
- Cupom T3 com 10%, 24h, uso único e sem combinação.
- Cutoff de migração evita blast histórico.

## Gaps / riscos encontrados

### P0 — nenhum bloqueador imediato encontrado

O fluxo está ativo, publicado, e as últimas execuções recentes estão passando.

### P1 — melhorias recomendadas antes de chamar de robusto/escala

1. `staticData` ainda é storage local do workflow, não banco transacional.
   - Risco: concorrência, crash entre etapas, manutenção difícil.
   - Recomendação: migrar dedup/eventos para Supabase/Postgres com unique constraint por `touchpoint + checkoutId + phone`.

2. Auth Crisp está hardcoded no node HTTP.
   - Risco: segredo em snapshot/export e rotação mais difícil.
   - Recomendação: mover para credential n8n dedicada.

3. Sem Error Workflow / alerta de falha.
   - Risco: falhas podem ficar só em executions.
   - Recomendação: criar workflow de erro/alerta Telegram ou fila de revisão.

4. Falhas de Crisp após criação de cupom T3 ficam como `failed` e não reentram automaticamente.
   - Risco: cupom criado sem mensagem entregue; cliente não recebe T3.
   - Recomendação: fila de revisão/retry controlado, com tratamento de cupom já existente.

5. Não há ligação entre `request_id` Crisp e callback de entrega/leitura.
   - Risco: `request_accepted` não prova entrega no WhatsApp.
   - Recomendação: persistir `request_id` em tabela e reconciliar callback.

6. Shopify query usa `first: 100`, sem paginação.
   - Risco: em volume maior, eligible antigo pode cair fora da janela.
   - Recomendação: subir para 250 ou implementar cursor pagination até cutoff.

7. Sem frequency cap por telefone/cliente entre múltiplos checkouts.
   - Risco: múltiplas sequências para o mesmo WhatsApp se houver múltiplos checkouts.
   - Recomendação: cap comercial por phone, ex. 1 sequência ativa por 72h.

8. Cupom T3 está com `customerSelection: all`.
   - Mitigação atual: código difícil + 24h + usageLimit 1.
   - Recomendação futura: restringir por customer quando Shopify trouxer customer id confiável.

### P2 — limpeza técnica

- Normalizar registros antigos de `staticData.sent` que não têm `status`, embora o código os trate como enviados.
- Melhorar o node `Preparar payload Crisp` para não usar fallback `originals[0]` se `pairedItem` vier ausente; deve falhar de forma explícita para evitar associação errada em múltiplos itens.
- Criar dashboard simples de contagens: eligible, skipped, sent, failed por touchpoint.

## Execuções e staticData

- `staticData.sent`: 3 registros antigos 30min com request_id.
- `staticData.failed`: 0.
- `staticData.skipped`: majoritariamente `before_migration_cutoff`; últimas execuções pulam itens recentes/aguardando 24h.
- Últimas execuções auditadas: sucesso e sem itens elegíveis no filtro.

## Nota

A auditoria Shopify direta via Admin API falhou por DNS temporário no ambiente Hermes, mas o próprio n8n está executando o node Shopify com sucesso nas execuções recentes. A conclusão principal é baseada no readback do n8n, últimas execuções n8n e Meta readback.

## Conclusão

O fluxo está bom para MVP/produção controlada. Para ficar mais profissional e menos frágil, priorizar:

1. Supabase/Postgres para dedup/event log.
2. Error workflow + alerta.
3. Callback reconciliation por `request_id`.
4. Credential n8n para Crisp.
5. Páginação Shopify + frequency cap por telefone.
