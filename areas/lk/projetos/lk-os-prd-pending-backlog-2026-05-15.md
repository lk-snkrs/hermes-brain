# LK OS — Backlog pendente do PRD

Status: `pending_backlog_canonical`
Data: 2026-05-15
Contexto: LK Sneakers / Projeto LK OS / Hermes Brain
Modo: documentação local. Nenhuma compra, contato, envio, write produtivo, cron, infra ou alteração externa foi executada por este artefato.

## Veredito

Lucas pediu para deixar as frentes anteriores como pendentes e seguir para as próximas etapas. Este arquivo consolida essas pendências como backlog canônico, para o LK OS não perder o estado e para impedir que uma pendência seja tratada como aprovação implícita.

## Pendências canônicas

### P1 — Operação Júlio / Sourcing

Status: `pending`

- Instrução operacional curta para Júlio usar P1/P2/P3 no dia a dia.
- Deve explicar que Júlio confirma disponibilidade, preço final e logística manualmente.
- Hermes não compra, não reserva, não paga, não contata vendedor/fornecedor e não manda WhatsApp.
- Base atual já pronta: sourcing v8/v9/v10/v11, 14 cards, pacote P1 com 4 itens.

### P1 — GMC preço / fonte de verdade

Status: `pending_ui_manual_evidence`

- Preço Merchant continua bloqueado para novos writes.
- Próximo passo pendente: checklist UI/manual Google & YouTube / Shopify / Merchant para SKUs amostra.
- Não reexecutar bulk price patch: ProductInputs v1 e Content API retornaram sucesso, mas readback não persistiu em parte relevante.
- Auto-updates/crawl/source ownership devem ser entendidos antes de qualquer novo patch.

### P2 — Residual GMC deduplicado

Status: `pending_preview_only`

- Gerar preview deduplicado de residuais atuais: `price_updated`, `strikethrough_price_updated`, landing/crawl.
- Separar price-only de salePrice/compare-at/preço riscado.
- Sem Merchant write até novo pacote com rollback e aprovação inline.

### P2 — Lead time real por canal

Status: `pending_business_parameters`

- Substituir lead time padrão por lead time real por fonte/canal.
- Parâmetros pendentes: Droper nacional, StockX/GOAT/importação, interno/Monbam e eventual fornecedor próprio.
- Depende de Lucas/Júlio confirmarem prazos/limites.

### P2 — Klaviyo P1 Draft

Status: `pending_panel_confirmation`

- Campanha P1 permanece Draft.
- Falta confirmar no painel Klaviyo se o HTML aprovado está selecionado no campaign message.
- Sem envio, agendamento, flow ou customer contact até aprovação explícita.

### P1 — LK + Check / Campanha Dia dos Namorados + CRO + Rarity

Status: `pending_improvement_track`

Origem: transcrição `Alinhamento Semanal | LK + Check` enviada por Lucas em 2026-05-15.

Artefato base: `areas/lk/rotinas/alinhamento-semanal-lk-check-2026-05-15.md`.

Regra Lucas: esta frente entra como **pendente do LK OS** porque é uma parte que a LK vai melhorar e precisa ficar visível como melhoria pendente, não como anotação solta de reunião.

Subpendências:

- Dia dos Namorados: transformar em pacote operacional com produtos pronta entrega, promoção, gift card, influenciadores, segmentação e calendário de disparos.
- Gift card: definir valores, regra de uso, validade, tracking, FAQ/atendimento e teste antes de campanha.
- Check/CRO: converter protótipo em backlog testável — modelos em destaque no PDP, ícone/endereço/mapa, personas/influenciadores e repositório cloud de fotos.
- Meta CRO: tratar 0,13% → 0,20% como experimento com baseline, hipótese e métrica, não como mexida solta em tema.
- Rarity: tratar como mini-lançamento premium, com narrativa de drop, pronta entrega, evento, segmentação e conteúdo.
- Novo tênis tecnologia 3D/spray: segmentação só dispara quando conteúdo estiver pronto; primeira comunicação sem desconto para preservar ticket médio, depois teste A/B.

Guardrails:

- Sem envio de e-mail/Klaviyo/WhatsApp/campanha sem aprovação explícita.
- Sem Shopify/Tiny/theme write sem preview, rollback e aprovação.
- Seleção de produtos deve cruzar Shopify + Tiny `LK | CONTROLE ESTOQUE` antes de recomendar pronta entrega/promoção.

### P2 — Mission Control produto/rotina

Status: `pending_scope_cadence_decision`

- Decidir se Mission Control fica: sob demanda, rotina diária/semanal, UI publicada ou worker/Kanban automático.
- UI/cron/worker exige escopo, cadência, rollback e aprovação.
- Até lá, Mission Control segue como cockpit/status/documentação operacional.

### P3 — Loyalty / Rivo / Judge.me

Status: `pending_future`

- Não é frente ativa.
- Retomar apenas quando Lucas pedir explicitamente.
- Pendências preservadas: tiers/marcos Rivo, aniversário, Judge.me/review request, benefícios finais.

## Correção 2026-05-15 — auditoria contra PRD inicial

Lucas apontou corretamente que este backlog estava estreito demais: ele consolidava as frentes recentes, mas não reabria todos os módulos do PRD v0.1/v0.2.

Auditoria criada: `areas/lk/projetos/lk-os-prd-full-gap-audit-2026-05-15.md`.

### Pendências adicionais que voltam ao backlog

P1 real:

1. Data Quality Layer e modelo operacional por variante/tamanho. Status: `v0_local_materialized`; próximo sub-bloco é Tiny stock snapshot completo read-only antes de estado comercial final.
2. Daily Sales Brief / Weekly CEO Review completos versus crons reais.
3. Pulso Comercial 16h como dry-run/template antes de cron.
4. CRO baseline e plano 0,13% → 0,20%.
5. Brand Mix Intelligence 30/90/120 dias.
6. Paid/Influencer attribution dictionary vivo e consequência de estoque.
7. Content & Campaign Production Engine conectado a sinais reais e DesignMD.
8. LK + Check / Dia dos Namorados + CRO + Rarity: transcrição 2026-05-15 virou pendência P1 de melhoria operacional, com pacote Dia dos Namorados, gift card, backlog CRO/protótipo, Rarity e novo tênis 3D/spray.
9. Trend-to-Product-to-Blog router.
10. Operação Júlio/Sourcing P1 já pronta, mas ainda precisa instrução curta.
11. GMC residual/preço continua bloqueado pelos gates já conhecidos.

P2:

1. Shopify Operations: coleções, tags, imagens, PDPs e guia LCWATSAP.
2. SEO orgânico/evergreen separado de GMC/feed.
3. Online vs loja física / WhatsApp / encomenda/importação.
4. Notion LK schema map completo: `LK Compras`, `LK Encomendas`, `LK Stock`.
5. Pricing Intelligence completa: custo trazer por origem, arredondamento e regra de alteração de preço.
6. Integrações pendentes: Wile, LCWATSAP, Cloudcio, Frenet, n8n.
7. Approval Manager / Learning Loop como superfície única de aprovações/resultados.

P3:

1. Cadência completa de crons do PRD.
2. Mission Control UI/worker/Kanban.
3. Loyalty/Rivo/Judge.me quando Lucas retomar.

## Próxima camada após pendências

Com a auditoria completa, a próxima etapa segura do LK OS deve ser uma das duas:

1. **Continuar o primeiro bloco P1 faltante:** Data Quality Layer/modelo operacional por variante já tem v0 local; próximo passo é Tiny stock snapshot completo read-only e estado comercial derivado.
2. **Mapear execução por trilhas do PRD completo**, sem writes, usando a auditoria full-gap como fonte.

Trilhas revisadas:

1. Trilha Data Quality/Data Spine — modelo operacional por variante e qualidade dos dados.
2. Trilha Comercial/Sourcing — pacote P1 pronto; aguarda Júlio/humano e instrução curta.
3. Trilha CRO/Brand Mix/Paid/Content — ainda subimplementada no backlog anterior; inclui agora a frente LK + Check / Dia dos Namorados + gift card + CRO/protótipo + Rarity como pendência P1 de melhoria operacional.
4. Trilha Merchant/GMC — preço/source pendente; residuais preview-only.
5. Trilha CRM/Klaviyo/WhatsApp — draft pendente; online/físico ainda precisa mapeamento.
6. Trilha Shopify/SEO/Conteúdo — operações e evergreen ainda pendentes.
7. Trilha Mission Control/Approval/Learning Loop — precisa virar superfície única.
8. Trilha Loyalty — pending_future.

## Não executado

- Sem compra ou reserva.
- Sem contato com fornecedor/vendedor/cliente.
- Sem WhatsApp/e-mail/campanha.
- Sem Shopify/Tiny/Merchant/Klaviyo/Rivo/Judge.me write.
- Sem cron/UI/worker/infra novo.

## Critério de retomada

Quando Lucas disser “seguir LK OS”, Hermes deve:

1. consultar este backlog;
2. escolher a primeira pendência autorizada ou o próximo bloco read-only seguro;
3. nunca transformar `pending` em execução externa sem aprovação inline;
4. atualizar o plano mestre e rodar Brain health após mudanças.
