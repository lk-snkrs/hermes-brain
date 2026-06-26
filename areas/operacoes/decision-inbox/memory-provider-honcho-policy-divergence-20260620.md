# Approval packet — Memory provider Honcho vs política Memory OS

> **Documento histórico / DO NOT RUN:** comandos e caminhos citados são evidência/registro; não executar sem aprovação escopada, backup, rollback e readback.


Data: 2026-06-20
Status: decisão pendente de Lucas
Escopo: read-only / documental. Nenhum runtime, gateway, Docker, VPS, Traefik, cron, provider ou secret foi alterado.

## Decisão necessária

Resolver divergência entre:

1. Runtime Hermes atual usando `memory.provider: honcho` no profile default.
2. Política canônica do Brain/Memory OS ainda dizendo que provider externo/Mem0 deve ficar off e que Brain continua como fonte rica canônica.
3. Watchdog Memory OS tratando qualquer provider externo ativo como `action_required`.
4. Watchdog Honcho tratando Honcho como estado esperado e ficando silent-OK quando Honcho está saudável.

## Evidência read-only coletada

- `/opt/data/config.yaml`: `memory.provider: honcho`.
- `/opt/data/honcho.json`: Honcho ativo para workspace `lucas-hermes`, peer `lucas`, `recallMode=hybrid`, `saveMessages=true`, `pinUserPeer=true`, `aiPeer=hermes-default`.
- `/opt/hermes/.venv/bin/hermes memory status`: `Provider: honcho`, plugin instalado, status disponível, Honcho ativo.
- `/opt/data/scripts/honcho_memory_watchdog.py`: saída vazia e rc=0; portanto, sob a política Honcho atual, estado está OK/silent.
- `/opt/data/hermes_bruno_ingest/hermes-brain/memories/politica-memoria-hermes.md`: ainda afirma que Mem0/provider externo está rejeitado/off e `memory.provider` deve ficar vazio/off.
- `daytime-latest.json`: `external_memory_provider_active=true`, `status=action_required`, rota `memory_provider_guard`.
- `scorecard-latest.json`: score 75, failed checks: `watchdog_stdout_empty`, `memory_latest_ok`, `provider_external_off`.
- `context-recovery probe`: status attention por causa dessa divergência; não por saturação, secrets ou templates.

## Diagnóstico

Isto não parece uma falha operacional imediata do Honcho. É uma divergência de governança:

- O runtime foi promovido para Honcho governado.
- A política Memory OS e parte dos watchdogs continuam com a decisão anterior: provider externo rejeitado/off.
- Resultado: sistemas de auditoria geram alerta recorrente mesmo quando Honcho está saudável.

## Opção A — Aceitar Honcho como provider governado (recomendada)

Autorizar um pacote documental + watchdog local para reconhecer Honcho como provider aprovado, mantendo Brain como fonte rica canônica.

Mudanças propostas:

1. Atualizar `memories/politica-memoria-hermes.md` para diferenciar:
   - Mem0/provider externo genérico: continua rejeitado/off.
   - Honcho: aprovado como camada governada de recall/contexto, não substitui Brain.
2. Atualizar skill/reference `memory-no-external-provider-watchdog-20260601.md` ou criar nova referência supersedida para não bloquear Honcho aprovado.
3. Ajustar scripts Memory OS que hoje fazem `external_memory_provider_active=true` virar falha automática, para aceitarem allowlist explícita `honcho` quando:
   - config aponta para `honcho`;
   - `honcho.json` tem workspace/peer esperados;
   - watchdog Honcho está silent-OK;
   - nenhum secret é impresso.
4. Atualizar scorecard/daytime/context-recovery para classificar provider externo não aprovado como falha, mas `honcho_governed=true` como OK.
5. Rodar verificação local/read-only e secret scan.

Impacto esperado:

- Remove alerta falso/recorrente do Memory OS.
- Preserva Brain como fonte de verdade rica.
- Mantém Honcho sob health/quality watchdog próprio.
- Não exige mexer no runtime agora.

Risco:

- Se a política for mal escrita, agentes podem interpretar Honcho como substituto do Brain. Mitigação: texto explícito de camadas e watchdog exigindo Brain como canonical.

Rollback:

- Restaurar backups dos arquivos Brain/skills/scripts alterados.
- Reverter allowlist `honcho` nos watchdogs Memory OS.
- Honcho runtime permaneceria como está, salvo decisão separada de runtime.

## Opção B — Desativar/migrar Honcho depois

Manter a política atual e preparar plano posterior para voltar `memory.provider` para vazio/off ou migrar dados/contexto para Brain/built-in/session_search.

Mudanças propostas agora:

1. Não tocar runtime imediatamente.
2. Criar plano de rollback com backup de `config.yaml`, `honcho.json`, critérios de desativação e verificação pós-restart.
3. Enquanto não executar rollback, aceitar que Memory OS continuará alertando `external_memory_provider_active`.

Impacto esperado:

- Mantém coerência com a política antiga.
- Evita consolidar dependência de Honcho.

Risco:

- Mantém ruído operacional até desativar runtime.
- Perde benefício de recall/hybrid que já está ativo.
- Exigirá aprovação operacional posterior para runtime/restart.

## Recomendação

Escolher Opção A.

Motivo: o estado live já está em Honcho, o plugin está disponível, o `honcho.json` está governado por workspace/peer explícitos e o watchdog Honcho está silent-OK. A falha atual é de política/watchdog desatualizado, não de runtime. O caminho mais seguro é reconhecer Honcho como camada governada sem promover Honcho a fonte de verdade no lugar do Brain.

## Aprovação solicitada

Responder com uma das opções:

- `Aprovar A` — ajustar política/watchdogs para aceitar Honcho governado, sem mexer no runtime.
- `Aprovar B` — manter política antiga e preparar rollback/desativação de Honcho em pacote separado.
- `Ajustar` — pedir uma variação do pacote antes de aprovar.

## Non-actions

- Nenhum secret lido/impresso (`values_printed=false`).
- Nenhum Docker/VPS/Traefik/gateway/container/restart.
- Nenhum cron/provider/runtime mutation.
- Nenhum write externo.
- Nenhuma mudança de `config.yaml` ou `honcho.json`.
