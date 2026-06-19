# Robots.txt format fix — receipt

Data UTC: `2026-06-18T22:42:14Z`
Execution dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/robots-semrush-format-20260618/execution-format-fix-20260618T224149Z`
values_printed=false

## Escopo aprovado

Correção de formato em `templates/robots.txt.liquid` no production theme.

## Executado

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Asset: `templates/robots.txt.liquid`
- Backup salvo: `robots-before.liquid`
- Proposta salva: `robots-after.proposed.liquid`
- Readback salvo: `robots-readback.liquid`

## Mudança aplicada

Removidas 2 linhas em branco internas que separavam `Disallow` de `Allow` dentro dos grupos:

- bloco `User-agent: *`
- bloco `User-agent: Googlebot`

Nenhuma regra foi alterada.

## Validação pública

- URL: `https://lksneakers.com.br/robots.txt`
- HTTP: `200`
- Content-Type: `text/plain; charset=utf-8`
- Parser estrito no arquivo público: `0` erros.
- `User-agent: SemrushBot` permanece com `Disallow: /`, conforme escopo conservador aprovado.

## Rollback

Restaurar `robots-before.liquid` no mesmo asset.
