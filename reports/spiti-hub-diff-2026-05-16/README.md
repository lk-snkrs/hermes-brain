# Spiti Hub local duplicate diff — 2026-05-16

A: `/opt/data/hermes_bruno_ingest/spiti-hub`
B: `/opt/data/hermes_bruno_ingest/spiti-hub-git`

Excluded: `.git, .next, build, dist, node_modules`

## Counts

- A files: 129
- B files: 127
- Only in A: 2
- Only in B: 0
- Same relative path, different content: 27

## Only in non-Git `spiti-hub`

- `.hermes_source.json`
- `docs/briefing-2026-04-30.md`

## Only in Git `spiti-hub-git`

- none

## Different files

- `src/App.jsx`
- `src/components/DrawerObra.jsx`
- `src/components/Layout.jsx`
- `src/components/ModalLeilao.jsx`
- `src/components/Toast.jsx`
- `src/lib/documentos.js`
- `src/lib/leilao-context.jsx`
- `src/lib/pdfTemplates.jsx`
- `src/lib/segmentos.js`
- `src/pages/AdminAudit.jsx`
- `src/pages/AdminUsuarios.jsx`
- `src/pages/BulkFotos.jsx`
- `src/pages/CampanhaDetalhe.jsx`
- `src/pages/Captacoes.jsx`
- `src/pages/CatalogoPublico.jsx`
- `src/pages/CobrancaPublica.jsx`
- `src/pages/Dashboard.jsx`
- `src/pages/Documentos.jsx`
- `src/pages/Leiloes.jsx`
- `src/pages/Obras.jsx`
- `src/pages/Pedidos.jsx`
- `src/pages/Pessoas.jsx`
- `src/pages/PosLeilao.jsx`
- `src/pages/Resultado.jsx`
- `src/pages/Segmentos.jsx`
- `src/pages/Vendas.jsx`
- `vite.config.js`

## Recommendation

Do not delete `spiti-hub` yet. It has unique files and 27 changed source files versus the canonical Git clone. Next action should be a human/agent review of these diffs and then either merge useful deltas into `spiti-hub-git` or archive the old non-Git directory.
