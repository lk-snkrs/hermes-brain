# LK GMC P1-B Availability Tiny Packet — Resume Status, 2026-05-12

Status: `gmc_p1_availability_tiny_packet_running_with_tiny_backpressure_handling`

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
