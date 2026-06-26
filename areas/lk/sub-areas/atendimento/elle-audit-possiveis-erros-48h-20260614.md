# Elle audit — possíveis erros de resposta últimas 48h — 2026-06-14

Escopo: leitura read-only de `/opt/elle-chatwoot/logs/events.jsonl` e Chatwoot Rails/DB para mensagens da conta LK nas últimas 48h.

Resumo observado:
- 62 eventos `processed` pela Elle.
- Categorias: `human_handoff` 35, `institutional` 15, `greeting` 9, `stock_handoff` 2, `product_clear` 1.
- 20 ocorrências sinalizadas por heurística como possíveis erros ou respostas subótimas.

Grupos principais:
1. Produto/coleção/Track123 “gostaria de saber mais” recebeu resposta de originalidade sem o cliente perguntar. Exemplos: home LK, NB 9060, Nike Moon Shoe, Maison Mihara, Nike x Jacquemus, Onitsuka, Track order status. Correção já aplicada em 2026-06-14 para próximos eventos; monitorar.
2. Site/guia de tamanhos/endereço de pedido recebeu resposta genérica “Temos sim. Nosso site é...”. Exemplos: guia de tamanhos Onitsuka que não abre; cliente recém-comprou e queria editar bloco/apartamento. Requer correção adicional.
3. Handoff sensível sem acolhimento público. Exemplos: cancelar pedido por atraso, pedido parcialmente entregue/ausente, estorno/reclamação, WhatsApp “não funciona”. Já houve melhoria parcial para reclamação sensível; monitorar e ajustar se necessário.
4. Perguntas institucionais simples caíram em human_handoff sem resposta. Ex.: “vcs fazem trocas ou apenas vendem produtos da pop mart?”. Requer decisão de política/resposta.
5. Perguntas de horário pós-greeting nem sempre respondidas pela Elle por lock/contexto. Ex.: cliente perguntou “fecha que horas?” depois de resposta errada de originalidade; humano respondeu depois.
6. Nova situação observada pós-correção: Lululemon/masculino/loja física. Elle respondeu com handoff de loja física; seguro por envolver loja física/pronta entrega, mas pode ser comercialmente seco. Recomendação: rule split para responder catálogo/linha geral sem prometer disponibilidade e só handoff para loja física/retirada/pronta entrega.

Não alterar produção sem aprovação escopada de Lucas.
