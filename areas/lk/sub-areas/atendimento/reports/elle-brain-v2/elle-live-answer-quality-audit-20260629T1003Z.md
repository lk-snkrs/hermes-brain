# Elle — auditoria rápida de respostas ao cliente

Data: 2026-06-29 10:03 UTC
Escopo: leitura read-only de runtime/container, `/var/log/elle/events.jsonl`, Chatwoot read-only via runtime Elle e supervised learning local. `values_printed=false`; nenhum secret impresso; nenhum write externo executado.

## Veredito

Não está 100%: a Elle está ativa e a maioria das respostas auditadas ficou segura, mas houve 1 caso `bad/high` nas últimas 24h com risco de promessa/consulta de disponibilidade e confusão de produto/contexto.

## Evidência operacional

- Container `elle-chatwoot`: up.
- Health interno: `ok=true`, `write_enabled=true`, `public_reply_enabled=true`, `hmac_secret_present=true`, `legacy_path_webhook_enabled=false`, `ai_provider=openrouter`, `elle_brain_v2_canary_percent=100`, `catalog_stock_included=false`.
- Janela 24h no log vivo `/var/log/elle/events.jsonl`:
  - events_total: 573
  - conversations: 45
  - processed: 13
  - ai_decision: 28
  - v2_canary_used: 6
  - v2_canary_skipped: 7
  - response_evaluated: 13
  - eval_bad: 1
  - eval_medium_high: 1
  - handoff_violations: 0
- Autonomy gate 24h: `hold`; recommendation: `do_not_expand_autonomy`; `customer_send_executed=false`; `writes_external=0`.

## Principais casos

| Conversa | Avaliação | O que aconteceu | Leitura operacional |
|---|---:|---|---|
| 2420 / msg 58818 | bad/high | Cliente perguntou “E se por acaso tem esse!?”; Elle respondeu como `product_clear`, repetiu abertura, respondeu autenticidade e ainda citou produto errado (Moletom Slyce) em contexto de Adidas Handball Spezial. | Erro material: deveria tratar como disponibilidade/identificação incerta e transbordar para Larissa/lk-stock sem prometer nem tentar confirmar. |
| 2416 / Crocs McQueen LED | ok com correção posterior | Primeiro respondeu genericamente que alguns modelos têm LED e pediu link/foto mesmo já tendo contexto; depois, quando o cliente disse “Esse do Mcqueen”, corrigiu para “a página não especifica”. | Parcial: a resposta final foi melhor, mas a primeira foi genérica demais e poderia induzir confirmação. |
| 2418 / Nike Air Rift numeração | good | Primeiro abriu com ajuda e citou tamanhos disponíveis; depois cliente perguntou numeração e Elle fez handoff sem resposta pública. | Seguro no handoff; melhoria: evitar oferecer “tamanhos disponíveis” antes de validação de estoque/grade. |
| 2424 / loja física | good | Cliente perguntou onde fica a loja; Elle respondeu com transbordo para Larissa e horário. | Seguro, mas UX pode ser mais objetiva: separar pergunta institucional de disponibilidade/reserva. |

## Auto-correção / aprendizado

- A Elle tem avaliação pós-resposta e loop supervisionado ativo.
- Ela registrou avaliações/candidatos locais, mas `auto_apply=false`: não altera política/código sozinha.
- Último erro high-risk entrou como `response_evaluated` com `possible_availability_promise`; ainda não há evidência de patch automático aplicado para esse caso.
- Portanto: houve auto-avaliação e alguns guardrails funcionaram, mas não houve auto-correção completa do erro sem revisão/gate.

## Melhorias recomendadas

1. Reforçar regra de “tem esse?” / “tem disponível?” / “tem na loja?” como `stock_handoff` mesmo quando há link/produto no contexto.
2. Bloquear resposta genérica sobre feature de produto quando a página não confirma; padrão: “não tenho confirmação segura pela página; vou chamar Larissa/atendimento para verificar”.
3. Evitar oferecer “tamanhos disponíveis” em abertura de produto; trocar por “posso te ajudar com detalhes do modelo, formas de pagamento ou encaminhar para confirmação de tamanho/disponibilidade”.
4. Melhorar dedupe/contexto para não enviar múltiplas respostas públicas no mesmo turno e não trocar o produto citado.
5. Separar intent de endereço/loja institucional de intent de estoque/pronta entrega/reserva, mantendo handoff apenas quando houver promessa operacional.
