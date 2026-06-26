# Receipt — Curadoria LK PDP cron source/auth repair

Data UTC: 2026-06-07T21:32Z

## Escopo

Após `Seguir`, revalidei o cron quinzenal de manutenção da Curadoria LK PDP em modo read-only e corrigi a rotina local para não gerar relatório com source stale.

## Evidência antes

- Cron ativo: `7e5ba8b565d5`
- Schedule: `0 11 * * 1` UTC = 08:00 BRT segunda-feira
- Próxima execução observada: `2026-06-08T11:00:00+00:00`
- Delivery: `telegram`
- Mode: `no-agent`
- Script: `/opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py`

Primeira reexecução forçada:

- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T182116-0300.md`
- Problema no JSON: `fetch_ok=false`
- Causa sanitizada: `fatal: could not read Username for 'https://github.com': No such device or address`
- Risco: relatório podia usar `origin/production` local stale e apontar falso amarelo para AJ4 já reconciliado.

## Correção local segura

Patch no script local do profile `lk-shopify`:

- adiciona fallback de GitHub auth read-only via env/Doppler;
- carrega `GITHUB_TOKEN`/`GITHUB_TOKEN_LUCASCIMINO` in-process;
- usa `GIT_ASKPASS` temporário;
- apaga askpass ao fim;
- imprime apenas status sanitizado (`values_printed=false`), nunca token;
- mantém escopo sem Shopify/Admin/DEV/Production write.

Também corrigi a classificação de grupos pequenos:

- grupos intencionais/collab/especiais com `<6` handles agora são `amarelo`/caveat;
- só viram `vermelho` se houver falha dura como URL pública inválida, placeholder ou erro real.

## Evidência depois

Comando verificado:

```bash
python3 -m py_compile /opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py
HERMES_HOME=/opt/data/profiles/lk-shopify /opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py --force
```

Resultado:

- Status: `OK`
- Gerado: `2026-06-07 18:31 BRT`
- Semáforo: verde `50` · amarelo `11` · vermelho `0` · cinza `0`
- Handles públicos checados: `260`
- JSON: `fetch_ok=true`
- Fetch msg: `fetch_ok_doppler_askpass; values_printed=false`
- Render snippets detectados: `lk-variante-cortez-speedcat-20260607`, `lk-variante-onitsuka-versace-gazelle-collabs-20260607`, `lk-variante-top30-visited-v2`
- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T183127-0300.md`

## Interpretação

O cron está ativo e agora deve usar fonte atualizada do GitHub privado no disparo de 2026-06-08 08:00 BRT. Não há vermelho após correção da fonte/classificação. Os 11 amarelos são oportunidades/caveats, principalmente grupos pequenos e um grupo Versace/Onitsuka com produtos públicos porém `available=false`.

## Não-ações

- Nenhum write Shopify.
- Nenhum write em DEV/Production theme.
- Nenhum PR/merge/deploy/publish.
- Nenhum segredo impresso.

## Próxima decisão

Aguardar a execução automática de 2026-06-08 08:00 BRT e conferir se o Telegram recebe o resumo correto. Se Lucas quiser agir nos amarelos, preparar approval packet separado; `Seguir` não autoriza upload/merge.
