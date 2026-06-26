# Correção Doppler-first — LK Growth

Data UTC: 2026-06-07

## Sintoma reportado

Lucas recebeu no LK Growth a mensagem: "O Doppler não carregou nesse shell por falta de project configurado...".

## Causa raiz

Erro operacional meu na Fase 4 anterior:

1. Eu padronizei o caminho de recuperação do watchdog para usar o helper Doppler-first nos perfis `managed`.
2. Eu reiniciei e validei somente `lk-content`.
3. Eu não reiniciei o processo vivo de `lk-growth`, então ele continuou rodando sem `DOPPLER_PROJECT`, `DOPPLER_CONFIG` e sem os secrets esperados no ambiente do gateway.
4. Além disso, as cópias da skill `doppler-secrets-operations` dentro de perfis como `lk-growth` estavam antigas; eu tinha verificado presença da skill, mas não sincronizei conteúdo/versão. O agente em LK Growth carregou instruções antigas e tentou usar Doppler CLI sem `--project lc-keys --config prd` / sem helper universal.

## Correção aplicada

- Reiniciado somente o gateway `lk-growth` pelo watchdog global Doppler-first.
- PID antigo: `207`.
- PID novo: `27994`.
- Processo novo verificado com:
  - `HERMES_HOME=/opt/data/profiles/lk-growth`;
  - `API_SERVER_ENABLED=false`;
  - `WEBHOOK_ENABLED=false`;
  - `DOPPLER_PROJECT=lc-keys`;
  - `DOPPLER_CONFIG=prd`;
  - `DOPPLER_TOKEN_in_child=false`;
  - secrets esperados do LK Growth presentes: `9/9`, por presença booleana apenas.
- Sincronizada a skill canônica `doppler-secrets-operations` para os 13 perfis especialistas em `/opt/data/profiles/*/skills/devops/doppler-secrets-operations`, com backups `.bak-sync-20260607T165901Z`.

## Validação

- Helper `run --profile lk-growth` testado: `9/9` secrets esperados presentes, `DOPPLER_TOKEN_in_child=false`.
- `hermes gateway status` do LK Growth: running, PID `27994`.
- Watchdog global: `rc=0`, stdout vazio.
- Skill do LK Growth contém instrução do helper universal `/opt/data/scripts/hermes_doppler.py`, `run --profile <profile>`, e remoção de `DOPPLER_TOKEN` no child env.

## Guardrails

- Nenhum valor de secret impresso.
- Nenhum secret copiado para Brain/skills/Telegram.
- Sem Docker/VPS/Traefik/Main.
- Sem writes em Shopify/Klaviyo/Google/Meta/etc.

## Status

Corrigido. A falha foi minha: confundi "watchdog preparado para futuro restart" com "processo vivo já está com Doppler-first" e também tratei presença de skill como se fosse versão atualizada.

`values_printed=false`.
