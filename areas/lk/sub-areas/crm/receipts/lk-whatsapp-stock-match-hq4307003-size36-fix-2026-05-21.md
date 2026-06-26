# LK WhatsApp — Correção HQ4307003-36 tamanho 36

Data: 2026-05-21
Responsável: Hermes
Escopo: LK Sneakers / WhatsApp estoque

## Sintoma

Resposta incorreta observada no grupo:

> Não encontrei candidato no Tiny para HQ4307003-36 tamanho 36.

## Causa raiz

O usuário digitou um código compacto de estilo+cor+tamanho: `HQ4307003-36`.

No catálogo LK, a família correta usa hífen interno na cor e sufixo opaco/indexado por variação:

- Entrada humana: `HQ4307003-36`
- Prefixo de catálogo: `HQ4307-003`
- Tamanho: `36`
- SKU real resolvido: `HQ4307-003-3`

A lógica anterior tentava termos como `HQ4307003-36` / `HQ4307003`, que não retornavam no Tiny.

## Correção

Foi adicionada normalização de tokens SKU compactos antes da resolução local de variação:

1. preserva o token digitado como fallback;
2. remove o tamanho final quando ele vem anexado ao token;
3. normaliza padrões estilo+cor compactos (`HQ4307003`) para prefixo com hífen (`HQ4307-003`);
4. consulta o catálogo local (`lk_product_variants`) por prefixo + tamanho;
5. usa o SKU real `HQ4307-003-3` para a consulta Tiny.

## Validação

Resposta live após correção:

```text
Tem sim: 3 par(es) no LK | CONTROLE ESTOQUE.
Produto: Slide Nike Mind 001 Light Smoke Grey Cinza (`HQ4307-003-3`).
```

Testes executados:

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`: OK
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`: OK / silent
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py --live-tiny`: OK / silent
- `git diff --check` no Brain: OK

## Guardrail mantido

A resposta continua read-only, sem alterar Tiny/Shopify/Notion, sem reserva, sem compra e sem contato com fornecedor.
