# LK - Checkout Abandonado 30min — revisão da crítica do Claude

Data: 2026-05-20
Workflow alvo: `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min Polling GraphQL - Crisp (ATIVO)`

## Veredito executivo

Claude está majoritariamente certo. A revisão dele pegou riscos reais de produção, especialmente:

- credencial Crisp hardcoded no JSON do workflow;
- dedup não-transacional com janela de duplicidade;
- staticData.skipped sem pruning;
- marcação de envio frágil em fluxo multi-item;
- paginação Shopify limitada a `first: 50` sem janela temporal/cursor;
- fallback `createdAt || updatedAt` perigoso;
- token do checkout sem limpeza de query string;
- fallback com `Math.random()` gerando lixo infinito.

A única nuance: `staticData` pode ser aceitável como MVP pequeno, mas para WhatsApp customer-facing o desenho ideal é DB externo com upsert atômico, Supabase/Redis/Postgres. Para produção estável, eu recomendaria sair de `staticData` assim que o MVP provar entrega.

## Checagem feita

Usei o snapshot local mais recente disponível:

- `/opt/data/hermes_bruno_ingest/n8n_snapshots/kWQbmEMuvdipcGjd_pre_mark_all_sent_fix_1779289971.json`

O snapshot confirma:

- workflow ativo no momento do snapshot;
- node Crisp com header `Authorization: Basic ...` hardcoded;
- filtro usa `staticData.sent` e `staticData.skipped`;
- `staticData.skipped` não é limpo;
- filtro tem `migrationCutoff` hardcoded;
- filtro usa `Math.random()` como fallback de chave skipped;
- filtro usa `createdAt || updatedAt`;
- `checkoutPath()` devolve URL inteira se não encontra `/checkouts/`;
- node de marcação usa `.item.json`, frágil para multi-item.

Tentei ler o workflow vivo pela API n8n, mas os segredos `N8N_API_TOKEN` e `N8N_API_KEY` retornaram 403 no endpoint `/api/v1/workflows`. Portanto, não apliquei write em produção.

## Correção recomendada — prioridade

### P0 — antes de qualquer volume real

1. Remover Basic Auth hardcoded do node Crisp.
   - Criar credential n8n tipo Header Auth ou Generic Credential.
   - Node deve referenciar credential, não header literal.
   - Rotacionar credencial Crisp exposta no export/snapshot.

2. Dedup com lock pré-envio.
   - No filtro: se elegível, gravar `staticData.sent[dedupKey] = { status: 'pending', lockedAt, ... }` antes de retornar o item.
   - No filtro: tratar `pending` e `sent` como bloqueados.
   - No mark node: atualizar para `status: 'sent'` após resposta Crisp aceita.
   - Em erro de envio: branch de falha deve marcar `status: 'failed'` ou liberar lock conforme política.

3. Substituir mark node por iteração sobre `$input.all()`.
   - Não usar apenas `$('Filtrar elegíveis + dedup').item.json`.
   - Retornar um item marcado para cada resposta.

4. Pruning de `skipped`, `sent`, `pending` e `failed`.
   - `sent`: manter 45 dias.
   - `skipped`: manter 7 dias.
   - `pending`: se > 2h, marcar `stale_pending` para revisão.
   - `failed`: manter 7 dias.

### P1 — robustez operacional

5. Shopify GraphQL com paginação/cursor ou janela explícita.
   - MVP: aumentar `first` para 250 e filtrar por cutoff/idade.
   - Melhor: paginar `abandonedCheckouts(first: 250, after: $cursor, reverse: true)` até encontrar itens abaixo do cutoff/idade mínima.

6. Não usar `updatedAt` como fallback silencioso de idade.
   - Se `createdAt` ausente: skip `missing_created_at`.

7. Limpar checkout token.
   - Parsear URL, remover query string/hash.
   - Se não houver `/checkouts/`, retornar string vazia e skipar.

8. Remover fallback `Math.random()`.
   - Usar chave determinística: `checkoutId`, `gid`, `email`, `phone`, ou hash estável do payload.

### P2 — arquitetura ideal

9. Migrar dedup/auditoria para Supabase/Redis/Postgres.
   - Chave única: `touchpoint + checkoutId + phone`.
   - Upsert atômico `pending` antes do send.
   - Update para `sent` com request_id/response.
   - Tabela também serve para monitoramento, rollback e reprocessamento seguro.

## Arquivos preparados

- Código corrigido do node de filtro: `reports/patches/lk-checkout-30min-filter-v3.js`
- Código corrigido do node de marcação: `reports/patches/lk-checkout-30min-mark-sent-v3.js`
- Ambos passaram em `node --check`.

## Gate de aprovação

Não aplicar diretamente em produção sem:

- snapshot do workflow vivo;
- rotação/criação da credential Crisp no n8n;
- readback do workflow pós-patch;
- execução controlada com destinatário interno;
- confirmação de receipt assíncrono Crisp/WhatsApp, não apenas `request_accepted`;
- plano de rollback: desativar workflow ou voltar snapshot anterior.
