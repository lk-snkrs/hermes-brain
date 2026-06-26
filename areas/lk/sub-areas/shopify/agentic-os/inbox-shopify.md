# Inbox Shopify — LK Shopify OS

Data de criação: 2026-06-05
Status: operacional local/read-only; não autoriza writes externos por si só.

## Função

Fila única de entradas para o agente-funcionário **LK Shopify**. Tudo que chega aqui deve virar uma saída técnica segura: diagnóstico read-only, preview, approval packet, readback, receipt, rollback, bloqueio ou handoff.

## Regra central

Nenhum item desta inbox autoriza criar/editar/publicar no Shopify, Tiny, GMC, Klaviyo, Meta, Google Ads, webhooks ou apps. Writes exigem aprovação explícita e escopada.

## Estados

- `new`: entrada bruta ainda não classificada.
- `triaged`: objeto Shopify, risco e fonte definidos.
- `source-needed`: falta fonte viva, objeto exato ou autorização read-only.
- `preview-queued`: pronto para entrar na fila de preview.
- `preview-ready`: preview/diff pronto.
- `approval-packet`: precisa aprovação de Lucas.
- `approved-scope`: aprovado para execução exata.
- `executed-readback-pending`: executado, aguardando readback/QA.
- `receipt-done`: receipt concluído.
- `blocked`: bloqueado por risco/fonte/aprovação.

## Campos obrigatórios por item

```yaml
id: SHOPIFY-INBOX-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source: Lucas | LK Growth | LK Ops | LK Trends | Hermes Geral | Shopify readback | Other
request: "descrição curta"
object:
  type: product | variant | collection | page | theme | section | snippet | asset | css | menu | tag | metafield | seo_field | price | promo | cart_drawer | feature | app_config | tracking | inventory_item | other
  identifier: "handle/id/url/theme/etc"
risk_level: A0 | A1 | A2 | A3 | A4
status: new
owner: lk-shopify
source_of_truth_needed:
  - Shopify read-only
  - Tiny
  - Brain
  - approved packet
  - browser QA
  - other
write_intent: none | preview_only | possible_write_after_approval | approved_write
approval_needed_before_write: true
required_output: diagnosis | preview | approval_packet | readback | receipt | rollback | blocked
originating_agent: none | lk-growth | lk-ops | lk-trends | hermes-geral
links:
  preview: null
  packet: null
  snapshot: null
  receipt: null
  rollback: null
notes: []
```

## Triagem rápida

### Pode seguir local/read-only

- identificar objeto;
- gerar rascunho;
- preparar diff;
- comparar antes/depois local;
- QA visual sem mutação;
- ler Shopify/Tiny quando credencial e escopo read-only já existirem;
- documentar packet/receipt local.

### Deve bloquear até aprovação

- produto/variant/coleção/page/theme/metafield/SEO field/menu/tag/inventory write;
- preço/estoque/disponibilidade/status/publicação;
- integração com Tiny/GMC/Klaviyo/Meta/Google Ads/webhook/app;
- produção/publish/deploy;
- contato externo.

## Relação com a fila de previews

Todo item que exigir mudança técnica deve ir para `preview-queue.md` antes de qualquer approval packet. Sem preview/diff/snapshot/rollback, não pedir aprovação de write.

## Entradas atuais

Sem entradas novas nesta criação. Usar no próximo fluxo real.
