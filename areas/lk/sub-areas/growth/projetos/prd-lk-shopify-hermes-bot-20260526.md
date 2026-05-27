# PRD — LK Shopify Hermes Bot

Data: 2026-05-26
Status: approval_packet_ready
Dono operacional proposto: LK Growth / LK Shopify
Supervisão: Hermes Geral como orquestrador e guardião de aprovação

## 1. Objetivo

Criar um especialista Hermes separado, chamado **LK Shopify**, como backup/apoio do LK Growth para tarefas de CRO, tema Shopify, SEO técnico/on-page, GMC/feed analysis, QA visual e preparação de alterações em Shopify.

O bot Telegram proposto é `@LKShopify_HermesBot`.

## 2. Problema

O LK Growth concentra analytics, SEO, CRO, GMC e experimentação. Quando ele está ocupado, Lucas precisa de um agente com o mesmo padrão de qualidade para preparar alterações de Shopify, principalmente tema/CRO/SEO, sem misturar com operação geral e sem executar writes perigosos sem aprovação.

## 3. Resultado esperado

- Perfil Hermes isolado: `/opt/data/profiles/lk-shopify`.
- Bot Telegram dedicado: `@LKShopify_HermesBot`.
- Brain dedicado em `areas/lk/sub-areas/growth/lk-shopify/` ou integrado ao Growth com índice próprio.
- Guardrails claros:
  - read-only e preview são livres;
  - dev-theme/theme/Shopify/GMC/Klaviyo/ads writes exigem aprovação explícita;
  - produção Shopify exige backup, preview, rollback e verificação.
- Handoff obrigatório para Hermes Geral/Brain após cada pacote ou execução.
- Operação silent-OK: sem mensagens de sucesso recorrentes; alertar só exceção, bloqueio ou decisão.

## 4. Escopo funcional

### 4.1 Permitido sem aprovação adicional

- Ler documentação Brain/skills.
- Consultar dados read-only de Shopify, páginas públicas, SEO, GSC/GMC quando credenciais existirem.
- Gerar scorecards, relatórios, QA, screenshots, approval packets e rollback plans.
- Preparar código local ou PR/branch sem publicar, quando o repositório/branch for seguro e não houver deploy automático.
- Preparar proposta de dev-theme com diffs e preview, sem upload externo, quando não houver aprovação para write.

### 4.2 Exige aprovação explícita de Lucas

- Qualquer Shopify write: produto, collection, SEO fields, metafields, tags, menus, páginas, apps, webhooks.
- Qualquer upload para theme, mesmo dev/unpublished theme.
- Qualquer publicação/merge/deploy que possa afetar storefront.
- GMC/feed/ProductInput/DataSource writes.
- Klaviyo, ads, WhatsApp, email, campanhas ou comunicação externa.
- Alterações de preço, estoque, disponibilidade, reserva, fulfillment, desconto.

### 4.3 Fora do escopo inicial

- Atendimento a cliente.
- Compras/sourcing.
- Financeiro.
- Automação de campanha.
- Publicação direta em produção sem approval packet.

## 5. Arquitetura proposta

### 5.1 Runtime

- Criar profile Hermes separado: `/opt/data/profiles/lk-shopify`.
- Basear em clone seguro do profile principal ou do `lk-growth`, removendo configurações de API/webhook que gerem conflito.
- Configurar Telegram token no `.env` do profile, nunca no Brain/docs.
- Desabilitar API server/webhook no profile salvo se houver aprovação futura:
  - `API_SERVER_ENABLED=false`
  - `API_SERVER_KEY=`
  - `API_SERVER_HOST=`
  - `API_SERVER_PORT=`
  - `WEBHOOK_ENABLED=false`
  - `WEBHOOK_SECRET=`
  - `WEBHOOK_PORT=`
- Rodar gateway isolado com `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- Watchdog silent-OK em `/opt/data/scripts/` para reiniciar apenas esse profile se cair.

### 5.2 Brain

Estrutura recomendada:

```text
areas/lk/sub-areas/growth/lk-shopify/
├── MAPA.md
├── SOUL.md
├── AGENTS.md
├── TOOLS.md
├── MEMORY.md
├── HEARTBEAT.md
├── APPROVALS.md
├── contexto/
│   ├── escopo-cro-tema-seo.md
│   └── fontes-e-conectores.md
├── rotinas/
│   ├── qa-dev-theme.md
│   ├── seo-field-preview.md
│   └── handoff-hermes-geral.md
└── projetos/
    └── prd-lk-shopify-hermes-bot-20260526.md
```

### 5.3 Identidade do bot

**Missão:** especialista em CRO, tema Shopify, SEO e QA visual da LK, funcionando como backup operacional do LK Growth.

**Tom:** técnico-executivo, premium, comercial, direto; nunca inventar dado; silêncio é melhor que dado errado.

**Padrão de saída:** sempre separar:
- evidência;
- interpretação;
- preview;
- risco;
- bloqueios;
- rollback;
- próxima decisão.

## 6. Modelo de aprovação

### Níveis

- A0 — leitura, relatório, comparação, scorecard: livre.
- A1 — documento/PRD/preview local: livre.
- A2 — branch/PR sem deploy ou write externo: permitido se não acionar deploy automático; registrar no Brain.
- A3 — dev-theme/Shopify/GMC write reversível: exige aprovação explícita com escopo, backup e rollback.
- A4 — produção, campanha, preço, estoque, cliente, app/admin destrutivo: exige approval packet completo e confirmação explícita.

## 7. PRD de implementação técnica

### Fase 0 — Preflight seguro

1. Verificar runtime Hermes e profiles existentes sem imprimir segredos.
2. Verificar se `/opt/data/profiles/lk-shopify` já existe.
3. Confirmar bot via Telegram `getMe` sem expor token.
4. Confirmar que main Hermes e `lk-growth` não serão re-tokenados nem reiniciados.

### Fase 1 — Documentação Brain

1. Criar pasta `areas/lk/sub-areas/growth/lk-shopify/`.
2. Criar `MAPA.md`, `SOUL.md`, `TOOLS.md`, `AGENTS.md`, `MEMORY.md`, `HEARTBEAT.md`, `APPROVALS.md`.
3. Referenciar skills obrigatórias:
   - `hermes-agent`
   - `multiempresa-routing-lucas`
   - `lk-seo-weekly-improvement`
   - `lk-shopify-readonly`
   - `seo-page`, `seo-content`, `seo-ecommerce`, `seo-schema`, `seo-geo` quando aplicável.
4. Garantir que nenhum token entre nos docs.

### Fase 2 — Profile Hermes

1. Criar profile `lk-shopify` por clone seguro.
2. Backup de `config.yaml`, `.env`, `auth.json` se existirem.
3. Inserir Telegram token somente no `.env` do profile.
4. Remover/neutralizar API server e webhook herdados.
5. Escrever `SOUL.md` do profile com escopo e guardrails.
6. Validar auth/model sem imprimir credenciais.

### Fase 3 — Gateway isolado

1. Subir gateway apenas do profile `lk-shopify`.
2. Confirmar logs:
   - profile ativo correto;
   - Telegram polling conectado;
   - sem conflito de porta API/webhook;
   - main Hermes continua com seu token/profile.
3. Lucas deve abrir o bot e enviar `/start`.
4. Se quiser entregas nesse bot, usar `/sethome` dentro do chat do LK Shopify.

### Fase 4 — Watchdog silent-OK

1. Criar script em `/opt/data/scripts/lk_shopify_gateway_watchdog.py`.
2. Detectar gateway por `/proc/<pid>/environ` com `HERMES_HOME=/opt/data/profiles/lk-shopify` e cmdline `hermes gateway run`.
3. Se saudável, stdout vazio.
4. Se ausente, iniciar profile e imprimir alerta curto.
5. Criar cron local/silent se aprovado para operação recorrente.

### Fase 5 — Verificação final

1. `getMe` OK sem imprimir token.
2. Gateway profile OK.
3. Main Hermes não reiniciado/re-tokenado.
4. Brain docs sem segredos.
5. Watchdog dry-run silent-OK.
6. Registro de handoff no Brain.
7. Resumo final a Lucas sem caminhos sensíveis nem token.

## 8. Riscos

- Token foi colado em chat; recomenda-se rotacionar no BotFather após o setup se houver qualquer dúvida sobre exposição em logs.
- Clonar profile pode herdar API/webhook e causar conflito de porta se não limpar `.env`.
- LK Shopify pode virar executor de writes por conveniência; bloquear por padrão com approval packet.
- Upload em dev-theme ainda é write externo e precisa aprovação.
- Se cron/watchdog for criado sem cuidado, pode gerar ruído no Telegram; usar silent-OK.

## 9. Rollback

- Parar gateway do profile `lk-shopify`.
- Remover/desabilitar watchdog/cron do profile.
- Restaurar backups de `.env`, `config.yaml` e `auth.json`.
- Remover token do `.env` ou rotacionar no BotFather.
- Reverter apenas docs locais via backup/git/Brain sync.
- Main Hermes e `lk-growth` não devem ser afetados.

## 10. Critérios de aceite

- Bot LK Shopify existe e responde no Telegram.
- Profile isolado existe e não conflita com API/webhook do main.
- Brain documenta escopo, ferramentas, limites e handoff.
- Nenhum secret/token aparece em docs, relatórios ou resposta final.
- Nenhum Shopify/GMC/theme/Klaviyo/ads write foi feito sem aprovação.
- Lucas recebe apenas aviso limpo de conclusão ou decisão pendente.

## 11. Revisão crítica

Verificação do PRD:

- O escopo cobre CRO, tema Shopify, SEO, GMC e QA visual.
- O bot é backup do LK Growth, não substituto desgovernado.
- Há separação entre preview/read-only e writes.
- Há rollback para profile, gateway, docs e token.
- Há risco explícito para token exposto em chat.
- Há handoff para Hermes Geral/Brain.

Status da revisão: aprovado para implementação local/runtime **somente se** o guardrail permitir profile/gateway/cron writes nesta sessão. Caso o guardrail bloqueie ferramentas de runtime, o próximo passo é aprovar explicitamente a ativação do profile/gateway LK Shopify.