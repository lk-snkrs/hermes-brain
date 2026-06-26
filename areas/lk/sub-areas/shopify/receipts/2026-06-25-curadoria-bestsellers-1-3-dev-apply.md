# Receipt — DEV Curadoria LK PDP / Bestsellers 1–3

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Escopo aprovado interpretado:** resposta curta “Aprovo” ao packet `2026-06-24-curadoria-bestsellers-1-3-pdp.md` foi tratada com segurança como aprovação **DEV/unpublished only**, não como merge Production, porque o packet tinha duas aprovações possíveis.
- **Writes executados:** Shopify Asset API somente no tema DEV/unpublished.
- **Writes NÃO executados:** nenhum merge/PR Production; nenhum produto/preço/estoque/GMC/Klaviyo.

## Temas verificados

| Ambiente | Theme ID | Nome | Role |
|---|---:|---|---|
| DEV | `155065450718` | `lk-new-theme/dev` | `unpublished` |
| Production | `155065417950` | `lk-new-theme/production` | `main` |

## Assets alterados em DEV

1. `snippets/lk-variante-top30-visited-v2.liquid`
   - Upload status: `200`
   - Readback DEV: OK na tentativa 2
   - SHA DEV: `cf980ccce9cf972dbc84c0ed7601b14ed389ccbfbafe8a4c40d2eddc79d3a3a2`
   - Bytes: `260552`
2. `snippets/lk-variante-bestsellers-1-3-20260624.liquid`
   - Upload status: `200`
   - Readback DEV: OK na tentativa 1
   - SHA DEV: `b29e8f872a676069feacbf38f37b3b3ad4aa0334027b26c81977f2011bcf3cf9`
   - Bytes: `16930`

## Grupos incluídos

- `top30-mexico66-regular-expansion-20260624`
- `top30-mexico66-sabot-expansion-20260624`
- `top30-mexico66-sd-expansion-20260624`
- `top30-nb-9060-expansion-20260624`
- `top30-adidas-samba-og-expansion-20260624`
- `top30-adidas-samba-jane-20260624`

## QA / readback

Relatório principal:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/dev-apply/20260625T100424Z_dev_apply_readback.json`

Resultado:

- DEV readback dos 2 assets: **OK**.
- Production SHA/readback: **unchanged**.
- Render line no `top30-visited-v2`: **presente**.
- Marker counts: **1/1** para cada um dos 6 grupos.
- Classes canônicas: presentes (`lk-variante`, `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`).
- Classes proibidas: `lk-variante__grid=0`, `lk-variante__image-wrap=0`.
- URL malformada `https:https://` / `https://https://`: **ausente**.

Preview público:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/dev-apply/20260625T100455Z_public_preview_probe.json`

- 6/6 PDPs responderam HTTP 200.
- `preview_theme_id` foi removido/redirecionado nas URLs finais.
- Markers novos não apareceram no HTML público porque a captura caiu no live/canonical, não no preview autenticado.
- Classificação: **preview público inconclusivo**, não falha de source/readback.

## Backups

Backups pré-write foram salvos em:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/dev-apply/`

Incluem snapshots DEV/Production dos assets envolvidos quando existentes.

## Rollback DEV

1. Restaurar o backup DEV de `snippets/lk-variante-top30-visited-v2.liquid` salvo no diretório acima.
2. Remover ou restaurar ausência anterior de `snippets/lk-variante-bestsellers-1-3-20260624.liquid` se necessário.
3. Repetir Asset API readback e confirmar Production unchanged.

## Próxima decisão

Para levar este mesmo escopo para Production pelo fluxo correto:

`Aprovo merge Production Curadoria Bestsellers 1-3`

A execução esperada é GitHub branch/PR → merge em `production` → Shopify sync/readback → public QA multi-round.
