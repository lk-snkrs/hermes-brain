# LK Growth — DataForSEO MCP Reload Approval Packet

Data: 2026-05-19
Status: `needs_current_approval_for_runtime_restart`
Tipo: approval packet / runtime-safe plan

## Contexto

O DataForSEO MCP foi instalado, configurado e validado em modo read-only no perfil `lk-growth`:

- package local: `dataforseo-mcp-server@2.9.2`;
- wrapper seguro busca credenciais no Doppler em runtime;
- `list-tools` via stdio retornou 79 tools;
- API DataForSEO respondeu `status_code=20000`;
- Brain já documenta a camada em `CONNECTORS-READONLY-INVENTORY.md` e nos reports de readiness.

O que ainda falta não é documentação nem credencial: falta o runtime ativo do agente recarregar/reiniciar para expor as 79 tools MCP no toolset nativo.

## Decisão necessária

Lucas precisa aprovar explicitamente uma das opções abaixo antes de qualquer ação de runtime:

### Opção A — Sem restart agora

- Manter DataForSEO como instalado/validado, mas não ativo no toolset desta sessão.
- Usar web/SEO/Claude SEO/GA4/GSC/GMC/Shopify para auditorias.
- Reavaliar quando houver janela operacional.

Risco: baixo.
Impacto: sem DataForSEO nativo para SERP/keyword/backlinks/AI visibility live.

### Opção B — Reload/restart controlado apenas do Hermes LK Growth

- Fazer snapshot/read-only do estado antes.
- Recarregar ou reiniciar somente o runtime necessário para o perfil/agente LK Growth, se o ambiente suportar reload isolado.
- Não alterar Docker networks, volumes, Traefik, apps, root password, firewall ou containers não relacionados.
- Verificar após restart:
  - gateway/Telegram ainda responde;
  - MCP server DataForSEO aparece no toolset;
  - smoke test com 1 chamada pequena/baixo custo;
  - logs sem erro crítico.

Risco: médio por mexer em runtime.
Impacto: libera DataForSEO nativo.
Aprovação necessária: sim, explícita no turno atual.

### Opção C — Restart amplo do Hermes runtime

- Só se reload isolado não existir.
- Exige cuidado extra por impactar bot/gateway/crons do Hermes.
- Necessita backup/rollback e janela operacional.

Risco: médio/alto.
Aprovação necessária: sim, explícita no turno atual.

## Pré-checks antes de qualquer runtime action

Executar somente após aprovação:

1. Confirmar container/processo Hermes ativo e escopo do restart.
2. Salvar estado read-only:
   - `docker ps` ou processo equivalente;
   - versão Hermes;
   - logs recentes relevantes;
   - status cron/gateway se disponível.
3. Confirmar que nenhum envio/campanha/job crítico está em execução.
4. Preparar rollback:
   - voltar para estado anterior do serviço/processo;
   - se falhar, parar a mudança e reportar logs;
   - não alterar config persistente sem novo approval.

## Smoke test pós-reload

Após reload/restart aprovado:

1. Verificar se DataForSEO MCP aparece no toolset ativo.
2. Rodar uma única consulta de baixo custo, por exemplo:
   - keyword/SERP limitada para uma query LK;
   - sem batch;
   - sem crawl/export grande;
   - registrar custo/limite quando a API retornar metadados.
3. Atualizar:
   - `CONNECTORS-READONLY-INVENTORY.md`;
   - `growth-360-smoke-test-2026-05-19.md`;
   - changelog;
   - health-check report.

## Guardrails

Este packet não autoriza:

- Shopify/GMC/Klaviyo/Ads writes;
- customer-facing send;
- price/stock/checkout changes;
- Docker network/volume/Traefik changes;
- alteração de outros apps na VPS;
- queries DataForSEO em lote ou custo alto.

## Recomendação

A próxima ação segura é Lucas escolher A, B ou C. Pela regra de proteção da VPS/runtime, o agente não deve reiniciar Hermes/Docker automaticamente apenas com uma intenção genérica de “seguir”; precisa aprovação explícita do tipo:

> “Aprovo a Opção B: reload/restart controlado apenas do Hermes LK Growth para expor DataForSEO MCP.”
