# Approval packet — Honcho semantic cleanup by ID/filter — 2026-06-26

## Contexto

O Honcho está tecnicamente saudável, mas o auditor semântico segue com `status=attention` porque buscas/contexto sob o peer `lucas` ainda retornam muito material operacional de Shopify/pedidos/clientes/webhooks.

Baseline atual:

- Honcho quality: `ok`, score `92/100`.
- Semantic contamination auditor: `attention`, score `55/100`, contamination ratio `0.75`.
- Raw examples printed: `false`.

## Decisão já executada antes deste packet

A higiene preventiva de ingestão/configuração já foi aplicada:

- `observationMode=unified`.
- `user.observeOthers=false`.
- `ai.observeMe=false`.
- 17 `honcho.json` e 33 host blocks ajustados.

Isso reduz contaminação futura, mas não apaga histórico antigo.

## Próxima limpeza possível

Limpeza por IDs/filtro, **não por heurística cega**.

### Opção A — filtro/ingestão primeiro, sem deleção

Escopo:

- Manter auditor semântico recorrente.
- Criar filtro local para impedir que novas mensagens/eventos operacionais de pedidos/clientes sejam promovidos como fatos pessoais do peer `lucas`.
- Não apagar dados antigos.

Risco: baixo.
Rollback: remover filtro/config local.

### Opção B — quarentena por IDs específicos

Escopo:

- Extrair candidatos agregados sem imprimir PII.
- Gerar lista de IDs/handles internos para revisão.
- Quarentenar/despromover apenas IDs confirmados.

Risco: médio.
Rollback: restaurar snapshot/provider backup quando disponível.
Bloqueio: exige suporte claro do provider/API para IDs e rollback.

### Opção C — deleção direta por heurística

Não recomendada.

Motivo:

- Risco de apagar memória útil.
- Risco de apagar evidência histórica necessária.
- Alto risco sem IDs/rollback.

## Recomendação

Executar Opção A como default e só avançar para B se, após alguns ciclos novos, o contamination ratio não cair.

## Guardrails

- Não imprimir PII/trechos de pedido/cliente.
- Não apagar memória Honcho sem IDs e rollback.
- Brain continua fonte canônica; Honcho é auxiliar de recall/contexto.
- Shopify/pedido/cliente/webhook em Honcho = pista operacional, não fato pessoal do Lucas.

## Status

Packet criado localmente. Nenhuma deleção/alteração externa executada.
