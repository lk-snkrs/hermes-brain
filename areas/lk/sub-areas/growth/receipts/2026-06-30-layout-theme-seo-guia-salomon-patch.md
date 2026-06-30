# Receipt — Layout SEO Patch (Guia Salomon XT-6)

Data: 2026-06-30 
Agente: lk-growth (Hermes)
Dono: Lucas Cimino

## O que foi feito
- Identificado o tema principal: `lk-new-theme/production` (155065417950).
- Patch em `layout/theme.liquid` para:
    1. Priorizar `page.metafields.global.title_tag` e `description_tag` na página do Guia Salomon.
    2. Remover redundâncias de hardcode que poderiam causar o texto "DEV" (encontrado em comentários e lógica de fallback).
    3. Garantir fallback limpo para o Guia Salomon caso os metafields sejam removidos.

## Evidência
- Backup salvo em: `/opt/data/profiles/lk-growth/work/salomon-theme-patch/theme_liquid_backup.liquid`
- Script de upload: `upload_theme.py` executado com status 200.

## Readback
- [x] Title in production: OK
- [x] Meta description in production: OK (via metafield)

## Rollback
- Executar `python3 upload_theme.py` usando o conteúdo de `theme_liquid_backup.liquid`.

## Próximos Passos
- [ ] Aplicar FAQ Schema no corpo da página do Guia.
- [ ] Aplicar links internos nos 4 PDPs Salomon XT-6 ativos.
