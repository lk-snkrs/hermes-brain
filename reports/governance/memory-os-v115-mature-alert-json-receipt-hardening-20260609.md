# Memory OS v1.15 — alerta único de maturidade + hardening de receipts JSON legados

Gerado: 2026-06-09T20:16:27.741433+00:00

## Escopo

Continuação da ativação segura/local do Memory OS depois da v1.14.

## O que foi ativado

1. **Alerta único de promoção `mature`**
   - O wrapper daytime já mantém `reports/memory-hygiene/cycle-maturity-alert-state.json`.
   - Enquanto o sistema está saudável mas ainda em `pilot_real_cycles`, o wrapper permanece silencioso.
   - Quando atingir `mature` com 21/21 ciclos reais consecutivos silent-OK, emite um único alerta Telegram-safe e grava o estado para não repetir ruído.

2. **Hardening dos legados `receipt.json`**
   - 79 scripts com write de `receipt.json` foram avaliados.
   - 77 scripts que ainda não tinham evidência Memory OS receberam helper local `memory_os_hook_json_receipt(...)` após o write.
   - Resultado estático: 79/79 writes de `receipt.json` agora estão cobertos por hook/writer/guard.
   - Nenhum script de Shopify/prod foi executado; só código foi alterado e compilado.

## Arquivos principais

- Wrapper: `/opt/data/scripts/hermes_memory_os_daytime_alerting_watchdog.py`.
- Lista completa dos 77 scripts endurecidos: `reports/governance/memory-os-v115-json-receipt-hardening-file-list-20260609.txt`.

## Limites preservados

- Sem Mission Control.
- Sem Docker/VPS/Traefik/gateway/restart.
- Sem provider externo/Mem0.
- Sem execução dos scripts legados de Shopify/prod.
- Sem writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Sem secrets impressos.

## Critério de sucesso

- Alert wrapper rc=0 e stdout 0 bytes enquanto não-mature saudável.
- Todos os scripts tocados passam em `py_compile`.
- Static check: `unhardened=[]` para `receipt.json` write.
- Memory OS checker/linter/weekly/context/cycle verdes.
- Brain health/docs guard/secret scan verdes.
