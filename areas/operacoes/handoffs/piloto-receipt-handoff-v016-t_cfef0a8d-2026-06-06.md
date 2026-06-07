# Piloto documental — Receipt/Handoff v0.16 entre agentes

Data: 2026-06-06T16:54:03Z
Board: `hermes-operating-layer-v016`
Card: `t_cfef0a8d` — `[R1] Pilotar receipt/handoff padrão entre agentes`
Executor: Hermes Geral / default, execução manual local
Status: piloto documental concluído; não houve worker, dispatch, cron, Telegram delivery ou write externo

## Objetivo do piloto

Validar, em baixa fricção, que o protocolo v0.16 de receipts/handoff cria um rastro operacional útil entre Hermes Geral e perfis especialistas sem gerar ruído no Telegram nem disparar execução automática.

Protocolo usado como fonte:

- `areas/operacoes/rotinas/protocolo-receipts-handoff-v016-operating-layer.md`

## Cenário simulado

Cenário documental escolhido:

- Hermes Geral recebe uma demanda multiempresa ou de maturidade operacional.
- Hermes Geral identifica que o owner final pode ser um especialista, mas o trabalho atual é apenas governança/local.
- Hermes Geral registra o piloto, critérios, fontes e próximo passo no Brain.
- Nenhum especialista é acionado automaticamente.
- Nenhum card é atribuído a worker.

## Classificação

- Risco: A0/A1, local/documental.
- Registro exigido: R1 — receipt simples.
- Handoff real para especialista: não executado neste piloto.
- Handoff simulado/documental: sim, para validar forma e critérios.

## Template validado — R1 mínimo

```md
# Receipt — [área/tarefa]
Data/hora:
Agente/profile:
Empresa/área:
Pedido original:
Classificação de risco: A0/A1/A2/A3/A4
O que foi feito:
Fontes/evidências:
Artefatos gerados:
O que não foi feito:
Próximo passo:
```

## Template validado — Handoff especialista mínimo

```md
# Handoff especialista → Hermes Central
Data/hora:
Agente/profile origem:
Agente/profile destino, se houver:
Empresa/área:
Pedido original:
Playbook usado:
Workers/subagents usados:
Workers pulados e motivo:
Fontes consultadas:
Output/artefato:
Aprovação recebida:
Writes externos:
Riscos/bloqueios:
Onde foi documentado no Brain:
Próximo passo:
```

## Critérios de sucesso do piloto

O piloto é considerado bem-sucedido se:

- o card Kanban mantém rastro claro;
- não há `assignee` nem worker automático;
- não há `dispatch`/run associado ao card;
- o artefato explica o que foi feito e o que não foi feito;
- o receipt/handoff aponta fonte, risco, evidência, artefato e próximo passo;
- Telegram não recebe ruído técnico;
- Brain Health e secret scan passam.

## Resultado do piloto

Padrão aprovado para uso futuro em tarefas locais/documentais:

1. Receber demanda.
2. Classificar risco A0–A4.
3. Identificar owner/profile.
4. Se for local/documental, executar sem worker quando o objetivo for apenas governança.
5. Registrar R1 no Brain.
6. Comentar/completar card Kanban manualmente quando aplicável.
7. Verificar estado vivo do board: sem `running`, sem `assignee`, sem `notify-list`, sem diagnostics.

## O que não foi feito

Não foi feito:

- assignee para profile especialista;
- dispatch;
- worker/subagent;
- cron;
- Telegram delivery;
- alteração de modelo, provider, gateway, Docker, Traefik, Dashboard, OIDC ou secrets;
- write externo.

## Próximo passo recomendado

Para amadurecer sem risco: escolher um próximo card R1 local/documental e repetir o mesmo padrão. Para qualquer R2/R3, exigir approval packet específico antes de runtime/config/infra.
