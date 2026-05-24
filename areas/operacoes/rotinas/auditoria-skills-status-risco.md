# Rotina — Auditoria de skills, status e risco

Status: ativo como rotina de governança  
Criada: 2026-05-20  
Escopo: skills Hermes Brain e skills operacionais que afetam LK, Zipper, SPITI, Operações e automações.

## Objetivo

Manter skills como capacidades confiáveis, não documentação obsoleta. Cada skill relevante precisa ter dono lógico, status, risco, última revisão e sinal de quando deve ser atualizada.

## Frequência recomendada

- Mensal para todas as skills relevantes.
- Imediata quando uma skill falhar, ficar incompleta ou for corrigida por Lucas.
- Antes de ativar cron/agente que dependa da skill.

## Campos mínimos por skill crítica

Registrar no índice ou report de auditoria:

- nome/caminho da skill;
- domínio/empresa;
- dono lógico: Hermes Central, LK, Zipper, SPITI, Operações etc.;
- status: ativo, experimental, legado, pausado, precisa revisão;
- risco: baixo, médio, alto;
- última revisão;
- última execução/verificação conhecida;
- comandos/ferramentas exigidas;
- falhas conhecidas;
- próximo passo.

## Checklist

1. A skill ainda representa o fluxo real?
2. Ela referencia paths, comandos, APIs ou ferramentas existentes?
3. Ela contém guardrails de writes externos, secrets e aprovação?
4. Ela diz como verificar conclusão?
5. Ela tem owner/status/risco claros no índice ou report?
6. Ela deve virar rotina, cron, template ou ser arquivada?

## Saída esperada

Criar report curado em `reports/governance/` quando a auditoria for ampla, ou patchar diretamente a skill quando o problema for pontual.

Formato sugerido:

```md
# Auditoria de skills — YYYY-MM-DD

## Resumo
- skills avaliadas:
- ativas:
- precisam revisão:
- legado/arquivar:

## Achados
- ...

## Correções aplicadas
- ...

## Próximos passos
- ...
```

## Regra de manutenção

Se uma skill estiver errada/incompleta durante o uso, corrigir imediatamente com `skill_manage(action='patch')` ou atualizar o arquivo no Brain correspondente quando for skill versionada no repositório.
