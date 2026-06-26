# LK OS Handoff — após restart gateway/servidor — 2026-05-12

Status salvo em: 2026-05-12T19:44:25Z

## Contexto ativo

Lucas vai reiniciar servidor/gateway. Ao voltar, continuar LK OS a partir do bloco GMC P1-B `availability`.

## Último estado confirmado

### GMC P1 4 campos — concluído e verificado

Status: `gmc_p1_core_attrs_4field_apply_verified`

Executado no Merchant para 1.627 produtos online:

- `title`
- `link`
- `imageLink`
- `price`

Resultado:

- 1.627/1.627 atualizados com sucesso.
- 0 faltando algum dos 4 campos alvo em verificação pós-apply.
- `availability` ficou fora por regra: Tiny é verdade de estoque.

Importante:

- Content API v2.1 neste Merchant funcionou via `POST /products` como upsert; `PUT /products/{productId}` retornou 404.
- Rollback snapshots privados estão em `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/` com chmod 600.

Arquivos principais:

- `reports/lk-gmc-2026-05-12-p1-core-attrs-4field-apply-final.md`
- `areas/lk/rotinas/gmc-2026-05-12-p1-core-attrs-4field-apply-final.md`
- `scripts/lk_gmc_p1_execute_core_attrs_4field_20260512.py`

### GMC P1-B availability — iniciado, não aplicado

Objetivo: montar packet no-write para preencher `availability` usando Tiny como fonte de estoque.

Script criado:

- `scripts/lk_gmc_p1_availability_tiny_packet_20260512.py`

Interim docs:

- `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet-interim.md`
- `areas/lk/rotinas/gmc-2026-05-12-p1-availability-tiny-packet-interim.md`

Primeiro teste pequeno:

- bateu rate-limit do Tiny (`codigo_erro=6`, API bloqueada temporariamente por excesso de acessos).
- corrigido o script para **nunca converter erro/rate-limit Tiny em `out of stock`**.
- erro API agora fica `blocked_tiny_stock_api_error`.

Processo background anterior:

- tentado: `proc_3ebe93b6e640`
- em 2026-05-12T19:44:25Z, `process list` retornou vazio; se servidor/gateway reiniciar, assumir que não há processo vivo e retomar manualmente.

## Próxima ação segura após restart

1. Entrar em `/opt/data/hermes_bruno_ingest/hermes-brain`.
2. Carregar skill `lk-operational-intelligence`.
3. Verificar arquivos e status.
4. Rechecar se Tiny saiu do rate-limit antes de rodar lote completo.
5. Rodar packet read-only de `availability` com pacing conservador.
6. Gerar números reais: ready, in stock, out of stock, bloqueados/revisão.
7. Não aplicar Merchant sem aprovação explícita nova do Lucas.

Comando recomendado após cooldown Tiny:

```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain
python3 scripts/lk_gmc_p1_availability_tiny_packet_20260512.py --tiny-index-sleep 1.2 --tiny-sleep 1.7
python3 scripts/brain_health_check.py
git diff --check
```

Se Tiny ainda retornar `codigo_erro=6`, não insistir em loop agressivo. Aguardar mais e/ou reduzir pacing.

## Guardrails obrigatórios

- Nenhum Merchant write sem aprovação explícita após packet.
- Nenhum Tiny/Shopify/feed/DB/POS/campaign write.
- Tiny é verdade de estoque; Shopify local é evidência auxiliar apenas.
- Secrets via Doppler; nunca imprimir tokens.
- Se for aplicar `availability` no Merchant depois: salvar rollback snapshot privado completo (`products.get`) antes e usar `POST /products` upsert preservando resource atual.

## Prompt para Lucas enviar depois do restart

```text
Continuar LK OS do handoff salvo em /opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-os-handoff-after-gateway-restart-2026-05-12.md.

Carregue a skill lk-operational-intelligence. Retome o bloco GMC P1-B availability: verificar se o Tiny saiu do rate-limit, rodar o packet read-only scripts/lk_gmc_p1_availability_tiny_packet_20260512.py com pacing conservador, gerar relatório com ready/in stock/out of stock/bloqueados, rodar brain_health_check.py e git diff --check, e me reportar. Não aplicar Merchant/Tiny/Shopify/feed/DB/POS/campanha sem nova aprovação explícita.
```
