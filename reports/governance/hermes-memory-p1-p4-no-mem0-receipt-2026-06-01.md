# Receipt — Memória Hermes P1–P4 sem Mem0

Data: 2026-06-01  
Escopo aprovado por Lucas: executar P1, P2, P3 e P4; **não usar Mem0**.

## P1 — USER.md default compactado

- Arquivo: `/opt/data/memories/USER.md`
- Backup pré-aplicação: `/opt/data/backups/memory_hygiene_20260601/USER.default.before-p1-final-20260601T143450Z.md`
- Resultado: perfil do usuário mantido como boot mínimo com 1084/1375 chars (78.8%).
- Observação: a sessão atual pode continuar mostrando snapshot antigo até nova sessão/restart do profile.

## P2 — monitor diário/silent-OK de higiene de memória

- Script criado: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`
- Contrato: `stdout` vazio = OK/silencioso; imprime alerta só se memória estiver saturada, provider externo ativo, palavra Mem0 reaparecer como backlog ativo, ou houver padrão de segredo.
- Cron ajustado após correções de Lucas: `f9a1d43caf48` — `Hermes memory hygiene watchdog 02h15 BRT`, `15 5 * * *` (= 02:15 BRT), `deliver=local`, `no_agent=true`. Motivo: memória/Brain é vivo; mensal deixa drift ficar errado tempo demais, e a higiene deve acontecer na madrugada junto do ciclo 02h para começar o dia com memória mais limpa, leve e registrada.

## P3 — Bruno como benchmark / Brain como fonte canônica

- Decisão consolidada: Bruno/OpenClaw é referência metodológica; Brain é a fonte rica canônica do Hermes; agente/profile não é o Brain.
- Política canônica atualizada em `memories/politica-memoria-hermes.md`.

## P4 — Mem0 rejeitado

- Decisão criada: `areas/operacoes/decisions/memoria-sem-mem0-2026-06-01.md`
- PRDs/artefatos de canário ficam históricos/rejeitados, não backlog ativo.
- Nenhum provider externo foi ativado.

## Não feito

- Sem gateway/restart/profile restart.
- Sem Docker/VPS/Traefik/compose/volumes.
- Sem escrita externa, API externa ou Mem0.
- Sem secrets impressos.

## Ajuste adicional disparado pelo P2

O dry-run do watchdog detectou `lk-ops/USER.md` acima de 85%; foi compactado com backup em `/opt/data/backups/memory_hygiene_20260601/` e ficou em 978/1375 chars.

## Verificação final

- `python3 scripts/brain_health_check.py` — passou (`All checks passed.`).
- `python3 -m py_compile /opt/data/scripts/hermes_memory_hygiene_watchdog.py` — passou.
- `/opt/data/scripts/hermes_memory_hygiene_watchdog.py` — passou com stdout vazio (silent-OK).
- Secret scan focado nos arquivos alterados — `secret_findings: []`.
- Config de memória: provider permanece vazio/off.
- Tamanhos verificados: default `MEMORY.md` 1092/2200; default `USER.md` 1084/1375; `lk-ops/USER.md` 978/1375 após alerta do watchdog.
