# Template — Relatório Interno SPITI com Matriz de Evidência

## Uso

Usar para relatórios internos de pregão, pós-leilão, divergência de lances ou acompanhamento executivo. O objetivo é separar dado confirmado de hipótese e impedir que site/meta tag virem “verdade” por acidente.

Regra: se a fonte correta não foi consultada, escrever “não confirmado”.

## Cabeçalho

- Data/hora do relatório:
- Leilão/pregão:
- Responsável pela coleta:
- Fontes consultadas:
- Fontes não consultadas:
- Nível de confiança geral: alto / médio / baixo

## Resumo executivo

```text
Resumo em 3–5 bullets, apenas com dados confirmados.
Se houver lacuna crítica, abrir com a lacuna.
```

## Matriz de evidência por lote

| Lote | Obra/artista | Base/estimativa | Lance atual confirmado | Total de lances confirmado | Tipo de lance | Fonte primária | Fonte secundária | Divergência? | Confiança | Ação recomendada |
|---|---|---:|---:|---:|---|---|---|---|---|---|
|  |  |  |  |  | A/O/n.d. | email/Supabase/site/outro |  | sim/não | alta/média/baixa |  |

Legenda:

- `A`: lance automático.
- `O`: lance normal.
- `n.d.`: não disponível/não confirmado.

## Hierarquia de fontes

1. Email: fonte de verdade para total de lances.
2. Supabase SPITI/CRM: base operacional interna, confirmar freshness.
3. Site LeilõesBR: útil para visualização/destaques, não para total final sem validação.
4. Meta tag: nunca usar como lance atual; pode representar preço base.

## Divergências e riscos

| Item | Divergência | Fontes em conflito | Impacto | Próximo passo |
|---|---|---|---|---|
|  |  |  | baixo/médio/alto |  |

Exemplos de risco:

- email não consultado;
- site mostra menos lances que email;
- Supabase desatualizado;
- monitor de lances não confirmado;
- n8n sem workflow ativo;
- scraping interpretou meta tag como preço atual.

## Próximas ações internas

| Ação | Responsável | Precisa aprovação? | Prazo | Observação |
|---|---|---|---|---|
|  |  | sim/não |  |  |

## Mensagem externa proposta, se necessária

Não enviar sem aprovação do Lucas.

```text
[Rascunho]
```

## Checklist antes de fechar

- [ ] Email consultado quando o assunto é total de lances.
- [ ] Tipo de lance informado quando disponível.
- [ ] Meta tag não foi usada como lance atual.
- [ ] Toda afirmação tem fonte.
- [ ] Lacunas foram declaradas como lacunas.
- [ ] Mensagem externa, se existir, ficou como rascunho pendente de aprovação.
