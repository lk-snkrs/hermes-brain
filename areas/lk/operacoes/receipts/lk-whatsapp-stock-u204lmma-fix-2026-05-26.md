# Receipt — correção estoque WhatsApp LK / U204LMMA

Data: 2026-05-26  
Área: LK Operações / WhatsApp stock responder  
Status: corrigido e verificado

## Pedido limpo
Lucas reportou resposta errada no LK Team para:

> @Hermes manda estoque atualizado do que temos u204lmma

Resposta incorreta observada:

> Está zerado nos candidatos consultados. Se quiser que eu anote para o Júlio, me manda exatamente o produto/SKU/tamanho.

## Causa

1. O parser tratava `ATUALIZADO` como token SKU forte antes de `U204LMMA`.
2. Quando Tiny retornava o produto pai `U204LMMA`, o responder consultava estoque do pai. O pai pode aparecer zerado enquanto as variações/filhos têm estoque.
3. Para pergunta sem tamanho específico (“do que temos”), o correto é expandir o pai Tiny em variações e listar os tamanhos com saldo no `LK | CONTROLE ESTOQUE`.

## Correção aplicada

Arquivo alterado:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

Mudanças:

- `ATUALIZADO/ATUALIZADA/ATUALIZADOS/ATUALIZADAS` adicionados ao stoplist de tokens de comando.
- Para busca por SKU base sem tamanho, o responder agora chama `produto.obter`, expande variações e consulta estoque dos filhos.
- Resposta de grade agora explicita `Tamanho: X` em cada linha.
- Ordenação de tamanhos por numeração crescente na resposta.

Teste atualizado:

- `/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`

## Resultado verificado

Consulta testada localmente com Tiny read-only:

```text
@Hermes manda estoque atualizado do que temos u204lmma
```

Resposta corrigida:

```text
No LK | CONTROLE ESTOQUE, encontrei:
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 34 (`U204LMMA-1`): 2 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 35 (`U204LMMA-2`): 3 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 36 (`U204LMMA-3`): 4 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 37 (`U204LMMA-4`): 3 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 38 (`U204LMMA-5`): 1 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 39 (`U204LMMA-6`): 2 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 40 (`U204LMMA-7`): 4 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 41 (`U204LMMA-8`): 3 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 42 (`U204LMMA-9`): 1 par(es).
• Tênis New Balance 204L Mushroom Arid Stone Marrom — Tamanho: 43 (`U204LMMA-10`): 1 par(es).
```

## Verificações

- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py --live-tiny --verbose` → OK.
- `python3 -m py_compile` no responder e selftest → OK.
- Processo do responder reiniciado após alteração e escutando em `127.0.0.1:8787`.
- POST local para `/wacli` retornou `200 ok`.

## Limites

- Sem write em Shopify/Tiny.
- Sem contato externo.
- Sem promessa para cliente.
- Fonte de estoque: Tiny / `LK | CONTROLE ESTOQUE` read-only no momento do teste.
