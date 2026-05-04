# Sistema de Memória — Hermes Brain

Este documento define como o Hermes deve gerenciar memória para Lucas.

## Camadas de memória

```text
1. User profile / memory tool
   Preferências duráveis do Lucas e regras compactas que precisam aparecer em futuras sessões.

2. Session search
   Histórico de conversas. Usado para recuperar o que foi feito antes, sem poluir memória permanente.

3. Hermes Brain GitHub
   Fonte de verdade durável para negócios, decisões, processos, rotinas, skills e agentes.

4. memories/ no repo
   Memória executiva compacta por negócio e arquivos globais de decisões/lições/pendências.

5. empresa/ e areas/
   Camada estruturada e navegável para operação real.

6. Dados vivos
   Supabase, Shopify, APIs, email e crons. São fonte para métricas e fatos operacionais atuais.
```

## O que vai para cada camada

### Memory tool / user profile

Salvar apenas fatos duráveis que reduzem retrabalho em qualquer sessão:

- preferências do Lucas;
- correções de comportamento;
- regras globais de operação;
- convenções estáveis.

Não salvar:

- progresso de tarefa;
- logs de execução;
- detalhes temporários;
- dados que pertencem ao Brain.

### session_search

Usar quando Lucas disser:

- “seguir”;
- “como fizemos antes”;
- “lembra?”;
- referências a uma tarefa anterior.

### Hermes Brain GitHub

Salvar quando a informação é operacional, empresarial ou processual:

- decisões;
- lições;
- rotinas;
- skills;
- mapas de áreas;
- regras por agente;
- segurança;
- documentação de integração.

### memories/

Manter compacto. Não virar dumping ground.

Usar para:

- resumo executivo por negócio;
- decisões permanentes;
- lições importantes;
- pendências de alto nível.

### empresa/ e areas/

Usar para detalhamento estruturado:

- playbooks;
- rotinas;
- templates;
- processos;
- contextos por sub-área.

## Fluxo de atualização

Ao final de cada fase relevante:

1. Atualizar arquivo certo no Brain.
2. Atualizar skill se o procedimento mudou.
3. Atualizar memory tool se for preferência durável do Lucas.
4. Rodar `scripts/brain_health_check.py`.
5. Rodar scan de secrets.
6. Commit e push.
7. Resumir para Lucas.

## Releases e novidades Hermes

Toda fase de evolução do Brain deve considerar novidades do Hermes Agent:

1. Verificar release mais recente do `NousResearch/hermes-agent`.
2. Extrair novidades aplicáveis.
3. Classificar cada novidade:
   - aplicar agora;
   - adaptar ao Brain;
   - monitorar;
   - ignorar por enquanto.
4. Atualizar skills/rotinas/docs se for útil.

Release mais recente consultado durante esta fase:

- `v2026.4.30` / Hermes Agent v0.12.0.
- Destaques úteis: Autonomous Curator, self-improvement loop melhorado, `hermes skills update/check`, `hermes update --check`, novos providers, gateway plugins, media parity, TTS registry, secret redaction off by default.

## Como vou gerenciar na prática

- Brain = fonte de verdade.
- Memory tool = preferências do Lucas e regras globais compactas.
- Skills = procedimentos reutilizáveis.
- Releases Hermes = checklist recorrente antes de melhorar sistema.
- Health check = proteção contra regressões.

## Regra final

Se é importante para operar o negócio, vai para o Brain.
Se é preferência permanente do Lucas, vai para memory tool.
Se é procedimento repetível, vira skill.
Se é estado temporário, fica no resumo da sessão ou em pendências, não na memória permanente.
