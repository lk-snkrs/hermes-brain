# Rotina — Digest/ledger de reviews D+7 da LK Growth

Status: desenho documental aprovado para execução local  
Owner: LK Growth OS  
Supervisor: Hermes Geral / COO  
Cadência pretendida: consolidada, semanal ou sob demanda conforme volume  
Entrega padrão: Brain/local; Telegram apenas para decisão, exceção, falha ou achado material  
Writes externos/runtime: não

## Objetivo

Reduzir ruído dos reviews D+7 da LK Growth sem perder rastreabilidade de impacto.

Hoje existem múltiplos reviews D+7 no profile `lk-growth` entregando separadamente em `origin`. O ownership está correto, mas a experiência operacional pode virar excesso de notificações. Esta rotina define um digest/ledger que consolida esses reviews antes de qualquer mudança de cron.

## Regra central

Não alterar cron, `deliver`, schedule, gateway ou runtime nesta fase. Primeiro validar o formato local e a utilidade executiva.

## Entradas

Usar read-only:

- Registry do profile LK Growth: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Reports e receipts em `reports/governance/` e `areas/lk/sub-areas/growth/reports/`.
- Dados de impacto quando disponíveis: GA4, GSC, GMC, Shopify, PageSpeed, SERP, logs/receipts.
- Contexto Brain: `IMPACT-REVIEWS.md`, `projetos/growth-action-prd-2026-05-19.md`, handoffs e approval ledger.

## Reviews D+7 inicialmente candidatos à consolidação

Lista observada na reauditoria de 2026-05-25:

- LK Auth Hub D+7 impact review
- LK blog boutique premium D+7 impact review
- LK cart intent Crisp REST identity review D+7
- LK collection GEO FAQ production D+7 impact review
- LK CRO dev preview impact review — Onitsuka/NB/Kill Bill
- LK D+7 impact review — Adidas SL 72 OG vs RS GEO page table
- LK D+7 impact review — Packet D GEO Source Pages
- LK D+7 review — botão Compre Já branco PDP
- LK D+7 review — PDP CRO production promotion 2026-05-19
- LK GEO llms.txt root D+7 impact review
- LK GEO Source Pages D+7 Impact Review
- LK Menu Drawer Production D+7 Review
- LK n8n checkout abandonado hardening impact review
- LK NB blog rewrite D+7 impact review
- LK PDP CRO hotfix D+7 review — trustbar/reviews/tryon
- LK PDP preorder compact hotfix D+7 review
- LK Recovery OS checkout_started webhook D+7 impact review
- LK Recovery OS T1 go-live D+7 impact review
- LK SEO/GEO Experiment Ledger — weekly impact review

## Classificação do review

Cada item do ledger deve ser classificado como:

- `material_decision`: exige Lucas/Renan/operador decidir algo.
- `material_anomaly`: queda, regressão, falha, alerta de dados ou oportunidade forte.
- `learning_only`: aprendizado útil, sem ação imediata.
- `no_signal_yet`: janela curta ou dados insuficientes.
- `duplicate_or_superseded`: coberto por outro review.

## O que vira Telegram

Enviar para Telegram apenas quando houver:

- decisão 1/N necessária;
- falha/regressão relevante;
- oportunidade comercial material;
- bloqueio que precisa de Lucas;
- confirmação de que um pacote aprovado gerou impacto relevante.

Não enviar Telegram para:

- “rodei e está ok”;
- dados insuficientes sem decisão;
- review duplicado;
- aprendizado incremental que pode ficar no Brain.

## Formato do digest

Salvar em:

`areas/lk/sub-areas/growth/reports/d7-digest/lk-growth-d7-digest-YYYY-MM-DD.md`

Usar o template:

`areas/lk/sub-areas/growth/templates/d7-review-digest-template.md`

## Critério antes de propor mudança de crons

Só propor alteração de `deliver`, pausa, remoção, digest automático ou novo cron depois de:

1. pelo menos duas execuções locais úteis;
2. baixo ruído;
3. formato estável;
4. clareza sobre quais reviews são duplicados/superseded;
5. aprovação explícita de Lucas para mudança runtime.

## Saída esperada por execução local

- Digest consolidado.
- Lista de decisões 1/N, se houver.
- Lista de reviews que podem ficar apenas no ledger.
- Lista de crons candidatos a mudança futura, sem executar mudança.
- Handoff ao Hermes Central quando houver decisão, risco ou aprendizado material.

## Não fazer

- Não alterar crons nesta rotina.
- Não mudar destinos `origin`/`telegram`/`local`.
- Não enviar WhatsApp, e-mail, Klaviyo ou qualquer mensagem externa.
- Não publicar theme, Shopify, GMC/feed, Ads ou conteúdo.
- Não ocultar falta de dados; marcar como `no_signal_yet`.
