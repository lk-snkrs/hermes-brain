# LK GMC P1-B Availability Tiny Packet — runtime note, 2026-05-12

Status: `gmc_p1_availability_tiny_packet_closed_after_persistent_tiny_backpressure_no_write`

## Resumo

- O packet final no-write já estava materializado em `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.md`.
- Resultado final operacional do packet: 5 itens com diagnóstico `availability` ausente, 0 ready para apply, 5 bloqueados/revisão por ausência de depósito oficial Tiny `LK | CONTROLE ESTOQUE`.
- Uma reexecução conservadora posterior (`proc_b97e693ef36f`, PID 208) ficou em cooldown/retry persistente do Tiny (`codigo_erro=6` / backpressure), sem stdout e sem atualizar artefatos finais.
- Para evitar pressão prolongada na API Tiny sem ganho operacional, a reexecução foi encerrada com SIGTERM pelo Hermes (`exit_code=-15`).

## Guardrails mantidos

- Tiny erro/rate-limit não foi convertido em `out of stock`.
- Nenhuma proposta `availability` foi criada sem leitura válida do depósito oficial.
- Nenhum write externo foi executado.

## Não executado

- Merchant write/update/insert/upsert
- Tiny write
- Shopify write
- feed/fetch
- DB/POS write
- campanha/envio externo

## Próximo passo seguro

Sem ação de Merchant para este packet, pois há 0 itens ready. Próximos blocos devem focar outro bucket P1 ou reavaliar Tiny/deposito oficial em janela de API saudável.
