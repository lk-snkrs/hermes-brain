# Auditoria sistêmica — Hermes v0.17 adoption across agentes, crons e scripts

Data: 2026-06-22
Responsável: Hermes Geral/default
Escopo: read-only audit + safe local/documental/config preparation. Nenhum restart/runtime activation/external write.

## Pedido de Lucas

Lucas pediu uma auditoria completa do que saiu no Hermes 0.17 e se alguma melhoria ficou sem implementação no agente principal, todos os agentes, crons, scripts e sistema.

## Método

Foram usados 3 subagentes paralelos:

1. Matriz de novidades v0.17 x superfícies de adoção.
2. Auditoria de perfis/agentes/configs.
3. Auditoria de crons/scripts/Brain/skills.

Depois disso, Hermes Geral aplicou as melhorias locais seguras:

- criou sentinel read-only v0.17;
- preparou configs de perfis para delegated tests/background delegation;
- criou rotina Brain;
- criou approval packets para ativação de perfis e hardening de crons Telegram.

## Veredito executivo

**Não estava 100% adotado.** A base v0.17 estava ativa, mas havia gaps de propagação para perfis, crons e scripts.

O gap mais importante era o que Lucas apontou: **delegated tests / delegate_task**. Isso agora foi elevado para regra operacional e parcialmente implementado em config + sentinel.

## Matriz resumida das novidades v0.17

| Bloco v0.17 | Status antes | Status após esta auditoria | Próximo passo |
|---|---|---|---|
| Runtime v0.17 default | Ativo | Mantido | Nenhum |
| Telegram rich/long messages | Herdado pelo runtime | Contrato auditado; crons ainda têm gaps documentais | Approval para hardening dos 13 crons `origin` |
| `delegate_task(background=true)` | Disponível/documentado | Smoke PASS + configs de perfis preparados | Restart controlado para ativar nos perfis |
| Delegated tests / Delegated Done | Gap crítico | Regra criada, skill/reference e sentinel criados | Aplicar como gate em tarefas futuras |
| Memory batch operations | Documentado | Sentinel inclui verificação documental indireta | Evoluir Memory OS prompts se necessário |
| Curator custo-zero/consolidate off | Validado manualmente | Sentinel/routine passa a monitorar adoção | Sem ação sensível |
| MCP catalog/governance | Inventariado | Gaps documentais mapeados; sem instalação | Approval se for instalar Linear/n8n/MCPs sensíveis |
| Dashboard/profile builder | Não exposto | Packet Onda 5 existe | Approval para local-only ou público |
| Desktop/watch-windows | Não adotado | Mantido como backlog sensível/cliente | Approval separado se Lucas quiser |
| xAI/Grok Composer | Secret presente | Não trocou default | Smoke isolado antes de qualquer uso como default |
| WhatsApp Cloud/Photon/Raft/SimpleX | Não adotado | Packets existem; sem ativação | Approval Onda 3 |
| Automation Blueprints/Chronos/fleet | Não adotado | Classificado como approval-gated | Approval Onda 5 |
| Itens revertidos | Não adotados | Mantidos como “não shipping” | Nenhum |

## Achados por superfície

### 1. Agente principal/default

- Runtime default já estava mais alinhado:
  - `_config_version: 30`;
  - `delegation.max_async_children: 3` já presente;
  - `delegation.max_concurrent_children: 3`;
  - `orchestrator_enabled: true`;
  - memory provider Honcho;
  - curator enabled;
  - MCPs configurados.

Status: **bom**.

### 2. Perfis/agentes especialistas

Foram encontrados 16 perfis ativos sob `/opt/data/profiles/*/config.yaml`.

Gap inicial:

- todos os 16 perfis estavam sem `delegation.max_async_children`;
- vários perfis tinham `orchestrator_enabled: true` mas não expunham `delegation` em `platform_toolsets.cli` e/ou `platform_toolsets.telegram`;
- muitos ainda têm `_config_version: 23/24/27`, enquanto o default está em 30.

Implementação segura aplicada agora:

- backup de configs:
  - `/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`
- 16 configs de perfis ajustadas com:
  - `delegation.max_async_children: 3`;
  - `platform_toolsets.cli += delegation` quando faltava;
  - `platform_toolsets.telegram += delegation` quando faltava.

Verificação pós-patch:

- `profile_gap_count: 0` no sentinel.
- Nenhum gateway/perfil foi reiniciado; portanto está **configured/prepared**, não necessariamente active em runtime.

### 3. Crons

Escopo auditado:

- registros de cron encontrados: 11;
- jobs totais: 103;
- jobs habilitados: 83.

Gap:

- 13 jobs `deliver=origin` não têm contrato explícito Telegram/noise/rich/actionability no registro/prompt.

Importante: isso não prova spam nem falha. Prova que a governança v0.17 ainda não está explícita no registro/prompt desses jobs.

Ação feita:

- criado approval packet para patch de metadata/prompt desses 13 jobs, preservando schedule/delivery/enabled/state/script.

Arquivo:

- `areas/operacoes/approval-packets/hermes-v017-cron-telegram-contract-hardening-20260622.md`

### 4. Scripts

Gap:

- scripts quase não continham termos/padrões v0.17 como `Delegated Done`, `Tester Receipt`, `delegate_task`, `background=true`, `MCP catalog`, `curator status`, `memory batch`.

Implementação feita:

- criado sentinel read-only:
  - `/opt/data/scripts/hermes_v017_adoption_sentinel.py`

Comportamento:

- `--json` imprime resumo sanitizado;
- `--quiet` fica silencioso se OK;
- não altera runtime/config/cron;
- não imprime secrets;
- `values_printed=false`.

### 5. Brain/skills

Já existiam bons artefatos:

- PRD adoção completa v0.17;
- relatório Onda 1;
- approval packets Onda 3/Onda 5;
- relatório/receipt de delegated tests;
- skill references em `lucas-runtime-operations`.

Implementação adicional:

- rotina criada:
  - `areas/operacoes/rotinas/hermes-v017-adoption-sentinel.md`
- indexada em:
  - `areas/operacoes/MAPA.md`
  - `empresa/rotinas/_index.md`

## Sentinel pós-implementação

Comando:

```bash
python3 /opt/data/scripts/hermes_v017_adoption_sentinel.py --json
```

Resumo:

- `sentinel_status: attention`
- `profile_gap_count: 0`
- `origin_without_explicit_contract_count: 13`
- `scripts_delegated_done_count: 1`
- `values_printed=false`

Interpretação:

- gaps de perfis corrigidos no disco;
- ainda há atenção por crons `origin` sem contrato explícito;
- script sentinel criado e passou py_compile.

## Arquivos criados/modificados

### Criados

- `/opt/data/scripts/hermes_v017_adoption_sentinel.py`
- `areas/operacoes/rotinas/hermes-v017-adoption-sentinel.md`
- `areas/operacoes/approval-packets/hermes-v017-profile-delegation-activation-20260622.md`
- `areas/operacoes/approval-packets/hermes-v017-cron-telegram-contract-hardening-20260622.md`

### Modificados

- 16 configs em `/opt/data/profiles/*/config.yaml`
- `areas/operacoes/MAPA.md`
- `empresa/rotinas/_index.md`

### Backups

- `/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`

## Não-ações

- Não reiniciei gateways/perfis.
- Não migrei config versions dos perfis via CLI.
- Não alterei crons vivos.
- Não alterei schedule/delivery/enabled/state de jobs.
- Não expus dashboard/API.
- Não ativei WhatsApp Cloud, Photon/iMessage, Raft ou SimpleX.
- Não instalei MCP novo.
- Não troquei modelo default.
- Não fiz Docker/VPS/Traefik/SSH.
- Não fiz writes externos/prod.

## Próximas decisões necessárias

### A. Ativar delegated tests nos perfis

Packet:

`areas/operacoes/approval-packets/hermes-v017-profile-delegation-activation-20260622.md`

Opções:

1. restart controlado de todos os perfis configurados;
2. restart só dos prioritários (`lk-growth`, `lk-shopify`, `lk-ops`, `mordomo`, `spiti`);
3. manter só configurado por enquanto;
4. rollback de configs.

### B. Hardening dos crons Telegram

Packet:

`areas/operacoes/approval-packets/hermes-v017-cron-telegram-contract-hardening-20260622.md`

Opções:

1. patch metadata/prompt dos 13 crons `origin`;
2. listar os 13 jobs para revisão humana;
3. manter só sentinel/report por enquanto.

## Conclusão

O principal esquecimento real era: **a v0.17 precisa virar protocolo de qualidade nos agentes, não só atualização de runtime**.

Isso foi corrigido no disco de forma segura:

- delegated tests configurado para todos os perfis;
- sentinel criado;
- rotina/índice criados;
- packets preparados para as partes que exigem ativação/runtime ou cron mutation.

Ainda falta aprovação para tornar algumas mudanças **active** em runtime, porque config em disco não reinicia perfis por si só.

`values_printed=false`
