# Mordomo — Tidio sem webhook: alternativa por Gmail

Atualizado: 2026-05-18

Lucas confirmou que o plano do Tidio não permite webhook. Portanto, a integração direta por webhook fica fora do caminho crítico.

## Decisão

Usar os e-mails do Tidio recebidos em `lucas@zippergaleria.com.br` como fonte de ingestão.

## Como funciona

1. Gmail recebe assunto do tipo `Tidio [1 nova mensagem] #...`.
2. Zipper Gmail draft engine lê a thread.
3. Se for ruído/candidato cru: silencia.
4. Se houver lead real com nome/e-mail/WhatsApp/artista: extrai dados.
5. Se for seguro: cria draft de resposta no Gmail ou prepara registro/follow-up.
6. Se faltarem dados ou houver preço/disponibilidade/negociação: pergunta a Lucas.

## Limitações

- Não vê conversa em tempo real dentro do painel Tidio.
- Depende do conteúdo que o Tidio envia por e-mail.
- Pode haver perda de mensagens se o e-mail do Tidio for pouco informativo.

## Próximo refinamento

Criar parser específico para assuntos `Tidio [1 nova mensagem] #...`, extraindo:

- hash/ID da conversa;
- nome/e-mail/telefone quando visível;
- artista de interesse;
- origem `Site - Tidio`;
- status `new_lead`, `needs_info`, `noise` ou `draft_created`.

Sem webhook, esta é a alternativa mais pragmática e segura.
