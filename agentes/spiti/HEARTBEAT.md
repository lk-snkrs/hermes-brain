# HEARTBEAT — Agente SPITI

Status: profile SPITI ativo; heartbeat deve ser baixo ruído e fonte-verificado.

## Checks sugeridos quando houver leilão ativo

- Último horário de atualização de lances.
- Falhas de workflow n8n relacionadas a SPITI.
- Divergência entre e-mail/fonte de verdade e banco.
- Mensagens pendentes para grupo aprovado.
- Lote/bidder/CRM com risco de resposta sem fonte oficial.
- Financial/Growth outputs pendentes de handoff.

Fora de período de leilão, manter baixa prioridade para evitar ruído.

## Política de ruído

Silent-OK: não avisar quando tudo está saudável.

Alertar apenas quando houver:

- decisão necessária;
- bloqueio por aprovação;
- divergência de fonte;
- risco de dado de lance/lote incorreto;
- falha operacional relevante;
- oportunidade/risco com evidência verificável.

## Bloqueios permanentes sem aprovação explícita

- contato com bidder/cliente/grupo;
- deploy, banco/write, workflow n8n ou produção;
- publicação externa;
- afirmação de lance/lote sem fonte oficial.

## Handoff

Registrar outputs materiais no ledger:

- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/YYYY-MM-DD.md`

Todo registro deve declarar a fonte oficial usada e `Writes externos: não` quando a execução foi apenas read-only/local.