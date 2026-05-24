# Hermes — regra global de decisão por etapas e botões — 2026-05-23

Status: aprovado por Lucas via voz.

## Correção de Lucas

Quando qualquer cron, rotina, agente ou sistema do Hermes precisar perguntar “o que fazer” para Lucas, não deve mandar um bloco grande com várias decisões misturadas.

## Regra global aprovada

- Dividir decisões em etapas sequenciais: `1/N`, `2/N`, etc.
- Pedir uma decisão por vez.
- Usar botões no Telegram quando possível.
- Opções padrão:
  - **Fazer**
  - **Não fazer**
  - **Agendar para depois**
  - **Outro / comentar** — Lucas escreve a instrução específica do que deve ser feito.
- Só avançar para a próxima decisão depois da aprovação, rejeição, agendamento ou comentário da etapa atual.
- A regra vale para todos os sistemas Hermes: crons, Mesa COO, Mission Control, rotinas, governança e especialistas — não apenas para o cron da Mesa COO.

## Artefatos atualizados

- Memória de preferência UX do Lucas.
- Skill `lucas-chief-of-staff`: adicionada regra global para decisões de cron/Hermes.
- Skill/reference `mesa/references/telegram-inline-buttons-cron.md`: ampliada de Mesa COO para Hermes/Mesa global.
- `empresa/gestao/hermes-learning-loop.md`: adicionada regra global de decisão por etapas.

## Limite técnico atual

- Em conversa ao vivo no Telegram, o padrão já funciona via `clarify` com botões inline.
- Em respostas finais de cron, botão inline verdadeiro ainda depende da implementação do caminho `cron -> live Telegram adapter -> reply_markup -> callback ib:`.
- Até essa implementação entrar em runtime, crons devem pelo menos respeitar o formato sequencial textual curto.

## Próximo passo técnico recomendado

Executar o plano local já salvo em:

`reports/governance/mesa-coo-cron-inline-buttons-implementation-plan-2026-05-23.md`

Sem restart/deploy/gateway até nova aprovação específica de implantação.
