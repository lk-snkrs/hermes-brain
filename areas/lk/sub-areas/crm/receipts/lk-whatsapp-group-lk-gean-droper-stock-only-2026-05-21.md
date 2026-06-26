# LK WhatsApp — Grupo LK + GEAN + DROPER com resposta de estoque

Data: 2026-05-21
Responsável: Hermes
Escopo: LK Sneakers / CRM / WhatsApp interno

## Pedido do Lucas

Lucas informou que adicionou o número do Hermes no grupo WhatsApp `LK + GEAN + DROPER` e pediu que Hermes saiba responder sobre estoque da LK nesse grupo.

## Implementação

- Grupo localizado via `wacli --account hermes groups list --json`.
- Grupo adicionado à allowlist do responder LK WhatsApp.
- Escopo definido como **stock-only** para esse grupo:
  - responde apenas quando Hermes for mencionado ou quando responderem uma mensagem do Hermes;
  - responde apenas perguntas de estoque com SKU/modelo + tamanho;
  - usa a lógica catalog-aware de SKU+tamanho antes de consultar Tiny;
  - fonte de estoque: `LK | CONTROLE ESTOQUE`.

## Guardrails

Neste grupo, Hermes não deve:

- responder vendas/site/GA4/Shopify analytics;
- criar cards de compra no Notion/Júlio;
- reservar produto;
- negociar preço/prazo;
- contactar fornecedor;
- comprar ou acionar fluxo de reposição;
- alterar Shopify, Tiny, Notion, estoque, preço ou campanhas.

## Validação

- `wacli --account hermes auth status --json`: autenticado.
- Grupo verificado localmente por nome e JID via wacli.
- `python3 -m py_compile` do responder: OK.
- `lk_hermes_whatsapp_responder_selftest.sh`: OK / silent.
- Responder reiniciado e `state.json` confirmou o grupo na allowlist ativa.

## Arquivos alterados

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- Skill runtime `wacli-whatsapp-cli`, referência `references/lk-group-responder-webhook-pattern.md`
