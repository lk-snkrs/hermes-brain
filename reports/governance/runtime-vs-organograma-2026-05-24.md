# Runtime vs Organograma — Inventário read-only

Data: 2026-05-24  
Status: Fase 3 concluída em modo somente leitura  
Escopo: comparar runtime real do Hermes com organograma/matriz documental, sem alterar processos, crons, Docker, gateway ou produção.

## Resumo executivo

O organograma documental principal está coerente com o runtime ativo:

- Hermes Geral está ativo no profile principal `/opt/data`.
- LK Growth está ativo em `/opt/data/profiles/lk-growth`.
- Mordomo está ativo em `/opt/data/profiles/mordomo`.
- SPITI está ativo em `/opt/data/profiles/spiti`.
- Zipper não tem profile dedicado ativo, coerente com a matriz atual: Zipper permanece documental/read-only até profile próprio existir.

Gaps encontrados, sem correção aplicada nesta fase:

1. Existem profiles extras/dormentes com `.env` e token Telegram configurado, mas sem gateway/cron ativo detectado:
   - `brain-process`
   - `hermes-ops-readonly`
   - `lk-analyst-readonly`
   - `lk-content-reviewer`
2. O scheduler principal ainda concentra vários jobs de LK/Zipper/Mordomo/LK Growth watchdog, embora o organograma esteja caminhando para separação por domínio/profile.
3. O job `Mesa COO diária Telegram` continua `deliver: origin`; isso é esperado como UX de decisão, mas depende do conserto de entrega limpa de Telegram para não vazar wrapper/JSON/job_id.

## Evidência read-only coletada

### Profiles existentes em `/opt/data/profiles`

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`
- `lk-growth`
- `mordomo`
- `spiti`

### Gateways ativos detectados por processo + `HERMES_HOME`

- Main Hermes: `/opt/data`
- LK Growth: `/opt/data/profiles/lk-growth`
- Mordomo: `/opt/data/profiles/mordomo`
- SPITI: `/opt/data/profiles/spiti`

### API/Webhook em processos ativos

- Main `/opt/data`:
  - API Server: enabled
  - Webhook: enabled
  - Telegram: token/home/allowed users presentes
- LK Growth:
  - API Server: disabled no ambiente vivo
  - Webhook: disabled no ambiente vivo
  - Telegram: token/home/allowed users presentes
- Mordomo:
  - API Server: disabled no ambiente vivo
  - Webhook: disabled no ambiente vivo
  - Telegram: token/home/allowed users presentes
- SPITI:
  - API Server: disabled no ambiente vivo
  - Webhook: disabled no ambiente vivo
  - Telegram: token/home/allowed users presentes

Observação: alguns arquivos `.env` de profiles secundários contêm chaves `API_SERVER_*`, mas o processo vivo dos profiles ativos está com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false`. Não houve alteração.

## Cron inventory por profile

### Main `/opt/data`

- Total: 23 jobs
- Ativos: 23
- Pausados: 0
- Entregas relevantes:
  - Muitos jobs `deliver: local`, coerente com silent-OK.
  - Jobs `deliver: origin` ainda existentes para relatórios/decisões Lucas.

Jobs destacados:

- `Mesa COO diária Telegram` — `deliver: origin`
- `Hermes runtime + cron watchdog no_agent` — `deliver: local`
- `Hermes compression failure self-heal watchdog` — `deliver: local`
- `Hermes Brain Fechamento Ágil 23h + Brain Sync` — `deliver: local`
- `LK Growth Telegram gateway watchdog` — `deliver: local`
- `Mordomo Telegram gateway watchdog` — `deliver: local`
- `SPITI Telegram gateway watchdog` — `deliver: local`
- `Zipper OS vendas 09h WhatsApp/email` — `deliver: local`
- LK daily/weekly/GMC report jobs — alguns `deliver: origin`

### LK Growth `/opt/data/profiles/lk-growth`

- Total: 26 jobs
- Ativos: 22
- Pausados: 4
- Padrão dominante: D+7 reviews, SEO/GEO/CRO/GMC e Growth reviews.
- Coerente com a matriz: conteúdo/Growth/SEO/GEO/CRO deve morar aqui.

Observação: vários jobs de impacto usam `deliver: origin`. Isso pode ser desejado para follow-up de impacto, mas se o objetivo for reduzir ruído no Telegram principal, precisa de uma fase separada de classificação de entrega, não foi alterado agora.

### Mordomo `/opt/data/profiles/mordomo`

- Total: 12 jobs
- Ativos: 11
- Pausados: 1
- Padrão dominante: WhatsApp watcher, Calendar watcher, CRM local sync, Decision Inbox, Zipper email/drafts e enquiry watcher.
- Coerente com a matriz: Mordomo cuida de intake pessoal/agenda/follow-up, com bloqueios para preço/disponibilidade/reserva/negociação/reclamação/supplier/bulk.

### SPITI `/opt/data/profiles/spiti`

- Cron registry: não encontrado.
- Gateway ativo: sim.
- Coerente parcialmente: SPITI profile existe e está online, mas não há crons próprios registrados no profile.

## Comparação com organograma/matriz

### Coerente

- Hermes Geral como entrada/orquestrador central: sim.
- LK Growth como profile ativo: sim.
- Mordomo como profile ativo: sim.
- SPITI como profile ativo: sim.
- Zipper sem profile dedicado: sim, continua documental/read-only.
- API/Webhook apenas no main vivo: sim, profiles ativos estão sem API/Webhook no ambiente de processo.

### Parcial / atenção

- Profiles dormentes não aparecem claramente no organograma canônico. Eles podem ser experimentos, perfis futuros ou sobras; precisam ser classificados antes de qualquer limpeza.
- Main scheduler ainda contém jobs de domínios especialistas. Isso pode ser legado/coordenação central, mas a direção do organograma sugere migrar ou documentar ownership por profile no futuro.
- A UX do `Mesa COO diária Telegram` depende do delivery path limpo com botões reais. A documentação já exige isso; runtime precisa de validação técnica separada.

### Divergência sem ação automática

Nenhuma divergência crítica exigiu correção imediata. Não apliquei pausa, migração, remoção ou alteração de cron/profile.

## Recomendações para próxima fase

### Fase 4A — Classificação de profiles dormentes

Criar um inventário documental para cada profile extra:

- dono pretendido;
- bot/token configurado ou legado;
- se deve ficar, virar especialista, ou ser arquivado;
- riscos de manter `.env` com Telegram token;
- critérios para ativar ou remover.

Profiles a classificar:

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`

Somente documentação/read-only por enquanto.

### Fase 4B — Matriz de ownership de crons

Criar relatório `cron-ownership-vs-task-router-2026-05-24.md` classificando cada job como:

- central/COO;
- LK Growth;
- Mordomo;
- SPITI;
- Zipper;
- Brain governance;
- legado/revisar.

Sem mudar `deliver`, `enabled`, schedule ou profile ainda.

### Fase 4C — Correção UX Mesa COO Telegram

O problema original do texto estranho do cron ainda precisa de validação no runtime:

- sem `Cronjob Response` visível;
- sem `job_id` visível;
- sem JSON/HTML marker visível;
- com botões nativos reais;
- uma decisão 1/N por mensagem.

Essa fase provavelmente envolve código/gateway/scheduler e exigirá plano técnico + teste + aprovação antes de restart/alteração de runtime.

## Guardrails desta fase

- Nenhum arquivo `.env` lido em valor; apenas presença de chaves foi inventariada.
- Nenhum secret impresso no relatório.
- Nenhum cron criado, pausado, removido ou editado.
- Nenhum gateway/processo reiniciado.
- Nenhum Docker/VPS/Traefik/volume/network alterado.
- Nenhum write externo executado.
