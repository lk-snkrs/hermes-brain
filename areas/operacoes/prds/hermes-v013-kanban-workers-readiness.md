# PRD — Kanban workers readiness Hermes v0.13

Data: 2026-05-10
Escopo: preparar workers reais para o board `lk-growth-ops` sem disparar execução automática antes de controles mínimos.

## Diagnóstico atual

- Board: `lk-growth-ops`.
- Cards: 8 em `ready`.
- Assignees dos cards: `unassigned`.
- Perfis Hermes existentes: apenas `default`.
- Dispatcher: integrado ao gateway v0.13; portanto atribuir cards a perfis pode iniciar execução quando o gateway despachar.

Conclusão: o board está pronto como Mission Control, mas não deve receber assignees reais antes de criar perfis com limites claros.

## Objetivo

Transformar o Kanban em operação real, mantendo as mesmas barreiras de segurança usadas no chat:

- sem envio externo sem aprovação;
- sem write em Shopify/Tiny/Meta/Google/Supabase sem preview e autorização;
- sem Docker/restart/compose/dashboard público sem plano + rollback;
- sem imprimir secrets;
- sem misturar LK, Zipper e SPITI.

## Perfis propostos

### `lk-analyst-readonly`

Função: análise comercial LK.

Permissões conceituais:

- ler Brain, relatórios locais e fontes read-only;
- produzir ranking/diagnóstico/recomendação;
- atualizar docs locais/Brain se não contiver PII/secrets.

Proibido:

- enviar e-mail/WhatsApp;
- alterar Shopify/Tiny/Klaviyo/Meta/Google;
- exportar PII;
- inferir produto por campanha/adset genérico.

### `lk-content-reviewer`

Função: QA de textos, e-mails, layout e tom LK.

Permissões conceituais:

- revisar HTML/MIME/preview local;
- checar nome+SKU+tamanho;
- apontar problemas de marca/tom/clareza.

Proibido:

- enviar campanha;
- subir arte final para canal externo;
- usar thumbnails ruins/blank de criativo Meta como se fossem aprovadas.

### `hermes-ops-readonly`

Função: observabilidade Hermes.

Permissões conceituais:

- ler config, cron status, logs redigidos, processos e arquivos locais;
- rodar checks read-only;
- escrever relatório/diagnóstico.

Proibido:

- restart gateway/Docker;
- alterar compose, imagem, volumes, redes, Traefik;
- acessar secrets em claro;
- corrigir produção automaticamente.

### `brain-process`

Função: manter Brain/skills/rotinas atualizados.

Permissões conceituais:

- editar Markdown/PRD/rotinas/skills;
- registrar aprovações, correções e padrões;
- rodar secret scan local antes de finalizar.

Proibido:

- deploy/runtime;
- banco/campanhas/envios;
- commit/merge de código runtime sem PR e aprovação aplicável.

## Sequência segura de ativação

1. Criar perfis ou aliases sem associar cards ainda.
2. Limitar toolsets por perfil quando possível.
3. Criar um card piloto novo, interno e baixo risco, por exemplo: atualizar uma rotina do Brain a partir de um relatório já existente.
4. Atribuir apenas esse card piloto a `brain-process`.
5. Rodar um único dispatch/pass ou observar gateway dispatcher.
6. Verificar logs, `kanban runs`, `kanban log` e diff dos arquivos.
7. Só depois atribuir cards reais por área.

## Rollback

Se um worker agir errado:

- `hermes kanban --board lk-growth-ops reclaim <task_id>` para liberar claim;
- `hermes kanban --board lk-growth-ops assign <task_id> none` para desatribuir, ou `hermes kanban --board lk-growth-ops assign <task_id> <perfil>` para reatribuir;
- arquivar ou bloquear o card com motivo;
- remover/editar perfil problemático;
- pausar qualquer cron/dispatcher extra se tiver sido criado;
- não reiniciar Docker/gateway salvo com plano separado.

## Critérios de pronto para ativar workers reais

- Perfis existem e aparecem em `hermes profile list` ou `hermes kanban assignees`.
- Toolsets mínimos definidos ou documentados.
- Card piloto completo com evidência.
- Nenhum secret impresso em logs ou comentários.
- Nenhum write externo executado.
- Lucas recebeu resumo de riscos e rollback antes de ativação ampla.

## Decisão atual

Piloto local de documentação concluído com sucesso em `t_8ba27e8d`. Os demais cards continuam `unassigned` por segurança. Próximo passo baixo risco: ativar 1 card real por vez, começando por análise/Brain read-only, usando dispatch manual com wrapper seguro de PATH e verificando logs antes de qualquer daemon/cron.

## Registro do card piloto — 2026-05-10

Perfis mínimos criados em `/opt/data/profiles/` e validados por existência de `SOUL.md` + `config.yaml`:

- `lk-analyst-readonly`: análise comercial LK; SOUL proíbe envios externos, writes em Shopify/Tiny/Klaviyo/Meta/Google/Supabase, exportação de PII e mudanças de infra.
- `lk-content-reviewer`: QA de conteúdo/marca LK; SOUL proíbe campanha/envio/publicação externa, upload de asset final, writes em canais externos e mudanças de infra.
- `hermes-ops-readonly`: observabilidade operacional; SOUL proíbe restart de gateway/Docker/Hostinger, alterações em compose/imagem/volumes/redes/Traefik/SSH/firewall e acesso/impressão de secrets.
- `brain-process`: manutenção de Brain/PRDs/rotinas/skills; SOUL limita a Markdown/skills locais, exige diff/readback/secret scan e proíbe deploy/runtime/banco/campanhas/envios.

Toolsets restritos por `platform_toolsets` nos `config.yaml` dos perfis: CLI limitado a `file`, `terminal`, `code_execution`, `skills`, `todo` e, conforme função, `session_search` ou `vision`; Telegram limitado a `skills`. O piloto atual editou apenas este PRD local do Brain, não tocou Docker/gateway, Shopify, bancos, secrets, campanhas, mensagens ou APIs externas.

Achado operacional do piloto: em layout Docker/custom PATH, o dispatcher v0.13 usa `hermes` via `PATH` ao spawnar worker; quando `hermes` não está no `PATH`, o primeiro run falha com `spawn_failed`. Mitigação sem restart/Docker criada em `/opt/data/scripts/kanban_dispatch_lk_growth_ops_once.sh`, que exporta `/opt/hermes/.venv/bin` no PATH e roda apenas um pass (`dispatch`). Teste `--dry-run --max 1` executou sem spawn indevido e manteve os cards restantes sem assignee.

Rollback operacional continua: reclaim/bloquear/arquivar card problemático, remover assignee ou perfil, e manter qualquer restart/infra fora de escopo até plano separado com backup, healthcheck e rollback.

## Registro do primeiro card real `brain-process` — 2026-05-10

Card `t_58ddd8d0` usado para validar o learning loop de aprovações/correções do Lucas sem tocar produção. O worker atualizou apenas Brain/Markdown local, registrando: Docker-awareness, `approvals.mode: off` com guardrails, perfis Kanban/piloto e achado do wrapper de PATH. Rotina criada em `areas/operacoes/rotinas/hermes-approval-learning-loop.md`.
