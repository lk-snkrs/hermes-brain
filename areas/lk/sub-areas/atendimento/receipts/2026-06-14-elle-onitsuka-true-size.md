# Elle — regra Onitsuka Tiger tamanho real aplicada

- Data UTC: 2026-06-14T23:52:55Z
- Data BRT: 2026-06-14T20:52:55-0300
- Área: LK / Atendimento / Elle Chatwoot
- Classificação: external-write
- Aprovação/scope: Lucas pediu no Telegram: "Implemente todas as melhorias na Elle", após corrigir que Onitsuka Tiger deve usar tamanho real.

## Escopo executado

Aplicada em produção a regra de calce:

- Onitsuka Tiger = tamanho normal / tamanho real.
- Exemplo aprovado: se o cliente normalmente usa 37, recomendar 37.
- Mantidas exceções já aprovadas: Mind 001, Yeezy Slide e Yeezy 350 = 1 número acima.

## Arquivos alterados

- VPS produção: `/opt/elle-chatwoot/app.py`

## Backup

- `/root/elle-rollbacks/elle-onitsuka-true-size-20260614-235159/`

## Deploy

Comando executado em `/opt/elle-chatwoot`:

```bash
python3 -m py_compile app.py elle_observer_summary.py
docker compose up -d --no-deps --build --force-recreate elle-chatwoot
```

## Verificação

Verificações executadas após deploy:

- `python3 -m py_compile app.py elle_observer_summary.py`: OK.
- Docker rebuild/recreate do container `elle-chatwoot`: OK.
- Testes sintéticos com assertions: OK.
- Observer summary smoke: OK.
- Health externo `https://elle.lkskrs.online/healthz`: OK.

Health verificado, sem secrets:

```json
{
  "ok": true,
  "dry_run": false,
  "write_enabled": true,
  "kill_switch": false,
  "public_reply_enabled": true,
  "ai_enabled": true,
  "ai_provider": "openrouter",
  "observer_enabled": true
}
```

## Testes sintéticos relevantes

- `onitsuka_37`: `product_clear`, `handoff=false`, reply contém `se você usa 37, recomendamos 37`.
- `onitsuka_generic`: `product_clear`, `handoff=false`, reply contém `tamanho normal` e não pede modelo/link.
- `fit_nb204l`: `product_clear`, recomenda tamanho normal.
- `fit_yeezy`: `product_clear`, recomenda 1 número acima.
- `store_hours`: `institutional`, responde horário.
- `exchange_policy`: `human_handoff`, coleta número do pedido + motivo.
- `photo_ambiguous`: `product_clear`, não adivinha modelo por foto.
- `mixed_catalog_store`: `stock_handoff`, mantém Larissa para loja física/pronta entrega/retirada.
- `repeat_intro_store_hours`: resposta sem repetir `Aqui é a Elle da LK`.

## Guardrails preservados

Não foi adicionado nenhum fluxo que prometa estoque, pronta entrega, disponibilidade, reserva, prazo, preço, desconto, troca/devolução/reembolso aprovado ou alteração operacional garantida.
