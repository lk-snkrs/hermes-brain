# Receipt — investigação read-only SKU/Tiny/Shopify (`NK-AMP-BLK-40`)

Data UTC: 2026-06-08T20:22:54Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Escopo aprovado por Lucas: investigação read-only do SKU `NK-AMP-BLK-40` no Tiny/Shopify para resolver mapping e atualizar apenas receipt/packet local, sem write externo.
Status: **investigação executada; SKU local inválido/não encontrado; candidato canônico provável encontrado com estoque Tiny zerado**

## Fontes consultadas

- Doppler: somente presença de credenciais, valores não impressos.
- Shopify Admin GraphQL: `query` read-only para variantes/produtos.
- Tiny API read-only:
  - `produtos.pesquisa`
  - `produto.obter.estoque`
- Depósito Tiny oficial: `LK | CONTROLE ESTOQUE`.

## Resultado 1 — SKU local `NK-AMP-BLK-40`

Consulta read-only executada para:

- SKU: `NK-AMP-BLK-40`
- título local: `Nike Air Max Plus Black`

Resultado resumido:

```json
{
  "status": "shopify_variant_not_resolved",
  "confidence": "blocked",
  "shopify_exact_sku_candidates": 0,
  "tiny_exact_codigo_candidates": 0,
  "tiny_title_size40_candidates": 2,
  "resolved_tiny_codigo": null,
  "resolved_tiny_id": null,
  "availability_claim_allowed": false,
  "writes_externos": 0
}
```

Interpretação: `NK-AMP-BLK-40` não apareceu como SKU/código exato nem no Shopify nem no Tiny. Ele deve ser tratado como SKU local/placeholder incorreto, não como SKU operacional confiável.

## Resultado 2 — candidato ativo mais provável

A busca por título/produto retornou como candidato Shopify ativo para Air Max Plus Black tamanho 40:

- Produto Shopify: `Tênis Air Max Plus Black University Blue Preto`
- Handle: `air-max-plus-black-university-blue`
- Status Shopify: `ACTIVE`
- Tamanho: `40`
- SKU Shopify: `DM0032005-40`
- Variant legacy ID: `44265045295326`

Consulta cruzada read-only para `DM0032005-40` retornou match exato no Tiny:

```json
{
  "status": "mapping_resolved_exact_sku",
  "confidence": "high",
  "shopify_exact_sku_candidates": 1,
  "tiny_exact_codigo_candidates": 1,
  "resolved_tiny_codigo": "DM0032005-40",
  "resolved_tiny_id": "937674228",
  "official_deposit_stock": {
    "deposito": "LK | CONTROLE ESTOQUE",
    "saldo": 0.0,
    "desconsiderar": "N"
  },
  "writes_externos": 0
}
```

## Veredito operacional

- O SKU local `NK-AMP-BLK-40` deve ser corrigido/substituído por um SKU real antes de entrar no Gate C.
- Se o item pretendido era **Air Max Plus Black University Blue, tamanho 40**, o mapping correto é:
  - Shopify SKU: `DM0032005-40`
  - Tiny código: `DM0032005-40`
  - Tiny id: `937674228`
  - Depósito oficial `LK | CONTROLE ESTOQUE`: saldo `0.0`
- Como a fonte Tiny viva foi consultada, para esse candidato específico é seguro dizer internamente: **saldo Tiny oficial está zerado no tamanho 40**.
- Ainda não prometi disponibilidade/pronta entrega nem fiz recomendação de compra/reposição automática; isso exigiria o próximo gate/decisão.

## Ações bloqueadas/não executadas

- Tiny write: `0`.
- Shopify write: `0`.
- Update de base SQLite Gate B: `0`.
- Cron novo: `0`.
- Telegram automático: `0`.
- Compra/transferência/reserva/campanha/fornecedor/cliente: `0`.
- Valores de secrets impressos: `0`.

## Próximo passo recomendado

Criar um **packet C2 de correção local/ingest autorizado** para substituir o placeholder `NK-AMP-BLK-40` pelo código real `DM0032005-40` no cache/fila Gate B/C e então recalcular a fila operacional. Isso ainda seria local/read-only quanto a Tiny/Shopify, mas escreveria na base local do agente; precisa aprovação separada se Lucas quiser que eu execute agora.
