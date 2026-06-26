# Approval/Handoff Packet — New Balance 740 (`/collections/new-balance-740`) — read-only unblock

Criado em: 2026-06-26T09:05:09Z  
Origem: Mesa COO — decisão de Lucas: **Fazer**  
Dono seguinte: **LK Shopify + LK Stock**  
Escopo: preparar validação read-only para decidir se a frente New Balance 740 pode sair do bloqueio.

## 1. Veredito curto

- **Tipo de ação:** handoff/approval packet read-only; sem execução de write.
- **Alvo exato:** coleção futura `new-balance-740` e produto candidato `tenis-new-balance-740-x-concepts-saignee-verde`.
- **Risco:** A1 preview/read-only agora; qualquer reativação/publicação/criação de coleção vira A3 Shopify write e exige aprovação escopada posterior.
- **Status recomendado:** manter **bloqueada** até LK Stock validar estoque/Tiny e LK Shopify validar publicabilidade/status/superfície.
- **Decisão de hoje:** não criar coleção vazia; só destravar se houver produto publicável/ativo ou plano aprovado para corrigir o produto primeiro.

## 2. Fonte viva e evidências

- **Histórico/local consultado:**
  - `/opt/data/tmp/lk_curadoria_next_batch_readonly_20260606.stdout` linhas 887-915: cluster `new-balance-740`, `total=1`, `covered=0`, produto validado publicamente em 2026-06-06.
  - `/opt/data/tmp/lk_curadoria_next_products_deep_scan_20260606.json` linhas 3658-3689: mesmo produto, `covered=false`, `covered_dev=false`, `covered_prod=false`; uma rodada teve `.js` 429, então não serve como decisão atual isolada.
- **Shopify Admin read-only consultado em:** 2026-06-26T09:05Z via GraphQL query; `values_printed=false`; secrets `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` existem no Doppler e foram injetados sem imprimir valores.
- **Shopify read-only atual:**
  - Produto: `Tênis New Balance 740 x Concepts Saignée Verde`
  - Product GID: `gid://shopify/Product/8780230492382`
  - legacy ID: `8780230492382`
  - handle: `tenis-new-balance-740-x-concepts-saignee-verde`
  - status: **ARCHIVED**
  - `publishedAt`: `null`
  - `onlineStoreUrl`: `null`
  - vendor: `New Balance`
  - product type: `Tênis`
  - variantes Shopify vistas: 8 (`37` a `44`), SKUs `U740GP2-1` a `U740GP2-8`.
  - `totalInventory` Shopify exibiu `24`, mas **Shopify não é fonte final de estoque**.
- **Collection read-only atual:** `collectionByHandle(handle: "new-balance-740")` retornou `null`; a coleção ainda não existe/ não está resolvida por esse handle no Admin GraphQL.
- **Tiny/Stock:** não consultado por este perfil. Por regra LKGOC/LK, estoque/disponibilidade precisa ser validado pelo **LK Stock**.

## 3. Snapshot antes

- Coleção `/collections/new-balance-740`: não encontrada via `collectionByHandle` no Admin GraphQL.
- Produto candidato existe no Shopify, mas está `ARCHIVED` e sem publicação online.
- IDs/handles envolvidos:
  - product GID: `gid://shopify/Product/8780230492382`
  - product legacy ID: `8780230492382`
  - product handle: `tenis-new-balance-740-x-concepts-saignee-verde`
  - collection handle pretendido: `new-balance-740`
- Backup/rollback path previsto se houver write futuro: LK Shopify deve capturar JSON completo do produto/coleção antes de qualquer mutation; para coleção nova, rollback = remover/arquivar a coleção criada + restaurar qualquer campo/status alterado no produto.

## 4. Alteração proposta

**Nenhuma alteração aprovada neste packet.**

Este packet só pede validação/handoff:

1. **LK Stock:** confirmar em Tiny/Stock OS se os SKUs `U740GP2-1`…`U740GP2-8` têm estoque real/publicável por tamanho e se há bloqueio operacional para venda/pronta entrega/encomenda.
2. **LK Shopify:** validar se o produto arquivado pode/ deve virar publicável, qual status/canal/publicação seriam necessários, se há campos obrigatórios ausentes e se faz sentido criar a coleção `new-balance-740` só após existir produto ativo/publicado.
3. **LKGOC:** só retoma guia/coleção quando houver resposta positiva dos dois donos ou um plano aprovado de correção.

Campos que seriam writes futuros, **não aprovados agora**:

| Objeto | Campo/ação possível | Status neste packet |
|---|---|---|
| Produto | mudar `ARCHIVED` → `ACTIVE` | não aprovado |
| Produto | publicar canal Online Store | não aprovado |
| Produto | editar SEO/title/body/tags/metafields/images | não aprovado |
| Coleção | criar `new-balance-740` | não aprovado |
| Coleção | adicionar produto, SEO, descrição, template | não aprovado |
| Tiny/estoque | corrigir código, estoque, disponibilidade | não aprovado |

## 5. Padrão canônico aplicado

- `lk-shopify-readonly` para evidência Shopify read-only.
- Template canônico `areas/lk/sub-areas/shopify/templates/preview-aprovacao-shopify.md` para packet/approval.
- Fronteira LKGOC: coleção/Guia LK só após produto publicável; criação de superfície vazia bloqueada.
- Fronteira LK Stock: Tiny/Stock OS é fonte final para estoque/disponibilidade.
- Fronteira LK Shopify: superfície Shopify/status/publicação/coleção exigem aprovação antes de write.

## 6. Readback e verificação esperados

### LK Stock — condição de sucesso

- Evidência Tiny/Stock OS por SKU/tamanho para `U740GP2-1`…`U740GP2-8`.
- Classificação explícita: `publicável`, `não publicável`, `precisa correção SKU/Tiny`, ou `indisponível/sem venda`.
- Não usar Shopify inventory como prova final.

### LK Shopify — condição de sucesso

- Read-only snapshot do produto completo e status de canais/publicações.
- Diagnóstico se `ARCHIVED` é intencional ou erro operacional.
- Se for destravável, preparar **novo approval packet** com campos exatos, snapshot, rollback e readback antes de qualquer mutation.
- Se não for destravável, manter bloqueio e registrar motivo.

### LKGOC — condição de sucesso

- Só considerar `/collections/new-balance-740` quando houver pelo menos um produto ativo/publicado ou plano aprovado para publicar.
- Não criar guia/coleção vazia.

## 7. Rollback

Como este packet não executa write, rollback atual = **não aplicável**.

Se houver approval futuro:

- Produto: salvar JSON antes; rollback = restaurar status/publicações/campos/tags/metafields originais.
- Coleção: salvar JSON/ID criado; rollback = remover/arquivar coleção e remover associações de produto se criadas.
- Tiny: qualquer alteração precisa do rollback próprio do LK Stock/Tiny.

## 8. O que NÃO está aprovado

- Reativar produto arquivado.
- Publicar produto no Online Store.
- Criar/editar coleção Shopify.
- Alterar preço, estoque, SKU, Tiny, tags, SEO, metafields, tema, menu, schema ou Guia LK.
- Contatar fornecedor/cliente.
- Campanha, Klaviyo, WhatsApp, Meta, GMC ou qualquer envio externo.

## 9. Texto de aprovação futuro para Telegram

Se LK Stock + LK Shopify retornarem OK e Lucas quiser executar, usar um novo packet com texto semelhante:

> Aprovo LK Shopify executar exatamente este preview para New Balance 740: [campos exatos], [produto/coleção IDs], [status/canais], com snapshot/readback/receipt/rollback. Não aprovo preço/estoque/Tiny/campanha/contato externo fora do que está listado.

## 10. Continuidade / handoff funcional

- Reminder OS loop needed: **yes**
- Owner primário: `lk-shopify` + `lk-stock`
- Próxima ação concreta: LK Stock validar Tiny/Stock OS dos SKUs; LK Shopify validar publicabilidade/status e preparar packet de write se cabível.
- Gatilho de revisão: resposta de ambos os donos ou nova decisão de Lucas sobre manter bloqueada.
- Writes externos executados neste turno: **0**
- Secrets impressos: **0** (`values_printed=false`)
