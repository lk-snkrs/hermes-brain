# Protocolo — registro de decisões aprovadas antes de compactação

Data: 2026-05-20
Origem: correção de Lucas sobre perda de mensagem aprovada de carrinho abandonado após compactações de conversa.
Status: regra operacional ativa.

## Problema

A conversa pode ser compactada durante o dia. A compactação preserva continuidade geral, mas pode perder detalhes exatos que são críticos para execução: texto aprovado, tom aprovado, canal, segmento, limites e próxima ação permitida.

Em contato com cliente/lead/fornecedor/coletor, isso é risco operacional: uma copy aprovada em chat não pode depender só do histórico temporário.

## Regra

Sempre que Lucas aprovar algo que possa virar contato externo, registrar imediatamente em camada durável antes de continuar o fluxo.

Isso vale para:

- carrinho abandonado;
- Klaviyo/CRM/newsletter;
- WhatsApp/e-mail;
- campanha ou sequência;
- abordagem comercial;
- resposta de cliente;
- oferta, condição, exceção, tom ou cadência de envio.

## Registro mínimo obrigatório

```text
Decision ID:
Data/hora:
Empresa/área:
Fluxo/campanha:
Canal:
Segmento/destinatário:
Copy aprovada ou path do artefato:
Tom aprovado:
O que Lucas aprovou exatamente:
Guardrails/limites:
Pode enviar agora? sim/não
Aprovação de envio externo atual? sim/não
Próxima ação permitida:
Status:
Fonte/contexto:
```

## Camada correta

- Decisão compacta/global: memória.
- Regra detalhada: `empresa/gestao/hermes-learning-loop.md` ou rotina específica.
- Fluxo/campanha LK/Zipper/SPITI: arquivo da área da empresa e, quando existir, ledger/Approval Manager.
- Procedimento repetível: skill.
- Pendência futura: backlog/pending da área.

## Regra de retomada após compactação

Antes de continuar um fluxo aprovado anteriormente, consultar o registro durável. Se não existir registro, não presumir que o texto/approval ainda está válido.

Resposta correta nesses casos:

1. reconstruir o preview/copy;
2. dizer que a aprovação anterior não está comprovada em ledger;
3. pedir confirmação antes de qualquer envio externo.

## Anti-padrão

Não dizer: “você aprovou antes na conversa” sem conseguir apontar para um registro durável.

Não enviar, agendar ou ativar contato externo com base apenas em memória resumida/compactada.

## Verificação

Ao terminar uma sessão com aprovações importantes, checar:

- houve copy ou tom aprovado?
- isso pode ser usado externamente?
- o texto exato ou artefato foi salvo?
- existe guardrail de envio?
- o próximo agente/cron/especialista saberá onde consultar?
