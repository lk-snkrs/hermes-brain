# Bruno Okamoto — Hermes 7 passos: resumo operacional para Lucas/Hermes

Data: 2026-06-04
Vídeo: `mU06NTyBsS8` — “7 passos obrigatórios para usar o Hermes e criar agentes que trabalham por você (guia completo)”
Fonte: transcript local obtido via TranscriptAPI. Nenhum segredo registrado.

## Tese executiva

Hermes não deve ser tratado como chatbot. O valor real aparece quando Hermes vira infraestrutura operacional: agentes com contexto, Brain, skills, tools, rotinas, permissões e governança.

A mensagem central para Lucas/Hermes/LK: **um agente útil e bem governado vale mais que vários agentes soltos**.

## Capítulos práticos

- `00:00` — Hermes não é chatbot; é camada operacional de agentes.
- `03:10` — Exemplo Dexter: agente de conteúdo operando via Telegram com equipe.
- `05:00` — Inbox + score para priorizar ideias/pautas.
- `08:00` — Agente como sistema de decisão, não apenas coletor de links.
- `10:00` — Autoavaliação e melhoria contínua do agente.
- `11:30` — Estrutura agêntica: skills, memórias e tools.
- `13:30` — Começar lendo, depois revisando, depois automatizando.
- `15:00` — Hermes é infraestrutura open source, não modelo.
- `22:30` — Componentes: modelo, memória, skills, tools, gateway, dashboard, crons e governança.
- `25:00` — Tríade: contexto + skills + rotina.
- `27:00` — Segundo cérebro e permissionamento por área.
- `30:00` — Memória como continuidade operacional.
- `44:00` — Skills = processos repetitivos padronizados.
- `45:50` — Soul/identidade operacional do agente.
- `68:00` — Crons acordam agentes e sustentam rotina.
- `70:00` — Agente de governança audita outros agentes.
- `74:30` — Começar com um agente útil antes de multiplicar.

## Dez aprendizados incorporáveis

1. Hermes é infraestrutura, não chatbot.
2. Começar por leitura/auditoria antes de automação.
3. Contexto é o ativo principal.
4. Brain/segundo cérebro é base de continuidade.
5. Skills transformam repetição em padrão.
6. Memória operacional preserva decisões, fatos e feedbacks, não conversa infinita.
7. Crons dão heartbeat ao agente.
8. Governança é parte do produto.
9. Um agente útil > dez agentes soltos.
10. Ferramenta muda; arquitetura operacional permanece.

## Modelo operacional recomendado

```text
inbox → score/classificação → roteamento → skill → output/receipt → feedback → melhoria do processo
```

Aplicações:

- conteúdo;
- atendimento;
- inteligência de mercado;
- operações comerciais;
- governança de crons/skills/agentes.

## Aplicação concreta para LK

### Agente inicial recomendado

`LK Content Manager`

Missão:

- ler tendências;
- organizar ideias;
- aplicar score;
- sugerir pautas;
- gerar briefs/roteiros/legendas;
- revisar tom de voz;
- criar relatório diário/semanal;
- não publicar sem aprovação no início.

### Duas skills iniciais de alto ROI

#### `lk_idea_scorer`

Entrada: link, print, texto, insight ou transcript.

Saída:

- nota 0–100;
- categoria;
- justificativa;
- urgência;
- formato sugerido;
- próximo passo.

Critérios possíveis:

- potencial de venda;
- fit com público LK;
- timing;
- tendência de busca/social;
- relação com estoque disponível;
- facilidade de produção;
- potencial Reels/TikTok;
- diferenciação competitiva.

#### `lk_content_brief`

Entrada: ideia aprovada.

Saída:

- briefing;
- gancho;
- roteiro;
- legenda;
- CTA;
- variações Instagram/TikTok;
- sugestão visual;
- relação com produtos/coleções LK.

### Rotinas sugeridas — preview, não ativadas

- Diário 08h: radar de tendências e oportunidades.
- Diário 10h: revisar inbox e aplicar score.
- Diário 17h: resumo do produzido, pendências e próximos posts.
- Segunda: calendário editorial da semana.
- Sexta: análise de performance e aprendizados.
- Mensal: revisão de tom, campanhas e oportunidades.

## Guardrails

- Sem publicação externa sem aprovação.
- Sem Shopify/Klaviyo/Meta/GMC writes por padrão.
- Sem credenciais em Brain/skills/chat.
- Agente começa read-only/preview.
- Crons novos exigem cadência, dono, output, silent-OK, kill criteria e aprovação se criarem automação recorrente.

## Próximos passos recomendados

1. Criar PRD curto do `LK Content Manager`.
2. Criar `soul`/identidade operacional do agente.
3. Criar skill `lk_idea_scorer`.
4. Criar skill `lk_content_brief`.
5. Rodar piloto manual com 5 ideias reais da LK.
6. Só depois propor cron/radar recorrente.

## Status

Este documento é aprendizado/planejamento local. Não ativa agente, cron, publicação, campanha, Shopify write ou envio externo.
