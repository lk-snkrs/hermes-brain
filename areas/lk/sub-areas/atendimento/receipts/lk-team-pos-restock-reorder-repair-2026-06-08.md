# Receipt — reparo ordem fila POS restock

Executado em: 2026-06-08T14:19:08.906376+00:00
Causa: processo antigo ainda usava ordenação lexicográfica e avançou 1→10→11→12.
Correção operacional: reordenei a fila pelo campo numérico `position` e reativei/enviei o item 2/14.
Próximo ativo: 2/14 — 1183A872-204-6 — Tam 39
Backup: `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/state.before-reorder-pos-restock-to-item2-20260608-20260608T141859Z.json`
Escopo negativo: sem compra/fornecedor/Shopify/Tiny write.
Secrets: values_printed=false.