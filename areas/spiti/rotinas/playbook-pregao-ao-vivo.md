# Playbook — SPITI Pregão ao Vivo

## Objetivo

Responder e operar durante pregão SPITI com máxima precisão, preservando a regra central: silêncio é melhor que dado errado.

## Quando usar

- Perguntas sobre lance atual, total de lances, lote, status de pregão ou relatório parcial.
- Monitoramento de alertas de lance.
- Situações em que site, email e banco podem divergir.

## Fontes e hierarquia

1. Email: fonte de verdade para total de lances.
2. Supabase/SPITI CRM `rmdugdkantdydivgnimb`, tabela operacional de lotes quando aplicável.
3. Monitor interno/documentado, se ativo e verificado.
4. Site: usar apenas com ressalva; pode mostrar destaques.
5. Meta tag: nunca usar como lance atual.

## Loop

```text
pergunta/lote → identificar dado necessário → consultar fonte correta → comparar divergência → responder com fonte e ressalva → registrar anomalia
```

## Checklist antes de responder

- [ ] Lote identificado sem ambiguidade.
- [ ] Tipo de dado identificado: total de lances, lance atual, status, destaque, preço base, relatório.
- [ ] Fonte correta consultada.
- [ ] Divergência marcada, se existir.
- [ ] Resposta informa a fonte ou diz que não há confirmação.
- [ ] Nenhum dado Zipper Vendas foi misturado com SPITI.

## Resposta padrão segura

```text
Fonte consultada: ...
Lote: ...
Dado confirmado: ...
Ressalva: ...
Se precisar, faço nova verificação antes de qualquer comunicação externa.
```

## Quando não responder com número

Não responder com número quando:

- só houver meta tag/preço base;
- o site mostrar destaque sem total completo;
- email ainda não confirmou total;
- o lote estiver ambíguo;
- houver conflito entre fontes sem resolução.

Nesses casos, responder:

```text
Ainda não tenho confirmação segura desse número. Pela regra SPITI, prefiro não afirmar até validar na fonte correta.
```

## Ações externas

Qualquer mensagem externa para comprador, vendedor, equipe externa ou público exige aprovação Lucas.
