# LK stock fast-answer cache — 2026-05-26

## Contexto
Lucas reportou latência de ~180s para pergunta de disponibilidade ampla (`New Balance 9060 tamanho 38`). Fonte de verdade permanece Tiny / `LK | CONTROLE ESTOQUE`; Shopify/base local só podem resolver catálogo/variante, não saldo oficial.

## Implementado localmente
- Adicionado cache local SQLite em `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/stock_cache.sqlite`.
- Cache guarda SKU, produto, tamanho, saldo oficial Tiny, fonte, confiança e timestamp.
- TTL curto: 10 minutos, para resposta operacional rápida sem promessa comercial.
- Resolver Tiny passa a popular o cache sempre que consulta estoque oficial.
- Fluxo assistido agora:
  1. resolve candidatos SKU/tamanho na base local (`lk_product_variants` + `lk_products`);
  2. consulta cache Tiny fresco;
  3. se cache faltar, confirma poucos SKUs no Tiny por SKU, com orçamento curto, sem varrer busca ampla;
  4. só então cai na busca ampla Tiny antiga.
- `--stock-only` agora aceita perguntas assistidas de disponibilidade (`cliente quer ... o que temos?`) sem criar cards/WhatsApp sends.
- Termos de busca preservam modelos numéricos de 4 dígitos, ex. `9060`.

## Evidência
- `python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v` → 5/5 OK.
- Primeira consulta live `@Hermes cliente quer New Balance 9060 38, o que temos?`: 18.4s; confirmou Tiny por SKU e populou cache.
- Segunda consulta live igual: 0.186s; respondeu via cache local Tiny.
- Após aprovação de Lucas, responder LK foi recarregado na porta 8787 com PID novo `239405`; processo está rodando.

## Guardrails
- Sem writes em Tiny/Shopify.
- Sem envio manual de WhatsApp durante teste CLI; somente reload do responder aprovado.
- Resposta mantém: uso interno, não reserva, não altera estoque, não promete entrega/preço.
- Cache local é aceleração operacional, não substitui Tiny. Para promessa a cliente, validar conforme política.

## Rollback
- Encerrar o PID novo e subir novamente o comando anterior com a versão de script anterior se necessário.
- Se houver comportamento incorreto em grupo, parar o responder primeiro para evitar novas respostas automáticas.
