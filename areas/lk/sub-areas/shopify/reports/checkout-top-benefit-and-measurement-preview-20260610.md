# Checkout LK — Preview: benefício no topo + mensuração

## Contexto

Lucas perguntou se faz sentido reforçar no topo do checkout:

- Parcelamento em até 10x sem juros
- Frete grátis acima de R$499

E pediu fazer a mensuração do microfunil (#9).

## Evidência já validada

QA mobile anterior no checkout real para carrinho de R$2.399,99 mostrou:

- `2 x ... sem juros` até `10 x ... sem juros`
- `11 x` e `12 x` têm copy problemática: aparecem como `com desconto`, mas o total fica maior que R$2.399,99

Conclusão: é seguro dizer `Parcele em até 10x sem juros`, mas não ampliar para 11x/12x e ainda é recomendado corrigir a copy de 11x/12x separadamente.

## Copy recomendada

### Para carrinho >= R$499

Linha 1:

```text
Parcele em até 10x sem juros
```

Linha 2:

```text
Frete grátis disponível após informar o CEP.
```

Racional: o cliente já é elegível; não precisa vender threshold, precisa reduzir ansiedade sobre cálculo do frete.

### Para carrinho < R$499

Linha 1:

```text
Parcele em até 10x sem juros
```

Linha 2, opção preferida:

```text
Frete grátis acima de R$499.
```

Linha 2, opção mais forte se o checkout extension conseguir ler subtotal:

```text
Faltam R$X para frete grátis.
```

Racional: só mostrar incentivo de threshold quando abaixo de R$499,99, conforme orientação de Lucas.

## Implementação proposta

Atualizar a extensão `lk-checkout-shipping-microcopy` já posicionada no Checkout Editor:

- Usar `useSubtotalAmount()` no checkout UI extension.
- Se `subtotal.amount >= 499`, exibir copy de frete disponível.
- Se `subtotal.amount < 499`, exibir incentivo de frete grátis.
- Manter o bloco no mesmo app block já posicionado no topo (`INFORMATION1`).

## Risco

- Baixo para copy de `10x sem juros`, pois foi observado no checkout real.
- Médio se houver produtos/condições onde parcelamento muda; ideal validar com 2 carrinhos: acima e abaixo de R$499.
- Ainda existe risco separado no seletor 11x/12x com copy contraditória; não deve ser misturado com esta melhoria.

## Rollback

- Reverter o texto da extensão para:

```text
Frete grátis acima de R$499
Calculado após informar o CEP.
```

- Deployar versão anterior/rollback do app ou remover o app block no Checkout Editor.

## Mensuração #9 — microfunil checkout

### Métricas desejadas

1. Checkout iniciado
2. Campo contato visível/preenchido
3. Etapa entrega visível/preenchida
4. Frete/método de entrega selecionado
5. Pagamento visível
6. Método de pagamento escolhido
7. Clique em `PAGAR AGORA`
8. Erro de pagamento/validação
9. Compra concluída

### Fontes possíveis

- Shopify analytics / checkout events
- Pixels existentes
- GA4/GTM, se ativo
- Web pixel extension, se houver
- Logs de eventos internos, se existentes

### Próximo passo seguro

Fazer auditoria read-only dos pixels/tracking atuais e produzir um mapa:

- evento existente
- fonte
- payload disponível
- lacuna
- proposta de implementação
- se exige write externo

Nenhum pixel/GA4/GTM/Shopify write deve ser feito sem aprovação explícita separada.
