# Curadoria LK — Force clone publish + rollback receipt — 2026-06-03

## Aprovação

Lucas aprovou publicar o clone force-fix após QA preview aprovado.

## Ação executada

- Publicado clone: `156623372510` — `LK Curadoria Force Fix Preview 2026-06-03`
- Tema anterior/live antes do publish: `155065417950` — `lk-new-theme/production`

## Resultado do publish

Shopify aceitou o publish: clone virou `main`.

Evidência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/publish-response.json`

## QA live pós-publish

Foram executadas 6 rodadas de espera/QA pós-publish.

- Passou 100%: `False`
- OK na última rodada: Canonical NB 530
- Ainda stale na última rodada: AJ1 Mid, AJ1 High, Shox TL, Foam Runner, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae

Interpretação: mesmo com novo theme ID/main, as PDPs afetadas continuaram servindo HTML antigo sem o marker `lk-variante-force-20260603`. O canônico NB 530 entrou no caminho novo, mas os handles problemáticos não.

Evidência QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/live-qa-after-publish/live-qa-post-publish-wait.json`

## Rollback executado

Como o QA live falhou, foi executado rollback conforme aprovado:

- Republicado tema anterior: `155065417950`
- Clone voltou para `unpublished`: `156623372510`

Evidência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/rollback-response.json`

## Smoke pós-rollback

- Smoke sem Liquid error: `True`
- Testado: Home, NB 530, AJ1 High, Shox TL

Evidência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/live-qa-after-rollback/rollback-smoke-qa.json`

## Estado atual

- Tema main atual: `155065417950`
- Clone force-fix preservado como unpublished: `156623372510`
- Problema original de stale HTML nas PDPs afetadas persiste.
- Monitor passivo antigo foi encerrado por ter ficado inválido após publish/rollback.

## Aprendizado

Trocar o theme ID/main não foi suficiente para invalidar o render cache das PDPs afetadas. Isso reforça hipótese de cache/render persistente por produto/rota na Shopify ou camada interna não controlável por Theme Asset API.

## Próximos caminhos possíveis

1. Escalar pacote para Shopify Support com evidência adicional de que até publish/rollback de tema não invalidou as PDPs afetadas.
2. Criar novas URLs/handles/canonical redirects temporários para os produtos afetados — alto risco SEO/operacional; exige plano separado.
3. Migrar Curadoria para render client-side externo/injetado por asset global que carregue mesmo em HTML antigo — precisaria de um asset já referenciado pelo HTML stale ou mudança em app/theme global que o cache antigo ainda carregue.
