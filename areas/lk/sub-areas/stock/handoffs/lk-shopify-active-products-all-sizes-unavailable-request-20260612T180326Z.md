# Handoff — LK Shopify → LK Stock: produtos ativos com todas as numerações indisponíveis

- Data UTC: 20260612T180326Z
- Origem: Lucas / Telegram / perfil `lk-shopify`
- Dono solicitado: `[LK] Estoque Loja Física` / `lk-stock`
- Classificação: validação de estoque/disponibilidade; read-only até evidência retornada pelo lk-stock

## Pedido de Lucas

Lucas perguntou se conseguimos ver produtos ativos no site em que todas as numerações estão esgotadas e que não estejam habilitados para vender sem estoque.

## Regra de fronteira aplicada

Pela regra operacional vigente, LK Shopify não deve consultar estoque/disponibilidade diretamente em Shopify, Tiny, DB local, planilha, relatório antigo ou cache próprio quando a pergunta envolve estoque/disponibilidade. Por isso, este handoff pede validação ao dono `lk-stock`.

## Contexto mínimo coletado

- Escopo: LK Sneakers, storefront/Shopify ativo.
- Critério desejado por Lucas:
  1. produto ativo/publicado no site;
  2. todas as variantes/numerações sem disponibilidade vendável;
  3. venda sem estoque desabilitada (`continue selling`/policy deny ou equivalente);
  4. resultado deve listar produto/link/tamanhos afetados e separar evidência de plataforma de verdade de estoque.
- Urgência: operacional; Lucas pediu “fazer”.

## Pedido ao lk-stock

Gerar relatório validado com:

- produtos candidatos ativos no site;
- grade/tamanhos por produto;
- confirmação de que nenhuma numeração está disponível para venda;
- confirmação de que venda sem estoque não está habilitada;
- evidência/fonte usada pelo `lk-stock` conforme sua política (Stock OS/Tiny e fallback/reconciliação se necessário);
- marcação clara: `confirmado`, `não confirmado`, `divergente`, `precisa reconciliação`;
- ação sugerida: manter ativo, ocultar/despublicar, revisar estoque/Tiny, ou encaminhar reposição — sem executar writes.

## Não feito pelo LK Shopify

- Nenhum Shopify/Tiny/DB read direto de estoque/disponibilidade foi executado para este pedido.
- Nenhum write externo foi feito.
- Nenhuma promessa de disponibilidade foi feita.

## Próximo passo

Aguardar retorno/evidência do `lk-stock`. Se a resposta não trouxer evidência suficiente, responder a Lucas como “não confirmado” e pedir reconciliação.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/lk-shopify-active-products-all-sizes-unavailable-request-20260612T180326Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/lk/sub-areas/stock/handoffs/lk-shopify-active-products-all-sizes-unavailable-request-20260612T180326Z.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
