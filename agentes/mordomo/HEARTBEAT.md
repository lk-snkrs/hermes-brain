# Mordomo — HEARTBEAT

Status: profile/rotinas parciais existentes; este arquivo não autoriza cron novo nem envio externo.

## Objetivo

Mordomo revisa inbox/follow-ups e lembra Lucas apenas quando houver algo útil, bloqueado ou vencendo.

## Checks sugeridos

- Follow-ups simples conhecidos/verificados que podem ser lembrados.
- Conversas com preço/disponibilidade/reserva/negociação/reclamação/supplier/bulk bloqueadas para aprovação.
- Itens com prazo, agenda ou compromisso claro.
- Mensagens que pertencem a LK, Zipper, SPITI ou Operações e precisam roteamento.
- Falha de rotina viva do Mordomo, quando houver impacto real.

## Política de ruído

Silent-OK: não avisar quando não houver novidade relevante. Não criar digest automático sem decisão de cadência/destino.

Alertar apenas quando houver:

- decisão de Lucas;
- follow-up vencendo ou com janela clara;
- bloqueio por aprovação;
- risco de promessa material sem fonte;
- item que precisa roteamento para especialista.

## Bloqueios permanentes sem aprovação explícita

- preço, disponibilidade, reserva, negociação, reclamação;
- supplier/compra, campanha/bulk;
- WhatsApp/e-mail/envio externo salvo exceção simples conhecida/verificada já aprovada;
- criação de cron, webhook, bot, worker, gateway ou runtime.

## Handoff

Registrar outputs materiais no ledger:

- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/YYYY-MM-DD.md`

Todo registro deve declarar origem do intake, área provável, risco/bloqueio e `Writes externos: não` quando a execução foi apenas read-only/local.