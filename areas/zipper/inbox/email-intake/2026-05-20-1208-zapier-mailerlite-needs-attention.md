# Zipper inbox intake — needs-attention

- Data: 2026-05-20T12:08:20+00:00
- Conta monitorada: lucas@zippergaleria.com.br
- Contexto: Zipper OS / e-mail intake draft-only
- Gmail message_id: 19e45454d28ffb69
- Thread ID: 19e45454d28ffb69
- Remetente: HubSpot <noreply@notifications.hubspot.com>
- Assunto: Nova conversa de E-mail desatribuída de Zapier Alerts
- Classificação: erro operacional / needs-attention
- Ação executada: marcado como needs-attention via zipper_gmail_draft_helper.py

## O que é

Notificação de erro do Zapier para o fluxo `TAG MAILERLITE GMAIL > MAILERLITE`.

## Por que importa

O Zapier informa que a API do MailerLite rejeitou o campo de e-mail por não ser um endereço válido. Isso pode impedir que um contato/lead entre corretamente no mailing/CRM de comunicação.

## Dono provável

Operação/automação Zipper, provavelmente Lucas ou quem administra Zapier/MailerLite.

## Próxima ação recomendada

Abrir o detalhe da execução no Zapier, identificar o registro com e-mail inválido e corrigir o mapeamento/validação do campo antes do envio ao MailerLite.

## Bloqueio/dado faltante

O e-mail recebido não mostra qual contato causou o erro, apenas o resumo da falha. É preciso acessar o detalhe do Zap run.
