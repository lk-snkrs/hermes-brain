# Receipt — rollback n8n para rota v2 texto após não recebimento com imagem

Data UTC: 2026-05-20T12:08:30.123491Z

## Motivo

Lucas confirmou que o teste com `HEADER IMAGE` via link (`IMG120032`) não chegou no WhatsApp.

## Ação

Workflow `kWQbmEMuvdipcGjd` restaurado para o backup pré-patch de imagem:

`/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-v3-image-hybrid-patch-20260520T120131Z.json`

## Verificação

- HTTP PUT n8n: `200`
- `active`: `False`
- Node Crisp: `Crisp Send lk_checkout_abandonado_30min_v2`
- Template v2 presente: `True`
- HEADER IMAGE ausente: `True`

## Observação

Foi enviado em paralelo um diagnóstico com WhatsApp Media ID (`MID120757`) para validar se a falha é específica do header por link.
