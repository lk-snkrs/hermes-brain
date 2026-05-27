# Matriz — agentes, donos lógicos, runtime e gaps

Data: 2026-05-26  
Escopo: documentação local/read-only pós-auditoria Amora/OpenClaw.  
Produção/runtime: nenhuma alteração feita.

## Veredito

O desenho está correto: Hermes Geral coordena, especialistas executam dentro de fronteiras, Brain registra, e produção/externo/write sensível exige aprovação escopada.

O ajuste prioritário é tornar explícito o vínculo entre **dono lógico**, **profile/runtime**, **bot/superfície**, **cron registry** e **handoff**.

## Matriz principal

### Hermes Geral / COO
- Dono lógico: Lucas / Hermes COO.
- Runtime: `/opt/data`.
- Gateway observado: ativo.
- Bot/superfície: Telegram principal.
- Brain: `agentes/hermes-geral/`, `empresa/contexto/`, `areas/operacoes/`.
- Cron registry: `/opt/data/cron/jobs.json`.
- Status: ativo e correto como centro.
- Gap: ainda abriga rotinas de negócio por histórico; precisa owner lógico claro e handoff.
- Próxima ação: manter como orquestrador, não executor universal.

### Mordomo
- Dono lógico: Lucas pessoal / intake pessoal.
- Runtime: `/opt/data/profiles/mordomo`.
- Gateway observado: ativo.
- Bot/superfície: Mordomo Telegram/WhatsApp conforme guardrails.
- Brain: `agentes/mordomo/`.
- Cron registry: `/opt/data/profiles/mordomo/cron/jobs.json`.
- Status: ativo.
- Gap: contém rotinas Zipper/LK por histórico; precisa classificação por dono lógico.
- Próxima ação: manter amplo, mas exigir handoff quando tocar LK/Zipper.

### LK Ops / Atendimento
- Dono lógico: LK Comercial/Ops/Atendimento.
- Runtime: `/opt/data/profiles/lk-ops` preparado; gateway não observado como ativo nesta leitura.
- Bot/superfície: `@LKOps_HermesBot` quando ativo.
- Brain: `areas/lk/sub-areas/atendimento/` e `agentes/lk/`.
- Cron registry: não encontrado no profile; rotinas ainda aparecem em Main/Mordomo.
- Status: categoria correta, runtime/profile preparado, ativação/rotinas pendentes de decisão runtime.
- Gap: precisa ser explicitado como dono de estoque, preço, disponibilidade, vendas operacionais, Tiny e atendimento.
- Próxima ação: docs/owner OK agora; migração de crons/gateway só com pacote de aprovação.

### LK Growth
- Dono lógico: LK Growth.
- Runtime: `/opt/data/profiles/lk-growth`.
- Gateway observado: ativo.
- Bot/superfície: `@LKGrowth_HermesBot` quando ativo.
- Brain: `areas/lk/sub-areas/growth/`.
- Cron registry: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Status: ativo e coerente.
- Gap: muitos D+7/impact reviews podem gerar ruído; não deve absorver Ops/Shopify por conveniência.
- Próxima ação: classificar delivery dos D+7 entre decisão Telegram, relatório local ou handoff Brain.

### LK Shopify
- Dono lógico: LK Shopify / superfície operacional da loja.
- Runtime: `/opt/data/profiles/lk-shopify` preparado; gateway não observado como ativo nesta leitura.
- Bot/superfície: `@LKShopify_HermesBot` quando token/gateway forem ativados.
- Brain: `areas/lk/sub-areas/shopify/`.
- Cron registry: não encontrado.
- Status: deve aparecer como nó próprio dentro do LK OS.
- Gap: contrato documental estava fraco/espalhado; não pode ficar implícito dentro de Growth.
- Próxima ação: manter read-only/preview; qualquer Shopify/Tiny write exige snapshot, preview, aprovação, readback, receipt e rollback.

### LK Trends
- Dono lógico: LK Trends / sourcing intelligence.
- Runtime: `/opt/data/profiles/lk-trends` preparado; gateway não observado como ativo nesta leitura.
- Bot/superfície: futuro/isolado quando justificado.
- Brain: `areas/lk/sub-areas/trends/`.
- Cron registry: não encontrado.
- Status: documental forte e runtime/profile preparado.
- Gap: precisa ficar separado de Growth e Ops: pesquisa/oportunidade não é compra, preço final, promessa ou atendimento.
- Próxima ação: manter como radar read-only; compras/negociações exigem aprovação.

### SPITI OS
- Dono lógico: SPITI Auction.
- Runtime: `/opt/data/profiles/spiti`.
- Gateway observado: ativo.
- Bot/superfície: `@SPITI_HermesBot`.
- Brain: `agentes/spiti/`, `areas/spiti/`.
- Cron registry: não encontrado no profile.
- Status: ativo sem scheduler local próprio observado.
- Gap: documentar se a ausência de crons é escolha ou pendência.
- Próxima ação: não criar crons sem aprovação; manter precisão alta e silêncio > dado errado.

### Zipper OS
- Dono lógico: Zipper Galeria.
- Runtime: dedicado não existe hoje.
- Bot/superfície: não criar por simetria.
- Brain: `agentes/zipper/`, `areas/zipper/`.
- Cron registry: rotinas espalhadas em Main/Mordomo.
- Status: documental/read-only correto por enquanto.
- Gap: volume já sugere critério objetivo para runtime futuro, mas não autorização automática.
- Próxima ação: definir gatilho formal antes de profile/bot.

### Brain Process / Governança documental
- Dono lógico: Hermes Geral / Governança.
- Runtime: profiles auxiliares existem (`brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`), mas sem gateway ativo observado nesta leitura.
- Status: auxiliares/dormentes/read-only.
- Gap: classificar como ativo, experimento, arquivo ou candidato a pausa.
- Próxima ação: não ativar/pausar automaticamente; registrar status e risco.

## Regra operacional curta

- Se é decisão/coordenação multiempresa: Hermes Geral.
- Se é pessoal/intake/follow-up simples: Mordomo.
- Se é estoque/preço/disponibilidade/atendimento/venda operacional: LK Ops.
- Se é SEO/GEO/CRO/GMC/conteúdo/analytics: LK Growth.
- Se é produto/upload/coleção/superfície Shopify: LK Shopify.
- Se é tendência/sourcing/radar de mercado: LK Trends.
- Se é Hub/obras/leilões/clientes SPITI: SPITI.
- Se é galeria/CRM/enquiry Zipper: Zipper documental até runtime aprovado.

## P0 concluído neste arquivo

A matriz deixa explícito o que antes estava implícito: LK Shopify é nó próprio, LK Ops é distinto de Growth, e Zipper segue documental/read-only até gatilho objetivo.
