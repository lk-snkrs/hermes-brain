# LK specialists Shopify write autonomy — approval packet

## Destino
Hermes Geral / Task Router / perfis LK Growth, LK Shopify e LK Trends.

## Pedido limpo
Corrigir o roteador/guardrail para que LK Growth, LK Shopify e LK Trends não fiquem presos em modo genérico read-only quando a tarefa é de publicação/alteração na Shopify dentro do escopo aprovado. Dar autonomia operacional aos especialistas para executar writes de Shopify no próprio domínio, com receipts e rollback, sem pedir a mesma aprovação a cada turno.

## Evidências
- O roteador atual tem rota específica apenas para o piloto estreito `lk-shopify-collections-auto-ordering-write-enabled`.
- Rotas gerais de LK Growth/content continuam classificando `publicar`/`Shopify` como `preparar_approval_packet` e exigem aprovação de Shopify/produção.
- A rota final genérica também transforma qualquer intenção de publicação/Shopify em approval packet, mesmo quando Lucas está pedindo uma correção estrutural de autonomia.
- O bloqueio visto no turno não indica erro da Shopify: é guardrail/preflight impedindo a ferramenta antes da chamada.

## Preview da correção proposta
Adicionar rotas específicas e estreitas antes das rotas genéricas:

1. `lk-growth-shopify-write-enabled`
   - Executor: `lk-growth`
   - Permite sem nova aprovação quando houver aprovação operacional atual ou rotina previamente aprovada: preview/snapshot, edição/publicação de conteúdo LK em Shopify, readback, receipt, handoff Brain.
   - Continua bloqueando: preço, estoque, disponibilidade, checkout/theme crítico, campanha paga, Klaviyo/envio externo, escopo novo.

2. `lk-shopify-admin-write-enabled`
   - Executor: `lk-shopify`
   - Permite: produtos/coleções/metafields/merchandising dentro do escopo aprovado, snapshot, write Shopify, poll/readback, receipt.
   - Continua bloqueando: alterações financeiras/preço/estoque sem fonte, checkout/theme crítico, apps/secrets, cron novo, bulk destrutivo sem rollback.

3. `lk-trends-shopify-write-enabled`
   - Executor: `lk-trends`
   - Permite: publicar/atualizar conteúdo de trend aprovado na Shopify, tags/metafields editoriais de trend quando reversíveis, preview, readback, receipt.
   - Continua bloqueando: claims sem fonte, campanha/comms, preço/estoque/disponibilidade, mudanças estruturais de tema/checkout.

4. Regra comum
   - Se Lucas disser explicitamente “aprovado”, “pode publicar”, “seguir”, “dar autonomia”, ou a rotina já estiver documentada como write-enabled, o roteador deve classificar como `executar_aqui`/especialista dono, não como generic approval packet.
   - Todo write precisa gerar receipt limpo: o que mudou, link/ID, fonte, rollback, handoff.

## Risco
- Abrir demais pode permitir alteração errada em produto, estoque, preço, theme ou comunicação externa.
- Deixar como está paralisa os especialistas e força Lucas a repetir aprovação, o que é exatamente o problema reportado.

## Bloqueios que permanecem
- Preço, estoque, disponibilidade, reserva e promessas comerciais sem fonte oficial.
- Theme/checkout/apps/secrets/integrações críticas.
- Campanhas pagas, Klaviyo, WhatsApp/email externo e bulk sem revisão.
- Cron/automação nova sem cadência, kill criteria e rollback.
- Produção/Docker/VPS/Traefik/gateway sem aprovação separada.

## Rollback
- Router: reverter o diff no `scripts/hermes_task_router.py` e nos testes correspondentes.
- Shopify write futuro: cada execução deve tirar snapshot antes, registrar IDs/links alterados, validar readback e guardar instrução de reversão por item/coleção/metafield.

## Próximo passo recomendado
Aprovar a correção local do Task Router: adicionar as 3 rotas write-enabled, testes de classificação para LK Growth/LK Shopify/LK Trends e registrar a mudança no Brain/skill. Isso não executa nenhum write na Shopify ainda; só destrava o roteamento para que, nos próximos pedidos aprovados, o especialista certo possa publicar sem cair no bloqueio genérico.
