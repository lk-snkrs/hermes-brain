# Checklist de Revisão — PR Bruno/OpenClaw → Hermes Brain

Use este checklist antes de mergear o PR.

## 1. Regra central

- [ ] O PR deixa claro que Hermes não é OpenClaw.
- [ ] A estrutura do Bruno foi adaptada, não copiada cegamente.
- [ ] Os diferenciais do Hermes foram preservados: Doppler, cronjobs, execução real, Telegram, memória persistente, session_search e ferramentas.

## 2. Segurança

- [ ] Nenhum valor de secret foi adicionado.
- [ ] Só aparecem nomes de secrets, nunca valores.
- [ ] Doppler continua sendo fonte de verdade.
- [ ] Ações externas continuam exigindo aprovação Lucas.

## 3. Compatibilidade com o Brain atual

- [ ] `memories/` foi preservado.
- [ ] Agentes LK/Zipper existentes não foram sobrescritos.
- [ ] A nova estrutura `areas/` complementa o Brain atual.
- [ ] Nenhum script ou cron real foi alterado neste PR.

## 4. Estrutura nova

- [ ] `ARCHITECTURE.md` explica a arquitetura multicamada Hermes.
- [ ] `areas/` cobre LK, Zipper, SPITI, Operações, Governança e Tecnologia.
- [ ] `seguranca/` documenta permissões e ações sensíveis.
- [ ] `empresa/skills/_templates/` tem template de skill de negócio.
- [ ] `empresa/rotinas/_templates/` tem template de rotina.

## 5. Próximos passos pós-merge

- [ ] Decidir se `memories/` continua como resumo global canônico.
- [ ] Enriquecer AGENTS/TOOLS/USER/MEMORY/HEARTBEAT de cada agente.
- [ ] Mapear crons reais atuais para `areas/*/rotinas/`.
- [ ] Criar segunda rodada focada em LK CRM e tráfego pago.
- [ ] Criar terceira rodada focada em Zipper e SPITI.
