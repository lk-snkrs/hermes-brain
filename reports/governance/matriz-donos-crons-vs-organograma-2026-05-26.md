# Matriz de Donos de Crons vs Organograma — Hermes Brain

Data: 2026-05-26  
Escopo: auditoria local/read-only dos registries de cron e comparação com o organograma de agentes.  
Sem alterações em cron, gateway, Docker, VPS, produção ou writes externos.

## Veredito

O organograma continua correto: Hermes Geral coordena, especialistas executam, Brain registra e produção/externo exige aprovação.

O principal gap não é criar mais agentes. O gap operacional é reconciliar rotinas recorrentes com seus donos lógicos e garantir handoff/receipt quando um cron gera decisão, entrega externa, risco ou output relevante.

## Evidência lida

Registries locais inspecionados:

- Main Hermes: `/opt/data/cron/jobs.json`
  - Total: 20
  - Ativos: 20
  - Inativos/pausados: 0
- LK Growth: `/opt/data/profiles/lk-growth/cron/jobs.json`
  - Total: 21
  - Ativos: 21
  - Inativos/pausados: 0
- Mordomo: `/opt/data/profiles/mordomo/cron/jobs.json`
  - Total parseável: 13
  - Ativos: 13
  - Observação: arquivo possui bytes inválidos/trailing data após o primeiro JSON parseável; requer saneamento controlado antes de qualquer edição.
- SPITI: `/opt/data/profiles/spiti/cron/jobs.json`
  - Registry não encontrado.
  - Interpretação: finding documental, não erro. Pode significar que SPITI tem runtime mas ainda não possui scheduler local próprio.

## Donos lógicos por profile

### Main Hermes / Hermes Geral

Deve conter:

- governança Brain;
- Mesa COO;
- watchdogs centrais;
- fechamento/sync;
- rotinas de observabilidade;
- supervisão de gateways especialistas quando o watchdog central é proposital.

Achados:

- Main contém corretamente a maior parte de governança Hermes/Brain.
- Main também contém watchdogs de Mordomo, LK Growth e SPITI. Isso é aceitável se entendido como supervisão central, não execução de negócio pelo Hermes Geral.
- Main contém rotinas LK operacionais/relatórios comerciais e Zipper documental. Isso pode estar correto enquanto não houver LK Ops/Zipper runtime próprio, mas precisa de dono lógico explícito.

Crons Main que merecem rotulagem de dono no relatório/dash:

- `LK Daily Sales Brief read-only mandatory delivery` — dono lógico: LK Ops/Comercial; runtime atual: Main.
- `LK Weekly CEO Review read-only mandatory delivery` — dono lógico: LK Ops/CEO review; runtime atual: Main.
- `LK Pulso Comercial 16h read-only delivery` — dono lógico: LK Comercial/Financeiro; runtime atual: Main.
- `LK 09h previous-day sales report external delivery` — dono lógico: LK Ops/Comercial; runtime atual: Main.
- `LK 19h30 physical store close external delivery` — dono lógico: LK Loja/Ops; runtime atual: Main.
- `Zipper OS vendas 09h WhatsApp/email` — dono lógico: Zipper documental/read-only; runtime atual: Main.

### LK Growth profile

Deve conter:

- SEO/GEO/CRO/GMC/analytics;
- conteúdo/blog/source pages;
- impact reviews D+7 de Growth;
- approval packets e relatórios Growth.

Achados:

- LK Growth está carregando corretamente a maioria das rotinas Growth.
- Há muitas revisões D+7 com `deliver=origin`; isso pode ser correto por serem decisões/impact reviews, mas aumenta ruído no Telegram se não vierem em formato decisão curta.
- Alguns jobs misturam Growth com infra/produção aplicada anteriormente. Devem permanecer read-only e gerar handoff quando avaliarem impacto.

Crons LK Growth que precisam de atenção de UX/delivery:

- Weekly/GMC review usam `deliver=telegram`.
- A maioria dos D+7 usa `deliver=origin`.
- Recomendação: não mudar agora; primeiro classificar quais devem virar silent-OK/local e quais devem continuar Telegram por exigirem decisão.

### Mordomo profile

Deve conter:

- WhatsApp pessoal;
- agenda/calendário;
- inbox pessoal;
- CRM pessoal/local;
- follow-ups simples permitidos.

Achados:

- Mordomo contém rotinas pessoais coerentes.
- Mordomo também contém quatro rotinas Zipper e duas rotinas LK WhatsApp. Isso é o maior desalinhamento encontrado.
- Pode ter histórico/razão operacional, mas pelo organograma atual esses jobs precisam ser reclassificados: ou ficam como intake multiempresa do Mordomo com handoff obrigatório, ou migram para Main/Zipper/LK Ops quando houver owner/runtime aprovado.

Crons Mordomo coerentes:

- `Mordomo global WhatsApp watcher — Lucas pessoal`
- `Mordomo global Calendar watcher`
- `Mordomo CRM local sync`
- `Mordomo Decision Inbox digest`
- `Mordomo WhatsApp pessoal resumo 17h BRT`
- `Follow-up Leticia Albuquerque — importação/Portugal`

Crons Mordomo com dono lógico a revisar:

- `Zipper Gmail draft engine — safe draft-only` — dono lógico: Zipper documental/read-only.
- `Zipper direct main e-mail monitor — zipper@zippergaleria.com.br` — dono lógico: Zipper documental/read-only; atenção por `deliver=origin`.
- `Zipper artist PDFs local-only known-answer ingest` — dono lógico: Zipper documental/read-only.
- `ZPR Enquiry Form watcher — approval-gated` — dono lógico: Zipper; atenção por `deliver=origin` e potencial contato/lead.
- `LK WhatsApp Hermes responder watchdog` — dono lógico: LK Ops/Atendimento.
- `LK WhatsApp Hermes responder regression watchdog` — dono lógico: LK Ops/Atendimento.

### SPITI profile

Achados:

- Não há registry local de cron encontrado para SPITI.
- Isso deve ser documentado como estado atual: SPITI pode estar ativo como profile/bot, mas sem scheduler próprio.
- Não criar cron novo sem aprovação; primeiro decidir se SPITI precisa mesmo de rotinas recorrentes próprias.

## Findings principais

### 1. Mordomo está acumulando rotinas de Zipper e LK Ops

Impacto:

- Risco de misturar pessoal, Zipper e LK no mesmo profile operacional.
- Risco de output ficar no lugar errado.
- Risco de handoff insuficiente para Hermes Central/Brain.

Correção recomendada:

- Antes de migrar qualquer cron, criar uma classificação read-only por job:
  - manter no Mordomo como intake multiempresa;
  - mover para Main enquanto Zipper é documental;
  - mover para futuro Zipper profile;
  - mover para futuro LK Ops/Atendimento;
  - manter local/silent-OK.

### 2. Zipper ainda não precisa necessariamente de runtime próprio, mas já tem rotinas suficientes para critério objetivo

Sinais de volume:

- Gmail draft engine;
- e-mail monitor;
- PDFs de artistas;
- enquiry form;
- vendas 09h.

Interpretação:

- Ainda não é prova automática para criar bot Zipper.
- Mas já justifica definir gatilho formal: se esses watchers gerarem decisões/contatos/outputs semanais recorrentes, criar `zipper` profile passa a fazer sentido.

### 3. LK Ops/Atendimento está sem runtime próprio claro

Achados:

- Rotinas comerciais e WhatsApp existem espalhadas entre Main e Mordomo.
- LK Growth está bem isolado para Growth, mas não deve virar dono de atendimento/estoque/preço por conveniência.

Recomendação:

- Manter LK Growth focado em Growth.
- Criar categoria documental `LK Ops/Atendimento` mais explícita antes de qualquer profile novo.

### 4. SPITI sem cron registry deve ser registrado como estado, não erro

Recomendação:

- Atualizar dashboard/status para refletir: `SPITI runtime ativo; cron registry local ausente/não necessário até decisão`.

### 5. Delivery Telegram precisa de revisão antes de mexer em runtime

Achados:

- Main tem pelo menos duas rotinas com `deliver=origin`: Mesa COO e relatório diário 23h+02h.
- LK Growth tem muitos D+7 com `deliver=origin`.
- Mordomo tem vários `deliver=origin`, incluindo Zipper.

Recomendação:

- Não alterar delivery ainda.
- Primeiro classificar:
  - decisão real para Lucas;
  - alerta/exceção;
  - relatório local/silent-OK;
  - handoff para Brain;
  - entrega externa aprovada.

## Próximos passos recomendados

1. Criar `dashboard-coerencia-operacional-hermes.md` com status curto de agentes, profiles, cron owners, handoffs e gaps.
2. Criar `cron-owner-classification-2026-05-26.md` com linha por job e ação recomendada: manter, documentar, migrar depois, pausar depois, transformar em silent-OK.
3. Saneamento do registry do Mordomo antes de qualquer edição, porque o arquivo tem trailing data/bytes inválidos. Fazer só com backup e teste de leitura.
4. Definir critério formal para Zipper runtime:
   - volume semanal de leads/obras/e-mails;
   - necessidade de resposta em canal próprio;
   - fontes e guardrails definidos;
   - handoff obrigatório;
   - humano aprovador claro.
5. Definir se LK Ops/Atendimento merece agente documental próprio antes de considerar bot/runtime.

## Decisão executiva sugerida

Próximo passo de menor risco: produzir a classificação completa linha-a-linha dos crons por dono lógico e recomendação, sem alterar nenhum job.

Não recomendado agora:

- criar bot Zipper imediatamente;
- migrar cron automaticamente;
- mudar `deliver=origin` em lote;
- criar cron novo;
- reiniciar gateway/Docker.
