# Approval packet — Skill Surface Diet LKGOC runtime activation

- Data/hora: 2026-06-29T10:55:27Z
- Dono: Operações Hermes / lk-collection-optimizer
- Pedido: Lucas disse `Seguir` após a aplicação configurada da Skill Surface Diet no profile `lk-collection-optimizer`.
- Status: **aguardando aprovação explícita de restart local do profile**

## Decisão necessária

Ativar a configuração já aplicada da Skill Surface Diet no runtime vivo do Telegram `lk-collection-optimizer`.

## Evidência atual

| Item | Estado |
|---|---|
| `config.yaml` modificado | 2026-06-29T10:46:26Z |
| `AGENTS.md` modificado | 2026-06-29T10:43:34Z |
| skill core modificada | 2026-06-29T10:44:03Z |
| gateway vivo do profile | PID 1006 |
| gateway start | 2026-06-28T19:37:58Z |
| Telegram state | connected |
| API/webhook surfaces | `API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false` |
| conclusão | mudanças estão **configured/readback OK**, mas runtime vivo é anterior ao patch; precisa restart/new session para comprovar active |

## Escopo aprovado anteriormente

Lucas aprovou a aplicação local da Skill Surface Diet. Isso já foi executado com backup, readback, Brain health e receipt.

Este packet é apenas para a etapa separada de **runtime activation**.

## Plano A — ativar agora

1. Não tocar Main/default, Docker, VPS, Traefik, API server, webhook, crons ou outros profiles.
2. Encerrar/reiniciar somente o gateway do profile:
   - `HERMES_HOME=/opt/data/profiles/lk-collection-optimizer`
   - target atual: PID 1006
3. Usar o mecanismo local já existente para managed specialist gateways: `/opt/data/scripts/hermes_all_gateway_watchdog.py` quando apropriado.
4. Verificar pós-restart:
   - PID novo com `HERMES_HOME=/opt/data/profiles/lk-collection-optimizer`;
   - start time posterior a `2026-06-29T10:46:26Z`;
   - Telegram `connected`;
   - API/webhook continuam false;
   - `skills.platform_disabled.telegram` lido como 209 disabled / 31 enabled;
   - core LKGOC habilitado;
   - secret scan `possible_credential_value_hits=0`.
5. Registrar receipt.

## Rollback

Se o gateway não voltar ou se o Telegram falhar:

1. Restaurar backups:
   - `areas/lk/sub-areas/collection-optimizer/backups/skill-surface-diet-apply-20260629T104249Z/AGENTS.md.before`
   - `areas/lk/sub-areas/collection-optimizer/backups/skill-surface-diet-apply-20260629T104249Z/lk-superpowers-collection-optimizer.SKILL.md.before`
   - `areas/lk/sub-areas/collection-optimizer/backups/skill-surface-diet-apply-20260629T104249Z/config.yaml.before`
2. Reiniciar somente o profile `lk-collection-optimizer` novamente.
3. Verificar Telegram connected e config anterior.

## Riscos

- Interrupção breve do bot `lk-collection-optimizer` durante restart local.
- Config check do profile mostra `Config version: 24 → 30`; isso é caveat preexistente e não será migrado neste escopo para evitar ampliar mudança.
- `Seguir` sozinho não deve ser tratado como aprovação universal de runtime quando há restart; por isso este packet separa a decisão.

## Opções

### A — Aprovar restart local do LKGOC agora
Executar somente o restart/verification do profile `lk-collection-optimizer`.

### B — Não reiniciar agora
Manter configured/readback OK; ativação acontece em próxima sessão/restart natural do profile.

### C — Ajustar escopo
Lucas define outro limite, por exemplo migrar config version antes, testar CLI primeiro, ou adiar.

## Recomendação

**A**, se a prioridade for comprovar `active` agora.  
**B**, se não houver urgência e a redução de superfície puder ativar no próximo restart natural.
