# LK Growth — GEO llms.txt root production receipt — 2026-05-22

## Status

- Resultado: **aplicado e verificado publicamente**.
- Aprovação: Lucas aprovou o Packet A em 2026-05-22.
- Ambiente: Shopify theme production `lk-new-theme/production`.
- Theme ID: `155065417950`.
- Escopo aprovado: corrigir `/llms.txt` e `/llms-full.txt` para incluir contexto comercial LK e P1s GEO.

## O que foi feito

1. Backup/readback dos assets envolvidos via Shopify Admin API.
2. Criados/atualizados templates de override:
   - `templates/llms.txt.liquid`
   - `templates/llms-full.txt.liquid`
3. Verificação pública mostrou que Shopify ainda servia `/llms.txt` e `/llms-full.txt` a partir de `templates/agents.md.liquid`.
4. Aplicado patch seguro em `templates/agents.md.liquid`, preservando as instruções agentic existentes e inserindo o bloco `LK commercial context for AI Search / GEO`.
5. Readback do asset confirmou hash esperado.
6. Verificação pública com cache-busting confirmou os marcadores P1 nos três endpoints:
   - `/llms.txt`
   - `/llms-full.txt`
   - `/agents.md`

## Verificação pública

- `/llms.txt`
  - HTTP: `200`
  - Content-Type: `text/markdown; charset=utf-8`
  - Tamanho: `6230`
  - SHA256 público: `24183dd47482bc24cba5e3179689063ce1a723ea8060e11065bdfcd51c3c1cb8`
  - Marcadores P1: `8/8`

- `/llms-full.txt`
  - HTTP: `200`
  - Content-Type: `text/markdown; charset=utf-8`
  - Tamanho: `6230`
  - SHA256 público: `24183dd47482bc24cba5e3179689063ce1a723ea8060e11065bdfcd51c3c1cb8`
  - Marcadores P1: `8/8`

- `/agents.md`
  - HTTP: `200`
  - Content-Type: `text/markdown; charset=utf-8`
  - Tamanho: `6230`
  - SHA256 público: `24183dd47482bc24cba5e3179689063ce1a723ea8060e11065bdfcd51c3c1cb8`
  - Marcadores P1: `8/8`

Marcadores verificados:

- `New Balance 204L`
- `Nike Mind 001`
- `Onitsuka Tiger Mexico 66`
- `Adidas Samba Jane`
- `Air Jordan Travis Scott`
- `Lululemon`
- `Kill Bill`
- `onitsuka-tiger-todos-os-modelos`

## Assets e hashes

### `templates/agents.md.liquid`

- Before SHA256: `2c5673f6bc88aaafbfabff98a852e024b411fcb678389e3a987b65815fb1255e`
- After SHA256: `6fb37769e639c5a3cefc080910814a565566573583ba97a6414900b28ed56d43`
- Readback SHA256: `6fb37769e639c5a3cefc080910814a565566573583ba97a6414900b28ed56d43`
- Readback: match

### `templates/llms.txt.liquid`

- Criado/atualizado como tentativa de override nativo.
- Readback: match.
- Observação: no momento da verificação, Shopify ainda entregava o conteúdo de `templates/agents.md.liquid` em `/llms.txt`.

### `templates/llms-full.txt.liquid`

- Criado/atualizado como tentativa de override nativo.
- Readback: match.
- Observação: no momento da verificação, Shopify ainda entregava o conteúdo de `templates/agents.md.liquid` em `/llms-full.txt`.

## Rollback

Backups locais:

- Tentativa `llms`/`llms-full`:
  - `/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-geo-llms-root-155065417950-20260522T163822Z/`
- Patch efetivo `agents.md`:
  - `/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-geo-agents-root-155065417950-20260522T164128Z/`

Rollback principal:

1. Restaurar `templates/agents.md.liquid` a partir de:
   - `templates__agents.md.liquid.before.liquid`
2. Opcionalmente remover/restaurar os overrides:
   - `templates/llms.txt.liquid`
   - `templates/llms-full.txt.liquid`
3. Validar publicamente:
   - `https://lksneakers.com.br/llms.txt`
   - `https://lksneakers.com.br/llms-full.txt`
   - `https://lksneakers.com.br/agents.md`

## Observação técnica importante

Apesar de fontes públicas indicarem que `templates/llms.txt.liquid` poderia sobrescrever `/llms.txt`, na LK em 2026-05-22 o endpoint raiz continuou servindo o template `templates/agents.md.liquid`. Por isso, o fix efetivo foi inserir o contexto GEO no `agents.md` preservando as instruções agentic existentes.

## Próximo impacto review

- Criar revisão D+7 read-only para checar:
  - se os endpoints continuam com 8/8 marcadores;
  - se Google/AI Search começa a associar LK aos P1s;
  - se há mudança em GSC/GA4/Shopify para as coleções P1 quando houver dado suficiente.
