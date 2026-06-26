# Mesa COO — preferência por botões inline — 2026-05-23

Status: registrado.

Lucas pediu que as decisões da Mesa COO usem botões inline quando possível, em vez de exigir leitura/resposta textual longa.

## Preferência operacional

- Fluxo: uma decisão por vez (`1/N`).
- Opções: **Fazer**, **Não fazer**, **Agendar para depois**.
- Em conversa ao vivo, usar o tool `clarify` quando disponível, pois no Telegram ele renderiza inline keyboard buttons.
- Em cron autônomo, se `clarify` não estiver disponível/adequado, manter opções textuais curtas até existir suporte de delivery com `reply_markup` em cron.

## Correções aplicadas

- Memória UX de Lucas atualizada para mencionar botões.
- Skill `mesa` atualizada para preferir `clarify`/botões inline em conversa ao vivo.

## Limite técnico atual

O Hermes Telegram renderiza botões inline quando o agente chama `clarify`. A entrega final de cron (`Cronjob Response`) é texto entregue pelo scheduler; transformar essa resposta final em botões inline persistentes pode exigir suporte explícito de `reply_markup` no caminho de delivery do cron/gateway.
