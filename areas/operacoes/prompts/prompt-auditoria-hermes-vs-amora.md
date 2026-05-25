# Prompt — auditoria Hermes vs Amora/Bruno

Data: 2026-05-25  
Uso: pedir uma auditoria comparativa do Hermes/COO contra o modelo Amora/Bruno, com notas por área e plano de melhoria.

## Prompt melhorado

Faça uma auditoria crítica do Hermes como COO/orquestrador e compare com a Amora do Bruno/OpenClaw.

Quero uma análise prática, não elogiosa. Use evidências do Brain, skills, rotinas, crons, handoffs, receipts e comportamento real observado. Separe claramente o que está documentado, o que está funcionando no runtime e o que ainda é só intenção/arquitetura.

Divida por áreas:

1. Identidade e papel do agente
2. Arquitetura do Brain e fonte de verdade
3. Task Router e separação por especialistas
4. Handoffs, receipts e continuidade após compactação
5. Proatividade, heartbeats e rotinas recorrentes
6. UX no Telegram/Mesa COO
7. Governança de risco e aprovações
8. Skills e aprendizado operacional
9. Observabilidade, testes e saúde do sistema
10. Maturidade prática em comparação com a Amora

Para cada área, entregue:

- Nota de 0 a 10
- O que está bom
- O que falta
- Evidências usadas
- Risco se não corrigir
- Melhorias recomendadas

No final, dê:

- Nota geral do Hermes hoje
- Nota estimada da Amora como benchmark
- Principais diferenças entre os dois
- Top 5 melhorias por prioridade
- O que não devemos copiar da Amora
- O que devemos adaptar imediatamente
- Próxima ação concreta, com escopo seguro e sem mexer em produção

Regras:

- Não invente capacidade que não foi verificada.
- Diferencie documentação, rotina viva e runtime real.
- Não proponha criar cron, bot, gateway ou write externo sem approval packet.
- Se encontrar gap documental seguro, corrija localmente e registre o handoff.
- Se encontrar gap de runtime/infra, prepare preview, evidência, risco e rollback, mas não execute sem aprovação.
- Responda em português, direto, com notas e recomendações acionáveis.
