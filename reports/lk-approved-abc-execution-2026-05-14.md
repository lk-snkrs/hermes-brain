# LK Approved A/B/C Execution — 2026-05-14

Gerado em: `2026-05-14T14:53:12.136741+00:00`

## Resultado final
- **A — Notion/Júlio:** concluído. Criados **15** cards em `[LK] Encomenda`; duplicados/skip: 0; erros: 0.
- **B — 12 URLs 404:** concluído em modo read-only. Todos os 12 handles existem no Shopify, mas estão **DRAFT**, por isso a URL pública retorna 404. Nenhum redirect/produto/Shopify foi alterado.
- **C — 68 atributos GMC:** concluído. Foram agrupadas 68 linhas em **64** produtos; patch Merchant API v1 executado; readback atrasado fechou 62/64; reparo pontual fechou 2/2; `productstatuses` final: **{'no_target_attr_issue': 64}**.

## Pacote B — diagnóstico das 12 URLs
- `online:pt:BR:15031239196158973196` — `nike-air-force-1-07-white` — Shopify `DRAFT` — Tênis Nike Air Force 1 '07' "White" Branco
- `online:pt:BR:9250025623243509812` — `calca-saint-studio-wide-alfaiataria-risca-de-giz-preta` — Shopify `DRAFT` — Calça Saint Studio Wide Alfaiataria Risca de Giz Preta
- `online:pt:BR:13622509763707629816` — `calca-saint-studio-wide-alfaiataria-risca-de-giz-cinza` — Shopify `DRAFT` — Calça Saint Studio Wide Alfaiataria Risca de Giz Cinza
- `online:pt:BR:10591784840915585992` — `bone-saint-studio-art-department-azul` — Shopify `DRAFT` — Boné Saint Studio Art Department Azul
- `online:pt:BR:3876299146406606317` — `calca-saint-studio-jeans-baggy-preta` — Shopify `DRAFT` — Calça Saint Studio Jeans Baggy Preta
- `online:pt:BR:10002025469927148791` — `calca-nude-project-jeans-soft-velvet-azul-marinho` — Shopify `DRAFT` — Calça Nude Project Jeans Soft Velvet Azul Marinho
- `online:pt:BR:1624428988081867066` — `bone-aime-leon-dore-porsche-nylon-logo-aspen-gold-amarelo` — Shopify `DRAFT` — Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo
- `online:pt:BR:6562590402534581177` — `calca-nude-project-illegal-jeans-ash-cinza` — Shopify `DRAFT` — Calça Nude Project Illegal Jeans Ash Cinza
- `online:pt:BR:2258634078163248862` — `calca-chino-saint-studio-supima-preto` — Shopify `DRAFT` — Calça Chino Saint Studio Supima Preto
- `online:pt:BR:13498809788548851139` — `moletom-essentials-fear-of-god-jet-black-ss24-preto` — Shopify `DRAFT` — Moletom Essentials Fear of God Jet black SS24 Preto
- `online:pt:BR:4041641007094962608` — `camisa-saint-studio-trico-palha` — Shopify `DRAFT` — Camisa Saint Studio Trico Palha
- `online:pt:BR:11314792792398542744` — `moletom-oversized-nylon-fear-of-god-essentials-jet-black-preto` — Shopify `DRAFT` — Moletom Oversized Nylon Fear of God Essentials Jet Black Preto

## Pacote C — verificação final
- `products.get` atrasado: {'match': 62, 'mismatch': 2}
- Reparo pontual: {'match': 2}
- `productstatuses` alvo: checked_ids=64, status_counts={'no_target_attr_issue': 64}, issue_counts={}

## Snapshots privados de rollback
- Snapshot principal C: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-c-attrs-rollback-20260514T145344Z.json`
- Snapshot reparo C: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-c-attrs-point-repair-rollback-20260514T145948Z.json`

## Arquivos públicos
- `reports/lk-approved-abc-execution-2026-05-14.json`
- `reports/lk-approved-abc-execution-2026-05-14.md`
- `reports/lk-approved-c-attrs-delayed-readback-2026-05-14.json`
- `reports/lk-approved-c-attrs-point-repair-readback-2026-05-14.json`
- `reports/lk-approved-c-attrs-poststatus-recheck-2026-05-14.json`

## Não executado
- Compra/reserva/pagamento.
- WhatsApp/fornecedor/grupo.
- Shopify write, publish, redirect ou feed upload.
- Tiny, preço, availability, title, categoria, campanha.
