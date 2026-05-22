# Needs-attention — Zapier/MailerLite com e-mail inválido

- Data do processamento: 2026-05-21T17:08:07Z
- Conta: lucas@zippergaleria.com.br
- Message ID Gmail: `19e4b7a6378b6400`
- Thread ID Gmail: `19e4a6b31f8b04dd`
- Remetente: HubSpot <noreply@notifications.hubspot.com>
- Assunto: Nova conversa de E-mail desatribuída de Zapier Alerts
- Classificação: Zipper / erro operacional de automação
- Ação executada: marcado como `needs-attention`; nenhum e-mail enviado; nenhum draft criado.

## O que é

Notificação do HubSpot informando conversa desatribuída gerada por Zapier Alerts. O alerta original diz que o Zap `TAG MAILERLITE GMAIL > MAILERLITE` recebeu 1 erro.

Erro reportado: `MailerLite API returned an error: The email field must be a valid email address.`

## Por que importa

Pode indicar que alguma automação de captura/tagueamento de contatos do Gmail para MailerLite está recebendo um campo de e-mail quebrado ou vazio. Se esse Zap estiver ligado a leads/newsletter/comunicação da Zipper, contatos válidos podem deixar de ser sincronizados ou tagueados.

## Dono provável

Operacional/técnico: Lucas ou quem mantém Zapier/MailerLite/HubSpot da Zipper.

## Próxima ação recomendada

Abrir o detalhe da execução do Zap no Zapier, identificar qual registro gerou o e-mail inválido e corrigir o mapeamento/filtro antes do passo MailerLite. Se o registro for apenas ruído/sem e-mail, adicionar filtro para não enviar ao MailerLite.

## Bloqueio/dado faltante

Sem acesso ao detalhe do Zap run a partir da notificação. É preciso entrar no Zapier para ver o payload do registro que falhou.

## Prazo sugerido

Baixo/médio: revisar nas próximas 24h se esse Zap alimenta base comercial ou newsletter; caso seja automação crítica de leads, revisar hoje.
