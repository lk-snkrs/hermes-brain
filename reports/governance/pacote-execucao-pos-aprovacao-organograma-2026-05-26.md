# Pacote de execução pós-aprovação — Organograma/Governança Hermes

Data: 2026-05-26  
Owner: Hermes Geral / COO  
Status: aprovação de princípio recebida; execução deve ser em fases escopadas.  
Produção/runtime: nenhuma alteração feita por este pacote.

## Interpretação da aprovação

Lucas aprovou que agentes possam fazer writes quando houver aprovação. Isso deve ser tratado como política operacional:

- Agente pode executar write **quando o write estiver aprovado e escopado**.
- Aprovação não remove snapshot, preview, readback, receipt e rollback.
- Aprovação ampla não deve disparar migrações/restarts/writes externos em lote sem ordem operacional.
- Em múltiplos sistemas, executar por fases pequenas, verificáveis e reversíveis.

## Fase 1 — local/read-only e docs, pode executar agora

1. Atualizar organograma canônico com profiles ativos.
2. Criar matriz única `agente → dono → profile → bot → área Brain → cron registry → status`.
3. Completar contratos/MAPA de LK Shopify e LK Trends.
4. Registrar status SPITI sobre crons próprios.
5. Criar checklist de handoff/receipt obrigatório.
6. Atualizar docs do Task Router com regra de aprovação escopada.

## Fase 2 — runtime local com aprovação específica por lote

1. Sanear registry Mordomo com backup e validação JSON.
2. Ajustar launcher/env/max iterations dos especialistas.
3. Reiniciar somente gateways afetados, um por vez.
4. Verificar logs: gateway conectado, Telegram ativo, budget esperado, API/webhook secundários desativados quando aplicável.

## Fase 3 — crons/delivery com aprovação específica por lote

1. Classificar jobs por dono lógico.
2. Migrar ou alterar delivery apenas dos jobs listados no lote aprovado.
3. Preservar rollback: backup registry anterior + comandos de restauração.
4. Registrar receipt por job alterado.

## Fase 4 — Zipper runtime/bot, somente se Lucas confirmar gatilho

1. Preparar profile/bot sem iniciar produção externa.
2. Validar token/bot sem expor segredo.
3. API/webhook off por padrão.
4. Start controlado e round-trip com Lucas.
5. Nenhum e-mail/WhatsApp/CRM write sem aprovação separada.

## Fase 5 — writes externos em sistemas de negócio

Para Tiny, Shopify, CRM, Klaviyo, WhatsApp, SPITI Hub, Zipper CRM/Main ou infra:

1. Escopo do item exato.
2. Fonte viva antes.
3. Snapshot antes.
4. Preview.
5. Execução.
6. Readback.
7. Receipt.
8. Rollback documentado.

## Próxima execução recomendada

Começar pela Fase 1 local/docs. É a base para permitir writes futuros com menos ambiguidade e sem bagunçar runtime.
