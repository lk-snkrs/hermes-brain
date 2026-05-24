# Revisão de watchdogs `origin` / silent-OK — 2026-05-22

Status: **análise e brief apenas**. Nenhum cron, schedule, delivery, script, gateway ou runtime foi alterado.

## Fonte viva

Fonte: `cronjob list` em 2026-05-22 ~12:06 UTC.

Resumo vivo:

- Jobs totais: 29.
- Candidatos revisados nesta rodada: watchdogs/script-only `no_agent` com `deliver=origin` e possibilidade de ruído.
- Últimos status observados nos candidatos: `ok`.
- Erros explícitos de delivery: nenhum observado.

## Critério de classificação

- **Seguro para considerar `local` depois de aprovação**: script é silent-OK, stdout só em alerta/falha/auto-heal, e mudar delivery não altera execução.
- **Manter `origin` por enquanto**: saída normal pode ser relatório obrigatório/decisão, ou o job entrega valor diretamente a Lucas.
- **Não executar manualmente nesta revisão**: scripts de gateway podem reiniciar processos se detectarem ausência; esta rodada foi leitura/brief, não ação runtime.

## Revisão por job

### 1. Hermes runtime + cron watchdog no_agent

- Job: `edd06fe19397`.
- Script: `/opt/data/scripts/hermes_runtime_cron_watchdog.py`.
- Schedule: `*/30 * * * *`.
- Delivery atual: `origin`.
- Contrato no script:
  - exit 0 + stdout vazio: OK/silent.
  - exit 0 + stdout: alerta operacional.
  - non-zero: falha do watchdog.
- Ações do script: read-only; não reinicia Docker/gateway, não altera cron e não envia externo.
- Classificação: **seguro para considerar `local`/manter alerta via stdout? Parcial**.
- Recomendação: manter `origin` se Lucas quer ser avisado de drift runtime crítico; se estiver gerando ruído de falsos positivos, migrar para `local` só junto com uma rota de alerta alternativa ou ajuste fino do script.
- Rollback se mudar delivery: `cronjob update edd06fe19397 deliver=origin`.

### 2. Hermes compression failure self-heal watchdog

- Job: `4bb4e2223fd3`.
- Script: `/opt/data/scripts/hermes_compression_failure_self_heal.py`.
- Schedule: `*/10 * * * *`.
- Delivery atual: `origin`.
- Contrato no script:
  - exit 0 + stdout vazio: sem falha nova ou já tratada.
  - exit 0 + stdout: report/brief acionável.
  - non-zero: falha do watchdog.
- Observação: script pode aplicar auto-heal local em código/testes Hermes para classificador de erro transitório; não reinicia gateway/container.
- Classificação: **manter `origin` por enquanto**.
- Motivo: quando imprime, normalmente quer informar auto-heal ou falha de contexto; enviar para Lucas pode ser útil por ser autorremediação sensível, mesmo local.
- Rollback se mudar delivery: `cronjob update 4bb4e2223fd3 deliver=origin`.

### 3. Mordomo Telegram gateway watchdog

- Job: `ac0b440e2643`.
- Script: `/opt/data/scripts/mordomo_gateway_watchdog.sh`.
- Schedule: every 1m.
- Delivery atual: `origin`.
- Contrato observado:
  - se gateway está rodando: exit 0, stdout vazio.
  - se gateway está parado: tenta iniciar o profile `/opt/data/profiles/mordomo` e imprime sucesso/falha.
- Ações do script: pode iniciar processo `hermes gateway run` do profile Mordomo; não mexe Docker/compose/main gateway.
- Classificação: **manter `origin` por enquanto**.
- Motivo: stdout indica reinício real de gateway, ação operacional relevante; Lucas deve saber até haver política explícita de auto-heal silencioso para perfis secundários.
- Rollback se mudar delivery: `cronjob update ac0b440e2643 deliver=origin`.

### 4. LK Growth Telegram gateway watchdog

- Job: `876d54c62ccd`.
- Script: `/opt/data/scripts/lk_growth_gateway_watchdog.sh`.
- Schedule: every 1m.
- Delivery atual: `origin`.
- Contrato observado:
  - se gateway está rodando: exit 0, stdout vazio.
  - se parado: tenta reiniciar profile `/opt/data/profiles/lk-growth`; imprime alerta de sucesso/falha.
- Ação relevante: exporta `TELEGRAM_ALLOWED_USERS="171397651,1305071627"` para o profile LK Growth, conforme autorização Renan documentada no próprio script.
- Classificação: **manter `origin` por enquanto**.
- Motivo: stdout indica reinício de gateway e acesso de profile especializado; não silenciar sem uma decisão clara.
- Rollback se mudar delivery: `cronjob update 876d54c62ccd deliver=origin`.

### 5. SPITI Telegram gateway watchdog

- Job: `663e3e6a148c`.
- Script: `/opt/data/scripts/spiti_gateway_watchdog.py`.
- Schedule: every 1m.
- Delivery atual: `origin`.
- Contrato observado:
  - se gateway está rodando: exit 0, stdout vazio.
  - se profile/binário ausente: imprime falha e retorna 2.
  - se gateway estava ausente: inicia profile `/opt/data/profiles/spiti` e imprime que iniciou.
- Classificação: **manter `origin` por enquanto**.
- Motivo: SPITI tem regra de silêncio > dado errado; porém reinício de gateway é ação operacional relevante e deve ser visível até haver política aprovada de auto-heal silencioso.
- Rollback se mudar delivery: `cronjob update 663e3e6a148c deliver=origin`.

### 6. Hermes Brain Operating Layer structural watchdog

- Job: `d03fa04e1188`.
- Script: `brain_operating_layer_audit.py`.
- Schedule: `10 11 * * *`.
- Delivery atual: `origin`.
- Evidência prévia: na verificação manual, `python3 /opt/data/scripts/brain_operating_layer_audit.py` retornou exit 0 e stdout vazio.
- Classificação: **melhor candidato para `local`**.
- Motivo: é estrutural/documental, silent-OK, e o Runtime Truth Reconciler + relatórios locais já preservam evidência. Alertas ainda poderiam aparecer como stdout se `origin` fosse mantido; mas o sucesso normal não deve aparecer. Como o contrato no_agent já só envia stdout, a diferença prática depende do scheduler: se success stdout vazio é silencioso, `origin` é aceitável. Para reduzir superfície Telegram, `local` é mais coerente.
- Rollback se mudar delivery: `cronjob update d03fa04e1188 deliver=origin`.

### 7. LK WhatsApp Hermes responder regression watchdog

- Job: `a5d7a392eed9`.
- Script wrapper: `/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.sh`.
- Script real: `/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`.
- Schedule: `*/30 * * * *`.
- Delivery atual: `origin`.
- Contrato observado:
  - testes offline/parser-only por padrão;
  - stdout vazio em sucesso;
  - imprime falhas e retorna non-zero em regressão;
  - `--live-tiny` existe, mas não é usado pelo wrapper atual.
- Classificação: **bom candidato para `local`**, se Lucas aceitar que regressão só alerte via falha de cron/alerta local ou relatório consolidado.
- Motivo: é teste de regressão local, não entrega executiva. Se imprimir, já é falha técnica; pode ser roteado para relatório local/Brain e só subir no Fechamento/Mesa se persistir.
- Rollback se mudar delivery: `cronjob update a5d7a392eed9 deliver=origin`.

## Outros jobs `origin` não tratados como “ruído” nesta rodada

- `LK Daily Sales Brief read-only mandatory delivery` (`7c688553e293`) — relatório obrigatório para Lucas, não é simples watchdog técnico.
- `LK Weekly CEO Review read-only mandatory delivery` (`953b9055458e`) — relatório obrigatório.
- `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) — relatório obrigatório/read-only; manter visível por enquanto.
- `Mesa COO diária Telegram` (`749ee30b51eb`) — entrega executiva intencional.
- `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — entrega semanal intencional.
- `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`) — entrega executiva intencional.
- One-shots/lembretes `origin` — tratar separadamente como limpeza/arquivamento, não como alteração de delivery.

## Recomendações de alteração — NÃO executadas

Se Lucas aprovar uma próxima rodada de mudança de delivery, a ordem recomendada é:

1. **Alterar para `local`:** `d03fa04e1188` — Operating Layer structural watchdog.
2. **Alterar para `local`:** `a5d7a392eed9` — LK WhatsApp responder regression watchdog.
3. **Manter `origin`:** gateway watchdogs Mordomo/LK Growth/SPITI, até política explícita para reinício silencioso de gateways especialistas.
4. **Manter `origin`:** compression self-heal, pois stdout indica auto-heal/falha relevante.
5. **Avaliar depois:** runtime + cron watchdog, porque alerta de drift runtime pode ser crítico.

## Rollback padrão

Para qualquer alteração futura de delivery:

1. Antes: registrar `cronjob list` com job_id, delivery, last_run e last_status.
2. Alterar apenas um ou dois jobs por vez.
3. Reexecutar/aguardar próximo tick e confirmar silent-OK.
4. Rollback: `cronjob update <job_id> deliver=origin`.
5. Registrar receipt em `reports/governance/`.

## Verificação final desta rodada

Executada em 2026-05-22 após criar este brief.

- `python3 scripts/brain_health_check.py`: OK — `FAIL=0`, `WARN=0`, `All checks passed`.
- `python3 /opt/data/scripts/brain_operating_layer_audit.py`: OK — exit 0, stdout vazio, contrato silent-OK preservado.
- `git diff --check`: OK.
- Secret scan em arquivos modificados/untracked: OK — `files_scanned=302`, `hits=0`.
- `python3 /opt/data/scripts/brain_sync_safe.py --dry-run`: OK — branch `consolidation/brain-filesystem-git-hygiene-20260516`, `allowed_files=39`, `skipped_files=283`.
- Evidência do dry-run salva em `reports/brain-sync-safe-dry-run-2026-05-22-watchdog-review.txt`.

Observação: uma primeira tentativa de dry-run usou caminho local incorreto (`scripts/brain_sync_safe.py`) e falhou porque o script canônico fica em `/opt/data/scripts/brain_sync_safe.py`. A verificação foi reexecutada com o caminho correto e passou.

## Mudança aprovada e aplicada

Aprovação recebida de Lucas no Telegram: “Aprovado”.

Alterações aplicadas via `cronjob update`:

- `d03fa04e1188` — Hermes Brain Operating Layer structural watchdog: `deliver=origin` → `deliver=local`.
- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog: `deliver=origin` → `deliver=local`.

Escopo deliberadamente não alterado:

- Nenhum schedule foi alterado.
- Nenhum script foi alterado.
- Nenhum job foi pausado/removido.
- Nenhum gateway foi executado/reiniciado.
- Nenhum Docker/host/GMC/Shopify/WhatsApp externo foi tocado.

Verificação pós-mudança via `cronjob list` confirmou ambos com `deliver=local`, `enabled=true`, `state=scheduled`, `last_status=ok` e `last_delivery_error=null`.

Rollback exato, se necessário:

- `cronjob update d03fa04e1188 deliver=origin`
- `cronjob update a5d7a392eed9 deliver=origin`

## Limite desta rodada

Nenhum job foi executado manualmente quando poderia reiniciar gateway. Foram atualizados apenas os dois `deliver` aprovados para `local`. Nenhum write externo ou runtime mutation além do registro de cron aprovado foi feito.
