# Elle — auditoria da madrugada 2026-06-15

Janela: 2026-06-15 00:00–06:46 BRT.
Fonte: Chatwoot API read-only, inbox LK WhatsApp (`inbox_id=2`).
Valores/segredos: não impressos (`values_printed=false`).

## Resumo

- Conversas com mensagem de cliente na madrugada: 2.
- Respostas públicas da Elle observadas: 3.
- Conversas sem resposta da Elle quando deveria responder: 0 observadas.
- Respostas com problema de qualidade/guardrail: 2 pontos.

## Conversa 1 — coleção/site

Cliente enviou mensagem automática de navegação em coleção: “Sneakers: tênis adidas, nike e mais” e pediu para saber mais.

Resposta da Elle observada:

> Sim, você consegue seguir pelo site: selecione a numeração na página do produto e finalize a compra por lá. Se quiser, me envie o link ou nome do modelo que eu te ajudo.

Avaliação: parcialmente incorreta.

Motivo: para navegação genérica em coleção, a regra corrigida pelo Lucas era responder de forma aberta e humana, por exemplo: “Olá! Como vai? Aqui é a Elle da LK. Vi que você estava olhando nossa coleção de sneakers. Como posso te ajudar?” A resposta atual pulou direto para checkout/numeração e pediu link/modelo mesmo a própria origem já indicando coleção.

## Conversa 2 — greeting + mensagem indisponível

Cliente cumprimentou (“Oiii”), depois enviou mensagem indisponível e mensagens vazias/possivelmente mídia.

Resposta inicial da Elle observada:

> Olá! Sou a Elle da LK Sneakers. Como posso te ajudar hoje?

Avaliação: correta para greeting, já usando “Olá” e sem emoji.

Depois, a conversa foi atribuída a Giselia e recebeu labels de humano/unclear_request.

Follow-up observado cerca de 1h depois:

> Olá! Passando para saber se consigo te ajudar com alguma dúvida antes de finalizar. Se quiser, é só me chamar por aqui.

Avaliação: potencialmente incorreto.

Motivo: apesar da copy estar correta, a conversa já estava em handoff/humano/unclear_request e atribuída a Giselia. O worker de follow-up deveria respeitar esse estado e não enviar follow-up automático em conversa já assumida/roteada para humano.

## Diagnóstico

A noite foi tranquila em volume, mas revelou dois ajustes necessários:

1. Corrigir a resposta de entrada para coleção/site genérica: não transformar em checkout/numeração quando o cliente só pediu “saber mais”.
2. Bloquear follow-up automático quando a conversa tiver label `humano`, label `unclear_request` ou assignee humano ativo.

## Próximo passo recomendado

Pedir aprovação do Lucas para correção de produção com backup, patch, rebuild, health check e dry-run do follow-up.
