# LK GMC P1 Core Attrs 4-Field Apply Final, 2026-05-12

Status: `gmc_p1_core_attrs_4field_apply_verified`

## Escopo aprovado

Lucas escolheu opção 2 para aplicar todos os candidatos do pacote 4 campos.

Campos atualizados no Merchant:

- `title`
- `link`
- `imageLink`
- `price`

Campo excluído por política de estoque:

- `availability`

## Execução

- Candidatos: 1.627 exact online product IDs.
- Atualizados com sucesso: 1.627.
- Falha inicial sem efeito: 1 tentativa via `PUT /products/{productId}` retornou 404 antes de qualquer alteração; o executor foi corrigido para usar upsert via `POST /products`.
- Execução retomada/resumida por progress files privados.
- Writes Shopify: 0.
- Writes Tiny: 0.
- Feed/datafeed/fetchNow: 0.
- DB/POS/campanha/envio: 0.

## Verificação pós-apply

Product resource atual, após delay de consistência:

- Candidate IDs verificados: 1.627.
- Presentes em `products.list`: 1.627.
- Com os 4 campos presentes (`title`, `link`, `imageLink`, `price`): 1.627.
- Missing nos 4 campos: 0.

Productstatus atual para os 1.627:

- Ainda com algum required-attribute issue: 1.627.
- Ainda faltando os 4 campos alvo no productstatus: 0.
- Ainda faltando `availability`: 1.616 linhas.

Observação: `availability` aparece com 3.232 instâncias porque o Merchant reporta por destino/issue instance; por linha, são 1.616 produtos ainda com availability ausente.

## Rollback privado

Snapshots de rollback completos salvos em `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/`, chmod 600:

- `lk-gmc-2026-05-12-p1-core-attrs-4field-executor-rollback-20260512T182442Z.json`
- `lk-gmc-2026-05-12-p1-core-attrs-4field-executor-rollback-20260512T183522Z.json`
- `lk-gmc-2026-05-12-p1-core-attrs-4field-executor-rollback-20260512T184539Z.json`

## Arquivos de verificação

- Product resource verify: `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-post-apply-verify.json`
- Productstatus verify: `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-post-apply-status-verify.json`
- Executor report: `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-executor.md`

## Próximo bloco seguro

`availability` deve ser tratado em pacote separado, preferencialmente validando Tiny como fonte de verdade de estoque antes de escrever disponibilidade no Merchant.
