# Zipper OS — Hermes WhatsApp responder dry-run Fase 1 (2026-05-18)

## Pedido de Lucas

Hermes deve responder perguntas sobre a Zipper no grupo `[ZPR] IA Bot` quando for marcado. Lucas corrigiu que a base não deve ser apenas Supabase `vendas_tango`; pode usar todo o contexto Zipper em modo read-only, incluindo CRM/Main.

## Implementado agora

Script:

- `/opt/data/scripts/zipper_group_mention_responder.py`

Teste:

- `/opt/data/scripts/tests/test_zipper_group_mention_responder.py`

Estado/receipts/previews:

- `/opt/data/hermes_bruno_ingest/local_sql/zipper_group_responder/state.json`
- `/opt/data/hermes_bruno_ingest/local_sql/zipper_group_responder/receipts.jsonl`
- `/opt/data/hermes_bruno_ingest/local_sql/zipper_group_responder/previews/`

## Escopo atual

Fase 1 dry-run apenas:

- valida conta WhatsApp `hermes`;
- valida grupo allowlistado `[ZPR] IA Bot` / `120363423418674006@g.us`;
- lê mensagens recentes do grupo em modo read-only;
- detecta menção ao Hermes ou reply ao Hermes;
- classifica intenção:
  - `sales_mtd`;
  - `crm_lookup`;
  - `sensitive_preview`;
  - `unknown`;
- gera preview local sanitizado;
- registra receipt sem conteúdo bruto e sem PII desnecessária;
- não envia WhatsApp;
- não escreve em Supabase/CRM.

## Fontes elegíveis

- Vendas realizadas: Supabase Zipper Vendas / `vendas_tango`.
- Contexto Zipper: CRM/Main read-only (`contacts`, `conversations`, `secretary_log`, `followups`, `contents`, `artists`, `exhibitions`, etc.).
- Brain Zipper: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper`.

Regra: `vendas_tango` segue sendo a única fonte de verdade para venda realizada. CRM/Brain enriquecem contexto, mas não confirmam venda.

## Validação

TDD:

- Teste RED falhou inicialmente porque o script não existia.
- Implementação criada depois.
- Testes passaram: 4/4.

Comandos validados:

```bash
python3 /opt/data/scripts/tests/test_zipper_group_mention_responder.py
python3 -m py_compile /opt/data/scripts/zipper_group_mention_responder.py /opt/data/scripts/tests/test_zipper_group_mention_responder.py
/opt/data/scripts/zipper_group_mention_responder.py --dry-run --sample-text '@Hermes quanto vendemos esse mês e o que temos no CRM de exposições?'
/opt/data/scripts/zipper_group_mention_responder.py --dry-run --sample-text '@Hermes o que temos no CRM da Zipper sobre exposições e contatos?'
/opt/data/scripts/zipper_group_mention_responder.py --dry-run --limit 10
```

Resultados:

- Grupo WhatsApp validado.
- Conta `hermes` autenticada.
- Últimas 10 mensagens reais escaneadas: 10 ignoradas corretamente porque não tinham menção/reply novo.
- Synthetic sales sample: detectado como `sales_mtd`.
- Synthetic CRM sample: detectado como `crm_lookup`.
- External sends: 0.
- Writes externos: 0.
- Secret scan nos previews/receipts/state: 0 hits.

## Próximo gate

Fase 2: ativar um modo listener/watchdog ainda dry-run ou responder real no grupo allowlistado quando marcado.

Antes de resposta real, recomendado testar no WhatsApp com uma mensagem explícita no grupo, por exemplo:

```text
@Hermes o que vendemos esse mês?
```

O dry-run deve detectar a menção real e registrar o formato observado de menção/reply. Depois disso, pode-se ligar envio controlado no grupo.
