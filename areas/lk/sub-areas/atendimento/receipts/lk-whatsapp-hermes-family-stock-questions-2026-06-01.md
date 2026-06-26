# Receipt — LK WhatsApp Hermes family stock questions

Data: 2026-06-01T12:13:25+00:00  
Aprovador: Lucas Cimino (`Sim fazer`)  
Escopo: ampliar famílias de perguntas do responder de estoque LK e priorizar quantidade de pares, modelo e tamanhos.

## Mudanças aplicadas

Arquivos:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`

### Parsing / famílias de perguntas

O `stock-only` passou a aceitar perguntas naturais sem tamanho explícito, como:

- `@Hermes quais pares 9060 temos?`
- `@Hermes quais modelos e tamanhos de Slide Nike Mind temos?`
- `@Hermes você tem Onitsuka 38?`

Ajustes:

- `STOCK_WORDS` ganhou termos como `temos`, `pares`, `par`, `modelo`, `modelos`, `o que temos`.
- Stopwords de catálogo/produto ganharam `voce/você/voc/vc`, `tem`, `tenho`, `pares`, `par`, `modelo`, `modelos` para não poluir a busca.
- `build_stock_only_answer()` agora roteia qualquer pergunta stock-only com termo de produto/SKU/família para o caminho rápido de atendimento, mesmo sem tamanho.

### Formato de resposta

Resposta de disponibilidade agora destaca:

- `Total validado: X par(es) em N tamanho(s) (...)`;
- cada linha começa com `Modelo: ...`;
- cada item inclui `Tamanho: X`, SKU e saldo em pares;
- mantém fonte/frescor quando vem do Tiny local snapshot;
- mantém guardrail: sem reserva, sem alteração de estoque, sem promessa de preço/entrega.

### Correção de falso match local

Foi removido o `v.product_title` bruto do haystack de busca de candidatos porque alguns registros locais carregam JSON bruto; isso causava match falso de `9060` por barcode dentro do JSON e podia mostrar produto errado. Agora a busca usa título limpo de `lk_products`, variante e SKU.

## Snapshot local Tiny ampliado

Foi feita leitura read-only via Tiny para famílias prioritárias, gravando apenas snapshot local derivado do Tiny:

- `New Balance 9060`
- `New Balance 9060 tamanho 38`
- `Onitsuka tamanho 38`
- `New Balance 204L`
- `Slide Nike Mind`

Resultado do snapshot local após leitura:

- `stock_by_sku`: 38 registros.
- `Slide Nike Mind`: 4 SKUs lidos, com positivos:
  - `HQ4307-003-2` — tamanho 35 — 3 pares;
  - `HQ4307-003-3` — tamanho 36 — 3 pares;
  - `HQ4307-001-9` — tamanho 42 — 1 par.
- `Onitsuka 38`: positivo:
  - `1183C102250-5` — tamanho 38 — 3 pares.
- `U9060%`: 14 SKUs lidos no snapshot local, todos com `official_available = 0` nos candidatos verificados.
- `U204L%`: 6 SKUs lidos no snapshot local, todos com `official_available = 0` nos candidatos verificados.

Observação: zero em candidatos verificados não significa que toda a família global está zerada; significa que o caminho rápido não encontrou positivo validado no recorte/candidatos lidos. O responder segue devolvendo fallback seguro quando não há validação rápida.

## Verificações

Comando:

```bash
python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_tiny_stock_local_db.py
python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v
```

Resultado:

- Sintaxe OK.
- 8 testes OK.

Smokes CLI read-only:

1. `@Hermes quais modelos e tamanhos de Slide Nike Mind temos?`

Resultado resumido:

- Total validado: 7 pares em 3 tamanhos `(35, 36, 42)`.
- Modelos/SKUs listados:
  - Slide Nike Mind 001 Light Smoke Grey Cinza — tamanho 35 — `HQ4307-003-2` — 3 pares;
  - Slide Nike Mind 001 Light Smoke Grey Cinza — tamanho 36 — `HQ4307-003-3` — 3 pares;
  - Slide Nike Mind 001 Black Chrome Preto — tamanho 42 — `HQ4307-001-9` — 1 par.

2. `@Hermes você tem Onitsuka 38?`

Resultado resumido:

- Total validado: 3 pares em tamanho 38.
- Modelo/SKU:
  - Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom — tamanho 38 — `1183C102250-5` — 3 pares.

3. `@Hermes quais pares 9060 temos?`

Resultado resumido:

- Sem saldo validado rápido no Tiny para `9060`.
- Retorna fallback seguro, com fonte tentada e sem promessa comercial.
- Não mostrou mais falso match de produto com JSON/barcode.

## Runtime

Responder reiniciado após alterações:

- Processo antigo: PID `19639` encerrado.
- Novo processo: PID `22997`.
- Hermes background session: `proc_c12a293a2fac`.
- Validação: `POST http://127.0.0.1:8787/ -> 200 ok`.
- `process poll`: running.

## O que não foi feito

- Nenhum envio WhatsApp manual.
- Nenhum write em Shopify.
- Nenhum write em Tiny.
- Nenhum write em Notion/CRM/Klaviyo/n8n.
- Nenhuma alteração de Docker/VPS/cron/gateway.
- Nenhuma promessa comercial.

## Próximo passo sugerido

Criar rotina/evento de refresh sob demanda para famílias perguntadas frequentemente: quando o Hermes responder fallback seguro para um modelo, enfileirar uma auditoria Tiny read-only mais ampla em background e atualizar o snapshot local para a próxima pergunta.
