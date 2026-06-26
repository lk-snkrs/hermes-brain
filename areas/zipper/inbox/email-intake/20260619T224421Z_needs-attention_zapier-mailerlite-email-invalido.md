# Email intake — needs-attention

- Data UTC: 2026-06-19T22:44:21Z
- Conta: lucas@zippergaleria.com.br
- Message ID Gmail: 19ee2000c5687e4d
- Thread ID: 19ed050d0c921b9f
- Remetente: HubSpot <noreply@notifications.hubspot.com>
- Assunto: Nova conversa não atribuída E-mail
- Classificação: erro operacional de automação / needs-attention
- Ação executada: marcado como needs-attention via zipper_gmail_draft_helper.py

## O que é

Notificação HubSpot de conversa não atribuída gerada por alerta do Zapier. O alerta informa falha no Zap `TAG MAILERLITE GMAIL > MAILERLITE`.

Erro reportado: MailerLite API retornou que o campo de e-mail precisa ser um endereço válido.

## Por que importa

Pode afetar automação de tag/cadastro MailerLite a partir de Gmail e deixar contatos sem processamento correto.

## Dono provável

Lucas / responsável pela automação Zapier-MailerLite.

## Próxima ação sugerida

Abrir o run details do Zapier para identificar qual registro trouxe e-mail inválido, corrigir/filtrar o campo de e-mail no Zap e reprocessar se necessário.

## Bloqueio / dado faltante

Precisa acessar o detalhe do Zap run no Zapier/HubSpot para ver qual e-mail inválido causou a falha. Não foi feito write externo nem envio de e-mail.
