# Memory OS v1.15 — alerta único de mature e fechamento dos legados ambíguos

Gerado: 2026-06-09T20:10:09.581834+00:00

## Escopo

Continuação após v1.14 (`seguir`):

- não fabricar ciclos para chegar a 21/21;
- garantir alerta limpo quando a maturidade real chegar a `mature`;
- revisar os candidatos legados ambíguos deixados para inspeção manual e corrigir só o que é seguro.

## Resultado

- O wrapper de 30min agora emite **um único alerta de promoção** quando `cycle-maturity` chegar a `mature`.
- Enquanto o estado for `pilot_real_cycles`/warming e saudável, continua **stdout 0 bytes**.
- O estado do alerta fica em `reports/memory-hygiene/cycle-maturity-alert-state.json` para não repetir Telegram.
- Dois scripts legados ambíguos foram endurecidos:
  - `scripts/lk_apply_moon_shoe_hero_only_fix_20260526.py`: após escrever `receipt.json`, roda o Memory OS event hook como artifact `unknown`, porque JSON não é aceito pelo receipt writer `.md`.
  - `scripts/lk_geo_source_pages_packet_d_publish_20260523.py`: após escrever o Markdown report com nome `*-receipt.md`, registra via `hermes_memory_os_receipt_writer.py --register-existing` sem sobrescrever conteúdo.
- Dois `ROLLBACK.md` em diretórios de receipt foram mantidos sem conversão: rollback não é receipt operacional.

## Estado vivo antes da execução

- Daytime: ok, routes 0.
- Adoption: ok, gap 0, drift 0.
- Weekly: ok, findings 0, Bruno-grade 10/10.
- Cycle: ok, `pilot_real_cycles`, 5/21 ciclos reais, faltam 16.
- Context recovery: ok.

## Verificação intermediária

- `py_compile` dos scripts alterados: ok.
- Alert wrapper em estado atual: rc=0 e stdout 0 bytes.

## Não-ações

- Sem execução dos scripts Shopify legados; apenas patches locais de auditabilidade.
- Sem writes externos/prod.
- Sem Mission Control.
- Sem alteração de cron além do comportamento local do wrapper já existente.
