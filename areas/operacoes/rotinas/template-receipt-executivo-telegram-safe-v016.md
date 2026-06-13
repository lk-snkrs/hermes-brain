# Template — Receipt executivo Telegram-safe v0.16

Status: template operacional/documental. Usar para conclusões manuais, handoffs e outputs materiais. Não ativa cron, worker, gateway ou delivery.

## Regra principal

Se Lucas pediu a execução agora, entregar o **resultado executivo no Telegram** e salvar o receipt completo no Brain.

Se for rotina saudável, log técnico, receipt detalhado, diagnóstico sem ação ou movimentação interna, manter local/Brain.

## Template curto para Telegram

```md
Feito: [resultado em 1 frase].

Resultado:
- [achado/entrega 1]
- [achado/entrega 2]
- [achado/entrega 3]

Não fiz:
- [ações bloqueadas/não autorizadas]

Verificação:
- [comando/check principal + status]
- [secret scan/Brain Health quando aplicável]

Próximo passo:
- [decisão ou ação recomendada]
```

## Template completo para Brain

Preferência operacional: criar o receipt completo via `/opt/data/scripts/hermes_memory_os_receipt_writer.py` para validar campos mínimos e chamar o hook automaticamente. Se escrever manualmente, executar o hook depois.

```md
# Receipt — [área/tarefa]

Data/hora:
Agente/profile:
Empresa/área:
Pedido original:
Classificação de risco: A0/A1/A2/A3/A4
Escopo autorizado:

## Resultado executivo

- [o que foi entregue]
- [achados principais]
- [decisão/recomendação]

## Artefatos criados/alterados

- `[path]` — [função]

## Fontes/evidências

- [fonte 1]
- [fonte 2]

## O que não foi feito

- [sem cron/runtime/write/etc.]

## Verificação executada

- [comando/check] — [resultado]
- Secret scan: [0 ou detalhes]
- Brain Health: [passou/warn/fail]

## Riscos restantes

- [risco]

## Próximo passo

- [ação/decisão]

## Reminder OS

- Reminder OS loop needed: yes/no
- Reminder OS owner:
- Reminder OS next action:
- Reminder OS review trigger:
- Reminder OS evidence:
```

## Checklist antes de enviar Telegram

- [ ] Lucas pediu esta execução ou precisa decidir algo?
- [ ] A mensagem contém o resultado, não só caminho interno?
- [ ] A mensagem evita wrapper, JSON bruto, job_id, stack trace e logs longos?
- [ ] O receipt completo ficou no Brain?
- [ ] O receipt novo foi criado pelo wrapper v1.5 ou teve hook Memory OS executado?
- [ ] Se há próximo passo aberto, existe campo Reminder OS ou loop criado/encaminhado?
- [ ] OK rotineiro ficou silencioso?
