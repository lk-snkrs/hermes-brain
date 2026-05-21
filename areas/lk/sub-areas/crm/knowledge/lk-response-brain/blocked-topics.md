# LK Response Brain — tópicos bloqueados

Atualizado: 2026-05-21
Fonte: decisão Lucas + arquitetura Crisp/Hugo Larissa.

## Regra principal

O bot nunca deve responder diretamente sobre:

1. Produto sob encomenda.
2. Status de pedido.
3. Entrega, rastreamento, transportadora ou prazo pós-compra.

Esses casos devem transbordar para Larissa/humano.

## Exemplos de gatilhos

### Sob encomenda

- "consegue encomendar?"
- "faz sob encomenda?"
- "não tem meu tamanho, dá pra pedir?"
- "tem previsão de chegar?"
- "consegue trazer esse modelo?"

Ação: handoff Larissa.

### Status de pedido

- "cadê meu pedido?"
- "qual status do meu pedido?"
- "meu pedido foi aprovado?"
- "pedido 123"

Ação: handoff Larissa.

### Entrega/rastreamento

- "quando chega?"
- "qual o rastreio?"
- "qual transportadora?"
- "prazo de entrega?"
- "meu pedido atrasou"

Ação: handoff Larissa.

## Resposta do bot para transbordo

Preferência: não inventar informação. Usar uma frase curta de encaminhamento, se o fluxo exigir mensagem ao cliente:

```text
Vou chamar uma atendente para te ajudar certinho com isso.
```

Resumo interno para Larissa deve conter categoria, última mensagem e contexto mínimo.
