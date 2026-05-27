# Receipt — correção relatório Hermes 02h30 para Telegram + explicação

Data: 2026-05-26  
Área: Operações Hermes / Cron  
Status: corrigido

## Pedido limpo
Lucas pediu para corrigir o relatório das 02h30 porque quer que o Hermes explique o que foi feito e pense em como melhorar, não apenas diga que o ciclo está saudável.

## Ações executadas

1. Backup do registry de cron criado:
   - `/opt/data/cron/jobs.json.bak-20260526-0230-report-deliver-origin-prompt-v2`

2. Cron corrigido:
   - `Relatório Hermes diário 23h + 02h para Lucas`
   - Schedule mantido: `30 5 * * *` = 02h30 BRT
   - Delivery alterado de `local` para `origin`
   - Próxima execução: 2026-05-27 02h30 BRT

3. Prompt do relatório melhorado para exigir:
   - seção **O que foi feito** com verbos concretos;
   - separação entre rotina saudável e mudança real;
   - explicação do efeito prático para Lucas;
   - seção **Como melhorar amanhã** com 1–2 melhorias seguras;
   - mensagem final limpa, sem job_id, wrapper, prompt interno, JSON ou logs brutos.

4. Preferência durável salva na memória do usuário:
   - relatórios devem explicar o que foi feito e como melhorar, não só status.

## Verificação
Listagem viva do cron confirmou:

- job ativo;
- `Deliver: origin`;
- schedule preservado;
- skills preservadas;
- workdir preservado;
- última execução anterior continuou `ok`.

## O que não foi feito

- Não rodei o cron manualmente agora.
- Não alterei Docker, gateway ou scheduler.
- Não alterei os crons de origem 23h/02h.
- Não criei novo cron.
- Não enviei contato externo.

## Rollback
Voltar somente o delivery para `local` e, se necessário, restaurar o backup do registry.
