# Approval Packet — propagar Task OS universal para profiles

- Data: 2026-06-25
- Status: aguardando aprovação Lucas
- generated_at_utc: `2026-06-25T16:45:56.048151+00:00`
- values_printed: `false`

## Objetivo

Fazer todos os agentes Hermes seguirem a lógica Task OS para tarefas operacionais não-triviais.

## Opção A — recomendada: patch documental sem restart

Escopo:

- Patchar/criar bloco curto em `AGENTS.md` dos profiles existentes sob `/opt/data/profiles/*` e `/opt/data/AGENTS.md`.
- Não tocar `.env`, `auth.json`, secrets, Docker, gateway, cron ou APIs externas.
- Backup por arquivo antes de patch.
- Verificar cada arquivo com grep/secret scan.
- Registrar receipt.

Efeito:

- Novas sessões/processos passam a ler a regra.
- Gateways vivos podem não observar imediatamente até restart natural/controlado.

## Opção B — patch documental + restart controlado de profiles ativos

Escopo A + restart um a um dos gateways ativos.

Risco maior: interrompe conversas/processos ativos. Exige janela e verificação por profile.

## Opção C — só manter policy Brain por enquanto

Sem patch profile-local.

Risco: especialistas continuam inconsistentes; depende de Hermes Geral lembrar/rotear.

## Bloqueados sem aprovação separada

- Docker/VPS/Traefik.
- `.env`/secrets/auth.
- cron mutation.
- API/webhook exposure.
- instalação de plugin/dashboard.
- external writes.

## Rollback

- Restaurar backups dos `AGENTS.md` alterados.
- Sem restart obrigatório na Opção A.
- Se B for aprovada, reiniciar novamente só profiles afetados após rollback.

## Recomendação Hermes

Aprovar **Opção A**.
