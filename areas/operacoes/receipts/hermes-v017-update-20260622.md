# Receipt — Hermes v0.17.0 update staging — 2026-06-22

- Data UTC: 2026-06-22
- Pedido: atualizar Hermes para a última versão.
- Escopo aprovado/interpretado: atualização local do pacote Hermes e migração de config; sem restart Docker/VPS/Traefik sem confirmação separada.
- Fonte oficial consultada: GitHub latest release `Hermes Agent v0.17.0 (v2026.6.19)`, tag `v2026.6.19`, release date 2026-06-19.
- Estado antes: pacote ativo em disco `hermes-agent==0.16.0`; config version `27`; gateway principal rodando em Docker foreground, PID 1, `HERMES_HOME=/opt/data`.
- Backup local criado: `/opt/data/backups/hermes-update-20260622T012915Z`.
- Ação executada: `uv pip install --upgrade 'hermes-agent[all]' --python /opt/data/hermes-0.15.1-venv/bin/python`.
- Estado em disco depois: `Hermes Agent v0.17.0 (2026.6.19)`, upstream `ba6ffd4f`, package `hermes-agent==0.17.0`.
- Config migrada: `27 → 30`; novo default registrado: `curator.consolidate: false`.
- Verificações OK:
  - `hermes --version`: v0.17.0, up to date.
  - `hermes config check`: config version `30 ✓`.
  - `hermes cron status`: gateway running; 39 active jobs.
  - `hermes memory status`: Honcho provider available.
  - `hermes doctor`: sem erro de config version; mantém avisos pré-existentes/ambientais de chaves opcionais e entrypoint de layout customizado.
- Verificação com ressalva:
  - CLI one-shot respondeu corretamente (`HERMES_V017_SMOKE_OK_*`), mas o processo encerrou com `Fatal Python error: Aborted`, exit `134`, após imprimir resposta e session_id.
  - Busca web encontrou issue pública similar: one-shot CLI imprime resposta e aborta no shutdown, relacionada a cleanup de background/native resources.
  - Classificação: não bloquearia necessariamente gateway long-lived, mas bloqueia declarar ativação 100% limpa sem restart controlado e validação pós-restart.
- Runtime ativo agora: processo PID 1 ainda é anterior ao update em disco; restart controlado é necessário para carregar código v0.17.0 no gateway Telegram principal.
- Writes externos: nenhum.
- Secrets: não registrar valores; relatório sanitizado; `values_printed=false` para este receipt.
- Rollback:
  1. Restaurar `/opt/data/config.yaml` de `/opt/data/backups/hermes-update-20260622T012915Z/config.yaml.before-migrate` ou `config.yaml`.
  2. Reinstalar pacote anterior no venv ativo se necessário: `uv pip install 'hermes-agent==0.16.0' --python /opt/data/hermes-0.15.1-venv/bin/python`.
  3. Reiniciar gateway principal apenas com aprovação escopada e validar Telegram/API/cron.
- Próxima decisão necessária: aprovar ou adiar restart controlado do gateway principal para ativar v0.17.0 em runtime.
