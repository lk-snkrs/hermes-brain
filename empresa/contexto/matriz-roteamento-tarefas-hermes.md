# Matriz de Roteamento de Tarefas — Hermes

Data: 2026-05-24  
Status: aprovado para Fase 1 documental  
PRD: `areas/operacoes/prds/hermes-orquestrador-tarefas-organograma-prd-2026-05-24.md`

## Como usar

Antes de executar uma tarefa operacional, Hermes Geral deve:

1. identificar contexto/empresa;
2. identificar tipo de tarefa;
3. consultar esta matriz;
4. executar no profile certo ou rotear;
5. respeitar approval boundary;
6. registrar handoff quando relevante.

Regra:

> Se existe especialista dono claro, Hermes Geral não deve executar por conveniência.

## Matriz v1

### 1. COO / decisão central

- **ID:** `central-coo-decision`
- **Triggers:** decisão, priorização, Mesa COO, “o que faço agora?”, “faz sentido?”, “aprovar/não aprovar”.
- **Contexto:** multiempresa/global.
- **Orquestrador:** Hermes Geral.
- **Executor:** Hermes Geral.
- **Output:** decisão curta, approval packet, botões/Telegram, registro no Brain quando durável.
- **Permitido sem aprovação:** análise, organização, documentação, plano, packet.
- **Exige aprovação:** ação externa, produção, write, cron novo, Docker/VPS.
- **Handoff:** se gerar decisão durável, registrar em Brain/skill/rotina.

### 2. LK Growth — conteúdo/blog/source pages/SEO/GEO/CRO copy

- **ID:** `lk-growth-content`
- **Triggers:** blog, source page, página SEO, copy SEO, GEO blocks, FAQ, schema editorial, conteúdo LK, Renan, newsletter de conteúdo.
- **Contexto:** LK Sneakers / Growth.
- **Orquestrador:** Hermes Geral.
- **Executor:** LK Growth profile.
- **Runtime:** `/opt/data/profiles/lk-growth`.
- **Brain path:** `areas/lk/sub-areas/growth/`.
- **Output:** draft, HTML/MD, brief, approval packet, scorecard, report.
- **Permitido sem aprovação:** pesquisa read-only, briefing, draft local, schema proposto, packet, preview local.
- **Exige aprovação:** Shopify Page/Product/Collection/theme write, publicação, Klaviyo send, GMC/feed write, Meta/Google Ads, produção.
- **Handoff:** obrigatório para conteúdo criado/revisado/aprovado/enviado, packets e riscos.
- **Anti-erro:** Hermes Geral não escreve conteúdo final da LK; rotear para LK Growth.

### 3. LK Growth — analytics/SEO/CRO/GMC read-only

- **ID:** `lk-growth-analytics-readonly`
- **Triggers:** GA4, GSC, GMC, Merchant, SEO audit, CRO, conversão, PageSpeed, GEO readiness, weekly improvement.
- **Contexto:** LK Sneakers / Growth.
- **Orquestrador:** Hermes Geral ou LK Growth, conforme entrada.
- **Executor:** LK Growth profile preferencial.
- **Runtime:** `/opt/data/profiles/lk-growth`.
- **Output:** relatório, fila priorizada, packet, scorecard, gap de dados.
- **Permitido sem aprovação:** leitura pública/autenticada read-only, relatórios, comparação, packet.
- **Exige aprovação:** qualquer correção em Shopify, GMC, theme, feeds, ads, Klaviyo.
- **Handoff:** obrigatório para packets, decisões, receipts e follow-ups.

### 4. LK operações/atendimento/estoque/preço

- **ID:** `lk-ops-commerce-sensitive`
- **Triggers:** pedido, cliente, estoque, preço, disponibilidade, reserva, desconto, Tiny, Shopify pedido/produto.
- **Contexto:** LK Sneakers / Operações.
- **Orquestrador:** Hermes Geral.
- **Executor:** depende da fonte; se atendimento/cliente, seguir guardrails LK/Mordomo; se produto/upload, usar skill LK apropriada.
- **Output:** resposta verificada, packet, rascunho, diagnóstico.
- **Permitido sem aprovação:** leitura read-only, resolução local de variantes, rascunho interno.
- **Exige aprovação:** preço, disponibilidade prometida, reserva, contato externo sensível, Shopify/Tiny write.
- **Handoff:** obrigatório se houver decisão ou resposta material.

### 5. Mordomo / Lucas pessoal

- **ID:** `mordomo-personal-intake`
- **Triggers:** WhatsApp pessoal, agenda, lembrete, follow-up, cliente no WhatsApp pessoal, compromisso, cobrança simples.
- **Contexto:** Lucas pessoal / multiempresa intake.
- **Orquestrador:** Hermes Geral.
- **Executor:** Mordomo profile.
- **Runtime:** `/opt/data/profiles/mordomo`.
- **Output:** triagem, lembrete, evento, follow-up permitido, draft.
- **Permitido sem aprovação:** calendário claro quando dentro dos guardrails, follow-up simples conhecido/verificado conforme exceção aprovada, alerta para Lucas.
- **Exige aprovação:** preço, disponibilidade, reserva, negociação, reclamação, fornecedor/compra, campanha/bulk, promessa material.
- **Handoff:** decisões, exceções, contatos sensíveis e aprendizados devem voltar ao Brain.

### 6. Zipper comunicação/CRM/obras

- **ID:** `zipper-os-readonly-comm-crm`
- **Triggers:** Zipper, artista, obra, colecionador, proposta, vendas_tango, logística de obra, exposição.
- **Contexto:** Zipper Galeria.
- **Orquestrador:** Hermes Geral.
- **Executor:** Zipper documental/read-only hoje; futuro profile Zipper quando existir.
- **Fontes:** Zipper Vendas `vendas_tango`, CRM/Main quando aplicável, textos institucionais no Brain.
- **Output:** análise, draft interno, relatório, evento com dados claros quando permitido.
- **Permitido sem aprovação:** leitura/análise, rascunho interno, relatório, organização documental.
- **Exige aprovação:** contato com colecionador/artista, proposta, preço, disponibilidade, logística externa sensível, e-mail/WhatsApp.
- **Handoff:** obrigatório para relatório enviado/agendado, decisão, proposta/draft material ou risco.

### 7. SPITI OS

- **ID:** `spiti-os`
- **Triggers:** SPITI, leilão, lote, lance, Hub, Financial, obra SPITI, bidder, SPITI Growth.
- **Contexto:** SPITI Auction.
- **Orquestrador:** Hermes Geral ou SPITI bot quando a entrada vier por lá.
- **Executor:** SPITI profile.
- **Runtime:** `/opt/data/profiles/spiti`.
- **Output:** análise verificada, PRD, issue/PR, packet, relatório read-only.
- **Permitido sem aprovação:** leitura read-only, documentação, análise com fonte, PRD, branch/PR quando solicitado conforme guardrails.
- **Exige aprovação:** deploy, banco/write, cliente/bidder contact, afirmação de lance/lote sem fonte oficial, publicação.
- **Handoff:** obrigatório para decisões, PRs, output de Hub/Financial/Growth e riscos.

### 8. Operações Hermes / Brain hygiene

- **ID:** `hermes-ops-brain-governance`
- **Triggers:** Brain, memória, skills, crons, watchdog, noise, handoff, governance, “organograma”, “Amora/Bruno”.
- **Contexto:** Operações Hermes / Governança.
- **Orquestrador:** Hermes Geral.
- **Executor:** Hermes Geral; scripts/crons aprovados quando existirem.
- **Output:** PRD, docs, skill patch, relatório de governança, health check.
- **Permitido sem aprovação:** documentação, auditoria local/read-only, skill/rotina quando corrige procedimento aprovado, relatórios internos.
- **Exige aprovação:** cron novo, Docker/gateway/restart arriscado, VPS/root/Traefik/volumes/networks, exposição de portas/secrets.
- **Handoff:** registrar alterações de governança e decisões duráveis.

### 9. Tecnologia / Infraestrutura / Mission Control

- **ID:** `tech-infra-mission-control`
- **Triggers:** deploy, Vercel, GitHub, repo, Mission Control, API, Docker, VPS, dashboard, plugin.
- **Contexto:** Tecnologia / Infra.
- **Orquestrador:** Hermes Geral.
- **Executor:** Hermes Geral ou agente de código delegado, conforme plano.
- **Output:** plano, branch, PR, relatório, preview, rollback.
- **Permitido sem aprovação:** leitura, inspeção, testes locais, branch/PR quando seguro e solicitado, docs.
- **Exige aprovação:** produção, deploy, Docker/VPS/root/SSH/Traefik/volumes/networks, secrets, write externo.
- **Handoff:** obrigatório para deploy/PR/risco/alteração técnica relevante.

### 10. Pesquisa / conteúdo geral não-LK

- **ID:** `general-research-content`
- **Triggers:** pesquisa, resumo, PRD, relatório, análise sem dono especialista claro.
- **Contexto:** global ou definido pelo pedido.
- **Orquestrador:** Hermes Geral.
- **Executor:** Hermes Geral ou subagente temporário.
- **Output:** resposta, relatório, arquivo, PRD.
- **Permitido sem aprovação:** pesquisa, síntese, documentação local.
- **Exige aprovação:** publicação, envio externo, produção, contato.
- **Handoff:** se decisão durável ou processo repetível.

## Regras de desempate

1. **Empresa vence ferramenta:** se é LK, Zipper ou SPITI, começar pelo contexto da empresa antes da ferramenta.
2. **Dono especialista vence conveniência:** se existe profile dono, rotear.
3. **Fonte viva vence memória:** dados atuais precisam de API/banco/fonte real.
4. **Write externo bloqueia:** preparar packet, não executar.
5. **Handoff fecha o ciclo:** especialista não deixa output só no chat local.

## Exemplos práticos

### Pedido: “faz uma source page do New Balance 530”

- Rota: `lk-growth-content`.
- Hermes Geral: distribui para LK Growth.
- Output: `areas/lk/sub-areas/growth/drafts/`.
- Bloqueio: Shopify/publicação.

### Pedido: “o que responder para esse cliente no WhatsApp?”

- Rota: `mordomo-personal-intake` ou empresa específica.
- Hermes Geral: classifica contexto e risco.
- Output: draft/preview ou envio permitido apenas se simples/conhecido/verificado conforme guardrails.

### Pedido: “confere esse lote da SPITI”

- Rota: `spiti-os`.
- Executor: SPITI profile/fonte verificada.
- Bloqueio: não afirmar lance/lote sem fonte oficial.

### Pedido: “reduz ruído dos crons”

- Rota: `hermes-ops-brain-governance`.
- Permitido: auditoria/listagem/local docs.
- Bloqueio: mudar entrega/cron se não estiver no escopo aprovado.
