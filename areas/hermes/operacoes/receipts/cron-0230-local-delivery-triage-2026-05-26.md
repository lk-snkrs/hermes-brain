# Receipt — triagem cron 02h30 não entregue no Telegram

Data: 2026-05-26  
Área: Operações Hermes / Cron  
Status: diagnosticado

## Pedido limpo
Lucas perguntou por que a mensagem do cron das 02h30 não chegou no Telegram.

## Evidência consultada
Inspeção read-only do registro vivo de crons via CLI Hermes.

Job identificado pelo horário:

- Nome: Relatório Hermes diário 23h + 02h para Lucas
- Schedule: `30 5 * * *` = 02h30 BRT
- Última execução: 2026-05-26 05:32 UTC = 02h32 BRT
- Status: ok
- Deliver: local

Artefato local encontrado:

- `/opt/data/cron/output/98478b820720/2026-05-26_05-32-08.md`

## Diagnóstico
Não foi falha de execução. O cron rodou OK, mas estava configurado para `deliver: local`, então salvou o output localmente em vez de enviar para o Telegram.

## Observação de UX
O output final do relatório estava humano e útil, mas o artefato local também contém cabeçalho/prompt do scheduler. Se for voltar para Telegram, deve ser entregue como mensagem final limpa, não como artefato bruto.

## O que não foi feito

- Não alterei o cron.
- Não mudei schedule.
- Não reiniciei gateway/scheduler.
- Não criei novo cron.
- Não enviei mensagem externa.

## Próximo passo seguro
Se Lucas aprovar, alterar somente `deliver` desse cron de `local` para `origin`, mantendo schedule, prompt, skills e workdir intactos. Rollback: voltar o mesmo campo para `local`.
