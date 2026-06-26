# Correção necessária — roteamento do piloto Shopify auto-ordenação LK

Data: 2026-05-26
Origem: Telegram Lucas

## Correção do usuário

Lucas corrigiu que a aprovação explícita dele deve permitir avançar para Shopify write neste caso. O bloqueio atual não é falta de autorização de negócio; é classificação/roteamento do runtime como tarefa genérica read-only.

## Problema observado

O Task Router classificou a solicitação como `pesquisa/pergunta/relatorio sem dono claro` / Hermes Geral, permitindo apenas pesquisa, síntese e documentação local.

Isso é incorreto para este caso, porque o assunto é claramente LK Growth / Shopify Collections e já possui:

- PRD/dry-run;
- approval packet;
- escopo piloto fechado;
- aprovação explícita e reiterada de Lucas para Shopify write;
- rollback planejado;
- requisito de snapshot + readback;
- proibição explícita de cron.

## Correção esperada

Roteamento futuro deve reconhecer pedidos de auto-ordenação de coleções LK / `collectionReorderProducts` como:

- contexto: LK Growth / Shopify;
- executor: LK Shopify/Growth write-enabled, quando houver aprovação explícita atual;
- task_type: Shopify collection merchandising write;
- allow: executar snapshot/readback e Shopify mutation dentro do escopo aprovado;
- block: cron, produtos, preço, estoque, tema, SEO, tags, checkout, campanha ou comunicação fora do escopo.

## Escopo autorizado para execução write-enabled

- Aplicar somente nas 10 coleções piloto aprovadas.
- Usar Tiny/SQLite como fonte primária para produtos esgotados.
- Mover produtos esgotados para o final.
- Gerar snapshot pré-write imediato.
- Executar `collectionReorderProducts`.
- Pollar jobs assíncronos.
- Fazer readback por coleção.
- Gerar receipt final.
- Não criar cron.

## Status deste arquivo

Documento local de correção/handoff. Nenhum Shopify write foi executado por este arquivo.
