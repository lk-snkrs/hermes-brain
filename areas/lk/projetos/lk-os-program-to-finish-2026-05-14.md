# LK OS — Programa para fechar o que foi programado

Status: `active_execution_map`
Data: 2026-05-14
Modo: plano operacional local/read-only. Nenhuma ação externa/write foi executada por este mapa.

## Veredito

Para fechar o LK OS programado nesta etapa, a sequência correta é **serializar writes e paralelizar inteligência**:

1. Finalizar e consolidar GMC P2A já autorizado.
2. Ativar o pacote de sourcing somente como consulta/preview depois do GMC.
3. Fechar Mission Control como cockpit operacional curto.
4. Manter Loyalty/Rivo/Judge.me como `pending_future` até Lucas retomar.
5. Não abrir nova frente externa enquanto GMC/sourcing estiverem em gate.

## Linha de execução ativa

### Track A — GMC / Merchant Center

Estado: `completed_post_status_monitor_readonly`.

Fechado até aqui:

- executor P2A principal: 9.826 patches aplicados e verificados por Merchant `products.get`;
- falhas de verificação: 0;
- rollback/progress JSONL preservados;
- mismatch review pós-readback executado;
- point repair de Bags executado em 44 produtos; 43 matches exatos e 1 variação apenas em `productTypes`;
- monitor pós-status: 23.279 productstatuses lidos; 9.826/9.826 IDs P2A presentes; 494 produtos P2A ainda com algum issue/destino reprovado, principalmente preço/promotional price, 136 missing attrs remanescentes e landing page errors.

Próximo fechamento:

- atualizar Mission Control/snapshot com estado final prático;
- tratar residuais GMC em pacotes separados, sem reexecutar P2A em massa;
- não iniciar novo Merchant write sem preview/rollback/aprovação.

### Track B — Stockout / Recompra / Sourcing

Estado: `prepared_waiting_gmc_final`.

Já pronto:

- ranking 120 dias;
- 18 candidatos Tiny zero/tamanho exato;
- padrão LK Compras/Júlio/Notion;
- cards no Mission Control.

Próximo fechamento:

- depois do GMC final, gerar pacote inline de aprovação para Droper read-only;
- limitar ao bucket `stockout_exact_ready`;
- StockX/GOAT só entram como fallback com nova aprovação/scope.

Critério de pronto:

- Lucas recebe payload inline dos candidatos, sem precisar abrir arquivo local;
- consulta Droper não acontece sem aprovação;
- Notion fica preview/log, sem write autônomo.

### Track C — Mission Control

Estado: `active_v2`.

Próximo fechamento:

- atualizar snapshot após GMC final;
- mostrar no painel: GMC final, sourcing queue, Klaviyo Draft, Loyalty pending_future, próximos gates;
- manter formato curto de Telegram.

Critério de pronto:

- Lucas pede `Status Projeto LK OS` e recebe: estado, bloqueios, próximos passos, aprovações pendentes.

### Track D — CRM/Klaviyo P1

Estado: `draft_safe_hold`.

Próximo fechamento:

- manter campanha em Draft;
- não enviar/agendar;
- só retomar quando Lucas pedir ajuste/envio/pausa formal.

Critério de pronto:

- readiness watcher continua manual/read-only;
- nada de cliente externo recebe mensagem sem aprovação.

### Track E — Loyalty / Customer Trust

Estado: `pending_future`.

Não puxar agora como frente ativa.

Pendências preservadas:

- capacidade Rivo/API/admin;
- captura de aniversário;
- audit review request Klaviyo/Judge.me;
- tabela final de tiers/benefícios.

Critério de retomada:

- Lucas dizer explicitamente para voltar a Loyalty/Rivo/Judge.me.

## Backlog de fechamento por ordem

1. `MISSION_CONTROL_REFRESH`: gerar snapshot pós-GMC com P2A `completed_post_status_monitor_readonly`.
2. `DROPER_APPROVAL_PACKET`: montar aprovação inline para 18 candidatos `stockout_exact_ready`.
3. `DROPER_READONLY_EXECUTION`: só se Lucas aprovar; sem compra/contato/write.
4. `GMC_RESIDUAL_PACKETS`: tratar preço/promotional price, color residual e landing page errors em pacotes próprios.
5. `SOURCING_DECISION_QUEUE`: comparar resultados e preparar Júlio/Notion preview.
6. `LK_OS_STATUS_SURFACE`: manter resposta padrão atualizada — fonte atual em `areas/lk/rotinas/lk-os-status-surface-2026-05-14.md`.
7. `LOYALTY_REOPEN`: apenas quando Lucas retomar.

## Guardrails finais desta etapa

- Writes externos: bloqueados salvo o GMC P2A já autorizado/em execução.
- Marketplace: bloqueado até aprovação inline pós-GMC.
- WhatsApp/fornecedor/cliente: bloqueado.
- Notion: bloqueado para write; preview/log permitido.
- Shopify/Tiny/Klaviyo/Rivo/Judge.me/Meta/Google: sem novos writes.
- Infra/Docker/cron/UI: sem mudanças.

## Artefatos de referência

- `areas/lk/projetos/lk-os-implementation-control.md`.
- `areas/lk/projetos/lk-operating-system-prd.md`.
- `areas/lk/projetos/lk-os-prd-continuation-2026-05-14.md`.
- `reports/lk-mission-control-snapshot-2026-05-14.md`.
- `reports/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.md`.
