# Receipt — Elle pronta entrega vs status de pedido fix

Data: 2026-06-15
Área: LK / atendimento / Elle / Chatwoot

## Correção

Lucas apontou erro em conversa Chatwoot #1924: cliente perguntou se o tênis estava à pronta entrega, mas Elle respondeu pedindo número do pedido para status do pedido.

Causa técnica: a frase “pronta entrega” contém o termo “entrega”, e o pós-processamento de IA priorizava `order_status` antes de `hard_stock` em uma etapa, permitindo cair na resposta de status de pedido.

Aplicado ajuste determinístico em `/app/app.py` do container `elle-chatwoot`:

- `hard_stock` agora bloqueia chamada de IA para perguntas de estoque/pronta entrega.
- `hard_stock` força `category=stock_handoff`, `handoff=true`, labels `estoque` + `humano`.
- A regra de status de pedido agora exige `not hard_stock`.
- Imagem atual do Compose persistida com `docker commit elle-chatwoot elle-chatwoot-elle-chatwoot:latest`.

## Backup / rollback

Backup final da aplicação antes/depois:

- `/opt/data/backups/elle-stock-vs-orderstatus-20260615T144547Z/app.py.before`
- `/opt/data/backups/elle-stock-vs-orderstatus-20260615T144547Z/app.py.after`

Rollback rápido:

```bash
docker cp /opt/data/backups/elle-stock-vs-orderstatus-20260615T144547Z/app.py.before elle-chatwoot:/app/app.py
docker restart elle-chatwoot
docker commit elle-chatwoot elle-chatwoot-elle-chatwoot:latest
```

## Verificação

Health live após restart:

- ok: true
- dry_run: false
- write_enabled: true
- kill_switch: false
- public_reply_enabled: true
- ai_enabled: true
- observer_enabled: true

Smoke live no container:

1. Entrada: `Esse você tem a pronta entrega ?`
   - category: `stock_handoff`
   - handoff: true
   - reply: Larissa/pronta entrega/modelo+numeração
   - ai.used: false

2. Entrada: `Estou apenas perguntando se vocês teriam esse tênis a pronta entrega ?`
   - category: `stock_handoff`
   - handoff: true
   - reply: Larissa/pronta entrega/modelo+numeração
   - ai.used: false

3. Controle: `Qual o status do pedido?`
   - category: `institutional`
   - handoff: false
   - reply: pede número do pedido
   - ai.used: true

## Observações

- Nenhuma disponibilidade foi prometida.
- Nenhuma consulta direta de estoque foi feita por LK Ops.
- Não houve retro-envio manual para a conversa da cliente neste receipt.
