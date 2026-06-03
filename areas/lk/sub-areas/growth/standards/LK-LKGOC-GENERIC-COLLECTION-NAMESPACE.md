# LK LKGOC — namespace genérico para coleções editoriais

Atualizado: 2026-06-03T00:02:35Z

## Decisão
O padrão visual que nasceu no New Balance 204L deve deixar de usar namespace específico de produto (`lk-204l-*`) e passar a usar namespace genérico LKGOC para coleções editoriais premium.

## Namespace canônico novo

- `lk-lkgoc-coll-preview`
- `lk-lkgoc-coll-preview__inner`
- `lk-lkgoc-copy`
- `lk-lkgoc-kicker`
- `lk-lkgoc-read-more`
- `lk-lkgoc-collage`
- `lk-lkgoc-card`
- `lk-lkgoc-card--large`
- `lk-lkgoc-open-photo`
- `lk-lkgoc-photo-modal`
- `lk-lkgoc-photo-modal__close`
- `lk-lkgoc-guide-panel` quando o guia for específico do padrão LKGOC; manter compatível com `lk-guide-standard-panel` durante migração.

## Política de migração segura

1. Não fazer troca seca em produção.
2. Primeiro criar aliases CSS/JS para suportar `lk-204l-*` e `lk-lkgoc-*` juntos.
3. Migrar 204L em DEV para emitir classes LKGOC novas mantendo aliases antigos enquanto houver dependências.
4. Migrar Sambae e próximas coleções para já nascerem LKGOC.
5. Só depois de QA visual e funcional remover dependências antigas, se necessário.

## QA obrigatório antes de produção

- 204L desktop/mobile: hero, collage, modal, botão Ler mais, guia pós-grid.
- Sambae desktop/mobile: paridade com 204L.
- Render público/preview sem depender de cookie especial.
- Asset readback.
- Screenshot desktop/mobile.
- Rollback com assets before.

## Guardrail
Writes em `lk-new-theme/production` exigem aprovação explícita do Lucas no turno atual.
