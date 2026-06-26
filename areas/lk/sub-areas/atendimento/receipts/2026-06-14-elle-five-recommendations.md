# Elle — 5 recomendações aplicadas

- Data UTC: 2026-06-14T23:43:38Z
- Data BRT: 2026-06-14T20:43:38-0300
- Área: LK / Atendimento / Elle Chatwoot
- Classificação: external-write
- Aprovação/scope: Lucas pediu no Telegram: "Fazer as 5 recomendações" em resposta à lista de melhorias recomendadas para a Elle.

## Escopo executado

Aplicadas em produção melhorias determinísticas e seguras para reduzir respostas erradas da Elle:

1. Redução de repetição da introdução da Elle quando já houve apresentação anterior na conversa.
2. Resposta para horário da loja/atendimento: segunda a sexta 10h–19h e sábado 10h–18h, sem prometer disponibilidade.
3. Fluxo seguro para troca/devolução/reembolso genérico: coletar número do pedido + motivo e transbordar para Larissa, sem aprovar troca/reembolso/devolução.
4. Micro-guias de calce aprovados: Mind 001, Yeezy Slide e Yeezy 350 = 1 número acima; New Balance 204L = tamanho normal; Onitsuka genérico pede modelo/link.
5. Foto/print/screenshot ambíguo: não adivinhar produto; pedir nome, link ou print com texto legível.
6. Relatório/observer: buckets de resposta adicionados para separar respondido, respondido com transbordo, não respondeu corretamente e não respondeu revisar.

## Arquivos alterados

- VPS produção: `/opt/elle-chatwoot/app.py`
- VPS produção: `/opt/elle-chatwoot/elle_observer_summary.py`
- Skill/reference local atualizado: `customer-chat-operations/references/elle-lucas-corrections-size-address-store-20260614.md`

## Backup

- `/root/elle-rollbacks/elle-five-recommendations-20260614-234046/`

## Deploy

Comando de produção executado em `/opt/elle-chatwoot`:

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

- `store_hours`: `institutional`, `handoff=false`, reply contém `10h às 19h` e `sábado das 10h às 18h`.
- `exchange_policy`: `human_handoff`, `handoff=true`, `blocked=["exchange_policy_collect_details"]`, coleta número do pedido + motivo.
- `fit_nb204l`: `product_clear`, `handoff=false`, recomenda tamanho normal.
- `fit_yeezy`: `product_clear`, `handoff=false`, recomenda 1 número acima.
- `photo_ambiguous`: `product_clear`, `handoff=false`, pede nome/link/print legível e não adivinha modelo.
- `mixed_catalog_store`: `stock_handoff`, `handoff=true`, inclui navegação pelo site + Larissa para loja física/pronta entrega/retirada.
- `repeat_intro_store_hours`: `institutional`, `handoff=false`, reply sem repetir `Aqui é a Elle da LK`.

## Guardrails preservados

Não foi adicionado nenhum fluxo que prometa:

- estoque;
- pronta entrega;
- disponibilidade em loja;
- reserva;
- prazo;
- preço;
- desconto;
- troca aprovada;
- devolução aprovada;
- reembolso/estorno aprovado;
- alteração de endereço garantida.

Disponibilidade, loja física, pronta entrega, retirada e reserva continuam transbordando para Larissa/lk-stock.
