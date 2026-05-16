HEARTBEAT.md — Workspace da Amora

Este é o HEARTBEAT.md real do workspace da Amora. Use como referência de profundidade — adapte ao SEU contexto.

Configuração do mecanismo de proatividade do agente. Define COMO ele vigia o dia do Bruno. O que ele vigia mora em memory/hot.md (auto-mantido).

Frequência

Poll a cada: 30 minutos

Janela ativa: 08:00 às 22:00

Quiet hours: 22:00 às 08:00 — só interrompe em urgência real

Checks rotacionáveis

Amora sorteia 2-4 destas por heartbeat. Não checa todas juntas — vira ruído.

Inbox triage — emails das últimas 4h, classifica em [urgente/pode esperar/lixo], avisa só urgentes

Pendências paradas — itens em pendencias.md com nome de terceiro parado 3+ dias dispara cobrança

Mention sweep — LinkedIn + Twitter + menções no Discord/Slack, só sinaliza se relevante

Memory maintenance — a cada 3 dias, lê memory/YYYY-MM-DD.md recentes e destila aprendizados pra MEMORY.md

Calendário próximo — coberto pela skill /rotina (cockpit matinal), heartbeat não duplica

Regras de silêncio (anti-spam)

Já checou nos últimos 30min? → HEARTBEAT_OK (silencioso)

Nada novo desde a última checagem? → silêncio (não mandar "tudo certo!" gratuito)

Bruno em call no Granola ou trabalho profundo (Cursor aberto há 30+ min)? → segura mensagem não-urgente

Quiet hours ativas (22h-8h)? → só interrompe se for urgência real

Em grupo (Discord/Slack/WhatsApp Community)? → padrão é HEARTBEAT_OK, só fala se mencionada

Regras de reach out (quando vale interromper)

Email importante chegou (cliente ativo da Pixel, parceiro estratégico, financeiro, fiscal)

Evento começa em <2h e Bruno ainda não confirmou no calendar

Achou algo genuinamente interessante (oportunidade, sinal forte, post viralizando, ameaça)

Faz mais de 8h sem dizer nada e tem coisa relevante acumulada

Pendência de terceiro parou há 3+ dias e pode bloquear projeto ativo

Como o heartbeat consulta contexto

Heartbeat NÃO duplica memória. Lê memory/hot.md (auto-mantido pela skill /salve) pra saber:

Top prioridades da semana

Negociações ativas e próximos passos pendentes

Decisões recentes

Métricas-chave (assinantes Newsletter, alunos PRO, MRR Pixel)

Prazos críticos por data

Se algum prazo de hot.md chega perto e ainda tá pendente, heartbeat avisa antes de virar urgência.

Como adaptar pro seu contexto

Amora roda com 4 checks ativos porque opera em múltiplos canais (Telegram, Discord, Slack, WhatsApp Community), tem 60+ crons rodando, e Bruno tem volume alto.

Pro seu agente novo (PME): Comece com 1 check só por 1 semana inteira. Sério.

```markdown
## Checks rotacionáveis

- [x] **Inbox triage** — emails das últimas 4h, avisa só urgentes

- # [ ] tudo o resto desativado por enquanto


```

Por que 1 check só:

Você precisa sentir o que é "barulho útil" vs "barulho que irrita"

Adicionar 4 checks no dia 1 = agente vira spam = você desliga proatividade inteira

Depois de 1 semana, ativa pendências paradas ou mention sweep

Vai adicionando 1 por vez

Janela ativa típica de PME:

08:00-19:00 (segue horário comercial)

Quiet hours mais largas: 19:00-08:00

Frequência inicial:

60 minutos (não 30) — heartbeat a cada hora dá tempo de "treinar" o que é urgência sem ser bombardeado

Conforme agente acerta o tom, você aperta a frequência (60min → 30min) e adiciona checks. Não tente começar com a config da Amora.

Versão de referência — workspace original da Amora.
