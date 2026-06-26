# Approval Packet — Ativar delegated tests v0.17 nos perfis Hermes

Data: 2026-06-22
Status: preparado; configs locais já foram ajustadas com backup, mas nenhum gateway/perfil foi reiniciado.

## Decisão solicitada

Aprovar ou não a ativação runtime das mudanças de delegação v0.17 nos perfis especialistas.

## O que já foi feito localmente

Backup criado em:

`/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`

Mudanças aplicadas em 16 configs de perfis:

- `delegation.max_async_children: 3`
- `platform_toolsets.cli += delegation` quando faltava
- `platform_toolsets.telegram += delegation` quando faltava

Config default já estava alinhado e não foi alterado.

## Por que isso importa

Sem isso, a v0.17 fica ativa no runtime principal, mas vários agentes especialistas não conseguem aplicar bem o padrão mais importante para Lucas:

> Feito = construído, rodado, testado por outro contexto e reconciliado.

## O que a aprovação permite

Se aprovado, executar uma onda controlada de ativação:

1. validar config de cada perfil;
2. reiniciar apenas perfis escolhidos, um bloco por vez;
3. verificar PID/HERMES_HOME correto;
4. verificar API/webhook continuam fechados onde esperado;
5. executar smoke local/read-only de `delegate_task` quando possível;
6. registrar receipt.

## O que a aprovação NÃO permite

- Não permite Docker/VPS/Traefik amplo.
- Não permite writes externos.
- Não permite ativar canais novos.
- Não permite instalar MCP novo.
- Não permite trocar modelo default.
- Não permite expor dashboard/API público.

## Opções

1. **Aprovar ativação em todos os perfis configurados**, com restart controlado por blocos.
2. **Aprovar só perfis prioritários**: `lk-growth`, `lk-shopify`, `lk-ops`, `mordomo`, `spiti`.
3. **Manter apenas configurado, sem restart por enquanto**.
4. **Rollback das mudanças de config** a partir do backup.

## Rollback

Restaurar cada `config.yaml` a partir de:

`/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`

Depois reiniciar somente os perfis afetados, se a mudança já tiver sido ativada em runtime.

`values_printed=false`
