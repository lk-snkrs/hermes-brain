# Email intake — needs-attention

- Data UTC: 2026-06-22T12:07:43Z
- Conta: lucas@zippergaleria.com.br
- Message ID Gmail: 19eef3795d2c0c46
- Thread ID: 19eef3795d2c0c46
- Remetente: HubSpot <noreply@notifications.hubspot.com>
- Assunto: Nova conversa não atribuída E-mail
- Classificação: erro operacional recorrente de automação / needs-attention
- Ação executada: marcado como needs-attention via zipper_gmail_draft_helper.py
- Draft criado: não

## O que é

Notificação HubSpot de conversa não atribuída gerada por alerta do Zapier. O alerta informa falha no Zap `TAG MAILERLITE GMAIL > MAILERLITE`.

Erro reportado: MailerLite API retornou que o campo de e-mail precisa ser um endereço válido.

## Por que importa

Pode afetar automação de tag/cadastro MailerLite a partir de Gmail e deixar contatos sem processamento correto. Há registro anterior do mesmo padrão em 2026-06-19, então parece recorrente.

## Dono provável

Responsável pela automação Zapier/MailerLite/HubSpot. Se Lucas não for dono, encaminhar internamente para quem mantém a automação.

## Próxima ação sugerida

Abrir o run details do Zapier, identificar qual registro trouxe e-mail inválido, corrigir/filtrar o campo de e-mail no Zap e reprocessar se necessário.

## Bloqueio / dado faltante

Precisa acessar o detalhe do Zap run no Zapier/HubSpot para ver qual e-mail inválido causou a falha. Não foi feito write externo nem envio de e-mail.

## Itens filtrados sem alerta

- 19eef3087622fd9f — Omie / Resumo Executivo de Finanças: ignorado como financeiro interno geral conforme regra operacional atual.
