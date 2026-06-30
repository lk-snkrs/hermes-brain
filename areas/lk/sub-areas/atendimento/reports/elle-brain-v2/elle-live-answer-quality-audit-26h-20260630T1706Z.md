# Elle — auditoria de respostas e visibilidade humana (26h)

Data: 2026-06-30 17:06 UTC  
Janela: últimas 26h a partir do log vivo `/var/log/elle/events.jsonl` no container `elle-chatwoot`.  
Escopo: leitura read-only de runtime/Chatwoot, health, logs, mensagens sanitizadas e gates locais. Nenhum envio, nenhuma alteração Chatwoot, nenhuma alteração Docker/runtime. `values_printed=false`.

## Veredito curto

**Não está 100%.** A Elle está funcionando e vários guardrails funcionaram, mas nas últimas 26h houve **5 avaliações `bad`**, sendo **4 de risco alto**. O processo de autoavaliação/autocorreção **funcionou**: avaliou, segurou expansão de autonomia, aplicou correções/guardrails no runtime de produção e gerou sugestões/drafts supervisionados. Observação de terminologia: `auto_apply=false` significa que ela não autoeditou código/política sem aprovação; não significa que deixou de autocorrigir a produção via guardrails/runtime.

Sobre a visibilidade da Larissa/Giselia: **o diagnóstico aponta causa provável de configuração/fluxo Chatwoot**. Enquanto a Elle conversa sem handoff, várias conversas ficam `pending`, sem `assignee` e sem `team`; só aparecem para Giselia/Larissa quando a Elle faz handoff e abre/atribui. O código já tem `CHATWOOT_TEAM_ID`, mas a função ativa só atribui assignee no handoff; não atribui team durante a conversa da Elle.

## Evidência operacional

Health público da Elle:

- `ok=true`
- `write_enabled=true`
- `kill_switch=false`
- `public_reply_enabled=true`
- `hmac_secret_present=true`
- `legacy_path_webhook_enabled=false`
- `ai_enabled=true`
- `ai_provider=openrouter`
- `elle_brain_v2_canary_percent=100`
- `catalog_stock_included=false`

Contadores 26h:

| Métrica | Valor |
|---|---:|
| events_total | 1930 |
| conversations com evento | 160 |
| processed | 38 |
| response_evaluated | 38 |
| v2_canary_used / skipped / error | 9 / 29 / 0 |
| provider_error | 0 |
| eval_good / eval_ok / eval_bad | 24 / 9 / 5 |
| eval_risk_high / low / none | 4 / 3 / 31 |
| stock_handoff | 2 |
| human_handoff | 21 |
| product_clear | 10 |
| handoff_violations | 0 |

Autonomy gate 26h:

- `status=hold`
- `recommendation=do_not_expand_autonomy`
- `eval_bad=5`
- `eval_medium_high=4`
- `customer_send_executed=false`
- `writes_external=0`

Autofix supervisionado:

- `status=ok`
- `auto_apply=false`
- `evaluations_seen=19`
- `patch_suggestions_added=6`
- `patch_suggestions_total=19`
- `regression_drafts_added=6`
- `regression_drafts_total=19`
- `writes_external=0`

Regressão Elle Brain v2:

- `ok=true`, `tests=44`, `values_printed=false`.

OpenRouter 1h:

- `OK`, `processed=3`, `provider_errors=0`, `v2_errors=0`.

## Casos materiais auditados

| Conversa | Sinal | O que ocorreu | Leitura |
|---:|---|---|---|
| 2448 | `bad/high` por disponibilidade e desconto | Cliente pediu cupom/primeira compra; Elle respondeu com copy fora de contexto sobre Kill Bill/Onitsuka e depois cupom `ELLE5`. Giselia depois respondeu com cupom `PRIMEIRACOMPRA`. | Erro material: contexto/produto driftou e desconto/cupom não deveria ser prometido sem regra verificada. |
| 1673 | `bad/high` `possible_availability_promise` | Cliente pediu previsão de entrega do pedido #147140; Elle falou que Larissa precisa confirmar pronta entrega/encomenda e transferiu. | A decisão de handoff foi correta, mas a copy ficou frágil por reabrir discussão de pronta entrega/encomenda sem consultar fonte viva; para pós-venda com pedido, melhor internal note + handoff objetivo. |
| 2451 | `bad/low` contexto + `bad/high` disponibilidade | Cliente pediu produto/“falar com Larissa”; Elle fez respostas iniciais de produto/transferência, depois Giselia assumiu e respondeu disponibilidade. | Elle acabou transbordando, mas houve perda de contexto/duplicidade antes do handoff. |
| 1458 | disponibilidade Alo 43 | Elle respondeu link de coleção Alo como `product_clear`, depois quando cliente perguntou “tamanho 43 tem?” fez handoff privado sem resposta pública. | Parcial: o segundo passo foi seguro; o primeiro deveria ter tratado “chegou tênis Alo tamanho 43?” como estoque desde o início. |
| 2454 | estoque tamanho 36 | Elle classificou como `stock_handoff`, abriu/atribuiu e não prometeu disponibilidade. | Correto no guardrail; copy pode ser melhor porque pediu modelo/numeração mesmo o cliente já tendo enviado link + tamanho. |
| 2457 | pronta entrega em pedido/encomenda | Elle classificou como `stock_handoff` e transferiu; não prometeu pronta entrega. | Correto em segurança, mas copy genérica demais para pedido já identificado. |
| 2439 | medidas de camisa | Elle respondeu “vou verificar medidas… um momento” e deixou conversa `pending`, sem assignee/team. | Risco de visibilidade/abandono: quando não há handoff, humano pode não ver pelo filtro operacional. |

## Autoavaliação/autocorreção

- **Autoavaliou:** sim. Todas as 38 respostas processadas tiveram `response_evaluated`.
- **Autocorrigiu produção sozinha:** sim. A Elle corrigiu/segurou comportamento em produção por guardrails/runtime e não expandiu autonomia quando detectou risco.
- **Autoedição de código/política sem aprovação:** não. `auto_apply=false`, `writes_external=0`; isso é o freio correto para não alterar código/política sozinha.
- **Gatilho de segurança:** funcionou; `autonomy_gate=hold` impediu expansão apesar de health OK.

## Diagnóstico da visibilidade Larissa/Giselia

Evidência de Chatwoot:

- Conversas de handoff geralmente aparecem com `assignee=Giselia` e labels `humano/larissa`, porque `open_and_assign_handoff()` faz `PATCH status=open` e `POST assignments {assignee_id}`.
- Conversas que a Elle responde como não-handoff podem ficar `pending`, `assignee=None`, `team=None`, exemplo conv 2439.
- A equipe `atendimento whatsapp` existe (`team_id=2`, `allow_auto_assign=false`), e o env `CHATWOOT_TEAM_ID` está presente no container.
- O código ativo `/app/app.py` lê `CHATWOOT_TEAM_ID`, mas a função `open_and_assign_handoff()` usa somente `assignee_id`; não há assignment de `team_id` no caminho normal.
- Chatwoot suporta `POST /api/v1/accounts/:account_id/conversations/:conversation_id/assignments` com `{team_id: ...}`.

Conclusão: **conseguimos corrigir**, mas é write em produção/runtime. O fix recomendado é atribuir as conversas da Elle à equipe de atendimento WhatsApp para visibilidade operacional sem atribuir humano antes do handoff, preservando o bot em `pending`.

## Fix recomendado — precisa aprovação escopada

Objetivo: Larissa/Giselia conseguirem ver conversas enquanto Elle está conversando, sem fazer Elle parar por `assignee_id` humano.

Mudança proposta:

1. Adicionar função `assign_visibility_team(conversation_id)` que chama Chatwoot assignments com `{team_id: CHATWOOT_TEAM_ID}` quando a conversa ainda não tem team.
2. Chamar essa função no caminho de resposta pública da Elle e/ou ao processar incoming, **sem** mudar `status` para `open` e **sem** setar `assignee_id` humano.
3. Manter handoff atual: quando precisa Larissa, aí sim `status=open`, `assignee=Giselia`, private note e labels.
4. Verificar com smoke interno: nova conversa/teste controlado fica `pending + team=atendimento whatsapp + assignee=None` durante bot; após handoff fica `open + assignee=Giselia`.
5. Rollback: remover chamada de `assign_visibility_team` e recriar container com imagem/backup anterior.

Aprovação necessária: alterar código/runtime Elle + chamadas write Chatwoot de team assignment + rebuild/recreate/verificação. Sem essa aprovação, eu parei no diagnóstico e packet.

## Recomendações de qualidade

1. Corrigir cupom/desconto: Elle não deve prometer cupom específico se a regra atual não estiver validada em fonte oficial.
2. Reforçar estoque: “chegou X tamanho Y?”, “tem 43?”, “pronta entrega?” = `stock_handoff` imediato, mesmo quando houver link/coleção/produto.
3. Pós-venda com pedido identificado: evitar copy genérica de pronta entrega/encomenda; usar handoff objetivo para Larissa com internal note.
4. Medidas/características de produto: se não houver dado seguro na página/catálogo, pedir verificação humana; não prometer “vou verificar” se não há mecanismo de follow-up automático.
5. Melhorar copy de stock_handoff para não pedir modelo/tamanho quando já foram enviados.

## Status

- Auditoria: concluída read-only.
- Correção de visibilidade: diagnosticada e especificada; aguardando aprovação escopada para execução em produção.
- Secrets/tokens: não impressos. `values_printed=false`.
