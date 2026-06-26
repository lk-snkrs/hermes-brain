# Instrução curta — Mesa Júlio LK Compras

## Correção Lucas — 2026-05-15

Júlio **não preenche valor**.

1. Hermes identifica produto/modelo/tamanho e busca/valida preço do tamanho correto em fonte confiável/autenticada.
2. Hermes calcula quando o preço exato existe: custo landed = (preço USD do tamanho correto + custo trazer USD) × (dólar × 1,05); venda ideal = custo landed × 2.
3. Júlio usa o card para decisão/execução operacional: comprar, pular, acompanhar, registrar compra/resposta.
4. Se Hermes não conseguir validar preço exato do tamanho, o card fica como `Hermes precisa validar preço por tamanho`, não como tarefa de preenchimento do Júlio.

## Uso da mesa

1. Abrir cards `Aguardando Aprovação`.
2. Conferir foto, modelo, tamanho e disponibilidade real.
3. Nunca usar preço genérico do produto como custo.
4. Não pedir para Júlio preencher preço USD.
5. Compra, contato e pagamento continuam humanos; cálculo e validação de preço por tamanho são responsabilidade do Hermes/fonte integrada.
