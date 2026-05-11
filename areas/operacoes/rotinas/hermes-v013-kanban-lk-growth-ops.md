# Rotina — Kanban LK Growth Ops com Hermes v0.13

Data: 2026-05-10
Escopo: desenho operacional inicial do Mission Control LK usando Kanban v0.13, sem ativar workers de produção.

## Objetivo

Parar de deixar iniciativas LK espalhadas em chat e transformar trabalho recorrente em cards com dono, fonte, próximo passo, evidência e status.

## Board operacional

Nome: `lk-growth-ops`.
Status: criado no Hermes Kanban v0.13 em 2026-05-10, sem workers automáticos e sem exposição pública.
DB local: `/opt/data/kanban/boards/lk-growth-ops/kanban.db`.

Comandos úteis:
- listar: `/opt/hermes/.venv/bin/hermes kanban --board lk-growth-ops list`
- ver card: `/opt/hermes/.venv/bin/hermes kanban --board lk-growth-ops show <task_id>`
- adicionar card seguro: `/opt/hermes/.venv/bin/hermes kanban --board lk-growth-ops create "Título" --body "Fonte, risco, next step" --created-by Hermes`

Cards iniciais criados:
- `t_9ef75b30` — LK Growth Ops — triagem diária de receita e fontes
- `t_0b17108f` — LK Weekly Influencer Email — QA produto-first
- `t_df6dc802` — Paid/Influencer — auditoria Meta ad_name por ad_id
- `t_bc29671d` — Stock/Sourcing — sinais de reposição
- `t_2b69dfc8` — SEO/Google — Search Console/Search Central backlog
- `t_80bbf009` — Hermes Ops — watchdogs no_agent e release watch
- `t_58ddd8d0` — Brain/Process — learning loop de aprovações Lucas

Card adicional criado após ativação do `approvals.mode: off`:
- `t_8ba27e8d` — Hermes v0.13 — Kanban worker readiness pilot

Todos foram deixados `unassigned` de propósito: isso cria o Mission Control durável sem disparar workers/daemon/ações externas.

Colunas:
- Backlog: ideia ou demanda ainda não triada.
- Doing: execução ativa.
- Waiting Lucas: precisa decisão/aprovação/asset do Lucas.
- Waiting External: depende de Meta, Google, Shopify, fornecedor, equipe ou plataforma.
- QA: precisa validação, secret scan, fonte ou visual review.
- Done: entregue com evidência e aprendizado registrado.

## Tipos de card

### Data/Revenue
Fonte: Shopify, Tiny, GA4, Meta, Pareto/Metricool, Supabase LK.
Critério de pronto: números reconciliados, fonte declarada, PII mascarada.

### CRM/Email
Fonte: Shopify/Klaviyo/CRM, mas envio externo exige aprovação.
Critério de pronto: preview aprovado, segmentação explicada, nenhum envio sem autorização.

### Paid/Influencer
Fonte: Meta Ads ad-level, GA4, Shopify bridge seguro.
Critério de pronto: influencer via `ad_name`, produto por SKU/tamanho quando houver bridge confiável; sem inferir produto por campaign/adset genérico.

### Stock/Sourcing
Fonte: Tiny `LK | CONTROLE ESTOQUE`, Shopify SKU, vendas e lead time.
Critério de pronto: produto nome+SKU+tamanho, recomendação separada de decisão de compra.

### Brain/Processo
Fonte: Hermes Brain, skills, memória, rotinas.
Critério de pronto: arquivo atualizado, skill patch se procedimento mudou, secret scan limpo.

### Infra/Hermes
Fonte: Docker/status/logs/cron read-only.
Critério de pronto: evidência sem secrets, plano/rollback se qualquer mudança for recomendada.

## Handoff mínimo de cada card

- Contexto usado: LK/Zipper/SPITI/Hermes/global.
- Fonte consultada.
- Ação executada.
- Risco e aprovação necessária.
- Evidência/arquivo/PR.
- Próximo passo.
- Aprendizado a registrar, se houver.

## Execuções validadas

### 2026-05-11 — `t_9ef75b30` / LK Growth Ops triagem diária

Status: concluído por `lk-analyst-readonly` em modo read-only.

Artefato Brain: `reports/lk-growth-ops/lk-growth-ops-triagem-2026-05-10.md`.

Fontes usadas: Shopify Admin API como venda/source truth; GA4 property LK `348553567` para sessões/canais/conversão; Metricool para Google Ads; Meta Graph API direto para Meta Ads.

Guardrails respeitados: nenhum write externo; nenhum envio; nenhum PII exportado; nenhum Docker/gateway/banco alterado; secret scan limpo no workspace.

Próximo passo: reexecutar em data fechada e investigar apenas se o gap Shopify x GA4 persistir, usando comparação sem PII por timestamp/valor/source-medium mascarado.


### 2026-05-11 — `t_df6dc802` / Meta influencer por `ad_name` + `ad_id`

Status: concluído por `lk-analyst-readonly` em modo read-only.

Artefatos Brain:
- `reports/lk-growth-ops/lk_meta_influencer_adname_audit_2026-05-09.md`
- `reports/lk-growth-ops/lk_meta_influencer_adname_audit_2026-05-09.csv`

Fonte usada: Meta Graph API direto, conta `act_1242062509867163`, nível `ad`, janela `7d_click` + `1d_view`.

Guardrails respeitados: influencer identificado primariamente por `ad_name`; soma por todos os `ad_id` do mesmo influencer normalizado; Maria/Mariah/Maria Fernanda mantidas separadas; nenhum produto/SKU inferido por campaign/adset; nenhum write externo; secret scan limpo nos artefatos publicados no Brain.

Lacuna registrada: produto/SKU por influencer exige bridge Shopify segura por `ad_id`/UTM/cupom/referrer/nota/tag; não foi inferido neste card.


### 2026-05-11 — `t_0b17108f` / QA LK Weekly Influencer Email

Status: concluído por `lk-content-reviewer` em modo read-only.

Artefato Brain: `reports/lk-growth-ops/lk_weekly_influencer_email_qa_2026-05-11.md`.

Veredito: não aprovado para envio. Passou como rascunho técnico local em estrutura produto-first/SKU/tamanho e MIME real; falhou para envio por não comprovar Klaviyo real, conter `display:grid`, incluir criativos/imagens no e-mail semanal padrão e usar `Silvia Henz` em vez de `Silvia Heinz` como canônico.

Guardrails respeitados: nenhum envio externo; nenhum write Klaviyo/Shopify/Meta/GA4; nenhum PII exportado; nenhum Docker/gateway alterado; secret scan limpo no relatório publicado no Brain.

Follow-ups: gerar versão no-creatives e email-safe; gerar/validar preview Klaviyo real ou documentar canal Gmail-only; corrigir canonical label `Silvia Heinz`; revalidar totais Shopify antes de aprovação de envio.


### 2026-05-11 — `t_bc29671d` / Stock-Sourcing sinais de reposição

Status: concluído por `lk-analyst-readonly` em modo read-only; o run original gerou artefatos mas excedeu TTL e foi reclaimado, então a conclusão foi registrada manualmente após verificação e secret scan.

Artefatos Brain:
- `reports/lk-growth-ops/lk_stock_sourcing_signals_2026-05-11.md`
- `reports/lk-growth-ops/lk_stock_sourcing_signals_2026-05-11.csv`

Fontes usadas: Shopify vendas/SKU/line_items sem PII; Tiny consultado por SKU vendido; estoque decisório somente do depósito oficial `LK | CONTROLE ESTOQUE`.

Resultado: 316 SKUs vendidos em 30 dias; Tiny retornou 267 encontrados; depósito oficial explícito em 265/316; lead time por SKU/tamanho não disponível e tratado como lacuna bloqueante para decisão final. Foram gerados sinais analíticos de cotação/sourcing, não decisões automáticas de compra.

Guardrails respeitados: nenhuma alteração Tiny/Shopify; nenhuma PO/compra/repor estoque; nenhum monitoramento amplo de retailers; nenhum PII exportado; nenhum Docker/gateway alterado; secret scan limpo nos artefatos publicados.

Follow-ups: criar/validar campo canônico de lead time por produto+SKU+tamanho; investigar SKUs sem depósito oficial explícito antes de usar estoque total; revisar política de cobertura por categoria/curva.

## Guardrail

Este documento não autoriza ativar workers, criar daemon Kanban, expor dashboard ou alterar gateway. Isso é mudança operacional/produção e exige aprovação Lucas com plano e rollback.
