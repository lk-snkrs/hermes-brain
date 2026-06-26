# Receipt — Hermes Memory OS v1.3 integração padrão do hook

Data: 2026-06-09T14:02:21Z  
Owner: LC Hermes / Hermes Agent central  
Escopo: integração local/documental do hook nos protocolos canônicos; sem runtime sensível.

## Objetivo

Reduzir dependência de lembrança manual: os templates/protocolos canônicos de receipt/handoff agora instruem a chamada do Memory OS event hook após artefatos materiais.

## Mudanças executadas

- Atualizado `areas/operacoes/templates/receipt-operacional.md` com seção `Memory OS hook obrigatório`.
- Atualizado `areas/operacoes/rotinas/protocolo-receipts-handoff-v016-operating-layer.md` com regra `Memory OS v1.3 — hook pós-receipt/handoff`.
- Atualizado `areas/operacoes/rotinas/checklist-handoff-receipt-obrigatorio-2026-05-26.md` com checklist de hook.
- Atualizados PRD, rotina, dashboard, hot e daily para refletir v1.3.

## Comando padrão

```bash
python3 /opt/data/scripts/hermes_memory_os_event_hook.py <caminho-do-artefato>
```

## Contrato operacional

- Hook fica silencioso quando verde.
- Saída do hook vira alerta local/actionable, não Telegram automático.
- Hook não substitui receipt/handoff; só atualiza Memory OS imediatamente.
- Hook não autoriza provider externo, Docker/VPS/gateway ou writes de negócio.

## Guardrails preservados

- Nenhum cron novo.
- Nenhum Docker/VPS/Traefik/gateway/container/restart.
- Nenhum provider externo/Mem0/Honcho ativado.
- Nenhum write em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/campanha.
- Nenhum secret impresso ou copiado.

## Rollback

- Remover as seções v1.3 dos três templates/protocolos.
- Manter v1.2 hook e v1.1 checker/scorecard operando independentemente.
