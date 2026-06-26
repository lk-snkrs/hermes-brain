# Incidente LKGOC — Adidas Samba guia/hero fora do padrão

Data UTC: 2026-06-03T19:21:54.136566+00:00

## Causa-raiz
- O snippet `lk-samba-204l-guide-v2` foi adaptado a partir de padrão legado `lk-guide-standard-*`/`lk-lkgoc-*`, sem portar o contrato visual completo do Gold Source 204L.
- O bloco ficou com largura/tipografia diferentes porque o QA anterior validou presença de HTML, mas não mediu CSS computado no browser.
- O botão `Ler mais` do hero mobile existia, mas não estava ligado ao estado visual da collage de fotos no mobile.

## Correção aplicada no DEV
- Tema: `155065450718` / `lk-new-theme/dev` / role `unpublished` verificado.
- `snippets/lk-samba-204l-guide-v2.liquid`: CSS escopado com contrato `width:min(1180px,calc(100vw - 32px))`, `max-width:1180px`, tipografia/paridade mobile.
- `snippets/lk-samba-204l-hero-v2.liquid`: `Ler mais` no mobile alterna `.is-photos-open`, controla `aria-expanded` e revela `.lk-goc-collage`.

## QA obrigatório daqui para frente
Antes de pedir aprovação visual de LKGOC:
1. Readback Asset API precisa bater para todos os assets alterados.
2. Browser real desktop deve medir:
   - guide width = 1180px em desktop amplo;
   - max-width computado = 1180px;
   - título no padrão Gold Source.
3. Browser real mobile deve medir:
   - guide width = viewport - 32px;
   - título mobile = 34px quando aplicável;
   - `Ler mais` muda `aria-expanded=false` para `true`;
   - collage muda de `display:none` para `display:grid` e mostra 3 imagens.
4. Não aceitar QA apenas por HTML/string count quando houver queixa visual.

## Receipt
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-adidas-samba-guide-hero-mobile-fix-20260603T191902Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-adidas-samba-final-public-qa-20260603T191954Z/cdp-qa.json`
