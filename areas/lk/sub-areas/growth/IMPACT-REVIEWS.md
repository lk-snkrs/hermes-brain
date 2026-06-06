# LK Growth OS — Política de impact reviews

Última revisão: 2026-05-19.

## Princípio

Toda mudança Growth/SEO/CRO aprovada e executada precisa gerar accountability posterior. O follow-up deve nascer no profile especialista `lk-growth`, entregar no canal do LK Growth OS e rodar em modo read-only.

## Regra permanente

Depois de qualquer execução aprovada em SEO/CRO/GMC/GEO/Shopify SEO fields/tema dev ou produção:

1. Criar baseline antes ou durante a execução, quando possível.
2. Salvar artefatos com data em `reports/` e/ou `areas/lk/sub-areas/growth/rotinas/`.
3. Criar cron one-shot no profile `lk-growth`, não no Hermes principal.
4. Entregar no canal `@LKGrowth_HermesBot`/home do profile `lk-growth`.
5. Usar apenas fontes read-only.
6. Declarar limites de amostra, sazonalidade e atraso de dados.
7. Nunca executar novo write como parte do impact review; gerar apenas approval packets.

## Comando padrão

Usar o profile isolado:

```bash
HERMES_HOME=/opt/data/profiles/lk-growth /opt/hermes/.venv/bin/hermes cron create '<ISO ou cron>' '<prompt self-contained>' \
  --name 'LK Growth OS <nome do impact review>' \
  --deliver telegram \
  --repeat 1 \
  --skill lk-seo-weekly-improvement \
  --skill lk-shopify-readonly \
  --skill doppler-secrets-operations \
  --skill seo-google \
  --workdir /opt/data/hermes_bruno_ingest/hermes-brain
```

## Impact review migrado em 2026-05-19

### SEO title/meta P1 packets — mudanças aplicadas em 2026-05-18

- Job antigo no Hermes principal: `a7e883edd200`.
- Status antigo: pausado após migração.
- Novo job no `lk-growth`: `c45cda5fe2df`.
- Nome novo: `LK Growth OS SEO/CRO impact review — SEO title/meta P1 packets`.
- Schedule: `2026-05-25T14:34:23Z`.
- Deliver: `telegram` no profile `lk-growth`.
- Prompt salvo em: `/opt/data/profiles/lk-growth/cron-prompts/seo-impact-review-20260525.md`.
- Referência de execução: `lk-seo-weekly-improvement/references/approved-seo-fields-execution-impact-review-20260518.md`.

## Métricas mínimas por impact review

- URLs/handles afetados.
- Data/hora da mudança.
- Fonte e freshness dos dados.
- Antes/depois quando houver baseline:
  - sessões/visitas;
  - conversão;
  - pedidos/receita;
  - GSC impressões/cliques/CTR/posição;
  - GMC status quando aplicável;
  - CWV/PSI/CrUX quando aplicável.
- Separar collections, PDPs e páginas institucionais.
- Veredito: melhorou, neutro, piorou ou inconclusivo.
- Próximo passo: manter, reverter, iterar, ou criar approval packet.

## Restrições

Impact review não autoriza:

- Shopify writes;
- GMC writes;
- GSC/GA4 writes;
- theme publish/merge;
- campanha/envio externo;
- preço, estoque, SKU, produto, coleções;
- contato com clientes/fornecedores/time.

Qualquer ação produtiva posterior precisa de novo preview + aprovação explícita do Lucas.

## Impact review criado em 2026-06-05

### Product operational copy cleanup — descrições/SEO/WhatsApp URL

- Mudança executada: 2026-06-05.
- Escopo: limpeza de termos operacionais customer-facing em product descriptions/body_html, product SEO e WhatsApp URL text; preservados `Sujeito a encomenda`, `sob encomenda`, prazo 4–6 semanas, tags, variantes, estoque, preço, theme e checkout.
- Baseline: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/product-description-operational-copy-cleanup-baseline-20260605T191325Z`.
- QA final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/product-audits/final-product-operational-terms-qa-20260605T190954Z`.
- Job D+7 no `lk-growth`: `12b96a478751`.
- Nome: `LK Growth OS impact review D+7 — product operational copy cleanup`.
- Schedule: `2026-06-12T19:15:00Z`.
- Deliver: `telegram` no profile `lk-growth`.
- Prompt salvo em: `/opt/data/profiles/lk-growth/cron-prompts/product-description-operational-copy-cleanup-d7-20260612.md`.
- Modo: read-only; qualquer nova alteração vira approval packet, sem write automático.

