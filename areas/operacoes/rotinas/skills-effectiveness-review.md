# Rotina — Revisão de efetividade de skills

Status: ativa como rotina documental  
Owner: Hermes Geral / COO  
Cadência recomendada: mensal ou após erro repetido  
Writes externos: não

## Objetivo

Garantir que skills realmente mudam comportamento. Se Lucas corrigiu algo e a skill foi patchada, o mesmo erro não pode reaparecer como se nada tivesse acontecido.

## Perguntas da revisão

1. Qual erro/correção de Lucas gerou skill patch ou referência?
2. A skill certa foi carregada nos trabalhos seguintes?
3. O comportamento melhorou?
4. O erro se repetiu?
5. A skill está curta, acionável e atualizada?
6. Existe referência longa demais que deveria ser quebrada?
7. O aprendizado deveria estar em Brain/rotina em vez de skill?

## Escopo

Auditar principalmente skills de:

- Hermes Agent / gateway / cron / Telegram UX;
- Lucas Chief of Staff;
- Multiempresa routing;
- LK Growth;
- SPITI;
- Zipper;
- Mordomo;
- Brain governance.

## Saída

Salvar em:

`reports/governance/skills-effectiveness-review-YYYY-MM.md`

## Classificação por skill

- `efetiva`: evitou erro ou acelerou execução.
- `parcial`: contém regra certa, mas ainda exige correção frequente.
- `inchada`: informação demais, difícil de aplicar.
- `desatualizada`: regra conflita com runtime atual.
- `errada`: induz ação ruim ou insegura.

## Template

```md
# Revisão de efetividade de skills

Período:
Owner: Hermes Geral / COO

## Resumo

Skills revisadas:
Efetivas:
Parciais:
Inchadas:
Desatualizadas:
Erradas:

## Achados por skill

### Skill
Status:
Correção/feedback relacionado:
Evidência de uso:
Erro repetido?: sim/não
Patch necessário:

## Próximas ações

1.
2.
3.
```

## Gatilho imediato

Se Lucas corrigir o mesmo erro duas vezes após uma skill patchada, abrir revisão da skill na mesma sessão.
