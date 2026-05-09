# Template — Report Health Executivo

Use este template para transformar checks técnicos, rotinas e pendências em um relatório curto, verificável e útil para Lucas.

## Princípios

- Separar fato, interpretação e recomendação.
- Não dizer que algo “roda” sem checar execução real.
- Não imprimir segredos; mencionar apenas nomes de secrets quando necessário.
- Separar correções seguras de ações que exigem aprovação.
- Fechar com evidências.

---

# Health Executivo — [tema] — YYYY-MM-DD

## Status geral

- Estado: `verde | amarelo | vermelho`
- Escopo avaliado:
- Última verificação:
- Resultado em uma frase:

## Placar

- Brain/estrutura: __/100 — motivo
- Segurança/secrets: __/100 — motivo
- Rotinas/crons: __/100 — motivo
- Integrações: __/100 — motivo
- Negócios: __/100 — motivo
- Pendências/roadmap: __/100 — motivo

## Fatos verificados

- Fato:
  - Evidência:
  - Fonte/comando:

## Interpretações

- Interpretação:
  - Base:
  - Incerteza:

## Recomendações seguras

Ações que podem virar documentação, branch, PR ou análise read-only:

1. Ação:
   - Risco: L0/L1/L2
   - Arquivos prováveis:
   - Verificação:

## Aprovação Lucas necessária

Ações que não devem ser executadas sem aprovação explícita:

1. Ação:
   - Por que exige aprovação:
   - Plano de backup/rollback ou preview:

## Riscos

- Risco:
  - Impacto:
  - Mitigação:

## Não feito

- Item:
  - Motivo:
  - Como retomar:

## Próxima decisão

Minha recomendação:

- Próximo passo:
- Por quê:
- O que não será tocado:

## Evidências

- Health check:
- Secret scan:
- Git diff/PR/commit:
- Arquivos consultados:
- Comandos relevantes:

## Checklist de fechamento

- [ ] Dados não inventados.
- [ ] Secret scan limpo ou achados redigidos.
- [ ] Rotina documentada não foi confundida com cron ativo.
- [ ] Ações externas/produtivas não foram executadas.
- [ ] Próximo passo tem dono e risco claro.
