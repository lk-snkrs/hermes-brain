# Approval Packet — Ativar `/kanban stats` executivo no Telegram

Data: 2026-06-06
Dono: Hermes / infra / operating layer
Origem: Lucas validou que o output atual do `/kanban stats` não adianta para decisão: “Não consigo entender nada”.

## Problema
O comando atual retorna métricas técnicas:

- `By status`
- `By assignee`
- idade em segundos (`Oldest ready task age: 2324662s`)

Isso prova que o comando funciona, mas falha como produto Telegram. O usuário precisa de interpretação executiva e próxima ação.

## Correção implementada no candidate
Arquivos alterados no candidate `/opt/data/hermes-v016-candidate-20260606/src`:

- `hermes_cli/kanban.py`
  - `kanban stats` sem `--json` agora retorna resumo executivo em português.
  - `--json` continua preservado para automação e debug técnico.
- `tests/hermes_cli/test_kanban_cli.py`
  - novo teste `test_run_slash_stats_plain_is_executive_for_telegram`.

## Novo formato esperado

```text
Kanban — resumo executivo
Aguardando ação: 6
Em andamento: 0
Bloqueados: 0
Agendados: 0
Concluídos: 9
Mais antigo aguardando: 26.9 dias
Próxima ação: escolher um card ready para executar ou arquivar se não for mais prioridade.
Detalhe técnico: use `/kanban stats --json` para números crus.
```

## Evidência de teste

- RED: o novo teste falhou no formato antigo.
- GREEN: teste específico passou.
- Regressão targeted:
  - `tests/hermes_cli/test_commands.py tests/hermes_cli/test_kanban_cli.py` → `192 passed`
  - `tests/hermes_cli/test_kanban_core_functionality.py` → `167 passed`
- Smoke do source alterado com board real read-only:
  - `run_slash('stats')` retornou formato executivo.

## Estado runtime atual
O gateway default ativo roda pelo venv instalado:

- PID: `1`
- `HERMES_HOME=/opt/data`
- comando: `/opt/data/hermes-0.15.1-venv/bin/python /opt/data/hermes-0.15.1-venv/bin/hermes gateway run`

O patch está no candidate source, não ativado no gateway vivo. Um simples teste no Telegram ainda mostrará o formato antigo até ativação.

## Escopo de aprovação A3 proposto
Ativar a correção no runtime default com restart controlado:

1. Fazer backup do arquivo instalado atual:
   - `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/hermes_cli/kanban.py`
2. Copiar a versão testada do candidate para o venv instalado ou aplicar patch equivalente.
3. Rodar smoke local no venv instalado:
   - `HERMES_HOME=/opt/data /opt/data/hermes-0.15.1-venv/bin/python -c "from hermes_cli import kanban; print(kanban.run_slash('stats'))"`
4. Reiniciar somente o gateway default.
5. Validar pós-restart:
   - PID novo com `HERMES_HOME=/opt/data`.
   - Telegram conectado.
   - `/status` responde.
   - `/kanban stats` neste chat retorna formato executivo.
6. Registrar receipt sanitizado no Brain.

## Fora de escopo / bloqueado
- Não alterar cards reais.
- Não executar dispatch/worker.
- Não mexer em Docker, Traefik, VPS, secrets, provider/model, cron, Dashboard ou perfis especialistas.
- Não alterar comandos write de Kanban.
- Não ativar sem aprovação explícita deste packet.

## Rollback
Se houver falha:

1. Restaurar backup de `kanban.py` no venv instalado.
2. Reiniciar somente o gateway default.
3. Validar `/status` e Telegram conectado.
4. Registrar rollback receipt.

## Decisão solicitada
Aprovar ativação A3:

- aplicar patch testado no venv instalado do gateway default;
- reiniciar somente o gateway default;
- validar `/kanban stats` em Telegram real;
- manter rollback pronto.
