# Organograma de Agentes — Hermes Brain

Última atualização: 2026-05-30

## Status curto

O organograma estratégico está correto: uma Grande Mente central, com Lucas pessoal e os OSs das empresas/frentes abaixo. A versão atual separa explicitamente:

- **camada de negócio**;
- **agente documental**;
- **runtime profile/bot ativo**;
- **dono lógico de rotina/cron**;
- **approval boundary**;
- **handoff/receipt obrigatório quando houver decisão, risco, write ou output durável**.

Regra central:

> Hermes Geral coordena. Especialistas executam no escopo. Brain registra. Produção/externo/write sensível exige aprovação explícita e escopada; quando aprovado, o especialista executa livremente dentro do escopo concedido.

## Hierarquia canônica

```text
Lucas / Telegram principal
  ↓
Hermes Geral — COO / Orquestrador Central
  Runtime: /opt/data
  ↓
Task Router / Approval Gate
  ↓
Hermes Brain — fonte de verdade, evidência, handoff, memória e skills
  ├── Lucas pessoal / Mordomo
  │   ├── Runtime: /opt/data/profiles/mordomo
  │   └── Dono lógico: intake pessoal, agenda, follow-ups permitidos, triagem pessoal/multiempresa
  │
  ├── [LC] Claude Cli — brainstorm de pautas
  │   ├── Runtime: /opt/data/profiles/lc-claude-cli
  │   ├── Modelo: Claude via Claude CLI/proxy local
  │   └── Dono lógico: ideação editorial, pauta, ângulos, títulos e briefs internos; sem publicação/envio automático
  │
  ├── LK OS — LK Sneakers
  │   ├── LK Growth
  │   │   ├── Runtime: /opt/data/profiles/lk-growth
  │   │   └── Dono: SEO, GEO, CRO, GMC, analytics, conteúdo, source pages, D+7 impact reviews
  │   ├── [LK] Otimização de Coleção
  │   │   ├── Runtime: /opt/data/profiles/lk-collection-optimizer
  │   │   └── Dono: LKGOC, otimização de coleções, guias/páginas de produto-modelo, evidence packets, scorecards, approval packets e impact reviews; Shopify writes approval-gated
  │   ├── LK Ops / Atendimento
  │   │   ├── Runtime: /opt/data/profiles/lk-ops
  │   │   └── Dono: atendimento, loja, vendas operacionais, estoque, preço, disponibilidade, Tiny/Shopify operacional
  │   ├── LK Shopify
  │   │   ├── Runtime: /opt/data/profiles/lk-shopify
  │   │   └── Dono: Shopify operacional/preview, produto/upload, superfície de publicação, sempre approval-gated para writes
  │   └── LK Trends
  │       ├── Runtime: /opt/data/profiles/lk-trends
  │       └── Dono: tendências, sourcing intelligence, sinais de mercado, pesquisas read-only
  │
  ├── Zipper OS — Zipper Galeria
  │   ├── Status atual: documental/read-only
  │   ├── Runtime dedicado: não criado nesta data
  │   └── Dono lógico: CRM/Main, vendas, artistas, colecionadores, enquiries, rascunhos internos
  │
  ├── SPITI OS — SPITI Auction
  │   ├── Runtime: /opt/data/profiles/spiti
  │   └── Dono: Hub, obras, leilões, clientes, CRM/admin, análises com fonte verificável
  │
  ├── Brain Process / Governança documental
  │   └── Dono: higiene Brain, relatórios, handoffs, FTS, health checks
  │
  ├── Operações Hermes
  ├── Tecnologia / Infraestrutura
  └── Governança / Segurança / Aprovações
```

## Tipos de agente

### 1. Hermes Geral

- Caminho documental: `agentes/hermes-geral/`.
- Runtime: profile principal `/opt/data`.
- Papel: Chief of Staff/COO central, roteamento, Brain, decisões, Mission Control, crons, skills, integrações e guardrails.
- É a entrada padrão para Lucas no Telegram principal.
- Limite: não é executor universal; quando a matriz define especialista dono, deve rotear, cobrar handoff e registrar no Brain.
- Pode executar diretamente: governança central, documentação, auditoria local/read-only, PRDs, approval packets e coordenação multiempresa.

### 2. Mordomo / Lucas pessoal

- Runtime: `/opt/data/profiles/mordomo`.
- Papel: intake pessoal, follow-ups, inbox, drafts internos, agenda e roteamento pessoal/multiempresa.
- Regra: follow-up simples conhecido/verificado pode avançar conforme exceção aprovada; preço, disponibilidade, reserva, negociação, reclamação, fornecedor, campanha/bulk e promessa material exigem aprovação/fonte.
- Gap atual: rotinas Zipper/LK WhatsApp hospedadas no Mordomo devem ter dono lógico explícito e handoff.

### 2b. [LC] Claude Cli / brainstorm de pautas

- Caminho documental: `agentes/lc-claude-cli/`.
- Runtime: `/opt/data/profiles/lc-claude-cli`.
- Modelo: Claude via `claude-max-api`/Claude CLI proxy local (`http://127.0.0.1:3456/v1`).
- Papel: canal criativo de Lucas para brainstorm de pautas, ângulos editoriais, títulos, perguntas de pesquisa e briefs internos.
- Regra: ideação e organização são livres; publicação, envio externo, campanha, cron editorial ou alteração em superfícies de negócio exigem aprovação explícita e roteamento ao especialista correto.
- Status: profile CLI criado e validado; gateway/Telegram dedicado não ativado até existir token/canal aprovados.

### 3. LK OS — visão por subespecialista

#### LK Growth

- Caminho operacional: `areas/lk/sub-areas/growth/`.
- Runtime: `/opt/data/profiles/lk-growth`.
- Bot: `@LKGrowth_HermesBot` quando ativo.
- Dono: SEO/GEO/CRO/GMC/analytics/conteúdo/source pages/D+7 impact reviews.
- Regra: Growth é read-only/preview por padrão; Shopify/GMC/GA4/GSC/Klaviyo/Meta writes exigem approval packet e aprovação explícita.
- Anti-erro: Growth não é dono de atendimento, estoque, preço, disponibilidade ou loja.

#### [LK] Otimização de Coleção

- Caminho documental: `agentes/lk-otimizacao-colecao/`.
- Caminho operacional: `areas/lk/sub-areas/growth/collection-optimizer/`.
- Runtime: `/opt/data/profiles/lk-collection-optimizer`.
- Bot: `@lk_otimizacaodecolecao_bot`.
- Dono: LKGOC, otimização de coleções, guias/páginas de produto-modelo, evidence packets, scorecards, approval packets, receipts e impact reviews.
- Regra: read-only/preview por padrão; Shopify/theme/page/collection/metafield/SEO field writes exigem aprovação explícita, rollback, readback e receipt; preço/estoque/atendimento continuam fora do escopo.

#### LK Ops / Atendimento

- Caminho operacional: `areas/lk/sub-areas/atendimento/`.
- Runtime: `/opt/data/profiles/lk-ops`.
- Dono: atendimento, loja, vendas operacionais, WhatsApp/Chatwoot, pós-venda, triagem e resposta final ao cliente/equipe.
- Regra crítica: estoque, pronta entrega, disponibilidade, grade/tamanho, ruptura/baixo estoque e divergência SKU/Tiny/Shopify devem ser roteados obrigatoriamente para `lk-stock`; LK Ops não corrige/mapeia disponibilidade por conta própria.
- Regra: rascunho interno e diagnóstico read-only OK; promessa material, contato externo sensível e writes exigem aprovação explícita e escopada.

#### [LK] Estoque Loja Física

- Caminho operacional: `areas/lk/sub-areas/stock/`.
- Runtime: `/opt/data/profiles/lk-stock`.
- Dono: estoque físico, pronta entrega, disponibilidade por SKU/tamanho, ruptura/baixo estoque, best sellers disponíveis e filas de reposição/transferência/compra.
- Fonte de verdade: Tiny / `LK | CONTROLE ESTOQUE`; Shopify é superfície/gatilho/contexto, não verdade final de estoque.
- Regra: todos os agentes LK devem rotear demandas de estoque/pronta entrega para `lk-stock`; nenhum agente promete disponibilidade sem evidência retornada por ele.

#### LK Shopify

- Caminho operacional: `areas/lk/sub-areas/shopify/`.
- Runtime: `/opt/data/profiles/lk-shopify`.
- Dono: Shopify operacional/preview, produto/upload, coleções, superfícies de publicação e integração com Tiny quando aprovado.
- Regra: nenhum write em Shopify/Tiny sem snapshot, preview, aprovação, execução escopada, readback, receipt e rollback.
- Padrão canônico: usar `areas/lk/sub-areas/shopify/templates/preview-aprovacao-shopify.md` e as skills `lk-shopify-readonly`/`lk-shopify-product-upload`; quando publicar conteúdo editorial/guia via Shopify, herdar o padrão Moon Shoe do LK Growth.

#### LK Trends

- Caminho operacional: `areas/lk/sub-areas/trends/`.
- Runtime: `/opt/data/profiles/lk-trends`.
- Dono: tendências, sourcing intelligence, sinais de mercado, validação Droper/StockX/GOAT e oportunidades.
- Regra: pesquisa e relatório read-only OK; compra, reserva, negociação, disponibilidade, preço final e fornecedor exigem aprovação/fonte.

### 4. Zipper OS

- Caminho operacional: `areas/zipper/`.
- Agente documental: `agentes/zipper/`.
- Runtime dedicado: não existe hoje.
- Runtimes atuais relacionados: Main/Mordomo para rotinas documentais/read-only e intake.
- Fontes: CRM/Main, `vendas_tango`, textos institucionais, inbox e documentos no Brain.
- Regra: rascunhos e análises internas OK; colecionadores, artistas, propostas, preço, disponibilidade, logística e comunicação externa exigem aprovação explícita e escopada.
- Critério: criar runtime/bot próprio só se volume/risco/canal justificarem por período observado.

### 5. SPITI OS

- Caminho operacional: `areas/spiti/`.
- Runtime: `/opt/data/profiles/spiti`.
- Fonte: SPITI Hub/repo, Supabase/CRM e fontes verificadas de leilão/lances.
- Regra: silêncio é melhor que dado errado; lance/lote só com fonte verificável.
- Status de crons: registry local não encontrado em auditoria; documentar como escolha explícita ou pendência antes de criar rotina.

### 6. Brain Process / profiles auxiliares read-only

- Perfis observados: `brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`.
- Status: auxiliares/read-only/experimentos; não devem virar runtime público ou dono de produção sem justificativa e aprovação.
- Próxima ação: classificar cada um como ativo, experimento, arquivo ou candidato a pausa.

## O que é fonte de verdade

- Organograma global: `empresa/contexto/organograma-agentes-hermes.md`.
- Orquestração por tarefa: `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`.
- Matriz executor/aprovação/handoff: `empresa/contexto/matriz-roteamento-tarefas-hermes.md`.
- Algoritmo operacional: `empresa/contexto/task-router-hermes.md`.
- Política canônica de autonomia/aprovação: `empresa/contexto/politica-autonomia-aprovacao-hermes.md`.
- Matriz runtime/donos/status: `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`.
- Matriz cron/dono lógico/status: `empresa/contexto/matriz-crons-dono-logico-status.md`.
- Critérios de promoção de auxiliares/novos agentes: `empresa/contexto/criterios-promocao-agentes-auxiliares.md`.
- Rotina de revisão do organograma vivo: `areas/operacoes/rotinas/revisao-organograma-vivo-amora-bruno.md`.
- Regras globais: `AGENTS.md` e `agentes/hermes-geral/AGENTS.md`.
- Regras por negócio: `areas/<empresa>/MAPA.md` + documentação em `agentes/<empresa>/` e `areas/<empresa>/sub-areas/`.
- Runtime real: processos `hermes gateway run`, `HERMES_HOME`, registries de cron e configs dos profiles.

## Gaps conhecidos

1. Main e Mordomo ainda hospedam algumas rotinas LK Ops/Zipper por histórico; manter temporariamente com dono lógico explícito até migração aprovada. A classificação documental vive em `empresa/contexto/matriz-crons-dono-logico-status.md`.
2. LK Shopify, LK Trends, LK Ops/Atendimento e demais especialistas ativos já têm contrato documental mínimo uniforme (`SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS`, `MEMORY`); manter revisão periódica para evitar drift.
3. Watchdog global canônico dos gateways Telegram esperados: cron `b78ae7ac81d0`, script `scripts/hermes_all_gateway_watchdog.py`; cobre Main check-only + Mordomo + LK Growth + SPITI + LK Ops + LK Shopify + LK Trends.
4. SPITI sem cron próprio consolidado é tratado como escolha segura até existir ritual aprovado; qualquer cron novo/migração exige aprovação.
5. Zipper permanece sem runtime dedicado; critérios de promoção estão em `empresa/contexto/criterios-promocao-agentes-auxiliares.md`.
6. Todo profile/bot especialista deve reportar trabalho relevante ao Hermes Central e/ou registrar no Brain.

## Melhorias prioritárias recomendadas

Para ficar mais próximo da maturidade ritual/identitária observada na Amora, o próximo ganho não é criar mais agentes nem reduzir autonomia. É fechar contrato e uniformizar execução:

1. **Contrato completo por especialista**
   - garantir, para cada profile/bot, um pacote mínimo consistente: `IDENTITY`, `SOUL`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS`, `MEMORY` e template de `handoff`;
   - o pacote define fronteira, não microgestão;
   - LK Ops, LK Shopify e LK Trends devem continuar com a mesma clareza de dono, mas sem centralizar execução desnecessariamente.

2. **Handoff/receipt padronizado**
   - um formato único para decisão, preview, bloqueios, o que foi feito, o que ficou pendente e qual é o rollback;
   - evitar variação de formato entre Hermes Geral, LK, SPITI e Zipper;
   - handoff não é reaprovação: é registro, continuidade e memória.

3. **Separar sempre dono lógico, runtime e cron**
   - dono lógico da rotina não é automaticamente o profile que hoje a executa;
   - documentar explicitamente quando uma rotina está em Main/Mordomo por histórico e quando já tem owner próprio.

4. **Critérios de promoção para Zipper e perfis auxiliares**
   - manter Zipper documental/read-only até existir gatilho objetivo de volume, risco ou canal;
   - classificar auxiliares como ativo, experimento, arquivo ou candidato a pausa.

5. **Autonomia preservada por design**
   - documentação, handoff e receipt existem para dar contexto e segurança;
   - aprovação escopada deve destravar a execução do especialista no escopo aprovado, sem loop de bloqueio desnecessário;
   - evitar que governança vire microgerenciamento do perfil correto.

6. **Fechar a linguagem de autonomia**
   - manter a regra de que aprovação escopada destrava execução do escopo aprovado;
   - `seguir` continua significando continuidade local/documental, não novo bloqueio e não write externo.

## Regra curta

**A Grande Mente coordena. Profiles e bots são superfícies de execução. Agentes documentais explicam escopo e guardrails. Nenhum especialista vira uma mente separada. Writes são permitidos quando Lucas aprova de forma explícita e escopada, com preview/readback/receipt/rollback.**

## Autonomia por nível

Para evitar a sensação de "perda de autonomia" sem abrir mão da segurança, o organograma deve ser lido em três níveis. Fonte canônica: `empresa/contexto/politica-autonomia-aprovacao-hermes.md`.

1. **Autonomia livre local**
   - leitura, auditoria, síntese, documentação, preview, organização e diagnóstico read-only;
   - não pede aprovação quando não há write, contato externo, produção ou mudança de runtime sensível.

2. **Autonomia local com escopo aprovado**
   - manutenção bounded de runtime/profile nomeado;
   - restart controlado do perfil correto;
   - ajuste de launcher/env apenas do escopo aprovado;
   - correção de bugs locais, desde que não envolvam Docker, VPS, Traefik, secrets ou writes externos.

3. **Ações sensíveis / writes externos: somente com aprovação explícita atual**
   - produção, contatos externos, Shopify/Tiny/Klaviyo/WhatsApp/CRM writes, Docker/VPS/root/SSH/Traefik/volumes/networks e qualquer mudança fora do escopo aprovado;
   - com aprovação explícita atual, o especialista pode executar exatamente o write aprovado sem novo loop de bloqueio.

Regra operacional: **aprovação escopada deve destravar a execução do que foi aprovado; ela não deve ser reapresentada como novo bloqueio a cada etapa local segura.**

Regra de linguagem: **`seguir` sozinho é continuidade de análise/leitura/documentação; não autoriza write externo, produção, contato externo, Docker/VPS/Traefik/root/SSH, secrets ou ação fora do escopo aprovado.**

## Base Bruno/OpenClaw usada

A lógica vem da Aula 13 do Bruno/OpenClaw: `AGENTS.md` é o **organograma vivo** do time digital, contendo quem é cada agente, quem chama quem, onde vive, permissões cruzadas e governança. A Aula 06 complementa com `MAPA.md` distribuído por pasta; a Aula 07 complementa com a regra de memória: conversa/sessão não basta, conhecimento importante precisa virar arquivo no Brain/workspace.

Síntese aplicada ao Hermes: `areas/operacoes/base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md`.
