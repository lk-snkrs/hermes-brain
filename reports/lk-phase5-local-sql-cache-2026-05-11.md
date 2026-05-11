# LK OS Fase 5 — local SQL cache — 2026-05-11

## Veredito

A base operacional local agora existe. Supabase/Shopify/Tiny continuam sendo fontes vivas de verdade, mas o estado de trabalho/aprovação da Fase 5 foi materializado em SQLite local fora do repo.

## Caminho

- SQLite local: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite`
- Permissão: `chmod 600`
- Não versionado no Git
- Sem raw e-mail, nome, telefone ou endereço

## Tabelas

- `metadata`: origem dos relatórios e escopo da base local
- `p1_candidate_recipients`: recipients P1 com `customer_ref` hash, segmento, anchor, tamanho, SKU, RFM e flags de contato agregadas
- `p1_group_readiness`: prontidão por grupo P1
- `tiny_anchor_stock`: estoque Tiny por anchor/tamanho/SKU
- `final_approval_groups`: pacote final de aprovação READY/HOLD

## Contagens

- `p1_candidate_recipients`: 108
- `p1_group_readiness`: 10
- `tiny_anchor_stock`: 49
- `final_approval_groups`: 10

## Decisão operacional

- **Fonte de verdade comercial**: Shopify/Supabase/Tiny, conforme a integração.
- **Banco de trabalho Hermes**: SQLite local, para evitar depender de chamadas remotas em toda etapa, manter rastreabilidade e preparar aprovações.
- **Relatórios versionados**: somente agregados/anônimos.
- **PII**: fora do Git; por padrão não vai para relatórios ou Telegram.

## Script

- `scripts/lk_phase5_build_local_sql_20260511.py`

O script reconstrói o SQLite local a partir do approval packet, stock guard e arquivo privado de IDs.
