# Zipper e-mail intake — needs attention

- Data: 2026-06-01T14:50:20+00:00
- Conta: lucas@zippergaleria.com.br
- Message ID Gmail: 19e83a1f17dabbad
- Thread ID Gmail: 19e835dbe81f0348
- Origem: HubSpot notification / Zapier Alerts
- Assunto: Nova conversa de E-mail desatribuída de Zapier Alerts
- Classificação: erro operacional de automação
- Ação local executada: marcado como `needs_attention` no estado local do helper

## O que aconteceu

HubSpot notificou uma conversa desatribuída vinda de Zapier Alerts. O corpo indica falha no Zap `TAG MAILERLITE GMAIL > MAILERLITE`: `MailerLite API returned an error: The email field must be a valid email address`.

## Por que importa

Pode haver lead/contato que deveria entrar em MailerLite ou receber tag, mas a automação falhou por e-mail inválido. Não é caso para draft de resposta ao remetente automático.

## Próxima ação recomendada

Revisar o Zap/run no Zapier ou HubSpot, identificar qual registro estava com e-mail inválido, corrigir/suprimir o contato e reprocessar se for lead real.

## Bloqueio

Sem acesso seguro ao detalhe do run do Zapier pelo e-mail sozinho; precisa abrir o run no Zapier/HubSpot ou consultar logs internos da automação.

## Observação

Outro candidato do ciclo, `19e83a14991a98ba`, foi ignorado como financeiro interno/câmbio/pagamento administrativo relacionado a Adriana Duque, conforme regra de não priorizar administrativo geral salvo prazo crítico/reclamação/decisão explícita.
