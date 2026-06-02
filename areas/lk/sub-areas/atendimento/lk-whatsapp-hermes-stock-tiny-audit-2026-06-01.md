# LK WhatsApp Hermes — auditoria Tiny/estoque para respostas por produto/tamanho

Data: 2026-06-01 11:59 UTC  
Escopo: leitura local/read-only do responder LK WhatsApp/Telegram, catálogo Shopify local e espelhos Tiny locais.  
Bloqueios respeitados: sem envio WhatsApp, sem Shopify write, sem Tiny write, sem restart do responder.

## Pedido do Lucas

Lucas quer que o Hermes no WhatsApp responda perguntas internas do time como:

- `@Hermes você tem Onitsuka 38?`
- `@Hermes você tem New Balance 9060 38?`
- `@Hermes tem U9060WHT 38?`
- `@Hermes cliente quer Chinelo Slide Nike Mind 001 39.5, o que temos?`

Objetivo operacional: correlacionar produto/modelo/SKU + tamanho com o estoque oficial no Tiny, usando Shopify/base local apenas como resolução de catálogo/variante.

## Fonte de verdade e contrato

1. **Tiny é a fonte de verdade de estoque.**
2. O depósito oficial para disponibilidade é `LK | CONTROLE ESTOQUE`.
3. Shopify/local catalog serve para resolver candidato: produto, variante, tamanho, SKU e contexto visual/comercial.
4. Shopify inventory não pode ser usado como disponibilidade final.
5. Pergunta de disponibilidade precisa responder em nível de variante/tamanho.
6. Resposta deve incluir:
   - veredito de estoque;
   - quantidade no `LK | CONTROLE ESTOQUE` quando validada;
   - produto;
   - `Tamanho: X` explicitamente;
   - SKU canônico;
   - fonte e confiança;
   - aviso: sem reserva, sem alteração de estoque, sem promessa de preço/entrega.

## Código auditado

Arquivo principal:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

Funções-chave:

- `classify_request(text)` — classifica pergunta como `assist`, `stock`, `sales`, `ops`, etc.
- `build_stock_only_answer(text)` — caminho seguro para grupos de estoque: não cria Notion/card e não envia WhatsApp no modo CLI.
- `answer_assisted_sale(text)` — pergunta natural de atendimento (`cliente quer ... o que temos?`).
- `answer_stock(text)` — pergunta direta de estoque/SKU.
- `tiny_stock_resolver_v2(...)` — caminho Tiny oficial: pesquisa Tiny, expande variações, lê `produto.obter.estoque`, soma apenas `LK | CONTROLE ESTOQUE`, deduplica por produto/SKU/tamanho.
- `tiny_stock_for_exact_sku(...)` — consulta SKU exato delegando ao resolver v2.
- `local_catalog_candidates(...)` — acha candidatos por catálogo local Shopify/Data Spine, sem confiar no estoque Shopify.
- `local_stock_db_instock_variants_for_candidates(...)` — usa snapshot local derivado do Tiny quando fresco.
- `live_tiny_instock_for_candidates(...)` — confirma candidatos no Tiny por SKU, com orçamento de tempo.
- `tiny_search_instock_variants(...)` — fallback amplo no Tiny.

Banco catálogo local:

- `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite`
- Tabelas relevantes: `lk_products`, `lk_product_variants`, `lk_orders`, `lk_order_items`.

Banco local Tiny/snapshot:

- `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite`
- Tabela: `stock_by_sku`.
- Regra: é snapshot de leitura Tiny, nunca cálculo por delta local.

Cache curto:

- `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/stock_cache.sqlite`
- TTL do responder atual: 10 minutos.

## Como o Hermes deve ler o dado do Tiny

### Caminho rápido ideal para WhatsApp

1. Parsear texto:
   - marca/modelo: `New Balance 9060`, `Onitsuka Tiger Mexico 66`, `Chinelo Slide Nike Mind 001`;
   - SKU/base SKU: `U9060WHT`, `HQ4307003-36`;
   - tamanho: `38`, `39.5`, etc.
2. Resolver candidatos no catálogo local:
   - procurar variantes ativas por título/modelo/SKU;
   - restringir por `option1/title` quando houver tamanho;
   - normalizar SKU compacto quando aplicável.
3. Verificar snapshot local derivado do Tiny para esses SKUs:
   - aceitar somente leitura fresca;
   - somar somente `official_available` do depósito `LK | CONTROLE ESTOQUE`.
4. Se snapshot não tiver positivo, fazer consulta live Tiny por SKU para poucos candidatos, com timeout curto.
5. Se ainda não houver confiança, devolver resposta segura/interina em vez de travar o atendimento:
   - “não encontrei saldo validado rápido; precisa validação manual/live antes de prometer ao cliente”.
6. Só usar busca ampla/paginada no Tiny como diagnóstico/background, não como caminho bloqueante do WhatsApp.

### Caminho Tiny v2 atual

`tiny_stock_resolver_v2` faz:

- `produtos.pesquisa` por termo;
- paginação bounded (`max_pages`, padrão 20 para amplo; 3 para SKU exato);
- expansão de parent product via `produto.obter` quando precisa achar variação/tamanho;
- leitura de estoque por `produto.obter.estoque`;
- parse dos depósitos;
- soma de `LK | CONTROLE ESTOQUE`;
- dedupe por produto normalizado + SKU + tamanho;
- retorno de `confidence`: alta/média/baixa;
- escrita local de snapshot/cache Tiny-derived.

## Evidência local consultada

Em 2026-06-01 11:59 UTC:

- Catálogo local existe: `lk_os_phase5.sqlite`.
- `lk_products`: 2.241 registros.
- `lk_product_variants`: 14.466 registros.
- Snapshot local Tiny existe: `lk_tiny_stock_local.sqlite`.
- `stock_by_sku`: 9 registros.
- Amostra U9060 tamanho 38 no snapshot Tiny local indicou alguns SKUs lidos do Tiny com `official_available = 0`, por exemplo:
  - `U9060EEG` — tamanho 38 — 0 no controle;
  - `U9060TRU-38` — tamanho 38 — 0 no controle;
  - `U9060SG-5` — tamanho 38 — 0 no controle;
  - `U9060CTA-5` — tamanho 38 — 0 no controle;
  - `U9060ERA-5` — tamanho 38 — 0 no controle.

Observação: esses zeros são evidência de leitura Tiny para esses SKUs, mas não provam que **todos** os 9060 tamanho 38 estão zerados. Para afirmar disponibilidade de “9060 38” de forma ampla, precisa cobrir todos os candidatos relevantes ou responder com confiança limitada.

## Testes executados

Comando:

```bash
python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_tiny_stock_local_db.py
python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v
```

Resultado:

- Sintaxe OK.
- 6 testes OK.

Testes cobrem:

- resolver Tiny v2 formata resposta segura com fonte/confiança/no-promise;
- broad brand pagina e soma duplicados;
- CLI Telegram/stock-only não envia WhatsApp;
- stock-only assisted model+size usa cache/snapshot em cenário testado;
- Tiny local DB é preferido antes de cache/live Tiny em cenário testado;
- fallback Onitsuka próximo quando tamanho exato indisponível em teste unitário.

## Smoke live/read-only feito hoje

Foram tentados dois comandos CLI seguros, sem envio WhatsApp:

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes cliente quer New Balance 9060 38, o que temos?' --stock-only --json-output
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes tem U9060WHT 38?' --stock-only --json-output
```

Resultado observado:

- Ambos excederam timeout local de 90–120s.
- Isso viola o SLA operacional desejado para atendimento assistido.
- A causa provável é que, quando não há positivo fresco no snapshot/cache, o código entra em confirmação live Tiny/fallback amplo. Para SKU/modelo amplo, isso pode paginar/expandir/consultar muitos candidatos antes de devolver resposta.

## Diagnóstico

O desenho conceitual está certo:

- resolve candidato no catálogo local;
- Tiny confirma estoque oficial;
- resposta inclui tamanho/SKU/fonte/confiança;
- não promete preço/entrega/reserva;
- não usa delta Shopify como estoque.

Mas há uma lacuna operacional:

- o caminho live/read-only real ainda pode ficar lento demais em perguntas amplas ou sem positivo no cache;
- os testes passam, mas não protegem suficientemente contra timeout no CLI real com dados atuais;
- `stock_by_sku` local ainda tem cobertura muito baixa (9 registros), então o caminho rápido depende de acertos recentes/eventos e não cobre bem perguntas amplas como `9060 38` ou `Onitsuka 38`.

## Regras para responder no WhatsApp enquanto a cobertura local é baixa

### Pode responder com alta confiança quando

- SKU/tamanho foi resolvido para variante canônica;
- Tiny live ou snapshot fresco do Tiny retornou `official_available > 0` no `LK | CONTROLE ESTOQUE`;
- resposta mostra produto, tamanho, SKU, fonte e horário/frescor quando disponível.

### Deve responder com confiança média/baixa quando

- há candidato local, mas só alguns SKUs foram lidos no Tiny;
- há zeros para parte dos candidatos, mas não cobertura ampla;
- modelo é amplo (`9060 38`, `Onitsuka 38`) e existem muitos produtos/variações possíveis.

### Não deve dizer “não tem” quando

- a busca Tiny falhou ou estourou timeout;
- só o primeiro match foi consultado;
- só Shopify inventory indicou zero;
- a varredura ampla não cobriu todos os candidatos relevantes.

Resposta segura nesses casos:

```text
Não achei saldo validado rápido no Tiny para esse modelo/tamanho.
Fonte tentada: catálogo local + Tiny / LK | CONTROLE ESTOQUE.
Confiança: baixa/média.
Não prometi disponibilidade; precisa validação manual/live antes de responder cliente.
```

## Próximos ajustes recomendados

1. **Hotfix de SLA no responder**
   - Impor timeout global real no `build_stock_only_answer`/`answer_assisted_sale`.
   - Se não resolver em poucos segundos, retornar resposta segura/interina.
   - Não deixar fallback amplo Tiny bloquear WhatsApp.

2. **Aumentar cobertura do Tiny local DB**
   - Criar refresh read-only por demanda para famílias/modelos mais perguntados: Onitsuka 38, New Balance 9060, 204L, Slides Nike.
   - Importante: refresh deve ler Tiny absoluto e gravar snapshot; nunca calcular delta por venda/cancelamento.

3. **Criar bateria de smokes reais com timeout**
   - `@Hermes cliente quer New Balance 9060 38, o que temos?`
   - `@Hermes você tem Onitsuka 38?`
   - `@Hermes tem U9060WHT 38?`
   - `@Hermes cliente quer Chinelo Slide Nike Mind 001 39.5, o que temos?`
   - Critério: resposta em até poucos segundos ou fallback seguro, nunca silêncio > 30s.

4. **Separar resposta rápida vs diagnóstico completo**
   - WhatsApp: resposta curta e segura.
   - Background/Brain: auditoria ampla do modelo/tamanho, dedupe Tiny, cobertura por SKU.

5. **Antes de restart do runtime WhatsApp**
   - rodar py_compile + unit tests + smokes CLI;
   - pedir aprovação explícita para restart do processo na porta 8787;
   - matar somente PID exato do responder;
   - validar POST local e smoke stock-only;
   - registrar receipt.

## Status final desta auditoria

- Documentação criada.
- Testes unitários atuais passam.
- Smoke real revelou gargalo/timeout; portanto ainda não está pronto para eu afirmar “responde 9060/Onitsuka rápido em produção”.
- Nenhum write externo foi feito.
- Nenhum WhatsApp foi enviado.
- Nenhum restart/rollout foi feito.
