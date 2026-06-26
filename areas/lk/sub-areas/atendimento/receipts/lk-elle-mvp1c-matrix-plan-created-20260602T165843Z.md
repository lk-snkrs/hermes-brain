# Receipt — Elle MVP 1C operational matrix and implementation plan

- Data UTC: 2026-06-02T16:58:43Z
- Produto: Elle — Cérebro de Atendimento LK
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Conta: `LK Sneakers` / Account ID `1`

## Ação executada

Após Lucas responder `Seguir`, foram criados os artefatos de planejamento para o MVP 1C:

1. Matriz operacional:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/elle-mvp1-c-operational-matrix-20260602.md`
2. Plano técnico de implementação:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/implementation-plan-elle-mvp1c-chatwoot-20260602.md`

## Escopo documentado

MVP 1C:

- criar nota privada;
- aplicar labels;
- transbordar/atribuir para time humano;
- não enviar mensagem pública automática ao cliente.

Time padrão de transbordo proposto: `atendimento whatsapp`.

## Conteúdo da matriz

- Intenções: saudação, pedido, prazo, estoque, produto, troca, devolução, reclamação, financeiro, VIP, encomenda, ambíguo.
- Labels por intenção.
- Risco por intenção.
- Regras de transbordo.
- Fontes obrigatórias.
- Formato padrão da nota privada.
- Writes candidatos e writes proibidos.
- Approval packet para criação de webhook/agent.

## Conteúdo do plano técnico

- Tarefas para políticas YAML, fixtures, classificador dry-run, idempotência, adapter Chatwoot, contexto Shopify, gate Tiny, relatório dry-run, approval packet e ativação controlada.
- Critérios de verificação antes de chamar operacional.

## Guardrail crítico

Nenhum webhook, agent, write produtivo, mensagem pública, automação externa, alteração em Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema foi executado.

Para avançar para configuração produtiva, Lucas precisa aprovar explicitamente o approval packet do MVP 1C.
