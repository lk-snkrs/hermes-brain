# Receipt — PRD lk-stock: modo de trabalho gradual

Data UTC: 2026-06-08T15:42:56Z

## Decisão capturada

Lucas escolheu continuar o PRD do agente `[LK] Estoque Loja Física` pelo caminho:

**Sistema completo gradual: manual → rotina → bot, cada etapa com gate de aprovação.**

## Alteração documental

Arquivo atualizado:

- `areas/lk/sub-areas/stock/PRD.md`

Seções adicionadas/expandida:

- `10. Modo de trabalho gradual aprovado para desenho`
- `11. Contrato operacional — como o agente deve trabalhar`
- `12. Gates de ativação`
- renumeração de critérios de aceite para `13`

## Guardrails preservados

- Tiny/fonte viva continua obrigatório antes de afirmar disponibilidade.
- Writes externos executados: `0`.
- Cron/gateway/bot ativados: `0`.
- Compra, fornecedor, cliente, Tiny, Shopify, campanha e WhatsApp seguem bloqueados sem aprovação escopada.
- Telegram deve ser silent-OK e só alertar decisão acionável/falha/P0/aprovação.

## Próximo ponto de PRD

Definir o **Gate A — Manual read-only** em detalhe:

- quais fontes read-only serão usadas primeiro;
- quais 3 casos reais servem como aceite;
- formato final da fila/packet que Lucas quer receber.
