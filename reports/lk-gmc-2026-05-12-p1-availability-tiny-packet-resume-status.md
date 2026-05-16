# LK GMC P1-B Availability Tiny Packet — Resume Status, 2026-05-12

Status: `SUPERSEDED_BY_LUCAS_GMC_IN_STOCK_POLICY_2026_05_12`

## Correção posterior de Lucas

Lucas corrigiu a regra: mesmo sem estoque no Tiny, o produto deve aparecer disponível no GMC. Portanto, este packet Tiny-backed não deve ser usado para aprovar `out of stock` no Merchant. Tiny continua sendo evidência operacional para stockout/sourcing, não driver de `availability=out of stock` no GMC.

Packet corrigido: `reports/lk-gmc-2026-05-12-p1-availability-in-stock-policy-packet.md`

## O que foi retomado

- Handoff lido: `reports/lk-os-handoff-after-gateway-restart-2026-05-12.md`.
- Skill carregada: `lk-operational-intelligence`.
- Processo antigo não estava vivo após restart.
- Tiny test read-only simples retornou `OK` para `produtos.pesquisa` com 1 resultado.

## Bloqueio/ajuste encontrado

Ao rodar o packet completo, o Tiny voltou a bloquear na paginação de catálogo:

- endpoint: `produtos.pesquisa`
- página: 3
- `codigo_erro=6`
- status: `Erro`

Ação tomada:

- Corrigido `scripts/lk_gmc_p1_availability_tiny_packet_20260512.py` para tratar `codigo_erro=6` como backpressure/cooldown, não como falha de dados.
- Adicionado retry com cooldown para paginação Tiny e estoque Tiny.
- Mantido guardrail: resposta Tiny não-OK nunca vira `out of stock`.

## Execução atual

- Processo atual: `proc_b97e693ef36f`
- Comando: `python3 scripts/lk_gmc_p1_availability_tiny_packet_20260512.py --tiny-index-sleep 2.0 --tiny-sleep 2.5`
- Modo: read-only/no-write.
- `notify_on_complete=true`.

## Não executado

- Merchant write
- Tiny write
- Shopify write
- Feed/fetch
- DB/POS write
- campanha/envio

## Próximo

Aguardar o processo finalizar para gerar o relatório final com:

- ready
- in stock
- out of stock
- bloqueados/revisão

Nenhuma aplicação no Merchant deve ocorrer sem nova aprovação explícita.
