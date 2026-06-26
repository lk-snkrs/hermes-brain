# LC Mordomo OS — P1.4 Zipper packet QA + activation decision

**Data:** 2026-06-05
**Escopo:** regressão local do renderer de pacotes Zipper e decisão de ativação de entrega.
**Modo:** local/read-only; nenhum Telegram, WhatsApp, e-mail, cron, Supabase, banco de produção ou infraestrutura alterado.

---

## Resultado executivo

P1.4 criou a camada de QA que impede o renderer P1.3 de virar um digest/cron ruidoso por acidente.

Resultado atual:

- Pacotes renderizados pelo P1.3: 3.
- Pacotes esperados nos testes: 3.
- Itens negativos suprimidos: 12.
- Falhas de termos proibidos na prévia Lucas-facing: 0.
- Raw PII no relatório Brain gerado: 0 no teste local.
- Decisão de ativação: **bloqueada até aprovação explícita do Lucas para formato + destino + cadência**.

---

## Regressões adicionadas

Arquivo local:

- `/opt/data/profiles/mordomo/scripts/test_zipper_action_packet_renderer.py`

Cobertura:

1. **Renderização positiva:** só os 3 candidatos action-ready viram pacotes.
2. **Casos negativos:** `hard_recipient_blocklist`, erro técnico local, follow-up seguro, `needs_enrichment` e `review_before_alert` ficam fora.
3. **Contrato Lucas-facing:** cada pacote precisa ter urgência, cliente/contexto, o que aconteceu, por que importa, cuidado, recomendação, draft e decisão.
4. **Anti-dump:** termos de cron/log/classificador são proibidos.
5. **PII:** relatório Brain não pode conter JID WhatsApp, telefone cru ou e-mail cru.
6. **Máscara de JID:** WhatsApp JID numérico vira `[phone]`, não `[email]`.
7. **Ativação:** `activation_decision(..., explicit_approval=False)` bloqueia cron e Telegram.

---

## Decisão de ativação

Status atual:

```text
blocked_pending_lucas_approval
```

Motivo:

- falta aprovação explícita do Lucas para destino/cadência de entrega.

Permitido agora:

- manter renderer local;
- rodar QA local;
- gerar preview local/Brain;
- melhorar formato dos pacotes;
- preparar proposta de cadência.

Bloqueado agora:

- criar/reativar cron de Decision Inbox;
- enviar Telegram automático;
- enviar WhatsApp/e-mail para cliente;
- escrever Supabase/produção;
- alterar infraestrutura.

---

## Comando de regressão

```bash
cd /opt/data/profiles/mordomo/scripts
python3 -m unittest test_zipper_action_packet_renderer -v
```

Resultado observado:

```text
Ran 5 tests
OK
```

---

## Próxima frente segura

**P1.5 — revisão editorial dos 3 pacotes e proposta de contrato de entrega.**

Critério de pronto:

- reduzir duplicações no texto dos pacotes;
- calibrar tom Zipper;
- propor cadência/destino/limite sem ativar nada;
- só criar cron ou entrega se Lucas aprovar explicitamente.
