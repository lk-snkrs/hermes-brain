# Próximo gate — pós sequência 1/2/3

- Criado UTC: 2026-06-22T17:45:32.581264+00:00
- Modo: read-only planning; writes externos: 0.
- Base: sequência aprovada `Alo redirect`, `Crocs collection FAQ lite`, `GMC micro-piloto 10`.

## Trava anti-retrabalho continua ativa

Não propor novas alterações nas páginas já trabalhadas hoje:
- `/collections/alo-yoga` / redirect para `/collections/alo-yoga-1`.
- `/collections/crocs-relampago-mcqueen`.
- 10 offers GMC do micro-piloto.

Próximas ações nessas superfícies devem ser apenas:
- QA/readback;
- impact review;
- rollback se necessário.

## Próximo gate recomendado

### A. GMC D+1 stickiness check

Objetivo: confirmar que Simprosys/local feed não sobrescreveu `linkTemplate`, `mobileLinkTemplate` e `adsRedirect` nos 10 offers.

Critério para considerar estável:
- 10/10 com `{store_code}` nos 3 campos.
- 0/10 com issue `mhlsf_full_missing_valid_link_template`.
- Sem novos erros de leitura.

Se estável: preparar approval packet de **lote 100** ou **lote 500**, não executar automaticamente.

### B. Alo/Crocs GSC watch

Objetivo: medir se:
- `/collections/alo-yoga` deixa de cair na home e transfere sinais para `/collections/alo-yoga-1`.
- `/collections/crocs-relampago-mcqueen` melhora parsing/CTR com FAQPage.

Janela mínima: 7 dias.

### C. Anti-rework opportunity refresh

Rodar GSC/GA4 excluindo quarentena operacional antes de qualquer novo packet de SEO/CRO.

## Approval boundary

- Não escalar GMC sem aprovação explícita nova.
- Não mexer em Crocs/Alo novamente sem impact review ou rollback.
