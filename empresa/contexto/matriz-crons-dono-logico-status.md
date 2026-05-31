# Matriz de Crons — dono lógico, runtime atual e decisão de migração

Data: 2026-05-30
Owner: Hermes Geral / Governança Brain
Status: rotina documental ativa; não executa migração por si só.

## Regra central

Cron registry indica onde a rotina roda hoje; **não define dono lógico**. Antes de migrar, pausar, remover ou alterar qualquer cron, é obrigatório ter:

1. dono lógico confirmado;
2. registry atual identificado;
3. backup/rollback;
4. efeito esperado;
5. aprovação explícita de Lucas quando mudar runtime, schedule, entrega ou side effect.

## Classificação atual

### Hermes Geral / Main

- Registry: `/opt/data/cron/jobs.json`.
- Dono lógico: Governança central, Brain, watchdogs, Mesa COO, rotinas multiempresa.
- Status: correto para crons centrais.
- Pendência: rotinas LK/Zipper históricas devem ser marcadas por dono lógico antes de qualquer migração.

### Mordomo

- Registry: `/opt/data/profiles/mordomo/cron/jobs.json`.
- Dono lógico: Lucas pessoal/intake/follow-up permitido.
- Status: correto para rotinas pessoais.
- Pendência: rotinas Zipper/LK WhatsApp hospedadas por conveniência histórica precisam handoff e owner explícito.

### LK Growth

- Registry: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Dono lógico: SEO/GEO/CRO/GMC/content/analytics.
- Status: correto.
- Regra de entrega: separar decisão/exceção no Telegram de relatório local/silent-OK.

### LK Ops / Atendimento

- Registry próprio consolidado: não observado.
- Dono lógico: atendimento, vendas operacionais, estoque, preço, disponibilidade, Tiny/Shopify operacional.
- Runtime atual relacionado: Main/Mordomo enquanto migração não for aprovada.
- Status: pendência documentada; não é falha operacional automática.
- Próximo passo seguro: inventário linha a linha de crons comerciais antes de propor migração.

### LK Shopify

- Registry próprio consolidado: não observado.
- Dono lógico: Shopify operacional/preview, produto/upload, coleções, publicação com aprovação.
- Status: sem cron próprio por padrão; correto enquanto writes Shopify/Tiny forem approval-gated.
- Próximo passo seguro: só criar cron se houver rotina recorrente read-only ou approval packet aprovado.

### LK Trends

- Registry próprio consolidado: não observado.
- Dono lógico: tendências, sourcing intelligence e sinais de mercado.
- Status: sem cron próprio por padrão; correto enquanto trabalho for on-demand/read-only.
- Próximo passo seguro: documentar periodicidade somente se Lucas quiser rotina de inteligência recorrente.

### SPITI

- Registry próprio consolidado: não observado.
- Dono lógico: Hub, obras, leilões, clientes, CRM/admin, análises verificadas.
- Status: ausência de cron próprio tratada como escolha segura até existir ritual aprovado.
- Próximo passo seguro: declarar ritual desejado antes de qualquer cron.

### Zipper

- Registry próprio: nenhum.
- Runtime dedicado: nenhum.
- Dono lógico: Zipper documental/read-only.
- Status: correto; não criar cron/bot por simetria.
- Gatihos para promoção: volume recorrente, risco de resposta dispersa, canal dedicado, ou decisão explícita de Lucas.

## Quando migrar cron

Migrar somente se todos forem verdadeiros:

- há dono lógico claro diferente do runtime atual;
- a rotina é recorrente e útil;
- o especialista tem profile/runtime/documentação suficiente;
- existe rollback;
- a mudança reduz risco ou melhora resposta;
- Lucas aprovou a migração específica quando houver alteração de runtime/schedule/delivery/side effect.

## Quando não migrar

Não migrar se a razão for apenas estética de organograma, simetria, ou porque existe token/profile preparado. A lógica Bruno/Amora é maturidade viva, não multiplicação de agentes ou crons.
