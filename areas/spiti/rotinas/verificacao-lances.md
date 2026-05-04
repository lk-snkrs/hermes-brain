# Rotina — Verificação de lances SPITI

## O que faz

Define o procedimento seguro para responder sobre lance, lote, total de lances ou status de pregão.

## Fonte de verdade

1. Email: fonte de verdade para total de lances.
2. Supabase `rmdugdkantdydivgnimb`, tabela `spiti_lotes`: base operacional interna.
3. Site: usar com cautela; pode mostrar apenas destaques.
4. Meta tag: nunca usar como lance atual.

## Loop Hermes

```text
pergunta → identificar fonte necessária → consultar fonte correta → informar fonte → responder com ressalva se necessário
```

## Verificação obrigatória

- Fonte consultada identificada.
- Tipo de lance informado quando houver: A automático, O normal.
- Se não houver confirmação, dizer que não há confirmação.

## Nunca

- Nunca usar `product:price:amount` como lance atual.
- Nunca afirmar total de lances a partir do site.
- Nunca confundir SPITI com Zipper Vendas.
