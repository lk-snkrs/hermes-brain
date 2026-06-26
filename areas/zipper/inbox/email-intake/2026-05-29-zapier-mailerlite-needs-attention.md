# Zipper email intake — needs-attention

- Data/hora da triagem: 2026-05-29T12:17:41+0000
- Conta: lucas@zippergaleria.com.br
- Message ID: 19e739eb914becd3
- Thread ID: 19e739eb914becd3
- Remetente: HubSpot <noreply@notifications.hubspot.com>
- Assunto: Nova conversa de E-mail desatribuída de Zapier Alerts
- Classificação: bloqueio operacional / integração Zapier-MailerLite

## O que aconteceu

Notificação do HubSpot/Zapier informando erro no Zap `TAG MAILERLITE GMAIL > MAILERLITE`.

Erro reportado: `MailerLite API returned an error: The email field must be a valid email address.`

## Por que importa

A automação que parece levar contatos vindos do Gmail para MailerLite pode estar falhando quando o campo de e-mail vem inválido. Isso pode impedir cadastro/segmentação de lead ou contato, dependendo do run específico.

## Ação tomada

Marcado como `needs-attention` no helper local. Nenhum e-mail enviado. Nenhum rascunho criado.

## Próxima ação recomendada

Responsável operacional deve abrir o run do Zapier, identificar qual registro trouxe e-mail inválido, corrigir o mapeamento/validação do campo e, se for lead real da Zipper, garantir que o contato foi registrado no destino correto.

## Bloqueio/dado faltante

Falta acesso ao detalhe do Zap run para saber qual contato/lead falhou e se há impacto comercial concreto.
