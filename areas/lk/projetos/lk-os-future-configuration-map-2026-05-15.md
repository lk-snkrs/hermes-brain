# LK OS — mapa do que falta configurar para o futuro

Status: `future_configuration_map`
Data: 2026-05-15
Escopo: LK Sneakers / LK OS
Modo: documentação e priorização local. Nenhum Shopify, Tiny, Merchant, Klaviyo, WhatsApp, Notion, n8n, campanha, compra, envio, infra ou cron novo executado.

## Decisão Lucas

Lucas pediu para não avançar agora no checklist do Dia dos Namorados e seguir para o futuro do LK OS.

Portanto, a frente Dia dos Namorados permanece registrada como pendência P1 de melhoria operacional, mas fica fora da frente ativa imediata.

## O que falta configurar — visão executiva

### 1. Data Quality / Estado comercial por variante

Prioridade: P1
Status: `next_safe_core_block`

Falta configurar:

- Retomar snapshot Tiny completo read-only depois do cooldown/rate limit.
- Fechar estado comercial por variante/tamanho: `pronta_entrega`, `encomenda`, `sem_sku`, `tiny_ambiguous`, `tiny_zero`, `needs_manual_code`.
- Ligar esse estado às filas de sourcing, CRM, SEO, Merchant e campanhas.

Por que importa:

Sem esse estado, o LK OS ainda corre risco de recomendar produto/tamanho que está com dado incompleto ou estoque não confiável.

Ação segura imediata:

- Rodar/retomar apenas read-only local/API com throttle conservador.
- Atualizar SQLite local e relatório, sem write externo.

### 2. Mission Control v2 / Superfície única

Prioridade: P1
Status: `pending_scope_cadence_decision`

Falta configurar:

- Transformar reports espalhados em uma superfície curta padrão: hoje, bloqueios, aprovações, risco, próximos 3 passos.
- Definir se será apenas status sob demanda, cron diário/semanal, UI Mission publicada ou worker/Kanban.
- Criar formato de “Inbox COO”: o que Lucas precisa aprovar, o que está bloqueado, o que Hermes pode fazer sozinho.

Ação segura imediata:

- Gerar snapshot v2 read-only/local sob demanda.
- Sem UI/cron/worker novo até Lucas aprovar cadência/superfície.

### 3. Approval Manager + Learning Loop global

Prioridade: P1
Status: `active_local_rule_layer_needs_runtime_surface`

Falta configurar:

- Superfície única de aprovações: aprovado, rejeitado, needs_data, needs_preview, executed, rolled_back.
- Aprendizados do Lucas virarem regra viva em Brain/skills.
- Registrar visual corrections, campanha gates, sourcing gates, GMC gates e tema/CRO gates no mesmo padrão.

Ação segura imediata:

- Consolidado em `areas/lk/rotinas/lk-os-approval-manager-learning-loop-v0-2026-05-15.md`.
- Correção `/background` → draft-only registrada como gate global.
- Próximo: ligar esse ledger à superfície Mission Control v2/InBox COO e, depois, criar runtime/checker sem envio externo automático.

### 4. Brand Mix / Paid / Influencer Intelligence futuro

Prioridade: P1/P2
Status: `partially_started_needs_live_bridge`

Falta configurar:

- Brand Mix 30/90/120 dias com receita real Shopify + estoque Tiny + demanda paga/social.
- Dicionário vivo de influencer/ad_name/ad_id/cupom/UTM/landing/referrer.
- Consequência operacional: quando influencer vende, qual SKU/tamanho repor, pausar, empurrar ou transformar em conteúdo.
- Separar Meta/Pareto como sinal de plataforma, não venda real.

Ação segura imediata:

- Rodar preview read-only com dados reais e marcar confiança por ponte.

### 5. Content & Campaign Production Engine

Prioridade: P2
Status: `pending_designmd_signal_connection`

Falta configurar:

- Motor que transforma sinais reais em briefs de campanha/conteúdo.
- Conectar: produto em alta, ruptura/baixo estoque, SEO query, influencer, CRM segmento e calendário.
- DesignMD/guia visual para não depender de improviso a cada campanha.

Ação segura imediata:

- Criar templates/briefs locais e exemplos de saída.
- Sem e-mail/Klaviyo/WhatsApp/campanha até aprovação.

### 6. Trend-to-Product-to-Blog Router

Prioridade: P2
Status: `pending_router`

Falta configurar:

- Quando aparecer tendência/produto novo, decidir: subir produto, sourcing, blog/SEO, campanha, só monitorar.
- Usar Droper/StockX/GOAT/KicksDev apenas sob demanda, não como full sync permanente.
- Vincular a produto/SKU/tamanho e estoque real antes de acionar compra/campanha.

Ação segura imediata:

- Criar roteador read-only com exemplos e critérios de decisão.

### 7. Lead time real por canal

Prioridade: P2
Status: `pending_business_parameters`

Falta configurar:

- Substituir lead time padrão por lead time real por origem/canal.
- Parâmetros pendentes: Droper nacional, StockX/GOAT/importação, interno/Monbam, fornecedores próprios.
- Definir quando uma oportunidade vira `cotação`, `compra manual`, `não agir` ou `esperar`.

Ação segura imediata:

- Preparar tabela de parâmetros para Lucas/Júlio preencherem.

### 8. GMC residual/preço/governança

Prioridade: P1/P2
Status: `blocked_for_writes_preview_only`

Falta configurar:

- Checklist UI/manual Google & YouTube / Shopify / Merchant antes de novos price patches.
- Preview residual deduplicado atual: `price_updated`, `strikethrough_price_updated`, landing/crawl.
- Separar source ownership/crawl/API/supplemental feed.

Ação segura imediata:

- Gerar apenas preview deduplicado, sem write.

### 9. CRM/Klaviyo/WhatsApp futuro

Prioridade: P2
Status: `draft_and_preview_only`

Falta configurar:

- Confirmar campanha P1 Draft no painel Klaviyo antes de qualquer envio.
- Definir WhatsApp concierge como preview, não envio automático.
- Ligar recompra/RFM a produto disponível e margem/estoque confiável.

Ação segura imediata:

- Auditoria read-only de readiness, sem envio/agendamento/flow.

### 10. Loyalty / Rivo / Judge.me

Prioridade: P3
Status: `pending_future`

Falta configurar:

- Capacidade Rivo para tiers/marcos automáticos por gasto acumulado.
- Review request Judge.me/Klaviyo sem disparo.
- Captura de aniversário e benefícios finais.

Ação segura imediata:

- Só retomar quando Lucas pedir Loyalty/Recompra/Reviews.

## Próximo bloco recomendado agora

Como Lucas pediu futuro e não Dia dos Namorados, o próximo bloco seguro é:

**Configurar o núcleo futuro do LK OS começando pela Data Quality / Estado Comercial por variante.**

Motivo:

- É fundação para sourcing, campanha, CRO, CRM, SEO e Merchant.
- É read-only/local/reversível.
- Reduz erro operacional antes de qualquer automação mais inteligente.

Execução proposta:

1. Retomar Tiny stock snapshot completo read-only com throttle/cooldown.
2. Atualizar SQLite local com estado comercial por variante/tamanho.
3. Gerar relatório curto: quantos `pronta_entrega`, `encomenda`, `sem_sku`, `tiny_zero`, `ambiguous`, `manual_code`.
4. Atualizar Mission Control com esse novo baseline.

## Não fazer agora

- Não continuar checklist Dia dos Namorados.
- Não enviar campanha.
- Não mexer em Klaviyo/WhatsApp/Meta/Google como execução.
- Não fazer novo patch de preço GMC.
- Não comprar/cotar/contatar fornecedor.
- Não publicar UI/cron/worker novo sem escopo.
