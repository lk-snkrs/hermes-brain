# LK GMC P1-B Availability Tiny Packet — Interim, 2026-05-12

Status: `gmc_p1_availability_tiny_packet_queued_after_tiny_rate_limit`

## Resumo executivo

- Próximo bloco iniciado: P1-B `availability` usando Tiny como verdade de estoque.
- Merchant read-only já confirmou que há 1.616 linhas online ainda com `availability` ausente após o apply dos 4 campos.
- Foi criado o executor/packet no-write: `scripts/lk_gmc_p1_availability_tiny_packet_20260512.py`.
- O primeiro teste pequeno bateu no limite temporário da API Tiny (`codigo_erro=6`, API bloqueada por excesso de acessos).
- Corrigido o script para nunca transformar erro/rate-limit do Tiny em evidência de `out of stock`.
- Reexecução completa foi enfileirada em background com cooldown de 30 minutos e pacing conservador.

## Guardrail aplicado

- `availability` só será proposta quando houver leitura Tiny válida.
- Erro/rate-limit Tiny agora fica `blocked_tiny_stock_api_error`, não vira proposta de disponibilidade.
- Nenhum Merchant/Tiny/Shopify/feed/DB/POS/campanha write foi executado.

## Background run

- Processo: `proc_3ebe93b6e640`
- Comando: `python3 scripts/lk_gmc_p1_availability_tiny_packet_20260512.py --tiny-index-sleep 1.2 --tiny-sleep 1.7`
- Início efetivo: após 30 minutos de cooldown Tiny.
- Saída esperada: relatório público `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.md` + JSON/CSV e CSV privado chmod 600.

## Não executado

- merchant_product_update
- merchant_product_insert_upsert
- tiny_write
- shopify_write
- feed_update_or_fetch
- database_write
- pos_write
- campaign_or_external_send
