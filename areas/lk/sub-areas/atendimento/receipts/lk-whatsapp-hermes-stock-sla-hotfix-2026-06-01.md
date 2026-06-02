# Receipt — LK WhatsApp Hermes stock SLA hotfix

Data: 2026-06-01T12:05:26+00:00  
Aprovador: Lucas Cimino (`Aprovo`)  
Escopo aprovado: hotfix de SLA do responder WhatsApp LK; ajustar código local para resposta segura/interina quando a consulta Tiny passar do timeout, rodar testes/smokes read-only e reiniciar somente o processo do responder na porta 8787.

## Arquivos alterados

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`

## Mudança aplicada

- Adicionado `safe_stock_validation_answer(...)` para retorno seguro quando não houver saldo validado rápido.
- `answer_assisted_sale(...)` agora aceita:
  - `allow_broad_fallback`;
  - `live_time_budget_seconds`.
- `build_stock_only_answer(...)` agora usa caminho rápido para perguntas `stock` e `assist` com tamanho/modelo/SKU:
  - consulta catálogo local/snapshot/cache/Tiny por candidato;
  - não deixa fallback Tiny amplo bloquear stock-only;
  - retorna resposta segura com fonte tentativa, confiança baixa/média e sem promessa quando não valida rápido.
- Mantido caminho amplo para `answer_assisted_sale(...)` normal quando chamado fora de `stock-only`, preservando diagnósticos existentes.

## Teste RED criado

- `test_stock_only_cli_returns_safe_answer_instead_of_broad_tiny_blocking`
- O teste garante que `@Hermes tem U9060WHT 38?` em stock-only:
  - não chama fallback Tiny amplo;
  - não chama `answer_stock` lento;
  - devolve resposta segura com `Tamanho: 38`, Tiny/LK Controle e validação manual.

## Verificações executadas

Comando:

```bash
python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_tiny_stock_local_db.py
python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v
```

Resultado:

- Sintaxe OK.
- 7 testes OK.

Smokes CLI read-only, sem envio WhatsApp:

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes cliente quer New Balance 9060 38, o que temos?' --stock-only --json-output
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes tem U9060WHT 38?' --stock-only --json-output
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes você tem Onitsuka 38?' --stock-only --json-output
```

Resultado:

- Todos responderam rápido dentro do timeout de 180s do gate.
- Quando não havia saldo validado rápido, retornaram fallback seguro:
  - `Não achei saldo validado rápido no Tiny...`
  - `Fonte tentada: catálogo local + Tiny / LK | CONTROLE ESTOQUE`
  - `Confiança: baixa/média`
  - sem reserva, sem alteração de estoque, sem promessa de preço/entrega.

## Restart runtime

Antes:

- Processo antigo: PID `157`
- Comando: `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`
- Porta 8787 aberta.

Ação:

- Encerrado somente PID `157`.
- Iniciado novo processo em background Hermes:
  - session_id: `proc_d9afbb5d5cc2`
  - PID: `19639`
  - comando: `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`

Validação pós-restart:

```text
POST http://127.0.0.1:8787/ -> 200 ok
process poll -> running
ps -> PID 19639 ativo
```

## O que não foi feito

- Nenhum envio WhatsApp manual de teste.
- Nenhum write Shopify.
- Nenhum write Tiny.
- Nenhum write Notion/CRM/Klaviyo/n8n.
- Nenhuma alteração de Docker/VPS/cron/gateway.
- Nenhuma promessa de disponibilidade/preço/entrega/reserva.

## Rollback

Rollback local simples:

1. Reverter as alterações em:
   - `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
   - `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`
2. Rodar py_compile + testes.
3. Matar somente o PID do responder atual na porta 8787.
4. Subir novamente:

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787
```

## Status

Hotfix aplicado e responder reiniciado. O stock-only agora falha de forma segura/rápida quando não consegue validar saldo no Tiny em tempo curto, em vez de ficar silencioso por minutos.
