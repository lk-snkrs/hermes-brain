# Approval Packet — Hermes Ops Bridge v1 read-only implementation

Data: 2026-06-29T09:55:51Z  
Status: **decidido — Opção B escolhida por Lucas em 2026-06-29T10:00:45Z**  
Origem: Onda 0/Onda 1 power-user audit + segundo uso real da Workcell v1.  
Classificação proposta: A2 local-code/read-only, sem runtime/externo.

## Decision / action requested

Aprovar ou bloquear a implementação de um **script local read-only** para o Hermes Ops Bridge v1.

A proposta é criar uma fachada simples sobre comandos já existentes para produzir resumo executivo local de status/health/smoke/logs/packets/receipts, começando **sem cron, sem dashboard/API e sem mutação**.

## Target / owner / system affected

- Owner lógico: Operações Hermes / Hermes Geral.
- Target documental já criado: `areas/operacoes/rotinas/hermes-ops-bridge-v1-readonly-spec-20260629.md`.
- Target técnico proposto, se aprovado: script local sob `/opt/data/scripts/`, nome sugerido `hermes_ops_bridge_readonly.py`.
- Output proposto: reports locais sob `reports/governance/` ou stdout executivo sanitizado.

## Escopo permitido

## Exact allowed scope if approved

Se Lucas aprovar a opção A:

1. Criar **um script local read-only** que rode apenas subcomandos seguros:
   - `status`: resumo local de Hermes/profile/crons a partir de arquivos/processos/CLI read-only;
   - `health`: Brain health e evidências locais existentes;
   - `cron-inventory`: leitura de registries locais;
   - `packet`: renderizar template local de approval packet, sem executar ação;
   - `receipt`: chamar receipt writer local para registrar execução documental;
   - `smoke`: somente se usar `hermes-cli-integrations smoke` via broker e reportar status/códigos sanitizados.
2. Criar testes locais básicos de não-mutação/saída sanitizada.
3. Criar um report de piloto local e receipt.
4. Atualizar a spec documental com o path do script se implementado.

## O que continua bloqueado

## Explicit exclusions / blocked actions

Mesmo com aprovação deste packet, continuam bloqueados:

- criar/alterar/remover cron;
- restart de gateway/profile;
- Docker/VPS/Traefik;
- dashboard/API/webhook;
- alteração/leitura/impressão de credenciais;
- login/reauth de integração;
- deploy;
- write externo;
- mutação Shopify/Tiny/Klaviyo/Supabase/Notion/Google/Telegram etc.;
- auto-dispatch de Kanban;
- skill deletion/cleanup real;
- mudar toolsets/profile config.

## Risk / blast radius

- Risco principal: criar mais uma camada de tooling que aumenta complexidade em vez de reduzir.
- Risco operacional: baixo se mantido read-only/local e sem cron/runtime.
- Blast radius: arquivos locais no Brain/scripts; sem efeitos externos.
- Mitigação: subcomandos mutáveis inexistentes ou hard-blocked, testes locais e output sanitizado.

## Rollback plan

Se a implementação atrapalhar:

1. Remover ou arquivar o script local criado.
2. Remover referências adicionadas à spec/MAPA, se houver.
3. Manter approval packet e receipt como histórico.
4. Nenhum rollback de runtime/cron/gateway/externo será necessário porque nada disso será tocado.

## Verification / readback plan

Antes de declarar concluído, rodar:

1. Teste local do script com `--help` e subcomando read-only piloto.
2. Varredura focada de credenciais em script, report e receipt.
3. Brain health check.
4. QA independente se o script tiver mais de um subcomando.
5. Receipt via Memory OS writer.
6. Resposta Telegram executiva com: resultado, evidência, não-ações e próximo gate.

## Approval options for Lucas

**A — Aprovar piloto local read-only agora**  
Implemento um script local mínimo, sem cron/dashboard/API/runtime, com 1–2 subcomandos e QA.

**B — Só manter documental por enquanto**  
Não implemento script; apenas uso os templates/rotinas existentes manualmente nas próximas tarefas.

**C — Ajustar escopo**  
Lucas define quais subcomandos entram ou saem antes de aprovar.

**D — Bloquear**  
Não avançar Ops Bridge; continuar apenas com Workcell/Task OS/Telegram UX.

## Credential hygiene

- `values_printed=false`.
- Não imprimir valores de credenciais, previews, tokens, service-account JSON, passwords ou connection strings.
- Se algum smoke usar broker, reportar apenas status/códigos/nomes de integração.

## Current recommendation

Recomendação: **B por padrão, A só se Lucas quiser transformar a especificação em ferramenta local agora**.

Motivo: a Workcell v1 já está útil; antes de criar tooling, vale garantir que o processo reduziu ruído em mais uma tarefa real. Este packet deixa o próximo passo pronto sem ultrapassar aprovação.
