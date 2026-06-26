# Operating Manual — Hermes/LK em produção

Gerado em: 2026-05-30T21:41:19+00:00  
Status: **canônico v0.1**

## 1. Princípio central

Hermes/LK não deve ser operado como “um bot só”. Deve ser operado como um conjunto de perfis com donos, superfícies e riscos diferentes.

A pergunta operacional diária é:

> Qual profile deve responder, qual surface está ativa, qual evidência prova isso e qual ação segura cabe agora?

## 2. Perfis principais

### Hermes Geral / default

- Papel: orquestrador geral, auditoria, coordenação, relatórios, approval packets e trabalhos profundos.
- Risco: tem toolsets amplos e API/webhook ativos no inventário mais recente.
- Regra: não usar como atalho para mexer em tudo. Se o domínio for LK Shopify, LK Ops, Growth, SPITI ou Mordomo, preferir o especialista ou um handoff limpo.

### LK Shopify

- Papel: Shopify, produto/upload, coleções, páginas/objetos Shopify, previews, readback e receipts.
- Fonte de verdade de estoque: **Tiny**, não Shopify.
- Regra: Shopify é superfície/gatilho; Tiny é verdade operacional de estoque.
- Se reportado offline: usar `RUNTIME_REPAIR_RUNBOOK.md`, não fazer mega-audit.

### LK Ops / Atendimento

- Papel: atendimento operacional, estoque, Tiny, pedidos, dúvidas práticas e reconciliação operacional.
- Regra: precisa ser rápido. Telegram conectado mas lento ainda é problema.
- Bloqueios: preço, disponibilidade, reserva, negociação, reclamação sensível, fornecedor, bulk, campanha e logística sensível exigem fonte verificável/approval.

### LK Growth

- Papel: SEO/GEO/CRO/GMC/analytics/content e melhoria de crescimento.
- Regra: trabalho pesado pode rodar em background/local; Telegram deve responder curto quando a pergunta for simples.

### LK Trends

- Papel: tendências, fila de oportunidades, relatórios read-only e insumos para conteúdo/compra/reposição.
- Regra: oportunidade não é ordem de compra nem write Shopify. Separar conteúdo, sourcing e reposição.

### Mordomo

- Papel: Telegram pessoal/follow-ups e ações simples verificadas.
- Regra: pode enviar WhatsApp/e-mail simples quando fatos estiverem verificados; bloquear assuntos sensíveis sem fonte/aprovação.

### SPITI

- Papel: CRM/admin obras/leilões/clientes/IA, Growth SPITI, financeiro ativo e Supabase conforme docs.
- Regra: silêncio é melhor que dado errado. Usar PRs/receipts e não inventar estado.

## 3. O que significa “online”

Não basta processo vivo.

Um bot só deve ser tratado como operacional quando houver:

1. processo `hermes gateway run` vivo com `HERMES_HOME` correto;
2. Telegram conectado;
3. API/webhook externos desligados ou justificados;
4. logs recentes sem erro bloqueante;
5. round-trip provado no bot correto quando o problema for “não responde”.

Estados:

- **Online provado:** processo + Telegram + resposta recente.
- **Vivo mas não provado:** processo existe, mas falta teste de resposta.
- **Degradado:** responde lento, conflito de polling, timeout, fallback ou compressão problemática.
- **Offline:** sem processo correto, Telegram desconectado ou erro bloqueante.
- **Preparado:** config/env existe, mas não há runtime live.

## 4. Regra de comunicação com Lucas

Lucas deve receber pouco e acionável:

- decisão necessária;
- alerta real;
- falha relevante;
- resumo final com evidência curta.

Evitar:

- logs longos;
- `job_id`/wrappers técnicos;
- tokens/chaves;
- “processo vivo” como se fosse “bot respondendo”;
- novos PRDs quando o pedido é reparo operacional.

## 5. Ordem de operação padrão

Para qualquer problema de produção local:

1. Triagem read-only.
2. Identificar profile/surface exato.
3. Confirmar se é chat, API, webhook, cron, provider, toolset ou dado externo.
4. Verificar logs/processo/estado sem imprimir secrets.
5. Se precisar mutar, aplicar `DECISION_POLICY.md`.
6. Executar uma mudança por vez.
7. Verificar sucesso com evidência objetiva.
8. Registrar receipt curto quando houver alteração.

## 6. Frases que devem acionar playbooks

- “LK Shopify está offline” → `RUNTIME_REPAIR_RUNBOOK.md#lk-shopify-offline-ou-nao-responde`
- “LK Ops não responde / está lento” → `RUNTIME_REPAIR_RUNBOOK.md#lk-ops-atendimento-lento-ou-sem-resposta`
- “cron não rodou / não chegou no Telegram” → `RUNTIME_REPAIR_RUNBOOK.md#cron-nao-entregou`
- “modelo travou / provider sem resposta” → `RUNTIME_REPAIR_RUNBOOK.md#provider-modelo-travou`
- “tem gateway duplicado / conflito Telegram” → `RUNTIME_REPAIR_RUNBOOK.md#gateway-duplicado-ou-conflito-de-polling`

## 7. Antipadrões

- Criar mais bots antes de estabilizar os atuais.
- Usar Hermes Geral como executor universal sem roteamento.
- Dizer “online” sem round-trip quando Lucas reporta offline.
- Mexer em Docker/VPS/Traefik/Main para problema de perfil especialista.
- Tratar auditoria histórica como estado atual.
- Enviar Telegram de sucesso para watchdog silent-OK.
