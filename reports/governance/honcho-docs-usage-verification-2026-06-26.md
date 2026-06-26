# Honcho docs usage verification — 2026-06-26

## Pedido

Lucas pediu: “Leia os docs do HONCHO, na página deles, e verifique se estamos usando o Honcho bem”.

## Fontes oficiais consultadas

- Honcho — Architecture & Intuition: `https://honcho.dev/docs/v3/documentation/core-concepts/architecture`
- Honcho — Reasoning: `https://honcho.dev/docs/v3/documentation/core-concepts/reasoning`
- Honcho — SDK Reference: `https://honcho.dev/docs/v3/documentation/reference/sdk`
- Honcho — Get Context: `https://honcho.dev/docs/v3/documentation/features/get-context`
- Honcho — Storing Data: `https://honcho.dev/docs/v3/documentation/features/storing-data`
- Honcho — Peer Card: `https://honcho.dev/docs/v3/documentation/features/advanced/peer-card`
- Honcho — Reasoning Configuration: `https://honcho.dev/docs/v3/documentation/features/advanced/reasoning-configuration`
- Hermes Agent — Honcho Memory: `https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho`

## Critérios extraídos dos docs

1. Honcho é memória com raciocínio, não só storage/RAG.
2. O modelo correto é Workspace → Peers → Sessions → Messages.
3. Peers são entidades persistentes; sessions são contextos/threads.
4. Messages disparam background reasoning por padrão.
5. Reasoning pode ser controlado em workspace/session/message via configuration.
6. Peer cards são para fatos estáveis/biográficos/preferências/instruções, não estado transitório.
7. Context deve usar summary, recent messages, peer representation, peer card e, quando relevante, `peer_target`, `peer_perspective` e `search_query`.
8. Para chatbots, padrão recomendado é peer do usuário + peer do assistente + session por conversa/thread.
9. Multi-agent deve separar AI peers para evitar contaminação.
10. Token/cadence/depth devem equilibrar custo, utilidade e latência.

## Estado local verificado

### Configuração

- Workspace: `lucas-hermes`.
- User peer: `lucas`.
- AI peers: separados por profile (`hermes-default`, `lk-growth`, `lk-shopify`, `mordomo`, etc.).
- Profiles auditados: 17 `honcho.json`.
- `saveMessages=true`.
- `recallMode=hybrid`.
- `writeFrequency=async`.
- `contextTokens=2000`.
- `contextCadence=1`.
- `dialecticCadence=2`.
- `dialecticDepth=2`.
- `observationMode=unified`.
- `pinUserPeer=true`.

### Health / qualidade

- Honcho quality: `ok`, score `92/100`.
- Memory hygiene: `ok`.
- Peer card count: `10`.
- Queue status endpoint respondeu como `QueueStatusResponse`.
- Utility score: `attention`, score `80/100`.
- Semantic contamination: `attention`, score `55/100`, contamination ratio `0.75`.
- Cleanup candidates: `92`, sanitized; `safe_to_delete_now=false`.

### Código Hermes verificado

- Auto context/dialectic existe no provider Hermes.
- `dialectic_query()` usa `peer.chat()` com target quando AI observe_others permite.
- `get_prefetch_context()` busca summary, user representation/card e AI representation/card.
- `get_session_context()` usa `honcho_session.context(summary=True, peer_target=..., peer_perspective=...)`.
- `_fetch_peer_context()` usa `search_query` quando recebe mensagem do usuário.
- Ingestion filter local novo existe em `session.py`, bloqueando Shopify/order/customer/webhook/address/email/phone/raw payload de entrar no Honcho como memória pessoal.

## Comparação com docs

| Critério oficial | Estado local | Veredito |
|---|---|---|
| Workspace isolado | `lucas-hermes` | bom |
| Peer canônico usuário | `lucas` + `pinUserPeer=true` | bom para single-operator Telegram |
| AI peer separado por agente | sim | bom |
| Session/thread context | Hermes usa session key/gateway key | bom |
| Async writes | `writeFrequency=async` | bom |
| Context com summary/card/representation | implementado | bom |
| `peer_target`/`peer_perspective` | implementado em session context | bom |
| `search_query` para relevância | implementado em peer context | bom |
| Peer card para fatos estáveis | card existe, guardrails adicionados | bom, mas monitorar |
| Reasoning configuration granular por message/session | ainda subutilizado | gap |
| Contaminação semântica baixa | ratio `0.75` | gap crítico/P1 |
| Delete/cleanup histórico seguro | não seguro ainda | correto bloquear |
| Utility mensurada | scorer novo `80/100` | bom avanço |

## Veredito

Estamos usando Honcho **bem tecnicamente e arquiteturalmente**, mas ainda não perfeitamente como memória semântica.

Bom:

- Configuração segue o modelo oficial.
- Workspace/peers/sessions estão coerentes.
- Multi-profile com AI peers separados está alinhado com docs.
- `hybrid`, async, context/dialectic e peer cards estão ativos.
- Honcho quality está alta (`92/100`).
- Utility score já mede valor real (`80/100`).
- Filtro de ingestão foi adicionado para evitar nova contaminação operacional.

Ruim / atenção:

- Histórico antigo tem contaminação semântica alta (`0.75`) por eventos Shopify/pedidos/clientes sob peer `lucas`.
- Ainda não usamos plenamente configuração granular por mensagem/session do Honcho, especialmente `reasoning.enabled=false` em mensagens operacionais.
- Limpeza histórica não deve acontecer sem rollback/snapshot + IDs/granularidade confirmada.
- O filtro patchado no plugin pode precisar de restart controlado para afetar processos já carregados.

## Próximos passos recomendados

P1:

1. Usar configuração por mensagem do Honcho (`reasoning.enabled=false`, `peer_card.create=false`) para payloads operacionais, em vez de só skip local quando aplicável.
2. Restart controlado para carregar filtro de ingestão no gateway vivo.
3. Rodar 7 dias de utility scoring: utility score, contamination ratio, filter events, recall useful/noise.

P2:

1. Implementar cleanup histórico apenas se houver provider rollback/snapshot + IDs seguros.
2. Separar ingestão operacional em sessions/peers próprios quando for necessário usar Honcho para eventos externos.
3. Ajustar specialist profiles com modos mais conservadores (`tools` ou `saveMessages=false`) se algum domínio gerar ruído.

## Non-actions

- Não houve delete Honcho.
- Não houve external write.
- Não houve restart.
- Não houve secrets/PII impressos.
