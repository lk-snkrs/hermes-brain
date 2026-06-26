# Auditoria — Telegram noise / receipts / handoffs Hermes v0.16

Data: 2026-06-06
Card: `t_e5273358` — `[R1] Auditoria de noise/receipts para Telegram`
Status: execução local/documental aprovada por Lucas; nenhuma alteração de cron, gateway, delivery ou runtime feita
Owner: Hermes Geral / Operações Hermes

## Tese

Telegram do Lucas deve funcionar como canal executivo, não como log técnico. O padrão correto é:

- **silent-OK** para rotinas saudáveis;
- Telegram somente para decisão, exceção, falha, risco, ação requerida ou resumo explicitamente desejado;
- receipts completos ficam no Brain;
- handoffs carregam evidência, mas não inundam o chat.

## Matriz de entrega

### Deve ir para Telegram

- Decisão A3/A4 necessária.
- Falha atual e ainda não recuperada.
- Anomalia acionável com gatilho claro e ação recomendada.
- Risco de perda de dados, segurança, cliente, dinheiro ou produção.
- Resumo executivo que Lucas explicitamente quer receber.
- Pedido de escolha entre opções com impacto real.

Formato recomendado:

- 1 frase de gatilho.
- 1 bloco curto: impacto.
- 1 bloco curto: ação sugerida.
- Botões/opções claras quando suportado.
- Sem `job_id`, JSON bruto, wrapper, stack trace ou path interno desnecessário.

### Deve ficar só no Brain/local

- Execução OK de rotina recorrente.
- Receipt detalhado de tarefa concluída.
- Logs completos.
- Diagnósticos sem anomalia atual.
- Resultados intermediários de Kanban.
- Comentários técnicos de card.
- Artefatos de verificação sem decisão pendente.

### Deve ser suprimido

- Fallback benigno já recuperado.
- Alerta histórico que não é atual.
- Repetição de alerta já enviado sem mudança de estado.
- Aviso de latência isolada quando a próxima resposta já foi saudável.
- Mensagem técnica que não permite ação por Lucas.

## Padrão de receipt

Todo receipt deve responder:

- pedido original;
- escopo autorizado;
- artefatos criados/alterados;
- o que não foi feito;
- verificação executada;
- riscos restantes;
- próximo passo.

Local preferencial:

- `receipts/` para recibos finais;
- `reports/governance/` para auditorias e packets;
- área específica do Brain para rotinas de domínio.

## Padrão de handoff

Um handoff entre agentes/perfis deve conter:

- owner lógico;
- destino sugerido;
- risco A0-A4;
- fonte da verdade;
- escopo permitido;
- ações bloqueadas;
- evidência e receipt paths;
- critério de done;
- critério de kill/rollback.

O handoff **não** deve executar automaticamente nada. Ele só habilita execução se o destino já tiver escopo aprovado e tool/runtime correto.

## Aplicação ao board `hermes-operating-layer-v016`

- Movimentação de card: não enviar Telegram.
- Card Done: escrever receipt no Brain.
- Card bloqueado por decisão: enviar Telegram apenas com opções humanas.
- Card com erro de execução: enviar Telegram se erro for atual, acionável e não recuperado.
- Pilotos com workers: exigir approval packet separado antes de assignee/dispatch.

## Checklist de higiene para crons/rotinas futuras

Antes de permitir entrega Telegram:

1. A saída é uma decisão/exceção/falha atual?
2. Lucas consegue agir com base na mensagem?
3. A mensagem explica gatilho e ação?
4. A mensagem omite wrapper, JSON bruto e logs longos?
5. Existe receipt completo no Brain?
6. OK saudável fica silencioso?

Se qualquer resposta crítica for “não”, usar `deliver=local` ou ajustar o script para stdout vazio em OK.

## Recomendações

1. Usar este documento como referência para novos receipts/handoffs do Operating Layer v0.16.
2. Só mudar delivery de cron existente com approval separado e lista nominal dos jobs.
3. Para Kanban, manter Telegram como canal de decisão, não de status de card.
4. Adotar um template único de receipt curto + artifact path em toda conclusão manual.

## Resultado

Card `t_e5273358` pode ser considerado concluído no escopo aprovado: matriz documental criada, sem runtime/delivery change.
