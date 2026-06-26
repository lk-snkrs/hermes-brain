# LK Dia dos Namorados — extração Top 30 clientes 2026

Data: 2026-06-10
Operador: Hermes lk-ops
Escopo aprovado por Lucas: extrair lista read-only; sem envio externo.

## Fonte

- Shopify Admin REST, somente leitura.
- Período: pedidos criados desde 2026-01-01T00:00:00-03:00.
- Critério: clientes com compra paga/não cancelada em 2026, telefone disponível, mais de 20 dias sem compra.
- Ranking: maior total comprado em 2026, depois maior quantidade de pedidos, depois compra mais recente.

## Resultado

- Pedidos lidos: 2191.
- Pedidos incluídos pagos/não cancelados: 1789.
- Grupos de clientes: 1548.
- Elegíveis antes do Top 30: 1246.
- Selecionados: 30.
- Desqualificados por telefone ausente: 99.
- Desqualificados por última compra há menos de 20 dias: 203.
- Pedidos excluídos: refunded 48, cancelados 289, pending 65.

## Observação de vendedor

- 17 dos 30 selecionados não tinham vendedor identificável no último pedido/histórico carregado.
- 19 dos 30 não tinham vendedor exatamente na última compra; em alguns casos foi encontrado vendedor conhecido em compra anterior.
- Isso precisa de decisão antes de envio real: usar apenas clientes com vendedor da última compra, usar último vendedor conhecido, ou assinar como Equipe LK Sneakers quando faltar vendedor.

## Artefatos locais com PII

Não versionar/não enviar sem necessidade.

- Raw JSON: `/opt/data/profiles/lk-ops/reports/lk-valentines-2026/lk_valentines_top30_raw_20260610T162248Z.json`
- Raw CSV: `/opt/data/profiles/lk-ops/reports/lk-valentines-2026/lk_valentines_top30_raw_20260610T162248Z.csv`
- Redacted JSON: `/opt/data/profiles/lk-ops/reports/lk-valentines-2026/lk_valentines_top30_redacted_20260610T162248Z.json`

## Segurança

- `send_executed=false`.
- `external_write_executed=false`.
- `values_printed=false`.
- Sem write em Shopify, Chatwoot ou Evolution.

## Decisão de Lucas no Telegram

Lucas escolheu: se não houver vendedor, assinar como `Equipe LK Sneakers`.

## Próximo gate

Próxima etapa ainda exige aprovação separada se envolver write externo:

- dry-run/local preview: permitido sem envio;
- criação de notas/conversas/labels no Chatwoot: write externo, pedir aprovação escopada;
- envio real via Evolution API: pedir aprovação explícita da lista + texto final.
