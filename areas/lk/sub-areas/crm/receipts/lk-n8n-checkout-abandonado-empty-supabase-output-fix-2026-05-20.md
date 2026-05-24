# LK — n8n checkout abandonado: fix Supabase vazio interrompendo fluxo

Data UTC: 2026-05-20
Agente: Hermes LK Growth

## Pedido / aprovação

Lucas observou que era impossível não haver carrinho/checkout abandonado e aprovou corrigir o workflow de produção.

## Diagnóstico

Nas execuções recentes do workflow `kWQbmEMuvdipcGjd`, o Shopify GraphQL retornava abandoned checkouts normalmente, mas o fluxo parava antes do filtro/envio porque o node `Postgres Load CRM State` retornava `0 items` quando a tabela Supabase `lk_crm_checkout_sequences` estava vazia.

No n8n, `0 items` em um node intermediário interrompe a linha downstream. Com isso, o node `Filtrar elegíveis + dedup` não executava.

Evidência pré-fix:

- Execuções recentes como `11285`, `11283`, `11281`, `11279` tinham nodes:
  - `A cada 5 min`
  - `Shopify GraphQL abandonedCheckouts`
  - `Postgres Load CRM State`
- Não chegavam ao node `Filtrar elegíveis + dedup`.
- Na execução `11285`, Shopify retornou `250` abandoned checkouts.

## Alteração aplicada

Workflow:

- ID: `kWQbmEMuvdipcGjd`
- Nome: `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`

Patch aplicado:

- Node `Postgres Load CRM State` agora tem `alwaysOutputData: true`.
- Assim, quando o Supabase retorna `[]`, o n8n ainda passa um item vazio para o próximo node, permitindo que `Filtrar elegíveis + dedup` rode e consulte o Shopify output.

## Snapshot / rollback

Snapshot pré-write salvo fora do Brain por conter potencialmente headers/credenciais:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-empty-supabase-output-fix-20260520T200446Z.json`

Rollback: restaurar esse JSON no workflow `kWQbmEMuvdipcGjd` via API/UI n8n e confirmar `activeVersionId == versionId`.

## Readback pós-patch

- `active: true`
- `versionId: 7c63dd96-2b55-4c99-bdd6-9ebcedf350ee`
- `activeVersionId: 7c63dd96-2b55-4c99-bdd6-9ebcedf350ee`
- `Postgres Load CRM State.alwaysOutputData: true`

## Validação pós-patch

Execução automática seguinte:

- Execução: `11360`
- `startedAt: 2026-05-20T20:05:16.013Z`
- `status: success`

Nodes executados:

- `A cada 5 min`
- `Shopify GraphQL abandonedCheckouts`
- `Postgres Load CRM State`
- `Filtrar elegíveis + dedup`

Resultado:

- Shopify retornou `250` abandoned checkouts.
- `Postgres Load CRM State` retornou `1` item vazio, como esperado com `alwaysOutputData`.
- `Filtrar elegíveis + dedup` executou e retornou `0` itens elegíveis para envio naquele ciclo.

Motivos observados no staticData após a execução:

- `before_migration_cutoff`: 328 ocorrências — histórico antigo bloqueado por segurança para evitar blast retroativo.
- `too_recent_for_24h`: 3 ocorrências — os três checkouts que já receberam T1 ainda não têm 24h para T2.
- `missing_or_invalid_brazil_whatsapp_phone`: 2 ocorrências — checkouts recentes sem telefone BR válido.

## Backfill interno Supabase

Como a tabela Supabase estava vazia apesar de haver três envios aceitos previamente pela Crisp, foram reconciliados no Supabase os três registros já presentes no `staticData.sent` do n8n.

Registros backfilled:

- `30min:39499768103134:+55…9631` — `request_id: c67dc7ef-f788-46da-b508-2e2d7abdd7e3`
- `30min:39499747229918:+55…3361` — `request_id: 060da051-5750-4097-92ef-85495d7918fd`
- `30min:39499699585246:+55…3361` — `request_id: 60509b06-7965-4f05-bdad-ba8674d372a4`

## Conclusão

O bug de orquestração foi corrigido: o filtro voltou a rodar mesmo quando o Supabase está vazio.

A ausência de novos envios após o patch não significa falta de abandoned checkouts; significa que, no ciclo validado, nenhum checkout era elegível pelas regras atuais:

- histórico anterior ao cutoff não é enviado;
- T2 aguarda 24h após T1;
- novos checkouts sem telefone válido não podem receber WhatsApp.
