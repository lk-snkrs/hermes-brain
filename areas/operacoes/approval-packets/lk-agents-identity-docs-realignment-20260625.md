# Approval packet — LK agents identity/docs realignment

Generated at: `2026-06-25T18:02:05.877890+00:00`

## Pedido

Corrigir drift entre Brain, SOUL, AGENTS, MAPA, MEMORY e skills dos agentes LK, após confirmação de contaminação Growth no `lk-collection-optimizer/SOUL.md`.

## Recomendação

Aprovar **Fase 1 — realinhamento documental local + smoke read-only**, sem restart automático.

## Escopo aprovado se Lucas responder “Aprovo Fase 1”

- Profiles: `lk-growth`, `lk-shopify`, `lk-collection-optimizer`, `lk-stock`, `lk-trends`, `lk-finance`, `lk-content`, `lk-ops`, `lk-analyst-readonly`, `lk-content-reviewer`.
- Criar backups locais timestamped antes de qualquer edição.
- Corrigir `SOUL.md` do `lk-collection-optimizer` para identidade `[LK] Otimização de Coleções / LKGOC`.
- Criar/normalizar `MAPA.md` e `MEMORY.md` root mínimos onde ausentes, com ponteiros para Brain canônico e skills, sem duplicar documentos longos.
- Verificar presença de skill específica por profile; para support profiles, registrar justificativa.
- Criar smoke harness local/read-only para identidade e roteamento.
- Rodar smoke read-only por profile, sem writes externos.
- Gerar relatório + receipt + secret scan + Brain health.

## Fora de escopo

- Restart de gateway.
- Cron migration.
- Docker/VPS/Traefik/secrets.
- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail writes.
- Mudança em Honcho provider ou limpeza destrutiva de memória.

## Risco

Baixo/médio: muda prompt/docs locais de profiles. Pode afetar comportamento no próximo run; por isso precisa backup, diff e smoke antes de restart.

## Rollback

Restaurar arquivos dos backups timestamped por profile. Como Fase 1 não reinicia gateways, rollback é local e imediato.

## Aprovação sugerida

`Aprovo Fase 1 — realinhar docs/SOUL/MAPA/MEMORY dos agentes LK com backup e smoke read-only, sem restart nem writes externos.`
