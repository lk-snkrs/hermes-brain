# Roadmap — Hermes Brain pós-adaptação Bruno/OpenClaw

Este roadmap substitui o plano genérico de 30 dias por uma visão operacional do que já foi implementado e das próximas rodadas recomendadas.

## Princípio

Hermes não deve virar OpenClaw. O Brain usa a clareza organizacional ensinada pelo Bruno, mas preserva os diferenciais do Hermes:

- execução real com ferramentas;
- verificação antes de afirmação;
- memória persistente e `session_search`;
- Doppler para secrets;
- Telegram como interface;
- dados vivos em Supabase/Shopify/APIs;
- rotinas e crons verificáveis.

## Já implementado

### 1. Estrutura base

Status: concluído.

- `empresa/`
- `areas/`
- `agentes/`
- `seguranca/`
- índices executivos;
- manual operacional `START-HERE.md`.

### 2. Memórias preservadas

Status: concluído.

`memories/` continua como memória executiva compacta e global.

### 3. Agentes padronizados

Status: concluído.

- Hermes Geral.
- LK.
- Zipper.
- SPITI.

Cada agente tem estrutura operacional com identidade, ferramentas, usuário, memória e heartbeat conforme disponível.

### 4. LK operacionalizado

Status: fase base concluída.

- CRM.
- Tráfego pago.
- Ecommerce.
- Atendimento.
- Rotinas RFM, outcomes, consequence tracker, sync log, cross-sell e leads esfriando.

### 5. Zipper operacionalizado

Status: fase base concluída.

- Vendas de obras.
- Colecionadores.
- Feiras.
- Comunicação.
- Rotinas de consulta comercial, abordagem e planejamento.

### 6. SPITI operacionalizado

Status: fase base concluída.

- Verificação de lances.
- Alertas.
- Relatórios.
- Regras críticas de fonte: email > banco/site; meta tag não é lance.

### 7. Segurança e permissões

Status: concluído.

- Modelo de acesso por camada.
- Escopo por agente.
- Níveis de risco L0-L5.
- Regras de aprovação Lucas.
- Regras Doppler/secrets.

### 8. Remediação de secrets

Status: concluído no repo atual.

- Hardcoded secrets removidos dos scripts identificados.
- Whole-repo scan retornou `possible_secrets 0` na última rodada.

## Próximas rodadas recomendadas

### Rodada A — Verificação de crons reais na VPS

Status: inventário base concluído em `lc.vps`; n8n ainda merece rodada própria.

Resultado:

- Hostinger API confirmou VPS `lc.vps` (`72.60.150.124`) e `evo.lc` (`187.127.10.158`) rodando.
- Acesso a `lc.vps` resolvido com senha root fornecida pelo Lucas e chave dedicada instalada.
- Root crontab vazio; `/etc/cron.d` contém apenas Docker prune, sysstat e jobs de sistema.
- Systemd timers encontrados são padrão de sistema; nenhum timer de negócio/Hermes/LK/Zipper/SPITI.
- Docker ativo com Hermes Telegram, Hermes web, n8n, Paperclip e Traefik.
- Hermes cron confirmado: `Hermes release watch` semanal.
- Documento atualizado: `areas/operacoes/rotinas/cron-inventory.md`.

Objetivo final: transformar rotinas documentadas em estado operacional verificado.

Tarefas restantes:

1. Decidir se a chave SSH dedicada permanece ou será removida.
2. Rotacionar senha root enviada em chat, se desejado.
3. Investigar alerta de gateway parado no CLI vs container gateway rodando. — auditoria read-only documentada em `areas/operacoes/rotinas/hermes-runtime-observability.md`; próximo passo é decidir investigação/correção sem reiniciar containers automaticamente.
4. Fazer inventário específico de workflows n8n via API em rodada própria. — concluído em `areas/operacoes/rotinas/n8n-inventory.md`; workflow_count = 0 em `lc.vps`.
5. Atualizar `empresa/rotinas/_index.md` com coluna de status real se Lucas quiser visual executivo por rotina.
6. Decidir se update planejado do runtime Hermes Hostinger de v0.9.0 para v0.12.0 entra em janela de manutenção com backup/rollback.

### Rodada B — Integrações por ferramenta

Status: mapa base e aprofundamento operacional inicial concluídos.

Objetivo: criar mapa operacional por integração e transformar integrações críticas em rotinas seguras.

Entregas:

1. Doppler names por ferramenta mapeados sem valores.
2. Supabase LK, Zipper e SPITI documentados.
3. Shopify, Klaviyo, Evolution, Meta, GA4/GSC, n8n, GitHub, Hostinger e Telegram documentados.
4. Ações separadas em read-only, write, external-send e admin/destructive.
5. Integrações amarradas a áreas/agentes.
6. Rotinas criadas para validação de secrets, Shopify read-only, Supabase audit, Evolution approval, Klaviyo approval, Meta Ads reporting e Hostinger/VPS inventory.

Arquivos principais:

- `empresa/integracoes/MAPA.md`.
- Subdocs por ferramenta em `empresa/integracoes/`.
- Rotinas em `areas/operacoes/rotinas/`.
- `TOOLS.md` corrigido para evitar placeholders genéricos de Supabase.

Pendências futuras:

1. Criar subdocs para Judge.me, Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool quando virarem fluxo recorrente.
2. Transformar rotinas mais usadas em skills executáveis.
3. Rodar testes reais read-only por ferramenta quando houver pergunta operacional concreta.

### Rodada C — Aprofundamento LK

Objetivo: sair do mapa base para operação mais útil de CRM/performance.

Tarefas:

1. Expandir CRM LK com queries/padrões verificados.
2. Documentar segmentos principais.
3. Criar playbooks de cross-sell, reativação e RFM.
4. Conectar tráfego pago a criativos/learnings.
5. Criar templates de preview para aprovação Lucas.

Resultado esperado:

- Playbooks em `areas/lk/sub-areas/crm/playbooks/`.
- Templates em `areas/lk/sub-areas/crm/templates/`.
- Rotinas mais acionáveis.

### Rodada D — Aprofundamento Zipper

Objetivo: transformar sub-áreas Zipper em playbooks reais.

Tarefas:

1. Criar playbook de consulta `vendas_tango`.
2. Criar template de abordagem de colecionadores.
3. Criar checklist de feira por fase.
4. Criar guia de tom/comunicação por formato.
5. Definir regra de registro de resultados pós-contato.

Resultado esperado:

- `areas/zipper/sub-areas/vendas-obras/playbooks/`.
- `areas/zipper/sub-areas/colecionadores/templates/`.
- `areas/zipper/sub-areas/feiras/checklists/`.

### Rodada E — Aprofundamento SPITI

Objetivo: tornar impossível repetir erros de fonte de lance.

Tarefas:

1. Documentar árvore de decisão para resposta sobre lance.
2. Criar checklist de verificação antes de relatório.
3. Criar template de relatório interno.
4. Documentar falhas conhecidas do monitor/n8n.
5. Mapear quais ações são apenas internas e quais exigem aprovação.

Resultado esperado:

- `areas/spiti/playbooks/verificacao-lance.md`.
- `areas/spiti/templates/relatorio-leilao.md`.
- `areas/spiti/rotinas/monitor-health.md`.

### Rodada F — Health checks do Brain

Objetivo: validar automaticamente qualidade do Brain.

Tarefas:

1. Criar script de scan de secrets versionado em `scripts/`.
2. Criar check de links internos quebrados.
3. Criar check de arquivos obrigatórios por agente.
4. Criar check de rotinas sem índice.
5. Criar check de skills canônicas vs navegação por área.

Resultado esperado:

- `scripts/brain_health_check.py`.
- Rotina documentada em `areas/operacoes/rotinas/brain-health-check.md`.

## Critérios de qualidade para próximas fases

Toda fase deve terminar com:

1. Arquivos no lugar certo.
2. Dados não inventados.
3. Secrets não expostos.
4. Scan de secrets limpo.
5. Commit claro.
6. Push para `main` ou PR, conforme risco.
7. Resumo em português para Lucas.

## Sequência recomendada agora

1. Fechar decisão operacional sobre Hermes runtime/gateway: investigar conflito de polling e planejar update v0.9.0 → v0.12.0 somente com aprovação/rollback.
2. Rodada C — LK playbooks.
3. Rodada D — Zipper playbooks.
4. Rodada E — SPITI hardening.
5. Rodadas contínuas — Health checks, release watch Hermes, secret validation e inventário VPS/n8n conforme mudanças.

## Atualização contínua obrigatória

A cada rodada de evolução do Hermes Brain:

1. Verificar release atual do Hermes Agent.
2. Avaliar novidades aplicáveis a skills, memória, gateway, crons, ferramentas e segurança.
3. Atualizar skills internas quando o procedimento mudar.
4. Atualizar o Brain, índices e roadmap.
5. Rodar `scripts/brain_health_check.py` e scan de secrets.

## Sistema de memória

Documento canônico: `empresa/gestao/memory-system.md`.

Resumo:

- Memory tool: preferências duráveis do Lucas e regras globais compactas.
- `session_search`: recuperar histórico de conversas e progresso anterior.
- Hermes Brain GitHub: fonte de verdade para negócio, processos, decisões, rotinas, skills e agentes.
- `memories/`: memória executiva compacta por negócio.
- `empresa/` e `areas/`: detalhamento operacional estruturado.
- Dados vivos: Supabase, Shopify, APIs, email e crons.

Motivo: antes de aprofundar operação, vale criar health checks para proteger o Brain e evitar regressão de secrets, links quebrados e estrutura incompleta.
