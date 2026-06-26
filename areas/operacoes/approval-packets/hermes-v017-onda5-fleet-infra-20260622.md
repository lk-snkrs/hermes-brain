# Approval Packet — Hermes v0.17 Onda 5: fleet/infra avançada

Data: 2026-06-22
Status: preparado; nenhuma mudança infra/runtime executada.

## Escopo da Onda 5

Avaliar recursos avançados v0.17 de operação/frota:

1. Managed scope `/etc/hermes`.
2. Gateway multiplex / gateway-gateway relay.
3. Chronos/cron operacional avançado.
4. Dashboard/API como control plane técnico.
5. Multi-profile/fleet observability hardening.

## Estado atual relevante

- Runtime default já está em Hermes v0.17.
- Gateway Telegram default saudável conforme validação anterior.
- Dashboard real process count na Onda 1: `0`.
- MCP catalog mostra `linear` e `n8n` disponíveis, mas ainda não instalados pelo processo de adoção.
- Não houve Docker/VPS/Traefik/restart nesta Onda.
- `values_printed=false`.

## Valor esperado

- Melhor observabilidade/administração dos perfis Hermes.
- Menos drift entre default e especialistas.
- Base para dashboard/cockpit técnico sem misturar com Mission Control executivo.
- Rotinas mais auditáveis para cron/MCP/profile changes.

## Riscos

- Mudança de escopo global pode afetar todos os perfis.
- Dashboard/API expostos podem abrir acesso a ferramentas, sessões, config e possivelmente terminal/file operations.
- Gateway multiplex/relay pode alterar roteamento/identidade dos bots.
- Cron/fleet migration pode gerar spam Telegram ou executar jobs fora do dono correto.

## Guardrails obrigatórios

- Primeiro PoC isolado ou local-only.
- Sem `--insecure` / sem bind público sem aprovação explícita.
- Sem Traefik/Docker/VPS sem backup/rollback e janela clara.
- Sem migrar cron/profile owner por heurística.
- Validar live PIDs por `HERMES_HOME` e logs antes/depois.
- Secret scan dos artefatos.
- Silent-OK para watchdogs; Telegram só para decisões/falhas acionáveis.

## Proposta de execução segura

### Fase 5.1 — Auditoria read-only

- Mapear processos Hermes reais por `HERMES_HOME`.
- Mapear superfícies API/webhook/dashboard/listeners.
- Mapear cron registries por perfil.
- Mapear MCPs instalados/configurados.
- Gerar scorecard sem alterações.

### Fase 5.2 — PoC local-only

- Subir dashboard apenas em loopback/isolated ou verificar status sem exposição.
- Validar health/local access.
- Sem Docker/Traefik.

### Fase 5.3 — Approval infra

Só depois da Fase 5.1/5.2, apresentar plano com:

- mudança exata;
- arquivos/processos afetados;
- backup;
- rollback;
- smoke tests;
- janela de restart;
- critérios de abort.

## Aprovação necessária

Escolher uma destas opções:

1. **Aprovar Onda 5.1 auditoria read-only fleet/infra** — sem mudanças runtime.
2. **Aprovar Onda 5.2 PoC dashboard local-only** — sem exposição pública.
3. **Bloquear Onda 5 por enquanto**.

Qualquer etapa além disso exige approval adicional.

## Rollback geral

- Parar dashboard/processos novos.
- Reverter config/launcher se alterados.
- Restaurar backups.
- Validar gateway default e especialistas.
- Confirmar Telegram/webhook/API health.

`values_printed=false`
