# Mordomo — HEARTBEAT

Status: proposta documental. Nenhum heartbeat/cron foi criado por este arquivo.

## Objetivo

Se futuramente aprovado, Mordomo pode revisar inbox/follow-ups e lembrar Lucas apenas quando houver algo útil, bloqueado ou vencendo.

## Cadências candidatas (não ativas)

- Sob demanda: organizar uma conversa, áudio, print ou lista de tarefas.
- Diário leve: resumo de pendências internas, se aprovado.
- Semanal: higiene de follow-ups e itens esquecidos, se aprovado.

## Condições para virar rotina/cron

Antes de qualquer ativação real:

1. Definir canal/destino.
2. Definir cadência e janela de silêncio.
3. Definir fonte de dados.
4. Definir kill criteria.
5. Criar preview manual.
6. Obter aprovação explícita de Lucas.
7. Registrar em `areas/operacoes/rotinas/runtime-profile-channel-inventory-2026-05-19.md`.

## Contrato de silêncio

Não avisar quando não houver novidade relevante. Não criar digest automático sem decisão de cadência/destino.
