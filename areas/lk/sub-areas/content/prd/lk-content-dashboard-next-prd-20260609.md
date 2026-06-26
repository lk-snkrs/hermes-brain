# PRD — LK Content Executive Dashboard em Next.js

Data: 2026-06-09
Owner: LK Sneakers / LK Content
Status: v0 proposto para aprovação técnica de implementação

## 1. Objetivo

Criar um dashboard executivo web para o LK Content que consolide calendário editorial, campanhas Klaviyo, status de drafts/envios, métricas, pós-mortems, pendências e alertas operacionais em uma interface simples, premium e segura.

O dashboard não substitui o Brain. Ele é a camada visual/operacional para leitura e decisão. O Brain continua sendo a fonte documental canônica.

## 2. Problema

Hoje o LK Content já tem receipts, registry, calendário local, crons e métricas, mas a visão está distribuída em arquivos e outputs. O PRD original pede um dashboard executivo no Brain/Telegram; para operação recorrente, uma camada Next.js melhora:

- visibilidade rápida;
- acompanhamento de campanhas;
- leitura de pendências;
- status de automações;
- histórico de aprendizado;
- governança de aprovações.

## 3. Escopo MVP

### 3.1 Páginas

1. **Home / Cockpit**
   - Status geral do LK Content.
   - Próximas ações.
   - Campanhas em andamento.
   - Alertas e bloqueios.

2. **Calendário**
   - Visão mensal/semanal de newsletters e campanhas.
   - Status: ideia, pesquisa, preview, draft, aprovado, enviado, pós-mortem.
   - Links para Brain/receipts/Klaviyo UI quando aplicável.

3. **Campanhas Klaviyo**
   - Campaign ID.
   - Nome.
   - Subject / preview.
   - Status.
   - Send time.
   - Link UI correto: `https://www.klaviyo.com/campaign/{campaign_id}/wizard/1`.
   - Últimas métricas.
   - Checkpoints 2h/24h/72h.

4. **Performance / Pós-mortems**
   - Open rate.
   - Click rate.
   - Revenue/orders quando disponível.
   - Unsub/spam.
   - Aprendizados e confiança.

5. **Pendências / Gates**
   - Aprovações pendentes Lucas/Renan.
   - Bloqueios externos.
   - Ações que exigem dupla confirmação.
   - Pendências de PRD.

6. **Brand/Content Guide status**
   - Últimas atualizações.
   - Hipóteses em teste.
   - Aprendizados aprovados/reprovados.

### 3.2 Fontes de dados MVP

Somente leitura a partir de arquivos locais/Brain já sanitizados:

- `/opt/data/profiles/lk-content/klaviyo/campaign_registry.json`
- `/opt/data/profiles/lk-content/calendario/`
- `/opt/data/profiles/lk-content/brand-guide/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/`
- outputs de métricas sanitizados

Nenhum secret no frontend.
Nenhuma chamada direta do browser para Klaviyo, Shopify, Tiny, Google ou Doppler.

## 4. Fora do escopo MVP

- Login multiusuário complexo.
- Writes em Klaviyo/Shopify/Tiny/Calendar via dashboard.
- Envio/agendamento/ativação por botão.
- Exibição de PII.
- Exibição de secrets/tokens.
- Webhook receiver novo. O receiver Hermes/Vercel existente continua separado.

## 5. Segurança e governança

- Dashboard é read-only no MVP.
- Dados servidos via build/server layer a partir de arquivos sanitizados.
- Não incluir API keys no repo, env público, logs ou client bundle.
- Se houver autenticação, usar proteção simples via Vercel/env ou camada existente, sem PII.
- Ações sensíveis continuam no Telegram com gates atuais:
  - envio/agendamento Klaviyo: dupla confirmação;
  - flow activation: dupla confirmação;
  - deleção: aprovação específica;
  - Shopify/Tiny writes: aprovação específica.

## 6. Arquitetura recomendada

### Etapa 1 — Local PRD + protótipo

- Criar app Next.js local em repo próprio, por exemplo:
  - `lk-content-dashboard`
- Usar App Router.
- Componentes simples, sem dependências pesadas.
- Data adapters lendo JSON/Markdown sanitizados.
- Layout premium minimalista LK.

### Etapa 2 — GitHub

- Criar repo GitHub privado.
- Commit inicial com:
  - Next app;
  - adapters;
  - componentes;
  - README;
  - `.env.example` sem secrets.
- Rodar secret scan antes do push.

### Etapa 3 — Vercel

- Criar projeto Vercel conectado ao GitHub.
- Configurar envs não sensíveis ou paths via server only.
- Deploy preview.
- Validar que o build não expõe paths/secrets indevidos.

### Etapa 4 — Rotina de atualização

- Inicialmente o dashboard lê arquivos locais/receipts atualizados pelos crons/scripts.
- Futuro: gerar um `dashboard_state.json` sanitizado periodicamente para simplificar ingestão.

## 7. Critérios de aceite

MVP pronto quando:

- build Next.js passa;
- deploy Vercel abre;
- dashboard mostra campanha Gifts com status `Sent`, UI link e métricas 2h;
- mostra pendência Renan round-trip;
- mostra watchdog Klaviyo ativo;
- mostra bloqueio Advanced KDP;
- não há secrets no repo, bundle ou output;
- nenhum write externo é executado pelo dashboard.

## 8. Primeira versão de conteúdo

Cards obrigatórios v0:

- `PRD Gate 12`: pendente Renan round-trip.
- `Klaviyo watchdog`: ativo a cada 2h.
- `Gifts Dia dos Namorados`: Sent, campanha monitorada.
- `Pós-envio Gifts`: 2h concluído; 24h/72h agendados.
- `Webhook Klaviyo`: infra OK; Klaviyo bloqueado por Advanced KDP.
- `Próximas ativações`: Calendar mirror, Segment/Flow safe smoke, Advanced KDP request.

## 9. Decisão pedida

Aprovar implementação técnica do MVP Next.js read-only, repo GitHub privado e deploy Vercel preview.

Frase segura de aprovação:

> Pode criar o projeto Next.js read-only do LK Content Dashboard, preparar repo GitHub privado e subir preview no Vercel, sem writes em Klaviyo/Shopify/Tiny/Calendar e sem expor secrets.
